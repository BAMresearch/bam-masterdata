"""Tests for GitHub issue-to-PR label synchronization."""

import importlib.util
import unittest
from pathlib import Path

SCRIPT = (
    Path(__file__).resolve().parents[2] / ".github" / "scripts" / "sync_issue_labels.py"
)

spec = importlib.util.spec_from_file_location("sync_issue_labels", SCRIPT)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class TestSyncIssueLabels(unittest.TestCase):
    def test_issue_references(self):
        pr = {
            "body": "Refs #420; fixes #42",
            "head": {"ref": "420-label-work"},
        }

        self.assertEqual(
            module.issue_numbers_from_pr(pr, [12]),
            [12, 42, 420],
        )

    def test_unrelated_numbers(self):
        pr = {
            "body": "Version 420",
            "head": {"ref": "feature-420"},
        }

        self.assertEqual(
            module.issue_numbers_from_pr(pr),
            [],
        )

    def test_preserve_existing_semver(self):
        existing = {
            "semver:patch",
            "type:documentation",
        }

        incoming = [
            "semver:minor",
            "type:feature",
            "area:docs",
        ]

        self.assertEqual(
            module.labels_to_copy(existing, incoming),
            ["area:docs"],
        )

    def test_exclusive_labels(self):
        self.assertEqual(
            module.labels_to_copy(
                set(),
                [
                    "semver:minor",
                    "semver:patch",
                    "type:bug",
                    "type:feature",
                ],
            ),
            ["semver:minor", "type:bug"],
        )

    def test_copy_missing_labels(self):
        self.assertEqual(
            module.labels_to_copy(
                {"area:docs"},
                ["area:docs", "area:ci"],
            ),
            ["area:ci"],
        )

    def test_priority_labels_not_copied(self):
        existing = {"type:feature"}

        issue_labels = [
            "type:maintenance",
            "priority:urgent",
            "area:datamodel",
            "semver:minor",
            "backlog",
        ]

        result = module.labels_to_copy(existing, issue_labels)

        self.assertEqual(
            result,
            ["area:datamodel", "semver:minor"],
        )


if __name__ == "__main__":
    unittest.main()
