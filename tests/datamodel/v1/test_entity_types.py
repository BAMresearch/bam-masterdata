import json

import pytest

from bam_masterdata.datamodel.v1.activities import Computation
from bam_masterdata.datamodel.v1.base_objects import Entity
from bam_masterdata.datamodel.v1.entities import (
    HPC,
    ComputationalMethod,
    Context,
    MaterialEntity,
    Pseudopotential,
    Software,
    WorkflowDefinition,
)
from bam_masterdata.metadata.definitions import ObjectTypeDef
from bam_masterdata.metadata.entities import ObjectType

ENTITY_CLASSES = [
    Context,
    MaterialEntity,
    Software,
    WorkflowDefinition,
    Pseudopotential,
    ComputationalMethod,
    HPC,
]


@pytest.mark.parametrize("cls", ENTITY_CLASSES, ids=lambda cls: cls.__name__)
def test_entity_types_can_be_instantiated_and_exported(cls):
    obj = cls()
    assert isinstance(obj, Entity)
    assert isinstance(obj, ObjectType)
    assert isinstance(cls.defs, ObjectTypeDef)
    assert cls.defs.description.strip()

    exported = obj.model_to_dict()
    assert exported["defs"]["code"] == cls.defs.code
    assert json.loads(obj.model_to_json()) == exported


@pytest.mark.parametrize(
    "child, parent",
    [
        (Context, Entity),
        (MaterialEntity, Entity),
        (Software, Context),
        (WorkflowDefinition, Context),
        (Pseudopotential, Context),
        (ComputationalMethod, Context),
        (HPC, MaterialEntity),
    ],
)
def test_entity_hierarchy(child, parent):
    assert issubclass(child, parent)


@pytest.mark.parametrize("cls", ENTITY_CLASSES, ids=lambda cls: cls.__name__)
def test_inherited_properties_are_available(cls):
    obj = cls()
    assert {"name", "description"} <= set(obj._property_metadata)

    property_codes = [prop.code for prop in obj.properties]
    assert len(property_codes) == len(set(property_codes))


def test_shared_property_codes_have_identical_definitions():
    # openBIS property types are global, so assignments sharing a code must agree
    # on everything except the section they are shown in.
    fields = ("data_type", "property_label", "description", "multivalued")
    seen = {}
    for cls in ENTITY_CLASSES:
        for prop in cls().properties:
            definition = tuple(getattr(prop, field) for field in fields)
            assert seen.setdefault(prop.code, definition) == definition, prop.code


@pytest.mark.parametrize(
    "cls, activity, property_name",
    [
        (Software, Computation, "software"),
        (ComputationalMethod, Computation, "computational_method"),
    ],
)
def test_object_types_referenced_by_activities(cls, activity, property_name):
    assert activity()._property_metadata[property_name].object_code == cls.defs.code


def test_computational_method_has_no_subtypes():
    # OBJECT properties only accept objects of the exact type they point to
    assert ComputationalMethod.__subclasses__() == []
