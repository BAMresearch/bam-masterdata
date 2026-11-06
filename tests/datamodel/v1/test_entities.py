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
    InventoryInformation,
    Location,
    Material,
    MaterialEntity,
    Organism,
    ParameterSet,
    Person,
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
    InventoryInformation,
    Location,
    MaterialEntity,
    Organism,
    Animal,
    Person,
    BAMPerson,
    Device,
    Instrument,
    Sensor,
    Equipment,
    Sample,
    Material,
    Chemical,
]


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
    "child,parent",
    [
        (Context, Entity),
        (Software, Context),
        (ParameterSet, Context),
        (Classification, Context),
        (Document, Context),
        (InventoryInformation, Context),
        (Location, Entity),
        (MaterialEntity, Entity),
        (Organism, MaterialEntity),
        (Animal, Organism),
        (Person, Animal),
        (BAMPerson, Person),
        (Device, MaterialEntity),
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
    assert {"name", "description"} <= set(props)
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


def test_inventory_information_is_context_not_material_entity():
    assert issubclass(InventoryInformation, Context)
    assert not issubclass(InventoryInformation, MaterialEntity)
    assert InventoryInformation.defs.code == "INVENTORY_INFORMATION"
    assert {
        "manufacturer",
        "supplier",
        "lot_number",
        "location",
        "responsible_persons",
        "date_bottling",
        "date_opening",
        "date_expiration",
        "is_empty",
    } <= set(InventoryInformation()._property_metadata)


def test_inventory_reference_configuration():
    props = InventoryInformation()._property_metadata
    assert props["location"].data_type == DataType.OBJECT
    assert props["location"].object_code == "LOCATION"
    assert props["responsible_persons"].object_code == "PERSON"
    assert props["responsible_persons"].multivalued is True
    for field in ("date_bottling", "date_opening", "date_expiration"):
        assert props[field].data_type == DataType.DATE
    assert props["is_empty"].data_type == DataType.BOOLEAN


def test_device_subtypes_and_calibration_metadata():
    assert Instrument.last_calibration.data_type == DataType.DATE
    assert Instrument.calibration_status.data_type == DataType.CONTROLLEDVOCABULARY
    assert Instrument.calibration_status.vocabulary_code == "CALIBRATION_STATUS"
    for cls in (Device, Sensor, Equipment):
        assert "calibration_status" not in cls()._property_metadata
        assert "last_calibration" not in cls()._property_metadata


def test_barcode_is_defined_for_material_entities():
    assert MaterialEntity.barcode.code == "BARCODE"
    for cls in (Device, Instrument, Sensor, Equipment, Sample, Chemical, Material):
        assert cls()._property_metadata["barcode"].code == "BARCODE"

    # InventoryInformation is a Context, so it does not inherit this property.
    assert "barcode" in InventoryInformation()._property_metadata


def test_chemical_identity_and_sample_inventory_properties():
    chemical_props = Chemical()._property_metadata
    assert chemical_props["cas_number"].code == "CAS_NUMBER"
    assert chemical_props["molar_mass"].units == "g/mol"
    assert "lot_number" not in chemical_props

    sample_props = Sample()._property_metadata
    assert sample_props["manufacturer"].code == "MANUFACTURER"
    assert sample_props["supplier"].code == "SUPPLIER"
    assert sample_props["location"].object_code == "LOCATION"
    assert sample_props["responsible_persons"].multivalued is True


def test_legacy_mappings_on_representative_entities():
    assert "INSTRUMENT:v0" in Instrument.defs.prev_versions
    assert "CHEMICAL:v0" in Chemical.defs.prev_versions
    assert "SAMPLE:v0" in Sample.defs.prev_versions
    assert "MANUFACTURER:v0" in InventoryInformation.manufacturer.prev_versions
    assert "CAS_NUMBER:v0" in Chemical.cas_number.prev_versions
