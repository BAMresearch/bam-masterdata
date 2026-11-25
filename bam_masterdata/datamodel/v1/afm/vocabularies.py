from bam_masterdata.metadata.definitions import VocabularyTerm, VocabularyTypeDef
from bam_masterdata.metadata.entities import VocabularyType


class PremountedType(VocabularyType):
    defs = VocabularyTypeDef(
        code="PREMOUNTED_TYPE",
        description="AFM tip compatibility class.",
        description_de="Kompatibilitätsklasse der AFM-Spitze.",
    )

    non_proprietary = VocabularyTerm(
        code="NON_PROPRIETARY",
        label="Non-proprietary",
        description="Non-proprietary",
    )

    nano_ta = VocabularyTerm(
        code="NANO_TA",
        label="NanoTA",
        description="NanoTA",
    )

    nano_ir = VocabularyTerm(
        code="NANO_IR",
        label="NanoIR",
        description="NanoIR",
    )


class BaseShape(VocabularyType):
    defs = VocabularyTypeDef(
        code="BASE_SHAPE",
        description="Cantilever base geometry.",
        description_de="Geometrie des Cantilever-Grundkörpers.",
    )

    rectangular = VocabularyTerm(
        code="RECTANGULAR",
        label="Rectangular",
        description="Rectangular",
    )

    v_shaped = VocabularyTerm(
        code="V_SHAPED",
        label="V-shaped",
        description="V-shaped",
    )

    other = VocabularyTerm(
        code="OTHER",
        label="Other",
        description="Other",
    )


class TipShape(VocabularyType):
    defs = VocabularyTypeDef(
        code="TIP_SHAPE",
        description="AFM tip geometry.",
        description_de="Geometrie der AFM-Spitze.",
    )

    sharp = VocabularyTerm(
        code="SHARP",
        label="Sharp",
        description="Sharp",
    )

    colloidal = VocabularyTerm(
        code="COLLOIDAL",
        label="Colloidal",
        description="Colloidal",
    )

    tipless = VocabularyTerm(
        code="TIPLESS",
        label="Tipless",
        description="Cantilever without a tip.",
    )

    other = VocabularyTerm(
        code="OTHER",
        label="Other",
        description="Other",
    )


class AFMTipStatus(VocabularyType):
    defs = VocabularyTypeDef(
        code="AFM_TIP_STATUS",
        description="Lifecycle status of an AFM tip.",
        description_de="Lebenszyklusstatus einer AFM-Spitze.",
    )

    unused = VocabularyTerm(
        code="UNUSED",
        label="Unused",
        description="Unused",
    )

    active = VocabularyTerm(
        code="ACTIVE",
        label="Active",
        description="Active",
    )

    modified = VocabularyTerm(
        code="MODIFIED",
        label="Modified",
        description="Modified",
    )

    broken = VocabularyTerm(
        code="BROKEN",
        label="Broken",
        description="Broken",
    )

    archived = VocabularyTerm(
        code="ARCHIVED",
        label="Archived",
        description="Archived",
    )
