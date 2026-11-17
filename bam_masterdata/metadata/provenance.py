"""Reusable assignments for retaining an external record and ordered activity steps."""

from bam_masterdata.metadata.definitions import PropertyTypeAssignment

SOURCE_RECORD = PropertyTypeAssignment(
    code="SOURCE_RECORD",
    data_type="JSON",
    property_label="Source record",
    description="JSON provenance envelope containing the original archive, section identity, mapping profile, and qualified relationships.",
    mandatory=False,
    section="Source provenance",
)
STEP_ORDER = PropertyTypeAssignment(
    code="STEP_ORDER",
    data_type="INTEGER",
    property_label="Step order",
    description="One-based order of a step within the source activity; does not imply a material-flow relationship.",
    mandatory=False,
    section="Source provenance",
)
