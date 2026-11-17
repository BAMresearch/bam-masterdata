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

## Run the HZB battery example

The recursive fixture inventory is `tests/data/nomad_hzb_profile.json`. It explicitly
supplies upload IDs and mainfiles because the 19 supplied JSON files omit archive
metadata. One file, `1.archive.json`, contains only a schema name. The configuration
excludes that exact path with a reason; removing the exclusion makes strict parsing
fail on its missing name. No file is excluded by an implicit naming rule.

Run from the repository root:

```python
import json
from pathlib import Path
import structlog

from bam_masterdata.metadata.entities import CollectionType
from bam_masterdata.parsing.nomad import ArchiveSource, NomadParser
from bam_masterdata.parsing.nomad.hzb import HZBBatteryMapping

root = Path("tests/data")
profile = json.loads((root / "nomad_hzb_profile.json").read_text())
sources = [
    ArchiveSource(root / row["path"], row["upload_id"], row["mainfile"])
    for row in profile["sources"]
]
parser = NomadParser(
    mapping=HZBBatteryMapping(
        target_version="v1",  # select "v0" explicitly for the legacy catalog
        quantity_profile=profile["quantity_profile"],
    ),
    sources=sources,
    exclude={root / path: reason for path, reason in profile["exclude"].items()},
)
collection = CollectionType()
parser.parse([str(source.path) for source in sources], collection, structlog.get_logger())
print(len(collection.attached_objects))  # 21: 18 entries, synthesis, two steps
print(parser.report.to_json(indent=2))
```

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

HZB selection uses the complete `data.m_def` and a supported `data.m_def_id` pair
in `parsing/nomad/hzb.py`. The fixture profile recognizes nine top-level schemas,
including both observed hashes for `ElectrodeSheet`. Recognized nested geometry,
quantity-section, and pure-substance identifiers/hashes are checked too. Each
subsection accepts only its expected schema kind; a known geometry schema cannot
stand in for a pure-substance or volume section. Inline
subsections lacking these tags are supported only in the recognized parent
schemas. Filename changes never select a different mapping.

The archives do not declare units. The explicitly approved
`hzb-fixtures-20260701` profile uses these source conventions:

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
inform these conventions, but their current revision has not been shown to
reproduce the archived schema hashes. Applying this profile to another export
requires confirming its units; it must not be treated as an automatic NOMAD SI
or display-unit policy. Declared BAM `units` alone do not perform conversion.

`yield_percent=.8` and `wt_percent=.49` retain their source values with an
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
synthesis → powder. Ordered synthesis membership and workflow aliases are
qualified relations retained in source JSON, not misleading material-flow edges.
The two workflow tasks reuse the existing two step identities. The nested
synthesis shares the powder lab ID but has a distinct section-pointer identity.

## Identity, references, errors, and retained information

An `ArchiveSource` supplies the exact mainfile path relative to the upload's raw
directory, including any subdirectories. Local fixture folders are merely the
explicit layout used to construct the checked-in profile. Do not infer identity
from chemical names. An explicit entry ID can be supplied when available; otherwise
the [NOMAD entry-ID recipe](https://github.com/FAIRmat-NFDI/nomad/blob/develop/nomad/utils/__init__.py)
uses SHA-512 over upload ID, mainfile, and optional mainfile key, encoded as the
first 28 websafe-base64 characters. It reproduces every supplied cross-file target.

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
   supplies identity, so no battery layout or fixture profile is involved.
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

Regression tests map actual HZB fixtures against both versions, exercise the
synthetic extension, validate values/schema serialization, and run ordinary and
transactional loaders against mocks. These are offline and mocked checks. They do
not establish live openBIS masterdata provisioning, JSON property handling, server
reference validation or transaction behavior. Those require a disposable instance
and separately recorded execution evidence.
