# Explanation: `metadata/definitions.py`

This page explains the role of [`bam_masterdata/metadata/definitions.py`](../../bam_masterdata/metadata/definitions.py) and how it models the static schema layer of BAM masterdata.

## What this module is for

`definitions.py` contains the immutable building blocks that describe masterdata structure before any object is instantiated or pushed to openBIS.

In practice, this module answers questions like:

- Which kind of entity is being defined?
- Which openBIS code and description identify it?
- Which data type does a property use?
- Which vocabulary or object type does a property point to?
- Which labels should appear in Excel exports?

The runtime behavior lives elsewhere in `entities.py`. Here, the focus is on validated schema declarations.

## Main layers in the module

### `DataType`

`DataType` mirrors the set of openBIS property data types used by this package, for example:

- `VARCHAR`
- `INTEGER`
- `REAL`
- `DATE`
- `TIMESTAMP`
- `OBJECT`
- `CONTROLLEDVOCABULARY`

The `pytype` property provides the Python-side type used for runtime validation in `entities.py`. Not every openBIS type maps to a direct native Python type, so some values intentionally return `None`.

### `EntityDef`

`EntityDef` is the common base for all definition objects. It provides:

- `code`: the openBIS code
- `description`: the human-readable description
- `iri`: optional ontology identifier
- `id`: derived internal identifier used in exports
- `row_location`: source location metadata used by import/checker workflows

It also centralizes validation and export helpers:

- `validate_code()`: enforces openBIS-compatible code shapes
- `validate_iri()`: validates BAM ontology IRIs
- `strip_description()`: removes accidental whitespace
- `excel_name`: maps a definition type to the openBIS Excel section name
- `excel_headers_map`: maps model field names to Excel column headers

### Type-definition subclasses

The following classes extend `EntityDef` for each openBIS entity family:

- `CollectionTypeDef`
- `DatasetTypeDef`
- `ObjectTypeDef`
- `VocabularyTypeDef`

These classes only add fields relevant for that family. Examples:

- `ObjectTypeDef` adds `generated_code_prefix` and `auto_generate_codes`
- `DatasetTypeDef` adds dataset-specific path/pattern fields
- `VocabularyTypeDef` adds `url_template`

`ObjectTypeDef` also normalizes `generated_code_prefix` so an object type always has a usable prefix, even if the author omitted it.

### Property definitions

`PropertyTypeDef` models a property type independently of assignment to an entity. It adds:

- `property_label`
- `units`
- `data_type`
- `vocabulary_code`
- `object_code`
- `metadata`
- `dynamic_script`

This layer is still definition-only. It says what a property *is*, not yet how it is attached to an object type.

### Property assignments

`PropertyTypeAssignment` extends `PropertyTypeDef` with the assignment metadata that openBIS needs when a property is attached to an entity type:

- `mandatory`
- `show_in_edit_views`
- `section`
- `unique`
- `internal_assignment`

That split is important conceptually:

- `PropertyTypeDef` describes the property itself
- `PropertyTypeAssignment` describes the property as used by a specific entity type

### Vocabulary definitions

`VocabularyTerm` extends `VocabularyTypeDef` with term-specific fields:

- `label`
- `official`

This makes vocabulary terms look structurally similar to other definition objects, which simplifies export code and testing.

## Validation behavior

Several validators in this module are worth understanding because they influence how authors write new schema classes.

### Code validation

Entity codes are validated against openBIS-friendly characters and conventions. This allows:

- plain upper-case codes such as `INSTRUMENT`
- native openBIS codes such as `$NAME`
- inherited codes such as `WELDING_EQUIPMENT.INSTRUMENT`

### IRI validation

If an `iri` is provided, it must match the BAM ontology pattern:

`http://purl.obolibrary.org/bam-masterdata/<EntityName>:<version>`

### Property-label units handling

If `units` is present on a `PropertyTypeDef`, the model keeps `property_label` aligned with it.

Examples:

- `property_label="Length", units="meter"` becomes `Length in [meter]`
- `property_label="Length in [m]", units="meter"` stays unchanged
- `property_label="Length [m]", units="meter"` is rejected because it uses the bracketed-unit style without the required `in [...]` suffix

This behavior keeps Excel output and UI labels consistent.

## How this module is used in practice

Concrete datamodel classes in `bam_masterdata/datamodel/` use these definitions as class attributes. For example:

```python
class Instrument(ObjectType):
    defs = ObjectTypeDef(
        code="INSTRUMENT",
        description="Measuring instrument//Messgerät",
        generated_code_prefix="INS",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alias",
        description="Alternative name",
        mandatory=False,
        show_in_edit_views=True,
        section="General information",
    )
```

In that example:

- `ObjectTypeDef` defines the type itself
- `PropertyTypeAssignment` defines one property attached to the type

`entities.py` later reads those declarations and turns them into runtime entity behavior, serialization, validation, and openBIS upload logic.

## Why the separation matters

Keeping `definitions.py` separate from `entities.py` gives the codebase a clean boundary:

- `definitions.py` is about validated schema declarations
- `entities.py` is about runtime instances and behaviors

That separation makes the package easier to test, easier to export to Excel/JSON/RDF, and easier to reason about when the CLI compares or updates masterdata.
