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


def test_release_notes_group_prs_and_preserve_links():
    prs = [
        make_pr(100, ["type:feature", "semver:minor"]),
        make_pr(101, ["type:bug", "semver:patch"]),
    ]

    prs[0]["title"] = "Add instrument profiles"
    prs[0]["user"] = {"login": "alice"}

    prs[1]["title"] = "Fix Excel export"
    prs[1]["user"] = {"login": "bob"}

    notes = module.render_release_notes(
        prs,
        ["type:feature", "type:bug", "semver:minor"],
    )

    assert "**Suggested SemVer impact:** `minor`" in notes
    assert "## Features" in notes
    assert "## Bug Fixes" in notes

    assert "[#100](https://github.com/BAMresearch/bam-masterdata/pull/100)" in notes
    assert "Add instrument profiles (@alice)" in notes
    assert "Fix Excel export (@bob)" in notes


def test_release_notes_include_unmatched_commits():
    sha = "1dd09bbb990c1234567890123456789012345678"  # pragma: allowlist secret

    notes = module.render_release_notes(
        [make_pr(100, ["type:documentation", "semver:none"])],
        ["type:documentation", "semver:none"],
        unmatched=[sha],
    )

    assert "## Needs Manual Review" in notes
    assert sha in notes
    assert "Review these commits" in notes


def test_release_notes_uncategorized_pr():
    prs = [
        make_pr(100, ["area:datamodel", "semver:minor"]),
    ]

    notes = module.render_release_notes(prs, ["area:datamodel", "semver:minor"])

    assert "## Other Changes" in notes
    assert "[#100]" in notes


def test_release_notes_write_file(tmp_path, monkeypatch):
    output = tmp_path / "release-notes.md"

    monkeypatch.setattr(module, "RELEASE_NOTES_PATH", output)

    prs = [
        make_pr(100, ["type:feature", "semver:minor"]),
    ]

    module.write_release_notes(prs, ["type:feature", "semver:minor"])

    assert output.exists()
    assert "## Features" in output.read_text(encoding="utf-8")


@pytest.mark.parametrize(
    ("current", "impact", "expected"),
    [
        ("0.15.0", "none", None),
        ("0.15.0", "patch", "0.15.1"),
        ("0.15.0", "minor", "0.16.0"),
        ("0.15.0", "major", "0.16.0"),
        ("0.15.3", "minor", "0.16.0"),
        ("0.15.3", "major", "0.16.0"),
        ("1.2.3", "patch", "1.2.4"),
        ("1.2.3", "minor", "1.3.0"),
        ("1.2.3", "major", "2.0.0"),
        ("v1.2.3", "minor", "1.3.0"),
    ],
)
def test_suggest_next_version(current, impact, expected):
    assert module.suggest_next_version(current, impact) == expected


@pytest.mark.parametrize(
    "invalid_version",
    [
        "invalid",
        "1.2",
        "1.2.3.4",
        "1.0.0rc1",
        "01.2.3",
    ],
)
def test_invalid_version_rejected(invalid_version):
    with pytest.raises(ValueError, match="Invalid stable release version"):
        module.parse_version(invalid_version)


def test_unknown_semver_impact_rejected():
    with pytest.raises(ValueError, match="Unknown SemVer impact"):
        module.suggest_next_version("0.15.0", "unknown")


def test_missing_semver_impact_rejected():
    with pytest.raises(ValueError, match="Expected exactly one"):
        module.get_release_impact(["type:feature"])


def test_latest_release_version(monkeypatch):
    def fake_gh(*args):
        assert args == ("repos/BAMresearch/bam-masterdata/releases/latest",)
        return {"tag_name": "v0.15.0"}

    monkeypatch.setattr(module, "gh", fake_gh)

    assert module.get_latest_release_version() == "v0.15.0"


def test_release_notes_include_version_suggestion():
    prs = [
        make_pr(100, ["type:feature", "semver:minor"]),
    ]

    notes = module.render_release_notes(
        prs,
        ["type:feature", "semver:minor"],
        current_version="v0.15.0",
        next_version="0.16.0",
    )

    assert "**Current release:** `v0.15.0`" in notes
    assert "**Suggested release:** `v0.16.0`" in notes
    assert "**Suggested SemVer impact:** `minor`" in notes
