"""Resolve and validate workflow instance references before ingestion or export."""

from collections.abc import Callable, Mapping
from dataclasses import dataclass
from typing import Any, Literal

from bam_masterdata.workflows.models import (
    ExecutedTask,
    FunctionSpecification,
    TargetLocator,
    TaskReference,
    WorkflowGraph,
    WorkflowSpecification,
)


@dataclass(frozen=True)
class ResolvedTarget:
    """Resolved resource root. ``canonical_id`` identifies aliases of that resource."""

    canonical_id: str
    value: Any
    object_type: str | None = None
    workflow_graph: WorkflowGraph | dict | str | None = None
    category: Literal["data", "execution", "function", "definition"] = "data"


Resolver = Callable[[TargetLocator], ResolvedTarget]


def select_value(value: Any, selector: str | None) -> Any:
    """Resolve an RFC 6901 pointer; missing paths fail instead of becoming null."""
    if not selector:
        return value
    for segment in selector[1:].split("/"):
        key = segment.replace("~1", "/").replace("~0", "~")
        if isinstance(value, Mapping) and key in value:
            value = value[key]
        elif isinstance(value, (list, tuple)) and (
            key == "0" or (key.isascii() and key.isdigit() and not key.startswith("0"))
        ):
            try:
                value = value[int(key)]
            except IndexError as exc:
                raise ValueError(f"Unresolved selector {selector!r}") from exc
        else:
            raise ValueError(f"Unresolved selector {selector!r}")
    return value


def resolve_target(locator: TargetLocator, resolver: Resolver) -> ResolvedTarget:
    try:
        result = resolver(locator)
    except Exception as exc:
        raise ValueError(
            f"Unresolved {locator.kind} target {locator.identifier!r}"
        ) from exc
    if not isinstance(result, ResolvedTarget) or not result.canonical_id:
        raise ValueError(f"Resolver did not resolve target {locator.identifier!r}")
    select_value(result.value, locator.selector)
    return result


def validate_function_specification(value) -> FunctionSpecification:
    return (
        FunctionSpecification.model_validate_json(value)
        if isinstance(value, str)
        else FunctionSpecification.model_validate(value)
    )


def _validate_function(locator, resolver, inputs, outputs):
    target = resolve_target(locator, resolver)
    if target.category != "function" and target.object_type != "WORKFLOW_FUNCTION":
        raise ValueError(
            "Workflow function reference must resolve to a workflow function"
        )
    if locator.selector and locator.kind != "nomad":
        raise ValueError("Workflow function reference must identify the whole function")
    specification = (
        target.value.get("function_specification")
        if isinstance(target.value, Mapping)
        else None
    )
    if specification is not None:
        spec = validate_function_specification(specification)
        if {port.name for port in inputs} != {port.name for port in spec.inputs}:
            raise ValueError("Task input ports do not match the workflow function")
        if {port.name for port in outputs} != {port.name for port in spec.outputs}:
            raise ValueError("Task output ports do not match the workflow function")


def validate_workflow_specification(value, resolver: Resolver) -> WorkflowSpecification:
    specification = (
        WorkflowSpecification.model_validate_json(value)
        if isinstance(value, str)
        else WorkflowSpecification.model_validate(value)
    )
    for task in specification.tasks:
        _validate_function(task.function, resolver, task.inputs, task.outputs)
    return specification


def validate_workflow_graph(
    value, resolver: Resolver, root_identifier: str | None = None
) -> WorkflowGraph:
    """Validate graph shape, data links, function ports and nested containment.

    ``resolver`` must perform actual resource lookup and return the resource root.
    References may reuse an execution in multiple graphs; containment must be acyclic.
    No network or storage writes are performed here.
    """
    graph = (
        WorkflowGraph.model_validate_json(value)
        if isinstance(value, str)
        else WorkflowGraph.model_validate(value)
    )
    visited = set()
    active = set()
    containment = {}

    def visit(current, identity):
        if identity in visited or identity in active:
            return
        active.add(identity)
        containment.setdefault(identity, set())
        by_id = {task.id: task for task in current.tasks}
        endpoint_identity = {}
        for owner_id, owner in [(None, current), *by_id.items()]:
            for direction in ("inputs", "outputs"):
                for link in getattr(owner, direction):
                    resolved = resolve_target(link.target, resolver)
                    endpoint_identity[(owner_id, direction, link.name)] = (
                        resolved.canonical_id,
                        link.target.selector or "",
                    )
        for connection in current.connections:
            source_direction = "inputs" if connection.source_task is None else "outputs"
            target_direction = "outputs" if connection.target_task is None else "inputs"
            source = endpoint_identity[
                (connection.source_task, source_direction, connection.source_port)
            ]
            target = endpoint_identity[
                (connection.target_task, target_direction, connection.target_port)
            ]
            if source != target:
                raise ValueError(
                    "Connected ports must identify the same data target and selector"
                )
        for task in current.tasks:
            if isinstance(task, ExecutedTask) and task.function is not None:
                _validate_function(task.function, resolver, task.inputs, task.outputs)
            elif isinstance(task, TaskReference):
                resolved = resolve_target(task.target, resolver)
                if resolved.category != "execution" and resolved.workflow_graph is None:
                    raise ValueError("Task reference must resolve to an execution")
                if task.target.selector and task.target.kind != "nomad":
                    raise ValueError("Task reference must identify a whole execution")
                if task.relation == "contains":
                    containment[identity].add(
                        (resolved.canonical_id, task.target.selector or "")
                    )
                if resolved.workflow_graph is not None:
                    nested = (
                        WorkflowGraph.model_validate_json(resolved.workflow_graph)
                        if isinstance(resolved.workflow_graph, str)
                        else WorkflowGraph.model_validate(resolved.workflow_graph)
                    )
                    # A reference may expose a subset or use different labels,
                    # but matching boundary names cannot contradict the execution.
                    for direction in ("inputs", "outputs"):
                        nested_ports = {
                            link.name: link for link in getattr(nested, direction)
                        }
                        for link in getattr(task, direction):
                            if link.name not in nested_ports:
                                continue
                            target = nested_ports[link.name].target
                            boundary = resolve_target(target, resolver)
                            if endpoint_identity[(task.id, direction, link.name)] != (
                                boundary.canonical_id,
                                target.selector or "",
                            ):
                                raise ValueError(
                                    "Task reference contradicts the referenced workflow boundary"
                                )
                    visit(nested, (resolved.canonical_id, task.target.selector or ""))
        active.remove(identity)
        visited.add(identity)

    visit(graph, (root_identifier or "<root>", ""))
    pending, finished = set(), set()

    def visit_containment(identity):
        if identity in pending:
            raise ValueError("Recursive workflow containment")
        if identity in finished:
            return
        pending.add(identity)
        for child in containment.get(identity, ()):
            visit_containment(child)
        pending.remove(identity)
        finished.add(identity)

    for identity in containment:
        visit_containment(identity)
    return graph
