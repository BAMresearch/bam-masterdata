import pytest
from pydantic import ValidationError

from bam_masterdata.workflows.models import (
    ExecutedTask,
    FunctionSpecification,
    TargetLocator,
    WorkflowGraph,
    WorkflowSpecification,
)


def execution(task_id="step", **kwargs):
    return {"kind": "execution", "id": task_id, "name": task_id, **kwargs}


def test_graph_roundtrip_preserves_named_links_and_selectors():
    target = {"kind": "dataset", "identifier": "trajectory", "selector": "/frames/0"}
    graph = WorkflowGraph.model_validate(
        {
            "schema_version": "1",
            "tasks": [execution(inputs=[{"name": "configuration", "target": target}])],
        }
    )
    assert graph.tasks[0].inputs[0].target.selector == "/frames/0"
    assert WorkflowGraph.model_validate_json(graph.model_dump_json()) == graph


@pytest.mark.parametrize("selector", ["frames/0", "/bad~2", "/trailing~"])
def test_invalid_json_pointer(selector):
    with pytest.raises(ValidationError, match="RFC 6901"):
        TargetLocator(kind="dataset", identifier="trajectory", selector=selector)


@pytest.mark.parametrize("version", [None, "2", 1])
def test_graph_requires_supported_explicit_version(version):
    value = {} if version is None else {"schema_version": version}
    with pytest.raises(ValidationError):
        WorkflowGraph.model_validate(value)


def test_execution_and_reference_are_exclusive():
    with pytest.raises(ValidationError, match="Extra inputs"):
        WorkflowGraph.model_validate(
            {
                "schema_version": "1",
                "tasks": [execution(target={"kind": "object", "identifier": "RUN"})],
            }
        )


def test_duplicate_task_ids_are_rejected():
    with pytest.raises(ValidationError, match="Duplicate task IDs"):
        WorkflowGraph(schema_version="1", tasks=[execution(), execution()])


def test_unknown_dependency_and_cycles_are_rejected():
    for dependencies, match in [
        ([{"source": "a", "target": "missing"}], "unknown task"),
        ([{"source": "a", "target": "b"}, {"source": "b", "target": "a"}], "Cyclic"),
    ]:
        with pytest.raises(ValidationError, match=match):
            WorkflowGraph(
                schema_version="1",
                tasks=[execution("a"), execution("b")],
                dependencies=dependencies,
            )


def test_invalid_connection_ports_are_rejected():
    with pytest.raises(ValidationError, match="unknown source port"):
        WorkflowGraph(
            schema_version="1",
            tasks=[execution()],
            connections=[
                {"source_task": "step", "source_port": "missing", "target_port": "out"}
            ],
        )


def test_task_times_must_be_ordered():
    with pytest.raises(ValidationError, match="precedes"):
        ExecutedTask(
            **execution(start="2026-01-02T00:00:00Z", end="2026-01-01T00:00:00Z")
        )


def test_function_and_definition_validate_prescribed_port_names():
    with pytest.raises(ValidationError, match="Duplicate input"):
        FunctionSpecification(schema_version="1", inputs=[{"name": "x"}, {"name": "x"}])
    with pytest.raises(ValidationError, match="unknown target port"):
        WorkflowSpecification(
            schema_version="1",
            inputs=[{"name": "x"}],
            connections=[{"source_port": "x", "target_port": "missing"}],
        )


def test_long_recorded_trajectory_does_not_use_python_recursion():
    task_ids = [str(i) for i in range(1500)]
    value = WorkflowGraph(
        schema_version="1",
        tasks=[execution(task_id) for task_id in task_ids],
        dependencies=[
            {"source": first, "target": second}
            for first, second in zip(task_ids, task_ids[1:])
        ],
    )
    assert len(value.tasks) == 1500
