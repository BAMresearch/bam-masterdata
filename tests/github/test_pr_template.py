"""Tests for the pull request template."""

from pathlib import Path

TEMPLATE = Path(__file__).resolve().parents[2] / ".github" / "pull_request_template.md"


def test_pr_template_exists():
    assert TEMPLATE.exists()


def test_pr_template_contains_required_sections():
    content = TEMPLATE.read_text(encoding="utf-8")

    assert "## Description" in content
    assert "## Related issue" in content
    assert "## Checklist" in content


def test_pr_template_contains_required_guidance():
    content = TEMPLATE.read_text(encoding="utf-8")

    assert "type:*" in content
    assert "area:*" in content
    assert "semver:*" in content
    assert "Tests have been added or updated" in content
    assert "Documentation has been updated" in content
