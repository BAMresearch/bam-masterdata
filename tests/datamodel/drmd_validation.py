"""
Optional validation of generated DRMD documents with the DRMD schema repository.

Set the environment variable DRMD_SCHEMA_DIR to the folder of the schema repository, i.e. the
folder that contains drmd.xsd, drmd-business-rules.sch, catalog.xml, supporting/ and
tools/validate.py. The validation uses the functions of tools/validate.py, so the result is the
same as running that script. lxml must be installed. Without the folder or without lxml, the
tests that need the schema are skipped.
"""

from __future__ import annotations

import functools
import importlib.util
import os
from dataclasses import dataclass
from pathlib import Path

SCHEMA_DIR_VARIABLE = "DRMD_SCHEMA_DIR"


@dataclass
class SchemaValidator:
    """drmd.xsd and drmd-business-rules.sch, loaded once."""

    module: object
    xmlschema: object
    schematron: tuple

    def validate(self, document: bytes) -> tuple[list[str], list[dict]]:
        """Return the XSD errors and the Schematron findings of an XML document."""
        etree = self.module.etree
        tree = etree.fromstring(document).getroottree()
        errors = []
        if not self.xmlschema.validate(tree):
            errors = [f"line {e.line}: {e.message}" for e in self.xmlschema.error_log]
        namespaces, phases, patterns = self.schematron
        findings = self.module.run_schematron(tree, namespaces, phases, patterns, "all")
        return errors, findings


@functools.cache
def schema_validator() -> SchemaValidator | None:
    """The validator of the schema repository named in DRMD_SCHEMA_DIR, or None."""
    folder = os.environ.get(SCHEMA_DIR_VARIABLE)
    if not folder:
        return None
    if importlib.util.find_spec("lxml") is None:
        return None
    script = Path(folder) / "tools" / "validate.py"
    if not script.is_file():
        raise FileNotFoundError(
            f"{SCHEMA_DIR_VARIABLE}={folder} has no tools/validate.py"
        )
    spec = importlib.util.spec_from_file_location("drmd_schema_validate", script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    xmlschema = module.etree.XMLSchema(module.etree.parse(str(module.XSD)))
    return SchemaValidator(module, xmlschema, module.load_schematron(module.SCH))
