import pytest

from bam_masterdata.datamodel.v0.object_types import DataTransfer
from bam_masterdata.metadata.entities import CollectionType


def test_reusable_instruction_does_not_require_a_concrete_package():
    instruction = DataTransfer(
        name="CSV import",
        description="Import exported measurement files without changing the originals.",
        file_format="CSV",
    )
    assert CollectionType().add(instruction)
    assert "input_data_package" not in instruction.to_dict()


def test_input_package_link_is_optional_and_targets_transfer_packages():
    instruction = DataTransfer(
        name="CSV import",
        description="Import exported measurement files without changing the originals.",
        file_format="CSV",
        input_data_package="/LAB_NOTEBOOK/REFERENCE_CASES/DTP1",
    )
    assert CollectionType().add(instruction)
    assert instruction.to_dict()["input_data_package"] == (
        "/LAB_NOTEBOOK/REFERENCE_CASES/DTP1"
    )
    prop = next(p for p in instruction.properties if p.code == "INPUT_DATA_PACKAGE")
    assert prop.object_code == "DATA_TRANSFER_PACKAGE"
    assert not prop.mandatory


@pytest.mark.parametrize("missing_field", ["name", "description", "file_format"])
def test_reusable_instruction_still_requires_the_source_fields(missing_field):
    values = {
        "name": "CSV import",
        "description": "Import exported measurement files.",
        "file_format": "CSV",
    }
    del values[missing_field]
    with pytest.raises(ValueError, match=missing_field):
        CollectionType().add(DataTransfer(**values))
