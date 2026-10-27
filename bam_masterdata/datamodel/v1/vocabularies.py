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
