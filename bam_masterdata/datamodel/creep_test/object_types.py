from bam_masterdata.datamodel.object_types import (
    ComputationalAnalysis,
    EnvironmentalConditions,
    ExperimentalStep,
    Instrument,
    InstrumentAccessory,
    Sample,
    TestingMachine,
)
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.entities import ObjectType


class MechanicalTest(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST",
        description="""Mechanical test (experimental step) // Mechanischer Test (Versuchsschritt)""",
        generated_code_prefix="EXP.MECH_TEST",
    )


class CreepTest(MechanicalTest):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST",
        description="""Creep test (mechanical) // Kriechversuch (mechanisch)""",
        generated_code_prefix="EXP.MECH.CREEP",
    )

    # --- Links to related creep-test sub-objects (OBJECT properties) ---
    link_material_history_and_condition = PropertyTypeAssignment(
        code="CREEP_TEST_LINK_MATERIAL_HISTORY_AND_CONDITION",
        data_type="OBJECT",
        object_code="CREEP_TEST_MATERIAL_HISTORY_AND_CONDITION",
        property_label="Material history and condition",
        description="""Linked object: Material history and condition""",
        mandatory=False,
        section="Linked objects",
    )

    link_test_piece = PropertyTypeAssignment(
        code="CREEP_TEST_LINK_TEST_PIECE",
        data_type="OBJECT",
        object_code="SAMPLE.CREEP_TEST_TEST_PIECE",
        property_label="Test piece",
        description="""Linked object: Test piece""",
        mandatory=False,
        section="Linked objects",
    )

    link_test_machine = PropertyTypeAssignment(
        code="CREEP_TEST_LINK_TEST_MACHINE",
        data_type="OBJECT",
        object_code="TESTING_MACHINE.CREEP_TEST_TEST_MACHINE",
        property_label="Test machine",
        description="""Linked object: Test machine""",
        mandatory=False,
        section="Linked objects",
    )

    link_load_sensor = PropertyTypeAssignment(
        code="CREEP_TEST_LINK_LOAD_SENSOR",
        data_type="OBJECT",
        object_code="INSTRUMENT.CREEP_TEST_LOAD_SENSOR",
        property_label="Load sensor",
        description="""Linked object: Load sensor""",
        mandatory=False,
        section="Linked objects",
    )
    link_load_measuring_data_acquisition = PropertyTypeAssignment(
        code="CREEP_TEST_LINK_LOAD_MEASURING_DATA_ACQUISITION",
        data_type="OBJECT",
        object_code="CREEP_TEST_LOAD_DATA_ACQUISITION",
        property_label="Load measuring system data acquisition",
        description="""Linked object: Load measuring system data acquisition""",
        mandatory=False,
        section="Linked objects",
    )

    link_laboratory_conditions = PropertyTypeAssignment(
        code="CREEP_TEST_LINK_LABORATORY_CONDITIONS",
        data_type="OBJECT",
        object_code="ENVIRONMENTAL_CONDITIONS.CREEP_TEST_LABORATORY_CONDITIONS",
        property_label="Laboratory conditions",
        description="""Linked object: Laboratory conditions""",
        mandatory=False,
        section="Linked objects",
    )

    link_temperature_measuring_system = PropertyTypeAssignment(
        code="CREEP_TEST_LINK_TEMPERATURE_MEASURING_SYSTEM",
        data_type="OBJECT",
        object_code="INSTRUMENT.CREEP_TEST_TEMPERATURE_MEASURING_SYSTEM",
        property_label="Temperature-measuring system",
        description="""Linked object: Temperature-measuring system""",
        mandatory=False,
        section="Linked objects",
    )
    link_temperature_sensor = PropertyTypeAssignment(
        code="CREEP_TEST_LINK_TEMPERATURE_SENSOR",
        data_type="OBJECT",
        object_code="INSTRUMENT.CREEP_TEST_TEMPERATURE_SENSOR",
        property_label="Temperature sensor",
        description="""Linked object: Temperature sensor""",
        mandatory=False,
        section="Linked objects",
    )
    link_temperature_daq = PropertyTypeAssignment(
        code="CREEP_TEST_LINK_TEMPERATURE_DAQ",
        data_type="OBJECT",
        object_code="INSTRUMENT.CREEP_TEST_TEMPERATURE_DATA_ACQUISITION",
        property_label="Temperature DAQ",
        description="""Linked object: Temperature measuring system data acquisition""",
        mandatory=False,
        section="Linked objects",
    )

    link_extensometer_system = PropertyTypeAssignment(
        code="CREEP_TEST_LINK_EXTENSOMETER_SYSTEM",
        data_type="OBJECT",
        object_code="INSTRUMENT.CREEP_TEST_EXTENSOMETER_SYSTEM",
        property_label="Extensometer system",
        description="""Linked object: Extensometer system""",
        mandatory=False,
        section="Linked objects",
    )
    link_contacting_extensometer = PropertyTypeAssignment(
        code="CREEP_TEST_LINK_CONTACTING_EXTENSOMETER",
        data_type="OBJECT",
        object_code="INSTRUMENT.CREEP_TEST_EXTENSION_VALUES_CONTACTING_EXTENSOMETER",
        property_label="Contacting extensometer",
        description="""Linked object: Contacting extensometer""",
        mandatory=False,
        section="Linked objects",
    )

    link_elongation_cross_sectional = PropertyTypeAssignment(
        code="CREEP_TEST_LINK_ELONGATION_CROSS_SECTIONAL",
        data_type="OBJECT",
        object_code="INSTRUMENT.CREEP_TEST_ELONGATION_VALUES_AND_CROSS_SECTIONAL_DIMENSIONS",
        property_label="Elongation & cross-sectional dimensions",
        description="""Linked object: Elongation values and cross-sectional dimensions""",
        mandatory=False,
        section="Linked objects",
    )

    link_data_processing = PropertyTypeAssignment(
        code="CREEP_TEST_LINK_DATA_PROCESSING",
        data_type="OBJECT",
        object_code="COMPUTATIONAL_ANALYSIS.CREEP_TEST_DATA_PROCESSING_PROCEDURES",
        property_label="Data processing procedures",
        description="""Linked object: Data processing procedures""",
        mandatory=False,
        section="Linked objects",
    )

    link_primary_data_at_start = PropertyTypeAssignment(
        code="CREEP_TEST_LINK_PRIMARY_DATA_AT_START",
        data_type="OBJECT",
        object_code="CREEP_TEST_PRIMARY_VALUES_RECORDED_AT_TEST_START",
        property_label="Primary data at test start",
        description="""Linked object: Primary data (values at test start)""",
        mandatory=False,
        section="Linked objects",
    )
    link_primary_data_during_run = PropertyTypeAssignment(
        code="CREEP_TEST_LINK_PRIMARY_DATA_DURING_RUN",
        data_type="OBJECT",
        object_code="CREEP_TEST_VALUES_RECORDED_DURING_TEST_RUN_BASE.CREEP_TEST_PRIMARY_VALUES_RECORDED_DURING_TEST_RUN",
        property_label="Primary data during test run",
        description="""Linked object: Primary data (values during test run)""",
        mandatory=False,
        section="Linked objects",
    )
    link_primary_data_after_end = PropertyTypeAssignment(
        code="CREEP_TEST_LINK_PRIMARY_DATA_AFTER_END",
        data_type="OBJECT",
        object_code="CREEP_TEST_PRIMARY_VALUES_RECORDED_AFTER_END_OF_TEST",
        property_label="Primary data after end of test",
        description="""Linked object: Primary data (values after end of test)""",
        mandatory=False,
        section="Linked objects",
    )
    link_secondary_data_during_run = PropertyTypeAssignment(
        code="CREEP_TEST_LINK_SECONDARY_DATA_DURING_RUN",
        data_type="OBJECT",
        object_code="CREEP_TEST_VALUES_RECORDED_DURING_TEST_RUN_BASE.CREEP_TEST_SECONDARY_VALUES_RECORDED_DURING_TEST_RUN",
        property_label="Secondary data during test run",
        description="""Linked object: Secondary data (values during test run)""",
        mandatory=False,
        section="Linked objects",
    )

    link_secondary_elongation_values = PropertyTypeAssignment(
        code="CREEP_TEST_LINK_SECONDARY_ELONGATION_VALUES",
        data_type="OBJECT",
        object_code="CREEP_TEST_SECONDARY_ELONGATION_VALUES",
        property_label="Secondary elongation values",
        description="""Linked object: Secondary data (elongation values)""",
        mandatory=False,
        section="Linked objects",
    )
    link_secondary_extension_values = PropertyTypeAssignment(
        code="CREEP_TEST_LINK_SECONDARY_EXTENSION_VALUES",
        data_type="OBJECT",
        object_code="CREEP_TEST_SECONDARY_EXTENSION_VALUES",
        property_label="Secondary extension values",
        description="""Linked object: Secondary data (extension values)""",
        mandatory=False,
        section="Linked objects",
    )

    # ---------------------------
    # Section: Metadata - Test info - Test job details
    # ---------------------------
    creep_test_id = PropertyTypeAssignment(
        code="CREEP_TEST_ID",
        data_type="VARCHAR",
        property_label="Test ID",
        description="""Test ID // Prüf-ID""",
        mandatory=True,
        section="Test job details",
    )
    creep_test_project_id = PropertyTypeAssignment(
        code="CREEP_TEST_LINK_PROJECT",
        data_type="OBJECT",
        object_code="PROJECT",
        property_label="Project",
        description="""Linked object: Project associated with this creep test // Verknüpftes Objekt: Projekt, dem dieser Kriechversuch zugeordnet ist""",
        mandatory=False,
        section="Test job details",
    )

    # ---------------------------
    # Section: Metadata - Test info - Test parameters
    # ---------------------------
    creep_test_standard_applied = PropertyTypeAssignment(
        code="CREEP_TEST_STANDARD_APPLIED",
        data_type="BOOLEAN",
        property_label="Test standard applied?",
        description="""Test standard applied - Was the test performed according to a test standard? // Prüfnorm angewendet - Wurde die Prüfung gemäß einer Prüfnorm durchgeführt?""",
        mandatory=True,
        section="Test parameters",
    )
    creep_test_standard = PropertyTypeAssignment(
        code="CREEP_TEST_STANDARD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_STANDARD",
        property_label="Test standard",
        description="""Test standard // Prüfnorm""",
        mandatory=True,
        section="Test parameters",
    )
    creep_test_specified_temperature = PropertyTypeAssignment(
        code="TEMPERATURE_IN_KELVIN",
        data_type="REAL",
        property_label="Specified temperature",
        units="K",
        description="""Specified temperature // Vorgegebene Temperatur""",
        mandatory=True,
        section="Test parameters",
    )
    creep_test_type_of_loading = PropertyTypeAssignment(
        code="CREEP_TEST_TYPE_OF_LOADING",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_TYPE_OF_LOADING",
        property_label="Type of loading",
        description="""Type of loading // Art der Belastung""",
        mandatory=True,
        section="Test parameters",
    )
    creep_test_load_control_type = PropertyTypeAssignment(
        code="CREEP_TEST_LOAD_CONTROL_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_LOAD_CONTROL_TYPE",
        property_label="Load control type",
        description="""Load control type // Lastregelungsart""",
        mandatory=True,
        section="Test parameters",
    )
    creep_test_initial_stress = PropertyTypeAssignment(
        code="CREEP_TEST_INITIAL_STRESS",
        data_type="REAL",
        property_label="Initial stress",
        units="MPa",
        description="""Initial stress // Anfangsspannung""",
        mandatory=True,
        section="Test parameters",
    )
    creep_test_test_type = PropertyTypeAssignment(
        code="CREEP_TEST_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_TYPE",
        property_label="Test type",
        description="""Test type // Prüftyp""",
        mandatory=True,
        section="Test parameters",
    )
    creep_test_end_of_test_criterium = PropertyTypeAssignment(
        code="CREEP_TEST_END_OF_TEST_CRITERIUM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_END_OF_TEST_CRITERIUM",
        property_label="End of test criterium",
        description="""End of test criterium // Abbruchkriterium""",
        mandatory=True,
        section="Test parameters",
    )
    creep_test_time_limit = PropertyTypeAssignment(
        code="CREEP_TEST_TIME_LIMIT",
        data_type="REAL",
        property_label="Time Limit",
        units="h",
        description="""Time Limit // Zeitlimit""",
        mandatory=True,
        section="Test parameters",
    )
    creep_test_extension_limit = PropertyTypeAssignment(
        code="CREEP_TEST_EXTENSION_LIMIT",
        data_type="REAL",
        property_label="Extension Limit",
        units="%",
        description="""Extension Limit // Dehnungsgrenze""",
        mandatory=True,
        section="Test parameters",
    )
    creep_test_end_of_test = PropertyTypeAssignment(
        code="CREEP_TEST_END_OF_TEST",
        data_type="VARCHAR",
        property_label="End of test",
        description="""End of test - Describe the end of test if none of the preset criteria (time or extension limit) could be met // Testende - Beschreiben Sie das Testende, falls keines der vorgegebenen Kriterien (Zeit- oder Dehnungsgrenze) erreicht werden konnte.""",
        mandatory=False,
        section="Test parameters",
    )
    creep_test_interruption_course = PropertyTypeAssignment(
        code="CREEP_TEST_INTERRUPTION_COURSE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_INTERRUPTION_COURSE",
        property_label="Interruption course",
        description="""Interruption course // Unterbrechungsverlauf""",
        mandatory=True,
        section="Test parameters",
    )
    creep_test_test_force = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_FORCE",
        data_type="REAL",
        property_label="Test force",
        units="kN",
        description="""Test force // Prüfkraft""",
        mandatory=False,
        section="Test parameters",
    )
    creep_test_preload = PropertyTypeAssignment(
        code="CREEP_TEST_PRELOAD",
        data_type="REAL",
        property_label="Preload",
        units="kN",
        description="""Preload - Part of the test force // Vorspannkraft - Teil der Prüfkraft""",
        mandatory=True,
        section="Test parameters",
    )

    # --------------------------------
    # Section: Metadata - Test info - Related research outcome
    # --------------------------------
    creep_test_any_related_articles = PropertyTypeAssignment(
        code="CREEP_TEST_ANY_RELATED_ARTICLES",
        data_type="BOOLEAN",
        property_label="Any related articles?",
        description="""Any related articles? // Zugehörige Artikel vorhanden?""",
        mandatory=False,
        section="Related research outcome",
    )
    creep_test_related_article = PropertyTypeAssignment(
        code="CREEP_TEST_RELATED_ARTICLE",
        data_type="MULTILINE_VARCHAR",
        property_label="Related article",
        description="""Related article - Multiple input entries for instance for MSE research article DOI, Zenodo DOI, FDO // Zugehöriger Artikel - Mehrfache Eingaben, z. B. für DOI eines Fachartikels, Zenodo-DOI, FDO.""",
        mandatory=False,
        section="Related research outcome",
    )


class CreepTestMaterialHistoryAndCondition(ObjectType):
    defs = ObjectTypeDef(
        code="CREEP_TEST_MATERIAL_HISTORY_AND_CONDITION",
        description="""Material history and condition for creep tests // Materialhistorie und -zustand für Kriechversuche""",
        generated_code_prefix="CREEP_MATER_HISTO",
    )

    # --- Links to material sub-objects (OBJECT properties) ---
    link_chemical_composition_nominal = PropertyTypeAssignment(
        code="CREEP_TEST_MATERIAL_LINK_CHEMICAL_COMPOSITION_NOMINAL",
        data_type="OBJECT",
        object_code="CREEP_TEST_CHEMICAL_COMPOSITION_NOMINAL",
        property_label="Chemical composition (nominal)",
        description="""Linked object: Chemical composition (nominal)""",
        mandatory=False,
        section="Linked material objects",
    )
    link_chemical_composition_measured = PropertyTypeAssignment(
        code="CREEP_TEST_MATERIAL_LINK_CHEMICAL_COMPOSITION_MEASURED",
        data_type="OBJECT",
        object_code="CREEP_TEST_CHEMICAL_COMPOSITION_MEASURED",
        property_label="Chemical composition (measured)",
        description="""Linked object: Chemical composition (measured)""",
        mandatory=False,
        section="Linked material objects",
    )
    link_ndt_results = PropertyTypeAssignment(
        code="CREEP_TEST_MATERIAL_LINK_NDT_RESULTS",
        data_type="OBJECT",
        object_code="CREEP_TEST_MATERIAL_HISTORY_NDT_RESULTS",
        property_label="NDT results",
        description="""Linked object: NDT results""",
        mandatory=False,
        section="Linked material objects",
    )
    link_mechanical_tests_results = PropertyTypeAssignment(
        code="CREEP_TEST_MATERIAL_LINK_MECHANICAL_TESTS_RESULTS",
        data_type="OBJECT",
        object_code="CREEP_TEST_MATERIAL_HISTORY_MECHANICAL_TESTS_RESULTS",
        property_label="Mechanical tests results",
        description="""Linked object: Mechanical tests results""",
        mandatory=False,
        section="Linked material objects",
    )

    # --------------------------------
    # Section: Metadata - Material history and condition
    # --------------------------------
    creep_test_material_identifier = PropertyTypeAssignment(
        code="CREEP_TEST_MATERIAL_IDENTIFIER",
        data_type="VARCHAR",
        property_label="Material Identifier",
        description="""Material Identifier - E.g., NIMONIC 75, 2.4630, CMSX-6, CMSX-4, ERBO1, // Materialkennung - z. B. NIMONIC 75, 2.4630, CMSX-6, CMSX-4, ERBO1,""",
        mandatory=True,
        section="Material history and condition",
    )

    # --------------------------------
    # Section: As-manufactured material
    # --------------------------------
    creep_test_phase_transformation_during_test = PropertyTypeAssignment(
        code="CREEP_TEST_PHASE_TRANSFORMATION_DURING_TEST",
        data_type="BOOLEAN",
        property_label="Phase transformation during test?",
        description="""Phase transformation during test? // Phasenumwandlung während der Prüfung?""",
        mandatory=False,
        section="As-manufactured material",
    )
    creep_test_possible_phase_transformation = PropertyTypeAssignment(
        code="CREEP_TEST_POSSIBLE_PHASE_TRANSFORMATION",
        data_type="VARCHAR",
        property_label="Possible phase transformation",
        description="""Possible phase transformation - Is any phase transformation expected due to temperature during the creep test?. Please provide any supporting material if possible. Answers could be, e.g., a link to a TTT-curve or a DOI of an article // Mögliche Phasenumwandlung - Wird aufgrund der Temperatur während des Kriechversuchs eine Phasenumwandlung erwartet? Bitte fügen Sie nach Möglichkeit unterstützendes Material bei (z. B. Link zu einer ZTU-/TTT-Kurve oder DOI eines Artikels).""",
        mandatory=False,
        section="As-manufactured material",
    )
    creep_test_form_of_as_manufactured_material = PropertyTypeAssignment(
        code="CREEP_TEST_FORM_OF_AS_MANUFACTURED_MATERIAL",
        data_type="VARCHAR",
        property_label="Form of as-manufactured material",
        description="""Form of as-manufactured material - E.g., Cast, Ingot, Extrusion rod, // Form des Materials im Herstellungszustand - z. B. Guss, Block (Ingot), Extrusionsstab,""",
        mandatory=True,
        section="As-manufactured material",
    )
    creep_test_geometry_size_as_manufactured_material = PropertyTypeAssignment(
        code="CREEP_TEST_GEOMETRY_SIZE_AS_MANUFACTURED_MATERIAL",
        data_type="VARCHAR",
        property_label="Geometry/size as-manufactured material",
        description="""Geometry/size as-manufactured material - Please provide a description or/and any supporting material, e.g., link to image or technical drawing, if possible. // Geometrie/Abmessungen des Materials im Herstellungszustand - Bitte geben Sie eine Beschreibung und/oder nach Möglichkeit unterstützendes Material an (z. B. Link zu einem Bild oder einer technischen Zeichnung).""",
        mandatory=True,
        section="As-manufactured material",
    )
    creep_test_manufacturing_process_description_as_manufactured_material = PropertyTypeAssignment(
        code="CREEP_TEST_MANUFACTURING_PROCESS_DESCRIPTION_AS_MANUFACTURED_MATERIAL",
        data_type="VARCHAR",
        property_label="Manufacturing process description as-manufactured material",
        description="""Manufacturing process description as-manufactured material - E.g., Cast / Melting, Casting, and Remelting / Induction melting in air, casting into a circular ingot and then electroslag remelting // Beschreibung des Herstellungsprozesses (Herstellungszustand) - z. B. Guss / Schmelzen, Gießen und Umschmelzen / Induktionsschmelzen in Luft, Gießen in einen Rundblock und anschließend Elektroschlacke-Umschmelzen""",
        mandatory=False,
        section="As-manufactured material",
    )
    creep_test_casting_temperature = PropertyTypeAssignment(
        code="CREEP_TEST_CASTING_TEMPERATURE",
        data_type="REAL",
        property_label="Casting temperature",
        units="degC",
        description="""Casting temperature in degrees Celsius // Gießtemperatur in Grad Celsius""",
        mandatory=False,
        section="As-manufactured material",
    )
    creep_test_casting_speed = PropertyTypeAssignment(
        code="CREEP_TEST_CASTING_SPEED",
        data_type="REAL",
        property_label="Casting speed",
        description="""Casting speed // Gießgeschwindigkeit""",
        mandatory=False,
        section="As-manufactured material",
    )
    creep_test_solidification = PropertyTypeAssignment(
        code="CREEP_TEST_SOLIDIFICATION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_SOLIDIFICATION",
        property_label="Solidification",
        description="""Solidification - Single/Polycrystal solidified? // Erstarrungsform - Einkristallin oder polykristallin erstarrt?""",
        mandatory=True,
        section="As-manufactured material",
    )
    creep_test_condition = PropertyTypeAssignment(
        code="CREEP_TEST_CONDITION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_CONDITION",
        property_label="Condition",
        description="""Condition // Zustand""",
        mandatory=True,
        section="As-manufactured material",
    )

    # --------------------------------
    # Section: As-tested material
    # --------------------------------
    creep_test_supplier = PropertyTypeAssignment(
        code="SUPPLIER",
        data_type="VARCHAR",
        property_label="Supplier",
        description="""Supplier // Lieferant""",
        mandatory=True,
        section="As-tested material",
    )
    creep_test_geometry_size_as_tested_material = PropertyTypeAssignment(
        code="CREEP_TEST_GEOMETRY_SIZE_AS_TESTED_MATERIAL",
        data_type="VARCHAR",
        property_label="Geometry/size as-tested material",
        description="""Geometry/size as-tested material - The test piece is manufactured from the as-tested material. Please add a description or a link to Image or technical drawing. The as-tested material is the material to be tested. The as-tested material can be a component. // Geometrie/Abmessungen des Materials im Prüfzustand - Der Probekörper wird aus dem Material im Prüfzustand gefertigt. Bitte fügen Sie eine Beschreibung oder einen Link zu Bild/technischer Zeichnung hinzu. Das Material im Prüfzustand ist das zu prüfende Material und kann auch ein Bauteil sein.""",
        mandatory=True,
        section="As-tested material",
    )
    creep_test_manufacturing_process_description_as_tested_material = PropertyTypeAssignment(
        code="CREEP_TEST_MANUFACTURING_PROCESS_DESCRIPTION_AS_TESTED_MATERIAL",
        data_type="VARCHAR",
        property_label="Manufacturing process description as-tested material",
        description="""Manufacturing process description as-tested material // Beschreibung des Herstellungsprozesses (Prüfzustand)""",
        mandatory=True,
        section="As-tested material",
    )
    creep_test_supply_date = PropertyTypeAssignment(
        code="SAMPLE_RECEIVED",
        data_type="TIMESTAMP",
        property_label="Supply Date",
        description="""Supply Date // Lieferdatum""",
        mandatory=True,
        section="As-tested material",
    )
    creep_test_order_number = PropertyTypeAssignment(
        code="WORKSHOP_ORDER_ID",
        data_type="VARCHAR",
        property_label="Order number",
        description="""Workshop/Order identifier (free text)""",
        mandatory=False,
        section="As-tested material",
    )

    # --------------------------------
    # Section: Heat treatment
    # --------------------------------
    creep_test_heat_treatment_state = PropertyTypeAssignment(
        code="CREEP_TEST_HEAT_TREATMENT_STATE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_HEAT_TREATMENT_STATE",
        property_label="Heat treatment - State",
        description="""Heat treatment - State // Wärmebehandlungszustand""",
        mandatory=True,
        section="Heat treatment",
    )
    creep_test_multistage_annealing = PropertyTypeAssignment(
        code="CREEP_TEST_MULTISTAGE_ANNEALING",
        data_type="BOOLEAN",
        property_label="Multistage annealing?",
        description="""Multistage annealing? // Mehrstufiges Glühen?""",
        mandatory=False,
        section="Heat treatment",
    )
    creep_test_multistage_ageing = PropertyTypeAssignment(
        code="CREEP_TEST_MULTISTAGE_AGEING",
        data_type="BOOLEAN",
        property_label="Multistage ageing?",
        description="""Multistage ageing? // Mehrstufiges Auslagern?""",
        mandatory=False,
        section="Heat treatment",
    )
    creep_test_heat_treatment_annealing_description = PropertyTypeAssignment(
        code="CREEP_TEST_HEAT_TREATMENT_ANNEALING_DESCRIPTION",
        data_type="VARCHAR",
        property_label="Heat treatment - Annealing - Description",
        description="""Heat treatment - Annealing - Description // Wärmebehandlung - Glühen - Beschreibung""",
        mandatory=True,
        section="Heat treatment",
    )
    creep_test_heat_treatment_ageing_description = PropertyTypeAssignment(
        code="CREEP_TEST_HEAT_TREATMENT_AGEING_DESCRIPTION",
        data_type="VARCHAR",
        property_label="Heat treatment - Ageing - Description",
        description="""Heat treatment - Ageing - Description // Wärmebehandlung - Auslagern - Beschreibung""",
        mandatory=True,
        section="Heat treatment",
    )
    creep_test_heat_treatment_protocol = PropertyTypeAssignment(
        code="CREEP_TEST_HEAT_TREATMENT_PROTOCOL",
        data_type="VARCHAR",
        property_label="Heat treatment - Protocol",
        description="""Heat treatment - Protocol - Link to file, preferably with machine-readable (meta)dataeta),
    data // Wärmebehandlung - Protokoll - Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=False,
        section="Heat treatment",
    )

    # --------------------------------
    # Section: Microstructure
    # --------------------------------
    creep_test_microstructure_feature = PropertyTypeAssignment(
        code="CREEP_TEST_MICROSTRUCTURE_FEATURE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_MICROSTRUCTURE_FEATURE",
        property_label="Microstructure feature",
        description="""Microstructure feature // Mikrostrukturmerkmal""",
        mandatory=True,
        section="Microstructure",
    )
    creep_test_characterization_method = PropertyTypeAssignment(
        code="CREEP_TEST_CHARACTERIZATION_METHOD",
        data_type="VARCHAR",
        property_label="Characterization method",
        description="""Characterization method - E.g., STEM, HRTEM, TEM-EDX, AFM, SEM, SEM-EBSD, .... // Charakterisierungsmethode - z. B. STEM, HRTEM, TEM-EDX, AFM, SEM, SEM-EBSD, …""",
        mandatory=True,
        section="Microstructure",
    )
    creep_test_measured_condition = PropertyTypeAssignment(
        code="CREEP_TEST_MEASURED_CONDITION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_MEASURED_CONDITION",
        property_label="Measured condition",
        description="""Measured condition - E.g., as-manufactured, heat-treated, before testing, after testing // Gemessener Zustand - z. B. wie hergestellt, wärmebehandelt, vor der Prüfung, nach der Prüfung""",
        mandatory=True,
        section="Microstructure",
    )
    creep_test_measuring_position = PropertyTypeAssignment(
        code="CREEP_TEST_MEASURING_POSITION",
        data_type="VARCHAR",
        property_label="Measuring position",
        description="""Measuring position - Specify position(s) for bulk (middle/top/bottom/surface) and/or microstructure feature (matrix, interdendtitic region, phase,...) // Messposition - Geben Sie Position(en) an, z. B. im Volumen (Mitte/oben/unten/Oberfläche) und/oder bezogen auf das Mikrostrukturmerkmal (Matrix, interdendritischer Bereich, Phase, …).""",
        mandatory=True,
        section="Microstructure",
    )
    creep_test_microstructure_feature_information = PropertyTypeAssignment(
        code="CREEP_TEST_MICROSTRUCTURE_FEATURE_INFORMATION",
        data_type="VARCHAR",
        property_label="Microstructure feature - Information",
        description="""Microstructure feature - Information - Include all relevant characterization results // Mikrostrukturmerkmal - Informationen - Führen Sie alle relevanten Charakterisierungsergebnisse auf.""",
        mandatory=False,
        section="Microstructure",
    )
    creep_test_microstructure_image = PropertyTypeAssignment(
        code="CREEP_TEST_MICROSTRUCTURE_IMAGE",
        data_type="VARCHAR",
        property_label="Microstructure Image",
        description="""Microstructure Image - Link to File, e.g., an optical micrograph, preferably with machine-readable (meta)data // Mikrostrukturbild - Link zu einer Datei, z. B. zu einem optischen Mikrographen, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=False,
        section="Microstructure",
    )
    creep_test_microstructure_report = PropertyTypeAssignment(
        code="CREEP_TEST_MICROSTRUCTURE_REPORT",
        data_type="VARCHAR",
        property_label="Microstructure report",
        description="""Microstructure report - Link to file, preferably with machine-readable (meta)data // Mikrostrukturbericht - Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=False,
        section="Microstructure",
    )
    creep_test_grain_size = PropertyTypeAssignment(
        code="CREEP_TEST_GRAIN_SIZE",
        data_type="REAL",
        property_label="Grain size",
        units="µm",
        description="""Grain size - If polycrystal // Korngröße [µm] - Falls polykristallin.""",
        mandatory=True,
        section="Microstructure",
    )
    creep_test_grain_size_determination_method = PropertyTypeAssignment(
        code="CREEP_TEST_GRAIN_SIZE_DETERMINATION_METHOD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_GRAIN_SIZE_DETERMINATION_METHOD",
        property_label="Grain size - Determination method",
        description="""Grain size - Determination method // Korngröße - Bestimmungsmethode""",
        mandatory=True,
        section="Microstructure",
    )
    creep_test_grain_size_measuring_region = PropertyTypeAssignment(
        code="CREEP_TEST_GRAIN_SIZE_MEASURING_REGION",
        data_type="VARCHAR",
        property_label="Grain size - measuring region",
        description="""Grain size - measuring region - E.g., in the bulk // Korngröße - Messbereich - z. B. im Volumen""",
        mandatory=True,
        section="Microstructure",
    )
    creep_test_grain_size_distribution = PropertyTypeAssignment(
        code="CREEP_TEST_GRAIN_SIZE_DISTRIBUTION",
        data_type="VARCHAR",
        property_label="Grain size distribution",
        description="""Grain size distribution - Link to file, preferably with machine-readable (meta)data // Korngrößenverteilung - Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=False,
        section="Microstructure",
    )
    creep_test_grain_additional_information = PropertyTypeAssignment(
        code="CREEP_TEST_GRAIN_ADDITIONAL_INFORMATION",
        data_type="VARCHAR",
        property_label="Grain - Additional Information",
        description="""Grain - Additional Information - Include all further relevant characterization results // Korn - Zusätzliche Informationen - Führen Sie weitere relevante Charakterisierungsergebnisse auf.""",
        mandatory=False,
        section="Microstructure",
    )
    creep_test_reprecipitated_gamma_gamma_prime_regions = PropertyTypeAssignment(
        code="CREEP_TEST_REPRECIPITATED_GAMMA_GAMMA_PRIME_REGIONS",
        data_type="VARCHAR",
        property_label="Reprecipitated gamma-gamma prime regions",
        units="%",
        description="""Reprecipitated gamma-gamma prime regions - Completely dissolved and re-precipitated gamma-gamma' regions // Wieder ausgeschiedene Gamma/Gamma-Bereiche [%] - Vollständig gelöste und wieder ausgeschiedene Gamma/Gamma-Bereiche""",
        mandatory=False,
        section="Microstructure",
    )
    creep_test_gamma_prime_particles_average_size = PropertyTypeAssignment(
        code="CREEP_TEST_GAMMA_PRIME_PARTICLES_AVERAGE_SIZE",
        data_type="VARCHAR",
        property_label="Gamma prime particles - average size",
        units="µm",
        description="""Gamma prime particles - average size // Gamma-Partikel - mittlere Größe [µm]""",
        mandatory=False,
        section="Microstructure",
    )
    creep_test_gamma_prime_particles_maximum_size = PropertyTypeAssignment(
        code="CREEP_TEST_GAMMA_PRIME_PARTICLES_MAXIMUM_SIZE",
        data_type="REAL",
        property_label="Gamma prime particles - maximum size",
        units="µm",
        description="""Gamma prime particles - maximum size // Gamma-Partikel - maximale Größe [µm]""",
        mandatory=False,
        section="Microstructure",
    )
    creep_test_dendrite_spacings = PropertyTypeAssignment(
        code="CREEP_TEST_DENDRITE_SPACINGS",
        data_type="VARCHAR",
        property_label="Dendrite spacings",
        description="""Dendrite spacings - Please describe the procedure and add a link to file, preferably with machine-readable (meta)data or add a reference to paper and section // Dendritenabstände - Bitte beschreiben Sie das Verfahren und fügen Sie einen Dateilink (vorzugsweise mit maschinenlesbaren (Meta-)Daten) oder eine Referenz auf Publikation und Abschnitt hinzu.""",
        mandatory=False,
        section="Microstructure",
    )
    creep_test_proof_of_single_crystallinity = PropertyTypeAssignment(
        code="CREEP_TEST_PROOF_OF_SINGLE_CRYSTALLINITY",
        data_type="VARCHAR",
        property_label="Proof of single crystallinity",
        description="""Proof of single crystallinity - Link to file, preferably with machine-readable (meta)data // Nachweis der Einkristallinität - Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=False,
        section="Microstructure",
    )
    creep_test_single_crystal_orientation = PropertyTypeAssignment(
        code="CREEP_TEST_SINGLE_CRYSTAL_ORIENTATION",
        data_type="VARCHAR",
        property_label="Single crystal orientation",
        description="""Single crystal orientation - Link to file, preferably with machine-readable (meta)data. Laue Crystal Verification. Must be documented for each test piece. // Einkristallorientierung - Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten. Laue-Einkristallprüfung; muss für jeden Probekörper dokumentiert werden.""",
        mandatory=True,
        section="Microstructure",
    )
    creep_test_single_crystal_orientation_determination_method = PropertyTypeAssignment(
        code="CREEP_TEST_SINGLE_CRYSTAL_ORIENTATION_DETERMINATION_METHOD",
        data_type="VARCHAR",
        property_label="Single crystal orientation - Determination method",
        description="""Single crystal orientation - Determination method // Einkristallorientierung - Bestimmungsmethode""",
        mandatory=True,
        section="Microstructure",
    )
    creep_test_single_crystal_orientation_measuring_point = PropertyTypeAssignment(
        code="CREEP_TEST_SINGLE_CRYSTAL_ORIENTATION_MEASURING_POINT",
        data_type="VARCHAR",
        property_label="Single crystal orientation - Measuring point",
        description="""Single crystal orientation - Measuring point // Einkristallorientierung - Messpunkt""",
        mandatory=True,
        section="Microstructure",
    )
    creep_test_orientation_determination_accuracy = PropertyTypeAssignment(
        code="CREEP_TEST_ORIENTATION_DETERMINATION_ACCURACY",
        data_type="VARCHAR",
        property_label="Orientation - Determination accuracy",
        description="""Orientation - Determination accuracy // Orientierung - Bestimmungsgenauigkeit""",
        mandatory=False,
        section="Microstructure",
    )


class CreepTestChemicalCompositionNominal(ObjectType):
    defs = ObjectTypeDef(
        code="CREEP_TEST_CHEMICAL_COMPOSITION_NOMINAL",
        description="""Material history and condition / Chemical composition (NOMINAL) // Materialhistorie und Zustand / Chemische Zusammensetzung (NOMINAL)""",
        generated_code_prefix="CREEP_CHEMI_COMPO",
    )

    creep_test_measured_condition = PropertyTypeAssignment(
        code="CREEP_TEST_MEASURED_CONDITION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_MEASURED_CONDITION",
        property_label="Measured condition",
        description="""Measured condition // Gemessener Zustand""",
        mandatory=True,
        section="Chemical composition",
    )
    creep_test_measuring_position = PropertyTypeAssignment(
        code="CREEP_TEST_MEASURING_POSITION",
        data_type="VARCHAR",
        property_label="Measuring position",
        description="""Measuring position - Specify position(s) for bulk (middle/top/bottom/surface) and/or microstructure feature (matrix, interdendtitic region, phase,...) // Messposition - Geben Sie Position(en) an, z. B. im Volumen (Mitte/oben/unten/Oberfläche) und/oder bezogen auf das Mikrostrukturmerkmal (Matrix, interdendritischer Bereich, Phase, ...).""",
        mandatory=True,
        section="Chemical composition",
    )
    creep_test_measurement_method = PropertyTypeAssignment(
        code="CREEP_TEST_MEASUREMENT_METHOD",
        data_type="VARCHAR",
        property_label="Measurement method",
        description="""Measurement method - Provide a description of the used method(s) and details about measurement volume/points // Messmethode - Beschreiben Sie die verwendete(n) Methode(n) und geben Sie Details zu Messvolumen/-punkten an.""",
        mandatory=True,
        section="Chemical composition",
    )
    creep_test_chemical_composition_nominal = PropertyTypeAssignment(
        code="CHEM_SPECIES_BY_COMP_IN_PCT",
        data_type="VARCHAR",
        property_label="Chemical composition - nominal [wt.-% / at.-%]",
        units="%",
        description="""Chemical composition - nominal - Link to file, preferably with machine-readable (meta)data or add the wt.-% value of for each element // Chemische Zusammensetzung - nominal [wt.-% / at.-%] - Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten, oder geben Sie für jedes Element den Gewichts-%-Wert an.""",
        mandatory=True,
        section="Chemical composition",
    )


class CreepTestChemicalCompositionMeasured(ObjectType):
    defs = ObjectTypeDef(
        code="CREEP_TEST_CHEMICAL_COMPOSITION_MEASURED",
        description="""Material history and condition / Chemical composition (MEASURED) // Materialhistorie und Zustand / Chemische Zusammensetzung (MEASURED)""",
        generated_code_prefix="CREEP_CHEMI_COMPO",
    )

    creep_test_measured_condition = PropertyTypeAssignment(
        code="CREEP_TEST_MEASURED_CONDITION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_MEASURED_CONDITION",
        property_label="Measured condition",
        description="""Measured condition // Gemessener Zustand""",
        mandatory=True,
        section="Chemical composition",
    )
    creep_test_measuring_position = PropertyTypeAssignment(
        code="CREEP_TEST_MEASURING_POSITION",
        data_type="VARCHAR",
        property_label="Measuring position",
        description="""Measuring position - Specify position(s) for bulk (middle/top/bottom/surface) and/or microstructure feature (matrix, interdendtitic region, phase,...) // Messposition - Geben Sie Position(en) an, z. B. im Volumen (Mitte/oben/unten/Oberfläche) und/oder bezogen auf das Mikrostrukturmerkmal (Matrix, interdendritischer Bereich, Phase, ...).""",
        mandatory=True,
        section="Chemical composition",
    )
    creep_test_measurement_method = PropertyTypeAssignment(
        code="CREEP_TEST_MEASUREMENT_METHOD",
        data_type="VARCHAR",
        property_label="Measurement method",
        description="""Measurement method - Provide a description of the used method(s) and details about measurement volume/points // Messmethode - Beschreiben Sie die verwendete(n) Methode(n) und geben Sie Details zu Messvolumen/-punkten an.""",
        mandatory=True,
        section="Chemical composition",
    )
    creep_test_chemical_composition_measured = PropertyTypeAssignment(
        code="CHEM_SPECIES_BY_COMP_IN_PCT",
        data_type="VARCHAR",
        property_label="Chemical composition - measured [wt.-% / at.-%]",
        units="%",
        description="""Chemical composition - measured - Include precision, if available. Link to file, preferably with machine-readable (meta)data or add the wt.-% value of for each element // Chemische Zusammensetzung - gemessen [wt.-% / at.-%] - Geben Sie, falls verfügbar, die Präzision an. Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten, oder geben Sie für jedes Element den Gewichts-%-Wert an.""",
        mandatory=True,
        section="Chemical composition",
    )


class CreepTestMaterialHistoryNDTResults(ObjectType):
    defs = ObjectTypeDef(
        code="CREEP_TEST_MATERIAL_HISTORY_NDT_RESULTS",
        description="""Material history and condition / NDT Results // Materialhistorie und Zustand / ZfP-Ergebnisse""",
        generated_code_prefix="CREEP_MATER_HISTO_NDT_RES",
    )

    creep_test_crack_or_defect_inspection_method = PropertyTypeAssignment(
        code="CREEP_TEST_CRACK_OR_DEFECT_INSPECTION_METHOD",
        data_type="VARCHAR",
        property_label="Crack or defect inspection - Method",
        description="""Crack or defect inspection - Method - E.g., Penetrant certification/Radiographic certification/XCT/X-Ray film. Link to file, preferably with machine-readable (meta)data // Riss- oder Defektprüfung - Methode - z. B. Farbeindringprüfung / Röntgenprüfung / XCT / Röntgenfilm. Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=False,
        section="NDT Results",
    )
    creep_test_crack_or_defect_inspection_result = PropertyTypeAssignment(
        code="CREEP_TEST_CRACK_OR_DEFECT_INSPECTION_RESULT",
        data_type="VARCHAR",
        property_label="Crack or defect inspection - Result",
        description="""Crack or defect inspection - Result // Riss- oder Defektprüfung - Ergebnis""",
        mandatory=False,
        section="NDT Results",
    )


class CreepTestMaterialHistoryMechanicalTestsResults(ObjectType):
    defs = ObjectTypeDef(
        code="CREEP_TEST_MATERIAL_HISTORY_MECHANICAL_TESTS_RESULTS",
        description="""Material history and condition / Mechanical tests results // Materialhistorie und Zustand / Ergebnisse mechanischer Prüfungen""",
        generated_code_prefix="CREEP_MATER_HISTO_MECH_TEST_RES",
    )

    creep_test_proof_strength_room_temperature = PropertyTypeAssignment(
        code="CREEP_TEST_PROOF_STRENGTH_ROOM_TEMPERATURE",
        data_type="REAL",
        property_label="Proof strength - room temperature",
        units="MPa",
        description="""Proof strength - room temperature - 0.2 % Proof strength at room temperature // Streckgrenze - Raumtemperatur [MPa] - 0,2-%-Dehngrenze bei Raumtemperatur.""",
        mandatory=False,
        section="Mechanical tests results",
    )
    creep_test_proof_strength_creep_test_temperature = PropertyTypeAssignment(
        code="CREEP_TEST_PROOF_STRENGTH_CREEP_TEST_TEMPERATURE",
        data_type="REAL",
        property_label="Proof strength - creep test temperature",
        units="MPa",
        description="""Proof strength - creep test temperature - 0.2 % Proof strength at creep test temperature // Streckgrenze - Kriechprüftemperatur [MPa] - 0,2-%-Dehngrenze bei Kriechprüftemperatur.""",
        mandatory=False,
        section="Mechanical tests results",
    )
    creep_test_hardness = PropertyTypeAssignment(
        code="CREEP_TEST_HARDNESS",
        data_type="VARCHAR",
        property_label="Hardness",
        description="""Hardness // Härte""",
        mandatory=False,
        section="Mechanical tests results",
    )


class CreepTestTestPiece(Sample):
    defs = ObjectTypeDef(
        code="SAMPLE.CREEP_TEST_TEST_PIECE",
        description="""Test piece // Probekörper""",
        generated_code_prefix="SAMPL.CREEP_PIECE",
    )

    creep_test_test_piece_id = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_PIECE_ID",
        data_type="VARCHAR",
        property_label="Test piece ID",
        description="""Test piece ID // Probekörper-ID""",
        mandatory=False,
        section="Test piece",
    )
    creep_test_workshop_order_id = PropertyTypeAssignment(
        code="WORKSHOP_ORDER_ID",
        data_type="VARCHAR",
        property_label="Workshop order ID",
        description="""Workshop/Order identifier (free text)""",
        mandatory=False,
        section="Test piece",
    )
    creep_test_test_piece_history = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_PIECE_HISTORY",
        data_type="VARCHAR",
        property_label="Test piece history",
        description="""Test piece history - Link to file, preferably with machine-readable (meta)data. The file(s) can include, e.g., data or documentation from previous experiments. // Probekörperhistorie - Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten. Die Datei(en) können z. B. Daten oder Dokumentationen aus früheren Experimenten enthalten.""",
        mandatory=False,
        section="Test piece",
    )
    creep_test_test_piece_type_i = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_PIECE_TYPE_I",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_TEST_PIECE_TYPE_I",
        property_label="Test piece type I",
        description="""Test piece type I // Probekörpertyp I""",
        mandatory=True,
        section="Test piece",
    )
    creep_test_test_piece_type_ii = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_PIECE_TYPE_II",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_TEST_PIECE_TYPE_II",
        property_label="Test piece type II",
        description="""Test piece type II // Probekörpertyp II""",
        mandatory=True,
        section="Test piece",
    )
    creep_test_test_piece_type_iii = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_PIECE_TYPE_III",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_TEST_PIECE_TYPE_III",
        property_label="Test piece type III",
        description="""Test piece type III // Probekörpertyp III""",
        mandatory=True,
        section="Test piece",
    )
    creep_test_test_piece_technical_drawing = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_PIECE_TECHNICAL_DRAWING",
        data_type="VARCHAR",
        property_label="Test piece technical drawing",
        description="""Test piece technical drawing - Link to file, preferably with machine-readable (meta)data // Technische Zeichnung des Probekörpers - Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=True,
        section="Test piece",
    )
    creep_test_test_piece_origin_and_orientation = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_PIECE_ORIGIN_AND_ORIENTATION",
        data_type="VARCHAR",
        property_label="Test piece origin and orientation",
        description="""Test piece origin and orientation - Describe the exact location / positioning of the test piece within the as-tested material. E.g.: Do rolling direction and the longitudinal axis coincide?. Is the test piece located on top or bottom. Do coordinate systems of as-tested material and test piece coincide?. Add a link to a file, e.g., a technical drawing showing this, preferably with machine-readable (meta)data. // Herkunft und Orientierung des Probekörpers - Beschreiben Sie die genaue Lage/Positionierung des Probekörpers im Material im Prüfzustand. z. B.: Stimmen Walzrichtung und Längsachse überein? Liegt der Probekörper oben oder unten? Stimmen die Koordinatensysteme von Material (Prüfzustand) und Probekörper überein? Fügen Sie nach Möglichkeit einen Dateilink (z. B. technische Zeichnung) mit maschinenlesbaren (Meta-)Daten hinzu.""",
        mandatory=True,
        section="Test piece",
    )
    creep_test_test_piece_orientation_in_test_machine = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_PIECE_ORIENTATION_IN_TEST_MACHINE",
        data_type="VARCHAR",
        property_label="Test piece orientation in test machine",
        description="""Test piece orientation in test machine - Describe the exact orientation of the test piece within the test machine. E.g., is the longitudinal axis of the test piece exactly parallel to the loading axis of the test machine?. Add a link to a file providing evidence, preferably with machine-readable (meta)data. This can be, e.g., a technical drawing. // Orientierung des Probekörpers in der Prüfmaschine - Describe the exact orientation of the test piece within the test machine. E.g., is the longitudinal axis of the test piece exactly parallel to the loading axis of the test machine?. Add a link to a file providing evidence, preferably with machine-readable (meta)data. This can be, e.g., a technical drawing.""",
        mandatory=True,
        section="Test piece",
    )
    creep_test_additional_information_test_piece = PropertyTypeAssignment(
        code="CREEP_TEST_ADDITIONAL_INFORMATION_TEST_PIECE",
        data_type="VARCHAR",
        property_label="Additional information test piece",
        description="""Additional information test piece - Add the information or a link to file, preferably with machine-readable (meta)data, e.g., Roughness // Zusätzliche Informationen zum Probekörper - Fügen Sie die Information oder einen Dateilink hinzu, vorzugsweise mit maschinenlesbaren (Meta-)Daten, z. B. Rauheit.""",
        mandatory=False,
        section="Test piece",
    )


class CreepTestTestMachine(TestingMachine):
    defs = ObjectTypeDef(
        code="TESTING_MACHINE.CREEP_TEST_TEST_MACHINE",
        description="""Measuring and test equipment / Test machine // Mess- und Prüfmittel / Prüfmaschine""",
        generated_code_prefix="TM.CREEP_MACHI",
    )

    # --- Links to test machine sub-systems (OBJECT properties) ---
    link_heating_system = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_MACHINE_LINK_HEATING_SYSTEM",
        data_type="OBJECT",
        object_code="INSTRUMENT.CREEP_TEST_TEST_MACHINE_HEATING_SYSTEM",
        property_label="Heating system",
        description="""Linked object: Heating system""",
        mandatory=False,
        section="Linked test machine objects",
    )
    link_holder_system = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_MACHINE_LINK_HOLDER_SYSTEM",
        data_type="OBJECT",
        object_code="INSTRUMENT_ACCESSORY.CREEP_TEST_TEST_PIECE_HOLDER_SYSTEM",
        property_label="Test piece holder system",
        description="""Linked object: Test piece holder system""",
        mandatory=False,
        section="Linked test machine objects",
    )
    link_loading_system = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_MACHINE_LINK_LOADING_SYSTEM",
        data_type="OBJECT",
        object_code="INSTRUMENT.CREEP_TEST_TEST_MACHINE_LOADING_SYSTEM",
        property_label="Loading system",
        description="""Linked object: Loading system""",
        mandatory=False,
        section="Linked test machine objects",
    )
    link_data_acquisition = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_MACHINE_LINK_DATA_ACQUISITION",
        data_type="OBJECT",
        object_code="INSTRUMENT.CREEP_TEST_TEST_MACHINE_DATA_ACQUISITION",
        property_label="Data acquisition",
        description="""Linked object: Data acquisition""",
        mandatory=False,
        section="Linked test machine objects",
    )

    creep_test_test_machine_id = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_MACHINE_ID",
        data_type="VARCHAR",
        property_label="Test machine ID",
        description="""Test machine ID // Prüfmaschinen-ID""",
        mandatory=False,
        section="Test machine",
    )
    creep_test_test_machine_type = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_MACHINE_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_MACHINE_TYPE",
        property_label="Test machine type",
        description="""Test machine type // Prüfmaschinentyp""",
        mandatory=False,
        section="Test machine",
    )
    creep_test_minimum_applicable_force = PropertyTypeAssignment(
        code="CREEP_TEST_MINIMUM_APPLICABLE_FORCE",
        data_type="REAL",
        property_label="Minimum applicable force",
        units="kN",
        description="""Minimum applicable force // Minimale anwendbare Kraft""",
        mandatory=False,
        section="Test machine",
    )
    creep_test_maximum_applicable_force = PropertyTypeAssignment(
        code="MAX_STATIC_FORCE",
        data_type="REAL",
        property_label="Maximum applicable force",
        units="kN",
        description="""Maximum applicable force // Maximale anwendbare Kraft""",
        mandatory=False,
        section="Test machine",
    )
    creep_test_test_frame_and_specimen_alignment = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_FRAME_AND_SPECIMEN_ALIGNMENT",
        data_type="BOOLEAN",
        property_label="Test frame and specimen alignment?",
        description="""Test frame and specimen alignment - Verification of Test Frame and Specimen Alignment according to ASTM E1012? // Ausrichtung von Testrahmen und Probekörper - Überprüfung der Ausrichtung von Testrahmen und Probekörper gemäß ASTM E1012?""",
        mandatory=True,
        section="Test machine",
    )
    creep_test_test_frame_and_specimen_alignment_description = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_FRAME_AND_SPECIMEN_ALIGNMENT_DESCRIPTION",
        data_type="VARCHAR",
        property_label="Test frame and specimen alignment - description",
        description="""Test frame and specimen alignment - description - Please provide a description on the procedure followed for the Verification of Test Frame and Specimen Alignment if different from ASTM E1012 // Ausrichtung von Testrahmen und Probekörper - Beschreibung - Bitte beschreiben Sie das Verfahren zur Überprüfung der Ausrichtung von Testrahmen und Probekörper, falls es von ASTM E1012 abweicht.""",
        mandatory=True,
        section="Test machine",
    )
    creep_test_calibration_class = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_CLASS",
        data_type="REAL",
        property_label="Calibration class",
        description="""Calibration class - Calibration class of test frame and specimen alignment, e.g., 5 / 5 starting from 3 kN (according to ASTM E1012) // Kalibrierklasse - Kalibrierklasse der Ausrichtung von Testrahmen und Probekörper, z. B. 5/5 ab 3 kN (gemäß ASTM E1012).""",
        mandatory=True,
        section="Test machine",
    )


class CreepTestTestMachineHeatingSystem(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.CREEP_TEST_TEST_MACHINE_HEATING_SYSTEM",
        description="""Measuring and test equipment / Test machine / Heating system // Mess- und Prüfmittel / Prüfmaschine / Heizsystem""",
        generated_code_prefix="INS.CREEP_MACHI_HEATI",
    )
    creep_test_furnace_type = PropertyTypeAssignment(
        code="CREEP_TEST_FURNACE_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_FURNACE_TYPE",
        property_label="Furnace type",
        description="""Furnace type // Ofentyp""",
        mandatory=True,
        section="Heating system",
    )


class CreepTestTestPieceHolderSystem(InstrumentAccessory):
    defs = ObjectTypeDef(
        code="INSTRUMENT_ACCESSORY.CREEP_TEST_TEST_PIECE_HOLDER_SYSTEM",
        description="""Measuring and test equipment / Test machine / Test piece holder system // Mess- und Prüfmittel / Prüfmaschine / Probenhaltersystem""",
        generated_code_prefix="INS_ACC.CREEP_PIECE_HOLDE",
    )
    creep_test_fixing_technique = PropertyTypeAssignment(
        code="CREEP_TEST_FIXING_TECHNIQUE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_FIXING_TECHNIQUE",
        property_label="Fixing technique",
        description="""Fixing technique // Befestigungstechnik""",
        mandatory=True,
        section="Test piece holder system",
    )


class CreepTestTestMachineLoadingSystem(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.CREEP_TEST_TEST_MACHINE_LOADING_SYSTEM",
        description="""Measuring and test equipment / Test machine / Loading system // Mess- und Prüfmittel / Prüfmaschine / Belastungssystem""",
        generated_code_prefix="INS.CREEP_MACHI_LOADI",
    )

    creep_test_verification_of_loading_system = PropertyTypeAssignment(
        code="CREEP_TEST_VERIFICATION_OF_LOADING_SYSTEM",
        data_type="BOOLEAN",
        property_label="Was the loading system calibrated/verified?",
        description="""Verification of loading system - Was the loading system calibrated/verified? // Überprüfung des Belastungssystems - Wurde das Belastungssystem kalibriert/überprüft?""",
        mandatory=True,
        section="Loading system",
    )
    creep_test_calibration_certificate = PropertyTypeAssignment(
        code="CALIBRATION_CERTIFICATE_NUMBER",
        data_type="VARCHAR",
        property_label="Calibration certificate",
        description="""Calibration certificate - Link to file, preferably with machine-readable (meta)data. Please specify which device/feature/part of the test machine was calibrated. // Kalibrierzertifikat - Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten. Bitte geben Sie an, welches Gerät/Feature/welcher Teil der Prüfmaschine kalibriert wurde.""",
        mandatory=False,
        section="Loading system",
    )
    creep_test_calibration_date = PropertyTypeAssignment(
        code="CALIBRATION_DATE",
        data_type="DATE",
        property_label="Calibration date",
        description="""Calibration date // Kalibrierdatum""",
        mandatory=True,
        section="Loading system",
    )
    creep_test_calibration_validity_time_period = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_VALIDITY_TIME_PERIOD",
        data_type="REAL",
        property_label="Calibration validity time period",
        description="""Calibration validity time period // Gültigkeitszeitraum der Kalibrierung""",
        mandatory=True,
        section="Loading system",
    )
    creep_test_calibration_standard = PropertyTypeAssignment(
        code="CREEP_TEST_LOADING_SYSTEM_CALIBRATION_STANDARD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_LOAD_SYSTEM_CALIBRATION_STANDARD",
        property_label="Calibration standard",
        description="""Calibration standard // Kalibrierstandard""",
        mandatory=True,
        section="Loading system",
    )
    creep_test_calibration_class = PropertyTypeAssignment(  # ? unclear
        code="CREEP_TEST_CALIBRATION_CLASS",
        data_type="REAL",
        property_label="Calibration class",
        description="""Calibration class // Kalibrierklasse""",
        mandatory=True,
        section="Loading system",
    )
    creep_test_calibration_range = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_RANGE",
        data_type="REAL",
        property_label="Calibration range",
        units="kN",
        description="""Calibration range // Kalibrierbereich [kN]""",
        mandatory=True,
        section="Loading system",
    )
    creep_test_use_of_calibrated_weights = PropertyTypeAssignment(
        code="CREEP_TEST_USE_OF_CALIBRATED_WEIGHTS",
        data_type="BOOLEAN",
        property_label="Use of calibrated weights?",
        description="""Use of calibrated weights - Were calibrated weights used to apply the test force? // Verwendung kalibrierter Gewichte - Wurden kalibrierte Gewichte verwendet, um die Prüfkraft aufzubringen?""",
        mandatory=True,
        section="Loading system",
    )
    creep_test_description_of_the_loading_system = PropertyTypeAssignment(
        code="CREEP_TEST_DESCRIPTION_OF_THE_LOADING_SYSTEM",
        data_type="BOOLEAN",
        property_label="Were the loading system and related verification described in the case that calibrated weights were not used?",
        description="""Description of The Loading System - Were the loading system and related verification described in the case that calibrated weights were not used? (Metadata, Measuring and test equipment, Test machine, Loading system) // Beschreibung des Belastungssystems - Wurden das Belastungssystem und die damit verbundene Überprüfung beschrieben im Fall, dass keine kalibrierten Gewichte verwendet wurden? (Metadaten, Mess- und Prüfmittel, Prüfmaschine, Belastungssystem).""",
        mandatory=True,
        section="Loading system",
    )


class CreepTestTestMachineDataAcquisition(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.CREEP_TEST_TEST_MACHINE_DATA_ACQUISITION",
        description="""Measuring and test equipment / Test machine / Data acquisition // Mess- und Prüfmittel / Prüfmaschine / Datenerfassung""",
        generated_code_prefix="INS.CREEP_MACHI_DATA",
    )

    creep_test_data_acquisition_unit_model_information = PropertyTypeAssignment(
        code="CREEP_TEST_DATA_ACQUISITION_UNIT_MODEL_INFORMATION",
        data_type="VARCHAR",
        property_label="Data acquisition unit - Model information",
        description="""Data acquisition unit - Model information // Datenerfassungseinheit - Modellinformationen""",
        mandatory=False,
        section="Data acquisition",
    )
    creep_test_data_acquisition_unit_id = PropertyTypeAssignment(
        code="CREEP_TEST_DATA_ACQUISITION_UNIT_ID",
        data_type="VARCHAR",
        property_label="Data acquisition unit - ID",
        description="""Data acquisition unit - ID // Datenerfassungseinheit - ID""",
        mandatory=False,
        section="Data acquisition",
    )
    creep_test_data_acquisition_software_and_version = PropertyTypeAssignment(
        code="CREEP_TEST_DATA_ACQUISITION_SOFTWARE_AND_VERSION",
        data_type="VARCHAR",
        property_label="Data acquisition software and version",
        description="""Data acquisition software and version // Datenerfassungssoftware und Version""",
        mandatory=True,
        section="Data acquisition",
    )
    creep_test_data_acquisition_description = PropertyTypeAssignment(
        code="CREEP_TEST_DATA_ACQUISITION_DESCRIPTION",
        data_type="VARCHAR",
        property_label="Data acquisition - description",
        description="""Data acquisition - description // Datenerfassung - Beschreibung""",
        mandatory=True,
        section="Data acquisition",
    )
    creep_test_data_acquisition_time_check = PropertyTypeAssignment(
        code="CREEP_TEST_DATA_ACQUISITION_TIME_CHECK",
        data_type="BOOLEAN",
        property_label="Was the time checked during data acquisition?",
        description="""Data acquisition time check - Was the time checked during data acquisition? // Zeitprüfung der Datenerfassung - Wurde die Zeit während der Datenerfassung überprüft?""",
        mandatory=False,
        section="Data acquisition",
    )


class CreepTestLoadSensor(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.CREEP_TEST_LOAD_SENSOR",
        description="""Measuring and test equipment / Load-measuring system / Load sensor // Mess- und Prüfmittel / Kraftmesssystem / Kraftsensor""",
        generated_code_prefix="INS.CREEP_LOAD_SENSO",
    )

    creep_test_load_sensor_during_loading = PropertyTypeAssignment(
        code="CREEP_TEST_LOAD_SENSOR_DURING_LOADING",
        data_type="BOOLEAN",
        property_label="Was a load sensor used during loading?",
        description="""Load sensor during loading - Was a load sensor used during loading? // Kraftsensor während der Belastung - Wurde während des Lastaufbringens ein Kraftsensor verwendet?""",
        mandatory=True,
        section="Load sensor",
    )
    creep_test_load_sensor_calibration = PropertyTypeAssignment(
        code="CREEP_TEST_LOAD_SENSOR_CALIBRATION",
        data_type="BOOLEAN",
        property_label="Was the load sensor calibrated?",
        description="""Load sensor calibration - Was the load sensor calibrated? // Kalibrierung des Kraftsensors - War der Kraftsensor kalibriert?""",
        mandatory=True,
        section="Load sensor",
    )
    creep_test_calibration_certificate = PropertyTypeAssignment(
        code="CALIBRATION_CERTIFICATE_NUMBER",
        data_type="VARCHAR",
        property_label="Calibration certificate",
        description="""Calibration certificate - Link to file, preferably with machine-readable (meta)data. // Kalibrierzertifikat - Link to file, preferably with machine-readable (meta)data.""",
        mandatory=False,
        section="Load sensor",
    )
    creep_test_calibration_date = PropertyTypeAssignment(
        code="CALIBRATION_DATE",
        data_type="DATE",
        property_label="Calibration date",
        description="""Calibration date // Kalibrierdatum""",
        mandatory=True,
        section="Load sensor",
    )
    creep_test_calibration_validity_time_period = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_VALIDITY_TIME_PERIOD",
        data_type="REAL",
        property_label="Calibration validity time period",
        description="""Calibration validity time period // Gültigkeitszeitraum der Kalibrierung""",
        mandatory=True,
        section="Load sensor",
    )
    creep_test_calibration_standard = PropertyTypeAssignment(
        code="CREEP_TEST_LOAD_SENSOR_CALIBRATION_STANDARD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_LOAD_SYSTEM_CALIBRATION_STANDARD",
        property_label="Calibration standard",
        description="""Calibration standard // Kalibrierstandard""",
        mandatory=True,
        section="Load sensor",
    )
    creep_test_calibration_class = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_CLASS",
        data_type="REAL",
        property_label="Calibration class",
        description="""Calibration class // Kalibrierklasse""",
        mandatory=True,
        section="Load sensor",
    )
    creep_test_calibration_range = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_RANGE",
        data_type="REAL",
        property_label="Calibration Range",
        units="kN",
        description="""Calibration Range // Kalibrierbereich [kN]""",
        mandatory=True,
        section="Load sensor",
    )


class CreepTestLoadDataAcquisition(ObjectType):
    defs = ObjectTypeDef(
        code="CREEP_TEST_LOAD_DATA_ACQUISITION",
        description="""Measuring and test equipment / Load-measuring system / Data acquisition // Mess- und Prüfmittel / Kraftmesssystem / Datenerfassung""",
        generated_code_prefix="CREEP_LOAD_DATA_ACQU",
    )
    creep_test_force_recording = PropertyTypeAssignment(
        code="CREEP_TEST_FORCE_RECORDING",
        data_type="BOOLEAN",
        property_label="Was the force recorded continuously or periodically (e.g. during loading)? ",
        description="""Force recording - Was the force recorded continuously or periodically (e.g. during loading)? // Kraftaufzeichnung - Wurde die Kraft kontinuierlich oder periodisch aufgezeichnet (z. B. während des Lastaufbringens)?""",
        mandatory=True,
        section="Data acquisition",
    )


class CreepTestLaboratoryConditions(EnvironmentalConditions):
    defs = ObjectTypeDef(
        code="ENVIRONMENTAL_CONDITIONS.CREEP_TEST_LABORATORY_CONDITIONS",
        description="""Metadata / Environmental conditions / Laboratory conditions during creep test // Metadaten / Umgebungsbedingungen / Laborbedingungen während des Kriechversuchs""",
        generated_code_prefix="ENV.CREEP_LABOR_CONDI",
    )
    creep_test_room_temperature = PropertyTypeAssignment(
        code="CREEP_TEST_ROOM_TEMPERATURE",
        data_type="BOOLEAN",
        property_label="Was the room temperature recorded and checked?",
        description="""Room temperature - Was the room temperature recorded and checked? // Raumtemperatur - Wurde die Raumtemperatur aufgezeichnet und überprüft?""",
        mandatory=True,
        section="Laboratory conditions",
    )
    creep_test_room_humidity = PropertyTypeAssignment(
        code="CREEP_TEST_ROOM_HUMIDITY",
        data_type="BOOLEAN",
        property_label="Was the room humidity recorded and checked?",
        description="""Room humidity - Was the room humidity recorded and checked? // Raumluftfeuchte - Wurde die Raumluftfeuchte aufgezeichnet und überprüft?""",
        mandatory=False,
        section="Laboratory conditions",
    )


class CreepTestTemperatureMeasuringSystem(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.CREEP_TEST_TEMPERATURE_MEASURING_SYSTEM",
        description="""Metadata / Measuring and test equipment / Temperature-measuring system // Metadaten / Mess- und Prüfmittel / Temperaturmesssystem""",
        generated_code_prefix="INS.CREEP_TEMPE_MEASU",
    )

    creep_test_temperature_signal = PropertyTypeAssignment(
        code="CREEP_TEST_TEMPERATURE_SIGNAL",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_TEMPERATURE_SIGNAL",
        property_label="Temperature signal",
        description="""Temperature signal - Which temperature signal was used for temperature control? // Temperatursignal - Welches Temperatursignal wurde für die Temperaturregelung verwendet?""",
        mandatory=True,
        section="Temperature-measuring system",
    )
    creep_test_metrological_traceability = PropertyTypeAssignment(
        code="CREEP_TEST_METROLOGICAL_TRACEABILITY",
        data_type="BOOLEAN",
        property_label="True if temperature sensor and data acquisition are calibrated.",
        description="""Metrological traceability - Yes, if temperature sensor and data acquisition are calibrated. // Metrologische Rückführbarkeit - Ja, wenn Temperatursensor und Datenerfassung kalibriert sind.""",
        mandatory=True,
        section="Temperature-measuring system",
    )


class CreepTestTemperatureSensor(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.CREEP_TEST_TEMPERATURE_SENSOR",
        description="""Metadata / Measuring and test equipment / Temperature-measuring system / Temperature sensor // Metadaten / Mess- und Prüfmittel / Temperaturmesssystem / Temperatursensor""",
        generated_code_prefix="INS.CREEP_TEMPE_SENSO",
    )

    creep_test_sensor_type = PropertyTypeAssignment(
        code="CREEP_TEST_SENSOR_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_SENSOR_TYPE",
        property_label="Sensor type",
        description="""Sensor type // Sensortyp""",
        mandatory=True,
        section="Temperature sensor",
    )
    creep_test_sensor_id = PropertyTypeAssignment(
        code="CREEP_TEST_SENSOR_ID",
        data_type="VARCHAR",
        property_label="Sensor ID",
        description="""Sensor ID // Sensor-ID""",
        mandatory=False,
        section="Temperature sensor",
    )
    creep_test_thermocouple_type = PropertyTypeAssignment(
        code="CREEP_TEST_THERMOCOUPLE_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="THERMOCOUPLE_TYPE",
        property_label="Thermocouple type",
        description="""Thermocouple type // Thermoelementtyp""",
        mandatory=True,
        section="Temperature sensor",
    )
    creep_test_wire_gauge = PropertyTypeAssignment(
        code="CREEP_TEST_WIRE_GAUGE",
        data_type="REAL",
        property_label="Wire gauge",
        units="mm",
        description="""Wire gauge // Drahtdurchmesser""",
        mandatory=False,
        section="Temperature sensor",
    )
    creep_test_layout = PropertyTypeAssignment(
        code="CREEP_TEST_LAYOUT",
        data_type="VARCHAR",
        property_label="Layout",
        description="""Layout - E.g., wire with 2-hole ceramic beads // Aufbau - E.g., wire with 2-hole ceramic beads""",
        mandatory=False,
        section="Temperature sensor",
    )
    creep_test_calibration_status = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_STATUS",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_CALIBRATION_STATUS",
        property_label="Is/are the thermocouples calibrated?",
        description="""Calibration status - Is/are the thermocouples calibrated? // Kalibrierstatus - Ist/sind das/die Thermoelement(e) kalibriert?""",
        mandatory=True,
        section="Temperature sensor",
    )
    creep_test_calibration_method = PropertyTypeAssignment(
        code="CREEP_TEST_TEMPERATURE_SENSOR_CALIBRATION_METHOD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_THERMOCOUPLE_CALIBRATION_METHOD",
        property_label="Calibration method",
        description="""Calibration method // Kalibriermethode""",
        mandatory=True,
        section="Temperature sensor",
    )
    creep_test_calibration_standard = PropertyTypeAssignment(
        code="CREEP_TEST_TEMPERATURE_SENSOR_CALIBRATION_STANDARD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_THERMOCOUPLE_CALIBRATION_STANDARD",
        property_label="Calibration standard",
        description="""Calibration standard // Kalibrierstandard""",
        mandatory=True,
        section="Temperature sensor",
    )
    creep_test_calibration_certificate = PropertyTypeAssignment(
        code="CALIBRATION_CERTIFICATE_NUMBER",
        data_type="VARCHAR",
        property_label="Calibration certificate",
        description="""Calibration certificate - Link to file, preferably with machine-readable (meta)data. // Kalibrierzertifikat - Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=False,
        section="Temperature sensor",
    )
    creep_test_calibration_date = PropertyTypeAssignment(
        code="CALIBRATION_DATE",
        data_type="DATE",
        property_label="Calibration date",
        description="""Calibration date // Kalibrierdatum""",
        mandatory=True,
        section="Temperature sensor",
    )
    creep_test_calibration_validity_time_period = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_VALIDITY_TIME_PERIOD",
        data_type="REAL",
        property_label="Calibration validity time period",
        description="""Calibration validity time period // Gültigkeitszeitraum der Kalibrierung""",
        mandatory=True,
        section="Temperature sensor",
    )
    creep_test_temperature_deviation = PropertyTypeAssignment(
        code="CREEP_TEST_TEMPERATURE_DEVIATION",
        data_type="VARCHAR",
        property_label="Temperature deviation",
        units="degC",
        description="""Temperature deviation - Measurement deviation detected during calibration // Temperaturabweichung [°C] - Bei der Kalibrierung festgestellte Messabweichung""",
        mandatory=False,
        section="Temperature sensor",
    )
    creep_test_calibration_range = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_RANGE",
        data_type="REAL",
        property_label="Calibration Range",
        units="degC",
        description="""Calibration Range // Kalibrierbereich [°C]""",
        mandatory=True,
        section="Temperature sensor",
    )
    creep_test_contact_method = PropertyTypeAssignment(
        code="CREEP_TEST_CONTACT_METHOD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_THERMOCOUPLE_CONTACT_METHOD",
        property_label="Contact method",
        description="""Contact method // Kontaktmethode""",
        mandatory=True,
        section="Temperature sensor",
    )
    creep_test_number_of_thermocouples = PropertyTypeAssignment(
        code="CREEP_TEST_NUMBER_OF_THERMOCOUPLES",
        data_type="INTEGER",
        vocabulary_code="CREEP_TEST_NUMBER_OF_THERMOCOUPLES",
        property_label="Number of thermocouples (max. 3)",
        description="""Number of thermocouples (max. 3) // Anzahl der Thermoelemente (maximum 3)""",
        mandatory=True,
        section="Temperature sensor",
    )
    creep_test_thermocouple_location = PropertyTypeAssignment(
        code="CREEP_TEST_THERMOCOUPLE_LOCATION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_THERMOCOUPLE_LOCATION",
        property_label="Thermocouple location",
        description="""Thermocouple location - Location with respect to gauge section // Position des Thermoelements - Position in Bezug auf den Messbereich""",
        mandatory=True,
        section="Temperature sensor",
    )


class CreepTestTemperatureDataAcquisition(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.CREEP_TEST_TEMPERATURE_DATA_ACQUISITION",
        description="""Metadata / Measuring and test equipment / Temperature-measuring system / Data acquisition // Metadaten / Mess- und Prüfmittel / Temperaturmesssystem / Datenerfassung""",
        generated_code_prefix="INS.CREEP_TEMPE_DATA",
    )

    creep_test_calibration_status = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_STATUS",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_CALIBRATION_STATUS",
        property_label="Is/are the data acquisition unit calibrated?",
        description="""Calibration status - Is/are the data acquisition unit calibrated? // Kalibrierstatus - Ist/sind die Datenerfassungseinheit(en) kalibriert?""",
        mandatory=True,
        section="Data acquisition",
    )
    creep_test_reference_junction = PropertyTypeAssignment(
        code="CREEP_TEST_REFERENCE_JUNCTION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_REFERENCE_JUNCTION",
        property_label="Reference junction",
        description="""Reference junction // Referenzstelle""",
        mandatory=False,
        section="Data acquisition",
    )
    creep_test_calibration_certificate = PropertyTypeAssignment(
        code="CALIBRATION_CERTIFICATE_NUMBER",
        data_type="VARCHAR",
        property_label="Calibration certificate",
        description="""Calibration certificate - Link to file, preferably with machine-readable (meta)data. // Kalibrierzertifikat - Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=False,
        section="Data acquisition",
    )
    creep_test_calibration_date = PropertyTypeAssignment(
        code="CALIBRATION_DATE",
        data_type="DATE",
        property_label="Calibration date",
        description="""Calibration date // Kalibrierdatum""",
        mandatory=True,
        section="Data acquisition",
    )
    creep_test_calibration_validity_time_period = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_VALIDITY_TIME_PERIOD",
        data_type="REAL",
        property_label="Calibration validity time period",
        description="""Calibration validity time period // Gültigkeitszeitraum der Kalibrierung""",
        mandatory=True,
        section="Data acquisition",
    )
    creep_test_calibration_method = PropertyTypeAssignment(
        code="CREEP_TEST_TEMPERATURE_DAQ_CALIBRATION_METHOD",
        data_type="VARCHAR",
        property_label="Calibration method",
        description="""Calibration method // Kalibriermethode""",
        mandatory=True,
        section="Data acquisition",
    )
    creep_test_calibration_standard = PropertyTypeAssignment(
        code="CREEP_TEST_TEMPERATURE_DAQ_CALIBRATION_STANDARD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_DATA_ACQUISITION_CALIBRATION_STANDARD",
        property_label="Calibration standard",
        description="""Calibration standard // Kalibrierstandard""",
        mandatory=True,
        section="Data acquisition",
    )
    creep_test_temperature_deviation = PropertyTypeAssignment(
        code="CREEP_TEST_TEMPERATURE_DEVIATION",
        data_type="VARCHAR",
        property_label="Temperature deviation",
        units="degC",
        description="""Temperature deviation - Measurement deviation detected during calibration // Temperaturabweichung [°C] - Bei der Kalibrierung festgestellte Messabweichung""",
        mandatory=False,
        section="Data acquisition",
    )
    creep_test_calibration_range = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_RANGE",
        data_type="REAL",
        property_label="Calibration Range",
        units="degC",
        description="""Calibration Range // Kalibrierbereich [°C]""",
        mandatory=True,
        section="Data acquisition",
    )


class CreepTestExtensometerSystem(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.CREEP_TEST_EXTENSOMETER_SYSTEM",
        description="""Metadata / Measuring and test equipment / Extensometer system // Metadaten / Mess- und Prüfmittel / Extensometersystem""",
        generated_code_prefix="INS.CREEP_EXTEN_SYSTE",
    )

    creep_test_displacement_measuring_method = PropertyTypeAssignment(
        code="CREEP_TEST_DISPLACEMENT_MEASURING_METHOD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_DISPLACEMENT_MEASURING_METHOD",
        property_label="Displacement measuring method",
        description="""Displacement measuring method - Type of strain measuring device // Wegmessverfahren - Art des Dehnungsmessgeräts""",
        mandatory=True,
        section="Extensometer system",
    )
    creep_test_sensor_type_contacting_method = PropertyTypeAssignment(
        code="CREEP_TEST_SENSOR_TYPE_CONTACTING_METHOD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_SENSOR_TYPE_CONTACTING_METHOD",
        property_label="Sensor type - Contacting method",
        description="""Sensor type - Contacting method // Sensortyp - Kontaktmethode""",
        mandatory=True,
        section="Extensometer system",
    )
    creep_test_sensor_type_non_contacting_method = PropertyTypeAssignment(
        code="CREEP_TEST_SENSOR_TYPE_NON_CONTACTING_METHOD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_SENSOR_TYPE_NON_CONTACTING_METHOD",
        property_label="Sensor type - Non-contacting method",
        description="""Sensor type - Non-contacting method // Sensortyp - berührungslose Methode""",
        mandatory=True,
        section="Extensometer system",
    )


class CreepTestExtensionValuesContactingExtensometer(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.CREEP_TEST_EXTENSION_VALUES_CONTACTING_EXTENSOMETER",
        description="""Metadata / Measuring and test equipment / Extension values / Contacting extensometer // Metadaten / Mess- und Prüfmittel / Dehnungswerte / kontaktierendes Extensometer""",
        generated_code_prefix="INS.CREEP_EXTEN_VALUE",
    )

    creep_test_measurement_setup = PropertyTypeAssignment(
        code="CREEP_TEST_MEASUREMENT_SETUP",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_MEASUREMENT_SETUP",
        property_label="Measurement setup",
        description="""Measurement setup - Measurement one-sided or two-sided? // Messaufbau - Einseitige oder beidseitige Messung?""",
        mandatory=True,
        section="Contacting extensometer",
    )
    creep_test_extension_averaging = PropertyTypeAssignment(
        code="CREEP_TEST_EXTENSION_AVERAGING",
        data_type="BOOLEAN",
        property_label="Was there an averaging of the extension values? (two-sided extensometer)",
        description="""Extension averaging - Was there an averaging of the extension values? (two-sided extensometer) // Dehnungsmittelung - Wurden die Dehnungswerte gemittelt? (beidseitiger Dehnungsmesser)""",
        mandatory=True,
        section="Contacting extensometer",
    )
    creep_test_measurement_direction = PropertyTypeAssignment(
        code="CREEP_TEST_MEASUREMENT_DIRECTION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_EXTENSION_MEASUREMENT_DIRECTION",
        property_label="Measurement direction",
        description="""Measurement direction // Messrichtung""",
        mandatory=True,
        section="Contacting extensometer",
    )
    creep_test_mounting_type = PropertyTypeAssignment(
        code="CREEP_TEST_MOUNTING_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_EXTENSOMETER_MOUNTING_TYPE",
        property_label="Mounting type",
        description="""Mounting type // Montageart""",
        mandatory=True,
        section="Contacting extensometer",
    )
    creep_test_extensometer_model_information = PropertyTypeAssignment(
        code="CREEP_TEST_EXTENSOMETER_MODEL_INFORMATION",
        data_type="VARCHAR",
        property_label="Extensometer model information",
        description="""Extensometer model information // Extensometer-Modellinformationen""",
        mandatory=False,
        section="Contacting extensometer",
    )
    creep_test_extensometer_id = PropertyTypeAssignment(
        code="CREEP_TEST_EXTENSOMETER_ID",
        data_type="VARCHAR",
        property_label="Extensometer ID",
        description="""Extensometer ID - The ID used for identification in the laboratory // Extensometer-ID - ID zur Identifikation im Labor""",
        mandatory=False,
        section="Contacting extensometer",
    )
    creep_test_extensometer_leg_material = PropertyTypeAssignment(
        code="CREEP_TEST_EXTENSOMETER_LEG_MATERIAL",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_EXTENSOMETER_LEG_MATERIAL",
        property_label="Extensometer leg material",
        description="""Extensometer leg material - Material of upper/lower legs, e.g., in LVDT systems // Material der Extensometerschenkel - Material der Ober-/Unterbeine, z. B. in LVDT-Systemen""",
        mandatory=False,
        section="Contacting extensometer",
    )
    creep_test_measuring_amplifier_model_information = PropertyTypeAssignment(
        code="CREEP_TEST_MEASURING_AMPLIFIER_MODEL_INFORMATION",
        data_type="VARCHAR",
        property_label="Measuring amplifier - Model information",
        description="""Measuring amplifier - Model information // Messverstärker - Modellinformationen""",
        mandatory=False,
        section="Contacting extensometer",
    )
    creep_test_extension_range_upper_limit = PropertyTypeAssignment(
        code="CREEP_TEST_EXTENSION_RANGE_UPPER_LIMIT",
        data_type="REAL",
        property_label="Extension range - Upper limit",
        units="% / mm",
        description="""Extension range - Upper limit // Dehnmessbereich - Obergrenze [% / mm]""",
        mandatory=True,
        section="Contacting extensometer",
    )
    creep_test_extension_range_lower_limit = PropertyTypeAssignment(
        code="CREEP_TEST_EXTENSION_RANGE_LOWER_LIMIT",
        data_type="REAL",
        property_label="Extension range - Lower limit",
        units="% / mm",
        description="""Extension range - Lower limit // Dehnmessbereich - Untergrenze [%  / mm]""",
        mandatory=True,
        section="Contacting extensometer",
    )
    creep_test_nominal_gauge_length = PropertyTypeAssignment(
        code="CREEP_TEST_NOMINAL_GAUGE_LENGTH",
        data_type="REAL",
        property_label="Nominal gauge length",
        units="mm",
        description="""Nominal gauge length - If applicable // Nennmesslänge [mm] - If applicable""",
        mandatory=True,
        section="Contacting extensometer",
    )
    creep_test_is_the_extensometer_incl_the_data_acquisition_calibrated = PropertyTypeAssignment(
        code="CREEP_TEST_IS_THE_EXTENSOMETER_INCL_THE_DATA_ACQUISITION_CALIBRATED",
        data_type="BOOLEAN",
        property_label="Is the extensometer incl. the data acquisition calibrated?",
        description="""Is the extensometer incl. the data acquisition calibrated? - Is the extensometer incl. the data acquisition calibrated? // Extensometer inkl. Datenerfassung kalibriert? - Ist/War das Extensometer inkl. Datenerfassung kalibriert?""",
        mandatory=True,
        section="Contacting extensometer",
    )
    creep_test_calibration_certificate = PropertyTypeAssignment(
        code="CALIBRATION_CERTIFICATE_NUMBER",
        data_type="VARCHAR",
        property_label="Calibration certificate",
        description="""Calibration certificate - Link to file, preferably with machine-readable (meta)data. // Kalibrierzertifikat - Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=False,
        section="Contacting extensometer",
    )
    creep_test_calibration_date = PropertyTypeAssignment(
        code="CALIBRATION_DATE",
        data_type="DATE",
        property_label="Calibration date",
        description="""Calibration date // Kalibrierdatum""",
        mandatory=True,
        section="Contacting extensometer",
    )
    creep_test_calibration_validity_time_period = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_VALIDITY_TIME_PERIOD",
        data_type="REAL",
        property_label="Calibration validity time period",
        description="""Calibration validity time period // Gültigkeitszeitraum der Kalibrierung""",
        mandatory=True,
        section="Contacting extensometer",
    )
    creep_test_calibration_class = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_CLASS",
        data_type="REAL",
        property_label="Calibration class",
        description="""Calibration class // Calibration class""",
        mandatory=True,
        section="Contacting extensometer",
    )
    creep_test_calibration_range = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_RANGE",
        data_type="REAL",
        property_label="Calibration Range",
        units="% (mm)",
        description="""Calibration Range // Kalibrierbereich [% (mm)]""",
        mandatory=True,
        section="Contacting extensometer",
    )
    creep_test_calibration_standard = PropertyTypeAssignment(
        code="CREEP_TEST_EXTENSOMETER_CALIBRATION_STANDARD",
        data_type="VARCHAR",
        property_label="Calibration standard",
        description="""Calibration standard // Kalibrierstandard""",
        mandatory=True,
        section="Contacting extensometer",
    )


class CreepTestElongationValuesAndCrossSectionalDimensions(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.CREEP_TEST_ELONGATION_VALUES_AND_CROSS_SECTIONAL_DIMENSIONS",
        description="""Metadata / Measuring and test equipment / Elongation values and cross-sectional dimensions // Metadaten / Mess- und Prüfmittel / Verlängerungswerte und Querschnittsabmessungen""",
        generated_code_prefix="INS.CREEP_ELONG_VALUE",
    )

    creep_test_measuring_equipment = PropertyTypeAssignment(
        code="CREEP_TEST_MEASURING_EQUIPMENT",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_MEASURING_EQUIPMENT",
        property_label="Measuring equipment",
        description="""Measuring equipment // Messgerät""",
        mandatory=True,
        section="Elongation values and cross-sectional dimensions",
    )
    creep_test_measuring_equipments_usage = PropertyTypeAssignment(
        code="CREEP_TEST_MEASURING_EQUIPMENTS_USAGE",
        data_type="VARCHAR",
        property_label="Measuring equipment's usage",
        description="""Measuring equipment's usage // Verwendung des Messgeräts""",
        mandatory=True,
        section="Elongation values and cross-sectional dimensions",
    )
    creep_test_resolution = PropertyTypeAssignment(
        code="CREEP_TEST_RESOLUTION",
        data_type="INTEGER",
        property_label="Resolution",
        units="mm",
        description="""Resolution // Auflösung""",
        mandatory=True,
        section="Elongation values and cross-sectional dimensions",
    )
    creep_test_measuring_equipment_type = PropertyTypeAssignment(
        code="CREEP_TEST_MEASURING_EQUIPMENT_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_MEASURING_EQUIPMENT_TYPE",
        property_label="Measuring equipment type",
        description="""Measuring equipment type // Messgerätetyp""",
        mandatory=False,
        section="Elongation values and cross-sectional dimensions",
    )
    creep_test_equipment_model_information = PropertyTypeAssignment(
        code="DEVICE_MODEL_NAME",
        data_type="VARCHAR",
        property_label="Equipment model information",
        description="""Equipment model information // Gerätemodellinformationen""",
        mandatory=False,
        section="Elongation values and cross-sectional dimensions",
    )
    creep_test_equipment_id = PropertyTypeAssignment(
        code="CREEP_TEST_EQUIPMENT_ID",
        data_type="VARCHAR",
        property_label="Equipment ID",
        description="""Equipment ID - The ID used for identification in the laboratory // Geräte-ID - ID zur Identifikation im Labor""",
        mandatory=False,
        section="Elongation values and cross-sectional dimensions",
    )
    creep_test_calibration_status = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_STATUS",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_CALIBRATION_STATUS",
        property_label="Is the measuring equipment calibrated?",
        description="""Calibration status - Is the measuring equipment calibrated? // Kalibrierstatus - Sind/Waren die Messgeräte kalibriert?""",
        mandatory=True,
        section="Elongation values and cross-sectional dimensions",
    )
    creep_test_calibration_certificate = PropertyTypeAssignment(
        code="CALIBRATION_CERTIFICATE_NUMBER",
        data_type="VARCHAR",
        property_label="Calibration certificate",
        description="""Calibration certificate - Link to file, preferably with machine-readable (meta)data. // Kalibrierzertifikat - Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=False,
        section="Elongation values and cross-sectional dimensions",
    )
    creep_test_calibration_date = PropertyTypeAssignment(
        code="CALIBRATION_DATE",
        data_type="DATE",
        property_label="Calibration date",
        description="""Calibration date // Kalibrierdatum""",
        mandatory=True,
        section="Elongation values and cross-sectional dimensions",
    )
    creep_test_calibration_validity_time_period = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_VALIDITY_TIME_PERIOD",
        data_type="REAL",
        property_label="Calibration validity time period",
        description="""Calibration validity time period // Gültigkeitszeitraum der Kalibrierung""",
        mandatory=True,
        section="Elongation values and cross-sectional dimensions",
    )
    creep_test_calibration_result = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_RESULT",
        data_type="BOOLEAN",
        property_label="Does the measuring equipment meet the required calibration standards?",
        description="""Calibration result - Does the measuring equipment meet the required calibration standards? // Kalibrierergebnis - Erfüllt das Messgerät die erforderlichen Kalibrierstandards?""",
        mandatory=True,
        section="Elongation values and cross-sectional dimensions",
    )
    creep_test_calibration_range = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_RANGE",
        data_type="REAL",
        property_label="Calibration range",
        units="mm",
        description="""Calibration range // Kalibrierbereich [mm]""",
        mandatory=True,
        section="Elongation values and cross-sectional dimensions",
    )
    creep_test_calibration_standard = PropertyTypeAssignment(
        code="CREEP_TEST_ELONGATION_MEASURING_EQUIPMENT_CALIBRATION_STANDARD",
        data_type="VARCHAR",
        property_label="Calibration standard",
        description="""Calibration standard // Kalibrierstandard""",
        mandatory=True,
        section="Elongation values and cross-sectional dimensions",
    )


class CreepTestDataProcessingProcedures(ComputationalAnalysis):
    defs = ObjectTypeDef(
        code="COMPUTATIONAL_ANALYSIS.CREEP_TEST_DATA_PROCESSING_PROCEDURES",
        description="""Metadata / Data processing procedures // Metadaten / Datenverarbeitungsverfahren""",
        generated_code_prefix="COMP.CREEP_DATA_PROCE",
    )

    creep_test_primary_data_series = PropertyTypeAssignment(
        code="CREEP_TEST_PRIMARY_DATA_SERIES",
        data_type="VARCHAR",
        property_label="Primary data series",
        description="""Primary data series - Primary data is data that is directly acquired by sensors or measuring instruments during or after a test. Please add a list of the measured quantities and their corresponsing units. // Primärdatenreihen - Primärdaten sind Daten, die während oder nach einer Prüfung direkt von Sensoren oder Messgeräten erfasst werden. Bitte fügen Sie eine Liste der gemessenen Größen und der zugehörigen Einheiten hinzu.""",
        mandatory=True,
        section="Data processing procedures",
    )
    creep_test_processed_data_series = PropertyTypeAssignment(
        code="CREEP_TEST_PROCESSED_DATA_SERIES",
        data_type="VARCHAR",
        property_label="Processed data series",
        description="""Processed data series - Processed data is obtained as a result of using procedures (equations, algorithms, methods, unit conversions, averaging, smoothing) to transform primary data. Please describe the transformed quantities, their corresponsing units, and the applied procedures. // Verarbeitete Datenreihen - Verarbeitete Daten entstehen durch Verfahren (Gleichungen, Algorithmen, Methoden, Einheitenumrechnungen, Mittelung, Glättung), die Primärdaten transformieren. Bitte beschreiben Sie die transformierten Größen, deren Einheiten sowie die angewandten Verfahren.""",
        mandatory=True,
        section="Data processing procedures",
    )
    creep_test_data_analysis_procedures = PropertyTypeAssignment(
        code="CREEP_TEST_DATA_ANALYSIS_PROCEDURES",
        data_type="VARCHAR",
        property_label="Data analysis procedures",
        description="""Data analysis procedures - Description of the data processing and analysis procedures used to obtain specific test results, e.g. percentage elastic extension, ee // Datenanalyseverfahren - Beschreibung der Datenverarbeitungs- und Analyseverfahren zur Ermittlung spezifischer Prüfergebnisse, z. B. prozentuale elastische Dehnung (ee).""",
        mandatory=True,
        section="Data processing procedures",
    )
    creep_test_workflow_usage = PropertyTypeAssignment(
        code="CREEP_TEST_WORKFLOW_USAGE",
        data_type="BOOLEAN",
        property_label="Were automated (user-independent) analysis workflows used?",
        description="""Workflow usage - Were automated (user-independent) analysis workflows used? // Workflow-Nutzung - Wurden automatisierte (benutzerunabhängige) Analyse-Workflows verwendet?""",
        mandatory=True,
        section="Data processing procedures",
    )
    creep_test_software = PropertyTypeAssignment(
        code="CREEP_TEST_SOFTWARE",
        data_type="VARCHAR",
        property_label="Software",
        description="""Software - If applicable, please list the used software/workflow, including product and version // Software - Falls zutreffend, bitte die verwendete Software bzw. den Workflow mit Produkt und Version angeben.""",
        mandatory=True,
        section="Data processing procedures",
    )
    creep_test_related_publications = PropertyTypeAssignment(
        code="CREEP_TEST_RELATED_PUBLICATIONS",
        data_type="MULTILINE_VARCHAR",
        property_label="Related publications",
        description="""Related publications - If applicable, please list publications related to the data analysis procedure/software used // Zugehörige Publikationen - Falls zutreffend, bitte Publikationen nennen, die sich auf das verwendete Datenanalyseverfahren bzw. die Software beziehen.""",
        mandatory=False,
        section="Data processing procedures",
    )


class CreepTestPrimaryValuesRecordedAtTestStart(ObjectType):
    defs = ObjectTypeDef(
        code="CREEP_TEST_PRIMARY_VALUES_RECORDED_AT_TEST_START",
        description="""Primary data / Test result / Values recorded at test start // Primärdaten / Prüfergebnis / Zu Testbeginn erfasste Werte""",
        generated_code_prefix="CREEP_PRIMA_VALUE",
    )

    creep_test_minimum_test_piece_diameter_at_room_temperature = PropertyTypeAssignment(
        code="CREEP_TEST_MINIMUM_TEST_PIECE_DIAMETER_AT_ROOM_TEMPERATURE",
        data_type="REAL",
        property_label="Minimum test piece diameter at room temperature",
        units="mm",
        description="""Minimum test piece diameter at room temperature // Minimaler Proben-Durchmesser bei Raumtemperatur [mm]""",
        mandatory=True,
        section="Values recorded at test start",
    )
    creep_test_original_gauge_length = PropertyTypeAssignment(
        code="CREEP_TEST_ORIGINAL_GAUGE_LENGTH",
        data_type="REAL",
        property_label="Original gauge length",
        units="mm",
        description="""Original gauge length // Ursprüngliche Messlänge [mm]""",
        mandatory=True,
        section="Values recorded at test start",
    )
    creep_test_parallel_length = PropertyTypeAssignment(
        code="CREEP_TEST_PARALLEL_LENGTH",
        data_type="REAL",
        property_label="Parallel length",
        units="mm",
        description="""Parallel length // Parallele Länge [mm]""",
        mandatory=True,
        section="Values recorded at test start",
    )
    creep_test_extensometer_gauge_length = PropertyTypeAssignment(
        code="CREEP_TEST_EXTENSOMETER_GAUGE_LENGTH",
        data_type="REAL",
        property_label="Extensometer gauge length",
        units="mm",
        description="""Extensometer gauge length // Extensometer-Messlänge [mm]""",
        mandatory=True,
        section="Values recorded at test start",
    )
    creep_test_determination_of_reference_length = PropertyTypeAssignment(
        code="CREEP_TEST_DETERMINATION_OF_REFERENCE_LENGTH",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_DETERMINATION_OF_REFERENCE_LENGTH",
        property_label="Determination of reference length",
        description="""Determination of reference length - Case 1: Reference length for calculation of percentage extensions/elongations if the original gauge length Lo and/or extensometer Le are inside the parallel length, Lc. In this case Lr = Le (percentage extensions) or Lr = Lo (percentage elongations). Case 2: Reference length for calculation of percentage extensions/elongations if the original gauge length Lo and/or extensometer Le are outside the parallel length, Lc. In this case, Lr, for calculation of percentage is corrected to consider the strain contributions of the shoulders/ridges. // Bestimmung der Referenzlänge - Case 1: Reference length for calculation of percentage extensions/elongations if the original gauge length Lo and/or extensometer Le are inside the parallel length, Lc. In this case Lr = Le (percentage extensions) or Lr = Lo (percentage elongations). Case 2: Reference length for calculation of percentage extensions/elongations if the original gauge length Lo and/or extensometer Le are outside the parallel length, Lc. In this case, Lr, for calculation of percentage is corrected to consider the strain contributions of the shoulders/ridges.""",
        mandatory=True,
        section="Values recorded at test start",
    )
    creep_test_reference_length_to_calculate_percentage_elongations = PropertyTypeAssignment(
        code="CREEP_TEST_REFERENCE_LENGTH_TO_CALCULATE_PERCENTAGE_ELONGATIONS",
        data_type="REAL",
        property_label="Reference length to calculate percentage elongations",
        units="mm",
        description="""Reference length to calculate percentage elongations // Referenzlänge zur Berechnung prozentualer Verlängerungen [mm]""",
        mandatory=True,
        section="Values recorded at test start",
    )
    creep_test_reference_length_to_calculate_percentage_extensions = PropertyTypeAssignment(
        code="CREEP_TEST_REFERENCE_LENGTH_TO_CALCULATE_PERCENTAGE_EXTENSIONS",
        data_type="REAL",
        property_label="Reference length to calculate percentage extensions",
        units="mm",
        description="""Reference length to calculate percentage extensions // Referenzlänge zur Berechnung prozentualer Dehnungen [mm]""",
        mandatory=True,
        section="Values recorded at test start",
    )
    creep_test_k_value = PropertyTypeAssignment(
        code="CREEP_TEST_K_VALUE",
        data_type="REAL",
        property_label="k-Value",
        units="mm",
        description="""k-Value - Lr / ?So // k-Wert [mm] - Lr / ?So""",
        mandatory=True,
        section="Values recorded at test start",
    )
    creep_test_ratio_reference_length_to_diameter = PropertyTypeAssignment(
        code="CREEP_TEST_RATIO_REFERENCE_LENGTH_TO_DIAMETER",
        data_type="REAL",
        property_label="Ratio reference length to diameter",
        units="mm",
        description="""Ratio reference length to diameter - Lr / D // Verhältnis Referenzlänge zu Durchmesser [mm] - Lr / D""",
        mandatory=True,
        section="Values recorded at test start",
    )


class CreepTestValuesRecordedDuringTestRunBase(ObjectType):
    defs = ObjectTypeDef(
        code="CREEP_TEST_VALUES_RECORDED_DURING_TEST_RUN_BASE",
        description="""Common properties for data recorded during test run""",
        generated_code_prefix="CREEP_VALUE_RECOR",
    )

    creep_test_elapsed_time_from_end_of_loading = PropertyTypeAssignment(
        code="CREEP_TEST_ELAPSED_TIME_FROM_END_OF_LOADING",
        data_type="REAL",
        property_label="Elapsed time from end of loading",
        units="s / h",
        description="""Elapsed time from end of loading - Link to file, preferably with machine-readable (meta)data. // Verstrichene Zeit seit Ende der Belastung [s / h] - Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=True,
        section="Values recorded during test run",
    )
    creep_test_heating_time = PropertyTypeAssignment(
        code="CREEP_TEST_HEATING_TIME",
        data_type="REAL",
        property_label="Heating time",
        units="h",
        description="""Heating time // Aufheizzeit [h]""",
        mandatory=True,
        section="Values recorded during test run",
    )
    creep_test_soak_time = PropertyTypeAssignment(
        code="CREEP_TEST_SOAK_TIME",
        data_type="REAL",
        property_label="Soak time",
        units="h",
        description="""Soak time - Soak time before the test // Haltezeit [h] - Haltezeit vor der Prüfung""",
        mandatory=True,
        section="Values recorded during test run",
    )
    creep_test_test_duration = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_DURATION",
        data_type="REAL",
        property_label="Test duration",
        units="h",
        description="""Test duration // Prüfdauer [h]""",
        mandatory=True,
        section="Values recorded during test run",
    )


class CreepTestPrimaryValuesRecordedDuringTestRun(
    CreepTestValuesRecordedDuringTestRunBase
):
    defs = ObjectTypeDef(
        code="CREEP_TEST_VALUES_RECORDED_DURING_TEST_RUN_BASE.CREEP_TEST_PRIMARY_VALUES_RECORDED_DURING_TEST_RUN",
        description="""Primary data / Test result / Values recorded during test run // Primärdaten / Prüfergebnis / Während des Versuchs erfasste Werte""",
        generated_code_prefix="CREEP_VALUE_RECOR.CREEP_PRIMA_VALUE",
    )
    creep_test_force = PropertyTypeAssignment(
        code="CREEP_TEST_FORCE",
        data_type="REAL",
        property_label="Force",
        units="kN",
        description="""Force // Kraft [kN]""",
        mandatory=True,
        section="Values recorded during test run",
    )
    creep_test_extension = PropertyTypeAssignment(
        code="CREEP_TEST_EXTENSION",
        data_type="REAL",
        property_label="Extension",
        units="mm",
        description="""Extension - Link to file, preferably with machine-readable (meta)data. // Dehnung [mm] - Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=False,
        section="Values recorded during test run",
    )
    creep_test_elongation = PropertyTypeAssignment(
        code="CREEP_TEST_ELONGATION",
        data_type="REAL",
        property_label="Elongation",
        units="mm",
        description="""Elongation - Link to file, preferably with machine-readable (meta)data. // Verlängerung [mm] - Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=False,
        section="Values recorded during test run",
    )


class CreepTestPrimaryValuesRecordedAfterEndOfTest(ObjectType):
    defs = ObjectTypeDef(
        code="CREEP_TEST_PRIMARY_VALUES_RECORDED_AFTER_END_OF_TEST",
        description="""Primary data / Test result / Values recorded after end of test // Primärdaten / Prüfergebnis / Nach Testende erfasste Werte""",
        generated_code_prefix="CREEP_PRIMA_VALUE",
    )

    creep_test_creep_rupture_time = PropertyTypeAssignment(
        code="CREEP_TEST_CREEP_RUPTURE_TIME",
        data_type="REAL",
        property_label="Creep rupture time",
        units="h",
        description="""Creep rupture time // Kriechbruchzeit [h]""",
        mandatory=True,
        section="Values recorded after end of test",
    )
    creep_test_fracture_position = PropertyTypeAssignment(
        code="CREEP_TEST_FRACTURE_POSITION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_FRACTURE_POSITION",
        property_label="Fracture position",
        description="""Fracture position // Bruchposition""",
        mandatory=True,
        section="Values recorded after end of test",
    )
    creep_test_final_gauge_length_after_fracture = PropertyTypeAssignment(
        code="CREEP_TEST_FINAL_GAUGE_LENGTH_AFTER_FRACTURE",
        data_type="REAL",
        property_label="Final gauge length after fracture",
        units="mm",
        description="""Final gauge length after fracture // Endmesslänge nach Bruch [mm]""",
        mandatory=False,
        section="Values recorded after end of test",
    )


class CreepTestSecondaryValuesRecordedDuringTestRun(
    CreepTestValuesRecordedDuringTestRunBase
):
    defs = ObjectTypeDef(
        code="CREEP_TEST_VALUES_RECORDED_DURING_TEST_RUN_BASE.CREEP_TEST_SECONDARY_VALUES_RECORDED_DURING_TEST_RUN",
        description="""Secondary data / Test result / Values recorded during test run // Sekundärdaten / Prüfergebnis / Während des Versuchs erfasste Werte""",
        generated_code_prefix="CREEP_VALUE_RECOR.CREEP_SECON_VALUE",
    )

    creep_test_loading_rate = PropertyTypeAssignment(
        code="CREEP_TEST_LOADING_RATE",
        data_type="REAL",
        property_label="Loading rate",
        units="MPa/s",
        description="""Loading rate // Belastungsrate [MPa/s]""",
        mandatory=False,
        section="Values recorded during test run",
    )
    creep_test_unloading_rate = PropertyTypeAssignment(
        code="CREEP_TEST_UNLOADING_RATE",
        data_type="REAL",
        property_label="Unloading rate",
        units="MPa/s",
        description="""Unloading rate // Entlastungsrate [MPa/s]""",
        mandatory=False,
        section="Values recorded during test run",
    )
    creep_test_heating_speed = PropertyTypeAssignment(
        code="CREEP_TEST_HEATING_SPEED",
        data_type="REAL",
        property_label="Heating speed",
        units="degC/min",
        description="""Heating speed // Aufheizgeschwindigkeit [?/min]""",
        mandatory=False,
        section="Values recorded during test run",
    )
    creep_test_cooling_speed = PropertyTypeAssignment(
        code="CREEP_TEST_COOLING_SPEED",
        data_type="REAL",
        property_label="Cooling speed",
        units="degC/min",
        description="""Cooling speed // Abkühlgeschwindigkeit [?/min]""",
        mandatory=False,
        section="Values recorded during test run",
    )
    creep_test_percentage_extension = PropertyTypeAssignment(
        code="CREEP_TEST_PERCENTAGE_EXTENSION",
        data_type="REAL",
        property_label="Percentage extension",
        units="%",
        description="""Percentage extension - Link to file, preferably with machine-readable (meta)data. Data series corresponds to the percentage plastic extension from end of loading. If the percentage initial plastic extension is not zero, these data series coresponds to the percentage creep extension from end of loading. // Prozentuale Dehnung [%] - Link to file, preferably with machine-readable (meta)data. Data series corresponds to the percentage plastic extension from end of loading. If the percentage initial plastic extension is not zero, these data series coresponds to the percentage creep extension from end of loading.""",
        mandatory=True,
        section="Values recorded during test run",
    )


class CreepTestSecondaryElongationValues(ObjectType):
    defs = ObjectTypeDef(
        code="CREEP_TEST_SECONDARY_ELONGATION_VALUES",
        description="""Secondary data / Test result / Elongation values // Sekundärdaten / Prüfergebnis / Verlängerungswerte""",
        generated_code_prefix="CREEP_SECON_ELONG",
    )

    creep_test_percentage_permanent_elongation = PropertyTypeAssignment(
        code="CREEP_TEST_PERCENTAGE_PERMANENT_ELONGATION",
        data_type="REAL",
        property_label="Percentage permanent elongation",
        units="%",
        description="""Percentage permanent elongation // Prozentuale bleibende Verlängerung [%]""",
        mandatory=True,
        section="Elongation values",
    )
    creep_test_percentage_elongation_after_creep_fracture = PropertyTypeAssignment(
        code="CREEP_TEST_PERCENTAGE_ELONGATION_AFTER_CREEP_FRACTURE",
        data_type="REAL",
        property_label="Percentage elongation after creep fracture",
        units="%",
        description="""Percentage elongation after creep fracture // Prozentuale Bruchverlängerung nach Kriechbruch [%]""",
        mandatory=True,
        section="Elongation values",
    )
    creep_test_percentage_reduction_of_area_after_creep_fracture = PropertyTypeAssignment(
        code="CREEP_TEST_PERCENTAGE_REDUCTION_OF_AREA_AFTER_CREEP_FRACTURE",
        data_type="REAL",
        property_label="Percentage reduction of area after creep fracture",
        units="%",
        description="""Percentage reduction of area after creep fracture // Prozentuale Brucheinschnürung nach Kriechbruch [%]""",
        mandatory=True,
        section="Elongation values",
    )


class CreepTestSecondaryExtensionValues(ObjectType):
    defs = ObjectTypeDef(
        code="CREEP_TEST_SECONDARY_EXTENSION_VALUES",
        description="""Secondary data / Test result / Extension values // Sekundärdaten / Prüfergebnis / Dehnungswerte""",
        generated_code_prefix="CREEP_SECON_EXTEN",
    )

    creep_test_percentage_total_extension = PropertyTypeAssignment(
        code="CREEP_TEST_PERCENTAGE_TOTAL_EXTENSION",
        data_type="REAL",
        property_label="Percentage total extension",
        units="%",
        description="""Percentage total extension // Prozentuale Gesamtdehnung [%]""",
        mandatory=True,
        section="Extension values",
    )
    creep_test_percentage_initial_total_extension = PropertyTypeAssignment(
        code="CREEP_TEST_PERCENTAGE_INITIAL_TOTAL_EXTENSION",
        data_type="REAL",
        property_label="Percentage initial total extension",
        units="%",
        description="""Percentage initial total extension // Prozentuale anfängliche Gesamtdehnung [%]""",
        mandatory=True,
        section="Extension values",
    )
    creep_test_percentage_elastic_extension = PropertyTypeAssignment(
        code="CREEP_TEST_PERCENTAGE_ELASTIC_EXTENSION",
        data_type="REAL",
        property_label="Percentage elastic extension",
        units="%",
        description="""Percentage elastic extension // Prozentuale elastische Dehnung [%]""",
        mandatory=True,
        section="Extension values",
    )
    creep_test_percentage_initial_plastic_extension = PropertyTypeAssignment(
        code="CREEP_TEST_PERCENTAGE_INITIAL_PLASTIC_EXTENSION",
        data_type="REAL",
        property_label="Percentage initial plastic extension",
        units="%",
        description="""Percentage initial plastic extension // Prozentuale anfängliche plastische Dehnung [%]""",
        mandatory=True,
        section="Extension values",
    )
    creep_test_percentage_plastic_extension = PropertyTypeAssignment(
        code="CREEP_TEST_PERCENTAGE_PLASTIC_EXTENSION",
        data_type="REAL",
        property_label="Percentage plastic extension",
        units="%",
        description="""Percentage plastic extension // Prozentuale plastische Dehnung [%]""",
        mandatory=True,
        section="Extension values",
    )
    creep_test_percentage_creep_extension = PropertyTypeAssignment(
        code="CREEP_TEST_PERCENTAGE_CREEP_EXTENSION",
        data_type="REAL",
        property_label="Percentage creep extension",
        units="%",
        description="""Percentage creep extension // Prozentuale Kriechdehnung [%]""",
        mandatory=True,
        section="Extension values",
    )
