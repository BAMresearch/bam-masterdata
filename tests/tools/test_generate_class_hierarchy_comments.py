import importlib.util
from pathlib import Path

import pytest

SCRIPT_PATH = (
    Path(__file__).resolve().parents[2]
    / "tools"
    / "scripts"
    / "generate_class_hierarchy_comments.py"
)

spec = importlib.util.spec_from_file_location(
    "generate_class_hierarchy_comments", SCRIPT_PATH
)
assert spec is not None
assert spec.loader is not None

generator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generator)


class TestClassHierarchyGeneration:
    def test_detects_local_inheritance(self):
        source = """
class Root:
    pass

class Child(Root):
    pass

class Grandchild(Child):
    pass
"""
        hierarchy = generator.get_class_hierarchy(source)

        assert hierarchy == {
            "Root": ["Child"],
            "Child": ["Grandchild"],
            "Grandchild": [],
        }

    def test_excludes_imported_parents(self):
        source = """
from another_module import External

class First(External):
    pass

class Second(First):
    pass
"""
        hierarchy = generator.get_class_hierarchy(source)

        assert hierarchy == {
            "First": ["Second"],
            "Second": [],
        }

    def test_formats_multiple_roots(self):
        source = """
class First:
    pass

class FirstChild(First):
    pass

class Second:
    pass

class SecondChild(Second):
    pass
"""
        hierarchy = generator.get_class_hierarchy(source)
        result = generator.format_hierarchy(hierarchy)

        assert result == ("# First\n# └── FirstChild\n#\n# Second\n# └── SecondChild")

    def test_preserves_class_declaration_order(self):
        source = """
class Parent:
    pass

class Beta(Parent):
    pass

class Alpha(Parent):
    pass
"""
        hierarchy = generator.get_class_hierarchy(source)
        result = generator.format_hierarchy(hierarchy)

        assert result == ("# Parent\n# ├── Beta\n# └── Alpha")


class TestHierarchyComments:
    def test_inserts_generated_comments(self):
        source = "class Root:\n    pass\n"

        result = generator.update_hierarchy_comments(source)

        assert result.startswith(generator.START_MARKER)
        assert "# Root" in result
        assert generator.END_MARKER in result
        assert result.endswith(source)

    def test_replaces_existing_comments(self):
        source = (
            f"{generator.START_MARKER}\n"
            "# Old hierarchy\n"
            f"{generator.END_MARKER}\n\n"
            "class Root:\n"
            "    pass\n"
        )

        result = generator.update_hierarchy_comments(source)

        assert "# Old hierarchy" not in result
        assert "# Root" in result
        assert result.count(generator.START_MARKER) == 1
        assert result.count(generator.END_MARKER) == 1

    def test_generation_is_idempotent(self):
        source = """
class Root:
    pass

class Child(Root):
    pass
"""
        first = generator.update_hierarchy_comments(source)
        second = generator.update_hierarchy_comments(first)

        assert first == second

    def test_does_not_modify_files_without_classes(self):
        source = "VALUE = 42\n"

        assert generator.update_hierarchy_comments(source) == source


class TestRepositoryIntegration:
    def test_all_v1_hierarchy_comments_are_current(self):
        """Ensure generated comments match the current v1 class definitions."""
        files = sorted(
            path
            for path in generator.DATAMODEL_DIR.rglob("*.py")
            if path.name not in {"__init__.py", "vocabularies.py"}
        )

        for path in files:
            source = path.read_text(encoding="utf-8")
            expected = generator.update_hierarchy_comments(source)

            assert source == expected, (
                f"Outdated hierarchy comments in {path}. "
                "Run the generator with --write."
            )
