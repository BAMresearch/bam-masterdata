"""Aggregate development PR labels for a dev-to-main release."""

import json
import os
import subprocess
from collections import defaultdict

REPO = os.environ.get("REPO", "BAMresearch/bam-masterdata")
PR_NUMBER = os.environ.get("PR_NUMBER")
DRY_RUN = os.environ.get("DRY_RUN", "true").lower() == "true"

SEMVER_ORDER = ("none", "patch", "minor", "major")


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


def main():
    release_pr = get_release_pr()
    prs, unmatched = get_development_prs()

    labels, problems = aggregate_labels(prs)

    print_report(prs, labels, problems, unmatched)

    if not prs:
        raise SystemExit("No merged development PRs found.")

    validate_release(problems, unmatched)

    if not release_pr:
        print("\nNo release PR specified. Analysis only.")
        return

    if DRY_RUN:
        print("\nDRY RUN: no GitHub labels modified.")
        return

    apply_labels(release_pr, labels)


if __name__ == "__main__":
    main()
