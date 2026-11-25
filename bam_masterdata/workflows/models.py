"""Versioned workflow instance contracts, independent of openBIS masterdata."""

import re
from datetime import datetime
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

Name = Annotated[str, Field(min_length=1, pattern=r"\S")]


class WorkflowModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class TargetLocator(WorkflowModel):
    """A resource identity plus an optional RFC 6901 JSON pointer into it."""

    kind: Literal["object", "dataset", "nomad"]
    identifier: Name
    selector: str | None = None

    @field_validator("selector")
    @classmethod
    def valid_pointer(cls, value):
        if value is not None and (
            (value and not value.startswith("/")) or re.search(r"~(?![01])", value)
        ):
            raise ValueError("selector must be an RFC 6901 JSON pointer")
        return value


class Link(WorkflowModel):
    name: Name
    target: TargetLocator


class Port(WorkflowModel):
    name: Name
    description: str | None = None


def _unique_names(items, label):
    names = [item.name for item in items]
    if len(set(names)) != len(names):
        raise ValueError(f"Duplicate {label} names")


class TaskBase(WorkflowModel):
    id: Name
    name: Name
    inputs: list[Link] = Field(default_factory=list)
    outputs: list[Link] = Field(default_factory=list)

    @model_validator(mode="after")
    def unique_ports(self):
        _unique_names(self.inputs, "input")
        _unique_names(self.outputs, "output")
        return self


class ExecutedTask(TaskBase):
    """An actual recorded step; absent provenance is not inferred."""

    kind: Literal["execution"]
    function: TargetLocator | None = None
    status: Literal["running", "completed", "failed", "aborted"] | None = None
    start: datetime | None = None
    end: datetime | None = None

    @model_validator(mode="after")
    def ordered_times(self):
        if self.start is not None and self.end is not None:
            try:
                if self.end < self.start:
                    raise ValueError("Task end precedes its start")
            except TypeError as exc:
                raise ValueError(
                    "Task timestamps must have comparable time zones"
                ) from exc
        return self


class TaskReference(TaskBase):
    """A reference to an existing execution, not a second execution event."""

    kind: Literal["reference"]
    target: TargetLocator
    relation: Literal["reference", "contains"] = "reference"


Task = Annotated[ExecutedTask | TaskReference, Field(discriminator="kind")]


class Dependency(WorkflowModel):
    source: Name
    target: Name


class Connection(WorkflowModel):
    # None denotes the workflow boundary: source=input, target=output.
    source_task: Name | None = None
    source_port: Name
    target_task: Name | None = None
    target_port: Name


def _check_structure(tasks, inputs, outputs, dependencies, connections):
    ids = [task.id for task in tasks]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate task IDs")
    by_id = {task.id: task for task in tasks}
    _unique_names(inputs, "workflow input")
    _unique_names(outputs, "workflow output")
    edges = {task_id: set() for task_id in ids}
    for dependency in dependencies:
        if dependency.source not in by_id or dependency.target not in by_id:
            raise ValueError("Dependency references an unknown task")
        edges[dependency.source].add(dependency.target)
    for connection in connections:
        if connection.source_task is None:
            source_ports = inputs
        elif connection.source_task in by_id:
            source_ports = by_id[connection.source_task].outputs
        else:
            raise ValueError("Connection references an unknown source task")
        if connection.target_task is None:
            target_ports = outputs
        elif connection.target_task in by_id:
            target_ports = by_id[connection.target_task].inputs
        else:
            raise ValueError("Connection references an unknown target task")
        if connection.source_port not in {port.name for port in source_ports}:
            raise ValueError("Connection references an unknown source port")
        if connection.target_port not in {port.name for port in target_ports}:
            raise ValueError("Connection references an unknown target port")
        if connection.source_task is not None and connection.target_task is not None:
            edges[connection.source_task].add(connection.target_task)
    incoming = dict.fromkeys(ids, 0)
    for successors in edges.values():
        for successor in successors:
            incoming[successor] += 1
    ready = [task_id for task_id, count in incoming.items() if count == 0]
    processed = 0
    while ready:
        task_id = ready.pop()
        processed += 1
        for successor in edges[task_id]:
            incoming[successor] -= 1
            if incoming[successor] == 0:
                ready.append(successor)
    if processed != len(ids):
        raise ValueError("Cyclic task dependencies")


class WorkflowGraph(WorkflowModel):
    schema_version: Literal["1"]
    inputs: list[Link] = Field(default_factory=list)
    outputs: list[Link] = Field(default_factory=list)
    tasks: list[Task] = Field(default_factory=list)
    dependencies: list[Dependency] = Field(default_factory=list)
    connections: list[Connection] = Field(default_factory=list)

    @model_validator(mode="after")
    def valid_structure(self):
        _check_structure(
            self.tasks, self.inputs, self.outputs, self.dependencies, self.connections
        )
        return self


class FunctionSpecification(WorkflowModel):
    schema_version: Literal["1"]
    inputs: list[Port] = Field(default_factory=list)
    outputs: list[Port] = Field(default_factory=list)

    @model_validator(mode="after")
    def unique_ports(self):
        _unique_names(self.inputs, "input")
        _unique_names(self.outputs, "output")
        return self


class PlannedTask(WorkflowModel):
    id: Name
    name: Name
    function: TargetLocator
    inputs: list[Port] = Field(default_factory=list)
    outputs: list[Port] = Field(default_factory=list)

    @model_validator(mode="after")
    def unique_ports(self):
        _unique_names(self.inputs, "input")
        _unique_names(self.outputs, "output")
        return self


class WorkflowSpecification(WorkflowModel):
    schema_version: Literal["1"]
    inputs: list[Port] = Field(default_factory=list)
    outputs: list[Port] = Field(default_factory=list)
    tasks: list[PlannedTask] = Field(default_factory=list)
    dependencies: list[Dependency] = Field(default_factory=list)
    connections: list[Connection] = Field(default_factory=list)

    @model_validator(mode="after")
    def valid_structure(self):
        _check_structure(
            self.tasks, self.inputs, self.outputs, self.dependencies, self.connections
        )
        return self
