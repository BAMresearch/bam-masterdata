import pytest

from bam_masterdata.datamodel.v1.base_objects import Activity, Entity, Root
from bam_masterdata.metadata.definitions import DataType


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


def test_instance_values_serialize():
    root = Root()
    assert root.to_dict() == {}
    root.name = "My sample"
    root.global_id = "111-111-111"
    root.hash = "abc123"
    assert root.to_dict() == {
        "name": "My sample",
        "global_id": "111-111-111",
        "hash": "abc123",
    }
