"""Equipment fields and required flags specified by the FB82 element matrix v0.5."""

import pytest

from bam_masterdata.datamodel import object_types as objects
from bam_masterdata.metadata.entities import CollectionType


@pytest.mark.parametrize(
    ("entity", "required", "optional"),
    [
        (
            objects.MeasuringInstrument,
            {
                "$NAME",
                "SERIAL_NUMBER",
                "INSTRUMENT_STATUS",
                "TEST_METHOD_KIND",
                "INSTRUMENT_CLASSIFICATION",
            },
            {
                "MANUFACTURER",
                "BAM_LOCATION_COMPLETE",
                "BAM_OE",
                "DEVICE_MODEL_NAME",
                "BAM_INVENTORY_NUMBER",
                "RESPONSIBLE_PERSON",
            },
        ),
        (
            objects.TestingEquipment,
            {"$NAME", "SERIAL_NUMBER", "INSTRUMENT_STATUS", "MEASUREMENT_QUANTITY"},
            {
                "MANUFACTURER",
                "BAM_LOCATION_COMPLETE",
                "BAM_OE",
                "DEVICE_MODEL_NAME",
                "BAM_INVENTORY_NUMBER",
                "RESPONSIBLE_PERSON",
            },
        ),
    ],
)
def test_source_field_contract(entity, required, optional):
    properties = entity().properties
    assert len(properties) == len(required | optional)
    assert {prop.code for prop in properties if prop.mandatory} == required
    assert {prop.code for prop in properties if not prop.mandatory} == optional


@pytest.mark.parametrize(
    ("entity", "classification"),
    [
        (
            objects.MeasuringInstrument,
            {
                "test_method_kind": "ULTRASONIC",
                "instrument_classification": "MECHANICAL",
            },
        ),
        (objects.TestingEquipment, {"measurement_quantity": "TEMPERATURE"}),
    ],
)
def test_minimal_inventory_record_and_missing_serial(entity, classification):
    sample = entity(
        name="Source-required fields", instrument_status="IN_USE", **classification
    )
    with pytest.raises(ValueError, match="serial_number"):
        CollectionType().add(sample)
    sample.serial_number = "CONTRACT-TEST"
    assert CollectionType().add(sample)
    assert sample.to_dict()["serial_number"] == "CONTRACT-TEST"


def test_existing_inventory_requirements_are_preserved():
    assert {
        prop.code for prop in objects.Instrument().properties if prop.mandatory
    } == {
        "$NAME",
        "MANUFACTURER",
        "BAM_OE",
        "BAM_LOCATION_COMPLETE",
    }
    assert {
        prop.code for prop in objects.TestingMachine().properties if prop.mandatory
    } == {
        "$NAME",
        "MANUFACTURER",
        "BAM_OE",
        "BAM_LOCATION_COMPLETE",
        "TESTING_MACHINE_DRIVE_TYPE",
        "TESTING_MACHINE_LOAD_TYPE",
        "MAX_LOAD_STATIC_PRIMARY",
        "MAX_LOAD_DYNAMIC_PRIMARY",
    }
