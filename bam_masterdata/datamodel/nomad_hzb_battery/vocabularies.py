from bam_masterdata.metadata.definitions import VocabularyTerm, VocabularyTypeDef
from bam_masterdata.metadata.entities import VocabularyType


class CaseCrimp(VocabularyType):
    defs = VocabularyTypeDef(
        code="CASE_CRIMP",
        description="""Case crimping method""",
    )

    manual = VocabularyTerm(
        code="MANUAL",
        label="Manual",
        description="""Manual crimping method""",
    )

    automatic = VocabularyTerm(
        code="AUTOMATIC",
        label="Automatic",
        description="Automatic crimping method",
    )
