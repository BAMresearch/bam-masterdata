# Define object types and properties

This guide explains how to declare operational openBIS object types in `bam-masterdata`, using the **explicit-code and Python-inheritance conventions for v1**. It also identifies which behavior remains valid for the existing v0 model.

The v1 refactor is tracked in [issue #395](https://github.com/BAMresearch/bam-masterdata/issues/395). Code identity, hierarchy inspection, and schema validation are covered by [issue #428](https://github.com/BAMresearch/bam-masterdata/issues/428). The complete v1 type catalog is still under development.

## 1. Choose the correct datamodel version and module

- **v0:** `bam_masterdata/datamodel/v0/` contains the existing definitions and domain subpackages. Preserve their identifiers and behavior; the refactor does not automatically migrate existing objects.
- **v1:** `bam_masterdata/datamodel/v1/` is the target package for new ontology-informed definitions. Initial base classes belong in `base_objects.py` (see [PR #401](https://github.com/BAMresearch/bam-masterdata/pull/401)); activity, entity, vocabulary, and domain-specific modules are being introduced in stages under #395.

Follow the version's existing module organization rather than creating a new top-level schema package. Avoid imports across v0 and v1 unless there is an explicit compatibility or migration reason.

## 2. Declare an object type and its parent

Each concrete class is an `ObjectType` subclass (directly or indirectly) and declares its **own** `ObjectTypeDef`. A v1 code is a stable openBIS identifier, **not an inheritance path**.

The following self-contained example illustrates the convention; it is not a declaration of additional production v1 classes:

```python
from bam_masterdata.metadata.definitions import (
    ObjectTypeDef,
    PropertyTypeAssignment,
)
from bam_masterdata.metadata.entities import ObjectType


class Root(ObjectType):
    defs = ObjectTypeDef(
        code="ROOT",
        description="Common root of this example schema",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="Human-readable name",
        mandatory=True,
        section="General Information",
    )


class Entity(Root):
    defs = ObjectTypeDef(
        code="ENTITY",
        description="A physical or informational entity",
    )


class Person(Entity):
    defs = ObjectTypeDef(
        code="PERSON",
        description="A person",
        generated_code_prefix="PER",
    )


assert Person.defs.code == "PERSON"
assert Person.get_hierarchy() == ["ROOT", "ENTITY", "PERSON"]
assert Person.is_subtype_of(Entity)
```

**Rules for v1:**

1. Define `ObjectTypeDef.code` explicitly, using a simple uppercase identifier such as `MATERIAL_ENTITY` or `PERSON`. Do not generate it from the Python class name or concatenate parent codes.
2. Use Python class inheritance for shared properties and hierarchy. A subclass can override an inherited property assignment.
3. Keep the object type code (`Person.defs.code`) separate from an object's instance code (`person.code`).
4. `generated_code_prefix` controls instance code generation and can be supplied explicitly; when omitted, its current fallback is derived from the beginning of `code`.
5. Legacy dotted v0 codes, such as `EXPERIMENTAL_STEP.DCPD`, remain supported. Do not rewrite them during v1 development.

## 3. Inspect inheritance

```python
Person.get_hierarchy()  # ["ROOT", "ENTITY", "PERSON"]
Person.get_hierarchy_path()  # "ROOT.ENTITY.PERSON"
Person.is_subtype_of(Entity)  # True
```

The path is a **computed description of Python ancestry**, not an identifier sent to openBIS. Classes that lack their own `ObjectTypeDef` are excluded from the hierarchy output, and multiple object-type parents are not supported by path introspection.

## 4. Define property assignments

Declare `PropertyTypeAssignment` objects as class attributes:

```python
class Instrument(Entity):
    defs = ObjectTypeDef(
        code="INSTRUMENT",
        description="An instrument",
        generated_code_prefix="INS",
    )

    manufacturer = PropertyTypeAssignment(
        code="MANUFACTURER",
        data_type="VARCHAR",
        property_label="Manufacturer",
        description="Instrument manufacturer",
        mandatory=False,
        section="General Information",
    )

    responsible_person = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON",
        property_label="Responsible person",
        description="Person responsible for the instrument",
        mandatory=False,
        section="General Information",
    )
```

Common fields:

| Field | Purpose |
| --- | --- |
| `code` | Property type identifier in openBIS. |
| `data_type` | `DataType` enum value or its equivalent string, such as `VARCHAR`, `REAL`, `TIMESTAMP`, `OBJECT`, `CONTROLLEDVOCABULARY`, or `XML`. |
| `property_label`, `description` | Human-readable metadata. Optional separate translated fields are supported by current definitions; `//`-separated legacy text remains compatible. |
| `mandatory` | **Required** Boolean: whether the assignment is mandatory. |
| `section` | **Required** string: where the property appears in the user interface. |
| `show_in_edit_views` | Whether to display the property in edit views (default: `True`). |
| `vocabulary_code` | Target vocabulary for `CONTROLLEDVOCABULARY` properties. |
| `object_code` | Optional target object type for `OBJECT` properties. |
| `multivalued` | Whether multiple values are allowed (default: `False`). |
| `units` | Optional pint-compatible unit expression. |

A subclass can replace a property assignment by assigning the same Python attribute name. Validate the resulting inherited property set rather than assuming every declared ancestor property is always active unchanged.

## 5. Add OBJECT references

`object_code` is a **concrete openBIS object type code**:

```python
responsible_person = PropertyTypeAssignment(
    code="RESPONSIBLE_PERSON",
    data_type="OBJECT",
    object_code="PERSON",
    property_label="Responsible person",
    description="Responsible person reference",
    mandatory=False,
    section="General Information",
)
```

The current semantics intentionally **do not** use Python subtype relationships to widen reference constraints. `object_code="ENTITY"` does not automatically mean “any `Entity` subclass.”

To declare an unrestricted reference, use `object_code=None` (or the legacy `"(ALL)"`):

```python
related_object = PropertyTypeAssignment(
    code="RELATED_OBJECT",
    data_type="OBJECT",
    object_code=None,
    property_label="Related object",
    description="Reference to another object",
    mandatory=False,
    section="Relationships",
)
```

For a restricted OBJECT property, synchronization sends the chosen code as the PyBIS `sampleType` constraint. For unrestricted properties, it omits that constraint. When an existing openBIS property's target differs from the definition, synchronization reports a rejected change rather than silently converting the constraint.

**Scope:** checking that `object_code="PERSON"` names a known schema type is different from checking the type of a particular `Person` instance at runtime. The schema validator does **not** perform runtime parser validation. See [Work with Object References](./object_references.md).

## 6. Controlled vocabularies and units

A controlled-vocabulary property identifies its vocabulary:

```python
status = PropertyTypeAssignment(
    code="ACTIVITY_STATUS",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="ACTIVITY_STATUS",
    property_label="Activity status",
    description="Current activity lifecycle status",
    mandatory=False,
    section="Activity Details",
)
```

Vocabularies and their terms must be defined in the relevant version and synchronized in a suitable order. Defining the complete v1 vocabulary catalog is part of #395.

For quantitative properties, specify optional pint-compatible units:

```python
length = PropertyTypeAssignment(
    code="LENGTH",
    data_type="REAL",
    property_label="Length",
    description="Measured length",
    mandatory=False,
    section="Measurements",
    units="mm",
)

assert length.property_label == "Length in [mm]"
```

If a label already includes the expected `in [units]` format, it is retained. Incompatible bracketed labels or unrecognized units fail validation. These formatting rules apply to the current metadata definitions, not only v1.

## 7. Validate the schema before synchronization

For a versioned package that exists in the installed checkout:

```python
from bam_masterdata.checker.schema_validator import (
    get_object_types,
    validate_object_references,
    validate_object_type_codes,
)

object_types = get_object_types("v1")
validate_object_type_codes(object_types)
validate_object_references(object_types)
```

`get_object_types()` discovers declared `ObjectType` classes in the selected version's Python modules and subpackages. The validators reject duplicate codes and unknown restricted OBJECT targets. `None` and `"(ALL)"` targets are unrestricted.

**Important:** This is an explicit validation step; it does not run automatically during parsing or synchronization. Do not mix classes from different versions in the same validation list. Complete v1 validation will be possible when its modules are integrated.

## 8. Synchronize and test

`ObjectType.to_openbis_sync()` registers object types using `defs.code`, including simple v1 codes. Parser workflows also use `object_instance.defs.code` for the openBIS type and keep `object_instance.code` as the instance identifier.

Relevant regression tests include:

```bash
uv run pytest \
    tests/checker/test_schema_validator.py \
    tests/datamodel/test_v0_compatibility.py \
    tests/metadata/test_entities.py \
    tests/metadata/test_object_data_type.py \
    tests/cli/test_v1_run_parser_compatibility.py -v
```

These tests cover unit behavior and mocked PyBIS interactions. They **do not** prove successful provisioning of the v1 catalog in a real server.

As tracked in [#395](https://github.com/BAMresearch/bam-masterdata/issues/395), remaining v1 work includes module and vocabulary completion, representative export/serialization tests, migration compatibility, disposable openBIS 7 provisioning, idempotent repeated synchronization, property/type updates, permissions/system-managed definitions, and broader CI coverage. Do not assume an object type is deployed just because its Python definition is valid.

See also [Schema Definitions](../explanations/schema_defs.md).