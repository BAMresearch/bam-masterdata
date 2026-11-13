import json

import pytest

from bam_masterdata.datamodel.v1.activities import Computation, Simulation
from bam_masterdata.datamodel.v1.base_objects import Entity
from bam_masterdata.datamodel.v1.entities import (
    HPC,
    ComputationalMethod,
    Context,
    Device,
    InteratomicPotential,
    MaterialEntity,
    ParameterSet,
    Pseudopotential,
    SimulatedSystem,
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
    InteratomicPotential,
    SimulatedSystem,
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
        (Pseudopotential, ParameterSet),
        (InteratomicPotential, ParameterSet),
        (SimulatedSystem, Context),
        (ComputationalMethod, Context),
        (HPC, Device),
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


@pytest.mark.parametrize(
    "cls, activity, property_name",
    [
        (Software, Computation, "software"),
        (SimulatedSystem, Simulation, "simulated_system"),
        (ComputationalMethod, Computation, "computational_method"),
    ],
)
def test_object_types_referenced_by_activities(cls, activity, property_name):
    assert activity()._property_metadata[property_name].object_code == cls.defs.code


def test_computational_method_has_no_subtypes():
    # OBJECT properties only accept objects of the exact type they point to
    assert ComputationalMethod.__subclasses__() == []
