"""Aggregate development PR labels for a dev-to-main release."""

import json
import os
import re
import subprocess
from pathlib import Path

REPO = os.environ.get("REPO", "BAMresearch/bam-masterdata")
PR_NUMBER = os.environ.get("PR_NUMBER")
DRY_RUN = os.environ.get("DRY_RUN", "true").lower() == "true"

SEMVER_ORDER = ("none", "patch", "minor", "major")

VERSION_PATTERN = re.compile(r"^v?(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")

RELEASE_NOTES_PATH = Path(os.environ.get("RELEASE_NOTES_PATH", "release-notes.md"))

RELEASE_COMMENT_MARKER = "<!-- bam-masterdata-release-notes -->"
GENERATED_START = "<!-- release-notes:start -->"
GENERATED_END = "<!-- release-notes:end -->"

MAINTAINER_SECTION = "\n## Maintainer notes\n\nAdd any release-specific notes here.\n"


def parse_version(tag):
    """Parse a stable SemVer tag into major, minor and patch."""
    match = VERSION_PATTERN.fullmatch(tag)

    if not match:
        raise ValueError(f"Invalid stable release version: {tag!r}")

    return tuple(int(value) for value in match.groups())


def get_latest_release_version():
    """Read the latest published stable release from GitHub."""
    release = gh(f"repos/{REPO}/releases/latest")
    tag = release["tag_name"]

    parse_version(tag)

    return tag


def suggest_next_version(current_version, impact):
    """Suggest the next release version, respecting the 0.x policy."""
    major, minor, patch = parse_version(current_version)

    if impact not in SEMVER_ORDER:
        raise ValueError(f"Unknown SemVer impact: {impact}")

    if impact == "none":
        return None

    if impact == "patch":
        patch += 1

    elif impact == "minor":
        minor += 1
        patch = 0

    elif impact == "major":
        if major == 0:
            minor += 1
        else:
            major += 1
            minor = 0

        patch = 0

    return f"{major}.{minor}.{patch}"


def gh(*args):
    """Call the GitHub API and return JSON."""
    result = subprocess.check_output(
        ["gh", "api", *args],
        text=True,
    )
    return json.loads(result)


def gh_pages(endpoint):
    """Retrieve paginated GitHub Compare API results."""
    pages = []
    page_number = 1

    separator = "&" if "?" in endpoint else "?"

    while True:
        url = f"{endpoint}{separator}page={page_number}"
        data = gh(url)

        pages.append(data)

        if len(data.get("commits", [])) < 100:
            break

        page_number += 1

    return pages


def aggregate_labels(prs):
    """Calculate release labels and detect missing SemVer labels."""
    labels = set()
    problems = []

    for pr in prs:
        names = {label["name"] for label in pr["labels"]}

        semver = sorted(name for name in names if name.startswith("semver:"))

        if len(semver) != 1 or semver[0].split(":")[-1] not in SEMVER_ORDER:
            problems.append(f"#{pr['number']}: invalid SemVer labels {semver}")
            continue

        labels.update(name for name in names if name.startswith(("type:", "area:")))

        labels.add(semver[0])

    if problems:
        return [], problems

    impacts = [name.split(":")[-1] for name in labels if name.startswith("semver:")]

    if impacts:
        highest = max(impacts, key=SEMVER_ORDER.index)
        labels = {name for name in labels if not name.startswith("semver:")}
        labels.add(f"semver:{highest}")

    return sorted(labels), []


def get_release_pr():
    """Validate the release PR when running from GitHub Actions."""
    if not PR_NUMBER:
        return None

    pr = gh(f"repos/{REPO}/pulls/{PR_NUMBER}")

    if (
        pr["base"]["ref"] != "main"
        or pr["head"]["ref"] != "dev"
        or pr["head"]["repo"]["full_name"] != REPO
    ):
        raise ValueError("Expected a release PR from dev to main")

    return pr


def get_development_prs():
    """Find merged development PRs in main...dev."""
    pages = gh_pages(f"repos/{REPO}/compare/main...dev?per_page=100")

    commits = [commit for page in pages for commit in page.get("commits", [])]

    found = {}
    unmatched = []

    for commit in commits:
        sha = commit["sha"]

        associated = gh(f"repos/{REPO}/commits/{sha}/pulls?per_page=100")

        matching = [
            pr
            for pr in associated
            if pr.get("merged_at") and pr["base"]["ref"] == "dev"
        ]

        if not matching:
            unmatched.append(sha)
            continue

        for pr in matching:
            found[pr["number"]] = pr

    return [found[n] for n in sorted(found)], unmatched


def print_report(prs, labels, problems, unmatched):
    """Display the proposed release classification."""
    print("\nRelease analysis: main...dev")
    print("=" * 45)

    for pr in prs:
        names = sorted(label["name"] for label in pr["labels"])
        print(f"#{pr['number']}: {pr['title']}")
        print(f"  Labels: {', '.join(names) or '(none)'}")

    print("\nAggregated labels:")
    for label in labels:
        print(f"  {label}")

    if problems:
        print("\nPRs requiring classification:")
        for problem in problems:
            print(f"  {problem}")

    if unmatched:
        print("\nCommits without an associated merged development PR:")
        for sha in unmatched:
            print(f"  {sha[:12]}")


def apply_labels(release_pr, labels):
    """Update release labels while keeping unrelated labels."""
    number = release_pr["number"]

    existing = {label["name"] for label in release_pr["labels"]}

    # Remove obsolete release classifications.
    managed_prefixes = ("type:", "area:", "semver:")

    obsolete = sorted(
        name
        for name in existing
        if name.startswith(managed_prefixes) and name not in labels
    )

    additions = sorted(set(labels) - existing)

    for label in obsolete:
        subprocess.run(
            [
                "gh",
                "api",
                "--method",
                "DELETE",
                f"repos/{REPO}/issues/{number}/labels/{label}",
            ],
            check=True,
        )

    if additions:
        subprocess.run(
            [
                "gh",
                "api",
                "--method",
                "POST",
                f"repos/{REPO}/issues/{number}/labels",
                "--input",
                "-",
            ],
            input=json.dumps({"labels": additions}),
            text=True,
            check=True,
        )

    print(f"\nUpdated release PR #{number}")


def validate_release(problems, unmatched):
    """Validate release classification and report unmatched commits."""
    if problems:
        raise SystemExit(
            "Release classification is incomplete. "
            "Some PRs have missing or invalid SemVer labels."
        )

    if unmatched:
        print(
            "\nWARNING: Some commits are not associated with a merged development PR."
        )
        print("Review these commits manually before approving the release.")


RELEASE_CATEGORIES = (
    ("Features", "type:feature"),
    ("Enhancements", "type:enhancement"),
    ("Bug Fixes", "type:bug"),
    ("Documentation", "type:documentation"),
    ("Maintenance", "type:maintenance"),
    ("Questions", "type:question"),
)


def markdown_text(value):
    """Normalize untrusted text for one Markdown line."""
    return (
        str(value)
        .replace("\\", "\\\\")
        .replace("[", "\\[")
        .replace("]", "\\]")
        .replace("\r", " ")
        .replace("\n", " ")
        .strip()
    )


def get_release_impact(labels):
    """Return the aggregated SemVer impact."""
    matches = [
        label.removeprefix("semver:") for label in labels if label.startswith("semver:")
    ]

    if len(matches) != 1 or matches[0] not in SEMVER_ORDER:
        raise ValueError(f"Expected exactly one valid SemVer label: {matches}")

    return matches[0]


def render_release_notes(
    prs,
    labels,
    unmatched=(),
    current_version=None,
    next_version=None,
):
    """Create categorized Markdown notes from original development PRs."""
    impact = get_release_impact(labels)

    lines = [
        "# Release Notes",
        "",
    ]

    if current_version is not None:
        lines.append(f"**Current release:** `{current_version}`")

    if next_version is not None:
        lines.append(f"**Suggested release:** `v{next_version}`")
    elif current_version is not None:
        lines.append("**Suggested release:** No version bump")

    lines.extend(
        [
            f"**Suggested SemVer impact:** `{impact}`",
            "",
        ]
    )

    used = set()

    for title, label in RELEASE_CATEGORIES:
        matching = [
            pr for pr in prs if label in {item["name"] for item in pr["labels"]}
        ]

        if not matching:
            continue

        lines.extend([f"## {title}", ""])

        for pr in sorted(matching, key=lambda item: item["number"]):
            number = pr["number"]
            author = (pr.get("user") or {}).get("login") or "unknown"
            title_text = markdown_text(pr["title"])

            url = f"https://github.com/{REPO}/pull/{number}"

            lines.append(f"- [#{number}]({url}) — {title_text} (@{author})")
            used.add(number)

        lines.append("")

    uncategorized = [pr for pr in prs if pr["number"] not in used]

    if uncategorized:
        lines.extend(["## Other Changes", ""])

        for pr in sorted(uncategorized, key=lambda item: item["number"]):
            number = pr["number"]
            author = (pr.get("user") or {}).get("login") or "unknown"
            title_text = markdown_text(pr["title"])
            url = f"https://github.com/{REPO}/pull/{number}"

            lines.append(f"- [#{number}]({url}) — {title_text} (@{author})")

        lines.append("")

    if unmatched:
        lines.extend(
            [
                "## Needs Manual Review",
                "",
                "The following commits could not be associated with "
                "a merged development PR:",
                "",
            ]
        )

        for sha in unmatched:
            lines.append(f"- [`{sha[:12]}`](https://github.com/{REPO}/commit/{sha})")

        lines.extend(
            [
                "",
                "Review these commits before approving the release.",
                "",
            ]
        )

    return "\n".join(lines).rstrip() + "\n"


def write_release_notes(
    prs,
    labels,
    unmatched=(),
    current_version=None,
    next_version=None,
):
    """Write the generated notes to a local Markdown file."""
    content = render_release_notes(
        prs,
        labels,
        unmatched,
        current_version=current_version,
        next_version=next_version,
    )
    RELEASE_NOTES_PATH.parent.mkdir(parents=True, exist_ok=True)
    RELEASE_NOTES_PATH.write_text(content, encoding="utf-8")

    print(f"\nRelease notes written to: {RELEASE_NOTES_PATH}")


def render_release_pr_body(notes, existing_body=""):
    """Render release notes while preserving manual content."""

    generated = f"{GENERATED_START}\n{notes.rstrip()}\n{GENERATED_END}"

    # Preserve everything following the generated section.
    if GENERATED_END in existing_body:
        manual_content = existing_body.split(GENERATED_END, 1)[1]
    else:
        # First run: discard GitHub's commit-generated description
        # and initialize a dedicated editable section.
        manual_content = MAINTAINER_SECTION

    return generated + manual_content


def update_release_pr(release_pr, notes, next_version):
    """Update the release PR title and description."""
    number = release_pr["number"]

    title = (
        f"Release v{next_version}"
        if next_version
        else "Release preparation (no version bump)"
    )

    body = render_release_pr_body(
        notes,
        release_pr.get("body") or "",
    )

    if release_pr.get("title") == title and release_pr.get("body") == body:
        print("\nRelease PR title and description already up to date.")
        return

    subprocess.run(
        [
            "gh",
            "api",
            "--method",
            "PATCH",
            f"repos/{REPO}/pulls/{number}",
            "--input",
            "-",
        ],
        input=json.dumps(
            {
                "title": title,
                "body": body,
            }
        ),
        text=True,
        check=True,
        capture_output=True,
    )

    print(f"\nUpdated release PR #{number}: {title}")


def remove_legacy_release_comment(pr_number):
    """Remove the comment created by the previous release workflow."""
    endpoint = f"repos/{REPO}/issues/{pr_number}/comments"
    page = 1
    legacy_ids = []

    while True:
        comments = gh(f"{endpoint}?per_page=100&page={page}")

        for comment in comments:
            if comment.get("user", {}).get(
                "type"
            ) == "Bot" and RELEASE_COMMENT_MARKER in comment.get("body", ""):
                legacy_ids.append(comment["id"])

        if len(comments) < 100:
            break

        page += 1

    for comment_id in legacy_ids:
        subprocess.run(
            [
                "gh",
                "api",
                "--method",
                "DELETE",
                f"repos/{REPO}/issues/comments/{comment_id}",
            ],
            check=True,
            capture_output=True,
        )

    if legacy_ids:
        print(f"\nRemoved {len(legacy_ids)} legacy release comment(s).")


def main():
    release_pr = get_release_pr()
    prs, unmatched = get_development_prs()

    labels, problems = aggregate_labels(prs)

    print_report(prs, labels, problems, unmatched)

    if not prs:
        raise SystemExit("No merged development PRs found.")

    validate_release(problems, unmatched)

    # Determine the next version from the latest published release.
    current_version = get_latest_release_version()
    impact = get_release_impact(labels)

    next_version = suggest_next_version(current_version, impact)

    print(f"\nCurrent release: {current_version}")
    print(f"Suggested SemVer impact: {impact}")
    print(
        "Suggested next version: "
        f"{f'v{next_version}' if next_version else 'No version bump'}"
    )

    # Generate notes only after validation succeeds.
    write_release_notes(
        prs,
        labels,
        unmatched,
        current_version=current_version,
        next_version=next_version,
    )

    if not release_pr:
        print("\nNo release PR specified. Analysis only.")
        return

    if DRY_RUN:
        print("\nDRY RUN: no GitHub metadata modified.")
        return

    apply_labels(release_pr, labels)

    notes = RELEASE_NOTES_PATH.read_text(encoding="utf-8")

    update_release_pr(release_pr, notes, next_version)
    remove_legacy_release_comment(release_pr["number"])


if __name__ == "__main__":
    main()
