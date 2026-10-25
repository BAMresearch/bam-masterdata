"""Tests for GitHub pull request validation."""

import importlib.util
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[2] / ".github/scripts/validate_pr.py"

spec = importlib.util.spec_from_file_location("validate_pr", SCRIPT)
module = importlib.util.module_from_spec(spec)

# Set test environment before loading the module.
import os

os.environ.setdefault("REPO", "BAMresearch/bam-masterdata")
os.environ.setdefault("PR_NUMBER", "421")

spec.loader.exec_module(module)


def make_pr(
    labels,
    body="Refs #420",
    branch="feature/test",
    base="dev",
):
    return {
        "number": 100,
        "body": body,
        "labels": [{"name": name} for name in labels],
        "base": {"ref": base},
        "head": {
            "ref": branch,
            "repo": {"full_name": "BAMresearch/bam-masterdata"},
        },
    }


def valid_labels():
    return [
        "type:feature",
        "area:datamodel",
        "semver:minor",
    ]


def test_valid_development_pr():
    pr = make_pr(valid_labels())

    errors = module.validate_pr(
        pr,
        issue_lookup=lambda number: {"number": number},
    )

    assert errors == []


def test_missing_semver():
    pr = make_pr(
        [
            "type:feature",
            "area:datamodel",
        ]
    )

    errors = module.validate_pr(pr)

    assert any("Exactly one semver" in e for e in errors)


def test_multiple_semver_labels():
    pr = make_pr(valid_labels() + ["semver:patch"])

    errors = module.validate_pr(pr)

    assert any("Exactly one semver" in e for e in errors)


def test_missing_type():
    pr = make_pr(
        [
            "area:datamodel",
            "semver:minor",
        ]
    )

    errors = module.validate_pr(pr)

    assert any("Exactly one type" in e for e in errors)


def test_missing_area():
    pr = make_pr(
        [
            "type:feature",
            "semver:minor",
        ]
    )

    errors = module.validate_pr(pr)

    assert any("area:" in e for e in errors)


def test_missing_issue():
    pr = make_pr(valid_labels(), body="")

    errors = module.validate_pr(pr)

    assert any("No associated issue" in e for e in errors)


def test_branch_issue_reference():
    pr = make_pr(
        valid_labels(),
        body="",
        branch="420-improve-label-handling",
    )

    errors = module.validate_pr(
        pr,
        issue_lookup=lambda number: {"number": number},
    )

    assert errors == []


def test_invalid_issue_reference():
    pr = make_pr(valid_labels(), body="Refs #999999")

    errors = module.validate_pr(
        pr,
        issue_lookup=lambda number: {
            "number": number,
            "pull_request": {},
        },
    )

    assert any("No valid issue" in e for e in errors)


def test_issue_exception():
    pr = make_pr(
        valid_labels() + ["no-issue-required"],
        body="",
    )

    assert module.validate_pr(pr) == []


def test_release_pr():
    pr = make_pr(
        [
            "type:feature",
            "type:bug",
            "area:datamodel",
            "semver:minor",
        ],
        body="",
        branch="dev",
        base="main",
    )

    assert module.validate_pr(pr) == []


def test_release_pr_requires_semver():
    pr = make_pr(
        ["type:feature"],
        body="",
        branch="dev",
        base="main",
    )

    errors = module.validate_pr(pr)

    assert any("Exactly one semver" in e for e in errors)


def test_non_release_pr_to_main():
    pr = make_pr(
        valid_labels(),
        branch="feature/test",
        base="main",
    )

    errors = module.validate_pr(pr)

    assert any("release PRs" in e for e in errors)


@pytest.mark.parametrize(
    "unknown_label",
    ["semver:invalid", "type:unknown"],
)
def test_unknown_classification(unknown_label):
    pr = make_pr(valid_labels() + [unknown_label])

    errors = module.validate_pr(pr)

    assert any("Unknown" in e for e in errors)
