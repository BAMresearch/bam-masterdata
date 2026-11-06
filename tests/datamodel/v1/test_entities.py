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


def test_device_subtypes_and_calibration_metadata():
    assert Instrument.last_calibration.data_type == DataType.DATE
    assert Instrument.calibration_status.data_type == DataType.CONTROLLEDVOCABULARY
    assert Instrument.calibration_status.vocabulary_code == "CALIBRATION_STATUS"
    for cls in (Device, Sensor, Equipment):
        assert "calibration_status" not in cls()._property_metadata
        assert "last_calibration" not in cls()._property_metadata


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
