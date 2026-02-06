# How-to: Define Object Types and Properties

This how-to guide shows how to create new Object Types in `bam-masterdata`, including how to define the
Object Type itself and the properties assigned to it. It also covers the optional `units` field
for property definitions.

## Create a New Object Type

Object types live in `bam_masterdata/datamodel/object_types.py` and are defined as subclasses of
`ObjectType` or of any other Object Type. Each object type must include:

- `defs`: an `ObjectTypeDef` instance describing the object type static metainformation
- one or more `PropertyTypeAssignment` entries describing assigned properties

Example:

```python
from bam_masterdata.metadata.definitions import DataType, ObjectTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.entities import ObjectType


class TestSpecimen(ObjectType):
    defs = ObjectTypeDef(
        code="TEST_SPECIMEN",
        description="Test specimen used in experiments//Testkoerper fuer Versuche",
        generated_code_prefix="TSP",
        auto_generate_codes=True,
    )

    name = PropertyTypeAssignment(
        code="NAME",
        data_type=DataType.VARCHAR,
        property_label="Name",
        description="Human readable name//Name",
        mandatory=True,
        show_in_edit_views=True,
        section="General",
    )
```

## `ObjectTypeDef` Options

`ObjectTypeDef` defines static metadata for the object type:

- `code`: OpenBIS object type code (uppercase with underscores)
- `description`: English text with optional German text separated by `//`
- `generated_code_prefix` (optional): short prefix used for auto-generated codes
- `auto_generate_codes` (optional): set `True` to auto-generate codes using the prefix

Rules:

- `code` must be uppercase, use underscores, and may include inheritance with dots.
- `description` should be human-readable and complete enough; use `//` to add the German version.
- If `generated_code_prefix` is not provided, it defaults to the first three letters of `code`.

## `PropertyTypeAssignment` Options

Each `PropertyTypeAssignment` supports:

- `code`: OpenBIS property code (uppercase with underscores)
- `data_type`: one of the `DataType` enum values (see [Data Types](#data-types) for all the options)
- `property_label`: human-readable label shown in the GUI
- `description`: English and optional German text (separated by `//`)
- `mandatory`: if `True`, the property must be set
- `show_in_edit_views`: if `True`, show the property in edit views
- `section`: section label used in the GUI to group properties
- `vocabulary_code` (optional): required for `CONTROLLEDVOCABULARY`
- `object_code` (optional): required for `OBJECT`
- `units` (optional): units in pint format

Other options are being deprecated in a near future, that is why they are not included here.

Rules:

- `code` must be uppercase, use underscores, and may include inheritance with dots.
- `description` uses `//` to include German text.
- If `data_type` is `CONTROLLEDVOCABULARY`, you must set `vocabulary_code`.
- If `data_type` is `OBJECT`, you must set `object_code`.
- `property_label` must be human-readable and should not include internal codes.
- When `units` is set, `property_label` will automatic include `in [units]` when displayed on the GUI.

## Data Types

`data_type` must be one of the `DataType` enum values. Common choices:

- `VARCHAR`, `MULTILINE_VARCHAR` for text
- `INTEGER`, `REAL` for numeric values
- `DATE`, `TIMESTAMP` for date/time
- `BOOLEAN` for true/false
- `HYPERLINK` for URLs
- `CONTROLLEDVOCABULARY` for pick-lists (requires `vocabulary_code`)
- `OBJECT` for references to other object types (requires `object_code`)

For object references, see [How-to: Work with Object References](./object_references.md).

## Units with pint

You can optionally attach units to any property using `units`. Units are parsed using pint and must
be valid according to the [default pint registry](https://github.com/hgrecco/pint/blob/master/pint/default_en.txt).

When `units` is provided, `property_label` is automatically suffixed with `in [units]` unless it
already includes `in [units]`. If it contains brackets but not the `in [units]` format, validation
fails.

Example:

```python
temperature = PropertyTypeAssignment(
    code="TEMPERATURE",
    data_type=DataType.REAL,
    property_label="Temperature",
    description="Measurement temperature//Messtemperatur",
    mandatory=False,
    show_in_edit_views=True,
    section="Measurements",
    units="degC",
)

# property_label becomes: "Temperature in [degC]"
```

If your `property_label` already includes `in [units]`, it will not be modified:

```python
length = PropertyTypeAssignment(
    code="LENGTH",
    data_type=DataType.REAL,
    property_label="Length in [mm]",
    description="Length of specimen//Laenge des Probenkoerpers",
    mandatory=False,
    show_in_edit_views=True,
    section="Measurements",
    units="mm",
)

# property_label remains: "Length in [mm]"
```
