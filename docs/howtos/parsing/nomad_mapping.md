# Map supported NOMAD archives locally

`NomadParser` maps explicit NOMAD schema profiles into BAM objects and relationships
through the existing `AbstractParser` / `CollectionType` workflow. It performs no
network requests and requires neither NOMAD nor openBIS to be running. It uses the
existing Pint dependency for unit conversion.

This is a small extension mechanism, not universal NOMAD compatibility. The shared
module, `bam_masterdata/parsing/nomad/core.py`, handles archive identity, reference
resolution, conversion, graph validation, portable serialization, and parser
integration. Domain mappings supply source-schema selection, field meaning, BAM
classes, units, vocabulary translations, and relationship roles. The shared module
contains no battery imports or battery dispatch rules.

## Configure an HZB mapping

Inspect the source archive and its originating schema before mapping. The HZB
mapper recognizes supported qualified schema names, but bundles no laboratory
records, source upload/entry IDs, or schema revision hashes. Supply the exact
`m_def_id` values whose definitions and units you have verified through the required
`schema_ids` configuration. A hash being present in an archive does not establish
compatibility by itself.

This self-contained example uses deliberately synthetic names and revision tags:

```python
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import structlog

from bam_masterdata.metadata.entities import CollectionType
from bam_masterdata.parsing.nomad import ArchiveSource, NomadParser
from bam_masterdata.parsing.nomad.hzb import HZBBatteryMapping

chemical_schema = "nomad_battery_space.schema_packages.hzb_bs_package.BS_Chemical"
# Demonstration placeholder only: replace with a revision you have inspected.
schema_ids = {chemical_schema: {"example-reviewed-revision"}}
parser = NomadParser(
    mapping=HZBBatteryMapping(
        target_version="v1",  # select "v0" explicitly for the legacy catalog
        quantity_profile="hzb-laboratory-units-v1",
        schema_ids=schema_ids,
    ),
)
with TemporaryDirectory() as directory:
    path = Path(directory) / "example.json"
    path.write_text(json.dumps({
        "metadata": {"upload_id": "example-upload", "mainfile": "example.json"},
        "data": {
            "m_def": chemical_schema,
            "m_def_id": "example-reviewed-revision",
            "name": "Synthetic chemical",
            "lab_id": "synthetic-chemical",
        },
    }))
    collection = CollectionType()
    parser.parse([str(path)], collection, structlog.get_logger())
    print(parser.report.to_json(indent=2))
```

For data-only archives lacking identity metadata, pass explicit source descriptors
such as `ArchiveSource(path, upload_id="example-upload", mainfile="example.json")`
in the parser's `sources` argument. Supply identifiers from the actual source
system rather than inferring them from local filenames or display names.

A successful mapping appends objects to the supplied collection after validating
all references and mandatory values. Required OBJECT assignments may be deferred
until all source objects exist; a missing required reference still fails before
the supplied collection changes. An error leaves it unchanged. Reusing the
same collection for the same source codes is rejected rather than silently
replacing objects. For new independent runs, use a new collection.

The parser also fits `files_parser={parser: files}` in `RunParsers` or
`RunParsersWithTransactions`. Loading is a separate operation that connects to
openBIS and may update existing records with the stable generated codes. Do not
use a production instance to test a new mapping. Source archives can additionally
be attached as datasets using the existing object dataset API.

### Schema selection and quantities

HZB selection uses the complete `data.m_def` and a `data.m_def_id` explicitly
permitted by the caller's `schema_ids` mapping. Its keys must be supported qualified
schema names and its values nonempty collections of inspected IDs. Missing
configuration, unsupported schema names, and unapproved revisions fail. There is
no default revision allowlist or name-only compatibility fallback.

The fixed supported names cover the nine top-level concepts below and the
following nested kinds: `DimensionsAndWeights`, `VolumeAndWeights`, `CircleGeometry`,
`RectangleGeometry` in `nomad_battery_space.schema_packages.utilities`, and
`nomad.datamodel.metainfo.basesections.v1.PubChemPureSubstanceSection`. Include any
named nested schemas encountered in `schema_ids` too. Named subsections require an
approved ID and are validated against their path's expected kind. A recognized
geometry schema cannot stand in for a pure-substance or volume section. Tagless
inline quantity and pure-substance subsections use the explicitly selected parent
schema/profile's layout; geometry still needs its supported qualified name and
approved revision. Filenames never select a mapping.

The explicitly selected `hzb-laboratory-units-v1` profile uses these conventions.
Confirm them against the exact source schema revision before selecting this
profile; it does not establish that an arbitrary NOMAD export uses these units.

| Source quantity | Profile unit | Typed BAM target unit |
| --- | --- | --- |
| Thickness | µm | µm |
| Mass/product weight | g | g |
| Length, width, diameter | mm | mm |
| Supplied area | cm² | cm² |
| Volume/product volume | mL | mL |
| Molar mass | g/mol | g/mol |
| Component molar concentration | mol/L | mol/m³ in qualified provenance |
| Chemical component volume/mass (`chemicals[]`) | mL / g | m³ / kg in qualified provenance |
| Active-material component mass (`electrode_materials[]`) | mg | kg in qualified provenance |

Current upstream [dimensions](https://github.com/nomad-hzb/nomad-battery-space/blob/main/src/nomad_battery_space/schema_packages/utilities/dimensions.py),
[geometry](https://github.com/nomad-hzb/nomad-battery-space/blob/main/src/nomad_battery_space/schema_packages/utilities/geometry.py),
and [component schemas](https://github.com/nomad-hzb/nomad-battery-space/blob/main/src/nomad_battery_space/schema_packages/hzb_bs_package.py)
inform these conventions. Compare them with the exact revisions of your source
schemas; a current upstream definition does not prove an older export's units.
The profile is not an automatic NOMAD SI or display-unit policy. Declared BAM
`units` alone do not perform conversion.

`yield_percent` and `wt_percent` retain their source values with an
`unconfirmed_scale` diagnostic. No multiplication by 100 is assumed. Supplied
areas are preserved rather than recalculated. Root `datetime` maps to
`RECORD_DATETIME`, not preparation or assembly date. Shipping/opening timestamps
retain their complete timestamp strings; existing DATE assignments are not
silently truncated.

### Target schemas and relationships

| Source class | v0 code | v1 code |
| --- | --- | --- |
| BS_Chemical | CHEMICAL.STOCK | CHEMICAL_STOCK |
| ElectrodeMaterial | MATERIAL_V1.ELECTRODE_MATERIAL | ELECTRODE_MATERIAL |
| ElectrodeSheet | MATERIAL_V1.ELECTRODE_SHEET | ELECTRODE_SHEET |
| ElectrolyteStock | MATERIAL_V1.ELECTROLYTE_STOCK | ELECTROLYTE_STOCK |
| SeparatorStock | MATERIAL_V1.SEPARATOR_STOCK | SEPARATOR_STOCK |
| ElectrodeSample | SAMPLE.ELECTRODE | ELECTRODE_SAMPLE |
| ElectrolyteSample | SAMPLE.ELECTROLYTE | ELECTROLYTE_SAMPLE |
| SeparatorSample | SAMPLE.SEPARATOR | SEPARATOR_SAMPLE |
| CoinCellBattery | SAMPLE.COIN_CELL | COIN_CELL |

The new v0 chemical stock relaxes only its inherited administrative requirements
for manufacturer, hazardous-substance status, BAM organizational unit and BAM
location. New v0 sample types similarly make BAM organizational unit optional.
Generic `Chemical` and `Sample` requirements are unchanged. Supplier is not used
as a guessed manufacturer. In v1, laboratory IDs populate existing material/sample
IDs; chemical stock and coin cell have `LAB_ID`.

Scalar OBJECT properties identify exact sheet/stock/component target codes for
the selected version. Working/counter electrode roles are cell relationships,
not inferred intrinsic anode/cathode classifications. The mapping does not loosen
or populate v1 Activity's exact `ENTITY` input/output constraints with subtypes.

Collection edges run input → derived material/sample/cell, or chemicals →
synthesis → material. Ordered synthesis membership and workflow aliases are
qualified relations retained in source JSON, not misleading material-flow edges.
Workflow tasks reuse the identities of the steps they reference. A nested
synthesis has a distinct section-pointer identity even when it shares its output
material's lab ID.

## Identity, references, errors, and retained information

An `ArchiveSource` supplies the exact mainfile path relative to the upload's raw
directory, including any subdirectories. Do not infer identity from chemical
names or assume that the local folder layout reproduces the source upload. An explicit entry ID can be supplied when available; otherwise
the [NOMAD entry-ID recipe](https://github.com/FAIRmat-NFDI/nomad/blob/develop/nomad/utils/__init__.py)
uses SHA-512 over upload ID, mainfile, and optional mainfile key, encoded as the
first 28 websafe-base64 characters.

With real archive `metadata.upload_id` and `metadata.mainfile`, descriptors may be
omitted. Optional entry ID/mainfile key are accepted there too. Supplied descriptors
are checked against any corresponding archive metadata. Physical sections are
identified by `(upload_id, entry_id, JSON pointer)`, not by lab ID. Target codes
are stable hashes of the mapping family, target version and section identity.

Supported reference forms are exactly:

- `../uploads/<upload_id>/archive/<entry_id>#data`
- `../uploads/<upload_id>/archive/<entry_id>#/data`, also with nested pointers
- Local `#/data/...` JSON pointers

No URL fetching, arbitrary API response wrappers, raw-file references, or cyclic
scalar OBJECT graphs are implemented. The shared resolver only links sections the
mapping has actually materialized. Scalar OBJECT dependencies are ordered before
the referring objects; source file order does not affect the result.

Unknown schemas/hashes, unsupported units, missing mandatory values, conflicting
identities, malformed/unresolved references, and wrong exact target types fail
mapping. Identical repeated archive identity/content is included once with a
diagnostic; repeated lab IDs across distinct archives are retained with a warning.
Empty component `{}` placeholders produce diagnostics without invented entities.
Explicit exclusions require reasons and remain visible in the report.

Every mapped target has `SOURCE_RECORD`: a JSON-encoded envelope containing the
unaltered parsed archive, mainfile/identity, source pointer, mapping/profile IDs,
retained-field paths, and qualified relations. It preserves elemental fractions,
HTML notes, empty arrays, ambiguous percentages and component amounts/roles. It
also preserves questionable upstream identity claims without endorsing or repairing
them. This is parsed JSON preservation, not a byte-identical file copy.

`report.to_json()` serializes the entire mapped graph using scalar target codes
for OBJECT values; collection-local IDs are random and should not be compared
across runs. Existing generic instance `to_json()` does not serialize nested
ObjectType references; use the report serializer for graphs. Existing schema
`model_to_json()` remains available for class definitions.

## Worked extension: synthetic software execution

This example is deliberately synthetic. Its fixtures are in
`tests/data/nomad_synthetic/`; its separate mapping and demonstration subclasses
are in `bam_masterdata/parsing/nomad/example_software.py`. The subclasses are not
part of production datamodel discovery. They demonstrate reuse, not compatibility
with all NOMAD software archives.

1. Inspect the source before choosing targets. The fixtures use
   `demo.synthetic.Software` and `demo.synthetic.Execution`, both explicitly tagged
   `m_def_id="synthetic-v1"`. Execution contains `duration={value: 2, unit: "minute"}`,
   `status="done"` and an upload/archive software reference. Their archive metadata
   supplies identity, so no battery layout or laboratory profile is involved.
2. Select `SyntheticSoftwareMapping(target_version="v0" or "v1")` explicitly.
   Its `map(context)` function recognizes only these schema/version pairs. A real
   third-party schema needs its own inspected names/hashes and mapping module.
3. Reuse `SoftwareCode`/`ComputationalAnalysis` in v0 and `Software`/`Computation`
   in v1 as parents. The demonstration adds provenance and missing duration/typed
   software assignments in narrow subclasses. It uses a new OBJECT property code
   instead of changing the inherited property's exact target constraint. v0 also
   supplies its existing mandatory `software_name` from the observed software name.
4. Map fields through `context.required_text` / `context.value`. Convert the
   explicitly declared source duration using `context.quantity(value, unit, "s")`:
   two minutes becomes 120 seconds. Translate source status `done` to existing
   v1 `ACTIVITY_STATUS.COMPLETED` or v0's reused completion flag. Other statuses
   fail rather than guessing. Original status remains in the source envelope.
5. Create all objects with `context.create(...)`, then resolve software with
   `context.reference(..., attribute="software", role="executed_software")`.
   The shared resolver enforces the new exact target and object identity; no
   changes to shared archive handling are needed.
6. Run locally and add regression tests:

```python
from pathlib import Path
import structlog
from bam_masterdata.metadata.entities import CollectionType
from bam_masterdata.parsing.nomad import NomadParser
from bam_masterdata.parsing.nomad.example_software import SyntheticSoftwareMapping

parser = NomadParser(SyntheticSoftwareMapping(target_version="v1"))
collection = CollectionType()
parser.parse(
    [str(p) for p in Path("tests/data/nomad_synthetic").glob("*.json")],
    collection,
    structlog.get_logger(),
)
```

Run `pytest tests/parsing/test_nomad_mapping.py`. Add real-schema fixtures separately,
assert actual values, conversions, identity, provenance, ordering independence and
failure behavior. Validate new definitions against a selected version's class set.
Run Ruff on changed files and obtain independent coverage/architecture reviews.

A new source layout, field mapping, unit profile, enum translation or relationship
role normally needs only a new mapping. A missing BAM scientific concept/property
needs a reviewed version-specific schema addition. A newly required reference or
archive envelope representation may require a focused shared-infrastructure
change with a domain-independent test. Do not add a universal mapping language,
NOMAD SDK dependency, remote crawler or speculative abstraction for this example.

## Verification boundary

Regression tests generate a small, explicitly synthetic HZB-schema graph in a
temporary directory for both BAM versions. They use placeholder schema revision
IDs supplied explicitly to the mapping and test roles, shared identity, ordering,
unit conversion, validation failures and atomicity. Separate synthetic non-battery
fixtures demonstrate reuse, and ordinary/transactional loaders run against mocks.
These checks do not validate compatibility with a real laboratory export or prove
live openBIS provisioning, JSON property handling, server reference validation or
transaction behavior. Those require separately supplied source evidence and a
disposable instance with recorded execution results.
