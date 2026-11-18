from bam_masterdata.metadata.definitions import VocabularyTerm, VocabularyTypeDef
from bam_masterdata.metadata.entities import VocabularyType


class SubframeType(VocabularyType):
    defs = VocabularyTypeDef(
        code="SUBFRAME_TYPE",
        description="""Subframe type""",
    )

    arbitrary = VocabularyTerm(
        code="ARBITRARY",
        label="Arbitrary",
        description="""Arbitrary frame""",
    )

    full_frame = VocabularyTerm(
        code="FULL_FRAME",
        label="Full Frame",
        description="""Full frame""",
    )

    half_frame = VocabularyTerm(
        code="HALF_FRAME",
        label="Half Frame",
        description="""Half frame""",
    )

    quarter_frame = VocabularyTerm(
        code="QUARTER_FRAME",
        label="Quarter Frame",
        description="""Quarter frame""",
    )


class IRCameraTriggerSetting(VocabularyType):
    defs = VocabularyTypeDef(
        code="IR_CAMERA_TRIGGER_SETTING",
        description="""Trigger Setting""",
    )

    hardware_individual_frame = VocabularyTerm(
        code="HARDWARE_INDIVIDUAL_FRAME",
        label="Hardware Individual Frame",
        description="""Hardware Trigger: Acquisiton of a single frame""",
    )

    hardware_start_acquisition = VocabularyTerm(
        code="HARDWARE_START_ACQUISITION",
        label="Hardware Start Acquisition",
        description="""Hardware Trigger: Start acquisiton""",
    )

    software = VocabularyTerm(
        code="SOFTWARE",
        label="Software",
        description="""Software trigger""",
    )

    temperature = VocabularyTerm(
        code="TEMPERATURE",
        label="Temperature",
        description="""Temperature trigger""",
    )


class NUCMode(VocabularyType):
    defs = VocabularyTypeDef(
        code="NUC_MODE",
        description="""Non-uniformity correction (NUC) mode""",
    )

    before_acquisition = VocabularyTerm(
        code="BEFORE_ACQUISITION",
        label="Before Acquisition",
        description="""NUC performed before every individual acquisition""",
    )

    initial = VocabularyTerm(
        code="INITIAL",
        label="Initial",
        description="""NUC performed before measurement""",
    )

    restore_saved = VocabularyTerm(
        code="RESTORE_SAVED",
        label="Restore Saved",
        description="""NUC restored from memory""",
    )


class ThermographicSetupConfig(VocabularyType):
    defs = VocabularyTypeDef(
        code="THERMOGRAPHIC_SETUP_CONFIG",
        description="""Thermographic setup configuration""",
    )

    indetermined = VocabularyTerm(
        code="INDETERMINED",
        label="Indetermined",
        description="""Indetermined""",
    )

    reflection = VocabularyTerm(
        code="REFLECTION",
        label="Reflection",
        description="""Reflection mode""",
    )

    transmission = VocabularyTerm(
        code="TRANSMISSION",
        label="Transmission",
        description="""Transmission mode""",
    )


class ThermographicSetupHsOrient(VocabularyType):
    defs = VocabularyTypeDef(
        code="THERMOGRAPHIC_SETUP_HS_ORIENT",
        description="""Heat source orientation""",
    )

    off_axis = VocabularyTerm(
        code="OFF_AXIS",
        label="Off Axis",
        description="""Off-Axis with camer""",
    )

    on_axis = VocabularyTerm(
        code="ON_AXIS",
        label="On Axis",
        description="""On-Axis with camera""",
    )

    other = VocabularyTerm(
        code="OTHER",
        label="Other",
        description="""Other orientation""",
    )


class TemporalHeatingStructure(VocabularyType):
    defs = VocabularyTypeDef(
        code="TEMPORAL_HEATING_STRUCTURE",
        description="""Temporal Structure of the heating""",
    )

    arbitrary = VocabularyTerm(
        code="ARBITRARY",
        label="Arbitrary",
        description="""arbitrary pulse form""",
    )

    continuous = VocabularyTerm(
        code="CONTINUOUS",
        label="Continuous",
        description="""continuous""",
    )

    impulse = VocabularyTerm(
        code="IMPULSE",
        label="Impulse",
        description="""Dirac-Impulse""",
    )

    rectangular_pulse = VocabularyTerm(
        code="RECTANGULAR_PULSE",
        label="Rectangular Pulse",
        description="""rectangular Pulse""",
    )

    sinusoidal = VocabularyTerm(
        code="SINUSOIDAL",
        label="Sinusoidal",
        description="""harmonic""",
    )


class HeatingPrinciple(VocabularyType):
    defs = VocabularyTypeDef(
        code="HEATING_PRINCIPLE",
        description="""Heating Principle""",
    )

    hot_air = VocabularyTerm(
        code="HOT_AIR",
        label="Hot_Air",
        description="""hot air""",
    )

    induction = VocabularyTerm(
        code="INDUCTION",
        label="Induction",
        description="""Induction""",
    )

    optical = VocabularyTerm(
        code="OPTICAL",
        label="Optical",
        description="""optical""",
    )

    oven = VocabularyTerm(
        code="OVEN",
        label="Oven",
        description="""Oven""",
    )

    vibration = VocabularyTerm(
        code="VIBRATION",
        label="Vibration",
        description="""Vibratiom""",
    )


class HeatingAreaDescription(VocabularyType):
    defs = VocabularyTypeDef(
        code="HEATING_AREA_DESCRIPTION",
        description="""Area of effect of the heating""",
    )

    full_body = VocabularyTerm(
        code="FULL_BODY",
        label="Full_Body",
        description="""Full body""",
    )

    full_face = VocabularyTerm(
        code="FULL_FACE",
        label="Full_Face",
        description="""Full face""",
    )

    roi = VocabularyTerm(
        code="ROI",
        label="ROI",
        description="""Region of Interest""",
    )
