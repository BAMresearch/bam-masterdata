import json

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
from bam_masterdata.datamodel.v1.base_objects import Activity
from bam_masterdata.metadata.definitions import ObjectTypeDef
from bam_masterdata.metadata.entities import ObjectType

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
def test_activity_types_can_be_instantiated_and_exported(cls):
    obj = cls()
    assert isinstance(obj, Activity)
    assert isinstance(obj, ObjectType)
    assert isinstance(cls.defs, ObjectTypeDef)
    assert cls.defs.code
    assert cls.defs.description.strip()

    exported = obj.model_to_dict()
    assert exported["defs"]["code"] == cls.defs.code
    assert json.loads(obj.model_to_json()) == exported


@pytest.mark.parametrize(
    "child, parent",
    [
        (Computation, Activity),
        (Analysis, Computation),
        (CreepTestDataProcessing, Analysis),
        (Simulation, Computation),
        (Experiment, Activity),
        (Processing, Experiment),
        (Measurement, Experiment),
        (Calibration, Experiment),
        (Synthesis, Experiment),
        (Test, Experiment),
    ],
)
def test_activity_hierarchy(child, parent):
    assert issubclass(child, parent)


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
    assert properties["name"].code == "$NAME"
    assert properties["inputs"].object_code == "ENTITY"
    assert properties["outputs"].object_code == "ENTITY"

    # Flattened export should contain every inherited assignment exactly once.
    property_codes = [prop.code for prop in obj.properties]
    assert len(property_codes) == len(set(property_codes))
    assert {prop.code for prop in properties.values()} == set(property_codes)


@pytest.mark.parametrize(
    "cls", [Computation, Analysis, CreepTestDataProcessing, Simulation]
)
def test_computations_inherit_computation_metadata(cls):
    props = cls()._property_metadata
    assert props["software"].object_code == "SOFTWARE"
    assert props["computational_method"].object_code == "COMPUTATIONAL_METHOD"
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
    assert props["automated_workflow"].data_type == "BOOLEAN"


def test_simulation_execution_metadata():
    props = Simulation()._property_metadata
    for name in (
        "walltime",
        "core_time",
        "n_cores",
        "n_gpus",
        "n_threads",
        "hpc_job_queue",
        "hpc_job_id",
    ):
        assert name in props
        assert props[name].section == "Execution Details"
    assert props["walltime"].units == "h"
    assert props["core_time"].units == "h"
    assert props["simulated_system"].object_code == "SIMULATED_SYSTEM"


@pytest.mark.parametrize(
    "cls", [Experiment, Processing, Measurement, Calibration, Synthesis, Test]
)
def test_experiments_inherit_experiment_metadata(cls):
    props = cls()._property_metadata
    assert props["method_name"].data_type == "VARCHAR"
    assert props["location"].object_code == "LOCATION"


def test_calibration_metadata():
    props = Calibration()._property_metadata
    assert props["calibration_date"].data_type == "DATE"
    assert props["accredited_calibration_lab"].data_type == "BOOLEAN"
    assert props["calibration_certificate_number"].data_type == "VARCHAR"


def test_legacy_mapping_is_recorded_for_migrated_types():
    assert "COMPUTATIONAL_ANALYSIS:v0" in Computation.defs.prev_versions
    assert "PYIRON_JOB:v0" in Simulation.defs.prev_versions
    assert "SAMPLE_PRETREATMENT:v0" in Processing.defs.prev_versions
    assert "CALIBRATION:v0" in Calibration.defs.prev_versions


def test_instance_values_serialize():
    simulation = Simulation()
    simulation.name = "Silicon calculation"
    simulation.walltime = 2.5
    simulation.n_cores = 16

    assert simulation.to_dict() == {
        "name": "Silicon calculation",
        "walltime": 2.5,
        "n_cores": 16,
    }
