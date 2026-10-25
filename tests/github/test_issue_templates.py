"""Validate GitHub Issue Forms."""

from pathlib import Path

import pytest
import yaml

TEMPLATE_DIR = Path(__file__).resolve().parents[2] / ".github" / "ISSUE_TEMPLATE"

EXPECTED_LABELS = {
    "bug.yml": "type:bug",
    "feature.yml": "type:feature",
    "task.yml": "type:maintenance",
}


@pytest.mark.parametrize("filename,label", EXPECTED_LABELS.items())
def test_issue_template(filename, label):
    path = TEMPLATE_DIR / filename

    assert path.exists()

    data = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert data["name"]
    assert data["description"]
    assert label in data["labels"]
    assert data["body"]

    required_fields = [
        field for field in data["body"] if field.get("validations", {}).get("required")
    ]

    assert required_fields, "Each template needs a required field"


def test_blank_issues_are_enabled():
    path = TEMPLATE_DIR / "config.yml"

    data = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert data["blank_issues_enabled"] is True
