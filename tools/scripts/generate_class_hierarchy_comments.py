import argparse
import ast
from pathlib import Path

DATAMODEL_DIR = (
    Path(__file__).resolve().parents[2] / "bam_masterdata" / "datamodel" / "v1"
)

START_MARKER = "# AUTO-GENERATED CLASS HIERARCHY — DO NOT EDIT"
END_MARKER = "# END AUTO-GENERATED CLASS HIERARCHY"


def get_class_hierarchy(source: str) -> dict[str, list[str]]:
    """Return parent-child relationships for classes defined in a module."""
    tree = ast.parse(source)

    classes = {node.name: node for node in tree.body if isinstance(node, ast.ClassDef)}

    hierarchy = {name: [] for name in classes}

    for name, node in classes.items():
        for base in node.bases:
            if isinstance(base, ast.Name) and base.id in classes:
                hierarchy[base.id].append(name)
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
        render(root)

    return "\n".join(f"# {line}" for line in lines)


def update_hierarchy_comments(source: str) -> str:
    """Insert or replace the generated hierarchy comment block."""
    hierarchy = get_class_hierarchy(source)

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

    args = parser.parse_args()

    # Discover all Python modules recursively, including subdirectories.
    files = sorted(
        path
        for path in DATAMODEL_DIR.rglob("*.py")
        if path.name not in ["__init__.py", "vocabularies.py"]
    )

    outdated = []

    for path in files:
        source = path.read_text(encoding="utf-8")
        updated = update_hierarchy_comments(source)

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
