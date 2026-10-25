"""Tests for release label aggregation."""

import importlib.util
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[2] / ".github/scripts/prepare_release.py"

spec = importlib.util.spec_from_file_location("prepare_release", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def make_pr(number, labels):
    return {
        "number": number,
        "title": f"Test PR {number}",
        "labels": [{"name": name} for name in labels],
    }


def test_aggregate_release_labels():
    prs = [
        make_pr(
            100,
            [
                "type:feature",
                "area:datamodel",
                "semver:minor",
            ],
        ),
        make_pr(
            101,
            [
                "type:bug",
                "area:cli",
                "semver:patch",
            ],
        ),
        make_pr(
            102,
            [
                "type:documentation",
                "area:docs",
                "semver:none",
            ],
        ),
    ]

    labels, problems = module.aggregate_labels(prs)

    assert problems == []
    assert labels == sorted(
        [
            "type:feature",
            "type:bug",
            "type:documentation",
            "area:datamodel",
            "area:cli",
            "area:docs",
            "semver:minor",
        ]
    )


def test_major_has_highest_priority():
    prs = [
        make_pr(100, ["semver:patch"]),
        make_pr(101, ["semver:major"]),
        make_pr(102, ["semver:minor"]),
    ]

    labels, problems = module.aggregate_labels(prs)

    assert problems == []
    assert labels == ["semver:major"]


def test_missing_semver_is_rejected():
    prs = [
        make_pr(100, ["type:feature"]),
    ]

    labels, problems = module.aggregate_labels(prs)

    assert labels == []
    assert len(problems) == 1


@pytest.mark.parametrize(
    "labels",
    [
        ["semver:minor", "semver:patch"],
        ["semver:invalid"],
    ],
)
def test_invalid_semver_is_rejected(labels):
    prs = [make_pr(100, labels)]

    result, problems = module.aggregate_labels(prs)

    assert result == []
    assert problems


def test_priority_labels_are_excluded():
    prs = [
        make_pr(
            100,
            [
                "type:feature",
                "priority:urgent",
                "semver:minor",
            ],
        ),
    ]

    labels, problems = module.aggregate_labels(prs)

    assert problems == []
    assert "priority:urgent" not in labels


def test_unmatched_commits_do_not_block_release(capsys):
    """Unmatched commits should generate warnings, not errors."""
    unmatched = ["1dd09bbb990c"]

    module.validate_release(problems=[], unmatched=unmatched)

    output = capsys.readouterr().out

    assert "WARNING" in output
    assert "Review these commits manually" in output


def test_invalid_semver_blocks_release():
    """Invalid PR classifications must prevent release preparation."""
    problems = ["#123: invalid SemVer labels []"]

    with pytest.raises(SystemExit, match="invalid SemVer labels"):
        module.validate_release(
            problems=problems,
            unmatched=[],
        )


def test_valid_release_has_no_warnings(capsys):
    """A fully classified release should pass without warnings."""
    module.validate_release(
        problems=[],
        unmatched=[],
    )

    output = capsys.readouterr().out

    assert output == ""
