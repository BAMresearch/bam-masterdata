# Metadata Entities Module

This page explains the role of [`bam_masterdata/metadata/entities.py`](../../bam_masterdata/metadata/entities.py), which is the runtime counterpart to `definitions.py`.

If `definitions.py` describes the schema, `entities.py` is the module that turns those declarations into working Python entities with validation, serialization, RDF export, and openBIS synchronization behavior.

## Core idea

Classes in `entities.py` are designed to be subclassed in the datamodel modules under `bam_masterdata/datamodel/`.

Each concrete class usually contains:

- one `defs` attribute holding a `*Def` model from `definitions.py`
- several `PropertyTypeAssignment` attributes for object-like entities
- or several `VocabularyTerm` attributes for vocabulary entities

The runtime classes inspect those class attributes and build convenient lists and metadata structures from them automatically.

## Main classes

### `BaseEntity`

`BaseEntity` is the common foundation for the metadata entity hierarchy. It provides:

- assignment-time validation in `__setattr__`
- human-readable `__repr__`
- property metadata discovery through `get_property_metadata()`
- JSON and dict serialization through `to_json()` and `to_dict()`
- HDF5 serialization through `to_hdf5()`
- model export helpers through `model_to_dict()` and `model_to_json()`
- RDF export helpers through `model_to_rdf()`

One important implementation detail is that `BaseEntity` inspects class attributes of type `PropertyTypeAssignment`. That inspection is what lets a concrete type declare its properties declaratively instead of building everything by hand in `__init__`.

### `VocabularyType`

`VocabularyType` extends `BaseEntity` for controlled vocabularies.

Its main job is to collect `VocabularyTerm` class attributes into the runtime `terms` list. That list is then reused by:

- JSON export
- checker logic
- Excel export
- mocked and real openBIS upload code

`to_openbis()` on this class handles two cases:

- the vocabulary already exists and only missing terms need to be added
- the vocabulary does not exist and must be created with its terms

### `ObjectType`

`ObjectType` is the central runtime class for object-like entity types, and it is also the parent for collection and dataset behavior in this package.

Its main responsibilities are:

- collect `PropertyTypeAssignment` class attributes into `properties`
- validate values assigned to those properties
- support special handling for `TIMESTAMP`, `OBJECT`, and `CONTROLLEDVOCABULARY`
- serialize instances for export or storage
- push new definitions to openBIS

The custom `__setattr__` is especially important. It turns the static property metadata from `definitions.py` into actual runtime validation.

#### Special value handling

`ObjectType.__setattr__` contains a few important cases:

- `TIMESTAMP`: accepts either a `datetime` object or an ISO-style string
- `OBJECT`: accepts either another `ObjectType` instance or an openBIS object path string
- `CONTROLLEDVOCABULARY`: validates the assigned term against the referenced vocabulary definition, unless it belongs to a known institutional vocabulary that is intentionally not checked locally

This is the part of the code that makes object instances feel schema-aware.

### `CollectionType`

`CollectionType` extends `ObjectType`, but adds an in-memory container role. It can:

- attach object instances
- generate local object identifiers
- record parent/child relationships

This is especially useful in parser workflows where data files create several related objects before any persistence step happens.

### `DatasetType`

`DatasetType` is another `ObjectType` specialization. In the current package structure it mostly reuses common object-type behavior while representing the openBIS dataset family.

## How class declarations become runtime metadata

The runtime classes work by introspecting the inheritance chain.

For object-like entities:

- `PropertyTypeAssignment` attributes are collected from parent and child classes
- they are grouped into the `properties` list
- their metadata is also available through `_property_metadata`

For vocabularies:

- `VocabularyTerm` attributes are collected into `terms`

This means that a class such as:

```python
class Instrument(ObjectType):
    defs = ObjectTypeDef(...)
    name = PropertyTypeAssignment(...)
    alias = PropertyTypeAssignment(...)
```

automatically becomes a runtime model with:

- `defs`
- `_property_metadata["name"]`
- `_property_metadata["alias"]`
- `properties == [name_assignment, alias_assignment]`

without requiring the author to manually maintain those structures.

## Serialization helpers

`entities.py` supports multiple output shapes because different parts of the repository need different representations.

### Instance serialization

- `to_dict()` returns the values currently assigned to an entity instance
- `to_json()` is the JSON equivalent

This is runtime data, not the full schema definition.

### Model serialization

- `model_to_dict()` exports the class model including `defs` and property/term definitions
- `model_to_json()` is the JSON equivalent

This is the representation used by `EntitiesDict`, CLI exports, and checker workflows.

### HDF5 export

`to_hdf5()` stores runtime instance values into a group named after the entity type unless a group name is provided explicitly.

### RDF export

`model_to_rdf()` translates entity definitions into RDF triples. It creates:

- entity nodes
- labels and descriptions
- property nodes
- mandatory/optional property restrictions
- object-reference restrictions for `OBJECT` properties

This is the ontology-facing export path of the metadata model.

## openBIS synchronization

The module also contains logic to push definitions into openBIS.

There are two patterns:

- shared legacy helper logic in `BaseEntity._to_openbis()`
- explicit entity-family methods such as `VocabularyType.to_openbis()` and `ObjectType.to_openbis()`

Those methods are responsible for tasks such as:

- checking whether an entity already exists
- creating missing property types
- assigning properties to a type
- adding missing vocabulary terms

For local testing, these methods can be exercised entirely with mocks because the code only relies on a small set of openBIS interactions.

## Relationship to `entities_dict.py`

`entities.py` defines the runtime export shape, while `entities_dict.py` walks over Python modules and calls `model_to_dict()` on the classes it finds.

That division of labor is useful:

- `entities.py` knows how one entity serializes itself
- `entities_dict.py` knows how to discover many entity classes across modules and enrich them with source line locations

## Why this module matters for the CLI

Many CLI features depend on `entities.py` directly or indirectly:

- exporting masterdata to JSON or Excel
- validating parser-created collections of objects
- comparing definitions with checker workflows
- pushing definitions to openBIS

Because of that, this module is one of the key bridges between static schema declarations and real operational behavior in the repository.
