from bam_masterdata.metadata.definitions import VocabularyTerm, VocabularyTypeDef
from bam_masterdata.metadata.entities import VocabularyType


class ActivityStatus(VocabularyType):
    defs = VocabularyTypeDef(
        code="ACTIVITY_STATUS",
        description="Current stage of an activity in its lifecycle",
    )

    planned = VocabularyTerm(
        code="PLANNED",
        label="Planned",
        description="The activity is defined but has not started yet",
    )

    in_progress = VocabularyTerm(
        code="IN_PROGRESS",
        label="In progress",
        description="The activity is currently being carried out",
    )

    on_hold = VocabularyTerm(
        code="ON_HOLD",
        label="On hold",
        description="The activity has started but is temporarily paused",
    )

    completed = VocabularyTerm(
        code="COMPLETED",
        label="Completed",
        description="The activity finished as intended",
    )

    failed = VocabularyTerm(
        code="FAILED",
        label="Failed",
        description="The activity ended before completion because of an error or problem",
    )

    cancelled = VocabularyTerm(
        code="CANCELLED",
        label="Cancelled",
        description="The activity was deliberately stopped before completion",
    )


class DocumentType(VocabularyType):
    defs = VocabularyTypeDef(
        code="DOCUMENT_TYPE",
        description="""Document Types""",
    )

    acceptance_certificate = VocabularyTerm(
        code="ACCEPTANCE_CERTIFICATE",
        label="Acceptance Certificate",
        description="""Acceptance Certificate""",
    )

    calibration_certificate = VocabularyTerm(
        code="CALIBRATION_CERTIFICATE",
        label="Calibration Certificate",
        description="""Calibration Certificate""",
    )

    catalog = VocabularyTerm(
        code="CATALOG",
        label="Catalog",
        description="""Catalog""",
    )

    datasheet = VocabularyTerm(
        code="DATASHEET",
        label="Datasheet",
        description="""Datasheet""",
    )

    datasheet_msds = VocabularyTerm(
        code="DATASHEET_MSDS",
        label="Material Safety Datasheet (MSDS)",
        description="""Material Safety Datasheet (MSDS)""",
    )

    datasheet_technical = VocabularyTerm(
        code="DATASHEET_TECHNICAL",
        label="Technical Datasheet",
        description="""Technical Datasheet""",
    )

    delivery_note = VocabularyTerm(
        code="DELIVERY_NOTE",
        label="Delivery Note",
        description="""Delivery Note""",
    )

    diagram = VocabularyTerm(
        code="DIAGRAM",
        label="Diagram",
        description="""Diagram""",
    )

    fabrication_order = VocabularyTerm(
        code="FABRICATION_ORDER",
        label="Fabrication Order",
        description="""Fabrication Order""",
    )

    inspection_certificate = VocabularyTerm(
        code="INSPECTION_CERTIFICATE",
        label="Inspection Certificate",
        description="""Inspection Certificate""",
    )

    installation_manual = VocabularyTerm(
        code="INSTALLATION_MANUAL",
        label="Installation Manual",
        description="""Installation Manual""",
    )

    invoice = VocabularyTerm(
        code="INVOICE",
        label="Invoice",
        description="""Invoice""",
    )

    maintenance_manual = VocabularyTerm(
        code="MAINTENANCE_MANUAL",
        label="Maintenance Manual",
        description="""Maintenance Manual""",
    )

    operating_instruction = VocabularyTerm(
        code="OPERATING_INSTRUCTION",
        label="Operating Instruction",
        description="""Operating Instruction""",
    )

    order = VocabularyTerm(
        code="ORDER",
        label="Order",
        description="""Order""",
    )

    photograph = VocabularyTerm(
        code="PHOTOGRAPH",
        label="Photograph",
        description="""Photograph""",
    )

    repair_manual = VocabularyTerm(
        code="REPAIR_MANUAL",
        label="Repair Manual",
        description="""Repair Manual""",
    )

    software_manual = VocabularyTerm(
        code="SOFTWARE_MANUAL",
        label="Software Manual",
        description="""Software Manual""",
    )

    specification = VocabularyTerm(
        code="SPECIFICATION",
        label="Technical Specification",
        description="""Technical Specification""",
    )

    technical_drawing = VocabularyTerm(
        code="TECHNICAL_DRAWING",
        label="Technical Drawing",
        description="""Technical Drawing""",
    )

    test_certificate = VocabularyTerm(
        code="TEST_CERTIFICATE",
        label="Test Certificate",
        description="""Test Certificate""",
    )

    training_document = VocabularyTerm(
        code="TRAINING_DOCUMENT",
        label="Training Document",
        description="""Training Document""",
    )

    user_manual = VocabularyTerm(
        code="USER_MANUAL",
        label="User Manual",
        description="""User Manual""",
    )

    technical_document = VocabularyTerm(
        code="TECHNICAL_DOCUMENT",
        label="Technical Document",
        description="Technical Document",
    )

    video = VocabularyTerm(
        code="VIDEO",
        label="Video",
        description="Video",
    )

    proposal = VocabularyTerm(
        code="PROPOSAL",
        label="Proposal",
        description="Proposal",
    )

    idea = VocabularyTerm(
        code="IDEA",
        label="Idea",
        description="Idea",
    )

    report = VocabularyTerm(
        code="REPORT",
        label="Report",
        description="Report",
    )

    publication = VocabularyTerm(
        code="PUBLICATION",
        label="Publication",
        description="Publication",
    )


class BAMDataStoreStatus(VocabularyType):
    defs = VocabularyTypeDef(
        code="BAM_DATA_STORE_STATUS",
        description="Status of a BAM data store",
    )

    active = VocabularyTerm(
        code="ACTIVE",
        label="Active",
        description="The data store is active and can be used for storing and retrieving data.",
    )

    inactive = VocabularyTerm(
        code="INACTIVE",
        label="Inactive",
        description="The data store is inactive and cannot be used for storing or retrieving data.",
    )


class DeviceStatus(VocabularyType):
    defs = VocabularyTypeDef(
        code="DEVICE_STATUS",
        description="""Device Status""",
    )

    in_repair = VocabularyTerm(
        code="IN_REPAIR",
        label="In repair",
        description="""Device is currently in repair""",
    )

    in_storage = VocabularyTerm(
        code="IN_STORAGE",
        label="In storage",
        description="""Device is currently in storage""",
    )

    in_use = VocabularyTerm(
        code="IN_USE",
        label="In use",
        description="""Device is currently in use""",
    )

    is_defect = VocabularyTerm(
        code="IS_DEFECT",
        label="Is defect",
        description="""Device is currently defect""",
    )

    is_discarded = VocabularyTerm(
        code="IS_DISCARDED",
        label="Is discarded",
        description="""Device is discarded""",
    )


class CalibrationStatus(VocabularyType):
    defs = VocabularyTypeDef(
        code="CALIBRATION_STATUS",
        description="Current calibration status of a device.",
    )

    valid = VocabularyTerm(
        code="VALID",
        label="Valid",
        description="The device has a valid calibration.",
    )

    expired = VocabularyTerm(
        code="EXPIRED",
        label="Expired",
        description="The device calibration has expired.",
    )

    pending = VocabularyTerm(
        code="PENDING",
        label="Pending",
        description="The device is awaiting calibration.",
    )

    not_required = VocabularyTerm(
        code="NOT_REQUIRED",
        label="Not required",
        description="The device does not require calibration.",
    )
