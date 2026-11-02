import json

import pytest

from bam_masterdata.datamodel.v1.base_objects import Activity, Entity, Root
from bam_masterdata.metadata.definitions import DataType, PropertyTypeAssignment
from bam_masterdata.metadata.entities import ObjectType


@pytest.mark.parametrize("cls", [Root, Activity, Entity])
def test_types_instantiate_and_export(cls):
    instance = cls()
    assert isinstance(instance, ObjectType)
    assert instance.defs.code == cls.defs.code
    assert instance.defs.description

    exported = instance.model_to_dict()
    assert exported["defs"]["code"] == cls.defs.code
    assert json.loads(instance.model_to_json()) == exported


def test_hierarchy():
    assert issubclass(Root, ObjectType)
    assert issubclass(Activity, Root)
    assert issubclass(Entity, Root)
    assert not issubclass(Activity, Entity)
    assert not issubclass(Entity, Activity)


def test_inherited_properties():
    root = Root()
    activity = Activity()
    entity = Entity()

    root_props = set(root._property_metadata)
    assert root_props <= set(activity._property_metadata)
    assert root_props <= set(entity._property_metadata)
    assert {"start_date", "end_date", "activity_status", "inputs", "outputs"} <= set(
        activity._property_metadata
    )
    assert "activity_status" not in entity._property_metadata


@pytest.mark.parametrize("cls", [Root, Activity, Entity])
def test_property_metadata_is_consistent(cls):
    instance = cls()
    codes = [prop.code for prop in instance.properties]
    assert len(codes) == len(set(codes))
    assert set(codes) == {prop.code for prop in instance._property_metadata.values()}

    for prop in instance.properties:
        assert prop.property_label
        assert prop.description
        assert prop.section
        if prop.data_type == DataType.CONTROLLEDVOCABULARY:
            assert prop.vocabulary_code
        if prop.data_type == DataType.OBJECT:
            assert prop.object_code


def test_essential_property_configuration():
    assert Root.name.code == "$NAME"
    assert Root.name.mandatory is True
    assert Root.external_identifiers.multivalued is True
    assert Root.external_references.multivalued is True

    assert Activity.activity_status.data_type == DataType.CONTROLLEDVOCABULARY
    assert Activity.activity_status.vocabulary_code == "ACTIVITY_STATUS"
    assert Activity.responsible_persons.object_code == "PERSON"
    assert Activity.responsible_persons.multivalued is True
    assert Activity.inputs.object_code == Entity.defs.code
    assert Activity.outputs.object_code == Entity.defs.code
    assert Activity.inputs.multivalued is True
    assert Activity.outputs.multivalued is True


def test_property_assignments_export_with_current_codes():
    exported = Activity().model_to_dict()
    exported_codes = {prop["code"] for prop in exported["properties"]}
    assert {
        "$NAME",
        "EXTERNAL_IDENTIFIER",
        "EXTERNAL_REFERENCE",
        "RESPONSIBLE_PERSON",
        "INPUT",
        "OUTPUT",
    } <= exported_codes


def test_instance_values_serialize():
    root = Root()
    assert root.to_dict() == {}
    root.name = "My sample"
    root.hash = "abc123"
    assert root.to_dict() == {"name": "My sample", "hash": "abc123"}
