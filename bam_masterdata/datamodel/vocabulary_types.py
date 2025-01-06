from bam_masterdata.metadata.definitions import (
    VocabularyTerm,
    VocabularyTypeDef,
)
from bam_masterdata.metadata.entities import VocabularyType


class DocumentType(VocabularyType):
    defs = VocabularyTypeDef(
        code='DOCUMENT_TYPE',
        description='Document type//Dokumententypen',
    )

    acceptance_certificate = VocabularyTerm(
        code='ACCEPTANCE_CERTIFICATE',
        label='Acceptance Certificate',
        description='Acceptance Certificate//Abnahmezeugnis',
    )

    calibration_certificate = VocabularyTerm(
        code='CALIBRATION_CERTIFICATE',
        label='Calibration Certificate',
        description='Calibration Certificate//Kalibrierschein',
    )

    catalog = VocabularyTerm(
        code='CATALOG',
        label='Catalog',
        description='Document type//Dokumententypen',
    )

    datasheet = VocabularyTerm(
        code='DATASHEET',
        label='Datasheet',
        description='Datasheet//Datenblatt',
    )

    datasheet_msds = VocabularyTerm(
        code='DATASHEET_MSDS',
        label='Material Safety Datasheet',
        description='Material Safety Datasheet (MSDS)//Sicherheitsdatenblatt',
    )

    datasheet_technical = VocabularyTerm(
        code='DATASHEET_TECHNICAL',
        label='Technical Datasheet',
        description='Technical Datasheet//Technisches Datenblatt',
    )

    delivery_note = VocabularyTerm(
        code='DELIVERY_NOTE',
        label='Delivery Note',
        description='Delivery Note//Lieferschein',
    )

    diagram = VocabularyTerm(
        code='DIAGRAM',
        label='Diagram',
        description='Diagram//Diagramm',
    )

    fabrication_order = VocabularyTerm(
        code='FABRICATION_ORDER',
        label='Fabrication Order',
        description='Fabrication Order//Fertigungsauftrag',
    )

    inspection_certificate = VocabularyTerm(
        code='INSPECTION_CERTIFICATE',
        label='Inspection Certificate',
        description='Inspection Certificate//Inspektionszeugnis',
    )
