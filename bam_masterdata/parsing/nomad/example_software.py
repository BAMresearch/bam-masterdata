"""Synthetic non-battery demonstration, not a production datamodel catalog.

These narrow subclasses illustrate adding missing BAM assignments. They are not
imported by datamodel discovery and do not claim to describe an external schema.
"""

from bam_masterdata.datamodel.v0.object_types import (
    ComputationalAnalysis,
    ExperimentalStep,
    SoftwareCode,
)
from bam_masterdata.datamodel.v1.activities import Computation
from bam_masterdata.datamodel.v1.entities import Software
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.provenance import SOURCE_RECORD

from .core import MappingError


class SyntheticSoftwareV0(SoftwareCode):
    defs = ObjectTypeDef(
        code="SOFTWARE_CODE.SYNTHETIC_EXAMPLE",
        description="Synthetic example software record.",
    )
    source_record = SOURCE_RECORD


class SyntheticExecutionV0(ComputationalAnalysis):
    defs = ObjectTypeDef(
        code="COMPUTATIONAL_ANALYSIS.SYNTHETIC_EXAMPLE",
        description="Synthetic example software execution.",
    )
    source_record = SOURCE_RECORD
    software = PropertyTypeAssignment(
        code="SYNTHETIC_SOFTWARE_V0",
        data_type="OBJECT",
        object_code="SOFTWARE_CODE.SYNTHETIC_EXAMPLE",
        property_label="Software",
        description="Software executed in this synthetic example.",
        mandatory=False,
        section="Synthetic example",
    )
    finished_flag = ExperimentalStep.finished_flag
    duration = PropertyTypeAssignment(
        code="SYNTHETIC_DURATION",
        data_type="REAL",
        units="s",
        property_label="Duration",
        description="Elapsed execution duration.",
        mandatory=False,
        section="Synthetic example",
    )


class SyntheticSoftwareV1(Software):
    defs = ObjectTypeDef(
        code="SYNTHETIC_SOFTWARE", description="Synthetic example software record."
    )
    source_record = SOURCE_RECORD


class SyntheticExecutionV1(Computation):
    defs = ObjectTypeDef(
        code="SYNTHETIC_EXECUTION", description="Synthetic example software execution."
    )
    source_record = SOURCE_RECORD
    # New property code: do not change Computation.SOFTWARE's exact SOFTWARE target.
    software = PropertyTypeAssignment(
        code="SYNTHETIC_SOFTWARE_V1",
        data_type="OBJECT",
        object_code="SYNTHETIC_SOFTWARE",
        property_label="Software",
        description="Software executed in this synthetic example.",
        mandatory=False,
        section="Synthetic example",
    )
    duration = SyntheticExecutionV0.duration


class SyntheticSoftwareMapping:
    """Separate mapping selected explicitly for demo.synthetic.* source schemas."""

    mapping_id = "synthetic-software/1"

    def __init__(self, *, target_version):
        if target_version not in ("v0", "v1"):
            raise MappingError(f"Unsupported target version: {target_version}")
        self.target_version = target_version
        self.software_type, self.execution_type = (
            (SyntheticSoftwareV0, SyntheticExecutionV0)
            if target_version == "v0"
            else (SyntheticSoftwareV1, SyntheticExecutionV1)
        )

    def map(self, context):
        for archive in context.archives:
            schema = context.required_text(archive, "/data/m_def")
            if schema not in ("demo.synthetic.Software", "demo.synthetic.Execution"):
                raise MappingError(f"Unsupported synthetic schema: {schema}")
            if context.required_text(archive, "/data/m_def_id") != "synthetic-v1":
                raise MappingError("Unsupported synthetic schema version")
            values = {"name": context.required_text(archive, "/data/name")}
            if schema == "demo.synthetic.Software":
                values["version"] = context.required_text(archive, "/data/version")
                if self.target_version == "v0":
                    values["software_name"] = values["name"]
                cls = self.software_type
            else:
                values["duration"] = context.quantity(
                    context.value(archive, "/data/duration/value"),
                    context.required_text(archive, "/data/duration/unit"),
                    "s",
                )
                status = context.required_text(archive, "/data/status")
                if status != "done":
                    raise MappingError(f"Unsupported synthetic status: {status}")
                # Explicit source-enum translation; no vocabulary guessing.
                values[
                    "finished_flag"
                    if self.target_version == "v0"
                    else "activity_status"
                ] = True if self.target_version == "v0" else "COMPLETED"
                cls = self.execution_type
            context.create(archive, cls, values, profile="explicit quantity units")
        for archive in context.archives:
            if archive.document["data"]["m_def"] == "demo.synthetic.Execution":
                context.reference(
                    archive,
                    archive.key(),
                    "/data/software",
                    attribute="software",
                    role="executed_software",
                )
