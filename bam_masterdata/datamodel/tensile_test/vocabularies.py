from bam_masterdata.metadata.definitions import VocabularyTerm, VocabularyTypeDef
from bam_masterdata.metadata.entities import VocabularyType

class TensileTestStandard(VocabularyType):
    defs = VocabularyTypeDef(
        code="TENSILE_TEST_STANDARD",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    din_en_iso_6892_1_2019 = VocabularyTerm(
        code="DIN_EN_ISO_6892_1_2019",
        label="DIN EN ISO 6892-1:2019",
        description="""DIN EN ISO 6892-1:2019 // DIN EN ISO 6892-1:2019""",
    )
    din_en_iso_6892_2_2020 = VocabularyTerm(
        code="DIN_EN_ISO_6892_2_2020",
        label="DIN EN ISO 6892-2:2020",
        description="""DIN EN ISO 6892-2:2020 // DIN EN ISO 6892-2:2020""",
    )
    astm_e8_e8m = VocabularyTerm(
        code="ASTM_E8_E8M",
        label="ASTM E8/E8M",
        description="""ASTM E8/E8M // ASTM E8/E8M""",
    )
    astm_e21 = VocabularyTerm(
        code="ASTM_E21",
        label="ASTM E21",
        description="""ASTM E21 // ASTM E21""",
    )
    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // Other (specify)""",
    )

class TensileTestTypeOfLoading(VocabularyType):
    defs = VocabularyTypeDef(
        code="TENSILE_TEST_TYPE_OF_LOADING",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    tension = VocabularyTerm(
        code="TENSION",
        label="Tension",
        description="""Tension // Tension""",
    )

class TensileTestMethodTestingRate(VocabularyType):
    defs = VocabularyTypeDef(
        code="TENSILE_TEST_METHOD_TESTING_RATE",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    method_a = VocabularyTerm(
        code="METHOD_A",
        label="Method A: testing rate based on strain rate control",
        description="""Method A: testing rate based on strain rate control // Method A: testing rate based on strain rate control""",
    )
    method_b = VocabularyTerm(
        code="METHOD_B",
        label="Method B: testing with expanded strain rate ranges",
        description="""Method B: testing with expanded strain rate ranges // Method B: testing with expanded strain rate ranges""",
    )

class TensileTestExtensometerGaugeLengthDetermination(VocabularyType):
    defs = VocabularyTypeDef(
        code="TENSILE_TEST_EXTENSOMETER_GAUGE_LENGTH_DETERMINATION",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    at_room_temperature = VocabularyTerm(
        code="AT_ROOM_TEMPERATURE",
        label="Le determined at room temperature",
        description="""Le determined at room temperature // Le determined at room temperature""",
    )
    at_test_temperature = VocabularyTerm(
        code="AT_TEST_TEMPERATURE",
        label="Le determined at test temperature",
        description="""Le determined at test temperature // Le determined at test temperature""",
    )
    shortened_at_test_temperature = VocabularyTerm(
        code="SHORTENED_AT_TEST_TEMPERATURE",
        label="Le based on test temperature: shortened Le at test temperature",
        description="""Le based on test temperature: shortened Le at test temperature // Le based on test temperature: shortened Le at test temperature""",
    )
    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // Other (specify)""",
    )

class TensileTestSolidification(VocabularyType):
    defs = VocabularyTypeDef(
        code="TENSILE_TEST_SOLIDIFICATION",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    single_crystal = VocabularyTerm(
        code="SINGLE_CRYSTAL",
        label="Single crystal",
        description="""Single crystal // Single crystal""",
    )
    polycrystal = VocabularyTerm(
        code="POLYCRYSTAL",
        label="Polycrystal",
        description="""Polycrystal // Polycrystal""",
    )
    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // Other (specify)""",
    )

class TensileTestCondition(VocabularyType):
    defs = VocabularyTypeDef(
        code="TENSILE_TEST_CONDITION",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    as_manufactured = VocabularyTerm(
        code="AS_MANUFACTURED",
        label="As manufactured",
        description="""As manufactured // As manufactured""",
    )
    heat_treated = VocabularyTerm(
        code="HEAT_TREATED",
        label="Heat treated",
        description="""Heat treated // Heat treated""",
    )
    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // Other (specify)""",
    )

class TensileTestHeatTreatmentState(VocabularyType):
    defs = VocabularyTypeDef(
        code="TENSILE_TEST_HEAT_TREATMENT_STATE",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    none = VocabularyTerm(
        code="NONE",
        label="None",
        description="""None // None""",
    )
    annealed = VocabularyTerm(
        code="ANNEALED",
        label="Annealed",
        description="""Annealed // Annealed""",
    )
    hardened = VocabularyTerm(
        code="HARDENED",
        label="Hardened",
        description="""Hardened // Hardened""",
    )
    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // Other (specify)""",
    )

class TensileTestTestPieceTypeI(VocabularyType):
    defs = VocabularyTypeDef(
        code="TENSILE_TEST_TEST_PIECE_TYPE_I",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    specimen_according_to_standard = VocabularyTerm(
        code="SPECIMEN_ACCORDING_TO_STANDARD",
        label="Specimen according to standard",
        description="""Specimen according to standard // Specimen according to standard""",
    )
    miniaturized_specimen = VocabularyTerm(
        code="MINIATURIZED_SPECIMEN",
        label="Miniaturized specimen",
        description="""Miniaturized specimen // Miniaturized specimen""",
    )
    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // Other (specify)""",
    )

class TensileTestTestPieceTypeIi(VocabularyType):
    defs = VocabularyTypeDef(
        code="TENSILE_TEST_TEST_PIECE_TYPE_II",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    round_cross_section = VocabularyTerm(
        code="ROUND_CROSS_SECTION",
        label="Round cross section",
        description="""Round cross section // Round cross section""",
    )
    rectangular_cross_section = VocabularyTerm(
        code="RECTANGULAR_CROSS_SECTION",
        label="Rectangular cross section",
        description="""Rectangular cross section // Rectangular cross section""",
    )
    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // Other (specify)""",
    )

class TensileTestTestPieceTypeIii(VocabularyType):
    defs = VocabularyTypeDef(
        code="TENSILE_TEST_TEST_PIECE_TYPE_III",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    smooth_test_piece = VocabularyTerm(
        code="SMOOTH_TEST_PIECE",
        label="Smooth test piece",
        description="""Smooth test piece // Smooth test piece""",
    )
    notched_test_piece = VocabularyTerm(
        code="NOTCHED_TEST_PIECE",
        label="Notched test piece",
        description="""Notched test piece // Notched test piece""",
    )
    combined_test_piece = VocabularyTerm(
        code="COMBINED_TEST_PIECE",
        label="Combined test piece",
        description="""Combined test piece // Combined test piece""",
    )
    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // Other (specify)""",
    )

class TensileTestMachineType(VocabularyType):
    defs = VocabularyTypeDef(
        code="TENSILE_TEST_MACHINE_TYPE",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    electromechanical_drive = VocabularyTerm(
        code="ELECTROMECHANICAL_DRIVE",
        label="Electromechanical drive",
        description="""Electromechanical drive // Electromechanical drive""",
    )
    hydraulic_drive = VocabularyTerm(
        code="HYDRAULIC_DRIVE",
        label="Hydraulic drive",
        description="""Hydraulic drive // Hydraulic drive""",
    )
    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // Other (specify)""",
    )

class TensileTestFurnaceType(VocabularyType):
    defs = VocabularyTypeDef(
        code="TENSILE_TEST_FURNACE_TYPE",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    split_tube_two_zones = VocabularyTerm(
        code="SPLIT_TUBE_TWO_ZONES",
        label="Split tube furnace with two zones",
        description="""Split tube furnace with two zones // Split tube furnace with two zones""",
    )
    split_tube_three_zones = VocabularyTerm(
        code="SPLIT_TUBE_THREE_ZONES",
        label="Split tube furnace with three zones",
        description="""Split tube furnace with three zones // Split tube furnace with three zones""",
    )
    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // Other (specify)""",
    )

class TensileTestFixingTechnique(VocabularyType):
    defs = VocabularyTypeDef(
        code="TENSILE_TEST_FIXING_TECHNIQUE",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    threaded = VocabularyTerm(
        code="THREADED",
        label="Threaded",
        description="""Threaded // Threaded""",
    )
    button_head = VocabularyTerm(
        code="BUTTON_HEAD",
        label="Button-head",
        description="""Button-head // Button-head""",
    )
    wedge_grip = VocabularyTerm(
        code="WEDGE_GRIP",
        label="Wedge grip",
        description="""Wedge grip // Wedge grip""",
    )
    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // Other (specify)""",
    )

class TensileTestTemperatureSignal(VocabularyType):
    defs = VocabularyTypeDef(
        code="TENSILE_TEST_TEMPERATURE_SIGNAL",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    on_test_piece = VocabularyTerm(
        code="ON_TEST_PIECE",
        label="On test piece",
        description="""On test piece // On test piece""",
    )
    via_furnace = VocabularyTerm(
        code="VIA_FURNACE",
        label="Via furnace",
        description="""Via furnace // Via furnace""",
    )
    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // Other (specify)""",
    )

class TensileTestTemperatureSensorType(VocabularyType):
    defs = VocabularyTypeDef(
        code="TENSILE_TEST_TEMPERATURE_SENSOR_TYPE",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    thermocouple = VocabularyTerm(
        code="THERMOCOUPLE",
        label="Thermocouple",
        description="""Thermocouple // Thermocouple""",
    )
    thermocamera = VocabularyTerm(
        code="THERMOCAMERA",
        label="Thermocamera",
        description="""Thermocamera // Thermocamera""",
    )
    resistance_thermometer = VocabularyTerm(
        code="RESISTANCE_THERMOMETER",
        label="Resistance thermometer",
        description="""Resistance thermometer // Resistance thermometer""",
    )
    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // Other (specify)""",
    )

class ThermocoupleType(VocabularyType):
    defs = VocabularyTypeDef(
        code="THERMOCOUPLE_TYPE",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    type_k = VocabularyTerm(
        code="TYPE_K",
        label="Type K",
        description="""Type K // Type K""",
    )
    type_n = VocabularyTerm(
        code="TYPE_N",
        label="Type N",
        description="""Type N // Type N""",
    )
    type_s = VocabularyTerm(
        code="TYPE_S",
        label="Type S",
        description="""Type S // Type S""",
    )
    type_r = VocabularyTerm(
        code="TYPE_R",
        label="Type R",
        description="""Type R // Type R""",
    )
    type_b = VocabularyTerm(
        code="TYPE_B",
        label="Type B",
        description="""Type B // Type B""",
    )
    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // Other (specify)""",
    )

class TensileTestThermocoupleCalibrationMethod(VocabularyType):
    defs = VocabularyTypeDef(
        code="TENSILE_TEST_THERMOCOUPLE_CALIBRATION_METHOD",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    comparison_method = VocabularyTerm(
        code="COMPARISON_METHOD",
        label="Comparison method",
        description="""Comparison method // Comparison method""",
    )
    fixed_point_method = VocabularyTerm(
        code="FIXED_POINT_METHOD",
        label="Fixed-point method",
        description="""Fixed-point method // Fixed-point method""",
    )
    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // Other (specify)""",
    )

class TensileTestThermocoupleContactMethod(VocabularyType):
    defs = VocabularyTypeDef(
        code="TENSILE_TEST_THERMOCOUPLE_CONTACT_METHOD",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    welded = VocabularyTerm(
        code="WELDED",
        label="Welded",
        description="""Welded // Welded""",
    )
    attached = VocabularyTerm(
        code="ATTACHED",
        label="Attached",
        description="""Attached // Attached""",
    )
    pressed = VocabularyTerm(
        code="PRESSED",
        label="Pressed",
        description="""Pressed // Pressed""",
    )
    glued = VocabularyTerm(
        code="GLUED",
        label="Glued",
        description="""Glued // Glued""",
    )
    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // Other (specify)""",
    )

class TensileTestDisplacementMeasuringMethod(VocabularyType):
    defs = VocabularyTypeDef(
        code="TENSILE_TEST_DISPLACEMENT_MEASURING_METHOD",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    contacting_method = VocabularyTerm(
        code="CONTACTING_METHOD",
        label="Contacting method",
        description="""Contacting method // Contacting method""",
    )
    non_contacting_method = VocabularyTerm(
        code="NON_CONTACTING_METHOD",
        label="Non-contacting method",
        description="""Non-contacting method // Non-contacting method""",
    )

class TensileTestSensorTypeContacting(VocabularyType):
    defs = VocabularyTypeDef(
        code="TENSILE_TEST_SENSOR_TYPE_CONTACTING",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    clip_on_extensometer = VocabularyTerm(
        code="CLIP_ON_EXTENSOMETER",
        label="Clip-on extensometer",
        description="""Clip-on extensometer // Clip-on extensometer""",
    )
    lvdt_with_extension_legs = VocabularyTerm(
        code="LVDT_WITH_EXTENSION_LEGS",
        label="LVDT with extension legs",
        description="""LVDT with extension legs // LVDT with extension legs""",
    )
    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // Other (specify)""",
    )

class TensileTestSensorTypeNonContacting(VocabularyType):
    defs = VocabularyTypeDef(
        code="TENSILE_TEST_SENSOR_TYPE_NON_CONTACTING",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    laser_extensometer = VocabularyTerm(
        code="LASER_EXTENSOMETER",
        label="Laser extensometer",
        description="""Laser extensometer // Laser extensometer""",
    )
    digital_image_correlation = VocabularyTerm(
        code="DIGITAL_IMAGE_CORRELATION",
        label="Digital image correlation",
        description="""Digital image correlation // Digital image correlation""",
    )
    video_extensometer = VocabularyTerm(
        code="VIDEO_EXTENSOMETER",
        label="Video extensometer",
        description="""Video extensometer // Video extensometer""",
    )
    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // Other (specify)""",
    )

class TensileTestMeasurementSetup(VocabularyType):
    defs = VocabularyTypeDef(
        code="TENSILE_TEST_MEASUREMENT_SETUP",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    one_sided = VocabularyTerm(
        code="ONE_SIDED",
        label="One-sided",
        description="""One-sided // One-sided""",
    )
    two_sided = VocabularyTerm(
        code="TWO_SIDED",
        label="Two-sided",
        description="""Two-sided // Two-sided""",
    )

class TensileTestMeasurementDirection(VocabularyType):
    defs = VocabularyTypeDef(
        code="TENSILE_TEST_MEASUREMENT_DIRECTION",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    axial_action = VocabularyTerm(
        code="AXIAL_ACTION",
        label="Axial action",
        description="""Axial action // Axial action""",
    )
    diametrical_action = VocabularyTerm(
        code="DIAMETRICAL_ACTION",
        label="Diametrical action",
        description="""Diametrical action // Diametrical action""",
    )

class TensileTestMountingType(VocabularyType):
    defs = VocabularyTypeDef(
        code="TENSILE_TEST_MOUNTING_TYPE",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    at_test_piece_in_parallel_length = VocabularyTerm(
        code="AT_TEST_PIECE_IN_PARALLEL_LENGTH",
        label="At test piece in parallel length",
        description="""At test piece in parallel length // At test piece in parallel length""",
    )
    at_collars = VocabularyTerm(
        code="AT_COLLARS",
        label="At collars",
        description="""At collars // At collars""",
    )
    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // Other (specify)""",
    )

class TensileTestMeasuringEquipment(VocabularyType):
    defs = VocabularyTypeDef(
        code="TENSILE_TEST_MEASURING_EQUIPMENT",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    caliper_gauge = VocabularyTerm(
        code="CALIPER_GAUGE",
        label="Caliper gauge",
        description="""Caliper gauge // Caliper gauge""",
    )
    micrometer = VocabularyTerm(
        code="MICROMETER",
        label="Micrometer",
        description="""Micrometer // Micrometer""",
    )
    measuring_microscope = VocabularyTerm(
        code="MEASURING_MICROSCOPE",
        label="Measuring microscope",
        description="""Measuring microscope // Measuring microscope""",
    )
    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // Other (specify)""",
    )

class TensileTestMeasuringEquipmentType(VocabularyType):
    defs = VocabularyTypeDef(
        code="TENSILE_TEST_MEASURING_EQUIPMENT_TYPE",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    digital = VocabularyTerm(
        code="DIGITAL",
        label="Digital",
        description="""Digital // Digital""",
    )
    analog = VocabularyTerm(
        code="ANALOG",
        label="Analog",
        description="""Analog // Analog""",
    )
    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // Other (specify)""",
    )

class TensileTestFracturePosition(VocabularyType):
    defs = VocabularyTypeDef(
        code="TENSILE_TEST_FRACTURE_POSITION",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    within_extensometer_gauge_length = VocabularyTerm(
        code="WITHIN_EXTENSOMETER_GAUGE_LENGTH",
        label="Within the extensometer gauge length",
        description="""Within the extensometer gauge length // Within the extensometer gauge length""",
    )
    outside_extensometer_gauge_length = VocabularyTerm(
        code="OUTSIDE_EXTENSOMETER_GAUGE_LENGTH",
        label="Outside the extensometer gauge length",
        description="""Outside the extensometer gauge length // Outside the extensometer gauge length""",
    )
    outside_parallel_length = VocabularyTerm(
        code="OUTSIDE_PARALLEL_LENGTH",
        label="Outside the parallel length",
        description="""Outside the parallel length // Outside the parallel length""",
    )
    no_fracture = VocabularyTerm(
        code="NO_FRACTURE",
        label="No fracture",
        description="""No fracture // No fracture""",
    )
    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // Other (specify)""",
    )

class TensileTestForceRecording(VocabularyType):
    defs = VocabularyTypeDef(
        code="TENSILE_TEST_FORCE_RECORDING",
        description="""Controlled vocabulary for tensile-test metadata // Kontrolliertes Vokabular fuer Zugversuchsmetadaten""",
    )
    continuously = VocabularyTerm(
        code="CONTINUOUSLY",
        label="Continuously",
        description="""Continuously // Continuously""",
    )
    periodically = VocabularyTerm(
        code="PERIODICALLY",
        label="Periodically",
        description="""Periodically // Periodically""",
    )

