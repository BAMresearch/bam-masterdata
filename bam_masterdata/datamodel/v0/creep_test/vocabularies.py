from bam_masterdata.metadata.definitions import VocabularyTerm, VocabularyTypeDef
from bam_masterdata.metadata.entities import VocabularyType


class CreepTestStandard(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_STANDARD",
        description="""Test Standard (Metadata, Test info, Test parameters) // Test Standard (Metadaten, Test-Information, Test-Parameter)""",
    )

    iso_204 = VocabularyTerm(
        code="DIN_EN_ISO_204",
        label="DIN EN ISO 204",
        description="""DIN EN ISO 204 - Metallic materials - Uniaxial creep testing in tension - Method of test // DIN EN ISO 204 - Metallische Werkstoffe - Einachsiger Zeitstandversuch unter Zugbeanspruchung - Prüfverfahren""",
    )

    astm_e139 = VocabularyTerm(
        code="ASTM_E139",
        label="ASTM E139",
        description="""ASTM E139 - Standard Test Methods for Conducting Creep, Creep-Rupture, and Stress-Rupture Tests of Metallic Materials // ASTM E139 - Standardtestmethoden zur Durchführung von Kriech-, Kriechbruch- und Spannungsbruchprüfungen an metallischen Werkstoffen""",
    )

    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (Specify)",
        description="""Other (Specify) // andere (bitte angeben)""",
    )


class TypeOfLoading(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_TYPE_OF_LOADING",
        description="""Type of Loading (Metadata, Test info, Test parameters) // Art der Lastaufbringung (Metadaten, Test-Information, Test-Parameter)""",
    )

    tension = VocabularyTerm(
        code="TENSION",
        label="Tension",
        description="""tension // Zug""",
    )

    compression = VocabularyTerm(
        code="COMPRESSION",
        label="Compression",
        description="""compression // Druck""",
    )

    bending = VocabularyTerm(
        code="BENDING",
        label="Bending",
        description="""bending // Biegung""",
    )


class LoadControlType(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_LOAD_CONTROL_TYPE",
        description="""Load Control Type (Metadata, Test info, Test parameters) // Laststeuerungstyp (Metadaten, Test-Information, Test-Parameter)""",
    )

    constant_force = VocabularyTerm(
        code="CONSTANT_FORCE",
        label="Constant force",
        description="""Constant force // Konstante Kraft""",
    )

    constant_stress = VocabularyTerm(
        code="CONSTANT_STRESS",
        label="Constant stress",
        description="""Constant stress // Konstante Spannung""",
    )


class CreepTestType(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_TYPE",
        description="""Test Type (Metadata, Test info, Test parameters) // Test-Typ (Metadaten, Test-Information, Test-Parameter)""",
    )

    uninterrupted_creep_tests_continuous_extension = VocabularyTerm(
        code="UNINTERRUPTED_CREEP_TESTS_CONTINUOUS_EXTENSION",
        label="Uninterrupted creep tests with continuous monitoring of extension",
        description="""Uninterrupted creep tests with continuous monitoring of extension // Ununterbrochene Kriechprüfungen mit kontinuierlicher Überwachung der Verlängerung""",
    )

    interrupted_creep_tests_periodic_elongation = VocabularyTerm(
        code="INTERRUPTED_CREEP_TESTS_PERIODIC_ELONGATION",
        label="Interrupted creep tests with periodic measurement of elongation",
        description="""Interrupted creep tests with periodic measurement of elongation // Unterbrochene Kriechprüfungen mit periodischer Messung der Verlängerung""",
    )

    stress_rupture_tests_time_to_fracture_measured = VocabularyTerm(
        code="STRESS_RUPTURE_TESTS_TIME_TO_FRACTURE_MEASURED",
        label="Stress rupture tests where normally only the time to fracture is measured",
        description="""Stress rupture tests where normally only the time to fracture is measured // Spannungsbruchprüfungen, bei denen normalerweise nur die Zeit bis zum Bruch gemessen wird""",
    )


class EndOfTestCriterium(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_END_OF_TEST_CRITERIUM",
        description="""End of Test Criterium (Metadata, Test info, Test parameters) // Testabbruchkriterium (Metadaten, Test-Information, Test-Parameter)""",
    )

    test_piece_break = VocabularyTerm(
        code="TEST_PIECE_BREAK",
        label="Test piece break",
        description="""Test piece break // Probenbruch""",
    )

    time_limit = VocabularyTerm(
        code="TIME_LIMIT",
        label="Time limit",
        description="""Time limit // Zeitlimit""",
    )

    extension_limit = VocabularyTerm(
        code="EXTENSION_LIMIT",
        label="Extension limit",
        description="""Extension limit // Dehnungsgrenzenlimit""",
    )

    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (Specify)",
        description="""Other (Specify) // andere (bitte angeben)""",
    )


class InterruptionCourse(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_INTERRUPTION_COURSE",
        description="""Interruption Course (Metadata, Test info, Test parameters) // Unterbrechungsverlauf (Metadaten, Test-Information, Test-Parameter)""",
    )

    unloading_before_cooling = VocabularyTerm(
        code="UNLOADING_BEFORE_COOLING",
        label="Unloading before cooling",
        description="""Unloading before cooling // Entlastung vor Abkühlung""",
    )

    unloading_after_cooling = VocabularyTerm(
        code="UNLOADING_AFTER_COOLING",
        label="Unloading after cooling",
        description="""Unloading after cooling // Entlastung nach Abkühlung""",
    )


class Solidification(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_SOLIDIFICATION",
        description="""Solidification - In which form was the material solidified, e.g. single crystal, poly crystal? (Metadata, Material history and condition, As-manufactured material) // Solidification - In welcher Form wurde das Material verfestigt, z. B. Einkristall, Polykristall? (Metadaten, Materialhistorie und Zustand, Material im Herstellungszustand)""",
    )

    single_crystal = VocabularyTerm(
        code="SINGLE_CRYSTAL",
        label="Single crystal",
        description="""Single crystal // Einkristall""",
    )

    polycrystal = VocabularyTerm(
        code="POLYCRYSTAL",
        label="Polycrystal",
        description="""polycrystal // Polykristall""",
    )


class Condition(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_CONDITION",
        description="""Condition (Metadata, Material history and condition, As-manufactured material) // Condition (Metadaten, Materialhistorie und Zustand, Material im Herstellungszustand)""",
    )

    heat_treated = VocabularyTerm(
        code="HEAT_TREATED",
        label="Heat treated",
        description="""Heat treated // Wärmebehandelt""",
    )

    as_manufactured = VocabularyTerm(
        code="AS_MANUFACTURED",
        label="As manufactured",
        description="""As manufactured // Material im Herstellungszustand""",
    )


class HeatTreatmentState(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_HEAT_TREATMENT_STATE",
        description="""Heat Treatment - State (Metadata, Material history and condition, Heat treatment) // Wärmebehandlung - Zustand (Metadaten, Materialhistorie und Zustand, Wärmebehandlung)""",
    )

    term_none = VocabularyTerm(
        code="NONE",
        label="None",
        description="""none // keine""",
    )

    annealed = VocabularyTerm(
        code="ANNEALED",
        label="Annealed",
        description="""annealed // annealed""",
    )

    hardened = VocabularyTerm(
        code="HARDENED",
        label="Hardened",
        description="""hardened // gehärtet""",
    )

    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (Specify)",
        description="""Other (Specify) // andere (bitte angeben)""",
    )


class MicrostructureFeature(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_MICROSTRUCTURE_FEATURE",
        description="""Microstructure Feature (Metadata, Material history and condition, Microstructure) // Mikrostrukturmerkmal (Metadaten, Materialhistorie und Zustand, Mikrostruktur)""",
    )

    matrix = VocabularyTerm(
        code="MATRIX",
        label="Matrix",
        description="""matrix // Matrix""",
    )

    phase = VocabularyTerm(
        code="PHASE",
        label="Phase",
        description="""phase // Phase""",
    )

    grain_boundary = VocabularyTerm(
        code="GRAIN_BOUNDARY",
        label="Grain Boundary",
        description="""Grain Boundary // Korngrenze""",
    )

    dendrite = VocabularyTerm(
        code="DENDRITE",
        label="Dendrite",
        description="""dendrite // Dendrit""",
    )

    precipitate = VocabularyTerm(
        code="PRECIPITATE",
        label="Precipitate",
        description="""precipitate // Ausscheidung""",
    )

    inclusion = VocabularyTerm(
        code="INCLUSION",
        label="Inclusion",
        description="""inclusion // Einschluss""",
    )

    grain = VocabularyTerm(
        code="GRAIN",
        label="Grain",
        description="""grain // Korn""",
    )

    segregation = VocabularyTerm(
        code="SEGREGATION",
        label="Segregation",
        description="""segregation // Segregation""",
    )

    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (Specify)",
        description="""Other (Specify) // andere (bitte angeben)""",
    )


class GrainSizeDeterminationMethod(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_GRAIN_SIZE_DETERMINATION_METHOD",
        description="""Grain Size - Determination Method (Metadata, Material history and condition, Microstructure) // Korngröße - Bestimmungsmethode (Metadaten, Materialhistorie und Zustand, Mikrostruktur)""",
    )

    line_intercept = VocabularyTerm(
        code="LINE_INTERCEPT",
        label="Line Intercept",
        description="""Line Intercept // Schnittlinienmethode""",
    )

    circular_intercept = VocabularyTerm(
        code="CIRCULAR_INTERCEPT",
        label="Circular Intercept",
        description="""Circular Intercept // kreisförmige Schnittlinienmethode""",
    )

    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (Specify)",
        description="""Other (Specify) // andere (bitte angeben)""",
    )


class MeasuredCondition(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_MEASURED_CONDITION",
        description="""Measured Condition (Metadata, Material history and condition, Chemical composition) // Gemessener Zustand (Metadaten, Materialhistorie und Zustand, Chemische Zusammensetzung)""",
    )

    as_manufactured = VocabularyTerm(
        code="AS_MANUFACTURED",
        label="As-manufactured",
        description="""As-manufactured // wie hergestellt""",
    )

    heat_treated = VocabularyTerm(
        code="HEAT_TREATED",
        label="Heat-treated",
        description="""Heat-treated // wärmebehandelt""",
    )

    as_tested = VocabularyTerm(
        code="AS_TESTED",
        label="As-tested",
        description="""As-tested // wie getestet""",
    )

    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (Specify)",
        description="""Other (Specify) // andere (bitte angeben)""",
    )


class TestPieceTypeI(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_TEST_PIECE_TYPE_I",
        description="""Test Piece Type I (Metadata, Test piece) // Prüfstück Typ I (Metadaten, Probenkörper)""",
    )

    miniaturized_specimen = VocabularyTerm(
        code="MINIATURIZED_SPECIMEN",
        label="Miniaturized specimen",
        description="""Miniaturized specimen // Miniaturisierte Proben""",
    )

    specimen_according_to_standard = VocabularyTerm(
        code="SPECIMEN_ACCORDING_TO_STANDARD",
        label="Specimen according to standard",
        description="""Specimen according to standard // Probe gemäß Norm""",
    )


class TestPieceTypeII(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_TEST_PIECE_TYPE_II",
        description="""Test Piece Type II (Metadata, Test piece) // Prüfstück Typ II (Metadaten, Probenkörper)""",
    )

    round_cross_section = VocabularyTerm(
        code="ROUND_CROSS_SECTION",
        label="Round cross section",
        description="""Round cross section // Rundquerschnitt""",
    )

    rectangular_section = VocabularyTerm(
        code="RECTANGULAR_SECTION",
        label="Rectangular section",
        description="""Rectangular section // Rechteckquerschnitt""",
    )


class TestPieceTypeIII(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_TEST_PIECE_TYPE_III",
        description="""Test Piece Type III (Metadata, Test piece) // Prüfstück Typ III (Metadaten, Probenkörper)""",
    )

    smooth_test_piece = VocabularyTerm(
        code="SMOOTH_TEST_PIECE",
        label="Smooth test piece",
        description="""Smooth test piece // Glatter Prüfkörper""",
    )

    notched_test_piece = VocabularyTerm(
        code="NOTCHED_TEST_PIECE",
        label="Notched test piece",
        description="""Notched test piece // Gekerbter Prüfkörper""",
    )

    combined_test_piece = VocabularyTerm(
        code="COMBINED_TEST_PIECE",
        label="Combined test piece",
        description="""Combined test piece // Kombinierter Prüfkörper""",
    )

    other_type_specify = VocabularyTerm(
        code="OTHER_TYPE_SPECIFY",
        label="Other type (specify)",
        description="""Other type (specify) // andere (bitte angeben)""",
    )


class CreepTestMachineType(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_MACHINE_TYPE",
        description="""Test Machine Type (Metadata, Measuring and test equipment, Test machine) // Prüfmaschinentyp (Metadaten, Mess- und Prüfmittel, Prüfmaschine)""",
    )

    lever_arm = VocabularyTerm(
        code="LEVER_ARM",
        label="Lever arm",
        description="""Lever arm // Hebelarm""",
    )

    electromechanical_drive = VocabularyTerm(
        code="ELECTROMECHANICAL_DRIVE",
        label="Electromechanical drive",
        description="""Electromechanical drive // Elektromechanischer Antrieb""",
    )

    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (Specify)",
        description="""Other (Specify) // andere (bitte angeben)""",
    )


class CreepTestFurnaceType(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_FURNACE_TYPE",
        description="""Furnace Type (Metadata, Measuring and test equipment, Test machine, Heating system) // Ofentyp (Metadaten, Mess- und Prüfmittel, Prüfmaschine, Heizsystem)""",
    )

    split_tube_furnace_with_two_zones = VocabularyTerm(
        code="SPLIT_TUBE_FURNACE_WITH_TWO_ZONES",
        label="Split Tube Furnace with Two-zones",
        description="""Split Tube Furnace with Two-zones // Spaltrohr-Röhrenofen mit zwei Zonen""",
    )

    split_tube_furnace_with_three_zones = VocabularyTerm(
        code="SPLIT_TUBE_FURNACE_WITH_THREE_ZONES",
        label="Split Tube Furnace with Three-zones",
        description="""Split Tube Furnace with Three-zones // Spaltrohr-Röhrenofen mit drei Zonen""",
    )

    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // andere (bitte angeben)""",
    )


class CreepTestFixingTechnique(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_FIXING_TECHNIQUE",
        description="""Fixing Technique (Metadata, Measuring and test equipment, Test machine, Test piece holder system) // Befestigungstechnik (Metadaten, Mess- und Prüfmittel, Prüfmaschine, Probenhaltersystem)""",
    )

    threaded = VocabularyTerm(
        code="THREADED",
        label="Threaded",
        description="""threaded // verschraubt""",
    )

    button_head = VocabularyTerm(
        code="BUTTON_HEAD",
        label="Button-head",
        description="""Button-head // Knopfkopf""",
    )

    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // andere (bitte angeben)""",
    )


class CreepTestLoadSystemCalibrationStandard(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_LOAD_SYSTEM_CALIBRATION_STANDARD",
        description="""Calibration Standard (Metadata, Measuring and test equipment, Test machine, Loading system) // Kalibrierstandard (Metadaten, Mess- und Prüfmittel, Prüfmaschine, Belastungssystem)""",
    )

    din_en_iso_7500_2 = VocabularyTerm(
        code="DIN_EN_ISO_7500_2",
        label="DIN EN ISO 7500-2",
        description="""DIN EN ISO 7500-2 - Metallic materials - Verification of static uniaxial testing machines - Part 2: Tension creep testing machines - Verification of the applied force // DIN EN ISO 7500-2 - Metallische Werkstoffe - Prüfung von statischen einachsigen Prüfmaschinen - Teil 2: Zeitstandprüfmaschinen für Zugbeanspruchung - Prüfung der angewendeten Kraft""",
    )

    others_specify = VocabularyTerm(
        code="OTHERS_SPECIFY",
        label="Others (specify)",
        description="""Others (specify) // Others (specify)""",
    )


class TemperatureSignal(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_TEMPERATURE_SIGNAL",
        description="""Temperature Signal - Which temperature signal was used for temperature control? (Metadata, Measuring and test equipment, Temperature-measuring system) // Temperatursignal - Welches Temperatursignal wurde für die Temperatursteuerung verwendet? (Metadaten, Mess- und Prüfmittel, Temperaturmesssystem)""",
    )

    on_test_piece = VocabularyTerm(
        code="ON_TEST_PIECE",
        label="On test piece",
        description="""On test piece // am Prüfkörper""",
    )

    via_furnace = VocabularyTerm(
        code="VIA_FURNACE",
        label="Via furnace",
        description="""Via furnace // über dem Ofen""",
    )

    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // andere (bitte angeben)""",
    )


class CreepTestSensorType(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_SENSOR_TYPE",
        description="""Sensor Type (Metadata, Measuring and test equipment, Temperature-measuring system, Temperature sensor) // Sensortyp (Metadaten, Mess- und Prüfmittel, Temperaturmesssystem, Temperatursensor)""",
    )

    thermocouple = VocabularyTerm(
        code="THERMOCOUPLE",
        label="Thermocouple",
        description="""thermocouple // Thermoelement""",
    )

    thermocamera = VocabularyTerm(
        code="THERMOCAMERA",
        label="Thermocamera",
        description="""thermocamera // Thermokamera""",
    )


class CreepTestThermocoupleCalibrationMethod(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_THERMOCOUPLE_CALIBRATION_METHOD",
        description="""Calibration Method (Metadata, Measuring and test equipment, Temperature-measuring system, Temperature sensor) // Kalibriermethode (Metadaten, Mess- und Prüfmittel, Temperaturmesssystem, Temperatursensor)""",
    )

    comparison_method = VocabularyTerm(
        code="COMPARISON_METHOD",
        label="Comparison method",
        description="""Comparison method // Vergleichsmethode""",
    )

    fix_point_method = VocabularyTerm(
        code="FIX_POINT_METHOD",
        label="Fix-point method",
        description="""Fix-point method // Fixpunktmethode""",
    )


class CreepTestThermocoupleCalibrationStandard(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_THERMOCOUPLE_CALIBRATION_STANDARD",
        description="""Calibration Standard (Metadata, Measuring and test equipment, Temperature-measuring system, Temperature sensor) // Kalibrierstandard (Metadaten, Mess- und Prüfmittel, Temperaturmesssystem, Temperatursensor)""",
    )

    astm_e220 = VocabularyTerm(
        code="ASTM_E220",
        label="ASTM E220",
        description="""ASTM E220 - Standard Test Method for Calibration of Thermocouples By Comparison Techniques // ASTM E220 - Standardtestverfahren zur Kalibrierung von Thermoelementen durch Vergleichstechniken""",
    )

    euramet_cg_08 = VocabularyTerm(
        code="EURAMET_CG_08",
        label="EURAMET cg-08",
        description="""EURAMET cg-08 - Calibration of Thermocouples // EURAMET cg-08 - Kalibrierung von Thermoelementen""",
    )

    guideline_dkd_r_5_3 = VocabularyTerm(
        code="GUIDELINE_DKD_R_5_3",
        label="Guideline DKD-R 5-3",
        description="""Guideline DKD-R 5-3  - Calibration of Thermocouples // Guideline DKD-R 5-3 - Kalibrierung von Thermoelementen""",
    )

    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (Specify)",
        description="""Other (Specify) // andere (bitte angeben)""",
    )


class CreepTestThermocoupleContactMethod(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_THERMOCOUPLE_CONTACT_METHOD",
        description="""Contact Method (Metadata, Measuring and test equipment, Temperature-measuring system, Temperature sensor) // Kontaktmethode (Metadaten, Mess- und Prüfmittel, Temperaturmesssystem, Temperatursensor)""",
    )

    welded = VocabularyTerm(
        code="WELDED",
        label="Welded",
        description="""welded // angeschweißt""",
    )

    attached = VocabularyTerm(
        code="ATTACHED",
        label="Attached",
        description="""attached // befestigt""",
    )

    pressed = VocabularyTerm(
        code="PRESSED",
        label="Pressed",
        description="""pressed // (an)gepresst""",
    )

    glued = VocabularyTerm(
        code="GLUED",
        label="Glued",
        description="""glued // geklebt""",
    )

    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // andere (bitte angeben)""",
    )


class CreepTestThermocoupleLocation(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_THERMOCOUPLE_LOCATION",
        description="""Thermocouple Location - Location with respect to gauge section (Metadata, Measuring and test equipment, Temperature-measuring system, Temperature sensor) // Position des Thermoelements - Position in Bezug auf den Messbereich (Metadaten, Mess- und Prüfmittel, Temperaturmesssystem, Temperatursensor)""",
    )

    inside = VocabularyTerm(
        code="INSIDE",
        label="Inside",
        description="""inside // innen""",
    )

    outside = VocabularyTerm(
        code="OUTSIDE",
        label="Outside",
        description="""outside // außen""",
    )


class CreepTestReferenceJunction(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_REFERENCE_JUNCTION",
        description="""Reference Junction (Metadata, Measuring and test equipment, Temperature-measuring system, Data acquisition) // Referenzstelle (Metadaten, Mess- und Prüfmittel, Temperaturmesssystem, Datenerfassung)""",
    )

    internal = VocabularyTerm(
        code="INTERNAL",
        label="Internal",
        description="""internal // intern""",
    )

    external = VocabularyTerm(
        code="EXTERNAL",
        label="External",
        description="""external // extern""",
    )


class CreepTestDataAcquisitionCalibrationStandard(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_DATA_ACQUISITION_CALIBRATION_STANDARD",
        description="""Calibration Standard for data acquisition system (Metadata, Measuring and test equipment, Temperature-measuring system, Data acquisition) // Kalibrierstandard für das Datenerfassungssystem (Metadaten, Mess- und Prüfmittel, Temperaturmesssystem, Datenerfassung)""",
    )

    euramet_cg_11 = VocabularyTerm(
        code="EURAMET_CG_11",
        label="EURAMET cg-11",
        description="""EURAMET cg-11 // EURAMET cg-11""",
    )

    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // Other (specify)""",
    )


class CreepTestDisplacementMeasuringMethod(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_DISPLACEMENT_MEASURING_METHOD",
        description="""Displacement Measuring Method - Type of strain measuring device (Metadata, Measuring and test equipment, Extensometer system) // Wegmessverfahren - Art des Dehnungsmessgeräts (Metadaten, Mess- und Prüfmittel, Extensometersystem)""",
    )

    contacting_method = VocabularyTerm(
        code="CONTACTING_METHOD",
        label="Contacting method",
        description="""Contacting method // Kontaktmethode""",
    )

    non_contacting_method = VocabularyTerm(
        code="NON_CONTACTING_METHOD",
        label="Non-contacting method",
        description="""Non-contacting method // berührungslose Methode""",
    )


class CreepTestSensorTypeContactingMethod(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_SENSOR_TYPE_CONTACTING_METHOD",
        description="""Sensor Type - Contacting Method (Metadata, Measuring and test equipment, Extensometer system) // Sensortyp – Kontaktmethode (Metadaten, Mess- und Prüfmittel, Extensometersystem)""",
    )

    lvdt_with_extension_legs = VocabularyTerm(
        code="LVDT_WITH_EXTENSION_LEGS",
        label="LVDT with extension legs",
        description="""LVDT with extension legs // LVDT mit Verlängerungsarmen""",
    )

    clip_on_extensometer = VocabularyTerm(
        code="CLIP_ON_EXTENSOMETER",
        label="Clip-on extensometer",
        description="""Clip-on extensometer // Clip-on-Extensometer""",
    )

    analog_dial_gauges = VocabularyTerm(
        code="ANALOG_DIAL_GAUGES",
        label="Analog dial gauges",
        description="""Analog dial gauges // Analoge Messuhren""",
    )

    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (Specify)",
        description="""Other (Specify) // andere (bitte angeben)""",
    )


class CreepTestSensorTypeNonContactingMethod(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_SENSOR_TYPE_NON_CONTACTING_METHOD",
        description="""Sensor Type - Non-contacting Method (Metadata, Measuring and test equipment, Extensometer system) // Sensortyp – berührungslose Methode (Metadaten, Mess- und Prüfmittel, Extensometersystem)""",
    )

    laserextensometer = VocabularyTerm(
        code="LASEREXTENSOMETER",
        label="Laserextensometer",
        description="""laserextensometer // Laserextensometer""",
    )

    digital_image_correlation_technique = VocabularyTerm(
        code="DIGITAL_IMAGE_CORRELATION_TECHNIQUE",
        label="Digital image correlation technique",
        description="""Digital image correlation technique // Digitale Bildkorrelation (DIC)""",
    )

    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (Specify)",
        description="""Other (Specify) // andere (bitte angeben)""",
    )


class CreepTestMeasurementSetup(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_MEASUREMENT_SETUP",
        description="""Measurement Setup - Measurement one-sided or two-sided? (Metadata, Measuring and test equipment, Extension values, Contacting extensometer) // Messaufbau - Einseitige oder beidseitige Messung? (Metadaten, Mess- und Prüfmittel, Dehnungswerte, kontaktierendes Extensometer)""",
    )

    one_sided = VocabularyTerm(
        code="ONE_SIDED",
        label="One-sided",
        description="""One-sided // einseitig""",
    )

    two_sided = VocabularyTerm(
        code="TWO_SIDED",
        label="Two-sided",
        description="""Two-sided // beidseitig""",
    )


class CreepTestMeasurementDirection(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_EXTENSION_MEASUREMENT_DIRECTION",
        description="""Measurement Direction (Metadata, Measuring and test equipment, Extension values, Contacting extensometer) // Messrichtung (Metadaten, Mess- und Prüfmittel, Dehnungswerte, kontaktierendes Extensometer)""",
    )

    axial_action = VocabularyTerm(
        code="AXIAL_ACTION",
        label="Axial action",
        description="""Axial action // axial""",
    )

    diametrical_action = VocabularyTerm(
        code="DIAMETRICAL_ACTION",
        label="Diametrical action",
        description="""Diametrical action // diametral""",
    )


class CreepTestMountingType(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_EXTENSOMETER_MOUNTING_TYPE",
        description="""Mounting Type (Metadata, Measuring and test equipment, Extension values, Contacting extensometer) // Montageart (Metadaten, Mess- und Prüfmittel, Dehnungswerte, kontaktierendes Extensometer)""",
    )

    at_test_piece_in_parallel_length = VocabularyTerm(
        code="AT_TEST_PIECE_IN_PARALLEL_LENGTH",
        label="At test piece in parallel length",
        description="""At test piece in parallel length // Am Prüfkörper in der parallelen Länge""",
    )

    at_collars = VocabularyTerm(
        code="AT_COLLARS",
        label="At collars",
        description="""At collars // An den Kragen""",
    )

    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (Specify)",
        description="""Other (Specify) // andere (bitte angeben)""",
    )


class ExtensometerLegMaterial(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_EXTENSOMETER_LEG_MATERIAL",
        description="""Extensometer Leg Material - Material of upper/lower legs, e.g., in LVDT systems (Metadata, Measuring and test equipment, Extension values, Contacting extensometer) // Material der Extensometerschenkel - Material der Ober-/Unterbeine, z. B. in LVDT-Systemen (Metadaten, Mess- und Prüfmittel, Dehnungswerte, kontaktierendes Extensometer)""",
    )

    ceramic_legs = VocabularyTerm(
        code="CERAMIC_LEGS",
        label="Ceramic legs",
        description="""Ceramic legs // Keramikschenkel""",
    )

    metallic_legs = VocabularyTerm(
        code="METALLIC_LEGS",
        label="Metallic legs",
        description="""Metallic legs // Metallschenkel""",
    )


class MeasuringEquipment(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_MEASURING_EQUIPMENT",
        description="""Measuring Equipment (Metadata, Measuring and test equipment, Elongation values and cross-sectional dimensions) // Messgeräte (Metadaten, Mess- und Prüfmittel, Dehnungswerte und Querschnittsabmessungen)""",
    )

    caliper_gauge = VocabularyTerm(
        code="CALIPER_GAUGE",
        label="Caliper gauge",
        description="""Caliper gauge // Messschieber""",
    )

    measuring_microscope = VocabularyTerm(
        code="MEASURING_MICROSCOPE",
        label="Measuring microscope",
        description="""Measuring microscope // Messmikroskop""",
    )

    micrometer_screw_gauge = VocabularyTerm(
        code="MICROMETER_SCREW_GAUGE",
        label="Micrometer screw gauge",
        description="""Micrometer screw gauge // Bügelmessschraube""",
    )

    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // andere (bitte angeben)""",
    )


class MeasuringEquipmentType(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_MEASURING_EQUIPMENT_TYPE",
        description="""Type of measuring equipment (Metadata, Measuring and test equipment, Elongation values and cross-sectional dimensions) // Typ der Messgeräte (Metadaten, Mess- und Prüfmittel, Dehnungswerte und Querschnittsabmessungen)""",
    )

    digital = VocabularyTerm(
        code="DIGITAL",
        label="Digital",
        description="""digital // digital""",
    )

    analog = VocabularyTerm(
        code="ANALOG",
        label="Analog",
        description="""analog // analog""",
    )

    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (specify)",
        description="""Other (specify) // andere (bitte angeben)""",
    )


class CreepTestDeterminationOfReferenceLength(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_DETERMINATION_OF_REFERENCE_LENGTH",
        description="""Determination of Reference Length - Case 1 or Case 2 (see description) // Bestimmung der Referenzlänge - Fall 1 oder Fall 2 (siehe Beschreibung) """,
    )

    case_1 = VocabularyTerm(
        code="CASE_1",
        label="Case 1",
        description="""Case 1 - Reference length for calculation of percentage extensions/elongations if the original gauge length Lo and/or extensometer Le are inside the parallel length, Lc. In this case Lr = Le (percentage extensions) or Lr = Lo (percentage elongations). // Fall 1 - Referenzlänge für die Berechnung der prozentualen Dehnungen/Verlängerungen, wenn die ursprüngliche Messlänge Lo und/oder der Dehnungsmesser Le innerhalb der parallelen Länge Lc liegen. In diesem Fall gilt Lr = Le (prozentuale Dehnungen) oder Lr = Lo (prozentuale Verlängerungen).
""",
    )

    case_2 = VocabularyTerm(
        code="CASE_2",
        label="Case 2",
        description="""Case 2 - Reference length for calculation of percentage extensions/elongations if the original gauge length Lo and/or extensometer Le are outside the parallel length, Lc. In this case, Lr, for calculation of percentage is corrected to consider the strain contributions of the shoulders/ridges.
 (Primary data, Test result, Values recorded at test start) // Fall 2 - Referenzlänge für die Berechnung der prozentualen Dehnungen/Verlängerungen, wenn die ursprüngliche Messlänge Lo und/oder der Dehnungsmesser Le außerhalb der parallelen Länge Lc liegen. In diesem Fall wird Lr für die Berechnung des Prozentsatzes korrigiert, um die Dehnungsbeiträge der Schultern/Kanten zu berücksichtigen.
 (Primärdaten, Prüfergebnis, Zu Testbeginn erfasste Werte)""",
    )


class CreepTestFracturePosition(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_FRACTURE_POSITION",
        description="""Fracture Position (Primary data, Test result, Values recorded after end of test) // Bruchposition (Primärdaten, Prüfergebnis, Nach Testende erfasste Werte)""",
    )

    centered = VocabularyTerm(
        code="CENTERED",
        label="Centered",
        description="""centered // mittig""",
    )

    within_the_gauge_length = VocabularyTerm(
        code="WITHIN_THE_GAUGE_LENGTH",
        label="Within the gauge length",
        description="""Within the gauge length // innerhalb der Messlänge""",
    )

    within_the_gauge_length_and_the_parallel_length = VocabularyTerm(
        code="WITHIN_THE_GAUGE_LENGTH_AND_THE_PARALLEL_LENGTH",
        label="Within the gauge length and the parallel length",
        description="""Within the gauge length and the parallel length // innerhalb der Messlänge und der parallelen Länge""",
    )

    at_the_edge_of_the_upper_extensometer_gauge_length = VocabularyTerm(
        code="AT_THE_EDGE_OF_THE_UPPER_EXTENSOMETER_GAUGE_LENGTH",
        label="At the edge of the upper extensometer gauge length",
        description="""At the edge of the upper extensometer gauge length // am Rand der oberen Extensometer-Messlänge""",
    )

    at_the_edge_of_the_lower_extensometer_gauge_length = VocabularyTerm(
        code="AT_THE_EDGE_OF_THE_LOWER_EXTENSOMETER_GAUGE_LENGTH",
        label="At the edge of the lower extensometer gauge length",
        description="""At the edge of the lower extensometer gauge length // am Rand der unteren Extensometer-Messlänge""",
    )

    at_the_edge_of_the_upper_parallel_length = VocabularyTerm(
        code="AT_THE_EDGE_OF_THE_UPPER_PARALLEL_LENGTH",
        label="At the edge of the upper parallel length",
        description="""At the edge of the upper parallel length // am Rand der oberen parallelen Länge""",
    )

    at_the_edge_of_the_lower_parallel_length = VocabularyTerm(
        code="AT_THE_EDGE_OF_THE_LOWER_PARALLEL_LENGTH",
        label="At the edge of the lower parallel length",
        description="""At the edge of the lower parallel length // am Rand der unteren parallelen Länge""",
    )

    outside_the_extensometer_gauge_length = VocabularyTerm(
        code="OUTSIDE_THE_EXTENSOMETER_GAUGE_LENGTH",
        label="Outside the extensometer gauge length",
        description="""Outside the extensometer gauge length // außerhalb der Extensometer-Messlänge""",
    )

    outside_extensometer_gauge_and_parallel_length = VocabularyTerm(
        code="OUTSIDE_EXTENSOMETER_GAUGE_AND_PARALLEL_LENGTH",
        label="Outside the extensometer the extensometer gauge length and the parallel length",
        description="""Outside the extensometer the extensometer gauge length and the parallel length // außerhalb der Extensometer-Messlänge und der parallelen Länge""",
    )


class CreepTestCalibrationStatus(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_CALIBRATION_STATUS",
        description="""Calibration status for creep-test instruments and measuring equipment // Kalibrierstatus für Kriechversuchsgeräte und Messmittel""",
    )
    calibrated = VocabularyTerm(
        code="CALIBRATED",
        label="Calibrated",
        description="""Calibrated // kalibriert""",
    )
    not_calibrated = VocabularyTerm(
        code="NOT_CALIBRATED",
        label="Not calibrated",
        description="""Not calibrated // nicht kalibriert""",
    )
    expired = VocabularyTerm(
        code="EXPIRED",
        label="Expired",
        description="""Calibration expired // Kalibrierung abgelaufen""",
    )
    unknown = VocabularyTerm(
        code="UNKNOWN",
        label="Unknown",
        description="""Unknown // unbekannt""",
    )
    not_applicable = VocabularyTerm(
        code="NOT_APPLICABLE",
        label="Not applicable",
        description="""Not applicable // nicht zutreffend""",
    )


class ThermocoupleType(VocabularyType):
    defs = VocabularyTypeDef(
        code="THERMOCOUPLE_TYPE",
        description="""Thermocouple type // Thermoelementtyp""",
    )
    type_k = VocabularyTerm(
        code="TYPE_K",
        label="Type K",
        description="""Type K // Typ K""",
    )
    type_n = VocabularyTerm(
        code="TYPE_N",
        label="Type N",
        description="""Type N // Typ N""",
    )
    type_s = VocabularyTerm(
        code="TYPE_S",
        label="Type S",
        description="""Type S // Typ S""",
    )
    type_r = VocabularyTerm(
        code="TYPE_R",
        label="Type R",
        description="""Type R // Typ R""",
    )
    other_specify = VocabularyTerm(
        code="OTHER_SPECIFY",
        label="Other (Specify)",
        description="""Other (Specify) // andere (bitte angeben)""",
    )


class CreepTestNumberOfThermocouples(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_NUMBER_OF_THERMOCOUPLES",
        description="""Number of thermocouples used in the creep-test temperature measurement // Anzahl der im Kriechversuch verwendeten Thermoelemente""",
    )
    one = VocabularyTerm(
        code="ONE",
        label="1",
        description="""One thermocouple // ein Thermoelement""",
    )
    two = VocabularyTerm(
        code="TWO",
        label="2",
        description="""Two thermocouples // zwei Thermoelemente""",
    )
    three = VocabularyTerm(
        code="THREE",
        label="3",
        description="""Three thermocouples // drei Thermoelemente""",
    )
