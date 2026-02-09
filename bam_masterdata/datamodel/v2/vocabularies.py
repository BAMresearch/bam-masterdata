from bam_masterdata.metadata.definitions import VocabularyTerm, VocabularyTypeDef
from bam_masterdata.metadata.entities import VocabularyType


class ActivityStatus(VocabularyType):
    defs = VocabularyTypeDef(
        code="ACTIVITY_STATUS",
        description="""Current status of the activity: PLANNED, RUNNING, COMPLETED, CANCELLED.""",
    )

    planned = VocabularyTerm(
        code="PLANNED",
        label="Planned",
        description="""The activity is planned but has not yet started.""",
    )

    running = VocabularyTerm(
        code="RUNNING",
        label="Running",
        description="""The activity is currently running.""",
    )

    completed = VocabularyTerm(
        code="COMPLETED",
        label="Completed",
        description="""The activity has been completed.""",
    )

    cancelled = VocabularyTerm(
        code="CANCELLED",
        label="Cancelled",
        description="""The activity has been cancelled and will not be completed.""",
    )
