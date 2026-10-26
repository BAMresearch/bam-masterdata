"""Validate GitHub Markdown issue templates."""

from pathlib import Path

import pytest
import yaml

TEMPLATE_DIR = Path(__file__).resolve().parents[2] / ".github" / "ISSUE_TEMPLATE"

EXPECTED_TEMPLATES = {
    "bug.md": {
        "name": "Bug report",
        "label": "type:bug",
        "sections": ["What is the problem?", "How can we reproduce it?"],
    },
    "feature.md": {
        "name": "Feature or enhancement",
        "label": "type:feature",
        "sections": ["What problem should we solve?", "Proposed solution"],
    },
    "task.md": {
        "name": "General task",
        "label": "type:maintenance",
        "sections": ["What needs to be done?", "When is this complete?"],
    },
}


def parse_markdown_template(path: Path) -> tuple[dict, str]:
    """Extract YAML front matter and Markdown body."""
    content = path.read_text(encoding="utf-8")

    assert content.startswith(
        "---\n"
    ), f"{path.name}: YAML front matter must start on the first line"

    parts = content.split("---\n", maxsplit=2)

    assert len(parts) == 3, f"{path.name}: Missing closing YAML front matter delimiter"

    metadata = yaml.safe_load(parts[1])
    body = parts[2]

    assert isinstance(metadata, dict)
    assert body.strip(), f"{path.name}: Markdown body must not be empty"

    return metadata, body


@pytest.mark.parametrize(
    "filename,expected",
    EXPECTED_TEMPLATES.items(),
)
def test_issue_template(filename: str, expected: dict):
    path = TEMPLATE_DIR / filename

    assert path.is_file(), f"Missing issue template: {filename}"

    metadata, body = parse_markdown_template(path)

    # GitHub Markdown issue template metadata
    assert metadata["name"] == expected["name"]
    assert metadata["about"]
    assert expected["label"] in metadata["labels"]

    # Check the expected sections
    for section in expected["sections"]:
        assert f"## {section}" in body, f"{filename}: Missing section '{section}'"


def test_no_legacy_yaml_issue_forms():
    """Ensure the old YAML issue forms have been removed."""
    for filename in ("bug.yml", "feature.yml", "task.yml"):
        assert not (
            TEMPLATE_DIR / filename
        ).exists(), f"Legacy issue form still exists: {filename}"


def test_blank_issues_are_enabled():
    path = TEMPLATE_DIR / "config.yml"

    data = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert data["blank_issues_enabled"] is True
