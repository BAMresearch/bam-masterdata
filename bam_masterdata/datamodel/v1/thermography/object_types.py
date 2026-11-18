from bam_masterdata.datamodel.v1.entities import ParameterSet
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment


class IRCameraAcquisitionParameters(ParameterSet):
    defs = ObjectTypeDef(
        code="IR_CAMERA_ACQUISITION_PARAMETERS",
        description="An IRCameraAcquisitionParameters is a parameter set that specifies "
        "image acquisition, triggering, and calibration settings for an infrared camera.",
        generated_code_prefix="IR_CAM_ACQ_PARAMS",
        prev_versions=["PARAMETER_SET.IR_CAMERA_ACQUISITION:v0"],
    )

    integration_time_us = PropertyTypeAssignment(
        code="INTEGRATION_TIME_US",
        data_type="REAL",
        units="microsecond",
        property_label="Integration time",
        description="Duration over which the infrared detector integrates the signal for each frame.",
        mandatory=False,
        section="Image Acquisition",
        prev_versions=["INTEGRATION_TIME_IN_MICROSECOND:v0"],
    )

    frame_rate_hz = PropertyTypeAssignment(
        code="FRAME_RATE_HZ",
        data_type="REAL",
        units="Hz",
        property_label="Frame rate",
        description="Number of image frames acquired per second.",
        mandatory=True,
        section="Image Acquisition",
        prev_versions=["FRAMERATE_IN_HERTZ:v0"],
    )

    n_recorded_frames = PropertyTypeAssignment(
        code="N_RECORDED_FRAMES",
        data_type="INTEGER",
        property_label="Number of recorded frames",
        description="Total number of image frames specified for an individual acquisition.",
        mandatory=True,
        section="Image Acquisition",
        prev_versions=["NUMBER_RECORDED_FRAMES:v0"],
    )

    n_pretrigger_frames = PropertyTypeAssignment(
        code="N_PRETRIGGER_FRAMES",
        data_type="INTEGER",
        property_label="Number of pretrigger frames",
        description="Number of image frames recorded before the acquisition trigger.",
        mandatory=True,
        section="Image Acquisition",
        prev_versions=["NUMBER_PRETRIGGER_FRAMES:v0"],
    )

    subframe_type = PropertyTypeAssignment(
        code="SUBFRAME_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="SUBFRAME_TYPE",
        property_label="Subframe type",
        description="Selection of the detector image area recorded during acquisition.",
        mandatory=True,
        section="Subframe Settings",
        prev_versions=["SUBFRAME:v0"],
    )

    subframe_height_px = PropertyTypeAssignment(
        code="SUBFRAME_HEIGHT_PX",
        data_type="INTEGER",
        property_label="Subframe height",
        units="pixels",
        description="Height of an arbitrarily configured subframe.",
        mandatory=False,
        section="Subframe Settings",
        prev_versions=["ARBITRARY_SUBFRAME_HEIGHT_IN_PIXEL:v0"],
    )

    subframe_width_px = PropertyTypeAssignment(
        code="SUBFRAME_WIDTH_PX",
        data_type="INTEGER",
        property_label="Subframe width",
        units="pixels",
        description="Width of an arbitrarily configured subframe.",
        mandatory=False,
        section="Subframe Settings",
        prev_versions=["ARBITRARY_SUBFRAME_WIDTH_IN_PIXEL:v0"],
    )

    subframe_start_row_px = PropertyTypeAssignment(
        code="SUBFRAME_START_ROW_PX",
        data_type="INTEGER",
        property_label="Subframe start row",
        units="pixels",
        description="Row coordinate at which an arbitrarily configured subframe begins "
        "within the full detector image.",
        mandatory=False,
        section="Subframe Settings",
        prev_versions=["ARBITRARY_SUBFRAME_START_HEIGHT_IN_PIXEL:v0"],
    )

    subframe_start_column_px = PropertyTypeAssignment(
        code="SUBFRAME_START_COLUMN_PX",
        data_type="INTEGER",
        property_label="Subframe start column",
        units="pixels",
        description="Column coordinate at which an arbitrarily configured subframe begins "
        "within the full detector image.",
        mandatory=False,
        section="Subframe Settings",
        prev_versions=["ARBITRARY_SUBFRAME_START_WIDTH_IN_PIXEL:v0"],
    )

    ir_camera_trigger_setting = PropertyTypeAssignment(
        code="IR_CAMERA_TRIGGER_SETTING",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="IR_CAMERA_TRIGGER_SETTING",
        property_label="Trigger setting",
        description="Mode by which image acquisition or individual frame acquisition is triggered.",
        mandatory=True,
        section="Trigger Settings",
        prev_versions=["IR_CAMERA.TRIGGER_SETTING:v0"],
    )

    n_consecutive_acquisitions = PropertyTypeAssignment(
        code="N_CONSECUTIVE_ACQUISITIONS",
        data_type="INTEGER",
        property_label="Number of consecutive acquisitions",
        description="Number of individual acquisitions specified for a consecutive acquisition sequence.",
        mandatory=True,
        section="Trigger Settings",
        prev_versions=["NUMBER_CONSECUTIVE_ACQUISITONS:v0"],
    )

    hardware_trigger_input = PropertyTypeAssignment(
        code="HARDWARE_TRIGGER_INPUT",
        data_type="VARCHAR",
        property_label="Hardware trigger input",
        description="Identifier of the camera input used to receive the hardware trigger signal.",
        mandatory=False,
        section="Trigger Settings",
        prev_versions=["HARDWARE_TRIGGER_INPUT:v0"],
    )

    ad_channel_description = PropertyTypeAssignment(
        code="AD_CHANNEL_DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="AD-channel description",
        description="Description of the auxiliary analog-to-digital channels recorded "
        "alongside the image sequence, including signal meanings and units where known.",
        mandatory=False,
        section="Auxiliary Channels",
        prev_versions=["AD_CHANNEL_DESCRIPTION:v0"],
    )

    nuc_mode = PropertyTypeAssignment(
        code="NUC_MODE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="NUC_MODE",
        property_label="Non-uniformity correction mode",
        description="Procedure used to obtain or restore the detector non-uniformity "
        "correction applied during acquisition.",
        mandatory=True,
        section="Calibration Settings",
        prev_versions=["NUC_PERFORMED:v0"],
    )

    calibration_range_min_celsius = PropertyTypeAssignment(
        code="CALIBRATION_RANGE_MIN_CELSIUS",
        data_type="REAL",
        units="celsius",
        property_label="Calibration range lower limit",
        description="Lower temperature limit of the camera calibration range selected for acquisition.",
        mandatory=False,
        section="Calibration Settings",
        prev_versions=["USED_CALIBRATION_RANGE_MIN_IN_CELSIUS:v0"],
    )

    calibration_range_max_celsius = PropertyTypeAssignment(
        code="CALIBRATION_RANGE_MAX_CELSIUS",
        data_type="REAL",
        units="celsius",
        property_label="Calibration range upper limit",
        description="Upper temperature limit of the camera calibration range selected for acquisition.",
        mandatory=False,
        section="Calibration Settings",
        prev_versions=["USED_CALIBRATION_RANGE_MAX_IN_CELSIUS:v0"],
    )


class ThermographyHeatingParameters(ParameterSet):
    defs = ObjectTypeDef(
        code="THERMOGRAPHY_HEATING_PARAMETERS",
        description="A ThermographyHeatingParameters is a parameter set that specifies "
        "the excitation mechanism and temporal and spatial heating settings used in active thermography.",
        generated_code_prefix="THERM_HEAT_PARAMS",
        prev_versions=["PARAMETER_SET.THERMOGRAPHY_HEATING:v0"],
    )

    temporal_heating_structure = PropertyTypeAssignment(
        code="TEMPORAL_HEATING_STRUCTURE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TEMPORAL_HEATING_STRUCTURE",
        property_label="Temporal heating structure",
        description="Temporal profile of the applied heating, such as continuous, "
        "pulsed, or sinusoidally modulated excitation.",
        mandatory=True,
        section="Heating Mechanism",
        prev_versions=["TEMPORAL_HEATING_STRUCTURE:v0"],
    )

    heating_principle = PropertyTypeAssignment(
        code="HEATING_PRINCIPLE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="HEATING_PRINCIPLE",
        property_label="Heating principle",
        description="Mechanism by which the specimen is heated, such as optical "
        "excitation, induction, or hot air.",
        mandatory=True,
        section="Heating Mechanism",
        prev_versions=["HEATING_PRINCIPLE:v0"],
    )

    heating_power_watt = PropertyTypeAssignment(
        code="HEATING_POWER_WATT",
        data_type="REAL",
        units="watt",
        property_label="Heating power",
        description="Power setting of the heating source.",
        mandatory=False,
        section="Heating Settings",
        prev_versions=["POWER_IN_WATT:v0"],
    )

    heating_pulse_energy_j = PropertyTypeAssignment(
        code="HEATING_PULSE_ENERGY_J",
        data_type="REAL",
        units="J",
        property_label="Heating pulse energy",
        description="Energy setting of the heating source for an individual excitation pulse.",
        mandatory=False,
        section="Heating Settings",
        prev_versions=["PULSE_ENERGY_IN_JOULE:v0"],
    )

    heating_source_temperature_celsius = PropertyTypeAssignment(
        code="HEATING_SOURCE_TEMPERATURE_CELSIUS",
        data_type="REAL",
        units="celsius",
        property_label="Heating source temperature",
        description="Temperature setting of the heating source.",
        mandatory=False,
        section="Heating Settings",
        prev_versions=["HEATING_TEMPERATURE_IN_CELSIUS:v0"],
    )

    heating_duration_s = PropertyTypeAssignment(
        code="HEATING_DURATION_S",
        data_type="REAL",
        units="s",
        property_label="Heating duration",
        description="Duration of an individual heating excitation.",
        mandatory=False,
        section="Heating Settings",
        prev_versions=["HEATING_DURATION_IN_SECONDS:v0"],
    )

    heating_frequency_hz = PropertyTypeAssignment(
        code="HEATING_FREQUENCY_HZ",
        data_type="REAL",
        units="Hz",
        property_label="Heating frequency",
        description="Frequency of the periodic heating excitation.",
        mandatory=False,
        section="Heating Settings",
        prev_versions=["HEATING_FREQUENCY_IN_HERTZ:v0"],
    )

    heating_area_description = PropertyTypeAssignment(
        code="HEATING_AREA_DESCRIPTION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="HEATING_AREA_DESCRIPTION",
        property_label="Heating extent",
        description="Spatial extent of the heating relative to the specimen, "
        "such as the whole specimen, a complete face, or a selected region.",
        mandatory=True,
        section="Heating Geometry",
        prev_versions=["HEATING_AREA_DESC:v0"],
    )

    heating_area_height_mm = PropertyTypeAssignment(
        code="HEATING_AREA_HEIGHT_MM",
        data_type="REAL",
        units="mm",
        property_label="Heating area height",
        description="Height of the heated region on the specimen.",
        mandatory=False,
        section="Heating Geometry",
        prev_versions=["HEATING_HEIGHT_IN_MILLIMETER:v0"],
    )

    heating_area_width_mm = PropertyTypeAssignment(
        code="HEATING_AREA_WIDTH_MM",
        data_type="REAL",
        units="mm",
        property_label="Heating area width",
        description="Width of the heated region on the specimen.",
        mandatory=False,
        section="Heating Geometry",
        prev_versions=["HEATING_WIDTH_IN_MILLIMETER:v0"],
    )


class ThermographySetup(ParameterSet):
    defs = ObjectTypeDef(
        code="THERMOGRAPHY_SETUP",
        description="A ThermographySetup is a parameter set that specifies the spatial "
        "arrangement and specimen surface condition used in a thermographic measurement.",
        generated_code_prefix="THERM_SETUP",
        prev_versions=["PARAMETER_SET.THERMOGRAPHY_SETUP:v0"],
    )

    camera_sample_distance_mm = PropertyTypeAssignment(
        code="CAMERA_SAMPLE_DISTANCE_MM",
        data_type="REAL",
        units="mm",
        property_label="Camera-to-sample distance",
        description="Distance between the camera reference point and the observed specimen surface.",
        mandatory=True,
        section="Setup Geometry",
        prev_versions=["CAMERA_DISTANCE_IN_MILLIMETER:v0"],
    )

    heat_source_sample_distance_mm = PropertyTypeAssignment(
        code="HEAT_SOURCE_SAMPLE_DISTANCE_MM",
        data_type="REAL",
        units="mm",
        property_label="Heat-source-to-sample distance",
        description="Distance between the heating-source reference point and the heated specimen surface.",
        mandatory=False,
        section="Setup Geometry",
        prev_versions=["HEAT_SOURCE_DISTANCE_IN_MILLIMETER:v0"],
    )

    sample_surface_condition = PropertyTypeAssignment(
        code="SAMPLE_SURFACE_CONDITION",
        data_type="MULTILINE_VARCHAR",
        property_label="Sample surface condition",
        description="Surface condition or treatment relevant to the thermographic "
        "measurement, such as an applied coating.",
        mandatory=False,
        section="Sample Condition",
        prev_versions=["SAMPLE_TREATMENT:v0"],
    )

    thermography_setup_configuration = PropertyTypeAssignment(
        code="THERMOGRAPHY_SETUP_CONFIGURATION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="THERMOGRAPHIC_SETUP_CONFIG",
        property_label="Setup configuration",
        description="Relative placement of the camera and heating source with respect "
        "to the specimen, distinguishing reflection and transmission arrangements.",
        mandatory=True,
        section="Setup Geometry",
        prev_versions=["SETUP_CONFIGURATION:v0"],
    )

    heat_source_orientation = PropertyTypeAssignment(
        code="HEAT_SOURCE_ORIENTATION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="THERMOGRAPHIC_SETUP_HS_ORIENT",
        property_label="Heat source orientation",
        description="Alignment of the heating source relative to the camera viewing axis.",
        mandatory=False,
        section="Setup Geometry",
        prev_versions=["HEAT_SOURCE_ORIENTATION:v0"],
    )
