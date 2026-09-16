from bam_masterdata.datamodel.activities import MechanicalTest
from bam_masterdata.datamodel.object_types import (
    ComputationalAnalysis, EnvironmentalConditions, Instrument, InstrumentAccessory,
    Sample, TestingMachine,
)
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.entities import ObjectType

class TensileTest(MechanicalTest):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.TENSILE_TEST",
        description="""Tensile-test data object: TensileTest // Datenobjekt fuer den Zugversuch: TensileTest""",
        generated_code_prefix="EXP.MECH.TENSILE",
    )
    tensile_test_link_materialhistoryandcondition = PropertyTypeAssignment(
        code="TENSILE_TEST_LINK_MATERIALHISTORYANDCONDITION",
        data_type="OBJECT",
        object_code="TENSILE_TEST_MATERIAL_HISTORY_AND_CONDITION",
        property_label="MaterialHistoryAndCondition",
        description="""Linked tensile-test sub-object // Verknuepftes Zugversuchs-Unterobjekt""",
        mandatory=False,
        section="Linked objects",
    )
    tensile_test_link_testpiece = PropertyTypeAssignment(
        code="TENSILE_TEST_LINK_TESTPIECE",
        data_type="OBJECT",
        object_code="SAMPLE.TENSILE_TEST_PIECE",
        property_label="TestPiece",
        description="""Linked tensile-test sub-object // Verknuepftes Zugversuchs-Unterobjekt""",
        mandatory=False,
        section="Linked objects",
        ontology_IRI="https://w3id.org/pmd/co/PMD_0020193",
    )
    tensile_test_link_testmachine = PropertyTypeAssignment(
        code="TENSILE_TEST_LINK_TESTMACHINE",
        data_type="OBJECT",
        object_code="TESTING_MACHINE.TENSILE_TEST_MACHINE",
        property_label="TestMachine",
        description="""Linked tensile-test sub-object // Verknuepftes Zugversuchs-Unterobjekt""",
        mandatory=False,
        section="Linked objects",
        ontology_IRI="https://w3id.org/pmd/co/PMD_0000973",
    )
    tensile_test_link_heatingsystem = PropertyTypeAssignment(
        code="TENSILE_TEST_LINK_HEATINGSYSTEM",
        data_type="OBJECT",
        object_code="INSTRUMENT.TENSILE_TEST_MACHINE_HEATING_SYSTEM",
        property_label="HeatingSystem",
        description="""Linked tensile-test sub-object // Verknuepftes Zugversuchs-Unterobjekt""",
        mandatory=False,
        section="Linked objects",
    )
    tensile_test_link_machinedataacquisition = PropertyTypeAssignment(
        code="TENSILE_TEST_LINK_MACHINEDATAACQUISITION",
        data_type="OBJECT",
        object_code="INSTRUMENT.TENSILE_TEST_MACHINE_DATA_ACQUISITION",
        property_label="MachineDataAcquisition",
        description="""Linked tensile-test sub-object // Verknuepftes Zugversuchs-Unterobjekt""",
        mandatory=False,
        section="Linked objects",
    )
    tensile_test_link_original_gauge_lengthadsensor = PropertyTypeAssignment(
        code="TENSILE_TEST_LINK_ORIGINAL_GAUGE_LENGTHADSENSOR",
        data_type="OBJECT",
        object_code="INSTRUMENT.TENSILE_TEST_LOAD_SENSOR",
        property_label="LoadSensor",
        description="""Linked tensile-test sub-object // Verknuepftes Zugversuchs-Unterobjekt""",
        mandatory=False,
        section="Linked objects",
    )
    tensile_test_link_original_gauge_lengthaddataacquisition = PropertyTypeAssignment(
        code="TENSILE_TEST_LINK_ORIGINAL_GAUGE_LENGTHADDATAACQUISITION",
        data_type="OBJECT",
        object_code="TENSILE_TEST_LOAD_DATA_ACQUISITION",
        property_label="LoadDataAcquisition",
        description="""Linked tensile-test sub-object // Verknuepftes Zugversuchs-Unterobjekt""",
        mandatory=False,
        section="Linked objects",
    )
    tensile_test_link_laboratoryconditions = PropertyTypeAssignment(
        code="TENSILE_TEST_LINK_LABORATORYCONDITIONS",
        data_type="OBJECT",
        object_code="ENVIRONMENTAL_CONDITIONS.TENSILE_TEST_LABORATORY_CONDITIONS",
        property_label="LaboratoryConditions",
        description="""Linked tensile-test sub-object // Verknuepftes Zugversuchs-Unterobjekt""",
        mandatory=False,
        section="Linked objects",
    )
    tensile_test_link_temperaturemeasuringsystem = PropertyTypeAssignment(
        code="TENSILE_TEST_LINK_TEMPERATUREMEASURINGSYSTEM",
        data_type="OBJECT",
        object_code="INSTRUMENT.TENSILE_TEST_TEMPERATURE_MEASURING_SYSTEM",
        property_label="TemperatureMeasuringSystem",
        description="""Linked tensile-test sub-object // Verknuepftes Zugversuchs-Unterobjekt""",
        mandatory=False,
        section="Linked objects",
    )
    tensile_test_link_temperaturesensor = PropertyTypeAssignment(
        code="TENSILE_TEST_LINK_TEMPERATURESENSOR",
        data_type="OBJECT",
        object_code="INSTRUMENT.TENSILE_TEST_TEMPERATURE_SENSOR",
        property_label="TemperatureSensor",
        description="""Linked tensile-test sub-object // Verknuepftes Zugversuchs-Unterobjekt""",
        mandatory=False,
        section="Linked objects",
    )
    tensile_test_link_temperaturedataacquisition = PropertyTypeAssignment(
        code="TENSILE_TEST_LINK_TEMPERATUREDATAACQUISITION",
        data_type="OBJECT",
        object_code="INSTRUMENT.TENSILE_TEST_TEMPERATURE_DATA_ACQUISITION",
        property_label="TemperatureDataAcquisition",
        description="""Linked tensile-test sub-object // Verknuepftes Zugversuchs-Unterobjekt""",
        mandatory=False,
        section="Linked objects",
    )
    tensile_test_link_extensometersystem = PropertyTypeAssignment(
        code="TENSILE_TEST_LINK_EXTENSOMETERSYSTEM",
        data_type="OBJECT",
        object_code="INSTRUMENT.TENSILE_TEST_EXTENSOMETER_SYSTEM",
        property_label="ExtensometerSystem",
        description="""Linked tensile-test sub-object // Verknuepftes Zugversuchs-Unterobjekt""",
        mandatory=False,
        section="Linked objects",
        ontology_IRI="https://w3id.org/pmd/co/PMD_0000636",
    )
    tensile_test_link_contactingextensometer = PropertyTypeAssignment(
        code="TENSILE_TEST_LINK_CONTACTINGEXTENSOMETER",
        data_type="OBJECT",
        object_code="INSTRUMENT.TENSILE_TEST_EXTENSION_VALUES_CONTACTING_EXTENSOMETER",
        property_label="ContactingExtensometer",
        description="""Linked tensile-test sub-object // Verknuepftes Zugversuchs-Unterobjekt""",
        mandatory=False,
        section="Linked objects",
        ontology_IRI="https://w3id.org/pmd/co/PMD_0000636",
    )
    tensile_test_link_elongationandcrosssectionalmeasuringequipment = PropertyTypeAssignment(
        code="TENSILE_TEST_LINK_ELONGATIONANDCROSSSECTIONALMEASURINGEQUIPMENT",
        data_type="OBJECT",
        object_code="INSTRUMENT.TENSILE_TEST_ELONGATION_VALUES_AND_CROSS_SECTIONAL_DIMENSIONS",
        property_label="ElongationAndCrossSectionalMeasuringEquipment",
        description="""Linked tensile-test sub-object // Verknuepftes Zugversuchs-Unterobjekt""",
        mandatory=False,
        section="Linked objects",
    )
    tensile_test_link_dataprocessingprocedures = PropertyTypeAssignment(
        code="TENSILE_TEST_LINK_DATAPROCESSINGPROCEDURES",
        data_type="OBJECT",
        object_code="COMPUTATIONAL_ANALYSIS.TENSILE_TEST_DATA_PROCESSING_PROCEDURES",
        property_label="DataProcessingProcedures",
        description="""Linked tensile-test sub-object // Verknuepftes Zugversuchs-Unterobjekt""",
        mandatory=False,
        section="Linked objects",
    )
    tensile_test_link_primaryvaluesrecordedatteststart = PropertyTypeAssignment(
        code="TENSILE_TEST_LINK_PRIMARYVALUESRECORDEDATTESTSTART",
        data_type="OBJECT",
        object_code="TENSILE_TEST_PRIMARY_VALUES_RECORDED_AT_TEST_START",
        property_label="PrimaryValuesRecordedAtTestStart",
        description="""Linked tensile-test sub-object // Verknuepftes Zugversuchs-Unterobjekt""",
        mandatory=False,
        section="Linked objects",
    )
    tensile_test_link_primaryvaluesrecordedduringtestrun = PropertyTypeAssignment(
        code="TENSILE_TEST_LINK_PRIMARYVALUESRECORDEDDURINGTESTRUN",
        data_type="OBJECT",
        object_code="TENSILE_TEST_PRIMARY_VALUES_RECORDED_DURING_TEST_RUN",
        property_label="PrimaryValuesRecordedDuringTestRun",
        description="""Linked tensile-test sub-object // Verknuepftes Zugversuchs-Unterobjekt""",
        mandatory=False,
        section="Linked objects",
    )
    tensile_test_link_primaryvaluesrecordedafterendoftest = PropertyTypeAssignment(
        code="TENSILE_TEST_LINK_PRIMARYVALUESRECORDEDAFTERENDOFTEST",
        data_type="OBJECT",
        object_code="TENSILE_TEST_PRIMARY_VALUES_RECORDED_AFTER_END_OF_TEST",
        property_label="PrimaryValuesRecordedAfterEndOfTest",
        description="""Linked tensile-test sub-object // Verknuepftes Zugversuchs-Unterobjekt""",
        mandatory=False,
        section="Linked objects",
    )
    tensile_test_link_secondaryvaluesrecordedduringtestrun = PropertyTypeAssignment(
        code="TENSILE_TEST_LINK_SECONDARYVALUESRECORDEDDURINGTESTRUN",
        data_type="OBJECT",
        object_code="TENSILE_TEST_SECONDARY_VALUES_RECORDED_DURING_TEST_RUN",
        property_label="SecondaryValuesRecordedDuringTestRun",
        description="""Linked tensile-test sub-object // Verknuepftes Zugversuchs-Unterobjekt""",
        mandatory=False,
        section="Linked objects",
    )
    tensile_test_link_secondarystrengthvalues = PropertyTypeAssignment(
        code="TENSILE_TEST_LINK_SECONDARYSTRENGTHVALUES",
        data_type="OBJECT",
        object_code="TENSILE_TEST_SECONDARY_STRENGTH_VALUES",
        property_label="SecondaryStrengthValues",
        description="""Linked tensile-test sub-object // Verknuepftes Zugversuchs-Unterobjekt""",
        mandatory=False,
        section="Linked objects",
    )
    tensile_test_link_secondaryelongationvalues = PropertyTypeAssignment(
        code="TENSILE_TEST_LINK_SECONDARYELONGATIONVALUES",
        data_type="OBJECT",
        object_code="TENSILE_TEST_SECONDARY_ELONGATION_VALUES",
        property_label="SecondaryElongationValues",
        description="""Linked tensile-test sub-object // Verknuepftes Zugversuchs-Unterobjekt""",
        mandatory=False,
        section="Linked objects",
    )
    tensile_test_link_secondaryextensionvalues = PropertyTypeAssignment(
        code="TENSILE_TEST_LINK_SECONDARYEXTENSIONVALUES",
        data_type="OBJECT",
        object_code="TENSILE_TEST_SECONDARY_EXTENSION_VALUES",
        property_label="SecondaryExtensionValues",
        description="""Linked tensile-test sub-object // Verknuepftes Zugversuchs-Unterobjekt""",
        mandatory=False,
        section="Linked objects",
    )
    tensile_test_project = PropertyTypeAssignment(
        code="TENSILE_TEST_PROJECT",
        data_type="VARCHAR",
        property_label="Project",
        description="""Project (Metadata → Test info → Test job details) // Project""",
        mandatory=False,
        section="Test job details",
    )
    tensile_test_order = PropertyTypeAssignment(
        code="TENSILE_TEST_ORDER",
        data_type="VARCHAR",
        property_label="Test order",
        description="""Test order (Metadata → Test info → Test job details) // Test order""",
        mandatory=False,
        section="Test job details",
    )
    tensile_test_standard_applied = PropertyTypeAssignment(
        code="TENSILE_TEST_STANDARD_APPLIED",
        data_type="BOOLEAN",
        property_label="Test standard applied Description: Was the test performed according to a test standard?",
        description="""Test standard applied Description: Was the test performed according to a test standard? (Metadata → Test info → Test parameters) // Test standard applied Description: Was the test performed according to a test standard?""",
        mandatory=True,
        section="Test parameters",
    )
    tensile_test_standard = PropertyTypeAssignment(
        code="TENSILE_TEST_STANDARD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_STANDARD",
        property_label="Test standard",
        description="""Test standard (Metadata → Test info → Test parameters) // Test standard""",
        mandatory=True,
        section="Test parameters",
    )
    tensile_test_specified_temperature = PropertyTypeAssignment(
        code="TENSILE_TEST_SPECIFIED_TEMPERATURE",
        data_type="REAL",
        property_label="Specified temperature",
        units="degC",
        description="""Specified temperature (Metadata → Test info → Test parameters) // Specified temperature""",
        mandatory=True,
        section="Test parameters",
        ontology_IRI="https://w3id.org/pmd/co/PMD_0000967",
    )
    tensile_test_type_of_loading = PropertyTypeAssignment(
        code="TENSILE_TEST_TYPE_OF_LOADING",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_TYPE_OF_LOADING",
        property_label="Type of loading",
        description="""Type of loading (Metadata → Test info → Test parameters) // Type of loading""",
        mandatory=True,
        section="Test parameters",
    )
    tensile_test_method_testing_rate = PropertyTypeAssignment(
        code="TENSILE_TEST_METHOD_TESTING_RATE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_METHOD_TESTING_RATE",
        property_label="Method testing rate  Method A: Testing rate based on strain rate control Method B: Method of testing with expanded strain rate ranges",
        description="""Method testing rate  Method A: Testing rate based on strain rate control Method B: Method of testing with expanded strain rate ranges (Metadata → Test info → Test parameters) // Method testing rate  Method A: Testing rate based on strain rate control Method B: Method of testing with expanded strain rate ranges""",
        mandatory=True,
        section="Test parameters",
    )
    tensile_test_testing_rate_1 = PropertyTypeAssignment(
        code="TENSILE_TEST_TESTING_RATE_1",
        data_type="REAL",
        property_label="Testing rate 1",
        units="1/s",
        description="""Testing rate 1 (Metadata → Test info → Test parameters) // Testing rate 1""",
        mandatory=True,
        section="Test parameters",
        ontology_IRI="https://w3id.org/pmd/tto/TTO_0000051",
    )
    tensile_test_switchover_point = PropertyTypeAssignment(
        code="TENSILE_TEST_SWITCHOVER_POINT",
        data_type="REAL",
        property_label="Switchover point Description: if applicable",
        units="%",
        description="""Switchover point Description: if applicable (Metadata → Test info → Test parameters) // Switchover point Description: if applicable""",
        mandatory=True,
        section="Test parameters",
        ontology_IRI="https://w3id.org/pmd/tto/TTO_0000057",
    )
    tensile_test_testing_rate_2 = PropertyTypeAssignment(
        code="TENSILE_TEST_TESTING_RATE_2",
        data_type="REAL",
        property_label="Testing rate 2",
        units="mm/s",
        description="""Testing rate 2 (Metadata → Test info → Test parameters) // Testing rate 2""",
        mandatory=True,
        section="Test parameters",
        ontology_IRI="https://w3id.org/pmd/tto/TTO_0000014",
    )
    tensile_test_extensometer_gauge_length_determination = PropertyTypeAssignment(
        code="TENSILE_TEST_EXTENSOMETER_GAUGE_LENGTH_DETERMINATION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_EXTENSOMETER_GAUGE_LENGTH_DETERMINATION",
        property_label="Extensometer's attachment and determination of extensometer gauge length, Le Description: please select the method that was used to determine Le",
        description="""Extensometer's attachment and determination of extensometer gauge length, Le Description: please select the method that was used to determine Le (Metadata → Test info → Test parameters) // Extensometer's attachment and determination of extensometer gauge length, Le Description: please select the method that was used to determine Le""",
        mandatory=True,
        section="Test parameters",
    )
    tensile_test_interruption_course = PropertyTypeAssignment(
        code="TENSILE_TEST_INTERRUPTION_COURSE",
        data_type="MULTILINE_VARCHAR",
        property_label="Interruption course. Description: Interim investigations or if the test was not run to failure, etc.",
        description="""Interruption course. Description: Interim investigations or if the test was not run to failure, etc. (Metadata → Test info → Test parameters) // Interruption course. Description: Interim investigations or if the test was not run to failure, etc.""",
        mandatory=True,
        section="Test parameters",
    )
    tensile_test_any_related_articles = PropertyTypeAssignment(
        code="TENSILE_TEST_ANY_RELATED_ARTICLES",
        data_type="BOOLEAN",
        property_label="Any related articles",
        description="""Any related articles (Metadata → Test info → Related research outcome) // Any related articles""",
        mandatory=False,
        section="Related research outcome",
    )
    tensile_test_related_article = PropertyTypeAssignment(
        code="TENSILE_TEST_RELATED_ARTICLE",
        data_type="MULTILINE_VARCHAR",
        property_label="Related article (Multiple input entries for instance for MSE research article DOI, Zenodo DOI, FDO)",
        description="""Related article (Multiple input entries for instance for MSE research article DOI, Zenodo DOI, FDO) (Metadata → Test info → Related research outcome) // Related article (Multiple input entries for instance for MSE research article DOI, Zenodo DOI, FDO)""",
        mandatory=False,
        section="Related research outcome",
    )

class TensileTestContactingExtensometer(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.TENSILE_TEST_EXTENSION_VALUES_CONTACTING_EXTENSOMETER",
        description="""Tensile-test data object: TensileTestContactingExtensometer // Datenobjekt fuer den Zugversuch: TensileTestContactingExtensometer""",
        generated_code_prefix="INS.TENSILE_EXTEN_VALUE",
    )
    tensile_test_measurement_set_up = PropertyTypeAssignment(
        code="TENSILE_TEST_MEASUREMENT_SET_UP",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_MEASUREMENT_SETUP",
        property_label="Measurement set-up Description: Measurement one-sided or two-sided?",
        description="""Measurement set-up Description: Measurement one-sided or two-sided? (Metadata → Measuring and test equipment → Extension values → Contacting extensometer) // Measurement set-up Description: Measurement one-sided or two-sided?""",
        mandatory=True,
        section="Contacting extensometer",
    )
    tensile_test_extension_averaging = PropertyTypeAssignment(
        code="TENSILE_TEST_EXTENSION_AVERAGING",
        data_type="MULTILINE_VARCHAR",
        property_label="Extension averaging Description: was there an averaging of the extension values? (two-sided extensometer)",
        description="""Extension averaging Description: was there an averaging of the extension values? (two-sided extensometer) (Metadata → Measuring and test equipment → Extension values → Contacting extensometer) // Extension averaging Description: was there an averaging of the extension values? (two-sided extensometer)""",
        mandatory=True,
        section="Contacting extensometer",
    )
    tensile_test_measurement_direction = PropertyTypeAssignment(
        code="TENSILE_TEST_MEASUREMENT_DIRECTION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_MEASUREMENT_DIRECTION",
        property_label="Measurement direction",
        description="""Measurement direction (Metadata → Measuring and test equipment → Extension values → Contacting extensometer) // Measurement direction""",
        mandatory=True,
        section="Contacting extensometer",
    )
    tensile_test_mounting_type = PropertyTypeAssignment(
        code="TENSILE_TEST_MOUNTING_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_MOUNTING_TYPE",
        property_label="Mounting type",
        description="""Mounting type (Metadata → Measuring and test equipment → Extension values → Contacting extensometer) // Mounting type""",
        mandatory=True,
        section="Contacting extensometer",
    )
    tensile_test_extensometer_model_information = PropertyTypeAssignment(
        code="TENSILE_TEST_EXTENSOMETER_MODEL_INFORMATION",
        data_type="MULTILINE_VARCHAR",
        property_label="Extensometer model information",
        description="""Extensometer model information (Metadata → Measuring and test equipment → Extension values → Contacting extensometer) // Extensometer model information""",
        mandatory=False,
        section="Contacting extensometer",
    )
    tensile_test_extensometer_id = PropertyTypeAssignment(
        code="TENSILE_TEST_EXTENSOMETER_ID",
        data_type="MULTILINE_VARCHAR",
        property_label="Extensometer ID Description: The ID used for identification in the laboratory",
        description="""Extensometer ID Description: The ID used for identification in the laboratory (Metadata → Measuring and test equipment → Extension values → Contacting extensometer) // Extensometer ID Description: The ID used for identification in the laboratory""",
        mandatory=False,
        section="Contacting extensometer",
        ontology_IRI="http://purl.obolibrary.org/obo/IAO_0020000",
    )
    tensile_test_extensometer_leg_material = PropertyTypeAssignment(
        code="TENSILE_TEST_EXTENSOMETER_LEG_MATERIAL",
        data_type="MULTILINE_VARCHAR",
        property_label="Extensometer leg material Description: material of upper/lower legs, e.g., in LVDT systems",
        description="""Extensometer leg material Description: material of upper/lower legs, e.g., in LVDT systems (Metadata → Measuring and test equipment → Extension values → Contacting extensometer) // Extensometer leg material Description: material of upper/lower legs, e.g., in LVDT systems""",
        mandatory=False,
        section="Contacting extensometer",
    )
    tensile_test_measuring_amplifier_model_information = PropertyTypeAssignment(
        code="TENSILE_TEST_MEASURING_AMPLIFIER_MODEL_INFORMATION",
        data_type="MULTILINE_VARCHAR",
        property_label="Measuring amplifier - Model information",
        description="""Measuring amplifier - Model information (Metadata → Measuring and test equipment → Extension values → Contacting extensometer) // Measuring amplifier - Model information""",
        mandatory=False,
        section="Contacting extensometer",
    )
    tensile_test_extension_range_upper_limit = PropertyTypeAssignment(
        code="TENSILE_TEST_EXTENSION_RANGE_UPPER_LIMIT",
        data_type="REAL",
        property_label="Extension range - Upper limit",
        units="%",
        description="""Extension range - Upper limit (Metadata → Measuring and test equipment → Extension values → Contacting extensometer) // Extension range - Upper limit""",
        mandatory=True,
        section="Contacting extensometer",
        ontology_IRI="https://w3id.org/pmd/tto/TTO_0000005",
    )
    tensile_test_extension_range_lower_limit = PropertyTypeAssignment(
        code="TENSILE_TEST_EXTENSION_RANGE_LOWER_LIMIT",
        data_type="REAL",
        property_label="Extension range - Lower limit",
        units="%",
        description="""Extension range - Lower limit (Metadata → Measuring and test equipment → Extension values → Contacting extensometer) // Extension range - Lower limit""",
        mandatory=True,
        section="Contacting extensometer",
        ontology_IRI="https://w3id.org/pmd/tto/TTO_0000005",
    )
    tensile_test_nominal_gauge_length = PropertyTypeAssignment(
        code="TENSILE_TEST_NOMINAL_GAUGE_LENGTH",
        data_type="REAL",
        property_label="Nominal gauge length Description: if applicable",
        units="mm",
        description="""Nominal gauge length Description: if applicable (Metadata → Measuring and test equipment → Extension values → Contacting extensometer) // Nominal gauge length Description: if applicable""",
        mandatory=True,
        section="Contacting extensometer",
    )
    tensile_test_calibration_status = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_STATUS",
        data_type="BOOLEAN",
        property_label="Calibration status Description: Is the extensometer calibrated?",
        description="""Calibration status Description: Is the extensometer calibrated? (Metadata → Measuring and test equipment → Extension values → Contacting extensometer) // Calibration status Description: Is the extensometer calibrated?""",
        mandatory=True,
        section="Contacting extensometer",
    )
    tensile_test_calibration_certificate = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_CERTIFICATE",
        data_type="MULTILINE_VARCHAR",
        property_label="Calibration certificate Description: Link to File, preferably with machine-readable (meta)data.",
        description="""Calibration certificate Description: Link to File, preferably with machine-readable (meta)data. (Metadata → Measuring and test equipment → Extension values → Contacting extensometer) // Calibration certificate Description: Link to File, preferably with machine-readable (meta)data.""",
        mandatory=False,
        section="Contacting extensometer",
    )
    tensile_test_calibration_date = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_DATE",
        data_type="DATE",
        property_label="Calibration date",
        description="""Calibration date (Metadata → Measuring and test equipment → Extension values → Contacting extensometer) // Calibration date""",
        mandatory=True,
        section="Contacting extensometer",
    )
    tensile_test_calibration_validity_time_period = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_VALIDITY_TIME_PERIOD",
        data_type="VARCHAR",
        property_label="Calibration validity time period",
        description="""Calibration validity time period (Metadata → Measuring and test equipment → Extension values → Contacting extensometer) // Calibration validity time period""",
        mandatory=True,
        section="Contacting extensometer",
    )
    tensile_test_calibration_class = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_CLASS",
        data_type="VARCHAR",
        property_label="Calibration class",
        description="""Calibration class (Metadata → Measuring and test equipment → Extension values → Contacting extensometer) // Calibration class""",
        mandatory=True,
        section="Contacting extensometer",
    )
    tensile_test_calibration_range = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_RANGE",
        data_type="REAL",
        property_label="Calibration Range",
        units="%",
        description="""Calibration Range (Metadata → Measuring and test equipment → Extension values → Contacting extensometer) // Calibration Range""",
        mandatory=True,
        section="Contacting extensometer",
    )
    tensile_test_calibration_standard = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_STANDARD",
        data_type="VARCHAR",
        property_label="Calibration standard",
        description="""Calibration standard (Metadata → Measuring and test equipment → Extension values → Contacting extensometer) // Calibration standard""",
        mandatory=True,
        section="Contacting extensometer",
    )

class TensileTestDataProcessingProcedures(ComputationalAnalysis):
    defs = ObjectTypeDef(
        code="COMPUTATIONAL_ANALYSIS.TENSILE_TEST_DATA_PROCESSING_PROCEDURES",
        description="""Tensile-test data object: TensileTestDataProcessingProcedures // Datenobjekt fuer den Zugversuch: TensileTestDataProcessingProcedures""",
        generated_code_prefix="COMP.TENSILE_DATA_PROCE",
    )
    tensile_test_primary_data_series = PropertyTypeAssignment(
        code="TENSILE_TEST_PRIMARY_DATA_SERIES",
        data_type="MULTILINE_VARCHAR",
        property_label="Primary data series Description: Primary data is data that is directly acquired by sensors or measuring instruments during or after a test. Please add a list of the measured quantities and their corresponsing units.",
        description="""Primary data series Description: Primary data is data that is directly acquired by sensors or measuring instruments during or after a test. Please add a list of the measured quantities and their corresponsing units. (Metadata → Data processing procedures) // Primary data series Description: Primary data is data that is directly acquired by sensors or measuring instruments during or after a test. Please add a list of the measured quantities and their corresponsing units.""",
        mandatory=True,
        section="Data processing procedures",
    )
    tensile_test_processed_data_series = PropertyTypeAssignment(
        code="TENSILE_TEST_PROCESSED_DATA_SERIES",
        data_type="MULTILINE_VARCHAR",
        property_label="Processed data series  Description: Processed data is obtained as a result of using procedures (equations, algorithms, methods, unit conversions, averaging, smoothing) to transform primary data. Please describe the transformed quantities, their corresponsing units, and the applied procedures.",
        description="""Processed data series  Description: Processed data is obtained as a result of using procedures (equations, algorithms, methods, unit conversions, averaging, smoothing) to transform primary data. Please describe the transformed quantities, their corresponsing units, and the applied procedures. (Metadata → Data processing procedures) // Processed data series  Description: Processed data is obtained as a result of using procedures (equations, algorithms, methods, unit conversions, averaging, smoothing) to transform primary data. Please describe the transformed quantities, their corresponsing units, and the applied procedures.""",
        mandatory=True,
        section="Data processing procedures",
    )
    tensile_test_data_analysis_procedures = PropertyTypeAssignment(
        code="TENSILE_TEST_DATA_ANALYSIS_PROCEDURES",
        data_type="MULTILINE_VARCHAR",
        property_label="Data analysis procedures Description: Description of the data processing and analysis procedures used to obtain specific test results, e.g. percentage extension, e",
        description="""Data analysis procedures Description: Description of the data processing and analysis procedures used to obtain specific test results, e.g. percentage extension, e (Metadata → Data processing procedures) // Data analysis procedures Description: Description of the data processing and analysis procedures used to obtain specific test results, e.g. percentage extension, e""",
        mandatory=True,
        section="Data processing procedures",
    )
    tensile_test_workflow_usage = PropertyTypeAssignment(
        code="TENSILE_TEST_WORKFLOW_USAGE",
        data_type="BOOLEAN",
        property_label="Workflow usage Description: Were automated (user-independent) analysis workflows used?",
        description="""Workflow usage Description: Were automated (user-independent) analysis workflows used? (Metadata → Data processing procedures) // Workflow usage Description: Were automated (user-independent) analysis workflows used?""",
        mandatory=True,
        section="Data processing procedures",
        ontology_IRI="https://w3id.org/pmd/co/PMD_0000016",
    )
    tensile_test_software = PropertyTypeAssignment(
        code="TENSILE_TEST_SOFTWARE",
        data_type="MULTILINE_VARCHAR",
        property_label="Software Description: If applicable, please list the used software/workflow, including product and version",
        description="""Software Description: If applicable, please list the used software/workflow, including product and version (Metadata → Data processing procedures) // Software Description: If applicable, please list the used software/workflow, including product and version""",
        mandatory=True,
        section="Data processing procedures",
        ontology_IRI="http://purl.obolibrary.org/obo/IAO_0000010",
    )
    tensile_test_related_publications = PropertyTypeAssignment(
        code="TENSILE_TEST_RELATED_PUBLICATIONS",
        data_type="MULTILINE_VARCHAR",
        property_label="Related publications Description: If applicable, please list  publications related to the data analysis procedure/software used",
        description="""Related publications Description: If applicable, please list  publications related to the data analysis procedure/software used (Metadata → Data processing procedures) // Related publications Description: If applicable, please list  publications related to the data analysis procedure/software used""",
        mandatory=False,
        section="Data processing procedures",
    )

class TensileTestElongationAndCrossSectionalMeasuringEquipment(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.TENSILE_TEST_ELONGATION_VALUES_AND_CROSS_SECTIONAL_DIMENSIONS",
        description="""Tensile-test data object: TensileTestElongationAndCrossSectionalMeasuringEquipment // Datenobjekt fuer den Zugversuch: TensileTestElongationAndCrossSectionalMeasuringEquipment""",
        generated_code_prefix="INS.TENSILE_ELONG_VALUE",
    )
    tensile_test_measuring_equipment_1 = PropertyTypeAssignment(
        code="TENSILE_TEST_MEASURING_EQUIPMENT_1",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_MEASURING_EQUIPMENT",
        property_label="Measuring equipment 1",
        description="""Measuring equipment 1 (Metadata → Measuring and test equipment → Elongation and cross-sectional values) // Measuring equipment 1""",
        mandatory=True,
        section="Elongation and cross-sectional values",
    )
    tensile_test_measuring_equipment_s_usage = PropertyTypeAssignment(
        code="TENSILE_TEST_MEASURING_EQUIPMENT_S_USAGE",
        data_type="VARCHAR",
        property_label="Measuring equipment's usage",
        description="""Measuring equipment's usage (Metadata → Measuring and test equipment → Elongation and cross-sectional values) // Measuring equipment's usage""",
        mandatory=True,
        section="Elongation and cross-sectional values",
    )
    tensile_test_resolution = PropertyTypeAssignment(
        code="TENSILE_TEST_RESOLUTION",
        data_type="REAL",
        property_label="Resolution",
        units="mm",
        description="""Resolution (Metadata → Measuring and test equipment → Elongation and cross-sectional values) // Resolution""",
        mandatory=True,
        section="Elongation and cross-sectional values",
    )
    tensile_test_type = PropertyTypeAssignment(
        code="TENSILE_TEST_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_MEASURING_EQUIPMENT_TYPE",
        property_label="Type",
        description="""Type (Metadata → Measuring and test equipment → Elongation and cross-sectional values) // Type""",
        mandatory=False,
        section="Elongation and cross-sectional values",
    )
    tensile_test_equipment_model_information = PropertyTypeAssignment(
        code="TENSILE_TEST_EQUIPMENT_MODEL_INFORMATION",
        data_type="MULTILINE_VARCHAR",
        property_label="Equipment model information",
        description="""Equipment model information (Metadata → Measuring and test equipment → Elongation and cross-sectional values) // Equipment model information""",
        mandatory=False,
        section="Elongation and cross-sectional values",
    )
    tensile_test_equipment_id = PropertyTypeAssignment(
        code="TENSILE_TEST_EQUIPMENT_ID",
        data_type="MULTILINE_VARCHAR",
        property_label="Equipment ID Description: The ID used for identification in the laboratory",
        description="""Equipment ID Description: The ID used for identification in the laboratory (Metadata → Measuring and test equipment → Elongation and cross-sectional values) // Equipment ID Description: The ID used for identification in the laboratory""",
        mandatory=False,
        section="Elongation and cross-sectional values",
        ontology_IRI="http://purl.obolibrary.org/obo/IAO_0020000",
    )
    tensile_test_calibration_status = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_STATUS",
        data_type="BOOLEAN",
        property_label="Calibration status Description: Is the measuring equipment calibrated?",
        description="""Calibration status Description: Is the measuring equipment calibrated? (Metadata → Measuring and test equipment → Elongation and cross-sectional values) // Calibration status Description: Is the measuring equipment calibrated?""",
        mandatory=True,
        section="Elongation and cross-sectional values",
    )
    tensile_test_calibration_certificate = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_CERTIFICATE",
        data_type="MULTILINE_VARCHAR",
        property_label="Calibration certificate Description: Link to File, preferably with machine-readable (meta)data.",
        description="""Calibration certificate Description: Link to File, preferably with machine-readable (meta)data. (Metadata → Measuring and test equipment → Elongation and cross-sectional values) // Calibration certificate Description: Link to File, preferably with machine-readable (meta)data.""",
        mandatory=False,
        section="Elongation and cross-sectional values",
    )
    tensile_test_calibration_date = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_DATE",
        data_type="DATE",
        property_label="Calibration date",
        description="""Calibration date (Metadata → Measuring and test equipment → Elongation and cross-sectional values) // Calibration date""",
        mandatory=True,
        section="Elongation and cross-sectional values",
    )
    tensile_test_calibration_validity_time_period = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_VALIDITY_TIME_PERIOD",
        data_type="VARCHAR",
        property_label="Calibration validity time period",
        description="""Calibration validity time period (Metadata → Measuring and test equipment → Elongation and cross-sectional values) // Calibration validity time period""",
        mandatory=True,
        section="Elongation and cross-sectional values",
    )
    tensile_test_calibration_result = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_RESULT",
        data_type="VARCHAR",
        property_label="Calibration result",
        description="""Calibration result (Metadata → Measuring and test equipment → Elongation and cross-sectional values) // Calibration result""",
        mandatory=True,
        section="Elongation and cross-sectional values",
    )
    tensile_test_calibration_range = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_RANGE",
        data_type="VARCHAR",
        property_label="Calibration range",
        units="mm",
        description="""Calibration range (Metadata → Measuring and test equipment → Elongation and cross-sectional values) // Calibration range""",
        mandatory=True,
        section="Elongation and cross-sectional values",
    )
    tensile_test_calibration_standard = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_STANDARD",
        data_type="VARCHAR",
        property_label="Calibration standard",
        description="""Calibration standard (Metadata → Measuring and test equipment → Elongation and cross-sectional values) // Calibration standard""",
        mandatory=True,
        section="Elongation and cross-sectional values",
    )
    tensile_test_measuring_equipment_2 = PropertyTypeAssignment(
        code="TENSILE_TEST_MEASURING_EQUIPMENT_2",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_MEASURING_EQUIPMENT",
        property_label="Measuring equipment 2",
        description="""Measuring equipment 2 (Metadata → Measuring and test equipment → Elongation and cross-sectional values) // Measuring equipment 2""",
        mandatory=True,
        section="Elongation and cross-sectional values",
    )
    tensile_test_measuring_equipment_3 = PropertyTypeAssignment(
        code="TENSILE_TEST_MEASURING_EQUIPMENT_3",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_MEASURING_EQUIPMENT",
        property_label="Measuring equipment 3",
        description="""Measuring equipment 3 (Metadata → Measuring and test equipment → Elongation and cross-sectional values) // Measuring equipment 3""",
        mandatory=True,
        section="Elongation and cross-sectional values",
    )

class TensileTestExtensometerSystem(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.TENSILE_TEST_EXTENSOMETER_SYSTEM",
        description="""Tensile-test data object: TensileTestExtensometerSystem // Datenobjekt fuer den Zugversuch: TensileTestExtensometerSystem""",
        generated_code_prefix="INS.TENSILE_EXTEN_SYSTE",
    )
    tensile_test_displacement_measuring_method = PropertyTypeAssignment(
        code="TENSILE_TEST_DISPLACEMENT_MEASURING_METHOD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_DISPLACEMENT_MEASURING_METHOD",
        property_label="Displacement measuring method Description: Type of strain measuring device",
        description="""Displacement measuring method Description: Type of strain measuring device (Metadata → Measuring and test equipment → Extensometer system) // Displacement measuring method Description: Type of strain measuring device""",
        mandatory=True,
        section="Extensometer system",
    )
    tensile_test_sensor_type_contacting_method = PropertyTypeAssignment(
        code="TENSILE_TEST_SENSOR_TYPE_CONTACTING_METHOD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_SENSOR_TYPE_CONTACTING",
        property_label="Sensor type - Contacting method",
        description="""Sensor type - Contacting method (Metadata → Measuring and test equipment → Extensometer system) // Sensor type - Contacting method""",
        mandatory=True,
        section="Extensometer system",
    )
    tensile_test_sensor_type_non_contacting_method = PropertyTypeAssignment(
        code="TENSILE_TEST_SENSOR_TYPE_NON_CONTACTING_METHOD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_SENSOR_TYPE_NON_CONTACTING",
        property_label="Sensor type - Non-contacting method",
        description="""Sensor type - Non-contacting method (Metadata → Measuring and test equipment → Extensometer system) // Sensor type - Non-contacting method""",
        mandatory=True,
        section="Extensometer system",
    )

class TensileTestHeatingSystem(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.TENSILE_TEST_MACHINE_HEATING_SYSTEM",
        description="""Tensile-test data object: TensileTestHeatingSystem // Datenobjekt fuer den Zugversuch: TensileTestHeatingSystem""",
        generated_code_prefix="INS.TENSILE_MACHI_HEATI",
    )
    tensile_test_furnace_type = PropertyTypeAssignment(
        code="TENSILE_TEST_FURNACE_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_FURNACE_TYPE",
        property_label="Furnace type",
        description="""Furnace type (Metadata → Measuring and test equipment → Test machine → Heating system) // Furnace type""",
        mandatory=True,
        section="Heating system",
        ontology_IRI="https://w3id.org/pmd/co/PMD_0000655",
    )

class TensileTestLaboratoryConditions(EnvironmentalConditions):
    defs = ObjectTypeDef(
        code="ENVIRONMENTAL_CONDITIONS.TENSILE_TEST_LABORATORY_CONDITIONS",
        description="""Tensile-test data object: TensileTestLaboratoryConditions // Datenobjekt fuer den Zugversuch: TensileTestLaboratoryConditions""",
        generated_code_prefix="ENV.TENSILE_LABOR_CONDI",
    )
    tensile_test_room_temperature = PropertyTypeAssignment(
        code="TENSILE_TEST_ROOM_TEMPERATURE",
        data_type="BOOLEAN",
        property_label="Room temperature Description: Was the room temperature recorded and checked?",
        description="""Room temperature Description: Was the room temperature recorded and checked? (Metadata → Measuring and test equipment → Laboratory conditions) // Room temperature Description: Was the room temperature recorded and checked?""",
        mandatory=True,
        section="Laboratory conditions",
    )
    tensile_test_air_flow_of_the_surrounding = PropertyTypeAssignment(
        code="TENSILE_TEST_AIR_FLOW_OF_THE_SURROUNDING",
        data_type="MULTILINE_VARCHAR",
        property_label="Air flow of the surrounding Description: Was the setup protected from drafts/room temperature fluctuations?",
        description="""Air flow of the surrounding Description: Was the setup protected from drafts/room temperature fluctuations? (Metadata → Measuring and test equipment → Laboratory conditions) // Air flow of the surrounding Description: Was the setup protected from drafts/room temperature fluctuations?""",
        mandatory=False,
        section="Laboratory conditions",
    )
    tensile_test_room_humidity = PropertyTypeAssignment(
        code="TENSILE_TEST_ROOM_HUMIDITY",
        data_type="BOOLEAN",
        property_label="Room humidity Description: Was the room humidity recorded and checked?",
        description="""Room humidity Description: Was the room humidity recorded and checked? (Metadata → Measuring and test equipment → Laboratory conditions) // Room humidity Description: Was the room humidity recorded and checked?""",
        mandatory=False,
        section="Laboratory conditions",
    )

class TensileTestLoadDataAcquisition(ObjectType):
    defs = ObjectTypeDef(
        code="TENSILE_TEST_LOAD_DATA_ACQUISITION",
        description="""Tensile-test data object: TensileTestLoadDataAcquisition // Datenobjekt fuer den Zugversuch: TensileTestLoadDataAcquisition""",
        generated_code_prefix="TENSILE_LOAD_DATA_ACQU",
    )
    tensile_test_force_recording = PropertyTypeAssignment(
        code="TENSILE_TEST_FORCE_RECORDING",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_FORCE_RECORDING",
        property_label="Force recording Description: Was the force recorded continuously or periodically?",
        description="""Force recording Description: Was the force recorded continuously or periodically? (Metadata → Measuring and test equipment → Load-measuring system → Data acquisition) // Force recording Description: Was the force recorded continuously or periodically?""",
        mandatory=True,
        section="Data acquisition",
    )

class TensileTestLoadSensor(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.TENSILE_TEST_LOAD_SENSOR",
        description="""Tensile-test data object: TensileTestLoadSensor // Datenobjekt fuer den Zugversuch: TensileTestLoadSensor""",
        generated_code_prefix="INS.TENSILE_LOAD_SENSO",
    )
    tensile_test_load_sensor = PropertyTypeAssignment(
        code="TENSILE_TEST_LOAD_SENSOR",
        data_type="BOOLEAN",
        property_label="Load sensor Description: Was a load sensor used?",
        description="""Load sensor Description: Was a load sensor used? (Metadata → Measuring and test equipment → Load-measuring system → Load sensor) // Load sensor Description: Was a load sensor used?""",
        mandatory=True,
        section="Load sensor",
    )
    tensile_test_load_sensor_calibration = PropertyTypeAssignment(
        code="TENSILE_TEST_LOAD_SENSOR_CALIBRATION",
        data_type="BOOLEAN",
        property_label="Load sensor calibration Description: Was the load sensor calibrated?",
        description="""Load sensor calibration Description: Was the load sensor calibrated? (Metadata → Measuring and test equipment → Load-measuring system → Load sensor) // Load sensor calibration Description: Was the load sensor calibrated?""",
        mandatory=True,
        section="Load sensor",
    )
    tensile_test_calibration_certificate = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_CERTIFICATE",
        data_type="MULTILINE_VARCHAR",
        property_label="Calibration certificate Description: Link to File, preferably with machine-readable (meta)data.",
        description="""Calibration certificate Description: Link to File, preferably with machine-readable (meta)data. (Metadata → Measuring and test equipment → Load-measuring system → Load sensor) // Calibration certificate Description: Link to File, preferably with machine-readable (meta)data.""",
        mandatory=False,
        section="Load sensor",
    )
    tensile_test_calibration_date = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_DATE",
        data_type="DATE",
        property_label="Calibration date",
        description="""Calibration date (Metadata → Measuring and test equipment → Load-measuring system → Load sensor) // Calibration date""",
        mandatory=True,
        section="Load sensor",
    )
    tensile_test_calibration_validity_time_period = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_VALIDITY_TIME_PERIOD",
        data_type="VARCHAR",
        property_label="Calibration validity time period",
        description="""Calibration validity time period (Metadata → Measuring and test equipment → Load-measuring system → Load sensor) // Calibration validity time period""",
        mandatory=True,
        section="Load sensor",
    )
    tensile_test_calibration_standard = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_STANDARD",
        data_type="VARCHAR",
        property_label="Calibration standard",
        description="""Calibration standard (Metadata → Measuring and test equipment → Load-measuring system → Load sensor) // Calibration standard""",
        mandatory=True,
        section="Load sensor",
    )
    tensile_test_calibration_class = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_CLASS",
        data_type="VARCHAR",
        property_label="Calibration class",
        description="""Calibration class (Metadata → Measuring and test equipment → Load-measuring system → Load sensor) // Calibration class""",
        mandatory=True,
        section="Load sensor",
    )
    tensile_test_calibration_range = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_RANGE",
        data_type="REAL",
        property_label="Calibration Range",
        description="""Calibration Range (Metadata → Measuring and test equipment → Load-measuring system → Load sensor) // Calibration Range""",
        mandatory=True,
        section="Load sensor",
    )

class TensileTestMachineDataAcquisition(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.TENSILE_TEST_MACHINE_DATA_ACQUISITION",
        description="""Tensile-test data object: TensileTestMachineDataAcquisition // Datenobjekt fuer den Zugversuch: TensileTestMachineDataAcquisition""",
        generated_code_prefix="INS.TENSILE_MACHI_DATA",
    )
    tensile_test_data_acquisition_unit_model_information = PropertyTypeAssignment(
        code="TENSILE_TEST_DATA_ACQUISITION_UNIT_MODEL_INFORMATION",
        data_type="MULTILINE_VARCHAR",
        property_label="Data acquisition unit - Model information",
        description="""Data acquisition unit - Model information (Metadata → Measuring and test equipment → Test machine → Data acquisition) // Data acquisition unit - Model information""",
        mandatory=False,
        section="Data acquisition",
    )
    tensile_test_data_acquisition_unit_id = PropertyTypeAssignment(
        code="TENSILE_TEST_DATA_ACQUISITION_UNIT_ID",
        data_type="VARCHAR",
        property_label="Data acquisition unit - ID",
        description="""Data acquisition unit - ID (Metadata → Measuring and test equipment → Test machine → Data acquisition) // Data acquisition unit - ID""",
        mandatory=False,
        section="Data acquisition",
        ontology_IRI="http://purl.obolibrary.org/obo/IAO_0020000",
    )
    tensile_test_data_acquisition_software_and_version = PropertyTypeAssignment(
        code="TENSILE_TEST_DATA_ACQUISITION_SOFTWARE_AND_VERSION",
        data_type="VARCHAR",
        property_label="Data acquisition software and version",
        description="""Data acquisition software and version (Metadata → Measuring and test equipment → Test machine → Data acquisition) // Data acquisition software and version""",
        mandatory=True,
        section="Data acquisition",
    )
    tensile_test_data_acquisition = PropertyTypeAssignment(
        code="TENSILE_TEST_DATA_ACQUISITION",
        data_type="MULTILINE_VARCHAR",
        property_label="Data acquisition - description",
        description="""Data acquisition - description (Metadata → Measuring and test equipment → Test machine → Data acquisition) // Data acquisition - description""",
        mandatory=True,
        section="Data acquisition",
    )
    tensile_test_time_verification_of_the_data_acquisition_unit = PropertyTypeAssignment(
        code="TENSILE_TEST_TIME_VERIFICATION_OF_THE_DATA_ACQUISITION_UNIT",
        data_type="BOOLEAN",
        property_label="Time verification of the data acquisition unit Description: Was the correctness of the time values of the data acquisition unit during data acquisition checked against a time reference?",
        description="""Time verification of the data acquisition unit Description: Was the correctness of the time values of the data acquisition unit during data acquisition checked against a time reference? (Metadata → Measuring and test equipment → Test machine → Data acquisition) // Time verification of the data acquisition unit Description: Was the correctness of the time values of the data acquisition unit during data acquisition checked against a time reference?""",
        mandatory=False,
        section="Data acquisition",
    )

class TensileTestMaterialHistoryAndCondition(ObjectType):
    defs = ObjectTypeDef(
        code="TENSILE_TEST_MATERIAL_HISTORY_AND_CONDITION",
        description="""Tensile-test data object: TensileTestMaterialHistoryAndCondition // Datenobjekt fuer den Zugversuch: TensileTestMaterialHistoryAndCondition""",
        generated_code_prefix="TENSILE_MATER_HISTO",
    )
    tensile_test_material_identifier = PropertyTypeAssignment(
        code="TENSILE_TEST_MATERIAL_IDENTIFIER",
        data_type="MULTILINE_VARCHAR",
        property_label="Material Identifier  Description: e.g., NIMONIC75, 2.4630, CMSX-6, CMSX-4, ERBO1, …",
        description="""Material Identifier  Description: e.g., NIMONIC75, 2.4630, CMSX-6, CMSX-4, ERBO1, … (Metadata → Material History and Condition) // Material Identifier  Description: e.g., NIMONIC75, 2.4630, CMSX-6, CMSX-4, ERBO1, …""",
        mandatory=True,
        section="Material History and Condition",
        ontology_IRI="http://purl.obolibrary.org/obo/IAO_0020000",
    )
    tensile_test_phase_transformation_during_test = PropertyTypeAssignment(
        code="TENSILE_TEST_PHASE_TRANSFORMATION_DURING_TEST",
        data_type="BOOLEAN",
        property_label="Phase transformation during test?",
        description="""Phase transformation during test? (Metadata → Material History and Condition → As-manufactured material) // Phase transformation during test?""",
        mandatory=False,
        section="As-manufactured material",
        ontology_IRI="https://w3id.org/pmd/co/PMD_0020136",
    )
    tensile_test_possible_phase_transformation = PropertyTypeAssignment(
        code="TENSILE_TEST_POSSIBLE_PHASE_TRANSFORMATION",
        data_type="MULTILINE_VARCHAR",
        property_label="Possible phase transformation Description: Is any phase transformation expected due to temperature during the creep test?. Please provide any supporting material if possible. Answers could be, e.g., a link to a TTT-curve or a DOI of an article",
        description="""Possible phase transformation Description: Is any phase transformation expected due to temperature during the creep test?. Please provide any supporting material if possible. Answers could be, e.g., a link to a TTT-curve or a DOI of an article (Metadata → Material History and Condition → As-manufactured material) // Possible phase transformation Description: Is any phase transformation expected due to temperature during the creep test?. Please provide any supporting material if possible. Answers could be, e.g., a link to a TTT-curve or a DOI of an article""",
        mandatory=False,
        section="As-manufactured material",
    )
    tensile_test_form_of_as_manufactured_material = PropertyTypeAssignment(
        code="TENSILE_TEST_FORM_OF_AS_MANUFACTURED_MATERIAL",
        data_type="MULTILINE_VARCHAR",
        property_label="Form of as-manufactured material Description: e.g., Cast, Ingot, Extrution rod, ...",
        description="""Form of as-manufactured material Description: e.g., Cast, Ingot, Extrution rod, ... (Metadata → Material History and Condition → As-manufactured material) // Form of as-manufactured material Description: e.g., Cast, Ingot, Extrution rod, ...""",
        mandatory=True,
        section="As-manufactured material",
    )
    tensile_test_geometry_size_as_manufactured_material = PropertyTypeAssignment(
        code="TENSILE_TEST_GEOMETRY_SIZE_AS_MANUFACTURED_MATERIAL",
        data_type="MULTILINE_VARCHAR",
        property_label="Geometry/size as-manufactured material Description: Please provide a description or/and any supporting material, e.g.,  link to image or technical drawing, if possible.",
        description="""Geometry/size as-manufactured material Description: Please provide a description or/and any supporting material, e.g.,  link to image or technical drawing, if possible. (Metadata → Material History and Condition → As-manufactured material) // Geometry/size as-manufactured material Description: Please provide a description or/and any supporting material, e.g.,  link to image or technical drawing, if possible.""",
        mandatory=True,
        section="As-manufactured material",
    )
    tensile_test_manufacturing_process = PropertyTypeAssignment(
        code="TENSILE_TEST_MANUFACTURING_PROCESS",
        data_type="MULTILINE_VARCHAR",
        property_label="Manufacturing process description as-manufactured material Description: e.g., Cast / Melting, Casting, and Remelting  / Induction melting in air, casting into a circular ingot and then electroslag remelting",
        description="""Manufacturing process description as-manufactured material Description: e.g., Cast / Melting, Casting, and Remelting  / Induction melting in air, casting into a circular ingot and then electroslag remelting (Metadata → Material History and Condition → As-manufactured material) // Manufacturing process description as-manufactured material Description: e.g., Cast / Melting, Casting, and Remelting  / Induction melting in air, casting into a circular ingot and then electroslag remelting""",
        mandatory=False,
        section="As-manufactured material",
    )
    tensile_test_casting_temperature = PropertyTypeAssignment(
        code="TENSILE_TEST_CASTING_TEMPERATURE",
        data_type="VARCHAR",
        property_label="Casting temperature",
        description="""Casting temperature (Metadata → Material History and Condition → As-manufactured material) // Casting temperature""",
        mandatory=False,
        section="As-manufactured material",
        ontology_IRI="https://w3id.org/pmd/co/PMD_0000967",
    )
    tensile_test_casting_speed = PropertyTypeAssignment(
        code="TENSILE_TEST_CASTING_SPEED",
        data_type="VARCHAR",
        property_label="Casting speed",
        description="""Casting speed (Metadata → Material History and Condition → As-manufactured material) // Casting speed""",
        mandatory=False,
        section="As-manufactured material",
    )
    tensile_test_solidification = PropertyTypeAssignment(
        code="TENSILE_TEST_SOLIDIFICATION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_SOLIDIFICATION",
        property_label="Solidification Description: Single/Polycrystal solidified?",
        description="""Solidification Description: Single/Polycrystal solidified? (Metadata → Material History and Condition → As-manufactured material) // Solidification Description: Single/Polycrystal solidified?""",
        mandatory=True,
        section="As-manufactured material",
    )
    tensile_test_condition = PropertyTypeAssignment(
        code="TENSILE_TEST_CONDITION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_CONDITION",
        property_label="Condition",
        description="""Condition (Metadata → Material History and Condition → As-manufactured material) // Condition""",
        mandatory=True,
        section="As-manufactured material",
    )
    tensile_test_supplier = PropertyTypeAssignment(
        code="TENSILE_TEST_SUPPLIER",
        data_type="VARCHAR",
        property_label="Supplier",
        description="""Supplier (Metadata → Material History and Condition → As-tested material) // Supplier""",
        mandatory=True,
        section="As-tested material",
    )
    tensile_test_geometry_size_as_tested_material = PropertyTypeAssignment(
        code="TENSILE_TEST_GEOMETRY_SIZE_AS_TESTED_MATERIAL",
        data_type="MULTILINE_VARCHAR",
        property_label="Geometry/size as-tested material Description: The test piece is manufactured from the as-tested material. Please add a description or a link to Image or technical drawing. The as-tested material is the material to be tested. The as-tested material can be a component.",
        description="""Geometry/size as-tested material Description: The test piece is manufactured from the as-tested material. Please add a description or a link to Image or technical drawing. The as-tested material is the material to be tested. The as-tested material can be a component. (Metadata → Material History and Condition → As-tested material) // Geometry/size as-tested material Description: The test piece is manufactured from the as-tested material. Please add a description or a link to Image or technical drawing. The as-tested material is the material to be tested. The as-tested material can be a component.""",
        mandatory=True,
        section="As-tested material",
    )
    tensile_test_manufacturing_process_details = PropertyTypeAssignment(
        code="TENSILE_TEST_MANUFACTURING_PROCESS_DETAILS",
        data_type="MULTILINE_VARCHAR",
        property_label="Manufacturing process description as-tested material",
        description="""Manufacturing process description as-tested material (Metadata → Material History and Condition → As-tested material) // Manufacturing process description as-tested material""",
        mandatory=True,
        section="As-tested material",
    )
    tensile_test_supply_date = PropertyTypeAssignment(
        code="TENSILE_TEST_SUPPLY_DATE",
        data_type="DATE",
        property_label="Supply Date",
        description="""Supply Date (Metadata → Material History and Condition → As-tested material) // Supply Date""",
        mandatory=True,
        section="As-tested material",
    )
    tensile_test_order_number = PropertyTypeAssignment(
        code="TENSILE_TEST_ORDER_NUMBER",
        data_type="VARCHAR",
        property_label="Order number",
        description="""Order number (Metadata → Material History and Condition → As-tested material) // Order number""",
        mandatory=False,
        section="As-tested material",
    )
    tensile_test_heat_treatment_state = PropertyTypeAssignment(
        code="TENSILE_TEST_HEAT_TREATMENT_STATE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_HEAT_TREATMENT_STATE",
        property_label="Heat treatment - State",
        description="""Heat treatment - State (Metadata → Material History and Condition → Heat treatment) // Heat treatment - State""",
        mandatory=True,
        section="Heat treatment",
    )
    tensile_test_multistage_annealing = PropertyTypeAssignment(
        code="TENSILE_TEST_MULTISTAGE_ANNEALING",
        data_type="BOOLEAN",
        property_label="Multistage annealing?",
        description="""Multistage annealing? (Metadata → Material History and Condition → Heat treatment) // Multistage annealing?""",
        mandatory=False,
        section="Heat treatment",
    )
    tensile_test_multistage_ageing = PropertyTypeAssignment(
        code="TENSILE_TEST_MULTISTAGE_AGEING",
        data_type="BOOLEAN",
        property_label="Multistage ageing?",
        description="""Multistage ageing? (Metadata → Material History and Condition → Heat treatment) // Multistage ageing?""",
        mandatory=False,
        section="Heat treatment",
    )
    tensile_test_heat_treatment_annealing = PropertyTypeAssignment(
        code="TENSILE_TEST_HEAT_TREATMENT_ANNEALING",
        data_type="MULTILINE_VARCHAR",
        property_label="Heat treatment - Annealing - Description",
        description="""Heat treatment - Annealing - Description (Metadata → Material History and Condition → Heat treatment) // Heat treatment - Annealing - Description""",
        mandatory=True,
        section="Heat treatment",
    )
    tensile_test_heat_treatment_ageing = PropertyTypeAssignment(
        code="TENSILE_TEST_HEAT_TREATMENT_AGEING",
        data_type="MULTILINE_VARCHAR",
        property_label="Heat treatment - Ageing - Description",
        description="""Heat treatment - Ageing - Description (Metadata → Material History and Condition → Heat treatment) // Heat treatment - Ageing - Description""",
        mandatory=True,
        section="Heat treatment",
    )
    tensile_test_heat_treatment_protocol = PropertyTypeAssignment(
        code="TENSILE_TEST_HEAT_TREATMENT_PROTOCOL",
        data_type="MULTILINE_VARCHAR",
        property_label="Heat treatment - Protocol Description: Link to file, preferably with machine-readable (meta)data",
        description="""Heat treatment - Protocol Description: Link to file, preferably with machine-readable (meta)data (Metadata → Material History and Condition → Heat treatment) // Heat treatment - Protocol Description: Link to file, preferably with machine-readable (meta)data""",
        mandatory=False,
        section="Heat treatment",
    )
    tensile_test_microstructure_feature = PropertyTypeAssignment(
        code="TENSILE_TEST_MICROSTRUCTURE_FEATURE",
        data_type="VARCHAR",
        property_label="Microstructure feature",
        description="""Microstructure feature (Metadata → Material History and Condition → Microstructure) // Microstructure feature""",
        mandatory=True,
        section="Microstructure",
        ontology_IRI="https://w3id.org/pmd/co/PMD_0000857",
    )
    tensile_test_characterization_method = PropertyTypeAssignment(
        code="TENSILE_TEST_CHARACTERIZATION_METHOD",
        data_type="MULTILINE_VARCHAR",
        property_label="Characterization method  Description: e.g., STEM, HRTEM, TEM-EDX, AFM, SEM, SEM-EBSD, …",
        description="""Characterization method  Description: e.g., STEM, HRTEM, TEM-EDX, AFM, SEM, SEM-EBSD, … (Metadata → Material History and Condition → Microstructure) // Characterization method  Description: e.g., STEM, HRTEM, TEM-EDX, AFM, SEM, SEM-EBSD, …""",
        mandatory=True,
        section="Microstructure",
    )
    tensile_test_measured_condition = PropertyTypeAssignment(
        code="TENSILE_TEST_MEASURED_CONDITION",
        data_type="MULTILINE_VARCHAR",
        property_label="Measured condition Description: e.g., as-manufactured, heat-treated, before testing, after testing",
        description="""Measured condition Description: e.g., as-manufactured, heat-treated, before testing, after testing (Metadata → Material History and Condition → Microstructure) // Measured condition Description: e.g., as-manufactured, heat-treated, before testing, after testing""",
        mandatory=True,
        section="Microstructure",
    )
    tensile_test_measuring_position = PropertyTypeAssignment(
        code="TENSILE_TEST_MEASURING_POSITION",
        data_type="MULTILINE_VARCHAR",
        property_label="Measuring position Description: Specify position(s) for bulk (middle/top/bottom/surface) and/or microstructure feature (matrix, interdendtitic region, phase,...)",
        description="""Measuring position Description: Specify position(s) for bulk (middle/top/bottom/surface) and/or microstructure feature (matrix, interdendtitic region, phase,...) (Metadata → Material History and Condition → Microstructure) // Measuring position Description: Specify position(s) for bulk (middle/top/bottom/surface) and/or microstructure feature (matrix, interdendtitic region, phase,...)""",
        mandatory=True,
        section="Microstructure",
    )
    tensile_test_microstructure_feature_information = PropertyTypeAssignment(
        code="TENSILE_TEST_MICROSTRUCTURE_FEATURE_INFORMATION",
        data_type="MULTILINE_VARCHAR",
        property_label="Microstructure feature - Information Description: Include all relevant characterization results",
        description="""Microstructure feature - Information Description: Include all relevant characterization results (Matadata → Material History and Condition → Microstructure) // Microstructure feature - Information Description: Include all relevant characterization results""",
        mandatory=False,
        section="Microstructure",
    )
    tensile_test_microstructure_image = PropertyTypeAssignment(
        code="TENSILE_TEST_MICROSTRUCTURE_IMAGE",
        data_type="MULTILINE_VARCHAR",
        property_label="Microstructure Image Description: Link to File, e.g., an optical micrograph, preferably wiht machine-readable (meta)data",
        description="""Microstructure Image Description: Link to File, e.g., an optical micrograph, preferably wiht machine-readable (meta)data (Matadata → Material History and Condition → Microstructure) // Microstructure Image Description: Link to File, e.g., an optical micrograph, preferably wiht machine-readable (meta)data""",
        mandatory=False,
        section="Microstructure",
    )
    tensile_test_microstructure_report = PropertyTypeAssignment(
        code="TENSILE_TEST_MICROSTRUCTURE_REPORT",
        data_type="MULTILINE_VARCHAR",
        property_label="Microstructure report Description: Link to file, preferably with machine-readable (neta) data",
        description="""Microstructure report Description: Link to file, preferably with machine-readable (neta) data (Metadata → Material History and Condition → Microstructure) // Microstructure report Description: Link to file, preferably with machine-readable (neta) data""",
        mandatory=False,
        section="Microstructure",
    )
    tensile_test_grain_size = PropertyTypeAssignment(
        code="TENSILE_TEST_GRAIN_SIZE",
        data_type="MULTILINE_VARCHAR",
        property_label="Grain size Description: if polycrystal",
        description="""Grain size Description: if polycrystal (Metadata → Material History and Condition → Microstructure) // Grain size Description: if polycrystal""",
        mandatory=True,
        section="Microstructure",
        ontology_IRI="https://w3id.org/pmd/co/PMD_0020243",
    )
    tensile_test_grain_size_determination_method = PropertyTypeAssignment(
        code="TENSILE_TEST_GRAIN_SIZE_DETERMINATION_METHOD",
        data_type="VARCHAR",
        property_label="Grain size - Determination method",
        description="""Grain size - Determination method (Metadata → Material History and Condition → Microstructure) // Grain size - Determination method""",
        mandatory=True,
        section="Microstructure",
    )
    tensile_test_grain_size_measuring_region = PropertyTypeAssignment(
        code="TENSILE_TEST_GRAIN_SIZE_MEASURING_REGION",
        data_type="MULTILINE_VARCHAR",
        property_label="Grain size - measuring region Description: E.g., in the bulk",
        description="""Grain size - measuring region Description: E.g., in the bulk (Metadata → Material History and Condition → Microstructure) // Grain size - measuring region Description: E.g., in the bulk""",
        mandatory=True,
        section="Microstructure",
    )
    tensile_test_grain_size_distribution = PropertyTypeAssignment(
        code="TENSILE_TEST_GRAIN_SIZE_DISTRIBUTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Grain size distribution Description: Link to file, preferably with machine-readable (meta)data",
        description="""Grain size distribution Description: Link to file, preferably with machine-readable (meta)data (Metadata → Material History and Condition → Microstructure) // Grain size distribution Description: Link to file, preferably with machine-readable (meta)data""",
        mandatory=False,
        section="Microstructure",
        ontology_IRI="https://w3id.org/pmd/co/PMD_0020112",
    )
    tensile_test_grain_additional_information = PropertyTypeAssignment(
        code="TENSILE_TEST_GRAIN_ADDITIONAL_INFORMATION",
        data_type="MULTILINE_VARCHAR",
        property_label="Grain - Additional Information Description: Include all further relevant characterization results",
        description="""Grain - Additional Information Description: Include all further relevant characterization results (Metadata → Material History and Condition → Microstructure) // Grain - Additional Information Description: Include all further relevant characterization results""",
        mandatory=False,
        section="Microstructure",
    )
    tensile_test_reprecipitated_gamma_gamma_prime_regions = PropertyTypeAssignment(
        code="TENSILE_TEST_REPRECIPITATED_GAMMA_GAMMA_PRIME_REGIONS",
        data_type="MULTILINE_VARCHAR",
        property_label="Reprecipitated gamma-gamma prime regions Description: Completely dissolved and re-precipitated gamma-gamma' regions",
        description="""Reprecipitated gamma-gamma prime regions Description: Completely dissolved and re-precipitated gamma-gamma' regions (Metadata → Material History and Condition → Microstructure) // Reprecipitated gamma-gamma prime regions Description: Completely dissolved and re-precipitated gamma-gamma' regions""",
        mandatory=False,
        section="Microstructure",
    )
    tensile_test_gamma_prime_particles_average_size = PropertyTypeAssignment(
        code="TENSILE_TEST_GAMMA_PRIME_PARTICLES_AVERAGE_SIZE",
        data_type="MULTILINE_VARCHAR",
        property_label="Gamma prime particles - average size",
        description="""Gamma prime particles - average size (Metadata → Material History and Condition → Microstructure) // Gamma prime particles - average size""",
        mandatory=False,
        section="Microstructure",
    )
    tensile_test_gamma_prime_particles_maximum_size = PropertyTypeAssignment(
        code="TENSILE_TEST_GAMMA_PRIME_PARTICLES_MAXIMUM_SIZE",
        data_type="MULTILINE_VARCHAR",
        property_label="Gamma prime particles - maximum size",
        description="""Gamma prime particles - maximum size (Metadata → Material History and Condition → Microstructure) // Gamma prime particles - maximum size""",
        mandatory=False,
        section="Microstructure",
    )
    tensile_test_dendrite_spacings = PropertyTypeAssignment(
        code="TENSILE_TEST_DENDRITE_SPACINGS",
        data_type="MULTILINE_VARCHAR",
        property_label="Dendrite spacings Description: Please describe the procedure and add  a link to file, preferably with machine-readable (meta)data, or add a reference to paper and section",
        description="""Dendrite spacings Description: Please describe the procedure and add  a link to file, preferably with machine-readable (meta)data, or add a reference to paper and section (Metadata → Material History and Condition → Microstructure) // Dendrite spacings Description: Please describe the procedure and add  a link to file, preferably with machine-readable (meta)data, or add a reference to paper and section""",
        mandatory=False,
        section="Microstructure",
    )
    tensile_test_proof_of_single_crystallinity = PropertyTypeAssignment(
        code="TENSILE_TEST_PROOF_OF_SINGLE_CRYSTALLINITY",
        data_type="MULTILINE_VARCHAR",
        property_label="Proof of single crystallinity Description: Link to file, preferably with machine-readable (meta)data",
        description="""Proof of single crystallinity Description: Link to file, preferably with machine-readable (meta)data (Metadata → Material History and Condition → Microstructure) // Proof of single crystallinity Description: Link to file, preferably with machine-readable (meta)data""",
        mandatory=False,
        section="Microstructure",
    )
    tensile_test_single_crystal_orientation = PropertyTypeAssignment(
        code="TENSILE_TEST_SINGLE_CRYSTAL_ORIENTATION",
        data_type="MULTILINE_VARCHAR",
        property_label="Single crystal orientation Description: Link to file, preferably with machine-readable (meta)data. Laue Crystal Verification. Must be documented for each test piece.",
        description="""Single crystal orientation Description: Link to file, preferably with machine-readable (meta)data. Laue Crystal Verification. Must be documented for each test piece. (Metadata → Material History and Condition → Microstructure) // Single crystal orientation Description: Link to file, preferably with machine-readable (meta)data. Laue Crystal Verification. Must be documented for each test piece.""",
        mandatory=True,
        section="Microstructure",
    )
    tensile_test_single_crystal_orientation_determination_method = PropertyTypeAssignment(
        code="TENSILE_TEST_SINGLE_CRYSTAL_ORIENTATION_DETERMINATION_METHOD",
        data_type="MULTILINE_VARCHAR",
        property_label="Single crystal orientation - Determination method",
        description="""Single crystal orientation - Determination method (Metadata → Material History and Condition → Microstructure) // Single crystal orientation - Determination method""",
        mandatory=True,
        section="Microstructure",
    )
    tensile_test_single_crystal_orientation_measuring_point = PropertyTypeAssignment(
        code="TENSILE_TEST_SINGLE_CRYSTAL_ORIENTATION_MEASURING_POINT",
        data_type="MULTILINE_VARCHAR",
        property_label="Single crystal orientation - Measuring point",
        description="""Single crystal orientation - Measuring point (Metadata → Material History and Condition → Microstructure) // Single crystal orientation - Measuring point""",
        mandatory=True,
        section="Microstructure",
    )
    tensile_test_orientation_determination_accuracy = PropertyTypeAssignment(
        code="TENSILE_TEST_ORIENTATION_DETERMINATION_ACCURACY",
        data_type="MULTILINE_VARCHAR",
        property_label="Orientation - Determination accuracy",
        description="""Orientation - Determination accuracy (Metadata → Material History and Condition → Microstructure) // Orientation - Determination accuracy""",
        mandatory=False,
        section="Microstructure",
    )
    tensile_test_measured_condition_value = PropertyTypeAssignment(
        code="TENSILE_TEST_MEASURED_CONDITION_VALUE",
        data_type="VARCHAR",
        property_label="Measured condition",
        description="""Measured condition (Metadata → Material History and Condition → Chemical composition) // Measured condition""",
        mandatory=True,
        section="Chemical composition",
    )
    tensile_test_chemical_composition_nominal = PropertyTypeAssignment(
        code="TENSILE_TEST_CHEMICAL_COMPOSITION_NOMINAL",
        data_type="MULTILINE_VARCHAR",
        property_label="Chemical composition - nominal Description:  Link to file, preferably with machine-readable (meta)data  or add the wt.-% value for each element",
        description="""Chemical composition - nominal Description:  Link to file, preferably with machine-readable (meta)data  or add the wt.-% value for each element (Metadata → Material History and Condition → Chemical composition) // Chemical composition - nominal Description:  Link to file, preferably with machine-readable (meta)data  or add the wt.-% value for each element""",
        mandatory=True,
        section="Chemical composition",
        ontology_IRI="https://w3id.org/pmd/co/PMD_0025002",
    )
    tensile_test_chemical_composition_measured = PropertyTypeAssignment(
        code="TENSILE_TEST_CHEMICAL_COMPOSITION_MEASURED",
        data_type="MULTILINE_VARCHAR",
        property_label="Chemical composition - measured Description: include precision, if available. Link to file, preferably with machine-readable (meta)data  or add the wt.-% value for each element",
        description="""Chemical composition - measured Description: include precision, if available. Link to file, preferably with machine-readable (meta)data  or add the wt.-% value for each element (Metadata → Material History and Condition → Chemical composition) // Chemical composition - measured Description: include precision, if available. Link to file, preferably with machine-readable (meta)data  or add the wt.-% value for each element""",
        mandatory=True,
        section="Chemical composition",
        ontology_IRI="https://w3id.org/pmd/co/PMD_0025002",
    )
    tensile_test_measurement_method = PropertyTypeAssignment(
        code="TENSILE_TEST_MEASUREMENT_METHOD",
        data_type="MULTILINE_VARCHAR",
        property_label="Measurement method Description: Provide a descsription of the used method(s) and details about measurement volume/points",
        description="""Measurement method Description: Provide a descsription of the used method(s) and details about measurement volume/points (Metadata → Material History and Condition → Chemical composition) // Measurement method Description: Provide a descsription of the used method(s) and details about measurement volume/points""",
        mandatory=True,
        section="Chemical composition",
    )
    tensile_test_crack_or_defect_inspection_method = PropertyTypeAssignment(
        code="TENSILE_TEST_CRACK_OR_DEFECT_INSPECTION_METHOD",
        data_type="MULTILINE_VARCHAR",
        property_label="Crack or defect inspection - Method Description: e.g., Penetrant certification/Radiographic certification/XCT/X-Ray film. Link to file, preferably with machine-readable (meta)data",
        description="""Crack or defect inspection - Method Description: e.g., Penetrant certification/Radiographic certification/XCT/X-Ray film. Link to file, preferably with machine-readable (meta)data (Metadata → Material History and Condition → NDT Results) // Crack or defect inspection - Method Description: e.g., Penetrant certification/Radiographic certification/XCT/X-Ray film. Link to file, preferably with machine-readable (meta)data""",
        mandatory=False,
        section="NDT Results",
    )
    tensile_test_crack_or_defect_inspection_result = PropertyTypeAssignment(
        code="TENSILE_TEST_CRACK_OR_DEFECT_INSPECTION_RESULT",
        data_type="VARCHAR",
        property_label="Crack or defect inspection - Result",
        description="""Crack or defect inspection - Result (Metadata → Material History and Condition → NDT Results) // Crack or defect inspection - Result""",
        mandatory=False,
        section="NDT Results",
    )
    tensile_test_proof_strength_room_temperature = PropertyTypeAssignment(
        code="TENSILE_TEST_PROOF_STRENGTH_ROOM_TEMPERATURE",
        data_type="BOOLEAN",
        property_label="Proof strength - room temperature Description: 0.2 % Proof strength at room temperature",
        description="""Proof strength - room temperature Description: 0.2 % Proof strength at room temperature (Metadata → Material History and Condition → Mechanical Tests Results) // Proof strength - room temperature Description: 0.2 % Proof strength at room temperature""",
        mandatory=False,
        section="Mechanical Tests Results",
    )
    tensile_test_hardness = PropertyTypeAssignment(
        code="TENSILE_TEST_HARDNESS",
        data_type="VARCHAR",
        property_label="Hardness",
        description="""Hardness (Metadata → Material History and Condition → Mechanical Tests Results) // Hardness""",
        mandatory=False,
        section="Mechanical Tests Results",
        ontology_IRI="https://w3id.org/pmd/co/PMD_0000773",
    )

class TensileTestPrimaryValuesRecordedAfterEndOfTest(ObjectType):
    defs = ObjectTypeDef(
        code="TENSILE_TEST_PRIMARY_VALUES_RECORDED_AFTER_END_OF_TEST",
        description="""Tensile-test data object: TensileTestPrimaryValuesRecordedAfterEndOfTest // Datenobjekt fuer den Zugversuch: TensileTestPrimaryValuesRecordedAfterEndOfTest""",
        generated_code_prefix="TENSILE_PRIMA_VALUE",
    )
    tensile_test_fracture_position = PropertyTypeAssignment(
        code="TENSILE_TEST_FRACTURE_POSITION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_FRACTURE_POSITION",
        property_label="Fracture position",
        description="""Fracture position (Primary data → Test result → Values recorded after end of test) // Fracture position""",
        mandatory=True,
        section="Values recorded after end of test",
    )
    tensile_test_final_gauge_length_after_fracture = PropertyTypeAssignment(
        code="TENSILE_TEST_FINAL_GAUGE_LENGTH_AFTER_FRACTURE",
        data_type="REAL",
        property_label="Final gauge length after fracture",
        description="""Final gauge length after fracture (Primary data → Test result → Values recorded after end of test) // Final gauge length after fracture""",
        mandatory=True,
        section="Values recorded after end of test",
        ontology_IRI="https://w3id.org/pmd/tto/TTO_0000018",
    )

class TensileTestPrimaryValuesRecordedAtTestStart(ObjectType):
    defs = ObjectTypeDef(
        code="TENSILE_TEST_PRIMARY_VALUES_RECORDED_AT_TEST_START",
        description="""Tensile-test data object: TensileTestPrimaryValuesRecordedAtTestStart // Datenobjekt fuer den Zugversuch: TensileTestPrimaryValuesRecordedAtTestStart""",
        generated_code_prefix="TENSILE_PRIMA_VALUE",
    )
    tensile_test_original_thickness_of_a_flat_test_piece = PropertyTypeAssignment(
        code="TENSILE_TEST_ORIGINAL_THICKNESS_OF_A_FLAT_TEST_PIECE",
        data_type="REAL",
        property_label="Original thickness of a flat test piece",
        description="""Original thickness of a flat test piece (Primary data → Test result → Values recorded at test start) // Original thickness of a flat test piece""",
        mandatory=True,
        section="Values recorded at test start",
        ontology_IRI="https://w3id.org/pmd/tto/TTO_0000029",
    )
    tensile_test_original_width_of_the_parallel_length_of_a_flat_test_piece = PropertyTypeAssignment(
        code="TENSILE_TEST_ORIGINAL_WIDTH_OF_THE_PARALLEL_LENGTH_OF_A_FLAT_TEST_PIECE",
        data_type="REAL",
        property_label="Original width of the parallel length of a flat test piece",
        description="""Original width of the parallel length of a flat test piece (Primary data → Test result → Values recorded at test start) // Original width of the parallel length of a flat test piece""",
        mandatory=True,
        section="Values recorded at test start",
        ontology_IRI="https://w3id.org/pmd/tto/TTO_0000030",
    )
    tensile_test_original_gauge_length = PropertyTypeAssignment(
        code="TENSILE_TEST_ORIGINAL_GAUGE_LENGTH",
        data_type="REAL",
        property_label="Original gauge length",
        units="mm",
        description="""Original gauge length (Primary data → Test result → Values recorded at test start) // Original gauge length""",
        mandatory=True,
        section="Values recorded at test start",
        ontology_IRI="https://w3id.org/pmd/tto/TTO_0000028",
    )
    tensile_test_parallel_length = PropertyTypeAssignment(
        code="TENSILE_TEST_PARALLEL_LENGTH",
        data_type="REAL",
        property_label="Parallel length",
        units="mm",
        description="""Parallel length (Primary data → Test result → Values recorded at test start) // Parallel length""",
        mandatory=True,
        section="Values recorded at test start",
        ontology_IRI="https://w3id.org/pmd/tto/TTO_0000031",
    )
    tensile_test_extensometer_gauge_length = PropertyTypeAssignment(
        code="TENSILE_TEST_EXTENSOMETER_GAUGE_LENGTH",
        data_type="REAL",
        property_label="Extensometer gauge length",
        units="mm",
        description="""Extensometer gauge length (Primary data → Test result → Values recorded at test start) // Extensometer gauge length""",
        mandatory=True,
        section="Values recorded at test start",
        ontology_IRI="https://w3id.org/pmd/tto/TTO_0000017",
    )

class TensileTestPrimaryValuesRecordedDuringTestRun(ObjectType):
    defs = ObjectTypeDef(
        code="TENSILE_TEST_PRIMARY_VALUES_RECORDED_DURING_TEST_RUN",
        description="""Tensile-test data object: TensileTestPrimaryValuesRecordedDuringTestRun // Datenobjekt fuer den Zugversuch: TensileTestPrimaryValuesRecordedDuringTestRun""",
        generated_code_prefix="TENSILE_PRIMA_VALUE",
    )
    tensile_test_force = PropertyTypeAssignment(
        code="TENSILE_TEST_FORCE",
        data_type="MULTILINE_VARCHAR",
        property_label="Force Description: Link to file, preferably with machine-readable (meta)data",
        units="kN",
        description="""Force Description: Link to file, preferably with machine-readable (meta)data (Primary data → Test result → Values recorded during test run) // Force Description: Link to file, preferably with machine-readable (meta)data""",
        mandatory=True,
        section="Values recorded during test run",
        ontology_IRI="https://w3id.org/pmd/co/PMD_0020200",
    )
    tensile_test_time = PropertyTypeAssignment(
        code="TENSILE_TEST_TIME",
        data_type="MULTILINE_VARCHAR",
        property_label="Time Description: Link to file, preferably with machine-readable (meta)data",
        units="s",
        description="""Time Description: Link to file, preferably with machine-readable (meta)data (Primary data → Test result → Values recorded during test run) // Time Description: Link to file, preferably with machine-readable (meta)data""",
        mandatory=True,
        section="Values recorded during test run",
    )
    tensile_test_crosshead_displacement = PropertyTypeAssignment(
        code="TENSILE_TEST_CROSSHEAD_DISPLACEMENT",
        data_type="MULTILINE_VARCHAR",
        property_label="Crosshead displacement Description: Link to file, preferably with machine-readable (meta)data",
        description="""Crosshead displacement Description: Link to file, preferably with machine-readable (meta)data (Primary data → Test result → Values recorded during test run) // Crosshead displacement Description: Link to file, preferably with machine-readable (meta)data""",
        mandatory=False,
        section="Values recorded during test run",
        ontology_IRI="https://w3id.org/pmd/tto/TTO_0000013",
    )

class TensileTestSecondaryElongationValues(ObjectType):
    defs = ObjectTypeDef(
        code="TENSILE_TEST_SECONDARY_ELONGATION_VALUES",
        description="""Tensile-test data object: TensileTestSecondaryElongationValues // Datenobjekt fuer den Zugversuch: TensileTestSecondaryElongationValues""",
        generated_code_prefix="TENSILE_SECON_ELONG",
    )
    tensile_test_percentage_elongation_after_fracture = PropertyTypeAssignment(
        code="TENSILE_TEST_PERCENTAGE_ELONGATION_AFTER_FRACTURE",
        data_type="REAL",
        property_label="Percentage elongation after fracture",
        units="%",
        description="""Percentage elongation after fracture (Secondary data → Test result → Elongation values) // Percentage elongation after fracture""",
        mandatory=True,
        section="Elongation values",
        ontology_IRI="https://w3id.org/pmd/tto/TTO_0000033",
    )

class TensileTestSecondaryExtensionValues(ObjectType):
    defs = ObjectTypeDef(
        code="TENSILE_TEST_SECONDARY_EXTENSION_VALUES",
        description="""Tensile-test data object: TensileTestSecondaryExtensionValues // Datenobjekt fuer den Zugversuch: TensileTestSecondaryExtensionValues""",
        generated_code_prefix="TENSILE_SECON_EXTEN",
    )
    tensile_test_extensometer_removal = PropertyTypeAssignment(
        code="TENSILE_TEST_EXTENSOMETER_REMOVAL",
        data_type="MULTILINE_VARCHAR",
        property_label="Extensometer removal Description: Extension value at the point of extensometer removal, if applicable",
        units="%/mm/-",
        description="""Extensometer removal Description: Extension value at the point of extensometer removal, if applicable (Secondary data → Test result → Extension values) // Extensometer removal Description: Extension value at the point of extensometer removal, if applicable""",
        mandatory=True,
        section="Extension values",
    )

class TensileTestSecondaryStrengthValues(ObjectType):
    defs = ObjectTypeDef(
        code="TENSILE_TEST_SECONDARY_STRENGTH_VALUES",
        description="""Tensile-test data object: TensileTestSecondaryStrengthValues // Datenobjekt fuer den Zugversuch: TensileTestSecondaryStrengthValues""",
        generated_code_prefix="TENSILE_SECON_STREN",
    )
    tensile_test_upper_yield_strength = PropertyTypeAssignment(
        code="TENSILE_TEST_UPPER_YIELD_STRENGTH",
        data_type="MULTILINE_VARCHAR",
        property_label="Upper yield strength Description: if applicable",
        units="MPa",
        description="""Upper yield strength Description: if applicable (Secondary data → Test result → Strength values) // Upper yield strength Description: if applicable""",
        mandatory=True,
        section="Strength values",
        ontology_IRI="https://w3id.org/pmd/tto/TTO_0000059",
    )
    tensile_test_lower_yield_strength = PropertyTypeAssignment(
        code="TENSILE_TEST_LOWER_YIELD_STRENGTH",
        data_type="MULTILINE_VARCHAR",
        property_label="Lower yield strength Description: if applicable",
        units="MPa",
        description="""Lower yield strength Description: if applicable (Secondary data → Test result → Strength values) // Lower yield strength Description: if applicable""",
        mandatory=True,
        section="Strength values",
        ontology_IRI="https://w3id.org/pmd/tto/TTO_0000022",
    )
    tensile_test_percentage_yield_point_extension = PropertyTypeAssignment(
        code="TENSILE_TEST_PERCENTAGE_YIELD_POINT_EXTENSION",
        data_type="MULTILINE_VARCHAR",
        property_label="Percentage yield point extension Description: if applicable",
        units="%",
        description="""Percentage yield point extension Description: if applicable (Secondary data → Test result → Strength values) // Percentage yield point extension Description: if applicable""",
        mandatory=True,
        section="Strength values",
        ontology_IRI="https://w3id.org/pmd/tto/TTO_0000041",
    )

class TensileTestSecondaryValuesRecordedDuringTestRun(ObjectType):
    defs = ObjectTypeDef(
        code="TENSILE_TEST_SECONDARY_VALUES_RECORDED_DURING_TEST_RUN",
        description="""Tensile-test data object: TensileTestSecondaryValuesRecordedDuringTestRun // Datenobjekt fuer den Zugversuch: TensileTestSecondaryValuesRecordedDuringTestRun""",
        generated_code_prefix="TENSILE_SECON_VALUE",
    )
    tensile_test_indicated_temperature = PropertyTypeAssignment(
        code="TENSILE_TEST_INDICATED_TEMPERATURE",
        data_type="MULTILINE_VARCHAR",
        property_label="Indicated temperature Description: Link to file, preferably with machine-readable (meta)data",
        description="""Indicated temperature Description: Link to file, preferably with machine-readable (meta)data (Secondary data → Test result → Values recorded during test run) // Indicated temperature Description: Link to file, preferably with machine-readable (meta)data""",
        mandatory=False,
        section="Values recorded during test run",
        ontology_IRI="https://w3id.org/pmd/co/PMD_0000967",
    )
    tensile_test_stress = PropertyTypeAssignment(
        code="TENSILE_TEST_STRESS",
        data_type="MULTILINE_VARCHAR",
        property_label="Stress Description: Link to file, preferably with machine-readable (meta)data",
        units="MPa",
        description="""Stress Description: Link to file, preferably with machine-readable (meta)data (Secondary data → Test result → Values recorded during test run) // Stress Description: Link to file, preferably with machine-readable (meta)data""",
        mandatory=True,
        section="Values recorded during test run",
    )
    tensile_test_percentage_extension = PropertyTypeAssignment(
        code="TENSILE_TEST_PERCENTAGE_EXTENSION",
        data_type="MULTILINE_VARCHAR",
        property_label="Percentage extension Description: Link to File, preferably with machine-readable (meta)data.",
        units="%/-",
        description="""Percentage extension Description: Link to File, preferably with machine-readable (meta)data. (Secondary data → Test result → Values recorded during test run) // Percentage extension Description: Link to File, preferably with machine-readable (meta)data.""",
        mandatory=True,
        section="Values recorded during test run",
        ontology_IRI="https://w3id.org/pmd/tto/TTO_0000034",
    )

class TensileTestTemperatureDataAcquisition(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.TENSILE_TEST_TEMPERATURE_DATA_ACQUISITION",
        description="""Tensile-test data object: TensileTestTemperatureDataAcquisition // Datenobjekt fuer den Zugversuch: TensileTestTemperatureDataAcquisition""",
        generated_code_prefix="INS.TENSILE_TEMPE_DATA",
    )
    tensile_test_calibration_status = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_STATUS",
        data_type="BOOLEAN",
        property_label="Calibration status Description: Is/are the data acquisition unit calibrated?",
        description="""Calibration status Description: Is/are the data acquisition unit calibrated? (Metadata → Measuring and test equipment → Temperature-measuring system → Data acquisition) // Calibration status Description: Is/are the data acquisition unit calibrated?""",
        mandatory=True,
        section="Data acquisition",
    )
    tensile_test_reference_junction = PropertyTypeAssignment(
        code="TENSILE_TEST_REFERENCE_JUNCTION",
        data_type="VARCHAR",
        property_label="Reference junction",
        description="""Reference junction (Metadata → Measuring and test equipment → Temperature-measuring system → Data acquisition) // Reference junction""",
        mandatory=False,
        section="Data acquisition",
    )
    tensile_test_calibration_certificate = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_CERTIFICATE",
        data_type="MULTILINE_VARCHAR",
        property_label="Calibration certificate Description: Link to File, preferably with machine-readable (meta)data.",
        description="""Calibration certificate Description: Link to File, preferably with machine-readable (meta)data. (Metadata → Measuring and test equipment → Temperature-measuring system → Data acquisition) // Calibration certificate Description: Link to File, preferably with machine-readable (meta)data.""",
        mandatory=False,
        section="Data acquisition",
    )
    tensile_test_calibration_date = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_DATE",
        data_type="DATE",
        property_label="Calibration date",
        description="""Calibration date (Metadata → Measuring and test equipment → Temperature-measuring system → Data acquisition) // Calibration date""",
        mandatory=True,
        section="Data acquisition",
    )
    tensile_test_calibration_validity_time_period = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_VALIDITY_TIME_PERIOD",
        data_type="VARCHAR",
        property_label="Calibration validity time period",
        description="""Calibration validity time period (Metadata → Measuring and test equipment → Temperature-measuring system → Data acquisition) // Calibration validity time period""",
        mandatory=True,
        section="Data acquisition",
    )
    tensile_test_calibration_method = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_METHOD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_THERMOCOUPLE_CALIBRATION_METHOD",
        property_label="Calibration method",
        description="""Calibration method (Metadata → Measuring and test equipment → Temperature-measuring system → Data acquisition) // Calibration method""",
        mandatory=True,
        section="Data acquisition",
    )
    tensile_test_calibration_standard = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_STANDARD",
        data_type="VARCHAR",
        property_label="Calibration standard",
        description="""Calibration standard (Metadata → Measuring and test equipment → Temperature-measuring system → Data acquisition) // Calibration standard""",
        mandatory=True,
        section="Data acquisition",
    )
    tensile_test_temperature_deviation = PropertyTypeAssignment(
        code="TENSILE_TEST_TEMPERATURE_DEVIATION",
        data_type="MULTILINE_VARCHAR",
        property_label="Temperature deviation Description: Temperature deviation from the reference thermostat detected during calibration",
        units="degC",
        description="""Temperature deviation Description: Temperature deviation from the reference thermostat detected during calibration (Metadata → Measuring and test equipment → Temperature-measuring system → Data acquisition) // Temperature deviation Description: Temperature deviation from the reference thermostat detected during calibration""",
        mandatory=False,
        section="Data acquisition",
    )
    tensile_test_calibration_range = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_RANGE",
        data_type="REAL",
        property_label="Calibration Range",
        units="degC",
        description="""Calibration Range (Metadata → Measuring and test equipment → Temperature-measuring system → Data acquisition) // Calibration Range""",
        mandatory=True,
        section="Data acquisition",
        ontology_IRI="https://w3id.org/pmd/co/PMD_0000967",
    )

class TensileTestTemperatureMeasuringSystem(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.TENSILE_TEST_TEMPERATURE_MEASURING_SYSTEM",
        description="""Tensile-test data object: TensileTestTemperatureMeasuringSystem // Datenobjekt fuer den Zugversuch: TensileTestTemperatureMeasuringSystem""",
        generated_code_prefix="INS.TENSILE_TEMPE_MEASU",
    )
    tensile_test_temperature_signal = PropertyTypeAssignment(
        code="TENSILE_TEST_TEMPERATURE_SIGNAL",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_TEMPERATURE_SIGNAL",
        property_label="Temperature signal Description: Which temperature signal was used for temperature control?",
        description="""Temperature signal Description: Which temperature signal was used for temperature control? (Metadata → Measuring and test equipment → Temperature-measuring system) // Temperature signal Description: Which temperature signal was used for temperature control?""",
        mandatory=True,
        section="Temperature-measuring system",
    )
    tensile_test_metrological_traceability = PropertyTypeAssignment(
        code="TENSILE_TEST_METROLOGICAL_TRACEABILITY",
        data_type="BOOLEAN",
        property_label="Metrological traceability Description: Yes, if temperature sensor and data acquisition are calibrated.",
        description="""Metrological traceability Description: Yes, if temperature sensor and data acquisition are calibrated. (Metadata → Measuring and test equipment → Temperature-measuring system) // Metrological traceability Description: Yes, if temperature sensor and data acquisition are calibrated.""",
        mandatory=True,
        section="Temperature-measuring system",
    )
    tensile_test_temperature_correction = PropertyTypeAssignment(
        code="TENSILE_TEST_TEMPERATURE_CORRECTION",
        data_type="BOOLEAN",
        property_label="Temperature correction Description: Is the temperature correction (from the calibration) included in the indicated temperature Ti",
        description="""Temperature correction Description: Is the temperature correction (from the calibration) included in the indicated temperature Ti (Metadata → Measuring and test equipment → Temperature-measuring system) // Temperature correction Description: Is the temperature correction (from the calibration) included in the indicated temperature Ti""",
        mandatory=True,
        section="Temperature-measuring system",
    )
    tensile_test_temperature_deviation = PropertyTypeAssignment(
        code="TENSILE_TEST_TEMPERATURE_DEVIATION",
        data_type="MULTILINE_VARCHAR",
        property_label="Temperature deviation Description: were permitted deviations between Ti and T observed?",
        description="""Temperature deviation Description: were permitted deviations between Ti and T observed? (Metadata → Measuring and test equipment → Temperature-measuring system) // Temperature deviation Description: were permitted deviations between Ti and T observed?""",
        mandatory=True,
        section="Temperature-measuring system",
    )
    tensile_test_temperature_deviation_over_parallel_length = PropertyTypeAssignment(
        code="TENSILE_TEST_TEMPERATURE_DEVIATION_OVER_PARALLEL_LENGTH",
        data_type="BOOLEAN",
        property_label="Temperature deviation over parallel length Description: was the permissible deviation over the entire parallel length of the test piece maintained?",
        description="""Temperature deviation over parallel length Description: was the permissible deviation over the entire parallel length of the test piece maintained? (Metadata → Measuring and test equipment → Temperature-measuring system) // Temperature deviation over parallel length Description: was the permissible deviation over the entire parallel length of the test piece maintained?""",
        mandatory=True,
        section="Temperature-measuring system",
    )

class TensileTestTemperatureSensor(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.TENSILE_TEST_TEMPERATURE_SENSOR",
        description="""Tensile-test data object: TensileTestTemperatureSensor // Datenobjekt fuer den Zugversuch: TensileTestTemperatureSensor""",
        generated_code_prefix="INS.TENSILE_TEMPE_SENSO",
    )
    tensile_test_sensor_type = PropertyTypeAssignment(
        code="TENSILE_TEST_SENSOR_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_TEMPERATURE_SENSOR_TYPE",
        property_label="Sensor type",
        description="""Sensor type (Metadata → Measuring and test equipment → Temperature-measuring system → Temperature sensor) // Sensor type""",
        mandatory=True,
        section="Temperature sensor",
    )
    tensile_test_sensor_id = PropertyTypeAssignment(
        code="TENSILE_TEST_SENSOR_ID",
        data_type="VARCHAR",
        property_label="Sensor ID",
        description="""Sensor ID (Metadata → Measuring and test equipment → Temperature-measuring system → Temperature sensor) // Sensor ID""",
        mandatory=False,
        section="Temperature sensor",
        ontology_IRI="http://purl.obolibrary.org/obo/IAO_0020000",
    )
    tensile_test_thermocouple_type = PropertyTypeAssignment(
        code="TENSILE_TEST_THERMOCOUPLE_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="THERMOCOUPLE_TYPE",
        property_label="Thermocouple type",
        description="""Thermocouple type (Metadata → Measuring and test equipment → Temperature-measuring system → Temperature sensor) // Thermocouple type""",
        mandatory=True,
        section="Temperature sensor",
        ontology_IRI="https://w3id.org/pmd/co/PMD_0000983",
    )
    tensile_test_wire_gauge = PropertyTypeAssignment(
        code="TENSILE_TEST_WIRE_GAUGE",
        data_type="REAL",
        property_label="Wire gauge",
        units="mm",
        description="""Wire gauge (Metadata → Measuring and test equipment → Temperature-measuring system → Temperature sensor) // Wire gauge""",
        mandatory=False,
        section="Temperature sensor",
        ontology_IRI="https://w3id.org/pmd/co/PMD_0050051",
    )
    tensile_test_layout = PropertyTypeAssignment(
        code="TENSILE_TEST_LAYOUT",
        data_type="MULTILINE_VARCHAR",
        property_label="Layout Description: e.g., wire with 2-hole ceramic beads",
        description="""Layout Description: e.g., wire with 2-hole ceramic beads (Metadata → Measuring and test equipment → Temperature-measuring system → Temperature sensor) // Layout Description: e.g., wire with 2-hole ceramic beads""",
        mandatory=False,
        section="Temperature sensor",
    )
    tensile_test_calibration_status = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_STATUS",
        data_type="BOOLEAN",
        property_label="Calibration status Description: Is/are the thermocouples calibrated?",
        description="""Calibration status Description: Is/are the thermocouples calibrated? (Metadata → Measuring and test equipment → Temperature-measuring system → Temperature sensor) // Calibration status Description: Is/are the thermocouples calibrated?""",
        mandatory=True,
        section="Temperature sensor",
    )
    tensile_test_calibration_method = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_METHOD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_THERMOCOUPLE_CALIBRATION_METHOD",
        property_label="Calibration method",
        description="""Calibration method (Metadata → Measuring and test equipment → Temperature-measuring system → Temperature sensor) // Calibration method""",
        mandatory=True,
        section="Temperature sensor",
    )
    tensile_test_calibration_standard = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_STANDARD",
        data_type="VARCHAR",
        property_label="Calibration standard",
        description="""Calibration standard (Metadata → Measuring and test equipment → Temperature-measuring system → Temperature sensor) // Calibration standard""",
        mandatory=True,
        section="Temperature sensor",
    )
    tensile_test_calibration_certificate = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_CERTIFICATE",
        data_type="MULTILINE_VARCHAR",
        property_label="Calibration certificate Description: Link to File, preferably with machine-readable (meta)data.",
        description="""Calibration certificate Description: Link to File, preferably with machine-readable (meta)data. (Metadata → Measuring and test equipment → Temperature-measuring system → Temperature sensor) // Calibration certificate Description: Link to File, preferably with machine-readable (meta)data.""",
        mandatory=False,
        section="Temperature sensor",
    )
    tensile_test_calibration_date = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_DATE",
        data_type="DATE",
        property_label="Calibration date",
        description="""Calibration date (Metadata → Measuring and test equipment → Temperature-measuring system → Temperature sensor) // Calibration date""",
        mandatory=True,
        section="Temperature sensor",
    )
    tensile_test_calibration_validity_time_period = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_VALIDITY_TIME_PERIOD",
        data_type="VARCHAR",
        property_label="Calibration validity time period",
        description="""Calibration validity time period (Metadata → Measuring and test equipment → Temperature-measuring system → Temperature sensor) // Calibration validity time period""",
        mandatory=True,
        section="Temperature sensor",
    )
    tensile_test_temperature_deviation = PropertyTypeAssignment(
        code="TENSILE_TEST_TEMPERATURE_DEVIATION",
        data_type="REAL",
        property_label="Temperature deviation Description: Temperature deviation from the reference thermostat detected during calibration",
        units="K",
        description="""Temperature deviation Description: Temperature deviation from the reference thermostat detected during calibration (Metadata → Measuring and test equipment → Temperature-measuring system → Temperature sensor) // Temperature deviation Description: Temperature deviation from the reference thermostat detected during calibration""",
        mandatory=False,
        section="Temperature sensor",
    )
    tensile_test_calibration_range = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_RANGE",
        data_type="REAL",
        property_label="Calibration Range",
        units="degC",
        description="""Calibration Range (Metadata → Measuring and test equipment → Temperature-measuring system → Temperature sensor) // Calibration Range""",
        mandatory=True,
        section="Temperature sensor",
        ontology_IRI="https://w3id.org/pmd/co/PMD_0000967",
    )
    tensile_test_contact_method = PropertyTypeAssignment(
        code="TENSILE_TEST_CONTACT_METHOD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_THERMOCOUPLE_CONTACT_METHOD",
        property_label="Contact method",
        description="""Contact method (Metadata → Measuring and test equipment → Temperature-measuring system → Temperature sensor) // Contact method""",
        mandatory=True,
        section="Temperature sensor",
    )
    tensile_test_number_of_thermocouples = PropertyTypeAssignment(
        code="TENSILE_TEST_NUMBER_OF_THERMOCOUPLES",
        data_type="INTEGER",
        property_label="Number of thermocouples",
        description="""Number of thermocouples (Metadata → Measuring and test equipment → Temperature-measuring system → Temperature sensor) // Number of thermocouples""",
        mandatory=True,
        section="Temperature sensor",
    )
    tensile_test_thermocouple_location = PropertyTypeAssignment(
        code="TENSILE_TEST_THERMOCOUPLE_LOCATION",
        data_type="MULTILINE_VARCHAR",
        property_label="Thermocouple location Description: location with respect to gauge section",
        description="""Thermocouple location Description: location with respect to gauge section (Metadata → Measuring and test equipment → Temperature-measuring system → Temperature sensor) // Thermocouple location Description: location with respect to gauge section""",
        mandatory=True,
        section="Temperature sensor",
    )

class TensileTestTestMachine(TestingMachine):
    defs = ObjectTypeDef(
        code="TESTING_MACHINE.TENSILE_TEST_MACHINE",
        description="""Tensile-test data object: TensileTestTestMachine // Datenobjekt fuer den Zugversuch: TensileTestTestMachine""",
        generated_code_prefix="TM.TENSILE_MACHI",
    )
    tensile_test_machine_id = PropertyTypeAssignment(
        code="TENSILE_TEST_MACHINE_ID",
        data_type="VARCHAR",
        property_label="Test machine ID",
        description="""Test machine ID (Metadata → Measuring and test equipment → Test machine) // Test machine ID""",
        mandatory=False,
        section="Test machine",
        ontology_IRI="http://purl.obolibrary.org/obo/IAO_0020000",
    )
    tensile_test_machine_type = PropertyTypeAssignment(
        code="TENSILE_TEST_MACHINE_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_MACHINE_TYPE",
        property_label="Test machine type",
        description="""Test machine type (Metadata → Measuring and test equipment → Test machine) // Test machine type""",
        mandatory=False,
        section="Test machine",
        ontology_IRI="https://w3id.org/pmd/co/PMD_0000973",
    )
    tensile_test_minimum_applicable_force = PropertyTypeAssignment(
        code="TENSILE_TEST_MINIMUM_APPLICABLE_FORCE",
        data_type="REAL",
        property_label="Minimum applicable force",
        units="kN",
        description="""Minimum applicable force (Metadata → Measuring and test equipment → Test machine) // Minimum applicable force""",
        mandatory=False,
        section="Test machine",
        ontology_IRI="https://w3id.org/pmd/co/PMD_0020200",
    )
    tensile_test_maximum_applicable_force = PropertyTypeAssignment(
        code="TENSILE_TEST_MAXIMUM_APPLICABLE_FORCE",
        data_type="REAL",
        property_label="Maximum applicable force",
        units="kN",
        description="""Maximum applicable force (Metadata → Measuring and test equipment → Test machine) // Maximum applicable force""",
        mandatory=False,
        section="Test machine",
        ontology_IRI="https://w3id.org/pmd/co/PMD_0020200",
    )
    tensile_test_zeroing_test_force = PropertyTypeAssignment(
        code="TENSILE_TEST_ZEROING_TEST_FORCE",
        data_type="BOOLEAN",
        property_label="Zeroing test force Description: was the force-measuring system set to zero before test piece installation?",
        description="""Zeroing test force Description: was the force-measuring system set to zero before test piece installation? (Metadata → Measuring and test equipment → Test machine) // Zeroing test force Description: was the force-measuring system set to zero before test piece installation?""",
        mandatory=True,
        section="Test machine",
    )
    tensile_test_frame_and_specimen_alignment = PropertyTypeAssignment(
        code="TENSILE_TEST_FRAME_AND_SPECIMEN_ALIGNMENT",
        data_type="MULTILINE_VARCHAR",
        property_label="Test frame and specimen alignment Description: Verification of Test Frame and Specimen Alignment according to ASTM E1012?",
        description="""Test frame and specimen alignment Description: Verification of Test Frame and Specimen Alignment according to ASTM E1012? (Metadata → Measuring and test equipment → Test machine) // Test frame and specimen alignment Description: Verification of Test Frame and Specimen Alignment according to ASTM E1012?""",
        mandatory=True,
        section="Test machine",
    )
    tensile_test_frame_and_specimen_alignment_details = PropertyTypeAssignment(
        code="TENSILE_TEST_FRAME_AND_SPECIMEN_ALIGNMENT_DETAILS",
        data_type="MULTILINE_VARCHAR",
        property_label="Test frame and specimen alignment - description Description: Please provide a description on the procedure followed for the Verification of Test Frame and Specimen Alignment if different from ASTM E1012",
        description="""Test frame and specimen alignment - description Description: Please provide a description on the procedure followed for the Verification of Test Frame and Specimen Alignment if different from ASTM E1012 (Metadata → Measuring and test equipment → Test machine) // Test frame and specimen alignment - description Description: Please provide a description on the procedure followed for the Verification of Test Frame and Specimen Alignment if different from ASTM E1012""",
        mandatory=True,
        section="Test machine",
    )
    tensile_test_calibration_class = PropertyTypeAssignment(
        code="TENSILE_TEST_CALIBRATION_CLASS",
        data_type="MULTILINE_VARCHAR",
        property_label="Calibration class Description: Calibration class of test frame and specimen alignment, e.g., 5 / 5 starting from 3 kN (according to ASTM E1012)",
        description="""Calibration class Description: Calibration class of test frame and specimen alignment, e.g., 5 / 5 starting from 3 kN (according to ASTM E1012) (Metadata → Measuring and test equipment → Test machine) // Calibration class Description: Calibration class of test frame and specimen alignment, e.g., 5 / 5 starting from 3 kN (according to ASTM E1012)""",
        mandatory=True,
        section="Test machine",
    )

class TensileTestTestPiece(Sample):
    defs = ObjectTypeDef(
        code="SAMPLE.TENSILE_TEST_PIECE",
        description="""Tensile-test data object: TensileTestTestPiece // Datenobjekt fuer den Zugversuch: TensileTestTestPiece""",
        generated_code_prefix="SAMPL.TENSILE_PIECE",
    )
    tensile_test_workshop_order_id = PropertyTypeAssignment(
        code="TENSILE_TEST_WORKSHOP_ORDER_ID",
        data_type="VARCHAR",
        property_label="Workshop order ID",
        description="""Workshop order ID (Metadata → Test piece) // Workshop order ID""",
        mandatory=False,
        section="Test piece",
    )
    tensile_test_piece_history = PropertyTypeAssignment(
        code="TENSILE_TEST_PIECE_HISTORY",
        data_type="MULTILINE_VARCHAR",
        property_label="Test piece history Description: Link to file, preferably with machine-readable (meta)data. The file(s) can include, e.g., data or documentation from previous experiments.",
        description="""Test piece history Description: Link to file, preferably with machine-readable (meta)data. The file(s) can include, e.g., data or documentation from previous experiments. (Metadata → Test piece) // Test piece history Description: Link to file, preferably with machine-readable (meta)data. The file(s) can include, e.g., data or documentation from previous experiments.""",
        mandatory=False,
        section="Test piece",
    )
    tensile_test_type_of_test_piece_i = PropertyTypeAssignment(
        code="TENSILE_TEST_TYPE_OF_TEST_PIECE_I",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_TEST_PIECE_TYPE_I",
        property_label="Type of test piece I",
        description="""Type of test piece I (Metadata → Test piece) // Type of test piece I""",
        mandatory=True,
        section="Test piece",
        ontology_IRI="https://w3id.org/pmd/co/PMD_0020193",
    )
    tensile_test_type_of_test_piece_ii = PropertyTypeAssignment(
        code="TENSILE_TEST_TYPE_OF_TEST_PIECE_II",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_TEST_PIECE_TYPE_II",
        property_label="Type of test piece II",
        description="""Type of test piece II (Metadata → Test piece) // Type of test piece II""",
        mandatory=True,
        section="Test piece",
        ontology_IRI="https://w3id.org/pmd/co/PMD_0020193",
    )
    tensile_test_type_of_test_piece_iii = PropertyTypeAssignment(
        code="TENSILE_TEST_TYPE_OF_TEST_PIECE_III",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_TEST_PIECE_TYPE_III",
        property_label="Type of test piece III",
        description="""Type of test piece III (Metadata → Test piece) // Type of test piece III""",
        mandatory=True,
        section="Test piece",
        ontology_IRI="https://w3id.org/pmd/co/PMD_0020193",
    )
    tensile_test_piece_technical_drawing = PropertyTypeAssignment(
        code="TENSILE_TEST_PIECE_TECHNICAL_DRAWING",
        data_type="MULTILINE_VARCHAR",
        property_label="Test piece technical drawing Description: Link to file, preferably with machine-readable (meta)data",
        description="""Test piece technical drawing Description: Link to file, preferably with machine-readable (meta)data (Metadata → Test piece) // Test piece technical drawing Description: Link to file, preferably with machine-readable (meta)data""",
        mandatory=True,
        section="Test piece",
    )
    tensile_test_piece_origin_and_orientation = PropertyTypeAssignment(
        code="TENSILE_TEST_PIECE_ORIGIN_AND_ORIENTATION",
        data_type="MULTILINE_VARCHAR",
        property_label="Test piece origin and orientation Description: Describe the exact location / positioning of the test piece within the as-tested material. E.g.: Do rolling direction and the longitudinal axis coincide?. Is the test piece located on top or bottom. Do coordinate systems of as-tested material and test piece coincide?. Add a link to a file, e.g., a technical drawing showing this, preferably with machine-readable (meta)data.",
        description="""Test piece origin and orientation Description: Describe the exact location / positioning of the test piece within the as-tested material. E.g.: Do rolling direction and the longitudinal axis coincide?. Is the test piece located on top or bottom. Do coordinate systems of as-tested material and test piece coincide?. Add a link to a file, e.g., a technical drawing showing this, preferably with machine-readable (meta)data. (Metadata → Test piece) // Test piece origin and orientation Description: Describe the exact location / positioning of the test piece within the as-tested material. E.g.: Do rolling direction and the longitudinal axis coincide?. Is the test piece located on top or bottom. Do coordinate systems of as-tested material and test piece coincide?. Add a link to a file, e.g., a technical drawing showing this, preferably with machine-readable (meta)data.""",
        mandatory=True,
        section="Test piece",
    )
    tensile_test_piece_orientation_in_test_machine = PropertyTypeAssignment(
        code="TENSILE_TEST_PIECE_ORIENTATION_IN_TEST_MACHINE",
        data_type="MULTILINE_VARCHAR",
        property_label="Test piece orientation in test machine Description: Describe the exact orientation of the test piece within the test machine.  E.g., is the longitudinal axis of the test piece exactly parallel to the loading axis of the test machine?. Add a link to a file providing evidence, preferably with machine-readable (meta)data. This can be, e.g., a technical drawing.",
        description="""Test piece orientation in test machine Description: Describe the exact orientation of the test piece within the test machine.  E.g., is the longitudinal axis of the test piece exactly parallel to the loading axis of the test machine?. Add a link to a file providing evidence, preferably with machine-readable (meta)data. This can be, e.g., a technical drawing. (Metadata → Test piece) // Test piece orientation in test machine Description: Describe the exact orientation of the test piece within the test machine.  E.g., is the longitudinal axis of the test piece exactly parallel to the loading axis of the test machine?. Add a link to a file providing evidence, preferably with machine-readable (meta)data. This can be, e.g., a technical drawing.""",
        mandatory=True,
        section="Test piece",
    )
    tensile_test_additional_information_test_piece = PropertyTypeAssignment(
        code="TENSILE_TEST_ADDITIONAL_INFORMATION_TEST_PIECE",
        data_type="MULTILINE_VARCHAR",
        property_label="Additional information test piece Description: Add the information or a link to file, preferably with machine-readable (meta)data, e.g., Roughness",
        description="""Additional information test piece Description: Add the information or a link to file, preferably with machine-readable (meta)data, e.g., Roughness (Metadata → Test piece) // Additional information test piece Description: Add the information or a link to file, preferably with machine-readable (meta)data, e.g., Roughness""",
        mandatory=False,
        section="Test piece",
    )
    tensile_test_fixing_technique = PropertyTypeAssignment(
        code="TENSILE_TEST_FIXING_TECHNIQUE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TENSILE_TEST_FIXING_TECHNIQUE",
        property_label="Fixing technique",
        description="""Fixing technique (Metadata → Measuring and test equipment → Test machine → Test piece holder system) // Fixing technique""",
        mandatory=True,
        section="Test piece holder system",
    )

