"""Preliminary Dataset types for development."""

from bam_masterdata.metadata.definitions import DatasetTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.entities import DatasetType


class RawData(DatasetType):
    defs = DatasetTypeDef(
        code="RAW_DATA",
        description="""""",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="Human-readable name identifying the object.",
        mandatory=True,
        section="General Information",
        prev_versions=["$NAME:v0"],
    )
