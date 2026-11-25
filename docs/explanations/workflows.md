# Workflows and NOMAD exchange

BAM distinguishes reusable workflow specifications from recorded executions:

| Type | Purpose |
| --- | --- |
| `WorkflowDefinition` | Prescribed procedure and port connections |
| `WorkflowFunction` | Callable software procedure with named ports |
| `WorkflowRun` | Recorded execution of a workflow |
| `SimulationWorkflow` | Workflow execution organizing simulations |
| `SinglePointCalculation` | Single-point simulation workflow |
| `GeometryOptimization` | Geometry-optimization workflow |
| `MolecularDynamics` | Molecular-dynamics workflow |
| `Simulation` | Generic simulation |

The specification and execution types follow
[PMDco concepts](https://materialdigital.github.io/core-ontology/).

## Electronic-structure basis settings

`ElectronicStructureParameters` supports different basis representations.
`PLANE_WAVE_CUTOFF` applies to plane-wave wave functions; pseudopotential and PAW
references apply when those datasets are used. Store other basis definitions and
code-specific settings in the inherited `GENERIC_PARAMETERS` JSON, for example:

```json
{
  "basis_sets": [
    {
      "name": "def2-TZVP",
      "representation": "gaussian",
      "role": "orbital",
      "elements": ["C", "H"]
    }
  ]
}
```

The scientific-data parser must interpret these settings and construct the
corresponding NOMAD sections. The JSON example is a storage convention, not a
validated interoperable basis-set schema.

## Graph format

A run's `workflow_graph` is JSON with `schema_version: "1"`. It contains named
workflow inputs and outputs, tasks, dependencies, and port connections. Reusable
specifications use `workflow_specification` and `function_specification` to describe
intended ports and procedures.

Tasks have one of two forms:

- `kind: execution`: a recorded task ID/name, named inputs and outputs, and optional
  function reference, status, and timestamps.
- `kind: reference`: a task ID/name referring to an existing execution. Its relation
  distinguishes `contains` from ordinary `reference` reuse.

Each input/output has a name and a target locator: `kind` (`object`, `dataset`, or
`nomad`), `identifier`, and an optional RFC 6901 JSON-pointer `selector`. A connection
names source/target task IDs and port names; a null task ID denotes the workflow
boundary. Connected ports must resolve to the same data and selector. Dependencies
and connections must be acyclic. Give recorded iterations distinct IDs.

The graph defines nesting. An existing execution may be referenced from several
workflows; containment cycles are rejected. Repeated invocations of a reusable
procedure have distinct run identities.

JSON-contained references are not enforced by openBIS. Before ingestion and export,
the workflow validator resolves targets, checks named ports and selectors, verifies
execution/function roles, and checks nesting. Dataset and NOMAD resources require
an explicit external resolver.

## Export to NOMAD

The exporter requires these optional packages, listed in
`tests/workflows/requirements-nomad.txt`:

```text
nomad-lab==2.0.1
nomad-simulations==0.10.0
```

Other versions are rejected. To export:

1. Prepare NOMAD archive dictionaries containing the scientific data, including
   `ModelSystem`, `ModelMethod`, and `Outputs` sections with unit-aware values.
2. Create `WorkflowExport` records with the canonical run identity, name, graph,
   destination archive filename, and workflow type: `workflow`,
   `geometry_optimization`, `molecular_dynamics`, or `single_point`.
3. Supply the authoritative workflow target resolver and a `section_map` mapping
   `(canonical resource ID, source selector)` to
   `NomadSection(archive filename, section path)`.
4. Call the exporter:

```python
from bam_masterdata.workflows.nomad import export_nomad_workflows

bundle = export_nomad_workflows(
    records,
    resolver,
    archives=archives,
    section_map=section_map,
)
```

Unmapped selectors, missing sections, and unresolved references cause an error.
The exporter validates sections and resolves references using the supplied archive
bundle. Export is offline: uploading, normalization, and workflow execution are
separate operations.

Keep both returned components:

- `archives`: NOMAD EntryArchive dictionaries with specialized `workflow2` sections,
  named input/output links, executed tasks, and task references. Control dependencies
  become named inputs referencing their source tasks. Existing workflow method/result
  sections and scientific data are preserved.
- `provenance`: a versioned sidecar with original graphs, canonical run IDs,
  task-ID-to-section-path mappings, and package versions. It preserves function
  references, timing/status, source locators, and reference-versus-containment
  semantics that native NOMAD tasks do not encode.

See the [NOMAD workflow schema](https://fairmat-nfdi.github.io/nomad-simulations/schema/workflow/)
and [execution structure](https://fairmat-nfdi.github.io/nomad-simulations/explanation/simulation_entry/).

## Examples

`tests/workflows/fixtures/geometry_optimization.json` contains a two-configuration
hydrogen relaxation with positions, DFT metadata, total-energy outputs, optimization
settings, and convergence data. Tasks link to the configuration and output sections.

`tests/workflows/fixtures/nested_workflow.json` contains relaxation followed by MD.
The enclosing workflow references both runs and connects the optimized final
configuration to the dynamics input.

With the pinned dependencies installed, run the examples' validation tests:

```bash
python -m pytest -q tests/workflows/test_nomad.py
```

These tests load NOMAD archives and resolve workflow and scientific-output
references. They are skipped without the pinned environment. Graph and mocked
parser tests use the normal BAM test dependencies.
