# Explanation: Schema and Masterdata Definitions

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

- `bam_masterdata/datamodel/object_types.py`
- `bam_masterdata/datamodel/dataset_types.py`
- `bam_masterdata/datamodel/collection_types.py`
- `bam_masterdata/datamodel/vocabulary_types.py`

These files contain the actual BAM type catalog (classes with real codes, descriptions, and assignments).

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
- Inheritance between Object Types is supported through dotted codes (for example `PARENT.CHILD` style codes).

!!! info
    In a future refactoring, the `code` of each Object Type, Vocabulary, and assigned Property Type should be unique. Inheritance
    will still be possible, but the handling of dotted paths will be moved to a hidden layer for the end user.

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
