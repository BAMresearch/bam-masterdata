"""Explicit, offline workflow export to the pinned NOMAD metainfo schema.

Scientific data are supplied as NOMAD archive sections. This adapter maps provenance;
it does not guess how arbitrary openBIS properties should become scientific quantities.
"""

import importlib
from copy import deepcopy
from dataclasses import dataclass
from importlib.metadata import version
from typing import Any

from bam_masterdata.workflows.models import WorkflowGraph
from bam_masterdata.workflows.validation import validate_workflow_graph

NOMAD_VERSIONS = {"nomad-lab": "2.0.1", "nomad-simulations": "0.10.0"}
WORKFLOW_CLASSES = {
    "workflow": "nomad_simulations.schema_packages.workflow.general.SimulationWorkflow",
    "geometry_optimization": "nomad_simulations.schema_packages.workflow.geometry_optimization.GeometryOptimization",
    "molecular_dynamics": "nomad_simulations.schema_packages.workflow.molecular_dynamics.MolecularDynamics",
    "single_point": "nomad_simulations.schema_packages.workflow.single_point.SinglePoint",
}
TASK_CLASS = "nomad_simulations.schema_packages.workflow.general.SimulationTask"
REFERENCE_CLASS = (
    "nomad_simulations.schema_packages.workflow.general.SimulationTaskReference"
)


@dataclass(frozen=True)
class NomadSection:
    """A section inside an archive supplied to the exporter, never a remote fetch."""

    archive: str
    path: str


@dataclass(frozen=True)
class WorkflowExport:
    """Identity and destination of one recorded workflow execution."""

    identifier: str
    name: str
    graph: WorkflowGraph | dict
    archive: str
    workflow_type: str = "workflow"


def _schema():
    """Load optional dependencies only when performing NOMAD interoperability."""
    for package, expected in NOMAD_VERSIONS.items():
        installed = version(package)
        if installed != expected:
            raise RuntimeError(f"Expected {package}=={expected}, found {installed}")
    from nomad.datamodel import (  # noqa: PLC0415 — optional interoperability dependency
        EntryArchive,
    )
    from nomad.datamodel.context import (  # noqa: PLC0415 — optional interoperability dependency
        Context,
    )
    from nomad.datamodel.metainfo.workflow import (  # noqa: PLC0415 — optional interoperability dependency
        Task,
    )
    from nomad.metainfo import (  # noqa: PLC0415 — optional interoperability dependency
        MSection,
        Reference,
    )

    for path in WORKFLOW_CLASSES.values():
        importlib.import_module(path.rsplit(".", 1)[0])
    importlib.import_module("nomad_simulations.schema_packages.general")
    return EntryArchive, Context, Task, MSection, Reference


def load_nomad_archives(archives: dict[str, dict]) -> dict[str, Any]:
    """Deserialize a self-contained archive bundle and resolve workflow references.

    The context never retrieves remote resources. Missing archives, section paths, or
    non-section input/output targets fail instead of appearing as successful exports.
    """
    EntryArchive, Context, Task, MSection, Reference = _schema()

    class BundleContext(Context):
        def load_url(self, url):
            raise ValueError(f"Archive is not present in the export bundle: {url}")

    context = BundleContext()
    loaded = {
        name: EntryArchive.m_from_dict(deepcopy(data), m_context=context)
        for name, data in archives.items()
    }
    for name, archive in loaded.items():
        context.cache_archive(name, archive)

    def resolve_reference(value):
        if value is None:
            raise ValueError("Reference resolves to no target")
        if isinstance(value, list | tuple):
            for item in value:
                resolve_reference(item)
        elif hasattr(value, "m_proxy_resolve"):
            if value.m_proxy_resolve() is None:
                raise ValueError("Reference resolves to no target")

    all_sections = [
        section
        for archive in loaded.values()
        for section in [archive, *archive.m_all_contents()]
    ]
    for section in all_sections:
        errors, _ = section.m_validate()
        if errors:
            raise ValueError(f"Invalid NOMAD section {section.m_path()}: {errors}")
        for name, quantity in section.m_def.all_quantities.items():
            if isinstance(quantity.type, Reference) and section.m_is_set(quantity):
                try:
                    resolve_reference(section.m_get(quantity))
                except Exception as exc:
                    raise ValueError(
                        f"Unresolved NOMAD reference {section.m_path()}.{name}"
                    ) from exc
    for section in all_sections:
        if isinstance(section, Task):
            for link in [*section.inputs, *section.outputs]:
                if not isinstance(link.section, MSection):
                    raise ValueError(f"Unresolved NOMAD link: {link.name}")
            if "task" in section.m_def.all_quantities:
                if not isinstance(section.task, Task):
                    raise ValueError(f"Task reference does not resolve: {section.name}")
    return loaded


def export_nomad_workflows(
    records: list[WorkflowExport],
    resolver,
    *,
    archives: dict[str, dict],
    section_map: dict[tuple[str, str | None], NomadSection],
) -> dict:
    """Export recorded workflow graphs, preserving existing scientific sections.

    ``resolver`` is the same authoritative resource resolver used at ingestion.
    ``section_map`` keys are (resolved canonical resource ID, source JSON pointer).
    Values identify actual NOMAD sections already supplied in ``archives``. Scientific
    values and units must be materialized by the scientific-data parser beforehand.

    Return ``archives`` plus a versioned ``provenance`` sidecar. Both form the export:
    the sidecar preserves task IDs, function/timing/status metadata, original source
    locators, and reference-versus-containment semantics not native to NOMAD Task.
    """
    output = deepcopy(archives)
    run_sections = {}
    graphs = {}
    destinations = set()
    for record in records:
        if record.identifier in graphs or record.archive in destinations:
            raise ValueError(
                "Workflow identities and destination archives must be unique"
            )
        if record.archive not in output:
            raise ValueError(f"Missing destination archive: {record.archive}")
        if record.workflow_type not in WORKFLOW_CLASSES:
            raise ValueError(f"Unsupported workflow type: {record.workflow_type}")
        graphs[record.identifier] = validate_workflow_graph(
            record.graph, resolver, root_identifier=record.identifier
        )
        run_sections[record.identifier] = NomadSection(record.archive, "/workflow2")
        destinations.add(record.archive)

    def reference(target, source_archive):
        if target.archive not in output or not target.path.startswith("/"):
            raise ValueError(f"Invalid NOMAD section destination: {target}")
        prefix = "" if target.archive == source_archive else target.archive
        return f"{prefix}#{target.path}"

    def data_reference(locator, source_archive):
        resource = resolver(locator)
        key = (resource.canonical_id, locator.selector)
        if key not in section_map:
            raise ValueError(f"No NOMAD section mapping for {key}")
        return reference(section_map[key], source_archive)

    def links(items, source_archive):
        return [
            {"name": item.name, "section": data_reference(item.target, source_archive)}
            for item in items
        ]

    manifest = {}
    for record in records:
        graph = graphs[record.identifier]
        tasks = []
        task_paths = {
            task.id: f"/workflow2/tasks/{index}"
            for index, task in enumerate(graph.tasks)
        }
        for task in graph.tasks:
            value = {
                "m_def": TASK_CLASS,
                "name": task.name,
                "inputs": links(task.inputs, record.archive),
                "outputs": links(task.outputs, record.archive),
            }
            if task.kind == "reference":
                resource = resolver(task.target)
                if (
                    task.target.selector is None
                    and resource.canonical_id in run_sections
                ):
                    destination = run_sections[resource.canonical_id]
                    if resource.workflow_graph is not None:
                        resolved_graph = validate_workflow_graph(
                            resource.workflow_graph,
                            resolver,
                            root_identifier=resource.canonical_id,
                        )
                        if resolved_graph != graphs[resource.canonical_id]:
                            raise ValueError(
                                "Referenced workflow graph differs from exported execution"
                            )
                else:
                    key = (resource.canonical_id, task.target.selector)
                    if key not in section_map:
                        raise ValueError(f"No NOMAD execution mapping for {key}")
                    destination = section_map[key]
                value["m_def"] = REFERENCE_CLASS
                value["task"] = reference(destination, record.archive)
            for dependency in graph.dependencies:
                if dependency.target == task.id:
                    label = f"Control dependency: {dependency.source}"
                    if any(item["name"] == label for item in value["inputs"]):
                        raise ValueError(f"Reserved dependency port name: {label}")
                    value["inputs"].append(
                        {"name": label, "section": f"#{task_paths[dependency.source]}"}
                    )
            tasks.append(value)
        previous = output[record.archive].get("workflow2", {})
        expected = WORKFLOW_CLASSES[record.workflow_type]
        if previous.get("tasks"):
            raise ValueError("Destination already contains workflow tasks")
        if previous.get("m_def", expected) != expected:
            raise ValueError("Destination workflow type conflicts with requested type")
        output[record.archive]["workflow2"] = {
            **previous,
            "m_def": expected,
            "name": record.name,
            "inputs": links(graph.inputs, record.archive),
            "outputs": links(graph.outputs, record.archive),
            "tasks": tasks,
        }
        manifest[record.identifier] = {
            "archive": record.archive,
            "workflow_type": record.workflow_type,
            "graph": graph.model_dump(mode="json"),
            "task_paths": task_paths,
        }
    loaded = load_nomad_archives(output)
    _, _, _, MSection, _ = _schema()
    for destination in section_map.values():
        if destination.archive not in loaded:
            raise ValueError(f"Mapped archive is missing: {destination.archive}")
        section = loaded[destination.archive].m_resolve(destination.path)
        if not isinstance(section, MSection):
            raise ValueError(f"Mapped target is not a NOMAD section: {destination}")
    return {
        "archives": output,
        "provenance": {
            "schema_version": "1",
            "nomad_versions": NOMAD_VERSIONS.copy(),
            "workflows": manifest,
        },
    }
