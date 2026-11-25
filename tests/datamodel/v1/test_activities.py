import pytest

from bam_masterdata.datamodel.v1.activities import (
    Analysis,
    Calibration,
    Computation,
    CreepTestDataProcessing,
    Experiment,
    Measurement,
    Processing,
    Simulation,
    Synthesis,
    Test,
)

ACTIVITY_CLASSES = [
    Computation,
    Analysis,
    CreepTestDataProcessing,
    Simulation,
    Experiment,
    Processing,
    Measurement,
    Calibration,
    Synthesis,
    Test,
]


@pytest.mark.parametrize("cls", ACTIVITY_CLASSES, ids=lambda cls: cls.__name__)
def test_inherited_properties_are_available(cls):
    obj = cls()
    properties = obj._property_metadata

    # Every activity should keep the common Root/Activity contract.
    assert {
        "name",
        "description",
        "start_date",
        "end_date",
        "inputs",
        "outputs",
    } <= set(properties)

    # Flattened export should contain every inherited assignment exactly once.
    property_codes = [prop.code for prop in obj.properties]
    assert len(property_codes) == len(set(property_codes))
    assert {prop.code for prop in properties.values()} == set(property_codes)


@pytest.mark.parametrize(
    "cls", [Computation, Analysis, CreepTestDataProcessing, Simulation]
)
def test_computations_inherit_computation_metadata(cls):
    props = cls()._property_metadata
    assert props["computational_method"].multivalued is True


@pytest.mark.parametrize("cls", [Analysis, CreepTestDataProcessing])
def test_analyses_inherit_processing_metadata(cls):
    props = cls()._property_metadata
    assert {
        "primary_data_series",
        "processed_data_series",
        "analysis_procedure",
        "automated_workflow",
    } <= set(props)


def test_instance_values_serialize():
    simulation = Simulation()
    simulation.name = "Silicon calculation"
    simulation.walltime_h = 2.5
    simulation.n_cores = 16

    assert simulation.to_dict() == {
        "name": "Silicon calculation",
        "walltime_h": 2.5,
        "n_cores": 16,
    }
