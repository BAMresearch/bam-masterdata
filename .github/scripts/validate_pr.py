"""Validate labels and issue associations on development and release PRs."""

import json
import os
import re
import subprocess
import sys

REPO = os.environ["REPO"]
PR_NUMBER = int(os.environ["PR_NUMBER"])

VALID_TYPES = {
    "type:bug",
    "type:feature",
    "type:enhancement",
    "type:documentation",
    "type:maintenance",
    "type:question",
}

VALID_SEMVER = {
    "semver:major",
    "semver:minor",
    "semver:patch",
    "semver:none",
}

ISSUE_PATTERN = re.compile(
    r"\b(?:refs?|closes?|fixes?|resolves?)\s+#(\d+)\b",
    re.IGNORECASE,
)

BRANCH_PATTERN = re.compile(r"^(\d+)[-_]")

ISSUE_EXCEPTION_LABEL = "no-issue-required"


def gh(*args):
    """Retrieve JSON from the GitHub API."""
    return json.loads(
        subprocess.check_output(
            ["gh", "api", *args],
            text=True,
        )
    )


def associated_issue_numbers(pr):
    """Find issue references in the PR description or branch name."""
    numbers = set()

    body = pr.get("body") or ""

    numbers.update(int(number) for number in ISSUE_PATTERN.findall(body))

    branch = pr["head"]["ref"]
    match = BRANCH_PATTERN.match(branch)

    if match:
        numbers.add(int(match.group(1)))

    return sorted(numbers)


def has_valid_issue(numbers, issue_lookup):
    """Confirm that at least one reference points to a real issue."""
    for number in numbers:
        try:
            issue = issue_lookup(number)
        except (subprocess.CalledProcessError, KeyError):
            continue

        if "pull_request" not in issue:
            return True

    return False


def validate_pr(pr, issue_lookup=None):
    """Return validation errors for a pull request."""
    errors = []

    labels = {label["name"] for label in pr.get("labels", [])}

    base = pr["base"]["ref"]
    head = pr["head"]["ref"]

    release_pr = (
        base == "main" and head == "dev" and pr["head"]["repo"]["full_name"] == REPO
    )

    if base not in {"dev", "main"}:
        return ["Unsupported target branch."]

    if base == "main" and not release_pr:
        return [
            "PRs targeting main must be release PRs from dev in the same repository."
        ]

    types = {label for label in labels if label.startswith("type:")}

    semver = {label for label in labels if label.startswith("semver:")}

    areas = {label for label in labels if label.startswith("area:")}

    unknown_types = types - VALID_TYPES
    unknown_semver = semver - VALID_SEMVER

    if unknown_types:
        errors.append(f"Unknown type labels: {sorted(unknown_types)}")

    if unknown_semver:
        errors.append(f"Unknown SemVer labels: {sorted(unknown_semver)}")

    if len(semver) != 1:
        errors.append("Exactly one semver:* label is required.")

    if release_pr:
        # Release PRs aggregate labels from multiple development PRs.
        return errors

    if len(types) != 1:
        errors.append("Exactly one type:* label is required.")

    if not areas:
        errors.append("At least one area:* label is required.")

    if ISSUE_EXCEPTION_LABEL not in labels:
        numbers = associated_issue_numbers(pr)

        if not numbers:
            errors.append(
                "No associated issue found. Add 'Refs #123' to the PR description."
            )
        elif issue_lookup is not None:
            if not has_valid_issue(numbers, issue_lookup):
                errors.append("No valid issue found among the references.")

    return errors


def main():
    pr = gh(f"repos/{REPO}/pulls/{PR_NUMBER}")

    def lookup_issue(number):
        return gh(f"repos/{REPO}/issues/{number}")

    errors = validate_pr(pr, issue_lookup=lookup_issue)

    if errors:
        print("PR validation failed:\n")

        for error in errors:
            print(f"- {error}")

        sys.exit(1)

    print(f"PR #{PR_NUMBER}: validation passed.")


if __name__ == "__main__":
    main()
