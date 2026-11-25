"""Cross-module checks for the types introduced by PR #465."""

import pytest

from bam_masterdata.checker.schema_validator import (
    get_object_types,
    validate_object_type_codes,
)
from bam_masterdata.datamodel.v1.building_materials.object_types import (
    BuildingMaterialsSpecimen,
    ConcreteMixture,
)
from bam_masterdata.datamodel.v1.creep_test.object_types import CreepTestPiece
from bam_masterdata.datamodel.v1.entities import Location, Material, Sample
from bam_masterdata.datamodel.v1.parameter_set import (
    EnvironmentalConditions,
    OutdoorConditions,
)
from bam_masterdata.datamodel.v1.welding.object_types import WeldingWire
from bam_masterdata.metadata.definitions import DataType

ADDED_TYPES = [
    BuildingMaterialsSpecimen,
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


def test_outdoor_location_uses_the_shared_typed_object_reference():
    outdoor_prop = OutdoorConditions()._property_metadata["location"]
    sample_prop = Sample()._property_metadata["location"]
    assert outdoor_prop.code == sample_prop.code
    assert outdoor_prop.data_type == sample_prop.data_type == DataType.OBJECT
    assert outdoor_prop.object_code == sample_prop.object_code == Location.defs.code


@pytest.mark.parametrize(
    "cls", [BuildingMaterialsSpecimen, ConcreteMixture, CreepTestPiece]
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
