"""Conventions of the DRMD datamodel in bam_masterdata/datamodel/drmd/."""

import importlib
import inspect
import os
import pkgutil
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

import bam_masterdata.datamodel as datamodel_package
from bam_masterdata.checker.checker import MasterdataChecker
from bam_masterdata.datamodel.drmd import object_types as drmd_object_types
from bam_masterdata.datamodel.drmd import vocabularies as drmd_vocabularies
from bam_masterdata.metadata.entities import ObjectType, VocabularyType
from tests.datamodel.drmd_validation import SCHEMA_DIR_VARIABLE

DRMD_DIR = Path(drmd_object_types.__file__).parent
DATAMODEL_DIR = DRMD_DIR.parent


def _classes(module, base):
    return [
        cls
        for _, cls in inspect.getmembers(module, inspect.isclass)
        if issubclass(cls, base) and cls.__module__ == module.__name__
    ]


DRMD_OBJECT_TYPES = _classes(drmd_object_types, ObjectType)
DRMD_VOCABULARIES = _classes(drmd_vocabularies, VocabularyType)

# Property types that existed in the BAM datamodel before and are reused unchanged
REUSED_PROPERTY_TYPES = {
    "$NAME",
    "DESCRIPTION",
    "ALIAS",
    "VERSION",
    "UUID",
    "DATE_EXPIRATION",
    "EMAIL",
    "TELEPHONE",
    "HOMEPAGE",
    "REFERENCE",
    "RESPONSIBLE_PERSON",
    "NOTES",
    "$XMLCOMMENTS",
}

# Properties that are mandatory in openBIS: those required in both document types
# (README.md, section 6 "Two document types, one datamodel")
MANDATORY = {
    "DRMD": {
        "DRMD_SCHEMA_VERSION",
        "DRMD_DOCUMENT_TITLE",
        "UUID",
        "VERSION",
        "DRMD_VALIDITY_TYPE",
        "DRMD_PRODUCER",
        "DRMD_INTENDED_USE",
        "DRMD_STORAGE_INFORMATION",
        "DRMD_HANDLING_INSTRUCTIONS",
    },
    "DRMD_PRODUCER": {"$NAME", "DRMD_CONTACT_NAME"},
    "DRMD_RESP_PERSON": {"$NAME"},
    "DRMD_IDENTIFIER": {"DRMD_SCHEME", "DRMD_IDENTIFIER_VALUE"},
    "SAMPLE.REFERENCE_MATERIAL": {"$NAME", "BAM_OE"},
    "DRMD_MATERIAL_CLASS": {"DRMD_SCHEME", "DRMD_CLASS_ID"},
    "DRMD_PROPERTY_SET": {"$NAME"},
    "DRMD_RESULT": {"$NAME"},
    "DRMD_QUANTITY": {"DRMD_VALUE_TYPE"},
    "DRMD_PROCEDURE": {"$NAME"},
    "DRMD_METADATA": set(),
    "DRMD_STATEMENT": set(),
    "DRMD_FILE": {"DRMD_FILE_NAME", "DRMD_MIME_TYPE"},
    "DRMD_TRANSLATION": {
        "DRMD_LANGUAGE",
        "DRMD_TARGET_PROPERTY",
        "DRMD_TRANSLATED_TEXT",
    },
}

# Enumerations of drmd.xsd and its supporting schemas, as written in the XML documents
SCHEMA_ENUMERATIONS = {
    "DRMD_DOCUMENT_TITLE": [
        "productInformationSheet",
        "referenceMaterialCertificate",
    ],
    "DRMD_REF_TYPE": ["basic_certificateIdentification", "basic_measuredValue"],
    "DRMD_CONFORMITY": [
        "pass",
        "fail",
        "conditionalPass",
        "conditionalFail",
        "noPass",
        "noFail",
    ],
    "DRMD_VALIDITY_TYPE": ["untilRevoked", "timeAfterDispatch", "specificTime"],
    "DRMD_UNCERTAINTY_TYPE": ["standardMU", "expandedMU", "coverageIntervalMU"],
    "DRMD_VALUE_TYPE": [
        "si:real",
        "si:hybrid",
        "si:constant",
        "si:realListXMLList",
        "dcc:noQuantity",
        "dcc:charsXMLList",
    ],
    "DRMD_QUANTITY_ROLE": [
        "data",
        "minimumSampleSize",
        "itemQuantities",
        "usedMethodQuantities",
    ],
}


def _bilingual(text: str) -> bool:
    parts = text.split("//")
    return len(parts) == 2 and all(part.strip() for part in parts)


def _assignments(cls) -> dict:
    """Property assignments defined in the class itself (not inherited)."""
    return {
        name: attr
        for name, attr in vars(cls).items()
        if type(attr).__name__ == "PropertyTypeAssignment"
    }


def _other_datamodel_properties() -> dict[str, list]:
    """Property assignments of all object types outside the DRMD folder, by code."""
    found: dict[str, list] = {}
    modules = [importlib.import_module("bam_masterdata.datamodel.object_types")]
    for info in pkgutil.walk_packages(
        datamodel_package.__path__, datamodel_package.__name__ + "."
    ):
        if info.name.endswith(".object_types") and ".drmd." not in info.name:
            modules.append(importlib.import_module(info.name))
    for module in modules:
        for cls in _classes(module, ObjectType):
            for prop in _assignments(cls).values():
                found.setdefault(prop.code, []).append(prop)
    return found


def _definition(prop) -> tuple:
    return (
        prop.data_type,
        prop.property_label,
        prop.description,
        prop.vocabulary_code,
        prop.object_code,
    )


@pytest.mark.parametrize("cls", DRMD_OBJECT_TYPES, ids=lambda c: c.defs.code)
def test_object_type_conventions(cls):
    code = cls.defs.code
    assert code == code.upper()
    assert _bilingual(cls.defs.description)
    assert cls.defs.generated_code_prefix == cls.defs.generated_code_prefix.upper()
    codes = [prop.code for prop in cls().properties]
    assert len(codes) == len(set(codes)), "a property is assigned twice"
    assert "$NAME" in codes
    assert "$XMLCOMMENTS" in codes
    # BFO/IAO transition note: every class carries an ontology mapping comment
    source = inspect.getsource(drmd_object_types)
    assert re.search(
        rf"# Ontology mapping \(BFO/IAO transition\): .*\nclass {cls.__name__}\(",
        source,
    )


def test_generated_code_prefixes_are_unique():
    prefixes = [cls.defs.generated_code_prefix for cls in DRMD_OBJECT_TYPES]
    assert len(prefixes) == len(set(prefixes))


@pytest.mark.parametrize("cls", DRMD_OBJECT_TYPES, ids=lambda c: c.defs.code)
def test_mandatory_properties(cls):
    mandatory = {prop.code for prop in cls().properties if prop.mandatory}
    assert mandatory == MANDATORY[cls.defs.code]


def test_new_property_types_are_bilingual_and_not_defined_elsewhere():
    others = _other_datamodel_properties()
    for cls in DRMD_OBJECT_TYPES:
        for prop in _assignments(cls).values():
            if prop.code in REUSED_PROPERTY_TYPES:
                continue
            assert prop.code.startswith("DRMD_"), prop.code
            assert prop.code not in others, f"{prop.code} already exists"
            assert _bilingual(prop.description), prop.code


def test_reused_property_types_keep_their_definition():
    others = _other_datamodel_properties()
    for cls in DRMD_OBJECT_TYPES:
        for prop in _assignments(cls).values():
            if prop.code not in REUSED_PROPERTY_TYPES:
                continue
            assert prop.code in others, f"{prop.code} is not in the BAM datamodel"
            existing = {_definition(p) for p in others[prop.code]}
            assert _definition(prop) in existing, prop.code


def test_shared_property_types_have_one_definition():
    definitions: dict[str, set] = {}
    for cls in DRMD_OBJECT_TYPES:
        for prop in _assignments(cls).values():
            definitions.setdefault(prop.code, set()).add(_definition(prop))
    assert {code: d for code, d in definitions.items() if len(d) > 1} == {}


def test_sections_follow_the_bam_order():
    for cls in DRMD_OBJECT_TYPES:
        sections = [prop.section for prop in cls().properties]
        own = [prop.section for prop in _assignments(cls).values()]
        for section in own:
            assert re.fullmatch(
                r"([A-Z][a-z]*|[A-Z]+)( ([A-Z][a-z]*|[A-Z]+))*", section
            )
        for current, following in zip(sections, sections[1:]):
            if current == "Additional Information":
                assert following in ("Additional Information", "Comments")


@pytest.mark.parametrize("vocabulary", DRMD_VOCABULARIES, ids=lambda v: v.defs.code)
def test_vocabulary_conventions(vocabulary):
    code = vocabulary.defs.code
    assert code == code.upper()
    assert _bilingual(vocabulary.defs.description)
    terms = vocabulary().terms
    for term in terms:
        assert re.fullmatch(r"[A-Z0-9_]+", term.code)
        assert len(term.code) <= 50
        assert _bilingual(term.description)
    assert len({t.label for t in terms}) == len(terms)
    # the labels are exactly the XML tokens of the schema, in schema order
    assert [t.label for t in terms] == SCHEMA_ENUMERATIONS[code]


def _enumeration(path: Path, type_name: str) -> list[str]:
    root = ET.parse(path).getroot()
    xs = "{http://www.w3.org/2001/XMLSchema}"
    for simple_type in root.iter(f"{xs}simpleType"):
        if simple_type.get("name") == type_name:
            return [e.get("value") for e in simple_type.iter(f"{xs}enumeration")]
    raise KeyError(type_name)


@pytest.mark.skipif(
    not os.environ.get(SCHEMA_DIR_VARIABLE),
    reason=f"set {SCHEMA_DIR_VARIABLE} to the DRMD schema repository",
)
def test_vocabularies_match_the_schema_files():
    folder = Path(os.environ[SCHEMA_DIR_VARIABLE])
    assert (
        _enumeration(folder / "drmd.xsd", "titleOfDocumentType")
        == SCHEMA_ENUMERATIONS["DRMD_DOCUMENT_TITLE"]
    )
    assert (
        _enumeration(folder / "drmd.xsd", "refTypesType")
        == SCHEMA_ENUMERATIONS["DRMD_REF_TYPE"]
    )
    assert (
        _enumeration(
            folder / "supporting" / "dcc.xsd", "stringConformityStatementStatusType"
        )
        == SCHEMA_ENUMERATIONS["DRMD_CONFORMITY"]
    )


def test_masterdata_checker_accepts_the_drmd_folder():
    checker = MasterdataChecker()
    checker.load_current_model(datamodel_dir=str(DATAMODEL_DIR))
    checker.load_new_entities(source=str(DRMD_DIR))
    results = checker.check(mode="individual")

    messages = []

    def collect(node):
        if isinstance(node, dict):
            for key, child in node.items():
                if key == "_log_msgs":
                    messages.extend(child)
                else:
                    collect(child)

    collect(results)
    # the only messages are the deprecation warnings for $ANNOTATIONS_STATE, which
    # SAMPLE.REFERENCE_MATERIAL inherits from SAMPLE
    assert messages
    for level, message in messages:
        assert level == "warning"
        assert "$ANNOTATIONS_STATE is deprecated" in message
