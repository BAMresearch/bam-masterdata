"""Validate workflow documents before a parser writes any object properties."""

import json
from collections import defaultdict

from bam_masterdata.checker.schema_validator import get_object_types
from bam_masterdata.datamodel.v1.activities import Computation
from bam_masterdata.datamodel.v1.entities import (
    WorkflowDefinition,
    WorkflowFunction,
)
from bam_masterdata.metadata.definitions import PropertyTypeAssignment
from bam_masterdata.metadata.entities import ObjectType
from bam_masterdata.workflows.models import TargetLocator
from bam_masterdata.workflows.validation import (
    ResolvedTarget,
    validate_function_specification,
    validate_workflow_graph,
    validate_workflow_specification,
)

WORKFLOW_DOCUMENTS = {
    "WORKFLOW_GRAPH",
    "WORKFLOW_SPECIFICATION",
    "FUNCTION_SPECIFICATION",
    "WORKFLOW_DEFINITION",
}


def workflow_documents(obj):
    """Return explicitly populated workflow documents, not class assignments."""
    for name, prop in obj._property_metadata.items():
        value = getattr(obj, name, None)
        if (
            prop.code in WORKFLOW_DOCUMENTS
            and value is not None
            and not isinstance(value, PropertyTypeAssignment)
        ):
            yield name, prop.code, value


def prepare_workflow_documents(objects, identifiers, openbis, external_resolver=None):
    """Resolve and validate a batch, returning canonical JSON property values.

    Object references can target this batch or existing openBIS objects. Dataset
    contents and NOMAD archives require an explicit resolver: their existence or
    a syntactically valid path alone does not prove a section selector resolves.
    Nothing in this function writes to openBIS.
    """

    aliases = defaultdict(list)
    for local_id, obj in objects.items():
        for alias in {local_id, obj.code, identifiers[local_id]} - {None}:
            aliases[alias].append((local_id, obj))

    canonical_by_instance = {id(obj): identifiers[key] for key, obj in objects.items()}

    def plain_value(value):
        if isinstance(value, ObjectType):
            if id(value) not in canonical_by_instance:
                sample = openbis.get_object(value.code)
                if sample.type.code != value.defs.code:
                    raise ValueError("Referenced object has an unexpected type")
                return sample.identifier
            return canonical_by_instance[id(value)]
        if isinstance(value, dict):
            return {key: plain_value(item) for key, item in value.items()}
        if isinstance(value, (list, tuple)):
            return [plain_value(item) for item in value]
        return value

    def object_target(local_id, obj):
        value = {}
        for name, prop in obj._property_metadata.items():
            item = getattr(obj, name, None)
            if isinstance(item, PropertyTypeAssignment):
                continue
            if prop.data_type == "JSON" and isinstance(item, str):
                item = json.loads(item)
            value[name] = plain_value(item)
        category = "data"
        if isinstance(obj, WorkflowFunction):
            category = "function"
        elif isinstance(obj, WorkflowDefinition):
            category = "definition"
        elif isinstance(obj, Computation):
            category = "execution"
        return ResolvedTarget(
            canonical_id=identifiers[local_id],
            value=value,
            object_type=obj.defs.code,
            category=category,
            workflow_graph=value.get("workflow_graph"),
        )

    def resolve(locator):
        if locator.kind == "object":
            matches = aliases.get(locator.identifier, [])
            if len(matches) > 1:
                raise ValueError(
                    f"Ambiguous workflow object identifier: {locator.identifier}"
                )
            if matches:
                return object_target(*matches[0])
            # An explicit resolver may supply additional object snapshots as well.
            if external_resolver is not None:
                return external_resolver(locator)
            sample = openbis.get_object(locator.identifier)
            value = dict(sample.props.all())
            value = {key.lower(): item for key, item in value.items()}
            type_code = sample.type.code
            types = {cls.defs.code: cls for cls in get_object_types("v1")}
            cls = types.get(type_code)
            category = "data"
            if cls is not None:
                # Locators use Python property names, consistently for batch and
                # persisted objects (openBIS stores lower-case property codes).
                metadata = cls()._property_metadata
                value = {
                    name: value[prop.code.lower()]
                    for name, prop in metadata.items()
                    if prop.code.lower() in value
                }
                for name, prop in metadata.items():
                    if prop.data_type == "JSON" and isinstance(value.get(name), str):
                        value[name] = json.loads(value[name])
                if issubclass(cls, WorkflowFunction):
                    category = "function"
                elif issubclass(cls, WorkflowDefinition):
                    category = "definition"
                elif issubclass(cls, Computation):
                    category = "execution"
            for name in (
                "workflow_graph",
                "workflow_specification",
                "function_specification",
            ):
                if isinstance(value.get(name), str):
                    value[name] = json.loads(value[name])
            graph = value.get("workflow_graph")
            return ResolvedTarget(
                canonical_id=sample.identifier,
                value=value,
                object_type=type_code,
                category=category,
                workflow_graph=graph,
            )
        if external_resolver is None:
            raise ValueError(
                f"A workflow resolver is required for {locator.kind} target {locator.identifier!r}"
            )
        return external_resolver(locator)

    def canonicalize(value):
        if isinstance(value, list):
            return [canonicalize(item) for item in value]
        if not isinstance(value, dict):
            return value
        if (
            value.get("kind") in {"object", "dataset", "nomad"}
            and "identifier" in value
        ):
            locator = TargetLocator.model_validate(value)
            target = resolve(locator)
            return {**value, "identifier": target.canonical_id}
        return {key: canonicalize(item) for key, item in value.items()}

    prepared = {}
    for local_id, obj in objects.items():
        for name, code, value in workflow_documents(obj):
            if code == "WORKFLOW_DEFINITION":
                target = resolve(
                    TargetLocator(kind="object", identifier=plain_value(value))
                )
                if target.object_type != "WORKFLOW_DEFINITION":
                    raise ValueError(
                        "workflow_definition must target WORKFLOW_DEFINITION"
                    )
                specification = target.value.get("workflow_specification")
                if specification is not None:
                    validate_workflow_specification(specification, resolve)
                prepared.setdefault(id(obj), {})[name] = target.canonical_id
                continue
            if isinstance(value, str):
                value = json.loads(value)
            if code == "WORKFLOW_GRAPH":
                model = validate_workflow_graph(
                    value, resolve, root_identifier=identifiers[local_id]
                )
            elif code == "WORKFLOW_SPECIFICATION":
                model = validate_workflow_specification(value, resolve)
            else:
                model = validate_function_specification(value)
            prepared.setdefault(id(obj), {})[name] = json.dumps(
                canonicalize(model.model_dump(mode="json")), sort_keys=True
            )
    return prepared
