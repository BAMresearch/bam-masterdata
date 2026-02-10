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


class DcpdPotDropCalibration(VocabularyType):
    defs = VocabularyTypeDef(
        code="DCPD_POT_DROP_CALIBRATION",
        description="""DCPD Potential Drop Calibration Options""",
    )

    fem_fit = VocabularyTerm(
        code="FEM_FIT",
        label="Finite Element Fit",
        description="""Finite Element Fit//Finite Elemente Anpassung""",
    )

    johnson = VocabularyTerm(
        code="JOHNSON",
        label="Johnson Formula",
        description="""Johnson Formula//Johnson Formel""",
    )


class MicroscopyFcgCracklengthType(VocabularyType):
    defs = VocabularyTypeDef(
        code="MIC_FCG_FRACSURF_CRACK_TYPE",
        description="""Describes which Cracklength has been measured""",
    )

    beachmark = VocabularyTerm(
        code="BEACHMARK",
        label="Cracklength corresponding with a beachmark",
        description="""Cracklength corresponding with a beachmark//Mit einer Rastlinie korrespondierende Risslänge""",
    )

    final = VocabularyTerm(
        code="FINAL",
        label="Final crack length",
        description="""Final crack length//Finale Risslänge""",
    )

    notch = VocabularyTerm(
        code="NOTCH",
        label="Notch depth",
        description="""Notch depth//Kerbtiefe""",
    )
