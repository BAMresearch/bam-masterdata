import json

import pytest

from bam_masterdata.datamodel.v1.base_objects import Entity, Root
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
from bam_masterdata.metadata.definitions import DataType, ObjectTypeDef
from bam_masterdata.metadata.entities import ObjectType

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
def test_entity_types_instantiate_and_export(cls):
    obj = cls()
    assert isinstance(obj, Entity)
    assert isinstance(obj, ObjectType)
    assert isinstance(cls.defs, ObjectTypeDef)
    assert cls.defs.code
    assert cls.defs.description.strip()

    exported = obj.model_to_dict()
    assert exported["defs"]["code"] == cls.defs.code
    assert json.loads(obj.model_to_json()) == exported


@pytest.mark.parametrize(
    "child, parent",
    [
        (Context, Entity),
        (Software, Context),
        (ParameterSet, Context),
        (Classification, Context),
        (Document, Context),
        (Location, Entity),
        (MaterialEntity, Entity),
        (Organism, MaterialEntity),
        (Animal, Organism),
        (Person, Animal),
        (BAMPerson, Person),
        (PhysicalObject, MaterialEntity),
        (Device, PhysicalObject),
        (Instrument, Device),
        (Sensor, Device),
        (Equipment, Device),
        (Sample, MaterialEntity),
        (Material, MaterialEntity),
        (Chemical, MaterialEntity),
    ],
)
def test_entity_hierarchy(child, parent):
    assert issubclass(child, parent)


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
    assert props["manufacturer"].code == "MANUFACTURER"
    assert props["supplier"].code == "SUPPLIER"
    assert props["lot_number"].code == "LOT_NUMBER"
    assert props["location"].object_code == "LOCATION"
    assert props["responsible_persons"].object_code == "PERSON"
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
    assert PhysicalObject.defs.code == "PHYSICAL_OBJECT"


def test_device_subtypes_and_calibration_metadata():
    assert Instrument.last_calibration.data_type == DataType.DATE
    assert Instrument.calibration_status.data_type == DataType.CONTROLLEDVOCABULARY
    assert Instrument.calibration_status.vocabulary_code == "CALIBRATION_STATUS"
    for cls in (Device, Sensor, Equipment):
        props = cls()._property_metadata
        assert "calibration_status" not in props
        assert "last_calibration" not in props


def test_chemical_identity_and_bottling_properties():
    props = Chemical()._property_metadata
    assert props["cas_number"].code == "CAS_NUMBER"
    assert props["iupac_name"].code == "IUPAC_NAME"
    assert props["molar_mass"].units == "g/mol"
    for name in ("date_bottling", "date_opening", "date_expiration"):
        assert props[name].data_type == DataType.DATE
    assert props["is_empty"].data_type == DataType.BOOLEAN


def test_sample_identity_properties():
    props = Sample()._property_metadata
    assert props["sample_id"].code == "SAMPLE_ID"
    assert props["sample_id"].mandatory is True


def test_representative_v0_mappings():
    assert "INSTRUMENT:v0" in Instrument.defs.prev_versions
    assert "SAMPLE:v0" in Sample.defs.prev_versions
    assert "CHEMICAL:v0" in Chemical.defs.prev_versions
    assert "IUPAC_NAME:v0" in Chemical.iupac_name.prev_versions
    assert "MANUFACTURER:v0" in PhysicalObject.manufacturer.prev_versions
    assert "SUPPLIER:v0" in PhysicalObject.supplier.prev_versions


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
