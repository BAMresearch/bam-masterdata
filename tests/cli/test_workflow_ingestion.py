import json
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

from bam_masterdata.cli.run_parser import RunParsers, RunParsersWithTransactions
from bam_masterdata.datamodel.v1.activities import GeometryOptimization, WorkflowRun
from bam_masterdata.datamodel.v1.entities import SimulatedSystem, WorkflowDefinition


@pytest.fixture(params=[RunParsers, RunParsersWithTransactions])
def runner(request):
    runner = request.param.__new__(request.param)
    runner.openbis = MagicMock()
    runner.openbis.get_object.side_effect = ValueError("Object not found")
    runner.openbis.new_object.side_effect = lambda **kwargs: SimpleNamespace(
        identifier=f"/SPACE/PROJECT/{kwargs['code']}", save=MagicMock()
    )
    runner.collection = SimpleNamespace(
        attached_objects={}, destinations={}, relationships={}
    )
    runner.space = SimpleNamespace(code="SPACE")
    runner.project = SimpleNamespace(code="PROJECT")
    runner.collection_name = ""
    runner.workflow_resolver = None
    runner.logger = MagicMock()
    runner.parsing = MagicMock()
    runner._save_datasets = MagicMock()
    runner._attach_datasets = MagicMock()
    return runner


def link(identifier, selector=None):
    return {
        "name": "configuration",
        "target": {"kind": "object", "identifier": identifier, "selector": selector},
    }


def test_invalid_workflow_rejected_before_any_object_write(runner):
    run = GeometryOptimization(code="OPT", name="Relaxation")
    run.workflow_graph = {"schema_version": "1", "inputs": [link("MISSING")]}
    runner.collection.attached_objects = {
        "first": SimulatedSystem(code="SYS", name="Initial structure"),
        "last": run,
    }
    with pytest.raises(ValueError):
        runner.run()
    runner.openbis.new_object.assert_not_called()
    runner.openbis.new_transaction.assert_not_called()
    runner._save_datasets.assert_not_called()


def test_same_batch_references_are_validated_and_persisted_as_durable_paths(runner):
    system = SimulatedSystem(code="SYS", name="Initial structure")
    system.n_particles = 2
    run = GeometryOptimization(code="OPT", name="Relaxation")
    run.workflow_graph = {
        "schema_version": "1",
        "inputs": [link("local-system", "/n_particles")],
    }
    runner.collection.attached_objects = {"local-run": run, "local-system": system}
    runner.run()
    props = next(
        call.kwargs["props"]
        for call in runner.openbis.new_object.call_args_list
        if call.kwargs["code"] == "OPT"
    )
    graph = json.loads(props["workflow_graph"])
    assert graph["inputs"][0]["target"]["identifier"] == "/SPACE/PROJECT/SYS"
    assert graph["inputs"][0]["target"]["selector"] == "/n_particles"


def test_missing_selector_is_not_treated_as_resolved(runner):
    run = WorkflowRun(code="RUN", name="Workflow")
    run.workflow_graph = {"schema_version": "1", "inputs": [link("SYS", "/missing")]}
    runner.collection.attached_objects = {
        "run": run,
        "system": SimulatedSystem(code="SYS", name="System"),
    }
    with pytest.raises(ValueError):
        runner.run()
    runner.openbis.new_object.assert_not_called()


def test_recursive_nested_workflows_are_rejected_before_writes(runner):
    a, b = WorkflowRun(code="A", name="A"), WorkflowRun(code="B", name="B")
    for obj, target in ((a, "B"), (b, "A")):
        obj.workflow_graph = {
            "schema_version": "1",
            "tasks": [
                {
                    "kind": "reference",
                    "id": "nested",
                    "name": "nested",
                    "relation": "contains",
                    "target": {"kind": "object", "identifier": target},
                }
            ],
        }
    runner.collection.attached_objects = {"a": a, "b": b}
    with pytest.raises(ValueError):
        runner.run()
    runner.openbis.new_object.assert_not_called()


def test_unknown_specification_version_rejected_before_writes(runner):
    definition = WorkflowDefinition(code="PLAN", name="Plan")
    definition.workflow_specification = {"schema_version": "999"}
    runner.collection.attached_objects = {"plan": definition}
    with pytest.raises(ValueError):
        runner.run()
    runner.openbis.new_object.assert_not_called()


def test_existing_json_property_selectors_match_batch_objects(runner):
    persisted = MagicMock()
    persisted.identifier = "/SPACE/PROJECT/SYS"
    persisted.type.code = "SIMULATED_SYSTEM"
    persisted.props.all.return_value = {
        "$name": "System",
        "lattice_vectors": "[[1, 0, 0], [0, 1, 0], [0, 0, 1]]",
    }

    def get_object(identifier):
        if identifier == persisted.identifier:
            return persisted
        raise ValueError("Object not found")

    runner.openbis.get_object.side_effect = get_object
    run = WorkflowRun(code="RUN", name="Workflow")
    run.workflow_graph = {
        "schema_version": "1",
        "inputs": [
            link(persisted.identifier, "/lattice_vectors/0"),
            {
                "name": "label",
                "target": {
                    "kind": "object",
                    "identifier": persisted.identifier,
                    "selector": "/name",
                },
            },
        ],
    }
    runner.collection.attached_objects = {"run": run}
    runner.run()
    runner.openbis.new_object.assert_called_once()


def test_definition_reference_is_checked_without_a_graph(runner):
    run = WorkflowRun(code="RUN", name="Workflow")
    run.workflow_definition = SimulatedSystem(code="SYS", name="Wrong type")
    runner.collection.attached_objects = {"run": run, "wrong": run.workflow_definition}
    with pytest.raises(ValueError, match="must target WORKFLOW_DEFINITION"):
        runner.run()
    runner.openbis.new_object.assert_not_called()


def test_forward_definition_reference_uses_prevalidated_identifier(runner):
    run = WorkflowRun(code="RUN", name="Workflow")
    definition = WorkflowDefinition(code="PLAN", name="Plan")
    definition.workflow_specification = {"schema_version": "1"}
    run.workflow_definition = definition
    runner.collection.attached_objects = {"run": run, "plan": definition}
    runner.run()
    props = runner.openbis.new_object.call_args_list[0].kwargs["props"]
    assert props["workflow_definition"] == "/SPACE/PROJECT/PLAN"
