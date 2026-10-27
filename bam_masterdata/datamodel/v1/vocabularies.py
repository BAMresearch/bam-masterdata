from bam_masterdata.metadata.definitions import VocabularyTerm, VocabularyTypeDef
from bam_masterdata.metadata.entities import VocabularyType


class ActivityStatus(VocabularyType):
    defs = VocabularyTypeDef(
        code="ACTIVITY_STATUS",
        description="Current stage of an activity in its lifecycle",
        description_de="Aktueller Stand einer Aktivität in ihrem Lebenszyklus",
    )

    planned = VocabularyTerm(
        code="PLANNED",
        label="Planned",
        label_de="Geplant",
        description="The activity is defined but has not started yet",
        description_de="Die Aktivität ist festgelegt, wurde aber noch nicht begonnen",
    )

    in_progress = VocabularyTerm(
        code="IN_PROGRESS",
        label="In progress",
        label_de="In Bearbeitung",
        description="The activity is currently being carried out",
        description_de="Die Aktivität wird gerade durchgeführt",
    )

    on_hold = VocabularyTerm(
        code="ON_HOLD",
        label="On hold",
        label_de="Pausiert",
        description="The activity has started but is temporarily paused",
        description_de="Die Aktivität wurde begonnen, ist aber vorübergehend unterbrochen",
    )

    completed = VocabularyTerm(
        code="COMPLETED",
        label="Completed",
        label_de="Abgeschlossen",
        description="The activity finished as intended",
        description_de="Die Aktivität wurde wie vorgesehen abgeschlossen",
    )

    failed = VocabularyTerm(
        code="FAILED",
        label="Failed",
        label_de="Fehlgeschlagen",
        description="The activity ended before completion because of an error or problem",
        description_de="Die Aktivität endete wegen eines Fehlers oder Problems vor dem Abschluss",
    )

    cancelled = VocabularyTerm(
        code="CANCELLED",
        label="Cancelled",
        label_de="Abgebrochen",
        description="The activity was deliberately stopped before completion",
        description_de="Die Aktivität wurde vor dem Abschluss bewusst beendet",
    )
