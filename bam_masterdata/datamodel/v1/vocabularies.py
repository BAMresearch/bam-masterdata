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
        description="""Document Types//Dokumententypen""",
    )

    acceptance_certificate = VocabularyTerm(
        code="ACCEPTANCE_CERTIFICATE",
        label="Acceptance Certificate",
        description="""Acceptance Certificate//Abnahmezeugnis""",
    )

    calibration_certificate = VocabularyTerm(
        code="CALIBRATION_CERTIFICATE",
        label="Calibration Certificate",
        description="""Calibration Certificate//Kalibrierschein""",
    )

    catalog = VocabularyTerm(
        code="CATALOG",
        label="Catalog",
        description="""Catalog/Katalog""",
    )

    datasheet = VocabularyTerm(
        code="DATASHEET",
        label="Datasheet",
        description="""Datasheet//Datenblatt""",
    )

    datasheet_msds = VocabularyTerm(
        code="DATASHEET_MSDS",
        label="Material Safety Datasheet (MSDS)",
        description="""Material Safety Datasheet (MSDS)//Sicherheitsdatenblatt""",
    )

    datasheet_technical = VocabularyTerm(
        code="DATASHEET_TECHNICAL",
        label="Technical Datasheet",
        description="""Technical Datasheet//Technisches Datenblatt""",
    )

    delivery_note = VocabularyTerm(
        code="DELIVERY_NOTE",
        label="Delivery Note",
        description="""Delivery Note//Lieferschein""",
    )

    diagram = VocabularyTerm(
        code="DIAGRAM",
        label="Diagram",
        description="""Diagram//Diagramm""",
    )

    fabrication_order = VocabularyTerm(
        code="FABRICATION_ORDER",
        label="Fabrication Order",
        description="""Fabrication Order//Fertigungsauftrag""",
    )

    inspection_certificate = VocabularyTerm(
        code="INSPECTION_CERTIFICATE",
        label="Inspection Certificate",
        description="""Inspection Certificate//Inspektionszeugnis""",
    )

    installation_manual = VocabularyTerm(
        code="INSTALLATION_MANUAL",
        label="Installation Manual",
        description="""Installation Manual//Installationsanleitung""",
    )

    invoice = VocabularyTerm(
        code="INVOICE",
        label="Invoice",
        description="""Invoice//Rechnung""",
    )

    maintenance_manual = VocabularyTerm(
        code="MAINTENANCE_MANUAL",
        label="Maintenance Manual",
        description="""Maintenance Manual//Wartungsanleitung""",
    )

    operating_instruction = VocabularyTerm(
        code="OPERATING_INSTRUCTION",
        label="Operating Instruction",
        description="""Operating Instruction//Betriebsanweisung""",
    )

    order = VocabularyTerm(
        code="ORDER",
        label="Order",
        description="""Order//Bestellung""",
    )

    photograph = VocabularyTerm(
        code="PHOTOGRAPH",
        label="Photograph",
        description="""Photograph//Foto""",
    )

    repair_manual = VocabularyTerm(
        code="REPAIR_MANUAL",
        label="Repair Manual",
        description="""Repair Manual//Reparaturanleitung""",
    )

    software_manual = VocabularyTerm(
        code="SOFTWARE_MANUAL",
        label="Software Manual",
        description="""Software Manual//Software Bedienungsanleitung""",
    )

    specification = VocabularyTerm(
        code="SPECIFICATION",
        label="Technical Specification",
        description="""Technical Specification//Technische Spezifikation""",
    )

    technical_drawing = VocabularyTerm(
        code="TECHNICAL_DRAWING",
        label="Technical Drawing",
        description="""Technical Drawing//Technische Zeichnung""",
    )

    test_certificate = VocabularyTerm(
        code="TEST_CERTIFICATE",
        label="Test Certificate",
        description="""Test Certificate//Prüfzeugnis""",
    )

    training_document = VocabularyTerm(
        code="TRAINING_DOCUMENT",
        label="Training Document",
        description="""Training Document//Schulungsunterlagen""",
    )

    user_manual = VocabularyTerm(
        code="USER_MANUAL",
        label="User Manual",
        description="""User Manual//Bedienungsanleitung""",
    )

    technical_document = VocabularyTerm(
        code="TECHNICAL_DOCUMENT",
        label="Technical Document",
        description="Technical Document//Technisches Dokument",
    )

    video = VocabularyTerm(
        code="VIDEO",
        label="Video",
        description="Video//Video",
    )

    proposal = VocabularyTerm(
        code="PROPOSAL",
        label="Proposal",
        description="Proposal//Antrag",
    )

    idea = VocabularyTerm(
        code="IDEA",
        label="Idea",
        description="Idea//Idee",
    )

    report = VocabularyTerm(
        code="REPORT",
        label="Report",
        description="Report//Bericht",
    )

    publication = VocabularyTerm(
        code="PUBLICATION",
        label="Publication",
        description="Publication//Publikation",
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
