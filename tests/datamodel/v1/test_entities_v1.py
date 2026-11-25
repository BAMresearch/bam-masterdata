import pytest

from bam_masterdata.datamodel.v1.base_objects import Root
from bam_masterdata.datamodel.v1.entities import (
    Animal,
    BAMPerson,
    Chemical,
    Classification,
    Context,
    Device,
    Document,
    Equipment,
    Instrument,
    Location,
    Material,
    MaterialEntity,
    Organism,
    ParameterSet,
    Person,
    PhysicalObject,
    Sample,
    Sensor,
    Software,
)
from bam_masterdata.metadata.definitions import DataType

ENTITY_CLASSES = [
    Context,
    Software,
    ParameterSet,
    Classification,
    Document,
    Location,
    MaterialEntity,
    Organism,
    Animal,
    Person,
    BAMPerson,
    PhysicalObject,
    Device,
    Instrument,
    Sensor,
    Equipment,
    Sample,
    Material,
    Chemical,
]

INVENTORY_PROPERTIES = {
    "manufacturer",
    "supplier",
    "lot_number",
    "location",
    "responsible_persons",
}


@pytest.mark.parametrize("cls", ENTITY_CLASSES, ids=lambda cls: cls.__name__)
def test_properties_are_consistent_and_inherited(cls):
    obj = cls()
    props = obj._property_metadata
    assert {"name", "description", "global_id"} <= set(props)
    assert props["name"].code == Root.name.code

    codes = [prop.code for prop in obj.properties]
    assert len(codes) == len(set(codes))
    assert set(codes) == {prop.code for prop in props.values()}

    for prop in obj.properties:
        assert prop.property_label
        assert prop.description
        assert prop.section
        if prop.data_type == DataType.CONTROLLEDVOCABULARY:
            assert prop.vocabulary_code
        if prop.data_type == DataType.OBJECT:
            assert prop.object_code


@pytest.mark.parametrize("cls", [PhysicalObject, Device, Instrument, Sensor, Equipment])
def test_physical_object_inventory_properties_are_inherited(cls):
    props = cls()._property_metadata
    assert INVENTORY_PROPERTIES <= set(props)
    assert props["responsible_persons"].multivalued is True


@pytest.mark.parametrize(
    "cls",
    [
        Context,
        Software,
        ParameterSet,
        Classification,
        Document,
        Location,
        MaterialEntity,
        Organism,
        Animal,
        Person,
        BAMPerson,
    ],
)
def test_non_physical_object_types_do_not_inherit_inventory_properties(cls):
    # Sample, Material and Chemical currently inherit MaterialEntity directly.
    assert INVENTORY_PROPERTIES.isdisjoint(cls()._property_metadata)


def test_organisms_and_physical_objects_are_separate_branches():
    assert not issubclass(Organism, PhysicalObject)
    assert not issubclass(PhysicalObject, Organism)


def test_device_subtypes_and_calibration_metadata():
    for cls in (Device, Sensor, Equipment):
        props = cls()._property_metadata
        assert "calibration_status" not in props
        assert "last_calibration" not in props


def test_physical_object_instance_values_serialize():
    device = Device()
    device.name = "Microscope A"
    device.manufacturer = "Example manufacturer"
    device.serial_number = "SN-123"
    assert device.to_dict() == {
        "name": "Microscope A",
        "manufacturer": "Example manufacturer",
        "serial_number": "SN-123",
    }
