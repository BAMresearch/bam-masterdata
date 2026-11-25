import pytest

from bam_masterdata.datamodel.v1.activities import (
    Computation,
    GeometryOptimization,
    MolecularDynamics,
    Simulation,
    SinglePointCalculation,
    WorkflowRun,
)
from bam_masterdata.datamodel.v1.entities import (
    Context,
    WorkflowDefinition,
    WorkflowFunction,
)


def test_specifications_are_distinct_from_executions():
    assert issubclass(WorkflowDefinition, Context)
    assert issubclass(WorkflowFunction, Context)
    assert not issubclass(WorkflowDefinition, Computation)
    assert issubclass(WorkflowRun, Computation)
    assert WorkflowRun()._property_metadata["workflow_definition"].object_code == (
        WorkflowDefinition.defs.code
    )


@pytest.mark.parametrize(
    "cls", [SinglePointCalculation, GeometryOptimization, MolecularDynamics]
)
def test_simulation_workflows_retain_execution_properties(cls):
    assert issubclass(cls, WorkflowRun)
    assert not issubclass(cls, Simulation)
    original = Simulation()._property_metadata
    actual = cls()._property_metadata
    for name, prop in original.items():
        assert actual[name] == prop
    assert {"workflow_graph", "workflow_definition"} <= actual.keys()
    assert cls.get_hierarchy() == [
        "ROOT",
        "ACTIVITY",
        "COMPUTATION",
        "WORKFLOW_RUN",
        "SIMULATION_WORKFLOW",
        cls.defs.code,
    ]


def test_generic_simulation_does_not_require_a_workflow():
    assert not issubclass(Simulation, WorkflowRun)
    assert "workflow_graph" not in Simulation()._property_metadata


def test_function_reuses_software_reference():
    assert WorkflowFunction()._property_metadata["software"] == Computation.software
