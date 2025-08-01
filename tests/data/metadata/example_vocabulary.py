from bam_masterdata.metadata.definitions import VocabularyTerm, VocabularyTypeDef
from bam_masterdata.metadata.entities import VocabularyType


class DefaultCollectionViews(VocabularyType):
    defs = VocabularyTypeDef(
        code="$DEFAULT_COLLECTION_VIEWS",
        description="""Default collection views""",
    )

    form_view = VocabularyTerm(
        code="FORM_VIEW",
        label="Form view",
        description="""""",
    )

    list_view = VocabularyTerm(
        code="LIST_VIEW",
        label="List view",
        description="""""",
    )
