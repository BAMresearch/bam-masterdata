import inspect
import json
import pathlib

import pytest

import bam_masterdata.datamodel.v1 as v1_package
from bam_masterdata.datamodel.v1.base_objects import Activity, Entity, Root
from bam_masterdata.metadata.definitions import (
    DataType,
    ObjectTypeDef,
    PropertyTypeAssignment,
)
from bam_masterdata.metadata.entities import ObjectType, VocabularyType
from bam_masterdata.utils import import_module

# Attribute names of the properties declared directly on each class. The flattened
# contract (codes and their order) is pinned separately in `EXPECTED_PROPERTY_ORDER`.
ROOT_PROPERTIES = {
    "name",
    "description",
    "external_identifiers",
    "hash",
    "external_references",
    "ontology_iri",
    "prev_permid",
}

ACTIVITY_PROPERTIES = {
    "start_date",
    "end_date",
    "activity_status",
    "operators",
    "objective",
    "activity_sheet",
    "inputs",
    "outputs",
}

MULTIVALUED_PROPERTIES = {
    "external_identifier",
    "external_reference",
    "operators",
    "inputs",
    "outputs",
}

# The flat, section-grouped list of codes that each type pushes to openBIS. Note that
# `START_DATE`/`END_DATE` are declared on `Activity` but appear next to the `Root`
# properties, because `section` grouping overrides declaration order.
EXPECTED_PROPERTY_ORDER = {
    "Root": [
        "$NAME",
        "DESCRIPTION",
        "EXTERNAL_IDENTIFIERS",
        "HASH",
        "EXTERNAL_REFERENCES",
        "ONTOLOGY_IRI",
        "PREV_PERMID",
    ],
    "Entity": [
        "$NAME",
        "DESCRIPTION",
        "EXTERNAL_IDENTIFIERS",
        "HASH",
        "EXTERNAL_REFERENCES",
        "ONTOLOGY_IRI",
        "PREV_PERMID",
    ],
    "Activity": [
        "$NAME",
        "DESCRIPTION",
        "EXTERNAL_IDENTIFIERS",
        "HASH",
        "EXTERNAL_REFERENCES",
        "ONTOLOGY_IRI",
        "PREV_PERMID",
        "START_DATE",
        "END_DATE",
        "ACTIVITY_STATUS",
        "OPERATORS",
        "OBJECTIVE",
        "ACTIVITY_SHEET",
        "INPUTS",
        "OUTPUTS",
    ],
}

ALL_CLASSES = [Root, Activity, Entity]


def _all_assignments():
    """Yield (class, attribute name, assignment) for every property defined directly on a class."""
    for cls in ALL_CLASSES:
        for attr_name, value in vars(cls).items():
            if isinstance(value, PropertyTypeAssignment):
                yield cls, attr_name, value


ALL_ASSIGNMENTS = list(_all_assignments())
ASSIGNMENT_IDS = [f"{cls.__name__}.{attr}" for cls, attr, _ in ALL_ASSIGNMENTS]


class TestHierarchy:
    def test_root_is_object_type(self):
        assert issubclass(Root, ObjectType)

    @pytest.mark.parametrize("cls", [Activity, Entity])
    def test_children_inherit_from_root(self, cls):
        assert cls.__bases__ == (Root,)

    def test_activity_and_entity_are_siblings(self):
        assert not issubclass(Activity, Entity)
        assert not issubclass(Entity, Activity)

    @pytest.mark.parametrize("cls", ALL_CLASSES)
    def test_instantiation(self, cls):
        instance = cls()
        assert isinstance(instance, ObjectType)
        assert instance.cls_name == cls.__name__


class TestDefs:
    @pytest.mark.parametrize(
        "cls, code, prefix",
        [
            (Root, "ROOT", "ROOT"),
            (Activity, "ACTIVITY", "ACT"),
            (Entity, "ENTITY", "ENT"),
        ],
    )
    def test_code_and_prefix(self, cls, code, prefix):
        assert isinstance(cls.defs, ObjectTypeDef)
        assert cls.defs.code == code
        assert cls.defs.generated_code_prefix == prefix

    @pytest.mark.parametrize("cls", ALL_CLASSES)
    def test_defs_are_not_inherited(self, cls):
        """Each class must declare its own `defs` rather than reuse its parent's."""
        assert "defs" in vars(cls)

    def test_codes_are_unique(self):
        codes = [cls.defs.code for cls in ALL_CLASSES]
        assert len(codes) == len(set(codes))

    def test_generated_code_prefixes_are_unique(self):
        """`generated_code_prefix` defaults to `code[:3]`, so it must be set explicitly."""
        prefixes = [cls.defs.generated_code_prefix for cls in ALL_CLASSES]
        assert len(prefixes) == len(set(prefixes))

    @pytest.mark.parametrize("cls", ALL_CLASSES)
    def test_bilingual_descriptions(self, cls):
        assert cls.defs.description
        assert cls.defs.description_de
        assert cls.defs.openbis_description == (
            f"{cls.defs.description}//{cls.defs.description_de}"
        )

    @pytest.mark.parametrize(
        "cls, prev_versions",
        [
            (Root, ["ENTRY:v0"]),
            (Activity, ["EXPERIMENTAL_STEP:v0"]),
            (Entity, None),
        ],
    )
    def test_prev_versions(self, cls, prev_versions):
        assert cls.defs.prev_versions == prev_versions

    @pytest.mark.parametrize(
        "cls, iri",
        [
            (Root, None),
            (
                Activity,
                [
                    "http://purl.obolibrary.org/obo/BFO_0000015",
                    "http://www.w3.org/ns/prov#Activity",
                ],
            ),
            (
                Entity,
                [
                    "http://purl.obolibrary.org/obo/BFO_0000002",
                    "http://www.w3.org/ns/prov#Entity",
                ],
            ),
        ],
    )
    def test_iri(self, cls, iri):
        assert cls.defs.iri == iri


class TestProperties:
    def test_root_properties(self):
        assert set(Root()._property_metadata) == ROOT_PROPERTIES

    def test_entity_inherits_exactly_root_properties(self):
        assert set(Entity()._property_metadata) == ROOT_PROPERTIES

    def test_activity_properties(self):
        assert (
            set(Activity()._property_metadata) == ROOT_PROPERTIES | ACTIVITY_PROPERTIES
        )

    @pytest.mark.parametrize("cls", ALL_CLASSES)
    def test_property_codes_are_unique(self, cls):
        """There is no de-duplication across the MRO, so an inherited property must
        never be redeclared on a child."""
        codes = [p.code for p in cls().properties]
        assert len(codes) == len(set(codes))

    @pytest.mark.parametrize("cls", ALL_CLASSES, ids=lambda c: c.__name__)
    def test_attribute_names_match_codes(self, cls):
        """A Python attribute name is the lowercase form of its `code`, minus the
        `$` prefix of openBIS-native properties."""
        for attr_name, value in vars(cls).items():
            if isinstance(value, PropertyTypeAssignment):
                assert attr_name == value.code.lstrip("$").lower()

    @pytest.mark.parametrize(
        "cls, attr_name, prop", ALL_ASSIGNMENTS, ids=ASSIGNMENT_IDS
    )
    def test_all_properties_are_optional(self, cls, attr_name, prop):
        assert prop.mandatory is False

    @pytest.mark.parametrize(
        "cls, attr_name, prop", ALL_ASSIGNMENTS, ids=ASSIGNMENT_IDS
    )
    def test_all_properties_are_bilingual(self, cls, attr_name, prop):
        assert prop.property_label
        assert prop.description
        assert prop.description_de

    @pytest.mark.parametrize(
        "cls, attr_name, prop", ALL_ASSIGNMENTS, ids=ASSIGNMENT_IDS
    )
    def test_controlled_vocabulary_has_vocabulary_code(self, cls, attr_name, prop):
        if prop.data_type == DataType.CONTROLLEDVOCABULARY:
            assert prop.vocabulary_code == prop.code
        else:
            assert prop.vocabulary_code is None

    @pytest.mark.parametrize(
        "cls, attr_name, prop", ALL_ASSIGNMENTS, ids=ASSIGNMENT_IDS
    )
    def test_object_properties_have_object_code(self, cls, attr_name, prop):
        if prop.data_type == DataType.OBJECT:
            assert prop.object_code
        else:
            assert prop.object_code is None

    @pytest.mark.parametrize(
        "attr_name, object_code",
        [("operators", "PERSON"), ("inputs", "ENTITY"), ("outputs", "ENTITY")],
    )
    def test_activity_object_codes(self, attr_name, object_code):
        assert vars(Activity)[attr_name].object_code == object_code

    def test_inputs_and_outputs_point_to_entity(self):
        """`INPUTS`/`OUTPUTS` must reference the code of the `Entity` class in this module."""
        assert Activity.inputs.object_code == Entity.defs.code
        assert Activity.outputs.object_code == Entity.defs.code

    @pytest.mark.parametrize(
        "cls, attr_name, prop", ALL_ASSIGNMENTS, ids=ASSIGNMENT_IDS
    )
    def test_multivalued_properties(self, cls, attr_name, prop):
        assert prop.multivalued is (attr_name in MULTIVALUED_PROPERTIES)


class TestFlattenedProperties:
    """openBIS has no type inheritance: what it receives is the flat `properties` list
    produced on instantiation, regrouped by `section`."""

    @pytest.mark.parametrize("cls", ALL_CLASSES, ids=lambda c: c.__name__)
    def test_property_order(self, cls):
        codes = [p.code for p in cls().properties]
        assert codes == EXPECTED_PROPERTY_ORDER[cls.__name__]

    @pytest.mark.parametrize("cls", ALL_CLASSES, ids=lambda c: c.__name__)
    def test_sections_are_contiguous(self, cls):
        """A section must appear as a single run; a typo in one `section` string would
        split it into two blocks in the openBIS form."""
        sections = [p.section for p in cls().properties]
        runs = [s for i, s in enumerate(sections) if i == 0 or s != sections[i - 1]]
        assert len(runs) == len(set(runs)), sections

    def test_activity_sections(self):
        sections = [p.section for p in Activity().properties]
        runs = [s for i, s in enumerate(sections) if i == 0 or s != sections[i - 1]]
        assert runs == ["General Information", "Activity Details", "Inputs and Outputs"]

    @pytest.mark.parametrize("cls", ALL_CLASSES, ids=lambda c: c.__name__)
    def test_properties_match_property_metadata(self, cls):
        instance = cls()
        assert len(instance.properties) == len(instance._property_metadata)
        assert {p.code for p in instance.properties} == {
            p.code for p in instance._property_metadata.values()
        }


class TestExport:
    @pytest.mark.parametrize("cls", ALL_CLASSES, ids=lambda c: c.__name__)
    def test_model_to_dict(self, cls):
        """The export payload carries the type definition plus the flattened properties."""
        exported = cls().model_to_dict()
        assert exported["defs"]["code"] == cls.defs.code
        assert exported["defs"]["generated_code_prefix"] == (
            cls.defs.generated_code_prefix
        )
        assert [p["code"] for p in exported["properties"]] == (
            EXPECTED_PROPERTY_ORDER[cls.__name__]
        )

    @pytest.mark.parametrize("cls", ALL_CLASSES, ids=lambda c: c.__name__)
    def test_model_to_json_round_trip(self, cls):
        assert json.loads(cls().model_to_json()) == cls().model_to_dict()


class TestInstanceValues:
    def test_unset_values_are_not_serialized(self):
        assert Activity().to_dict() == {}

    def test_set_values_are_serialized(self):
        root = Root()
        root.name = "My sample"
        root.hash = "abc123"
        assert root.to_dict() == {"name": "My sample", "hash": "abc123"}

    def test_entity_has_no_activity_properties(self):
        entity = Entity()
        for attr_name in ACTIVITY_PROPERTIES:
            assert attr_name not in entity._property_metadata


def _declared_codes(base: type) -> set[str]:
    """Codes of every `base` subclass declared anywhere in the `datamodel` package.

    Both version subpackages are scanned on purpose: v1 is being built on top of v0 and
    is expected to reference v0 types rather than redefine them. Note this deliberately
    does NOT use `DATAMODEL_DIR`, which currently resolves to `datamodel/v0` only.
    """
    codes = set()
    datamodel_dir = pathlib.Path(v1_package.__file__).parent.parent
    for path in sorted(datamodel_dir.rglob("*.py")):
        if path.name.startswith("_"):
            continue
        module = import_module(module_path=str(path.resolve()))
        for _, obj in inspect.getmembers(module, inspect.isclass):
            if obj.__module__ != module.__name__ or not hasattr(obj, "defs"):
                continue
            if issubclass(obj, base):
                codes.add(obj.defs.code)
    return codes


OBJECT_CODES = _declared_codes(ObjectType)
VOCABULARY_CODES = _declared_codes(VocabularyType)

# References that neither v0 nor v1 defines yet. `strict=True` means the test turns red
# once the type lands, so the marker has to be removed rather than lingering.
UNDEFINED_REFERENCES = {
    "ONTOLOGY_IRI": "`ONTOLOGY_IRI` vocabulary is not written yet in v1/vocabularies.py",
}


def _reference_params(kind: str):
    """Build (class, property, target code) params, xfailing the known-missing targets."""
    params = []
    for cls, attr_name, prop in ALL_ASSIGNMENTS:
        target = prop.object_code if kind == "OBJECT" else prop.vocabulary_code
        if not target:
            continue
        param = pytest.param(
            target,
            id=f"{cls.__name__}.{attr_name}->{target}",
            marks=(
                [pytest.mark.xfail(reason=UNDEFINED_REFERENCES[target], strict=True)]
                if target in UNDEFINED_REFERENCES
                else []
            ),
        )
        params.append(param)
    return params


class TestReferences:
    """Every `object_code`/`vocabulary_code` must name a type that exists in v0 or v1.

    `PropertyTypeAssignment` does not validate these, and openBIS only rejects them at
    push time, so a typo or a not-yet-written type is otherwise silent.
    """

    @pytest.mark.parametrize("target", _reference_params("OBJECT"))
    def test_object_references_resolve(self, target):
        assert target in OBJECT_CODES

    @pytest.mark.parametrize("target", _reference_params("VOCABULARY"))
    def test_vocabulary_references_resolve(self, target):
        assert target in VOCABULARY_CODES
