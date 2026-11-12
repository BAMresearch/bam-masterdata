"""Tests for the DRMD datamodel in `bam_masterdata/datamodel/v0/drmd/`."""

import re

import pytest

from bam_masterdata.checker.schema_validator import (
    get_object_types,
    validate_object_references,
    validate_object_type_codes,
)
from bam_masterdata.datamodel.v0.drmd import object_types as drmd_object_types
from bam_masterdata.datamodel.v0.drmd.object_types import (
    DrmdIdentifier,
    DrmdMaterialClass,
    DrmdProducer,
    DrmdResponsiblePerson,
)
from bam_masterdata.datamodel.v0.drmd.vocabularies import (
    DrmdConformity,
    DrmdDocumentTitle,
    DrmdQuantityRole,
    DrmdUncertaintyType,
    DrmdValidityType,
    DrmdValueType,
    Language,
)
from bam_masterdata.datamodel.v0.object_types import Person, Sample
from bam_masterdata.metadata.definitions import DataType

V0_TYPES = get_object_types("v0")
DRMD_TYPES = [cls for cls in V0_TYPES if cls.__module__ == drmd_object_types.__name__]

# Properties required in both document types (certificate and product information
# sheet) are mandatory; all other requirements depend on the document type.
MANDATORY = {
    "DRMD": {
        "DRMD_DOCUMENT_TITLE",
        "UUID",
        "VERSION",
        "DRMD_VALIDITY_TYPE",
        "DRMD_PRODUCER",
        "DRMD_INTENDED_USE",
        "DRMD_STORAGE_INFORMATION",
        "DRMD_HANDLING_INSTRUCTIONS",
    },
    "PERSON.DRMD_PRODUCER": {"$NAME", "AFFILIATION"},
    "PERSON.DRMD_RESPONSIBLE_PERSON": {"$NAME", "FAMILY_NAME", "AFFILIATION"},
    "DRMD_IDENTIFIER": {"DRMD_SCHEME", "DRMD_IDENTIFIER_VALUE"},
    "DRMD_IDENTIFIER.MATERIAL_CLASS": {"DRMD_SCHEME", "DRMD_IDENTIFIER_VALUE"},
    "SAMPLE.REFERENCE_MATERIAL": {"$NAME", "BAM_OE"},
    "DRMD_PROPERTY_SET": {"$NAME"},
    "DRMD_RESULT": {"$NAME"},
    "DRMD_QUANTITY": {"DRMD_VALUE_TYPE"},
    "DRMD_PROCEDURE": {"$NAME"},
    "DRMD_METADATA": set(),
    "DRMD_STATEMENT": set(),
    "DRMD_FILE": {"DRMD_FILE_NAME", "DRMD_MIME_TYPE"},
}

VOCABULARY_CODES = {
    Language: ["EN", "DE"],
    DrmdDocumentTitle: ["PRODUCT_INFORMATION_SHEET", "REFERENCE_MATERIAL_CERTIFICATE"],
    DrmdValidityType: ["UNTIL_REVOKED", "TIME_AFTER_DISPATCH", "SPECIFIC_TIME"],
    DrmdValueType: [
        "SI_REAL",
        "SI_HYBRID",
        "SI_CONSTANT",
        "SI_REAL_LIST_XML_LIST",
        "DCC_NO_QUANTITY",
        "DCC_CHARS_XML_LIST",
    ],
    DrmdQuantityRole: [
        "RESULT_DATA",
        "MINIMUM_SAMPLE_SIZE",
        "ITEM_QUANTITIES",
        "USED_METHOD_QUANTITIES",
    ],
    DrmdUncertaintyType: ["STANDARD_MU", "EXPANDED_MU", "COVERAGE_INTERVAL_MU"],
    DrmdConformity: [
        "PASS",
        "FAIL",
        "CONDITIONAL_PASS",
        "CONDITIONAL_FAIL",
        "NO_PASS",
        "NO_FAIL",
    ],
}


def test_drmd_types_are_discovered():
    assert {cls.defs.code for cls in DRMD_TYPES} == set(MANDATORY)


def test_v0_codes_and_object_references_are_valid():
    validate_object_type_codes(V0_TYPES)
    validate_object_references(V0_TYPES)


def test_generated_code_prefixes_are_unique():
    prefixes = [cls.defs.generated_code_prefix for cls in V0_TYPES]
    for cls in DRMD_TYPES:
        assert prefixes.count(cls.defs.generated_code_prefix) == 1


@pytest.mark.parametrize("cls", DRMD_TYPES, ids=lambda cls: cls.defs.code)
def test_mandatory_properties(cls):
    mandatory = {prop.code for prop in cls().properties if prop.mandatory}
    assert mandatory == MANDATORY[cls.defs.code]


def test_persons_extend_person():
    person_codes = {prop.code for prop in Person().properties}
    for cls in (DrmdProducer, DrmdResponsiblePerson):
        assert cls.is_subtype_of(Person)
        codes = {prop.code for prop in cls().properties}
        assert person_codes <= codes


def test_material_class_extends_identifier():
    assert DrmdMaterialClass.is_subtype_of(DrmdIdentifier)
    assert [p.code for p in DrmdMaterialClass().properties] == [
        p.code for p in DrmdIdentifier().properties
    ]


def test_controlled_vocabularies_are_defined():
    used = {
        prop.vocabulary_code
        for cls in DRMD_TYPES
        for prop in cls().properties
        if prop.data_type == DataType.CONTROLLEDVOCABULARY
    }
    # SAMPLE.REFERENCE_MATERIAL also has the controlled vocabularies of SAMPLE
    inherited = {prop.vocabulary_code for prop in Sample().properties}
    assert used - inherited == {vocabulary.defs.code for vocabulary in VOCABULARY_CODES}


@pytest.mark.parametrize(
    "vocabulary", VOCABULARY_CODES, ids=lambda vocabulary: vocabulary.defs.code
)
def test_vocabulary_terms(vocabulary):
    terms = vocabulary().terms
    assert [term.code for term in terms] == VOCABULARY_CODES[vocabulary]
    for term in terms:
        # human-readable labels: capitalised words, no XML tokens such as camelCase
        assert re.fullmatch(r"[A-Z][a-z]+( [a-z]+)*", term.label), term.label
        assert term.description
