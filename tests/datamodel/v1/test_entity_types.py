import pytest

from bam_masterdata.datamodel.v1.activities import Computation, Simulation
from bam_masterdata.datamodel.v1.entities import (
    HPC,
    CalculationDatum,
    ComputationalMethod,
    Context,
    DataItem,
    InteratomicPotential,
    MaterialEntity,
    MeasurementDatum,
    Pseudopotential,
    SimulatedSystem,
    Software,
)

ENTITY_CLASSES = [
    Context,
    MaterialEntity,
    Software,
    Pseudopotential,
    InteratomicPotential,
    SimulatedSystem,
    ComputationalMethod,
    HPC,
    DataItem,
    CalculationDatum,
    MeasurementDatum,
]


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
        (HPC, Computation, "executed_on"),
    ],
)
def test_object_types_referenced_by_activities(cls, activity, property_name):
    assert activity()._property_metadata[property_name].object_code == cls.defs.code
