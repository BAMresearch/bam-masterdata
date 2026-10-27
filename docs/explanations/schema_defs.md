# Schema Definitions

This page explains what "schema/Masterdata definitions" mean in openBIS and how they are represented in `bam-masterdata`.

## What Masterdata means in openBIS

In openBIS, Masterdata is the definition layer that tells the system:

- which entity types exist (in our case, Object Types),
- which properties are available for those types,
- which controlled vocabulary terms are allowed,

In other words, Masterdata is the metadata model (**meta-metadata**) used by the instance.

!!! info
    Note that openBIS entity types also include Collection Types and Dataset Types. As of 2026, the definitions of new types for these categories is locked, and we only accept new definitions for Object Types and Vocabularies.

## Where definitions are in this repository

The definitions are split into two layers.

### 1. Generic definition layer (abstract, reusable)

- `bam_masterdata/metadata/definitions.py`: Defines schema building blocks such as:
    - `ObjectTypeDef`, `VocabularyTypeDef`, `DatasetTypeDef`, `CollectionTypeDef`
    - `PropertyTypeAssignment`
    - `VocabularyTerm`
    - `DataType`
- `bam_masterdata/metadata/entities.py`: Defines runtime entities and behavior (validation, serialization, openBIS upload methods).

### 2. BAM datamodel layer (concrete masterdata content)

The BAM datamodel is organized into versioned Python packages:

- `bam_masterdata/datamodel/v0/`: Existing schema definitions, including
  legacy dotted object type codes.
- `bam_masterdata/datamodel/v1/`: Refactored schema definitions using
  explicit object type codes and Python class inheritance.

Individual versions may contain additional modules and domain-specific
subpackages.

Object type definitions are declared using `ObjectTypeDef`, while
properties are declared using `PropertyTypeAssignment`.

## How a definition is represented

Each concrete type class has:

- a `defs` attribute with static type metadata (`code`, `description`, optional validation/generated-code settings),
- plus `PropertyTypeAssignment` attributes (for object/collection/dataset types),
- or `VocabularyTerm` attributes (for vocabulary types).

This mirrors openBIS concepts:

- openBIS type registration -> `*TypeDef` objects in `defs`
- openBIS property assignment to a type -> `PropertyTypeAssignment`
- openBIS controlled vocabulary and terms -> `VocabularyTypeDef` + `VocabularyTerm`

`DataType` follows openBIS data types (for example `VARCHAR`, `INTEGER`, `OBJECT`, `CONTROLLEDVOCABULARY`, `XML`).

## openBIS-specific details reflected in the model

- Internal openBIS properties/vocabularies usually start with `$` (for example `$NAME`).
- Type and property codes follow openBIS conventions and are validated in the model.

### Object type codes and inheritance

In v0, some object type codes encode hierarchy using dotted identifiers,
such as `EXPERIMENTAL_STEP.DCPD`. These codes remain supported for
backward compatibility.

In v1, object type codes are simple, explicitly declared identifiers.
Inheritance is represented by Python classes, not by the object type code.

For example:

```python
class Entity(Root):
    defs = ObjectTypeDef(
        code="ENTITY",
        description="Entity",
    )


class Person(Entity):
    defs = ObjectTypeDef(
        code="PERSON",
        description="Person",
    )
```

The hierarchy can be inspected using:

```python
Person.get_hierarchy()  # ["ROOT", "ENTITY", "PERSON"]

Person.get_hierarchy_path()  # "ROOT.ENTITY.PERSON"

Person.is_subtype_of(Entity)  # True
```

These methods do not modify the codes registered in openBIS.

The object type code of Person remains `PERSON`, not `ROOT.ENTITY.PERSON`.

## Schema validation

The `bam_masterdata.checker.schema_validator` module provides utilities
for validating Python object type definitions.

```python
from bam_masterdata.checker.schema_validator import (
    get_object_types,
    validate_object_type_codes,
    validate_object_references,
)

object_types = get_object_types("v1")

validate_object_type_codes(object_types)
validate_object_references(object_types)
```

The checks verify that:

- Object type codes are unique within the selected version.
- OBJECT properties reference object types declared in that version.
- Unrestricted references using `object_code=None` or `"(ALL)"` are permitted.

An `object_code` refers to an exact openBIS object type. Python
subclasses are not automatically accepted as alternative reference types.

These checks validate schema definitions, not individual objects or
references created during parsing.

The validator is not automatically executed during synchronization
or parsing.

## How definitions move across formats

`bam-masterdata` is designed to move masterdata between Python modules, openBIS, and tabular exchange formats:

- `fill_masterdata` CLI:
    - openBIS -> Python modules, or
    - Excel -> Python modules
- `export_to_excel` CLI:
    - Python modules -> `masterdata.xlsx`
- `export_to_json` / `export_to_rdf` CLI:
    - Python modules -> JSON / RDF
- `checker` CLI:
    - validates and compares incoming model definitions against the current model

This allows teams to keep Python as the canonical source while still exchanging definitions through Excel or openBIS exports/imports.

## Mapping of terms

- openBIS "Experiment/Collection Type" <-> `CollectionTypeDef` and `CollectionType` in this package
- openBIS "Sample/Object Type" <-> `ObjectTypeDef` and `ObjectType`
- openBIS "DataSet Type" <-> `DatasetTypeDef` and `DatasetType`
- openBIS "Vocabulary/Terms" <-> `VocabularyTypeDef` and `VocabularyTerm`

See also: [How-to: Define Object Types and Properties](../howtos/object_types.md).


## Useful openBIS references:

- Data model overview: [openBIS Data Modelling](https://openbis.readthedocs.io/en/20.10.12-plus/user-documentation/advance-features/openbis-data-modelling.html)
