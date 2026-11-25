"""Cross-module checks for the types introduced by PR #465."""

import inspect
import json

import pytest

from bam_masterdata.checker.schema_validator import (
    get_object_types,
    validate_object_type_codes,
)
from bam_masterdata.datamodel.v1 import vocabularies as shared_vocabularies
from bam_masterdata.datamodel.v1.building_materials import (
    vocabularies as building_vocabularies,
)
from bam_masterdata.datamodel.v1.building_materials.object_types import (
    BuildingMaterialsSample,
    ConcreteMixture,
)
from bam_masterdata.datamodel.v1.creep_test import vocabularies as creep_vocabularies
from bam_masterdata.datamodel.v1.creep_test.object_types import CreepTestPiece
from bam_masterdata.datamodel.v1.entities import Location, Material, Sample
from bam_masterdata.datamodel.v1.parameter_set import (
    EnvironmentalConditions,
    OutdoorConditions,
)
from bam_masterdata.datamodel.v1.welding.object_types import WeldingWire
from bam_masterdata.metadata.definitions import DataType
from bam_masterdata.metadata.entities import VocabularyType

ADDED_TYPES = [
    BuildingMaterialsSample,
    ConcreteMixture,
    CreepTestPiece,
    WeldingWire,
    EnvironmentalConditions,
    OutdoorConditions,
]


def test_v1_catalog_can_be_discovered_with_unique_type_codes():
    """Catch invalid declarations even in modules not imported by other tests."""
    classes = get_object_types("v1")
    validate_object_type_codes(classes)
    assert set(ADDED_TYPES) <= set(classes)


@pytest.mark.parametrize("cls", ADDED_TYPES, ids=lambda cls: cls.__name__)
def test_added_types_export_without_duplicate_property_assignments(cls):
    obj = cls()
    codes = [prop.code for prop in obj.properties]
    assert len(codes) == len(set(codes))
    exported = obj.model_to_dict()
    assert exported["defs"]["code"] == cls.defs.code
    assert {prop["code"] for prop in exported["properties"]} == set(codes)
    assert json.loads(obj.model_to_json()) == exported


@pytest.mark.parametrize("cls", ADDED_TYPES, ids=lambda cls: cls.__name__)
def test_added_types_reference_available_vocabularies(cls):
    vocabulary_codes = {
        vocab.defs.code
        for module in (shared_vocabularies, building_vocabularies, creep_vocabularies)
        for _, vocab in inspect.getmembers(module, inspect.isclass)
        if vocab.__module__ == module.__name__ and issubclass(vocab, VocabularyType)
    }
    for prop in cls().properties:
        if prop.data_type == DataType.CONTROLLEDVOCABULARY:
            assert prop.vocabulary_code in vocabulary_codes, prop.code


def test_outdoor_location_uses_the_shared_typed_object_reference():
    outdoor_prop = OutdoorConditions()._property_metadata["location"]
    sample_prop = Sample()._property_metadata["location"]
    assert outdoor_prop.code == sample_prop.code
    assert outdoor_prop.data_type == sample_prop.data_type == DataType.OBJECT
    assert outdoor_prop.object_code == sample_prop.object_code == Location.defs.code
    assert outdoor_prop.vocabulary_code is None


@pytest.mark.parametrize(
    "cls", [BuildingMaterialsSample, ConcreteMixture, CreepTestPiece]
)
def test_sample_subtypes_inherit_promoted_geometry_and_origin(cls):
    assert issubclass(cls, Sample)
    props = cls()._property_metadata
    for name in ("sample_geometry", "sample_origin"):
        shared = Sample()._property_metadata[name]
        assert props[name].code == shared.code
        assert props[name].vocabulary_code == shared.vocabulary_code


def test_welding_wire_inherits_inventory_and_exports_mass():
    assert issubclass(WeldingWire, Material)
    wire = WeldingWire()
    assert wire._property_metadata["lot_number"].code == "LOT_NUMBER"
    assert "WELDING_WIRE.WEIGHT:v0" in (
        wire._property_metadata["mass_kg"].prev_versions or []
    )
    wire.name = "Wire batch A"
    wire.material_id = "WIRE-A"
    wire.lot_number = "LOT-123"
    wire.diameter_mm = 1.2
    wire.mass_kg = 5.0
    assert wire.to_dict() == {
        "name": "Wire batch A",
        "material_id": "WIRE-A",
        "lot_number": "LOT-123",
        "diameter_mm": 1.2,
        "mass_kg": 5.0,
    }
