"""Real, optional NOMAD metainfo interoperability tests (no server required)."""

import json
from copy import deepcopy
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

import pytest

from bam_masterdata.workflows.nomad import (
    NOMAD_VERSIONS,
    NomadSection,
    WorkflowExport,
    export_nomad_workflows,
    load_nomad_archives,
)
from bam_masterdata.workflows.validation import ResolvedTarget


def _have_pinned_nomad():
    try:
        return all(version(name) == pin for name, pin in NOMAD_VERSIONS.items())
    except PackageNotFoundError:
        return False


pytestmark = pytest.mark.skipif(
    not _have_pinned_nomad(), reason="Requires tests/workflows/requirements-nomad.txt"
)
FIXTURES = Path(__file__).parent / "fixtures"


def _example(name):
    fixture = json.loads((FIXTURES / f"{name}.json").read_text())

    def resolver(locator):
        return ResolvedTarget(
            canonical_id=locator.identifier, **fixture["resources"][locator.identifier]
        )

    mapping = {
        (item["identifier"], item.get("selector")): NomadSection(
            item["archive"], item["path"]
        )
        for item in fixture["section_map"]
    }
    return fixture, resolver, mapping


def _export(fixture, resolver, mapping):
    return export_nomad_workflows(
        [WorkflowExport(**record) for record in fixture["records"]],
        resolver,
        archives=fixture["archives"],
        section_map=mapping,
    )


def test_geometry_optimization_loads_and_resolves_with_units():
    fixture, resolver, mapping = _example("geometry_optimization")
    original = deepcopy(fixture)
    bundle = _export(fixture, resolver, mapping)
    archive = load_nomad_archives(bundle["archives"])["geometry.archive.json"]
    workflow = archive.workflow2
    assert workflow.m_def.name == "GeometryOptimization"
    assert workflow.method.optimization_type == "atomic"
    assert workflow.results.is_converged
    assert workflow.results.n_steps == 2
    assert len(workflow.tasks) == 2
    assert workflow.tasks[0].inputs[0].name == "Structure"
    assert (
        workflow.tasks[0].inputs[0].section.m_resolved() is archive.data.model_system[0]
    )
    assert workflow.tasks[1].outputs[0].section.m_resolved() is archive.data.outputs[1]
    assert archive.data.outputs[1].total_energies[0].value.to(
        "joule"
    ).magnitude == pytest.approx(-1.7e-18)
    assert archive.data.model_system[1].positions.to("meter").magnitude[
        1, 2
    ] == pytest.approx(7.4e-11)
    control = workflow.tasks[1].inputs[-1]
    assert control.name == "Control dependency: step-0"
    assert control.section.m_resolved() is workflow.tasks[0]
    manifest = bundle["provenance"]["workflows"]["geometry-run"]
    assert manifest["task_paths"] == {
        "step-0": "/workflow2/tasks/0",
        "step-1": "/workflow2/tasks/1",
    }
    assert manifest["graph"]["tasks"][0]["function"]["identifier"] == "energy-evaluator"
    assert manifest["graph"]["tasks"][0]["status"] == "completed"
    assert fixture == original


def test_nested_workflow_references_one_existing_execution():
    fixture, resolver, mapping = _example("nested_workflow")
    bundle = _export(fixture, resolver, mapping)
    loaded = load_nomad_archives(bundle["archives"])
    geometry = loaded["geometry.archive.json"].workflow2
    parent = loaded["project.archive.json"].workflow2
    reference = parent.tasks[0]
    assert reference.m_def.name == "SimulationTaskReference"
    assert reference.task.m_resolved() is geometry
    assert len(geometry.tasks) == 2
    assert len(parent.tasks) == 2
    assert parent.tasks[1].task.m_resolved() is loaded["md.archive.json"].workflow2
    assert (
        parent.tasks[1].inputs[0].section.m_resolved()
        is loaded["geometry.archive.json"].data.model_system[1]
    )
    assert (
        reference.inputs[0].section.m_resolved()
        is loaded["geometry.archive.json"].data.model_system[0]
    )
    assert (
        reference.outputs[0].section.m_resolved()
        is loaded["geometry.archive.json"].data.model_system[1]
    )
    assert (
        bundle["provenance"]["workflows"]["project-run"]["graph"]["tasks"][0][
            "relation"
        ]
        == "contains"
    )


def test_export_rejects_unmapped_source_section():
    fixture, resolver, mapping = _example("geometry_optimization")
    del mapping[("trajectory", "/outputs/1")]
    with pytest.raises(ValueError, match="No NOMAD section mapping"):
        _export(fixture, resolver, mapping)


def test_export_rejects_dangling_nomad_section():
    fixture, resolver, mapping = _example("geometry_optimization")
    mapping[("trajectory", "/outputs/1")] = NomadSection(
        "geometry.archive.json", "/data/outputs/99"
    )
    with pytest.raises(ValueError, match="Unresolved NOMAD reference"):
        _export(fixture, resolver, mapping)


def test_export_rejects_unresolved_source_before_serializing():
    fixture, resolver, mapping = _example("geometry_optimization")
    del fixture["resources"]["trajectory"]
    with pytest.raises(ValueError, match="Unresolved"):
        _export(fixture, resolver, mapping)


@pytest.mark.parametrize("quantity", ["model_system_ref", "model_method_ref"])
def test_export_rejects_dangling_scientific_reference(quantity):
    fixture, resolver, mapping = _example("geometry_optimization")
    fixture["archives"]["geometry.archive.json"]["data"]["outputs"][0][quantity] = (
        "#/data/model_system/99"
    )
    with pytest.raises(ValueError, match="Unresolved NOMAD reference"):
        _export(fixture, resolver, mapping)


def test_export_rejects_contradictory_nested_execution():
    fixture, resolver, mapping = _example("nested_workflow")
    fixture["resources"]["geometry-run"]["workflow_graph"]["tasks"][0]["name"] = (
        "Different run"
    )
    with pytest.raises(ValueError, match="differs from exported execution"):
        _export(fixture, resolver, mapping)
