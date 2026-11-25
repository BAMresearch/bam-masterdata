# Computational workflows and NOMAD exchange

BAM distinguishes reusable specifications from recorded executions. The v1 classes
use PMDco 3.1.2 concepts as follows:

| BAM class | Meaning | PMDco term |
| --- | --- | --- |
| `WorkflowDefinition` | Prescribed procedure and port connections | `PMD_0000012` |
| `WorkflowFunction` | Callable software procedure with named ports | `PMD_0000010` |
| `WorkflowRun` | Actual execution of a workflow | `PMD_0000016` |
| `SimulationWorkflow` | Local specialization for computational simulations | No additional exact-match IRI |

An embedded executed task represents a workflow-node occurrence (`PMD_0000011`).
A reference to another execution is a pointer to that event, not another node
execution. These conceptual correspondences do not assert OWL equivalence to NOMAD
metainfo sections. See the [PMDco definitions](https://materialdigital.github.io/core-ontology/).

`SinglePointCalculation`, `GeometryOptimization`, and `MolecularDynamics` inherit
from `SimulationWorkflow`, not from `Simulation`. Their type codes, scientific
properties, units, and existing parameter references are retained. Generic
`Simulation` remains available separately. Python inheritance does not imply
polymorphic openBIS OBJECT targets.

## Electronic-structure basis settings

`ElectronicStructureParameters` supports electronic-structure calculations using
different basis representations. `PLANE_WAVE_CUTOFF` applies only when the wave
functions use a plane-wave basis; pseudopotential or PAW references apply only
when those datasets are used. Other basis definitions and code-specific settings
can be stored in the inherited `GENERIC_PARAMETERS` JSON, for example:

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

This is a storage example, not a validated interoperable basis-set schema or an
automatic mapping to NOMAD. The scientific-data parser remains responsible for
interpreting these settings and constructing the corresponding NOMAD sections.

## Versioned graph contract

A run's `workflow_graph` is JSON with `schema_version: "1"`. It contains named
workflow inputs/outputs, tasks, dependencies, and port connections. Specifications
use `workflow_specification` and `function_specification`; these describe intended
ports and procedures, not evidence that a task happened.

Tasks have one of two exclusive forms:

- `kind: execution`: a recorded task ID/name, named inputs/outputs, and optional
  function reference, status, and timestamps.
- `kind: reference`: a task ID/name referring to an existing execution. Its relation
  distinguishes `contains` from ordinary `reference` reuse.

Each input/output has a name and a target locator: `kind` (`object`, `dataset`, or
`nomad`), `identifier`, and an optional RFC 6901 JSON-pointer `selector`. A connection
names source/target task IDs and port names; a null task ID denotes the workflow
boundary. Connected ports must resolve to the same data and selector. Dependencies
and connections must not introduce task cycles. Recorded iterations have distinct
IDs; missing iterations, functions, or convergence evidence are not invented.

The graph is the source of truth for nesting. No redundant `parent_run` is stored.
An existing execution may be referenced from several workflows; containment cycles
are rejected. Repeated invocation of one reusable procedure produces distinct run
identities.

This representation avoids one openBIS object per simulation frame. JSON-contained
references are **not enforced by openBIS**. The workflow validator resolves targets,
checks named ports and selectors, verifies referenced execution/function roles, and
checks nesting. The parser runs validation before writes in both normal and
transactional ingestion. Dataset and NOMAD resources require an explicit external
resolver; validation does not silently fetch remote resources. Existing OBJECT
constraints are unchanged.

## NOMAD export contract

`bam_masterdata.workflows.nomad.export_nomad_workflows` targets these pinned optional
packages:

```text
nomad-lab==2.0.1
nomad-simulations==0.10.0
```

They are optional interoperability-test dependencies listed in
`tests/workflows/requirements-nomad.txt`, not normal BAM runtime requirements.
Other versions are rejected until their compatibility is tested.

The exporter accepts:

1. `WorkflowExport` records: canonical run identity, name, graph, destination archive
   filename, and workflow type (`workflow`, `geometry_optimization`,
   `molecular_dynamics`, or `single_point`).
2. The authoritative workflow target resolver.
3. NOMAD archive dictionaries already containing the scientific data.
4. An explicit `section_map`: `(canonical resource ID, source selector)` to
   `NomadSection(archive filename, section path)`.

The scientific-data parser is responsible for materializing `ModelSystem`,
`ModelMethod`, and `Outputs` sections and their unit-aware values. The workflow
exporter does not guess mappings from arbitrary openBIS fields, energy conventions,
or dataset formats. Unmapped selectors and missing sections cause an error.

The returned bundle has two components:

- `archives`: real NOMAD EntryArchive dictionaries with specialized `workflow2`
  sections, named input/output `Link` sections, executed tasks, and task references.
  Explicit control dependencies become named inputs referencing their source tasks.
  Existing workflow method/result sections and scientific data are preserved.
- `provenance`: a versioned sidecar containing original graphs, canonical run IDs,
  task-ID-to-section-path mappings, and the pinned package versions. This preserves
  function references, timing/status, exact source locators, and
  reference-versus-containment semantics that native NOMAD Task does not encode.

Keep both components for lossless provenance exchange. The native NOMAD archive
alone does not preserve every BAM-specific graph field. Export does not upload,
normalize, or execute workflows. The offline loader registers only bundled archives;
it rejects unresolved cross-archive references rather than accessing a service.
Each section is validated and reference quantities are resolved before success.

This architecture follows NOMAD's separation of simulation data from workflow
organization, including nested workflow references. See the
[NOMAD workflow schema](https://fairmat-nfdi.github.io/nomad-simulations/schema/workflow/)
and [execution structure](https://fairmat-nfdi.github.io/nomad-simulations/explanation/simulation_entry/).

## Executable examples and verification

`tests/workflows/fixtures/geometry_optimization.json` contains a two-configuration
hydrogen relaxation with atomic positions, DFT method metadata, total-energy
outputs, optimization settings, and recorded convergence. Each task links to the
appropriate configuration and output sections.

`tests/workflows/fixtures/nested_workflow.json` contains relaxation followed by MD.
The enclosing workflow references both existing runs and binds the optimized final
configuration to the dynamics input. The child execution and its internal tasks
are not copied. The example contains only its explicitly recorded MD frame.

With the pinned dependencies installed, run:

```bash
python -m pytest -q tests/workflows/test_nomad.py
```

These tests deserialize real NOMAD archives and resolve references, including the
nested workflow and scientific output references, while checking positions, energy
units, convergence data, named links, and identity. Without the pinned environment,
these tests are explicitly skipped. Graph and mocked parser tests remain runnable
with normal BAM test dependencies.

Local schema loading and reference resolution are not evidence of live NOMAD
publication or openBIS synchronization. Those require separate integration tests.
