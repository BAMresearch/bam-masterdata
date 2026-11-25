import importlib.util
import sys
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

    def test_skips_private_mixins(self):
        source = """
class Root:
    pass

class _Mixin:
    pass

class Child(_Mixin, Root):
    pass
"""
        hierarchy = generator.get_class_hierarchy(source)

        assert hierarchy == {"Root": ["Child"], "Child": []}

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

    def test_marks_imported_ancestors(self, tmp_path, monkeypatch):
        monkeypatch.setattr(generator, "DATAMODEL_DIR", tmp_path)
        (tmp_path / "parents.py").write_text(
            "class Root: pass\nclass Parent(Root): pass\n", encoding="utf-8"
        )
        source = "from .parents import Parent\n\nclass Child(Parent): pass\n"
        module_path = tmp_path / "children.py"

        local_only = generator.update_hierarchy_comments(source, 0, module_path)
        one_layer = generator.update_hierarchy_comments(source, 1, module_path)
        all_layers = generator.update_hierarchy_comments(source, -1, module_path)

        assert "# Child\n" in local_only
        assert "Parent*" not in local_only
        assert "# Parent*\n# └── Child\n" in one_layer
        assert "Root*" not in one_layer
        assert "# Root*\n# └── Parent*\n#     └── Child\n" in all_layers


class TestRepositoryIntegration:
    def test_all_v1_hierarchy_comments_are_current(self, monkeypatch):
        """Ensure generated comments match the default CLI check used by CI."""
        monkeypatch.setattr(sys, "argv", [str(SCRIPT_PATH), "--check"])
        generator.main()
