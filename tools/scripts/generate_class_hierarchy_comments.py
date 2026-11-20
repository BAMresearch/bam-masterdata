import argparse
import ast
from pathlib import Path

DATAMODEL_DIR = (
    Path(__file__).resolve().parents[2] / "bam_masterdata" / "datamodel" / "v1"
)

START_MARKER = "# AUTO-GENERATED CLASS HIERARCHY — DO NOT EDIT"
END_MARKER = "# END AUTO-GENERATED CLASS HIERARCHY"


def get_class_hierarchy(
    source: str, import_depth: int = 0, module_path: Path | None = None
) -> dict[str, list[str]]:
    """Return local classes and up to import_depth imported ancestor layers.

    A depth of -1 follows ancestors to Root. Imports are resolved statically so
    generating comments does not execute the datamodel modules.
    """
    if import_depth < -1:
        raise ValueError("import_depth must be -1 or a non-negative integer")
    if import_depth and module_path is None:
        raise ValueError("module_path is required when import_depth is not zero")

    modules: dict[Path, ast.Module] = {}

    def parse(path: Path) -> ast.Module:
        if path not in modules:
            modules[path] = ast.parse(path.read_text(encoding="utf-8"))
        return modules[path]

    tree = ast.parse(source)
    if module_path is not None:
        module_path = module_path.resolve()
        modules[module_path] = tree
    classes = {node.name: node for node in tree.body if isinstance(node, ast.ClassDef)}
    hierarchy = {name: [] for name in classes}

    def resolve(
        path: Path, name: str, seen: set[tuple[Path, str]]
    ) -> tuple[Path, ast.ClassDef] | None:
        key = (path, name)
        if key in seen:
            return None
        seen.add(key)
        for node in parse(path).body:
            if isinstance(node, ast.ClassDef) and node.name == name:
                return path, node
            if isinstance(node, ast.Assign) and isinstance(node.value, ast.Name):
                if any(
                    isinstance(target, ast.Name) and target.id == name
                    for target in node.targets
                ):
                    return resolve(path, node.value.id, seen)
            if isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    if (alias.asname or alias.name) != name:
                        continue
                    if node.level:
                        base = path.parent
                        for _ in range(node.level - 1):
                            base = base.parent
                        parts = (node.module or "").split(".") if node.module else []
                        target = base.joinpath(*parts).with_suffix(".py")
                    elif node.module and node.module.startswith(
                        "bam_masterdata.datamodel.v1."
                    ):
                        parts = node.module.split(".")[3:]
                        target = DATAMODEL_DIR.joinpath(*parts).with_suffix(".py")
                    else:
                        return None
                    if target.is_file() and target.resolve().is_relative_to(
                        DATAMODEL_DIR.resolve()
                    ):
                        return resolve(target.resolve(), alias.name, seen)
        return None

    for name, node in classes.items():
        for base in node.bases:
            if not isinstance(base, ast.Name):
                continue
            if base.id in classes:
                hierarchy[base.id].append(name)
                break
            if import_depth and module_path is not None:
                parent = resolve(module_path, base.id, set())
                if parent is None:
                    continue
                child = name
                remaining = import_depth
                visited: set[tuple[Path, str]] = set()
                while parent is not None and remaining != 0:
                    path, ancestor = parent
                    key = (path, ancestor.name)
                    if key in visited:
                        break
                    visited.add(key)
                    hierarchy.setdefault(ancestor.name, [])
                    if child not in hierarchy[ancestor.name]:
                        hierarchy[ancestor.name].append(child)
                    if ancestor.name == "Root":
                        break
                    child = ancestor.name
                    if remaining > 0:
                        remaining -= 1
                    parent = next(
                        (
                            resolved
                            for item in ancestor.bases
                            if isinstance(item, ast.Name)
                            if (resolved := resolve(path, item.id, set())) is not None
                        ),
                        None,
                    )
                break

    return hierarchy


def format_hierarchy(hierarchy: dict[str, list[str]]) -> str:
    """Render inheritance relationships as a readable tree."""
    children = {child for descendants in hierarchy.values() for child in descendants}

    roots = [name for name in hierarchy if name not in children]
    lines = []

    def render(name: str, prefix: str = "") -> None:
        lines.append(f"{prefix}{name}")

        descendants = hierarchy[name]

        for index, child in enumerate(descendants):
            last = index == len(descendants) - 1
            connector = "└── " if last else "├── "
            continuation = "    " if last else "│   "

            render_child(child, prefix, connector, continuation)

    def render_child(
        name: str,
        prefix: str,
        connector: str,
        continuation: str,
    ) -> None:
        lines.append(f"{prefix}{connector}{name}")

        descendants = hierarchy[name]

        for index, child in enumerate(descendants):
            last = index == len(descendants) - 1
            next_connector = "└── " if last else "├── "
            next_continuation = "    " if last else "│   "

            render_child(
                child,
                prefix + continuation,
                next_connector,
                next_continuation,
            )

    for root in roots:
        if lines:
            lines.append("")
        render(root)

    return "\n".join(f"# {line}" if line else "#" for line in lines)


def update_hierarchy_comments(
    source: str, import_depth: int = 0, module_path: Path | None = None
) -> str:
    """Insert or replace the generated hierarchy comment block."""
    hierarchy = get_class_hierarchy(source, import_depth, module_path)

    if not hierarchy:
        return source

    generated = f"{START_MARKER}\n#\n{format_hierarchy(hierarchy)}\n#\n{END_MARKER}"

    if START_MARKER in source:
        start = source.index(START_MARKER)
        end = source.index(END_MARKER, start) + len(END_MARKER)

        return source[:start] + generated + source[end:]

    return generated + "\n\n" + source


def main() -> None:
    """Generate or validate hierarchy comments in all v1 Python modules."""
    parser = argparse.ArgumentParser(
        description="Generate or validate class hierarchy comments in datamodel/v1."
    )

    mode = parser.add_mutually_exclusive_group(required=True)

    mode.add_argument(
        "--write",
        action="store_true",
        help="Generate or update class hierarchy comments.",
    )

    mode.add_argument(
        "--check",
        action="store_true",
        help="Check whether class hierarchy comments are up to date.",
    )

    parser.add_argument(
        "--import-depth",
        type=int,
        default=0,
        help="Imported ancestor layers to include (default: 0; -1: through Root).",
    )
    parser.add_argument(
        "--path",
        type=Path,
        default=DATAMODEL_DIR,
        help="Python file or directory to process (default: datamodel/v1).",
    )
    args = parser.parse_args()
    if args.import_depth < -1:
        parser.error("--import-depth must be -1 or a non-negative integer")

    # Discover all Python modules recursively, including subdirectories.
    selected_path = args.path.resolve()
    candidates = (
        [selected_path] if selected_path.is_file() else selected_path.rglob("*.py")
    )
    files = sorted(
        path
        for path in candidates
        if path.name not in ["__init__.py", "vocabularies.py"]
    )

    outdated = []

    for path in files:
        source = path.read_text(encoding="utf-8")
        updated = update_hierarchy_comments(source, args.import_depth, path)

        relative_path = path.relative_to(DATAMODEL_DIR)

        # Files without class definitions remain unchanged.
        if updated == source:
            print(f"OK: {relative_path}")
            continue

        if args.write:
            path.write_text(updated, encoding="utf-8")
            print(f"Updated: {relative_path}")
        else:
            outdated.append(relative_path)
            print(f"Outdated: {relative_path}")

    if outdated:
        parser.exit(
            status=1,
            message=(
                "\nClass hierarchy comments are outdated.\n"
                "Run the following command to regenerate them:\n\n"
                "uv run python tools/scripts/"
                "generate_class_hierarchy_comments.py --write\n"
            ),
        )


if __name__ == "__main__":
    main()
