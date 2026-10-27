# Schema definitions and datamodel versions

`bam-masterdata` defines, validates, exports, and synchronizes the **masterdata** used by a BAM openBIS instance. Masterdata describes which object types, properties, controlled vocabularies, and assignments exist; it is distinct from the scientific data stored in individual objects and datasets.

This page describes the current Python architecture, the compatibility rules introduced by [issue #428](https://github.com/BAMresearch/bam-masterdata/issues/428), and the ongoing v1 schema redesign tracked in [issue #395](https://github.com/BAMresearch/bam-masterdata/issues/395). **The v1 design is work in progress:** examples of proposed types or modules should not be interpreted as a complete, deployed schema.

## Layers and responsibilities

| Location | Responsibility |
| --- | --- |
| `bam_masterdata/metadata/definitions.py` | Pydantic definitions: `ObjectTypeDef`, `PropertyTypeAssignment`, vocabulary definitions and terms, data types, and associated metadata. |
| `bam_masterdata/metadata/entities.py` | Python entity classes (`ObjectType`, `VocabularyType`, etc.), inherited properties, object values, serialization, and openBIS synchronization. |
| `bam_masterdata/metadata/entities_dict.py` | Discover definitions in supplied Python modules, instantiate them, and serialize them for downstream exchange. |
| `bam_masterdata/checker/` | Validation of masterdata and, in `schema_validator.py`, validation of Python object-type classes and references. |
| `bam_masterdata/datamodel/v0/` | The existing BAM definitions, retained for compatibility. |
| `bam_masterdata/datamodel/v1/` | The new ontology-informed datamodel being developed in separate work. |
| `bam_masterdata/cli/run_parser.py` and `bam_masterdata/parsing/` | Parsing files into objects, resolving object references, and sending data to openBIS. |

Python classes are the source of schema definitions. They are not an OWL ontology: their inheritance and optional ontology references inform the model, but openBIS object type codes and property constraints remain concrete operational identifiers.

## Versioned schema layout

### v0: existing definitions

The `v0` package contains general modules such as `object_types.py`, `activities.py`, `instruments.py`, `vocabulary_types.py`, `collection_types.py`, and `dataset_types.py`, plus domain-specific subpackages such as `welding/`, `creep_test/`, `ellipsometry/`, `building_materials/`, and `mass_spectrometry/`.

Some v0 object type codes are dotted, for example `EXPERIMENTAL_STEP.DCPD` and `CONSUMABLE.WELDING`. **These remain valid.** The v1 identity rules do not rewrite v0 identifiers or imply an automatic migration of existing openBIS objects.

### v1: ontology-informed refactor (in progress)

[Issue #395](https://github.com/BAMresearch/bam-masterdata/issues/395) coordinates the staged refactor. The intended hierarchy branches into activities (such as experiments and computations) and entities (such as contexts, locations, and material entities). Further classes, vocabularies, and domain-specific modules are planned; their final organization is not yet fixed.

The rollout plan includes:

1. Define base types and their shared properties.
2. Extend activity and entity branches and organize additional base modules where useful.
3. Review and define vocabularies.
4. Test schema provisioning and repeated `masterdata_sync` operations in openBIS 7.
5. Organize existing experimental-step and instrument definitions into use-case/domain subpackages.
6. Test exports, compatibility, migration metadata, and CI behavior as the v1 catalog grows.


## Object type identity versus Python inheritance

Every `ObjectType` definition explicitly declares an `ObjectTypeDef.code`. For v1, use simple, stable uppercase codes such as `ROOT`, `ACTIVITY`, `ENTITY`, and `PERSON` instead of encoding ancestry into the identifier.

```python
from bam_masterdata.metadata.definitions import ObjectTypeDef
from bam_masterdata.metadata.entities import ObjectType


class Root(ObjectType):
    defs = ObjectTypeDef(code="ROOT", description="Root type")


class Entity(Root):
    defs = ObjectTypeDef(code="ENTITY", description="Entity type")


class Person(Entity):
    defs = ObjectTypeDef(code="PERSON", description="Person type")


assert Person.defs.code == "PERSON"
assert Person.get_hierarchy() == ["ROOT", "ENTITY", "PERSON"]
assert Person.get_hierarchy_path() == "ROOT.ENTITY.PERSON"
assert Person.is_subtype_of(Entity)
```

The hierarchy is computed from Python inheritance; it is **not** a persisted Pydantic field or a replacement openBIS code. `get_hierarchy()` excludes framework classes and ancestor classes without their own `ObjectTypeDef`. Multiple object-type parents are explicitly unsupported by hierarchy-path introspection. `is_subtype_of()` follows ordinary Python subclass relationships.

`generated_code_prefix` controls generated *object instance* codes and is separate from the *object type* code and hierarchy. Existing defaults and explicitly declared prefixes remain supported.

## Properties and OBJECT references

Properties are declared on classes using `PropertyTypeAssignment`; inherited properties can be overridden in subclasses. Relevant fields include `code`, `data_type`, `property_label`, `description`, `mandatory`, `section`, `vocabulary_code`, `object_code`, and `units`.

For a typed OBJECT reference:

```python
from bam_masterdata.metadata.definitions import PropertyTypeAssignment

operator = PropertyTypeAssignment(
    code="OPERATOR",
    data_type="OBJECT",
    object_code="PERSON",
    property_label="Operator",
    description="Person responsible for the activity",
    mandatory=False,
    section="Activity Details",
)
```

`object_code="PERSON"` names the **exact openBIS target type**. It does **not** mean that any Python subtype of `PERSON` is automatically accepted. A reference to a parent type similarly does not imply polymorphic openBIS reference constraints.

`object_code=None` and legacy `object_code="(ALL)"` denote unrestricted OBJECT references. The schema validator allows both; synchronization omits the `sampleType` constraint when creating such a property. The actual value assigned while parsing must still be a supported object reference, such as an `ObjectType` instance with a code or a valid openBIS identifier path.

A **property's target-type declaration**, a **Python object's subclass relationship**, and an **instance's identifier** are three different concepts. Schema validation does not replace runtime object or openBIS server validation.

## Validate Python schema classes

The validator introduced in #428 operates on Python **classes**, not the serialized dictionaries emitted by `EntitiesDict`:

```python
from bam_masterdata.checker.schema_validator import (
    get_object_types,
    validate_object_references,
    validate_object_type_codes,
)

# Run this when the selected version's package is present.
object_types = get_object_types("v1")
validate_object_type_codes(object_types)
validate_object_references(object_types)
```

- `get_object_types(version)` imports the selected version package and subpackages and returns locally defined `ObjectType` subclasses that declare their own `ObjectTypeDef`.
- `validate_object_type_codes(classes)` rejects duplicate declared codes.
- `validate_object_references(classes)` checks that restricted OBJECT `object_code` targets are present in the **supplied class set** and accepts unrestricted references.

**Important limitations:** discovery and validation do not constitute a new registry; calling code is responsible for selecting the intended version. Mixed class lists can give misleading results. The validators are not automatically invoked by the parser or synchronization. The full v1 package will need its own discovery and validation tests once integrated.

## Synchronization, parsing, and exports

`ObjectType.to_openbis_sync()` registers or queries openBIS object types using `self.defs.code`, not `get_hierarchy_path()`. Existing OBJECT property target mismatches are reported as rejected synchronization changes rather than silently rewritten. Unit tests cover the registration calls and comparison logic; the exact representation returned by PyBIS and behavior against openBIS 7 must also be verified in integration tests.

The parser classes in `bam_masterdata/cli/run_parser.py` similarly create objects with `type=object_instance.defs.code`, while `object_instance.code` identifies the individual record. Mock-based compatibility tests cover ordinary and transactional parsing, same-batch OBJECT references, and fallback destination resolution.

The repository also supports exchange and inspection through Python-to-JSON/Excel/RDF exports, Python generation from upstream sources, and the existing masterdata checker. `EntitiesDict` performs instantiation/serialization and is separate from the new class-level validator. Version-specific export and serialization coverage for v1 remains part of #395.

## Verification and next work

The #428 branch includes focused tests in:

- `tests/checker/test_schema_validator.py`
- `tests/datamodel/test_v0_compatibility.py`
- `tests/metadata/test_entities.py`
- `tests/cli/test_v1_run_parser_compatibility.py`

These provide unit and **mocked workflow** coverage; they do not prove live openBIS 7 compatibility. [Issue #395](https://github.com/BAMresearch/bam-masterdata/issues/395) additionally tracks disposable-instance provisioning, idempotent synchronization, metadata updates, handling system-managed definitions, migration/compatibility tests, representative v1 exports, and wider CI coverage. Some older CLI and `EntitiesDict` tests are currently excluded from the main CI selection and need a separate review.

See [Define Object Types and Properties](../howtos/object_types.md) and [Work with Object References](../howtos/object_references.md).
