import inspect
import json

import pytest

from bam_masterdata.checker.schema_validator import (
    get_object_types,
    validate_object_references,
    validate_object_type_codes,
)
from bam_masterdata.datamodel.v1 import entities
from bam_masterdata.datamodel.v1 import vocabularies as v1_vocabularies
from bam_masterdata.datamodel.v1.afm import vocabularies as afm_vocabularies
from bam_masterdata.datamodel.v1.afm.object_types import AFMTip, AFMTipBox
from bam_masterdata.datamodel.v1.afm.vocabularies import (
    AFMTipStatus,
    BaseShape,
    PremountedType,
    TipShape,
)
from bam_masterdata.datamodel.v1.entities import PhysicalObject
from bam_masterdata.metadata.definitions import DataType
from bam_masterdata.metadata.entities import ObjectType, VocabularyType

AFM_CLASSES = [AFMTipBox, AFMTip]

AFM_VOCABULARIES = [PremountedType, BaseShape, TipShape, AFMTipStatus]


def _vocabulary_codes(module) -> set[str]:
    return {
        cls.defs.code
        for _, cls in inspect.getmembers(module, inspect.isclass)
        if issubclass(cls, VocabularyType) and cls is not VocabularyType
    }


KNOWN_V1_VOCABULARY_CODES = _vocabulary_codes(v1_vocabularies) | _vocabulary_codes(
    afm_vocabularies
)


@pytest.mark.parametrize("cls", AFM_CLASSES, ids=lambda cls: cls.__name__)
def test_afm_types_instantiate_and_export(cls):
    obj = cls()
    assert cls.defs.description.strip()
    assert cls.defs.description_de.strip()

    exported = obj.model_to_dict()
    assert exported["defs"]["code"] == cls.defs.code
    assert json.loads(obj.model_to_json()) == exported


def test_afm_types_are_discovered_in_v1():
    object_types = get_object_types("v1")
    assert set(AFM_CLASSES) <= set(object_types)
    validate_object_type_codes(object_types)


@pytest.mark.parametrize("cls", AFM_CLASSES, ids=lambda cls: cls.__name__)
def test_afm_types_are_physical_objects(cls):
    assert issubclass(cls, PhysicalObject)


def test_tip_does_not_inherit_from_box():
    # A tip originates from (is contained in) a box; it is not a specialization of it.
    assert not issubclass(AFMTip, AFMTipBox)
    assert not issubclass(AFMTipBox, AFMTip)


@pytest.mark.parametrize("cls", AFM_CLASSES, ids=lambda cls: cls.__name__)
def test_afm_properties_are_consistent(cls):
    obj = cls()
    codes = [prop.code for prop in obj.properties]
    assert len(codes) == len(set(codes))

    for prop in obj.properties:
        assert prop.property_label
        assert prop.description
        assert prop.section
        if prop.data_type == DataType.CONTROLLEDVOCABULARY:
            assert prop.vocabulary_code in KNOWN_V1_VOCABULARY_CODES
        if prop.data_type == DataType.OBJECT:
            assert prop.object_code


@pytest.mark.parametrize("cls", AFM_CLASSES, ids=lambda cls: cls.__name__)
def test_physical_object_properties_are_inherited(cls):
    parent_codes = {prop.code for prop in PhysicalObject().properties}
    assert parent_codes <= {prop.code for prop in cls().properties}


@pytest.mark.parametrize(
    "cls, expected",
    [
        (
            AFMTipBox,
            {
                "RESPONSIBLE_PERSON",
                "MANUFACTURER_INFO",
                "TIP_CLASS",
                "PREMOUNTED_TYPE",
                "BASE_SHAPE",
                "TIP_SHAPE",
                "CANTILEVER_THICKNESS",
                "CANTILEVER_LENGTH",
                "SPRING_CONSTANT_LOW",
                "SPRING_CONSTANT_HIGH",
                "RESONANCE_FREQUENCY_LOW",
                "RESONANCE_FREQUENCY_HIGH",
                "LAB",
                "STORAGE_COMPARTMENT",
                "NUMBER_OF_TIPS",
            },
        ),
        (AFMTip, {"TIP_BOX", "TIP_NUMBER", "TIP_CLASS", "AFM_TIP_STATUS"}),
    ],
    ids=lambda value: value.__name__ if isinstance(value, type) else "",
)
def test_mandatory_properties(cls, expected):
    # $NAME is mandatory on every v1 type and inherited from Root.
    mandatory = {prop.code for prop in cls().properties if prop.mandatory}
    assert mandatory - {"$NAME"} == expected


def test_afm_object_references_resolve():
    classes = [
        cls
        for _, cls in inspect.getmembers(entities, inspect.isclass)
        if issubclass(cls, ObjectType) and cls.__module__ == entities.__name__
    ]
    validate_object_references(classes + AFM_CLASSES)
    assert AFMTip.tip_box.object_code == AFMTipBox.defs.code


def test_responsible_person_override_keeps_parent_metadata():
    box_prop = AFMTipBox.responsible_persons
    parent_prop = PhysicalObject.responsible_persons
    assert box_prop.mandatory is True
    assert parent_prop.mandatory is False
    for field in ("code", "data_type", "object_code", "property_label", "description"):
        assert getattr(box_prop, field) == getattr(parent_prop, field)


def test_tip_class_metadata_is_shared():
    for field in ("code", "data_type", "property_label", "description"):
        assert getattr(AFMTipBox.tip_class, field) == getattr(AFMTip.tip_class, field)


def test_box_values_carry_units():
    assert AFMTipBox.cantilever_length.units == "um"
    assert AFMTipBox.spring_constant_low.units == "N/m"
    assert AFMTipBox.resonance_frequency_low.units == "kHz"
    assert AFMTipBox.tip_radius_low.units == "nm"


def test_tip_instance_values_serialize():
    tip = AFMTip()
    tip.name = "Tip 3"
    tip.tip_number = 3
    tip.tip_class = "F_S09_N_Si"
    tip.cantilever_variant = "B"
    assert tip.to_dict() == {
        "name": "Tip 3",
        "tip_number": 3,
        "tip_class": "F_S09_N_Si",
        "cantilever_variant": "B",
    }


@pytest.mark.parametrize("cls", AFM_VOCABULARIES, ids=lambda cls: cls.__name__)
def test_afm_vocabularies_instantiate_and_export(cls):
    vocabulary = cls()
    assert cls.defs.description.strip()
    assert cls.defs.description_de.strip()

    term_codes = [term.code for term in vocabulary.terms]
    assert term_codes
    assert len(term_codes) == len(set(term_codes))
    for term in vocabulary.terms:
        assert term.label
        assert term.description

    assert vocabulary.model_to_dict()["defs"]["code"] == cls.defs.code


def test_afm_vocabulary_codes_do_not_collide_with_v1_vocabularies():
    assert _vocabulary_codes(afm_vocabularies).isdisjoint(
        _vocabulary_codes(v1_vocabularies)
    )


@pytest.mark.parametrize(
    "cls, expected",
    [
        (PremountedType, {"NON_PROPRIETARY", "NANO_TA", "NANO_IR"}),
        (BaseShape, {"RECTANGULAR", "V_SHAPED", "ELSE"}),
        (TipShape, {"SHARP", "COLLOIDAL", "NONE", "ELSE"}),
        (AFMTipStatus, {"UNUSED", "ACTIVE", "MODIFIED", "BROKEN", "ARCHIVED"}),
    ],
    ids=lambda value: value.__name__ if isinstance(value, type) else "",
)
def test_vocabulary_terms_match_researcher_definitions(cls, expected):
    assert {term.code for term in cls().terms} == expected
