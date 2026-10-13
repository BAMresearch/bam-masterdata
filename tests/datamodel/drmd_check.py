"""
Check DRMD XML documents against the DRMD datamodel.

Run from the root of the repository:

    python -m tests.datamodel.drmd_check path/to/document.xml [more.xml ...]

For each document the command

1. reads it into the DRMD masterdata objects and lists every part that is not imported
   (`xml_to_graph()`),
2. checks the objects with the DRMD rules (`check_graph()`),
3. writes the objects back as XML (`graph_to_xml()`), into the folder given with `--output-dir`
   or next to the document as `<name>_regenerated.xml`,
4. compares the original with the regenerated document (`compare_documents()`),
5. validates the regenerated document with drmd.xsd and drmd-business-rules.sch when the
   environment variable DRMD_SCHEMA_DIR names the DRMD schema repository and lxml is installed.

The exit code is 0 if every document passes all steps, 1 otherwise. See README.md of
bam_masterdata/datamodel/drmd, section 15.
"""

from __future__ import annotations

import argparse
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from tests.datamodel.drmd_rules import check_graph, is_compliant
from tests.datamodel.drmd_validation import SCHEMA_DIR_VARIABLE, schema_validator
from tests.datamodel.drmd_xml import (
    UnsupportedContentError,
    compare_documents,
    graph_to_xml,
    xml_to_graph,
)


def check_document(source: Path, output_dir: Path | None = None) -> bool:
    """Run all steps for one document, print a report and return True if it passes."""
    print(f"\n{source}")
    passed = True

    try:
        graph = xml_to_graph(source, bam_oe="CHECK")
    except (UnsupportedContentError, ET.ParseError, KeyError, AttributeError) as error:
        # the document is not a valid DRMD 1.0.0 document; xml_to_graph() expects one
        print(f"  1. Import: not possible: {type(error).__name__}: {error}")
        print("  Result: NOT PASSED")
        return False
    print(f"  1. Import: {len(graph.collection.attached_objects)} objects")
    for warning in graph.warnings:
        print(f"     not imported: {warning}")
        passed = False

    findings = check_graph(graph)
    print(f"  2. Rules: {len(findings)} finding(s)")
    for finding in findings:
        print(f"     {finding.rule_id} ({finding.severity}): {finding.message}")
    passed = passed and is_compliant(findings)

    regenerated = graph_to_xml(graph)
    folder = output_dir if output_dir is not None else source.parent
    target = folder / f"{source.stem}_regenerated.xml"
    target.write_bytes(regenerated)
    print(f"  3. Written: {target}")

    differences = compare_documents(source, regenerated)
    if differences:
        print("  4. Round trip: differences")
        for line in differences:
            print(f"     {line}")
        passed = False
    else:
        print("  4. Round trip: identical")

    validator = schema_validator()
    if validator is None:
        print(
            f"  5. XSD and Schematron: skipped (set {SCHEMA_DIR_VARIABLE}, install lxml)"
        )
    else:
        errors, raised = validator.validate(regenerated)
        print(f"  5. XSD: {'valid' if not errors else 'invalid'}")
        for error in errors:
            print(f"     {error}")
        print(f"     Schematron: {len(raised)} finding(s)")
        for finding in raised:
            print(f"     {finding['rule_id']} ({finding['severity']})")
        blocking = [
            f for f in raised if f["severity"] in ("error", "conditional-error")
        ]
        passed = passed and not errors and not blocking

    print(f"  Result: {'PASSED' if passed else 'NOT PASSED'}")
    return passed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m tests.datamodel.drmd_check",
        description="Check DRMD XML documents against the DRMD datamodel.",
    )
    parser.add_argument("documents", nargs="+", type=Path, help="DRMD XML files")
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="folder for the regenerated documents (default: next to each document)",
    )
    args = parser.parse_args(argv)
    if args.output_dir is not None:
        args.output_dir.mkdir(parents=True, exist_ok=True)
    results = [check_document(path, args.output_dir) for path in args.documents]
    print(f"\n{sum(results)} of {len(results)} document(s) passed.")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
