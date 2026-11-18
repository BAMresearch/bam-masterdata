from bam_masterdata.datamodel.v1.entities import ParameterSet
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment


class EnvironmentalConditions(ParameterSet):
    defs = ObjectTypeDef(
        code="ENVIRONMENTAL_CONDITIONS",
        description="An EnvironmentalConditions is a parameter set that describes the ambient conditions "
        "associated with an entity or activity.",
        generated_code_prefix="ENV_COND",
        prev_versions=[
            "ENVIRONMENTAL_CONDITIONS:v0",
            "ENVIRONMENTAL_CONDITIONS.BAM_LABORATORY:v0",
            "ENVIRONMENTAL_CONDITIONS.CREEP_TEST_LABORATORY_CONDITIONS:v0",
        ],
    )

    air_temperature_celsius = PropertyTypeAssignment(
        code="AIR_TEMPERATURE_CELSIUS",
        data_type="REAL",
        property_label="Air temperature",
        units="celsius",
        description="...",
        mandatory=False,
        section="Air Conditions",
        prev_versions=["AIR_TEMPERATURE_IN_CELSIUS:v0"],
    )

    air_relative_humidity = PropertyTypeAssignment(
        code="AIR_RELATIVE_HUMIDITY",
        data_type="REAL",
        property_label="Air relative humidity",
        units="%",
        description="...",
        mandatory=False,
        section="Air Conditions",
        prev_versions=["AIR_REL_HUMIDITY_IN_PERCENT:v0"],
    )


class OutdoorConditions(EnvironmentalConditions):
    defs = ObjectTypeDef(
        code="OUTDOOR_CONDITIONS",
        description="An OutdoorConditions is an environmental conditions parameter set that describes ambient "
        "and weather conditions in an outdoor setting.",
        generated_code_prefix="OUT_COND",
        prev_versions=["ENVIRONMENTAL_CONDITIONS.OUTDOOR:v0"],
    )

    wind_speed_ms = PropertyTypeAssignment(
        code="WIND_SPEED_MS",
        data_type="REAL",
        property_label="Wind speed",
        units="m/s",
        description="...",
        mandatory=False,
        section="Outdoor Conditions",
        prev_versions=["WIND_SPEED_IN_METER_PER_SECOND:v0"],
    )

    wind_direction = PropertyTypeAssignment(
        code="WIND_DIRECTION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="WIND_DIRECTION",
        property_label="Wind direction",
        description="...",
        mandatory=False,
        section="Outdoor Conditions",
        prev_versions=["WIND_DIRECTION:v0"],
    )

    sun_irradiance_wattm2 = PropertyTypeAssignment(
        code="SUN_IRRADIANCE_WATTM2",
        data_type="REAL",
        property_label="Sun irradiance",
        units="watt/m^2",
        description="...",
        mandatory=False,
        section="Outdoor Conditions",
        prev_versions=["SUN_IRRADIANCE_IN_WATT_PER_METER_SQUARED:v0"],
    )

    weather_condition = PropertyTypeAssignment(
        code="WEATHER_CONDITION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="WEATHER_CONDITION",
        property_label="Weather condition",
        description="...",
        mandatory=False,
        section="Outdoor Conditions",
        prev_versions=["WEATHER_CONDITION:v0"],
    )

    location = PropertyTypeAssignment(
        code="LOCATION",
        data_type="OBJECT",
        object_code="LOCATION",
        property_label="Location",
        description="Location",
        mandatory=False,
        section="Outdoor Conditions",
    )

    # LOCATION_LATITUDE_IN_DEGREES, LOCATION_LONGITUDE_IN_DEGREES, LOCATION_ADDRESS map to LOCATION


class IRCameraAcquisitionParameters(ParameterSet):
    defs = ObjectTypeDef(
        code="IR_CAMERA_ACQUISITION_PARAMETERS",
        description="...",
        generated_code_prefix="IR_CAM_ACQ_PARAMS",
        prev_versions=["PARAMETER_SET.IR_CAMERA_ACQUISITION:v0"],
    )


class ThermographyHeatingParameters(ParameterSet):
    defs = ObjectTypeDef(
        code="THERMOGRAPHY_HEATING_PARAMETERS",
        description="...",
        generated_code_prefix="THERM_HEAT_PARAMS",
        prev_versions=["PARAMETER_SET.THERMOGRAPHY_HEATING:v0"],
    )


class ThermographySetup(ParameterSet):
    defs = ObjectTypeDef(
        code="THERMOGRAPHY_SETUP",
        description="...",
        generated_code_prefix="THERM_SETUP",
        prev_versions=["PARAMETER_SET.THERMOGRAPHY_SETUP:v0"],
    )
