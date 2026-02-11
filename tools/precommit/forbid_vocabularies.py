#!/usr/bin/env python3
from __future__ import annotations

import ast
import sys
from collections.abc import Iterable
from pathlib import Path

# Put codes you NEVER want committed here:
FORBIDDEN_CODES = {
    "BAM_LOCATION_COMPLETE",
    # Add more here...
}

TARGET_FILE = Path("bam_masterdata/datamodel/vocabulary_types.py")


def iter_vocabularytypedef_codes(tree: ast.AST) -> Iterable[tuple[str, int]]:
    """
    Yield (code_value, lineno) for occurrences of:
        VocabularyTypeDef(code="SOMETHING", ...)
    in the AST.
    """
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue

        # Match the call name "VocabularyTypeDef" (either direct or attribute)
        func_name = None
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
        elif isinstance(node.func, ast.Attribute):
            func_name = node.func.attr

        if func_name != "VocabularyTypeDef":
            continue

        # Find keyword argument "code"
        for kw in node.keywords:
            if kw.arg != "code":
                continue

            # We only enforce when it's a literal string.
            if isinstance(kw.value, ast.Constant) and isinstance(kw.value.value, str):
                yield (
                    kw.value.value,
                    getattr(kw.value, "lineno", getattr(node, "lineno", 0)),
                )


def main(argv: list[str]) -> int:
    # Pre-commit passes the matched filenames as argv[1:].
    # We still hard-guard to only enforce on the intended file.
    passed_files = [Path(p) for p in argv[1:]]
    if passed_files and all(
        p.as_posix() != TARGET_FILE.as_posix() for p in passed_files
    ):
        return 0

    if not TARGET_FILE.exists():
        # If file is missing in some ref / partial checkout, don't block commits.
        return 0

    try:
        source = TARGET_FILE.read_text(encoding="utf-8")
        tree = ast.parse(source, filename=str(TARGET_FILE))
    except SyntaxError as e:
        print(
            f"[forbid-vocabulary-codes] Syntax error in {TARGET_FILE}: {e}",
            file=sys.stderr,
        )
        return 1

    violations: list[tuple[str, int]] = []
    for code, lineno in iter_vocabularytypedef_codes(tree):
        if code in FORBIDDEN_CODES:
            violations.append((code, lineno))

    if violations:
        print(
            f"[forbid-vocabulary-codes] Forbidden VocabularyTypeDef.code value(s) found in {TARGET_FILE}:",
            file=sys.stderr,
        )
        for code, lineno in violations:
            print(f"  - {code!r} at line {lineno}", file=sys.stderr)
        print(
            "\nRemove/rename these codes or move them out of the repository.",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
