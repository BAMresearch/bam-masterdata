"""Synchronize labels from associated GitHub issues to pull requests."""

import json
import os
import re
import subprocess

ISSUE_REF_PATTERN = re.compile(
    r"\b(?:refs?|closes?|fixes?|resolves?)\s+#(\d+)\b",
    re.IGNORECASE,
)

BRANCH_PATTERN = re.compile(r"^(\d+)[-_]")

# Labels allowed on pull requests.
PR_LABEL_PREFIXES = ("type:", "area:", "semver:")

# Categories that allow only one label.
SINGLE_VALUE_PREFIXES = ("type:", "semver:")


def gh(*args):
    """Execute a GitHub API request using GitHub CLI."""
    return json.loads(
        subprocess.check_output(
            ["gh", "api", *args],
            text=True,
        )
    )


def issue_numbers_from_pr(pr, linked_numbers=()):
    """Identify issues associated with a pull request."""
    numbers = set(linked_numbers)

    # Explicit references in the PR description.
    body = pr.get("body") or ""

    numbers.update(int(number) for number in ISSUE_REF_PATTERN.findall(body))

    # Branches created with an issue-number prefix.
    branch = pr["head"]["ref"]
    match = BRANCH_PATTERN.match(branch)

    if match:
        numbers.add(int(match.group(1)))

    return sorted(numbers)


def labels_to_copy(existing, issue_labels):
    """Return eligible missing labels without replacing PR classifications."""
    additions = set()

    for label in issue_labels:
        # Only copy labels relevant to pull requests.
        if not label.startswith(PR_LABEL_PREFIXES):
            continue

        if label in existing or label in additions:
            continue

        # Avoid multiple type or SemVer labels.
        if any(
            label.startswith(prefix)
            and any(name.startswith(prefix) for name in existing | additions)
            for prefix in SINGLE_VALUE_PREFIXES
        ):
            continue

        additions.add(label)

    return sorted(additions)


def main():
    repo = os.environ["REPO"]
    owner, name = repo.split("/", 1)
    pr_number = int(os.environ["PR_NUMBER"])

    pr = gh(f"repos/{repo}/pulls/{pr_number}")

    # GitHub's native closing-issue relationships.
    query = """
    query($owner: String!, $name: String!, $number: Int!) {
      repository(owner: $owner, name: $name) {
        pullRequest(number: $number) {
          closingIssuesReferences(first: 100) {
            nodes {
              number
            }
          }
        }
      }
    }
    """

    response = gh(
        "graphql",
        "-f",
        f"query={query}",
        "-f",
        f"owner={owner}",
        "-f",
        f"name={name}",
        "-F",
        f"number={pr_number}",
    )

    linked = response["data"]["repository"]["pullRequest"]["closingIssuesReferences"]

    issue_numbers = issue_numbers_from_pr(
        pr,
        [item["number"] for item in linked["nodes"]],
    )

    if not issue_numbers:
        print("No associated issue found.")
        return

    existing = {label["name"] for label in pr["labels"]}

    candidates = []

    for issue_number in issue_numbers:
        try:
            issue = gh(f"repos/{repo}/issues/{issue_number}")
        except subprocess.CalledProcessError:
            print(f"Skipping unavailable issue #{issue_number}")
            continue

        # Ignore references to other pull requests.
        if "pull_request" in issue:
            continue

        candidates.extend(label["name"] for label in issue["labels"])

    additions = labels_to_copy(existing, candidates)

    if os.environ.get("DRY_RUN", "false").lower() == "true":
        print(f"DRY RUN - Existing PR labels: {sorted(existing)}")
        print(f"DRY RUN - Issue labels: {sorted(set(candidates))}")
        print(f"DRY RUN - Labels to copy: {additions}")
        return

    if not additions:
        print("No new labels to copy.")
        return

    subprocess.run(
        [
            "gh",
            "api",
            "--method",
            "POST",
            f"repos/{repo}/issues/{pr_number}/labels",
            "--input",
            "-",
        ],
        input=json.dumps({"labels": additions}),
        text=True,
        check=True,
    )

    print(f"Copied labels: {', '.join(additions)}")


if __name__ == "__main__":
    main()
