"""Regression coverage for the migrated thermography parameter sets."""

import importlib
import inspect
import json

import pytest

from bam_masterdata.datamodel.v1.thermography import vocabularies
from bam_masterdata.datamodel.v1.thermography.object_types import (
    IRCameraAcquisitionParameters,
    ThermographyHeatingParameters,
    ThermographySetup,
)
from bam_masterdata.metadata.definitions import PropertyTypeAssignment
from bam_masterdata.metadata.entities import VocabularyType

VOCABULARY_TYPES = [
    cls
    for _, cls in inspect.getmembers(vocabularies, inspect.isclass)
    if cls.__module__ == vocabularies.__name__ and issubclass(cls, VocabularyType)
]


@pytest.mark.parametrize(
    "cls, legacy_name",
    [
        (IRCameraAcquisitionParameters, "IrCameraAcquisition"),
        (ThermographyHeatingParameters, "ThermographyHeating"),
        (ThermographySetup, "ThermographySetup"),
    ],
)
def test_all_legacy_thermography_fields_have_migration_mappings(cls, legacy_name):
    """Renaming a field must not silently omit its legacy counterpart."""
    legacy_module = importlib.import_module("bam_masterdata.datamodel.v0.object_types")
    legacy_cls = getattr(legacy_module, legacy_name)
    assert f"{legacy_cls.defs.code}:v0" in (cls.defs.prev_versions or [])

    # Only fields declared by the legacy subtype are in this migration's scope.
    expected = {
        f"{prop.code}:v0"
        for prop in vars(legacy_cls).values()
        if isinstance(prop, PropertyTypeAssignment)
    }
    mappings = [
        reference
        for prop in cls().properties
        for reference in (prop.prev_versions or [])
        if reference in expected
    ]
    missing = expected - set(mappings)
    assert not missing, f"Unmapped legacy fields: {missing}"
    assert len(mappings) == len(set(mappings)), "Ambiguous legacy field mappings"


@pytest.mark.parametrize("cls", VOCABULARY_TYPES, ids=lambda cls: cls.__name__)
def test_migrated_vocabularies_preserve_legacy_term_codes(cls):
    legacy_module = importlib.import_module(
        "bam_masterdata.datamodel.v0.vocabulary_types"
    )
    legacy_codes = {cls.defs.code} | {
        reference.removesuffix(":v0")
        for reference in (cls.defs.prev_versions or [])
        if reference.endswith(":v0")
    }
    candidates = [
        old_cls
        for _, old_cls in inspect.getmembers(legacy_module, inspect.isclass)
        if old_cls.__module__ == legacy_module.__name__
        and issubclass(old_cls, VocabularyType)
        and old_cls.defs.code in legacy_codes
    ]
    assert len(candidates) == 1, "Missing or ambiguous legacy vocabulary mapping"
    legacy_terms = {term.code for term in candidates[0]().terms}
    current_terms = {term.code for term in cls().terms}
    assert legacy_terms <= current_terms


@pytest.mark.parametrize(
    "cls, values",
    [
        (
            IRCameraAcquisitionParameters,
            {
                "name": "IR acquisition",
                "frame_rate_hz": 100.0,
                "n_recorded_frames": 500,
                "n_pretrigger_frames": 20,
                "n_consecutive_acquisitions": 1,
                "subframe_type": "FULL_FRAME",
                "ir_camera_trigger_setting": "SOFTWARE",
                "nuc_mode": "INITIAL",
            },
        ),
        (
            ThermographyHeatingParameters,
            {
                "name": "Pulsed heating",
                "temporal_heating_structure": "RECTANGULAR_PULSE",
                "heating_principle": "OPTICAL",
                "heating_area_description": "FULL_FACE",
                "heating_power_watt": 500.0,
                "heating_duration_s": 0.1,
            },
        ),
        (
            ThermographySetup,
            {
                "name": "Reflection setup",
                "camera_sample_distance_mm": 300.0,
                "thermography_setup_configuration": "REFLECTION",
                "heat_source_orientation": "OFF_AXIS",
            },
        ),
    ],
)
def test_representative_acquisition_values_serialize(cls, values):
    obj = cls()
    # An unknown attribute can otherwise serialize silently as an omitted value.
    assert values.keys() <= obj._property_metadata.keys()
    for name, value in values.items():
        setattr(obj, name, value)
    assert obj.to_dict() == values
    assert json.loads(obj.to_json()) == values
