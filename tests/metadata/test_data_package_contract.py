import pytest

from bam_masterdata.datamodel.object_types import DataPackageFb82
from bam_masterdata.metadata.entities import CollectionType


def test_required_package_fields_and_optional_notes():
    package = DataPackageFb82(
        name="Raw CSV files",
        data_package_kind="RAW",
        notes="Keep the source files together",
    )
    with pytest.raises(ValueError, match="file_format"):
        CollectionType().add(package)
    package.file_format = "CSV"
    assert CollectionType().add(package)
    assert package.to_dict()["notes"] == "Keep the source files together"
    assert {prop.code for prop in package.properties if prop.mandatory} == {
        "$NAME",
        "DATA_PACKAGE_KIND",
        "FILE_FORMAT",
    }
    empty_notes = DataPackageFb82(
        name="Processed CSV", data_package_kind="PROCESSED", file_format="CSV"
    )
    assert CollectionType().add(empty_notes)
