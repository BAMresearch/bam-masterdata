from bam_masterdata.datamodel.object_types import ExperimentalStep
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.entities import ObjectType


class MechanicalTest(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST",
        description="""Mechanical test (experimental step) // Mechanischer Test (Versuchsschritt)""",
        generated_code_prefix="EXP.MECH",
    )


class CreepTest(MechanicalTest):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST",
        description="""Creep test (mechanical) // Kriechversuch (mechanisch)""",
        generated_code_prefix="EXP.MECH.CREEP",
    )

    # --- Links to related creep-test sub-objects (OBJECT properties) ---
    link_material_history_and_condition = PropertyTypeAssignment(
        code="CREEP_TEST.LINK.LINK_MATERIAL_HISTORY_AND_CONDITION",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST_MATERIAL_HISTORY_AND_CONDITION",
        property_label="Material history and condition",
        description="""Linked object: Material history and condition""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked objects",
    )

    link_test_piece = PropertyTypeAssignment(
        code="CREEP_TEST.LINK.LINK_TEST_PIECE",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.TEST_PIECE",
        property_label="Test piece",
        description="""Linked object: Test piece""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked objects",
    )

    link_test_machine = PropertyTypeAssignment(
        code="CREEP_TEST.LINK.LINK_TEST_MACHINE",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.MEASURING_AND_TEST_EQUIPMENT.TEST_MACHINE",
        property_label="Test machine",
        description="""Linked object: Test machine""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked objects",
    )

    link_test_machine_heating_system = PropertyTypeAssignment(
        code="CREEP_TEST.LINK.LINK_TEST_MACHINE_HEATING_SYSTEM",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.MEASURING_AND_TEST_EQUIPMENT.TEST_MACHINE.HEATING_SYSTEM",
        property_label="Heating system",
        description="""Linked object: Heating system""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked objects",
    )

    link_test_machine_holder_system = PropertyTypeAssignment(
        code="CREEP_TEST.LINK.LINK_TEST_MACHINE_HOLDER_SYSTEM",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.MEASURING_AND_TEST_EQUIPMENT.TEST_MACHINE.TEST_PIECE_HOLDER_SYSTEM",
        property_label="Test piece holder system",
        description="""Linked object: Test piece holder system""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked objects",
    )

    link_test_machine_loading_system = PropertyTypeAssignment(
        code="CREEP_TEST.LINK.LINK_TEST_MACHINE_LOADING_SYSTEM",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.MEASURING_AND_TEST_EQUIPMENT.TEST_MACHINE.LOADING_SYSTEM",
        property_label="Loading system",
        description="""Linked object: Loading system""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked objects",
    )

    link_test_machine_data_acquisition = PropertyTypeAssignment(
        code="CREEP_TEST.LINK.LINK_TEST_MACHINE_DATA_ACQUISITION",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.MEASURING_AND_TEST_EQUIPMENT.TEST_MACHINE.DATA_ACQUISITION",
        property_label="Data acquisition (test machine)",
        description="""Linked object: Data acquisition (test machine)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked objects",
    )

    link_load_sensor = PropertyTypeAssignment(
        code="CREEP_TEST.LINK.LINK_LOAD_SENSOR",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.MEASURING_AND_TEST_EQUIPMENT.LOAD_MEASURING_SYSTEM.LOAD_SENSOR",
        property_label="Load sensor",
        description="""Linked object: Load sensor""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked objects",
    )

    link_load_measuring_data_acquisition = PropertyTypeAssignment(
        code="CREEP_TEST.LINK.LINK_LOAD_MEASURING_DATA_ACQUISITION",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.MEASURING_AND_TEST_EQUIPMENT.LOAD_MEASURING_SYSTEM.DATA_ACQUISITION",
        property_label="Load measuring system data acquisition",
        description="""Linked object: Load measuring system data acquisition""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked objects",
    )

    link_laboratory_conditions = PropertyTypeAssignment(
        code="CREEP_TEST.LINK.LINK_LABORATORY_CONDITIONS",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.METADATA.MEASURING_AND_TEST_EQUIPMENT.LABORATORY_CONDITIONS",
        property_label="Laboratory conditions",
        description="""Linked object: Laboratory conditions""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked objects",
    )

    link_temperature_measuring_system = PropertyTypeAssignment(
        code="CREEP_TEST.LINK.LINK_TEMPERATURE_MEASURING_SYSTEM",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.METADATA.MEASURING_AND_TEST_EQUIPMENT.TEMPERATURE_MEASURING_SYSTEM",
        property_label="Temperature-measuring system",
        description="""Linked object: Temperature-measuring system""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked objects",
    )

    link_temperature_sensor = PropertyTypeAssignment(
        code="CREEP_TEST.LINK.LINK_TEMPERATURE_SENSOR",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.METADATA.MEASURING_AND_TEST_EQUIPMENT.TEMPERATURE_MEASURING_SYSTEM.TEMPERATURE_SENSOR",
        property_label="Temperature sensor",
        description="""Linked object: Temperature sensor""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked objects",
    )

    link_temperature_daq = PropertyTypeAssignment(
        code="CREEP_TEST.LINK.LINK_TEMPERATURE_DAQ",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.METADATA.MEASURING_AND_TEST_EQUIPMENT.TEMPERATURE_MEASURING_SYSTEM.DATA_ACQUISITION",
        property_label="Temperature DAQ",
        description="""Linked object: Temperature measuring system data acquisition""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked objects",
    )

    link_extensometer_system = PropertyTypeAssignment(
        code="CREEP_TEST.LINK.LINK_EXTENSOMETER_SYSTEM",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.METADATA.MEASURING_AND_TEST_EQUIPMENT.EXTENSOMETER_SYSTEM",
        property_label="Extensometer system",
        description="""Linked object: Extensometer system""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked objects",
    )

    link_contacting_extensometer = PropertyTypeAssignment(
        code="CREEP_TEST.LINK.LINK_CONTACTING_EXTENSOMETER",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.METADATA.MEASURING_AND_TEST_EQUIPMENT.EXTENSION_VALUES.CONTACTING_EXTENSOMETER",
        property_label="Contacting extensometer",
        description="""Linked object: Contacting extensometer""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked objects",
    )

    link_elongation_cross_sectional = PropertyTypeAssignment(
        code="CREEP_TEST.LINK.LINK_ELONGATION_CROSS_SECTIONAL",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.METADATA.MEASURING_AND_TEST_EQUIPMENT.ELONGATION_VALUES_AND_CROSS_SECTIONAL_DIMENSIONS",
        property_label="Elongation & cross-sectional dimensions",
        description="""Linked object: Elongation values and cross-sectional dimensions""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked objects",
    )

    link_data_processing = PropertyTypeAssignment(
        code="CREEP_TEST.LINK.LINK_DATA_PROCESSING",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.METADATA.DATA_PROCESSING_PROCEDURES",
        property_label="Data processing procedures",
        description="""Linked object: Data processing procedures""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked objects",
    )

    link_primary_data_at_start = PropertyTypeAssignment(
        code="CREEP_TEST.LINK.LINK_PRIMARY_DATA_AT_START",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.PRIMARY_DATA.TEST_RESULT.VALUES_RECORDED_AT_TEST_START",
        property_label="Primary data at test start",
        description="""Linked object: Primary data (values at test start)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked objects",
    )

    link_primary_data_during_run = PropertyTypeAssignment(
        code="CREEP_TEST.LINK.LINK_PRIMARY_DATA_DURING_RUN",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.PRIMARY_DATA.TEST_RESULT.VALUES_RECORDED_DURING_TEST_RUN",
        property_label="Primary data during test run",
        description="""Linked object: Primary data (values during test run)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked objects",
    )

    link_primary_data_after_end = PropertyTypeAssignment(
        code="CREEP_TEST.LINK.LINK_PRIMARY_DATA_AFTER_END",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.PRIMARY_DATA.TEST_RESULT.VALUES_RECORDED_AFTER_END_OF_TEST",
        property_label="Primary data after end of test",
        description="""Linked object: Primary data (values after end of test)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked objects",
    )

    link_secondary_data_during_run = PropertyTypeAssignment(
        code="CREEP_TEST.LINK.LINK_SECONDARY_DATA_DURING_RUN",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.SECONDARY_DATA.TEST_RESULT.VALUES_RECORDED_DURING_TEST_RUN",
        property_label="Secondary data during test run",
        description="""Linked object: Secondary data (values during test run)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked objects",
    )

    link_secondary_elongation_values = PropertyTypeAssignment(
        code="CREEP_TEST.LINK.LINK_SECONDARY_ELONGATION_VALUES",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.SECONDARY_DATA.TEST_RESULT.ELONGATION_VALUES",
        property_label="Secondary elongation values",
        description="""Linked object: Secondary data (elongation values)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked objects",
    )

    link_secondary_extension_values = PropertyTypeAssignment(
        code="CREEP_TEST.LINK.LINK_SECONDARY_EXTENSION_VALUES",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.SECONDARY_DATA.TEST_RESULT.EXTENSION_VALUES",
        property_label="Secondary extension values",
        description="""Linked object: Secondary data (extension values)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked objects",
    )

    # ---------------------------
    # Section: Metadata - Test info - Test job details
    # ---------------------------

    creep_test_date_of_test_start = PropertyTypeAssignment(
        code="START_DATE",
        data_type="TIMESTAMP",
        property_label="Date of test start",
        description="""Date of test start // Startdatum der Prüfung""",
        mandatory=True,
        show_in_edit_views=False,
        section="Test job details",
    )

    creep_test_date_of_test_end = PropertyTypeAssignment(
        code="END_DATE",
        data_type="TIMESTAMP",
        property_label="Date of test end",
        description="""Date of test end // Enddatum der Prüfung""",
        mandatory=True,
        show_in_edit_views=False,
        section="Test job details",
    )

    creep_test_test_id = PropertyTypeAssignment(
        code="CREEP_TEST.TEST_ID",
        data_type="VARCHAR",
        property_label="Test ID",
        description="""Test ID // Prüf-ID""",
        mandatory=True,
        show_in_edit_views=False,
        section="Test job details",
    )

    creep_test_project = PropertyTypeAssignment(
        code="REQUEST.PROJECT",
        data_type="VARCHAR",
        property_label="Project",
        description="""Project // Projekt""",
        mandatory=False,
        show_in_edit_views=False,
        section="Test job details",
    )

    # ---------------------------
    # Section: Metadata - Test info - Test parameters
    # ---------------------------

    creep_test_test_standard_applied = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_STANDARD_APPLIED",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TEST_STANDARD_APPLIED",
        property_label="Test standard applied",
        description="""Test standard applied - Was the test performed according to a test standard? // Prüfnorm angewendet – Wurde die Prüfung gemäß einer Prüfnorm durchgeführt?""",
        mandatory=True,
        show_in_edit_views=False,
        section="Test parameters",
    )

    creep_test_test_standard = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_STANDARD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_TEST_STANDARD",
        property_label="Test standard",
        description="""Test standard // Prüfnorm""",
        mandatory=True,
        show_in_edit_views=False,
        section="Test parameters",
    )

    creep_test_specified_temperature = PropertyTypeAssignment(
        code="ATOM_MD_TARG_TEMP_IN_K",
        data_type="REAL",
        property_label="Specified temperature [K]",
        description="""Specified temperature // Vorgegebene Temperatur""",
        mandatory=True,
        show_in_edit_views=False,
        section="Test parameters",
    )

    creep_test_type_of_loading = PropertyTypeAssignment(
        code="CREEP_TEST_TYPE_OF_LOADING",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_TYPE_OF_LOADING",
        property_label="Type of loading",
        description="""Type of loading // Art der Belastung""",
        mandatory=True,
        show_in_edit_views=False,
        section="Test parameters",
    )

    creep_test_load_control_type = PropertyTypeAssignment(
        code="CREEP_TEST_LOAD_CONTROL_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_LOAD_CONTROL_TYPE",
        property_label="Load control type",
        description="""Load control type // Lastregelungsart""",
        mandatory=True,
        show_in_edit_views=False,
        section="Test parameters",
    )

    creep_test_initial_stress = PropertyTypeAssignment(
        code="CREEP_TEST_INITIAL_STRESS",
        data_type="REAL",
        property_label="Initial stress [MPa]",
        description="""Initial stress // Anfangsspannung""",
        mandatory=True,
        show_in_edit_views=False,
        section="Test parameters",
    )

    creep_test_test_type = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_TEST_TYPE",
        property_label="Test type",
        description="""Test type // Prüftyp""",
        mandatory=True,
        show_in_edit_views=False,
        section="Test parameters",
    )

    creep_test_end_of_test_criterium = PropertyTypeAssignment(
        code="CREEP_TEST_END_OF_TEST_CRITERIUM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_END_OF_TEST_CRITERIUM",
        property_label="End of test criterium",
        description="""End of test criterium // Abbruchkriterium""",
        mandatory=True,
        show_in_edit_views=False,
        section="Test parameters",
    )

    creep_test_time_limit = PropertyTypeAssignment(
        code="CREEP_TEST_TIME_LIMIT",
        data_type="VARCHAR",
        property_label="Time Limit",
        description="""Time Limit // Zeitlimit""",
        mandatory=True,
        show_in_edit_views=False,
        section="Test parameters",
    )

    creep_test_extension_limit = PropertyTypeAssignment(
        code="CREEP_TEST_EXTENSION_LIMIT",
        data_type="VARCHAR",
        property_label="Extension Limit",
        description="""Extension Limit // Dehnungsgrenze""",
        mandatory=True,
        show_in_edit_views=False,
        section="Test parameters",
    )

    creep_test_end_of_test = PropertyTypeAssignment(
        code="CREEP_TEST_END_OF_TEST",
        data_type="VARCHAR",
        property_label="End of test",
        description="""End of test - Describe the end of test if none of the preset criteria (time or extension limit) could be met // Testende – Beschreiben Sie das Testende, falls keines der vorgegebenen Kriterien (Zeit- oder Dehnungsgrenze) erreicht werden konnte.""",
        mandatory=False,
        show_in_edit_views=False,
        section="Test parameters",
    )

    creep_test_interruption_course = PropertyTypeAssignment(
        code="CREEP_TEST_INTERRUPTION_COURSE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_INTERRUPTION_COURSE",
        property_label="Interruption course",
        description="""Interruption course // Unterbrechungsverlauf""",
        mandatory=True,
        show_in_edit_views=False,
        section="Test parameters",
    )

    creep_test_test_force = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_FORCE",
        data_type="REAL",
        property_label="Test force [kN]",
        description="""Test force // Prüfkraft""",
        mandatory=False,
        show_in_edit_views=False,
        section="Test parameters",
    )

    creep_test_preload = PropertyTypeAssignment(
        code="CREEP_TEST_PRELOAD",
        data_type="REAL",
        property_label="Preload [kN]",
        description="""Preload - Part of the test force // Vorspannkraft – Teil der Prüfkraft""",
        mandatory=True,
        show_in_edit_views=False,
        section="Test parameters",
    )

    creep_test_additional_information = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Additional information",
        description="""Additional information // Zusätzliche Informationen""",
        mandatory=False,
        show_in_edit_views=False,
        section="Test parameters",
    )

    # --------------------------------
    # Section: Metadata - Test info - Related research outcome
    # --------------------------------

    creep_test_any_related_articles = PropertyTypeAssignment(
        code="CREEP_TEST_ANY_RELATED_ARTICLES",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_ANY_RELATED_ARTICLES",
        property_label="Any related articles",
        description="""Any related articles // Zugehörige Artikel vorhanden""",
        mandatory=False,
        show_in_edit_views=False,
        section="Related research outcome",
    )

    creep_test_related_article = PropertyTypeAssignment(
        code="CREEP_TEST_RELATED_ARTICLE",
        data_type="MULTILINE_VARCHAR",
        property_label="Related article",
        description="""Related article - Multiple input entries for instance for MSE research article DOI, Zenodo DOI, FDO // Zugehöriger Artikel – Mehrfache Eingaben, z. B. für DOI eines Fachartikels, Zenodo-DOI, FDO.""",
        mandatory=False,
        show_in_edit_views=False,
        section="Related research outcome",
    )


class CreepTestMaterialHistoryAndCondition(ObjectType):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST_MATERIAL_HISTORY_AND_CONDITION",
        description="""Material history and condition for creep tests // Materialhistorie und -zustand für Kriechversuche""",
        generated_code_prefix="EXP.MECH.CREEP.MAT_HIST",
    )

    # --- Links to material sub-objects (OBJECT properties) ---
    link_chemical_composition_nominal = PropertyTypeAssignment(
        code="CREEP_TEST.MATERIAL.LINK.LINK_CHEMICAL_COMPOSITION_NOMINAL",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.MATERIAL_HISTORY_AND_CONDITION.CHEMICAL_COMPOSITION.NOMINAL",
        property_label="Chemical composition (nominal)",
        description="""Linked object: Chemical composition (nominal)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked material objects",
    )

    link_chemical_composition_measured = PropertyTypeAssignment(
        code="CREEP_TEST.MATERIAL.LINK.LINK_CHEMICAL_COMPOSITION_MEASURED",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.MATERIAL_HISTORY_AND_CONDITION.CHEMICAL_COMPOSITION.MEASURED",
        property_label="Chemical composition (measured)",
        description="""Linked object: Chemical composition (measured)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked material objects",
    )

    link_ndt_results = PropertyTypeAssignment(
        code="CREEP_TEST.MATERIAL.LINK.LINK_NDT_RESULTS",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.MATERIAL_HISTORY_AND_CONDITION.NDT_RESULTS",
        property_label="NDT results",
        description="""Linked object: NDT results""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked material objects",
    )

    link_mechanical_tests_results = PropertyTypeAssignment(
        code="CREEP_TEST.MATERIAL.LINK.LINK_MECHANICAL_TESTS_RESULTS",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.MATERIAL_HISTORY_AND_CONDITION.MECHANICAL_TESTS_RESULTS",
        property_label="Mechanical tests results",
        description="""Linked object: Mechanical tests results""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked material objects",
    )

    # --------------------------------
    # Section: Metadata - Material history and condition
    # --------------------------------

    creep_test_material_identifier = PropertyTypeAssignment(
        code="CREEP_TEST_MATERIAL_IDENTIFIER",
        data_type="VARCHAR",
        property_label="Material Identifier // Materialkennung",
        description="""Material Identifier - E.g., NIMONIC 75, 2.4630, CMSX-6, CMSX-4, ERBO1, // Materialkennung – z. B. NIMONIC 75, 2.4630, CMSX-6, CMSX-4, ERBO1,""",
        mandatory=True,
        show_in_edit_views=False,
        section="Material history and condition",
    )

    # Section: As-manufactured material
    creep_test_phase_transformation_during_test = PropertyTypeAssignment(
        code="CREEP_TEST_PHASE_TRANSFORMATION_DURING_TEST",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_PHASE_TRANSFORMATION_DURING_TEST",
        property_label="Phase transformation during test // Phasenumwandlung während der Prüfung",
        description="""Phase transformation during test // Phasenumwandlung während der Prüfung""",
        mandatory=False,
        show_in_edit_views=False,
        section="As-manufactured material",
    )

    creep_test_possible_phase_transformation = PropertyTypeAssignment(
        code="CREEP_TEST_POSSIBLE_PHASE_TRANSFORMATION",
        data_type="VARCHAR",
        property_label="Possible phase transformation // Mögliche Phasenumwandlung",
        description="""Possible phase transformation - Is any phase transformation expected due to temperature during the creep test?. Please provide any supporting material if possible. Answers could be, e.g., a link to a TTT-curve or a DOI of an article // Mögliche Phasenumwandlung – Wird aufgrund der Temperatur während des Kriechversuchs eine Phasenumwandlung erwartet? Bitte fügen Sie nach Möglichkeit unterstützendes Material bei (z. B. Link zu einer ZTU-/TTT-Kurve oder DOI eines Artikels).""",
        mandatory=False,
        show_in_edit_views=False,
        section="As-manufactured material",
    )

    creep_test_form_of_as_manufactured_material = PropertyTypeAssignment(
        code="CREEP_TEST_FORM_OF_AS_MANUFACTURED_MATERIAL",
        data_type="VARCHAR",
        property_label="Form of as-manufactured material // Form des Materials im Herstellungszustand",
        description="""Form of as-manufactured material - E.g., Cast, Ingot, Extrusion rod, // Form des Materials im Herstellungszustand – z. B. Guss, Block (Ingot), Extrusionsstab,""",
        mandatory=True,
        show_in_edit_views=False,
        section="As-manufactured material",
    )

    creep_test_geometry_size_as_manufactured_material = PropertyTypeAssignment(
        code="CREEP_TEST_GEOMETRY_SIZE_AS_MANUFACTURED_MATERIAL",
        data_type="VARCHAR",
        property_label="Geometry/size as-manufactured material // Geometrie/Abmessungen des Materials im Herstellungszustand",
        description="""Geometry/size as-manufactured material - Please provide a description or/and any supporting material, e.g., link to image or technical drawing, if possible. // Geometrie/Abmessungen des Materials im Herstellungszustand – Bitte geben Sie eine Beschreibung und/oder nach Möglichkeit unterstützendes Material an (z. B. Link zu einem Bild oder einer technischen Zeichnung).""",
        mandatory=True,
        show_in_edit_views=False,
        section="As-manufactured material",
    )

    creep_test_manufacturing_process_description_as_manufactured_material = PropertyTypeAssignment(
        code="CREEP_TEST_MANUFACTURING_PROCESS_DESCRIPTION_AS_MANUFACTURED_MATERIAL",
        data_type="VARCHAR",
        property_label="Manufacturing process description as-manufactured material // Beschreibung des Herstellungsprozesses (Herstellungszustand)",
        description="""Manufacturing process description as-manufactured material - E.g., Cast / Melting, Casting, and Remelting / Induction melting in air, casting into a circular ingot and then electroslag remelting // Beschreibung des Herstellungsprozesses (Herstellungszustand) – z. B. Guss / Schmelzen, Gießen und Umschmelzen / Induktionsschmelzen in Luft, Gießen in einen Rundblock und anschließend Elektroschlacke-Umschmelzen""",
        mandatory=False,
        show_in_edit_views=False,
        section="As-manufactured material",
    )

    creep_test_casting_temperature = PropertyTypeAssignment(
        code="CREEP_TEST_CASTING_TEMPERATURE",
        data_type="REAL",
        property_label="Casting temperature [°C] // Gießtemperatur [°C]",
        description="""Casting temperature // Gießtemperatur [°C]""",
        mandatory=False,
        show_in_edit_views=False,
        section="As-manufactured material",
    )

    creep_test_casting_speed = PropertyTypeAssignment(
        code="CREEP_TEST_CASTING_SPEED",
        data_type="REAL",
        property_label="Casting speed // Gießgeschwindigkeit",
        description="""Casting speed // Gießgeschwindigkeit""",
        mandatory=False,
        show_in_edit_views=False,
        section="As-manufactured material",
    )

    creep_test_solidification = PropertyTypeAssignment(
        code="CREEP_TEST_SOLIDIFICATION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_SOLIDIFICATION",
        property_label="Solidification // Erstarrungsform",
        description="""Solidification - Single/Polycrystal solidified? // Erstarrungsform – Einkristallin oder polykristallin erstarrt?""",
        mandatory=True,
        show_in_edit_views=False,
        section="As-manufactured material",
    )

    creep_test_condition = PropertyTypeAssignment(
        code="CREEP_TEST_CONDITION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_CONDITION",
        property_label="Condition // Zustand",
        description="""Condition // Zustand""",
        mandatory=True,
        show_in_edit_views=False,
        section="As-manufactured material",
    )

    # Section: As-tested material
    creep_test_supplier = PropertyTypeAssignment(
        code="SUPPLIER",
        data_type="VARCHAR",
        property_label="Supplier // Lieferant",
        description="""Supplier // Lieferant""",
        mandatory=True,
        show_in_edit_views=False,
        section="As-tested material",
    )

    creep_test_geometry_size_as_tested_material = PropertyTypeAssignment(
        code="CREEP_TEST_GEOMETRY_SIZE_AS_TESTED_MATERIAL",
        data_type="VARCHAR",
        property_label="Geometry/size as-tested material // Geometrie/Abmessungen des Materials im Prüfzustand",
        description="""Geometry/size as-tested material - The test piece is manufactured from the as-tested material. Please add a description or a link to Image or technical drawing. The as-tested material is the material to be tested. The as-tested material can be a component. // Geometrie/Abmessungen des Materials im Prüfzustand – Der Probekörper wird aus dem Material im Prüfzustand gefertigt. Bitte fügen Sie eine Beschreibung oder einen Link zu Bild/technischer Zeichnung hinzu. Das Material im Prüfzustand ist das zu prüfende Material und kann auch ein Bauteil sein.""",
        mandatory=True,
        show_in_edit_views=False,
        section="As-tested material",
    )

    creep_test_manufacturing_process_description_as_tested_material = PropertyTypeAssignment(
        code="CREEP_TEST_MANUFACTURING_PROCESS_DESCRIPTION_AS_TESTED_MATERIAL",
        data_type="VARCHAR",
        property_label="Manufacturing process description as-tested material // Beschreibung des Herstellungsprozesses (Prüfzustand)",
        description="""Manufacturing process description as-tested material // Beschreibung des Herstellungsprozesses (Prüfzustand)""",
        mandatory=True,
        show_in_edit_views=False,
        section="As-tested material",
    )

    creep_test_supply_date = PropertyTypeAssignment(
        code="SAMPLE_RECEIVED",
        data_type="TIMESTAMP",
        property_label="Supply Date // Lieferdatum",
        description="""Supply Date // Lieferdatum""",
        mandatory=True,
        show_in_edit_views=False,
        section="As-tested material",
    )

    creep_test_order_number = PropertyTypeAssignment(
        code="$ORDER.ADDITIONAL_INFORMATION",
        data_type="VARCHAR",
        property_label="Order number // Bestellnummer",
        description="""Order number // Bestellnummer""",
        mandatory=False,
        show_in_edit_views=False,
        section="As-tested material",
    )

    # Section: Heat treatment
    creep_test_heat_treatment_state = PropertyTypeAssignment(
        code="CREEP_TEST_HEAT_TREATMENT_STATE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_HEAT_TREATMENT_STATE",
        property_label="Heat treatment - State // Wärmebehandlungszustand",
        description="""Heat treatment - State // Wärmebehandlungszustand""",
        mandatory=True,
        show_in_edit_views=False,
        section="Heat treatment",
    )

    creep_test_multistage_annealing = PropertyTypeAssignment(
        code="CREEP_TEST_MULTISTAGE_ANNEALING",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_MULTISTAGE_ANNEALING",
        property_label="Multistage annealing? // Mehrstufiges Glühen?",
        description="""Multistage annealing? // Mehrstufiges Glühen?""",
        mandatory=False,
        show_in_edit_views=False,
        section="Heat treatment",
    )

    creep_test_multistage_ageing = PropertyTypeAssignment(
        code="CREEP_TEST_MULTISTAGE_AGEING",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_MULTISTAGE_AGEING",
        property_label="Multistage ageing? // Mehrstufiges Auslagern?",
        description="""Multistage ageing? // Mehrstufiges Auslagern?""",
        mandatory=False,
        show_in_edit_views=False,
        section="Heat treatment",
    )

    creep_test_heat_treatment_annealing_description = PropertyTypeAssignment(
        code="CREEP_TEST_HEAT_TREATMENT_ANNEALING_DESCRIPTION",
        data_type="VARCHAR",
        property_label="Heat treatment - Annealing - Description // Wärmebehandlung – Glühen – Beschreibung",
        description="""Heat treatment - Annealing - Description // Wärmebehandlung – Glühen – Beschreibung""",
        mandatory=True,
        show_in_edit_views=False,
        section="Heat treatment",
    )

    creep_test_heat_treatment_ageing_description = PropertyTypeAssignment(
        code="CREEP_TEST_HEAT_TREATMENT_AGEING_DESCRIPTION",
        data_type="VARCHAR",
        property_label="Heat treatment - Ageing - Description // Wärmebehandlung – Auslagern – Beschreibung",
        description="""Heat treatment - Ageing - Description // Wärmebehandlung – Auslagern – Beschreibung""",
        mandatory=True,
        show_in_edit_views=False,
        section="Heat treatment",
    )

    creep_test_heat_treatment_protocol = PropertyTypeAssignment(
        code="CREEP_TEST_HEAT_TREATMENT_PROTOCOL",
        data_type="VARCHAR",
        property_label="Heat treatment - Protocol // Wärmebehandlung – Protokoll",
        description="""Heat treatment - Protocol - Link to file, preferably with machine-readable (meta)dataeta)data // Wärmebehandlung – Protokoll – Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=False,
        show_in_edit_views=False,
        section="Heat treatment",
    )

    # Section: Microstructure
    creep_test_microstructure_feature = PropertyTypeAssignment(
        code="CREEP_TEST_MICROSTRUCTURE_FEATURE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_MICROSTRUCTURE_FEATURE",
        property_label="Microstructure feature // Mikrostrukturmerkmal",
        description="""Microstructure feature // Mikrostrukturmerkmal""",
        mandatory=True,
        show_in_edit_views=False,
        section="Microstructure",
    )

    creep_test_characterization_method = PropertyTypeAssignment(
        code="CREEP_TEST_CHARACTERIZATION_METHOD",
        data_type="VARCHAR",
        property_label="Characterization method // Charakterisierungsmethode",
        description="""Characterization method - E.g., STEM, HRTEM, TEM-EDX, AFM, SEM, SEM-EBSD, .... // Charakterisierungsmethode – z. B. STEM, HRTEM, TEM-EDX, AFM, SEM, SEM-EBSD, …""",
        mandatory=True,
        show_in_edit_views=False,
        section="Microstructure",
    )

    creep_test_measured_condition = PropertyTypeAssignment(
        code="CREEP_TEST_MEASURED_CONDITION",
        data_type="VARCHAR",
        property_label="Measured condition // Gemessener Zustand",
        description="""Measured condition - E.g., as-manufactured, heat-treated, before testing, after testing // Gemessener Zustand – z. B. wie hergestellt, wärmebehandelt, vor der Prüfung, nach der Prüfung""",
        mandatory=True,
        show_in_edit_views=False,
        section="Microstructure",
    )

    creep_test_measuring_position = PropertyTypeAssignment(
        code="CREEP_TEST_MEASURING_POSITION",
        data_type="VARCHAR",
        property_label="Measuring position // Messposition",
        description="""Measuring position - Specify position(s) for bulk (middle/top/bottom/surface) and/or microstructure feature (matrix, interdendtitic region, phase,...) // Messposition – Geben Sie Position(en) an, z. B. im Volumen (Mitte/oben/unten/Oberfläche) und/oder bezogen auf das Mikrostrukturmerkmal (Matrix, interdendritischer Bereich, Phase, …).""",
        mandatory=True,
        show_in_edit_views=False,
        section="Microstructure",
    )

    creep_test_microstructure_feature_information = PropertyTypeAssignment(
        code="CREEP_TEST_MICROSTRUCTURE_FEATURE_INFORMATION",
        data_type="VARCHAR",
        property_label="Microstructure feature - Information // Mikrostrukturmerkmal – Informationen",
        description="""Microstructure feature - Information - Include all relevant characterization results // Mikrostrukturmerkmal – Informationen – Führen Sie alle relevanten Charakterisierungsergebnisse auf.""",
        mandatory=False,
        show_in_edit_views=False,
        section="Microstructure",
    )

    creep_test_microstructure_image = PropertyTypeAssignment(
        code="CREEP_TEST_MICROSTRUCTURE_IMAGE",
        data_type="VARCHAR",
        property_label="Microstructure Image // Mikrostrukturbild",
        description="""Microstructure Image - Link to File, e.g., an optical micrograph, preferably with machine-readable (meta)data // Mikrostrukturbild – Link zu einer Datei, z. B. zu einem optischen Mikrographen, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=False,
        show_in_edit_views=False,
        section="Microstructure",
    )

    creep_test_microstructure_report = PropertyTypeAssignment(
        code="CREEP_TEST_MICROSTRUCTURE_REPORT",
        data_type="VARCHAR",
        property_label="Microstructure report // Mikrostrukturbericht",
        description="""Microstructure report - Link to file, preferably with machine-readable (meta)data // Mikrostrukturbericht – Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=False,
        show_in_edit_views=False,
        section="Microstructure",
    )

    creep_test_grain_size = PropertyTypeAssignment(
        code="CREEP_TEST_GRAIN_SIZE",
        data_type="REAL",
        property_label="Grain size [µm] // Korngröße [µm]",
        description="""Grain size - If polycrystal // Korngröße [µm] – Falls polykristallin.""",
        mandatory=True,
        show_in_edit_views=False,
        section="Microstructure",
    )

    creep_test_grain_size_determination_method = PropertyTypeAssignment(
        code="CREEP_TEST_GRAIN_SIZE_DETERMINATION_METHOD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_GRAIN_SIZE_DETERMINATION_METHOD",
        property_label="Grain size - Determination method // Korngröße – Bestimmungsmethode",
        description="""Grain size - Determination method // Korngröße – Bestimmungsmethode""",
        mandatory=True,
        show_in_edit_views=False,
        section="Microstructure",
    )

    creep_test_grain_size_measuring_region = PropertyTypeAssignment(
        code="CREEP_TEST_GRAIN_SIZE_MEASURING_REGION",
        data_type="VARCHAR",
        property_label="Grain size - measuring region // Korngröße – Messbereich",
        description="""Grain size - measuring region - E.g., in the bulk // Korngröße – Messbereich – z. B. im Volumen""",
        mandatory=True,
        show_in_edit_views=False,
        section="Microstructure",
    )

    creep_test_grain_size_distribution = PropertyTypeAssignment(
        code="CREEP_TEST_GRAIN_SIZE_DISTRIBUTION",
        data_type="VARCHAR",
        property_label="Grain size distribution // Korngrößenverteilung",
        description="""Grain size distribution - Link to file, preferably with machine-readable (meta)data // Korngrößenverteilung – Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=False,
        show_in_edit_views=False,
        section="Microstructure",
    )

    creep_test_grain_additional_information = PropertyTypeAssignment(
        code="CREEP_TEST_GRAIN_ADDITIONAL_INFORMATION",
        data_type="VARCHAR",
        property_label="Grain - Additional Information // Korn – Zusätzliche Informationen",
        description="""Grain - Additional Information - Include all further relevant characterization results // Korn – Zusätzliche Informationen – Führen Sie weitere relevante Charakterisierungsergebnisse auf.""",
        mandatory=False,
        show_in_edit_views=False,
        section="Microstructure",
    )

    creep_test_reprecipitated_gamma_gamma_prime_regions = PropertyTypeAssignment(
        code="CREEP_TEST_REPRECIPITATED_GAMMA_GAMMA_PRIME_REGIONS",
        data_type="VARCHAR",
        property_label="Reprecipitated gamma-gamma prime regions [%] // Wieder ausgeschiedene Gamma/Gamma′-Bereiche [%]",
        description="""Reprecipitated gamma-gamma prime regions - Completely dissolved and re-precipitated gamma-gamma' regions // Wieder ausgeschiedene Gamma/Gamma′-Bereiche [%] – Vollständig gelöste und wieder ausgeschiedene Gamma/Gamma′-Bereiche""",
        mandatory=False,
        show_in_edit_views=False,
        section="Microstructure",
    )

    creep_test_gamma_prime_particles_average_size = PropertyTypeAssignment(
        code="CREEP_TEST_GAMMA_PRIME_PARTICLES_AVERAGE_SIZE",
        data_type="VARCHAR",
        property_label="Gamma prime particles - average size [µm] // Gamma′-Partikel – mittlere Größe [µm]",
        description="""Gamma prime particles - average size // Gamma′-Partikel – mittlere Größe [µm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Microstructure",
    )

    creep_test_gamma_prime_particles_maximum_size = PropertyTypeAssignment(
        code="CREEP_TEST_GAMMA_PRIME_PARTICLES_MAXIMUM_SIZE",
        data_type="REAL",
        property_label="Gamma prime particles - maximum size [µm] // Gamma′-Partikel – maximale Größe [µm]",
        description="""Gamma prime particles - maximum size // Gamma′-Partikel – maximale Größe [µm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Microstructure",
    )

    creep_test_dendrite_spacings = PropertyTypeAssignment(
        code="CREEP_TEST_DENDRITE_SPACINGS",
        data_type="VARCHAR",
        property_label="Dendrite spacings // Dendritenabstände",
        description="""Dendrite spacings - Please describe the procedure and add a link to file, preferably with machine-readable (meta)data or add a reference to paper and section // Dendritenabstände – Bitte beschreiben Sie das Verfahren und fügen Sie einen Dateilink (vorzugsweise mit maschinenlesbaren (Meta-)Daten) oder eine Referenz auf Publikation und Abschnitt hinzu.""",
        mandatory=False,
        show_in_edit_views=False,
        section="Microstructure",
    )

    creep_test_proof_of_single_crystallinity = PropertyTypeAssignment(
        code="CREEP_TEST_PROOF_OF_SINGLE_CRYSTALLINITY",
        data_type="VARCHAR",
        property_label="Proof of single crystallinity // Nachweis der Einkristallinität",
        description="""Proof of single crystallinity - Link to file, preferably with machine-readable (meta)data // Nachweis der Einkristallinität – Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=False,
        show_in_edit_views=False,
        section="Microstructure",
    )

    creep_test_single_crystal_orientation = PropertyTypeAssignment(
        code="CREEP_TEST_SINGLE_CRYSTAL_ORIENTATION",
        data_type="VARCHAR",
        property_label="Single crystal orientation // Einkristallorientierung",
        description="""Single crystal orientation - Link to file, preferably with machine-readable (meta)data. Laue Crystal Verification. Must be documented for each test piece. // Einkristallorientierung – Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten. Laue-Einkristallprüfung; muss für jeden Probekörper dokumentiert werden.""",
        mandatory=True,
        show_in_edit_views=False,
        section="Microstructure",
    )

    creep_test_single_crystal_orientation_determination_method = PropertyTypeAssignment(
        code="CREEP_TEST_SINGLE_CRYSTAL_ORIENTATION_DETERMINATION_METHOD",
        data_type="VARCHAR",
        property_label="Single crystal orientation - Determination method // Einkristallorientierung – Bestimmungsmethode",
        description="""Single crystal orientation - Determination method // Einkristallorientierung – Bestimmungsmethode""",
        mandatory=True,
        show_in_edit_views=False,
        section="Microstructure",
    )

    creep_test_single_crystal_orientation_measuring_point = PropertyTypeAssignment(
        code="CREEP_TEST_SINGLE_CRYSTAL_ORIENTATION_MEASURING_POINT",
        data_type="VARCHAR",
        property_label="Single crystal orientation - Measuring point // Einkristallorientierung – Messpunkt",
        description="""Single crystal orientation - Measuring point // Einkristallorientierung – Messpunkt""",
        mandatory=True,
        show_in_edit_views=False,
        section="Microstructure",
    )

    creep_test_orientation_determination_accuracy = PropertyTypeAssignment(
        code="CREEP_TEST_ORIENTATION_DETERMINATION_ACCURACY",
        data_type="VARCHAR",
        property_label="Orientation - Determination accuracy // Orientierung – Bestimmungsgenauigkeit",
        description="""Orientation - Determination accuracy // Orientierung – Bestimmungsgenauigkeit""",
        mandatory=False,
        show_in_edit_views=False,
        section="Microstructure",
    )


# Section: Chemical composition
class CreepTestMaterialHistoryAndConditionChemicalCompositionNOMINAL(ObjectType):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.MATERIAL_HISTORY_AND_CONDITION.CHEMICAL_COMPOSITION.NOMINAL",
        description="""Material history and condition / Chemical composition (NOMINAL) // Materialhistorie und Zustand / Chemische Zusammensetzung (NOMINAL)""",
        generated_code_prefix="EXP.MECH.CREEP.MATERIAL.CHEMICAL.NOMINAL",
    )

    creep_test_measured_condition = PropertyTypeAssignment(
        code="CREEP_TEST_MEASURED_CONDITION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_MEASURED_CONDITION",
        property_label="Measured condition // Gemessener Zustand",
        description="""Measured condition // Gemessener Zustand""",
        mandatory=True,
        show_in_edit_views=False,
        section="Chemical composition",
    )

    creep_test_measuring_position = PropertyTypeAssignment(
        code="CREEP_TEST_MEASURING_POSITION",
        data_type="VARCHAR",
        property_label="Measuring position // Messposition",
        description="""Measuring position - Specify position(s) for bulk (middle/top/bottom/surface) and/or microstructure feature (matrix, interdendtitic region, phase,...) // Messposition – Geben Sie Position(en) an, z. B. im Volumen (Mitte/oben/unten/Oberfläche) und/oder bezogen auf das Mikrostrukturmerkmal (Matrix, interdendritischer Bereich, Phase, ...).""",
        mandatory=True,
        show_in_edit_views=False,
        section="Chemical composition",
    )

    creep_test_measurement_method = PropertyTypeAssignment(
        code="CREEP_TEST_MEASUREMENT_METHOD",
        data_type="VARCHAR",
        property_label="Measurement method // Messmethode",
        description="""Measurement method - Provide a description of the used method(s) and details about measurement volume/points // Messmethode – Beschreiben Sie die verwendete(n) Methode(n) und geben Sie Details zu Messvolumen/-punkten an.""",
        mandatory=True,
        show_in_edit_views=False,
        section="Chemical composition",
    )

    creep_test_chemical_composition_nominal = PropertyTypeAssignment(
        code="CHEM_SPECIES_BY_COMP_IN_PCT",
        data_type="VARCHAR",
        property_label="Chemical composition - nominal [wt.-% / at.-%] // Chemische Zusammensetzung – nominal [wt.-% / at.-%]",
        description="""Chemical composition - nominal - Link to file, preferably with machine-readable (meta)data or add the wt.-% value of for each element // Chemische Zusammensetzung – nominal [wt.-% / at.-%] – Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten, oder geben Sie für jedes Element den Gewichts-%-Wert an.""",
        mandatory=True,
        show_in_edit_views=False,
        section="Chemical composition",
    )


class CreepTestMaterialHistoryAndConditionChemicalCompositionMEASURED(ObjectType):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.MATERIAL_HISTORY_AND_CONDITION.CHEMICAL_COMPOSITION.MEASURED",
        description="""Material history and condition / Chemical composition (MEASURED) // Materialhistorie und Zustand / Chemische Zusammensetzung (MEASURED)""",
        generated_code_prefix="EXP.MECH.CREEP.MATERIAL.CHEMICAL.MEASURED",
    )

    creep_test_measured_condition = PropertyTypeAssignment(
        code="CREEP_TEST_MEASURED_CONDITION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_MEASURED_CONDITION",
        property_label="Measured condition // Gemessener Zustand",
        description="""Measured condition // Gemessener Zustand""",
        mandatory=True,
        show_in_edit_views=False,
        section="Chemical composition",
    )

    creep_test_measuring_position = PropertyTypeAssignment(
        code="CREEP_TEST_MEASURING_POSITION",
        data_type="VARCHAR",
        property_label="Measuring position // Messposition",
        description="""Measuring position - Specify position(s) for bulk (middle/top/bottom/surface) and/or microstructure feature (matrix, interdendtitic region, phase,...) // Messposition – Geben Sie Position(en) an, z. B. im Volumen (Mitte/oben/unten/Oberfläche) und/oder bezogen auf das Mikrostrukturmerkmal (Matrix, interdendritischer Bereich, Phase, ...).""",
        mandatory=True,
        show_in_edit_views=False,
        section="Chemical composition",
    )

    creep_test_measurement_method = PropertyTypeAssignment(
        code="CREEP_TEST_MEASUREMENT_METHOD",
        data_type="VARCHAR",
        property_label="Measurement method // Messmethode",
        description="""Measurement method - Provide a description of the used method(s) and details about measurement volume/points // Messmethode – Beschreiben Sie die verwendete(n) Methode(n) und geben Sie Details zu Messvolumen/-punkten an.""",
        mandatory=True,
        show_in_edit_views=False,
        section="Chemical composition",
    )

    creep_test_chemical_composition_measured = PropertyTypeAssignment(
        code="CHEM_SPECIES_BY_COMP_IN_PCT",
        data_type="VARCHAR",
        property_label="Chemical composition - measured [wt.-% / at.-%] // Chemische Zusammensetzung – gemessen [wt.-% / at.-%]",
        description="""Chemical composition - measured - Include precision, if available. Link to file, preferably with machine-readable (meta)data or add the wt.-% value of for each element // Chemische Zusammensetzung – gemessen [wt.-% / at.-%] – Geben Sie, falls verfügbar, die Präzision an. Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten, oder geben Sie für jedes Element den Gewichts-%-Wert an.""",
        mandatory=True,
        show_in_edit_views=False,
        section="Chemical composition",
    )


# Section: NDT results
class CreepTestMaterialHistoryAndConditionNDTResults(ObjectType):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.MATERIAL_HISTORY_AND_CONDITION.NDT_RESULTS",
        description="""Material history and condition / NDT Results // Materialhistorie und Zustand / ZfP-Ergebnisse""",
        generated_code_prefix="EXP.MECH.CREEP.MATERIAL.NDT_RESU",
    )

    creep_test_crack_or_defect_inspection_method = PropertyTypeAssignment(
        code="CREEP_TEST_CRACK_OR_DEFECT_INSPECTION_METHOD",
        data_type="VARCHAR",
        property_label="Crack or defect inspection - Method // Riss- oder Defektprüfung – Methode",
        description="""Crack or defect inspection - Method - E.g., Penetrant certification/Radiographic certification/XCT/X-Ray film. Link to file, preferably with machine-readable (meta)data // Riss- oder Defektprüfung – Methode – z. B. Farbeindringprüfung / Röntgenprüfung / XCT / Röntgenfilm. Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=False,
        show_in_edit_views=False,
        section="NDT Results",
    )

    creep_test_crack_or_defect_inspection_result = PropertyTypeAssignment(
        code="CREEP_TEST_CRACK_OR_DEFECT_INSPECTION_RESULT",
        data_type="VARCHAR",
        property_label="Crack or defect inspection - Result // Riss- oder Defektprüfung – Ergebnis",
        description="""Crack or defect inspection - Result // Riss- oder Defektprüfung – Ergebnis""",
        mandatory=False,
        show_in_edit_views=False,
        section="NDT Results",
    )


# Section: Mechanical tests results
class CreepTestMaterialHistoryAndConditionMechanicalTestsResults(ObjectType):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.MATERIAL_HISTORY_AND_CONDITION.MECHANICAL_TESTS_RESULTS",
        description="""Material history and condition / Mechanical tests results // Materialhistorie und Zustand / Ergebnisse mechanischer Prüfungen""",
        generated_code_prefix="EXP.MECH.CREEP.MATERIAL.MECHANIC",
    )

    creep_test_proof_strength_room_temperature = PropertyTypeAssignment(
        code="CREEP_TEST_PROOF_STRENGTH_ROOM_TEMPERATURE",
        data_type="REAL",
        property_label="Proof strength - room temperature [MPa] // Streckgrenze – Raumtemperatur [MPa]",
        description="""Proof strength - room temperature - 0.2 % Proof strength at room temperature // Streckgrenze – Raumtemperatur [MPa] – 0,2-%-Dehngrenze bei Raumtemperatur.""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical tests results",
    )

    creep_test_proof_strength_creep_test_temperature = PropertyTypeAssignment(
        code="CREEP_TEST_PROOF_STRENGTH_CREEP_TEST_TEMPERATURE",
        data_type="REAL",
        property_label="Proof strength - creep test temperature [MPa] // Streckgrenze – Kriechprüftemperatur [MPa]",
        description="""Proof strength - creep test temperature - 0.2 % Proof strength at creep test temperature // Streckgrenze – Kriechprüftemperatur [MPa] – 0,2-%-Dehngrenze bei Kriechprüftemperatur.""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical tests results",
    )

    creep_test_hardness = PropertyTypeAssignment(
        code="CREEP_TEST_HARDNESS",
        data_type="VARCHAR",
        property_label="Hardness // Härte",
        description="""Hardness // Härte""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical tests results",
    )


# --------------------------------
# Section: Metadata - Test piece
# --------------------------------


class CreepTestTestPiece(ObjectType):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.TEST_PIECE",
        description="""Test piece // Probekörper""",
        generated_code_prefix="EXP.MECH.CREEP.TEST_PIE",
    )

    creep_test_test_piece_id = PropertyTypeAssignment(
        code="CREEP_TEST.TEST_PIECE_ID",
        data_type="VARCHAR",
        property_label="Test piece ID // Probekörper-ID",
        description="""Test piece ID // Probekörper-ID""",
        mandatory=False,
        show_in_edit_views=False,
        section="Test piece",
    )

    creep_test_workshop_order_id = PropertyTypeAssignment(
        code="$ORDER.ADDITIONAL_INFORMATION",
        data_type="VARCHAR",
        property_label="Workshop order ID // Werkstattauftrag-ID",
        description="""Workshop order ID // Werkstattauftrag-ID""",
        mandatory=False,
        show_in_edit_views=False,
        section="Test piece",
    )

    creep_test_test_piece_history = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_PIECE_HISTORY",
        data_type="VARCHAR",
        property_label="Test piece history // Probekörperhistorie",
        description="""Test piece history - Link to file, preferably with machine-readable (meta)data. The file(s) can include, e.g., data or documentation from previous experiments. // Probekörperhistorie – Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten. Die Datei(en) können z. B. Daten oder Dokumentationen aus früheren Experimenten enthalten.""",
        mandatory=False,
        show_in_edit_views=False,
        section="Test piece",
    )

    creep_test_test_piece_type_i = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_PIECE_TYPE_I",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_TEST_PIECE_TYPE_I",
        property_label="Test piece type I // Probekörpertyp I",
        description="""Test piece type I // Probekörpertyp I""",
        mandatory=True,
        show_in_edit_views=False,
        section="Test piece",
    )

    creep_test_test_piece_type_ii = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_PIECE_TYPE_II",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_TEST_PIECE_TYPE_II",
        property_label="Test piece type II // Probekörpertyp II",
        description="""Test piece type II // Probekörpertyp II""",
        mandatory=True,
        show_in_edit_views=False,
        section="Test piece",
    )

    creep_test_test_piece_type_iii = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_PIECE_TYPE_III",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_TEST_PIECE_TYPE_III",
        property_label="Test piece type III // Probekörpertyp III",
        description="""Test piece type III // Probekörpertyp III""",
        mandatory=True,
        show_in_edit_views=False,
        section="Test piece",
    )

    creep_test_test_piece_technical_drawing = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_PIECE_TECHNICAL_DRAWING",
        data_type="VARCHAR",
        property_label="Test piece technical drawing // Technische Zeichnung des Probekörpers",
        description="""Test piece technical drawing - Link to file, preferably with machine-readable (meta)data // Technische Zeichnung des Probekörpers – Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=True,
        show_in_edit_views=False,
        section="Test piece",
    )

    creep_test_test_piece_origin_and_orientation = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_PIECE_ORIGIN_AND_ORIENTATION",
        data_type="VARCHAR",
        property_label="Test piece origin and orientation // Herkunft und Orientierung des Probekörpers",
        description="""Test piece origin and orientation - Describe the exact location / positioning of the test piece within the as-tested material. E.g.: Do rolling direction and the longitudinal axis coincide?. Is the test piece located on top or bottom. Do coordinate systems of as-tested material and test piece coincide?. Add a link to a file, e.g., a technical drawing showing this, preferably with machine-readable (meta)data. // Herkunft und Orientierung des Probekörpers – Beschreiben Sie die genaue Lage/Positionierung des Probekörpers im Material im Prüfzustand. z. B.: Stimmen Walzrichtung und Längsachse überein? Liegt der Probekörper oben oder unten? Stimmen die Koordinatensysteme von Material (Prüfzustand) und Probekörper überein? Fügen Sie nach Möglichkeit einen Dateilink (z. B. technische Zeichnung) mit maschinenlesbaren (Meta-)Daten hinzu.""",
        mandatory=True,
        show_in_edit_views=False,
        section="Test piece",
    )

    creep_test_test_piece_orientation_in_test_machine = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_PIECE_ORIENTATION_IN_TEST_MACHINE",
        data_type="VARCHAR",
        property_label="Test piece orientation in test machine // Orientierung des Probekörpers in der Prüfmaschine",
        description="""Test piece orientation in test machine - Describe the exact orientation of the test piece within the test machine. E.g., is the longitudinal axis of the test piece exactly parallel to the loading axis of the test machine?. Add a link to a file providing evidence, preferably with machine-readable (meta)data. This can be, e.g., a technical drawing. // Orientierung des Probekörpers in der Prüfmaschine – Describe the exact orientation of the test piece within the test machine. E.g., is the longitudinal axis of the test piece exactly parallel to the loading axis of the test machine?. Add a link to a file providing evidence, preferably with machine-readable (meta)data. This can be, e.g., a technical drawing.""",
        mandatory=True,
        show_in_edit_views=False,
        section="Test piece",
    )

    creep_test_additional_information_test_piece = PropertyTypeAssignment(
        code="CREEP_TEST_ADDITIONAL_INFORMATION_TEST_PIECE",
        data_type="VARCHAR",
        property_label="Additional information test piece // Zusätzliche Informationen zum Probekörper",
        description="""Additional information test piece - Add the information or a link to file, preferably with machine-readable (meta)data, e.g., Roughness // Zusätzliche Informationen zum Probekörper – Fügen Sie die Information oder einen Dateilink hinzu, vorzugsweise mit maschinenlesbaren (Meta-)Daten, z. B. Rauheit.""",
        mandatory=False,
        show_in_edit_views=False,
        section="Test piece",
    )


# --------------------------------
# Section: Metadata - Measuring and test equipment
# --------------------------------


# Section: Test machine
class CreepTestMeasuringAndTestEquipmentTestMachine(ObjectType):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.MEASURING_AND_TEST_EQUIPMENT.TEST_MACHINE",
        description="""Measuring and test equipment / Test machine // Mess- und Prüfmittel / Prüfmaschine""",
        generated_code_prefix="EXP.MECH.CREEP.MEASURIN.TEST_MAC",
    )

    # --- Links to test machine sub-systems (OBJECT properties) ---
    link_heating_system = PropertyTypeAssignment(
        code="CREEP_TEST.TEST_MACHINE.LINK.LINK_HEATING_SYSTEM",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.MEASURING_AND_TEST_EQUIPMENT.TEST_MACHINE.HEATING_SYSTEM",
        property_label="Heating system",
        description="""Linked object: Heating system""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked test machine objects",
    )

    link_holder_system = PropertyTypeAssignment(
        code="CREEP_TEST.TEST_MACHINE.LINK.LINK_HOLDER_SYSTEM",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.MEASURING_AND_TEST_EQUIPMENT.TEST_MACHINE.TEST_PIECE_HOLDER_SYSTEM",
        property_label="Test piece holder system",
        description="""Linked object: Test piece holder system""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked test machine objects",
    )

    link_loading_system = PropertyTypeAssignment(
        code="CREEP_TEST.TEST_MACHINE.LINK.LINK_LOADING_SYSTEM",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.MEASURING_AND_TEST_EQUIPMENT.TEST_MACHINE.LOADING_SYSTEM",
        property_label="Loading system",
        description="""Linked object: Loading system""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked test machine objects",
    )

    link_data_acquisition = PropertyTypeAssignment(
        code="CREEP_TEST.TEST_MACHINE.LINK.LINK_DATA_ACQUISITION",
        data_type="OBJECT",
        object_code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.MEASURING_AND_TEST_EQUIPMENT.TEST_MACHINE.DATA_ACQUISITION",
        property_label="Data acquisition",
        description="""Linked object: Data acquisition""",
        mandatory=False,
        show_in_edit_views=False,
        section="Linked test machine objects",
    )

    creep_test_test_machine_id = PropertyTypeAssignment(
        code="CREEP_TEST.TEST_MACHINE_ID",
        data_type="VARCHAR",
        property_label="Test machine ID // Prüfmaschinen-ID",
        description="""Test machine ID // Prüfmaschinen-ID""",
        mandatory=False,
        show_in_edit_views=False,
        section="Test machine",
    )

    creep_test_test_machine_type = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_MACHINE_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_MACHINE_TYPE",
        property_label="Test machine type // Prüfmaschinentyp",
        description="""Test machine type // Prüfmaschinentyp""",
        mandatory=False,
        show_in_edit_views=False,
        section="Test machine",
    )

    creep_test_minimum_applicable_force = PropertyTypeAssignment(
        code="CREEP_TEST_MINIMUM_APPLICABLE_FORCE",
        data_type="REAL",
        property_label="Minimum applicable force [kN] // Minimale anwendbare Kraft [kN]",
        description="""Minimum applicable force // Minimale anwendbare Kraft [kN]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Test machine",
    )

    creep_test_maximum_applicable_force = PropertyTypeAssignment(
        code="MAX_STATIC_FORCE",
        data_type="REAL",
        property_label="Maximum applicable force [kN] // Maximale anwendbare Kraft [kN]",
        description="""Maximum applicable force // Maximale anwendbare Kraft [kN]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Test machine",
    )

    creep_test_test_frame_and_specimen_alignment = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_FRAME_AND_SPECIMEN_ALIGNMENT",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_TEST_FRAME_AND_SPECIMEN_ALIGNMENT",
        property_label="Test frame and specimen alignment // Ausrichtung von Testrahmen und Probekörper",
        description="""Test frame and specimen alignment - Verification of Test Frame and Specimen Alignment according to ASTM E1012? // Ausrichtung von Testrahmen und Probekörper – Überprüfung der Ausrichtung von Testrahmen und Probekörper gemäß ASTM E1012?""",
        mandatory=True,
        show_in_edit_views=False,
        section="Test machine",
    )

    creep_test_test_frame_and_specimen_alignment_description = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_FRAME_AND_SPECIMEN_ALIGNMENT_DESCRIPTION",
        data_type="VARCHAR",
        property_label="Test frame and specimen alignment - description // Ausrichtung von Testrahmen und Probekörper – Beschreibung",
        description="""Test frame and specimen alignment - description - Please provide a description on the procedure followed for the Verification of Test Frame and Specimen Alignment if different from ASTM E1012 // Ausrichtung von Testrahmen und Probekörper – Beschreibung – Bitte beschreiben Sie das Verfahren zur Überprüfung der Ausrichtung von Testrahmen und Probekörper, falls es von ASTM E1012 abweicht.""",
        mandatory=True,
        show_in_edit_views=False,
        section="Test machine",
    )

    creep_test_calibration_class = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_CLASS",
        data_type="VARCHAR",
        property_label="Calibration class // Kalibrierklasse",
        description="""Calibration class - Calibration class of test frame and specimen alignment, e.g., 5 / 5 starting from 3 kN (according to ASTM E1012) // Kalibrierklasse – Kalibrierklasse der Ausrichtung von Testrahmen und Probekörper, z. B. 5/5 ab 3 kN (gemäß ASTM E1012).""",
        mandatory=True,
        show_in_edit_views=False,
        section="Test machine",
    )


class CreepTestMeasuringAndTestEquipmentTestMachineHeatingSystem(ObjectType):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.MEASURING_AND_TEST_EQUIPMENT.TEST_MACHINE.HEATING_SYSTEM",
        description="""Measuring and test equipment / Test machine / Heating system // Mess- und Prüfmittel / Prüfmaschine / Heizsystem""",
        generated_code_prefix="EXP.MECH.CREEP.MEASURIN.TEST_MAC.HEATING_",
    )

    creep_test_furnace_type = PropertyTypeAssignment(
        code="CREEP_TEST_FURNACE_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_FURNACE_TYPE",
        property_label="Furnace type // Ofentyp",
        description="""Furnace type // Ofentyp""",
        mandatory=True,
        show_in_edit_views=False,
        section="Heating system",
    )


class CreepTestMeasuringAndTestEquipmentTestMachineTestPieceHolderSystem(ObjectType):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.MEASURING_AND_TEST_EQUIPMENT.TEST_MACHINE.TEST_PIECE_HOLDER_SYSTEM",
        description="""Measuring and test equipment / Test machine / Test piece holder system // Mess- und Prüfmittel / Prüfmaschine / Probenhaltersystem""",
        generated_code_prefix="EXP.MECH.CREEP.MEASURIN.TEST_MAC.TEST_PIE",
    )

    creep_test_fixing_technique = PropertyTypeAssignment(
        code="CREEP_TEST_FIXING_TECHNIQUE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_FIXING_TECHNIQUE",
        property_label="Fixing technique // Befestigungstechnik",
        description="""Fixing technique // Befestigungstechnik""",
        mandatory=True,
        show_in_edit_views=False,
        section="Test piece holder system",
    )


class CreepTestMeasuringAndTestEquipmentTestMachineLoadingSystem(ObjectType):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.MEASURING_AND_TEST_EQUIPMENT.TEST_MACHINE.LOADING_SYSTEM",
        description="""Measuring and test equipment / Test machine / Loading system // Mess- und Prüfmittel / Prüfmaschine / Belastungssystem""",
        generated_code_prefix="EXP.MECH.CREEP.MEASURIN.TEST_MAC.LOADING_",
    )

    creep_test_verification_of_loading_system = PropertyTypeAssignment(
        code="CREEP_TEST_VERIFICATION_OF_LOADING_SYSTEM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_VERIFICATION_OF_LOADING_SYSTEM",
        property_label="Verification of loading system // Überprüfung des Belastungssystems",
        description="""Verification of loading system - Was the loading system calibrated/verified? // Überprüfung des Belastungssystems – Wurde das Belastungssystem kalibriert/überprüft?""",
        mandatory=True,
        show_in_edit_views=False,
        section="Loading system",
    )

    creep_test_calibration_certificate = PropertyTypeAssignment(
        code="CALIBRATION_CERTIFICATE_NUMBER",
        data_type="VARCHAR",
        property_label="Calibration certificate // Kalibrierzertifikat",
        description="""Calibration certificate - Link to file, preferably with machine-readable (meta)data. Please specify which device/feature/part of the test machine was calibrated. // Kalibrierzertifikat – Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten. Bitte geben Sie an, welches Gerät/Feature/welcher Teil der Prüfmaschine kalibriert wurde.""",
        mandatory=False,
        show_in_edit_views=False,
        section="Loading system",
    )

    creep_test_calibration_date = PropertyTypeAssignment(
        code="CALIBRATION_DATE",
        data_type="DATE",
        property_label="Calibration date // Kalibrierdatum",
        description="""Calibration date // Kalibrierdatum""",
        mandatory=True,
        show_in_edit_views=False,
        section="Loading system",
    )

    creep_test_calibration_validity_time_period = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_VALIDITY_TIME_PERIOD",
        data_type="VARCHAR",
        property_label="Calibration validity time period // Gültigkeitszeitraum der Kalibrierung",
        description="""Calibration validity time period // Gültigkeitszeitraum der Kalibrierung""",
        mandatory=True,
        show_in_edit_views=False,
        section="Loading system",
    )

    creep_test_calibration_standard = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_STANDARD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_LOAD_SYSTEM_CALIBRATION_STANDARD",
        property_label="Calibration standard // Kalibrierstandard",
        description="""Calibration standard // Kalibrierstandard""",
        mandatory=True,
        show_in_edit_views=False,
        section="Loading system",
    )

    creep_test_calibration_class = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_CLASS",
        data_type="REAL",
        property_label="Calibration class // Kalibrierklasse",
        description="""Calibration class // Kalibrierklasse""",
        mandatory=True,
        show_in_edit_views=False,
        section="Loading system",
    )

    creep_test_calibration_range = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_RANGE",
        data_type="VARCHAR",
        property_label="Calibration range [kN] // Kalibrierbereich [kN]",
        description="""Calibration range // Kalibrierbereich [kN]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Loading system",
    )

    creep_test_use_of_calibrated_weights = PropertyTypeAssignment(
        code="CREEP_TEST_USE_OF_CALIBRATED_WEIGHTS",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_USE_OF_CALIBRATED_WEIGHTS",
        property_label="Use of calibrated weights // Verwendung kalibrierter Gewichte",
        description="""Use of calibrated weights - Were calibrated weights used to apply the test force? // Verwendung kalibrierter Gewichte – Wurden kalibrierte Gewichte verwendet, um die Prüfkraft aufzubringen?""",
        mandatory=True,
        show_in_edit_views=False,
        section="Loading system",
    )

    creep_test_description_of_the_loading_system = PropertyTypeAssignment(
        code="CREEP_TEST_DESCRIPTION_OF_THE_LOADING_SYSTEM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_DESCRIPTION_OF_THE_LOADING_SYSTEM",
        property_label="Description of the loading system // Beschreibung des Belastungssystems",
        description="""Description of the loading system - Please describe the loading system and related verification in the case that calibrated weights were not used. // Beschreibung des Belastungssystems – Bitte beschreiben Sie das Belastungssystem und die zugehörige Überprüfung für den Fall, dass keine kalibrierten Gewichte verwendet wurden.""",
        mandatory=True,
        show_in_edit_views=False,
        section="Loading system",
    )


class CreepTestMeasuringAndTestEquipmentTestMachineDataAcquisition(ObjectType):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.MEASURING_AND_TEST_EQUIPMENT.TEST_MACHINE.DATA_ACQUISITION",
        description="""Measuring and test equipment / Test machine / Data acquisition // Mess- und Prüfmittel / Prüfmaschine / Datenerfassung""",
        generated_code_prefix="EXP.MECH.CREEP.MEASURIN.TEST_MAC.DATA_ACQ",
    )

    creep_test_data_acquisition_unit_model_information = PropertyTypeAssignment(
        code="CREEP_TEST_DATA_ACQUISITION_UNIT_MODEL_INFORMATION",
        data_type="VARCHAR",
        property_label="Data acquisition unit - Model information // Datenerfassungseinheit – Modellinformationen",
        description="""Data acquisition unit - Model information // Datenerfassungseinheit – Modellinformationen""",
        mandatory=False,
        show_in_edit_views=False,
        section="Data acquisition",
    )

    creep_test_data_acquisition_unit_id = PropertyTypeAssignment(
        code="CREEP_TEST_DATA_ACQUISITION_UNIT_ID",
        data_type="VARCHAR",
        property_label="Data acquisition unit - ID // Datenerfassungseinheit – ID",
        description="""Data acquisition unit - ID // Datenerfassungseinheit – ID""",
        mandatory=False,
        show_in_edit_views=False,
        section="Data acquisition",
    )

    creep_test_data_acquisition_software_and_version = PropertyTypeAssignment(
        code="CREEP_TEST_DATA_ACQUISITION_SOFTWARE_AND_VERSION",
        data_type="VARCHAR",
        property_label="Data acquisition software and version // Datenerfassungssoftware und Version",
        description="""Data acquisition software and version // Datenerfassungssoftware und Version""",
        mandatory=True,
        show_in_edit_views=False,
        section="Data acquisition",
    )

    creep_test_data_acquisition_description = PropertyTypeAssignment(
        code="CREEP_TEST_DATA_ACQUISITION_DESCRIPTION",
        data_type="VARCHAR",
        property_label="Data acquisition - description // Datenerfassung – Beschreibung",
        description="""Data acquisition - description // Datenerfassung – Beschreibung""",
        mandatory=True,
        show_in_edit_views=False,
        section="Data acquisition",
    )

    creep_test_data_acquisition_time_check = PropertyTypeAssignment(
        code="CREEP_TEST_DATA_ACQUISITION_TIME_CHECK",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_DATA_ACQUISITION_TIME_CHECK",
        property_label="Data acquisition time check // Zeitprüfung der Datenerfassung",
        description="""Data acquisition time check - Was the time checked during data acquisition? // Zeitprüfung der Datenerfassung – Wurde die Zeit während der Datenerfassung überprüft?""",
        mandatory=False,
        show_in_edit_views=False,
        section="Data acquisition",
    )


# Section: Load-measuring system
class CreepTestMeasuringAndTestEquipmentLoadMeasuringSystemLoadSensor(ObjectType):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.MEASURING_AND_TEST_EQUIPMENT.LOAD_MEASURING_SYSTEM.LOAD_SENSOR",
        description="""Measuring and test equipment / Load-measuring system / Load sensor // Mess- und Prüfmittel / Kraftmesssystem / Kraftsensor""",
        generated_code_prefix="EXP.MECH.CREEP.MEASURIN.LOAD_MEA.LOAD_SEN",
    )

    creep_test_load_sensor_during_loading = PropertyTypeAssignment(
        code="CREEP_TEST_LOAD_SENSOR_DURING_LOADING",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_LOAD_SENSOR_DURING_LOADING",
        property_label="Load sensor during loading // Kraftsensor während der Belastung",
        description="""Load sensor during loading - Was a load sensor used during loading? // Kraftsensor während der Belastung – Wurde während des Lastaufbringens ein Kraftsensor verwendet?""",
        mandatory=True,
        show_in_edit_views=False,
        section="Load sensor",
    )

    creep_test_load_sensor_calibration = PropertyTypeAssignment(
        code="CREEP_TEST_LOAD_SENSOR_CALIBRATION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_LOAD_SENSOR_CALIBRATION",
        property_label="Load sensor calibration // Kalibrierung des Kraftsensors",
        description="""Load sensor calibration - Was the load sensor calibrated? // Kalibrierung des Kraftsensors – War der Kraftsensor kalibriert?""",
        mandatory=True,
        show_in_edit_views=False,
        section="Load sensor",
    )

    creep_test_calibration_certificate = PropertyTypeAssignment(
        code="CALIBRATION_CERTIFICATE_NUMBER",
        data_type="VARCHAR",
        property_label="Calibration certificate // Kalibrierzertifikat",
        description="""Calibration certificate - Link to file, preferably with machine-readable (meta)data. // Kalibrierzertifikat – Link to file, preferably with machine-readable (meta)data.""",
        mandatory=False,
        show_in_edit_views=False,
        section="Load sensor",
    )

    creep_test_calibration_date = PropertyTypeAssignment(
        code="CALIBRATION_DATE",
        data_type="DATE",
        property_label="Calibration date // Kalibrierdatum",
        description="""Calibration date // Kalibrierdatum""",
        mandatory=True,
        show_in_edit_views=False,
        section="Load sensor",
    )

    creep_test_calibration_validity_time_period = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_VALIDITY_TIME_PERIOD",
        data_type="VARCHAR",
        property_label="Calibration validity time period // Gültigkeitszeitraum der Kalibrierung",
        description="""Calibration validity time period // Gültigkeitszeitraum der Kalibrierung""",
        mandatory=True,
        show_in_edit_views=False,
        section="Load sensor",
    )

    creep_test_calibration_standard = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_STANDARD",
        data_type="VARCHAR",
        property_label="Calibration standard // Kalibrierstandard",
        description="""Calibration standard // Kalibrierstandard""",
        mandatory=True,
        show_in_edit_views=False,
        section="Load sensor",
    )

    creep_test_calibration_class = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_CLASS",
        data_type="REAL",
        property_label="Calibration class // Kalibrierklasse",
        description="""Calibration class // Kalibrierklasse""",
        mandatory=True,
        show_in_edit_views=False,
        section="Load sensor",
    )

    creep_test_calibration_range = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_RANGE",
        data_type="VARCHAR",
        property_label="Calibration Range [kN] // Kalibrierbereich [kN]",
        description="""Calibration Range // Kalibrierbereich [kN]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Load sensor",
    )


class CreepTestMeasuringAndTestEquipmentLoadMeasuringSystemDataAcquisition(ObjectType):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.MEASURING_AND_TEST_EQUIPMENT.LOAD_MEASURING_SYSTEM.DATA_ACQUISITION",
        description="""Measuring and test equipment / Load-measuring system / Data acquisition // Mess- und Prüfmittel / Kraftmesssystem / Datenerfassung""",
        generated_code_prefix="EXP.MECH.CREEP.MEASURIN.LOAD_MEA.DATA_ACQ",
    )

    creep_test_force_recording = PropertyTypeAssignment(
        code="CREEP_TEST_FORCE_RECORDING",
        data_type="VARCHAR",
        property_label="Force recording // Kraftaufzeichnung",
        description="""Force recording - Was the force recorded continuously or periodically (e.g. during loading)? // Kraftaufzeichnung – Wurde die Kraft kontinuierlich oder periodisch aufgezeichnet (z. B. während des Lastaufbringens)?""",
        mandatory=True,
        show_in_edit_views=False,
        section="Data acquisition",
    )


# Section: Laboratory conditions
class CreepTestMetadataMeasuringAndTestEquipmentLaboratoryConditions(ObjectType):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.METADATA.MEASURING_AND_TEST_EQUIPMENT.LABORATORY_CONDITIONS",
        description="""Metadata / Measuring and test equipment / Laboratory conditions // Metadaten / Mess- und Prüfmittel / Laborbedingungen""",
        generated_code_prefix="EXP.MECH.CREEP.METADATA.MEASURIN.LABORATO",
    )

    creep_test_room_temperature = PropertyTypeAssignment(
        code="CREEP_TEST_ROOM_TEMPERATURE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_ROOM_TEMPERATURE",
        property_label="Room temperature // Raumtemperatur",
        description="""Room temperature - Was the room temperature recorded and checked? // Raumtemperatur – Wurde die Raumtemperatur aufgezeichnet und überprüft?""",
        mandatory=True,
        show_in_edit_views=False,
        section="Laboratory conditions",
    )

    creep_test_room_humidity = PropertyTypeAssignment(
        code="CREEP_TEST_ROOM_HUMIDITY",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_ROOM_HUMIDITY",
        property_label="Room humidity // Raumluftfeuchte",
        description="""Room humidity - Was the room humidity recorded and checked? // Raumluftfeuchte – Wurde die Raumluftfeuchte aufgezeichnet und überprüft?""",
        mandatory=False,
        show_in_edit_views=False,
        section="Laboratory conditions",
    )


# Section: Temperature-measuring system
class CreepTestMetadataMeasuringAndTestEquipmentTemperatureMeasuringSystem(ObjectType):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.METADATA.MEASURING_AND_TEST_EQUIPMENT.TEMPERATURE_MEASURING_SYSTEM",
        description="""Metadata / Measuring and test equipment / Temperature-measuring system // Metadaten / Mess- und Prüfmittel / Temperaturmesssystem""",
        generated_code_prefix="EXP.MECH.CREEP.METADATA.MEASURIN.TEMPERAT",
    )

    creep_test_temperature_signal = PropertyTypeAssignment(
        code="CREEP_TEST_TEMPERATURE_SIGNAL",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_TEMPERATURE_SIGNAL",
        property_label="Temperature signal // Temperatursignal",
        description="""Temperature signal - Which temperature signal was used for temperature control? // Temperatursignal – Welches Temperatursignal wurde für die Temperaturregelung verwendet?""",
        mandatory=True,
        show_in_edit_views=False,
        section="Temperature-measuring system",
    )

    creep_test_metrological_traceability = PropertyTypeAssignment(
        code="CREEP_TEST_METROLOGICAL_TRACEABILITY",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_METROLOGICAL_TRACEABILITY",
        property_label="Metrological traceability // Metrologische Rückführbarkeit",
        description="""Metrological traceability - Yes, if temperature sensor and data acquisition are calibrated. // Metrologische Rückführbarkeit – Ja, wenn Temperatursensor und Datenerfassung kalibriert sind.""",
        mandatory=True,
        show_in_edit_views=False,
        section="Temperature-measuring system",
    )


class CreepTestMetadataMeasuringAndTestEquipmentTemperatureMeasuringSystemTemperatureSensor(
    ObjectType
):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.METADATA.MEASURING_AND_TEST_EQUIPMENT.TEMPERATURE_MEASURING_SYSTEM.TEMPERATURE_SENSOR",
        description="""Metadata / Measuring and test equipment / Temperature-measuring system / Temperature sensor // Metadaten / Mess- und Prüfmittel / Temperaturmesssystem / Temperatursensor""",
        generated_code_prefix="EXP.MECH.CREEP.METADATA.MEASURIN.TEMPERAT.TEMPERAT",
    )

    creep_test_sensor_type = PropertyTypeAssignment(
        code="CREEP_TEST_SENSOR_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_SENSOR_TYPE",
        property_label="Sensor type // Sensortyp",
        description="""Sensor type // Sensortyp""",
        mandatory=True,
        show_in_edit_views=False,
        section="Temperature sensor",
    )

    creep_test_sensor_id = PropertyTypeAssignment(
        code="CREEP_TEST.SENSOR_ID",
        data_type="VARCHAR",
        property_label="Sensor ID // Sensor-ID",
        description="""Sensor ID // Sensor-ID""",
        mandatory=False,
        show_in_edit_views=False,
        section="Temperature sensor",
    )

    creep_test_thermocouple_type = PropertyTypeAssignment(
        code="CREEP_TEST_THERMOCOUPLE_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        # Vocabulary type taken from existing vocabulary
        vocabulary_code="THERMOCOUPLE_TYPE",
        property_label="Thermocouple type // Thermoelementtyp",
        description="""Thermocouple type // Thermoelementtyp""",
        mandatory=True,
        show_in_edit_views=False,
        section="Temperature sensor",
    )

    creep_test_wire_gauge = PropertyTypeAssignment(
        code="CREEP_TEST_WIRE_GAUGE",
        data_type="REAL",
        property_label="Wire gauge [mm] // Drahtdurchmesser [mm]",
        description="""Wire gauge // Drahtdurchmesser [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Temperature sensor",
    )

    creep_test_layout = PropertyTypeAssignment(
        code="CREEP_TEST_LAYOUT",
        data_type="VARCHAR",
        property_label="Layout // Aufbau",
        description="""Layout - E.g., wire with 2-hole ceramic beads // Aufbau – E.g., wire with 2-hole ceramic beads""",
        mandatory=False,
        show_in_edit_views=False,
        section="Temperature sensor",
    )

    creep_test_calibration_status = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_STATUS",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_THERMOCOUPLE_CALIBRATION_STATUS",
        property_label="Calibration status // Kalibrierstatus",
        description="""Calibration status - Is/are the thermocouples calibrated? // Kalibrierstatus – Ist/sind das/die Thermoelement(e) kalibriert?""",
        mandatory=True,
        show_in_edit_views=False,
        section="Temperature sensor",
    )

    creep_test_calibration_method = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_METHOD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_THERMOCOUPLE_CALIBRATION_METHOD",
        property_label="Calibration method // Kalibriermethode",
        description="""Calibration method // Kalibriermethode""",
        mandatory=True,
        show_in_edit_views=False,
        section="Temperature sensor",
    )

    creep_test_calibration_standard = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_STANDARD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_THERMOCOUPLE_CALIBRATION_STANDARD",
        property_label="Calibration standard // Kalibrierstandard",
        description="""Calibration standard // Kalibrierstandard""",
        mandatory=True,
        show_in_edit_views=False,
        section="Temperature sensor",
    )

    creep_test_calibration_certificate = PropertyTypeAssignment(
        code="CALIBRATION_CERTIFICATE_NUMBER",
        data_type="VARCHAR",
        property_label="Calibration certificate // Kalibrierzertifikat",
        description="""Calibration certificate - Link to file, preferably with machine-readable (meta)data. // Kalibrierzertifikat – Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=False,
        show_in_edit_views=False,
        section="Temperature sensor",
    )

    creep_test_calibration_date = PropertyTypeAssignment(
        code="CALIBRATION_DATE",
        data_type="DATE",
        property_label="Calibration date // Kalibrierdatum",
        description="""Calibration date // Kalibrierdatum""",
        mandatory=True,
        show_in_edit_views=False,
        section="Temperature sensor",
    )

    creep_test_calibration_validity_time_period = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_VALIDITY_TIME_PERIOD",
        data_type="VARCHAR",
        property_label="Calibration validity time period // Gültigkeitszeitraum der Kalibrierung",
        description="""Calibration validity time period // Gültigkeitszeitraum der Kalibrierung""",
        mandatory=True,
        show_in_edit_views=False,
        section="Temperature sensor",
    )

    creep_test_temperature_deviation = PropertyTypeAssignment(
        code="CREEP_TEST_TEMPERATURE_DEVIATION",
        data_type="VARCHAR",
        property_label="Temperature deviation [°C] // Temperaturabweichung [°C]",
        description="""Temperature deviation - Measurement deviation detected during calibration // Temperaturabweichung [°C] – Bei der Kalibrierung festgestellte Messabweichung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Temperature sensor",
    )

    creep_test_calibration_range = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_RANGE",
        data_type="VARCHAR",
        property_label="Calibration Range [°C] // Kalibrierbereich [°C]",
        description="""Calibration Range // Kalibrierbereich [°C]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Temperature sensor",
    )

    creep_test_contact_method = PropertyTypeAssignment(
        code="CREEP_TEST_CONTACT_METHOD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_THERMOCOUPLE_CONTACT_METHOD",
        property_label="Contact method // Kontaktmethode",
        description="""Contact method // Kontaktmethode""",
        mandatory=True,
        show_in_edit_views=False,
        section="Temperature sensor",
    )

    creep_test_number_of_thermocouples = PropertyTypeAssignment(
        code="CREEP_TEST_NUMBER_OF_THERMOCOUPLES",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_NUMBER_OF_THERMOCOUPLES",
        property_label="Number of thermocouples // Anzahl der Thermoelemente",
        description="""Number of thermocouples // Anzahl der Thermoelemente""",
        mandatory=True,
        show_in_edit_views=False,
        section="Temperature sensor",
    )

    creep_test_thermocouple_location = PropertyTypeAssignment(
        code="CREEP_TEST_THERMOCOUPLE_LOCATION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_THERMOCOUPLE_LOCATION",
        property_label="Thermocouple location // Position des Thermoelements",
        description="""Thermocouple location - Location with respect to gauge section // Position des Thermoelements – Position in Bezug auf den Messbereich""",
        mandatory=True,
        show_in_edit_views=False,
        section="Temperature sensor",
    )


class CreepTestMetadataMeasuringAndTestEquipmentTemperatureMeasuringSystemDataAcquisition(
    ObjectType
):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.METADATA.MEASURING_AND_TEST_EQUIPMENT.TEMPERATURE_MEASURING_SYSTEM.DATA_ACQUISITION",
        description="""Metadata / Measuring and test equipment / Temperature-measuring system / Data acquisition // Metadaten / Mess- und Prüfmittel / Temperaturmesssystem / Datenerfassung""",
        generated_code_prefix="EXP.MECH.CREEP.METADATA.MEASURIN.TEMPERAT.DATA_ACQ",
    )

    creep_test_calibration_status = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_STATUS",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_DATA_AQUISITION_CALIBRATION_STATUS",
        property_label="Calibration status // Kalibrierstatus",
        description="""Calibration status - Is/are the data acquisition unit calibrated? // Kalibrierstatus – Ist/sind die Datenerfassungseinheit(en) kalibriert?""",
        mandatory=True,
        show_in_edit_views=False,
        section="Data acquisition",
    )

    creep_test_reference_junction = PropertyTypeAssignment(
        code="CREEP_TEST_REFERENCE_JUNCTION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_REFERENCE_JUNCTION",
        property_label="Reference junction // Referenzstelle",
        description="""Reference junction // Referenzstelle""",
        mandatory=False,
        show_in_edit_views=False,
        section="Data acquisition",
    )

    creep_test_calibration_certificate = PropertyTypeAssignment(
        code="CALIBRATION_CERTIFICATE_NUMBER",
        data_type="VARCHAR",
        property_label="Calibration certificate // Kalibrierzertifikat",
        description="""Calibration certificate - Link to file, preferably with machine-readable (meta)data. // Kalibrierzertifikat – Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=False,
        show_in_edit_views=False,
        section="Data acquisition",
    )

    creep_test_calibration_date = PropertyTypeAssignment(
        code="CALIBRATION_DATE",
        data_type="DATE",
        property_label="Calibration date // Kalibrierdatum",
        description="""Calibration date // Kalibrierdatum""",
        mandatory=True,
        show_in_edit_views=False,
        section="Data acquisition",
    )

    creep_test_calibration_validity_time_period = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_VALIDITY_TIME_PERIOD",
        data_type="VARCHAR",
        property_label="Calibration validity time period // Gültigkeitszeitraum der Kalibrierung",
        description="""Calibration validity time period // Gültigkeitszeitraum der Kalibrierung""",
        mandatory=True,
        show_in_edit_views=False,
        section="Data acquisition",
    )

    creep_test_calibration_method = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_METHOD",
        data_type="VARCHAR",
        property_label="Calibration method // Kalibriermethode",
        description="""Calibration method // Kalibriermethode""",
        mandatory=True,
        show_in_edit_views=False,
        section="Data acquisition",
    )

    creep_test_calibration_standard = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_STANDARD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_DATA_ACQUISITION_CALIBRATION_STANDARD",
        property_label="Calibration standard // Kalibrierstandard",
        description="""Calibration standard // Kalibrierstandard""",
        mandatory=True,
        show_in_edit_views=False,
        section="Data acquisition",
    )

    creep_test_temperature_deviation = PropertyTypeAssignment(
        code="CREEP_TEST_TEMPERATURE_DEVIATION",
        data_type="VARCHAR",
        property_label="Temperature deviation [°C] // Temperaturabweichung [°C]",
        description="""Temperature deviation - Measurement deviation detected during calibration // Temperaturabweichung [°C] – Bei der Kalibrierung festgestellte Messabweichung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Data acquisition",
    )

    creep_test_calibration_range = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_RANGE",
        data_type="VARCHAR",
        property_label="Calibration Range [°C] // Kalibrierbereich [°C]",
        description="""Calibration Range // Kalibrierbereich [°C]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Data acquisition",
    )


# Section: Extensometer system
class CreepTestMetadataMeasuringAndTestEquipmentExtensometerSystem(ObjectType):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.METADATA.MEASURING_AND_TEST_EQUIPMENT.EXTENSOMETER_SYSTEM",
        description="""Metadata / Measuring and test equipment / Extensometer system // Metadaten / Mess- und Prüfmittel / Extensometersystem""",
        generated_code_prefix="EXP.MECH.CREEP.METADATA.MEASURIN.EXTENSOM",
    )

    creep_test_displacement_measuring_method = PropertyTypeAssignment(
        code="CREEP_TEST_DISPLACEMENT_MEASURING_METHOD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_DISPLACEMENT_MEASURING_METHOD",
        property_label="Displacement measuring method // Wegmessverfahren",
        description="""Displacement measuring method - Type of strain measuring device // Wegmessverfahren – Art des Dehnungsmessgeräts""",
        mandatory=True,
        show_in_edit_views=False,
        section="Extensometer system",
    )

    creep_test_sensor_type_contacting_method = PropertyTypeAssignment(
        code="CREEP_TEST_SENSOR_TYPE_CONTACTING_METHOD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_SENSOR_TYPE_CONTACTING_METHOD",
        property_label="Sensor type - Contacting method // Sensortyp – Kontaktmethode",
        description="""Sensor type - Contacting method // Sensortyp – Kontaktmethode""",
        mandatory=True,
        show_in_edit_views=False,
        section="Extensometer system",
    )

    creep_test_sensor_type_non_contacting_method = PropertyTypeAssignment(
        code="CREEP_TEST_SENSOR_TYPE_NON_CONTACTING_METHOD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_SENSOR_TYPE_NON_CONTACTING_METHOD",
        property_label="Sensor type - Non-contacting method // Sensortyp – berührungslose Methode",
        description="""Sensor type - Non-contacting method // Sensortyp – berührungslose Methode""",
        mandatory=True,
        show_in_edit_views=False,
        section="Extensometer system",
    )


# Section: Extension values
class CreepTestMetadataMeasuringAndTestEquipmentExtensionValuesContactingExtensometer(
    ObjectType
):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.METADATA.MEASURING_AND_TEST_EQUIPMENT.EXTENSION_VALUES.CONTACTING_EXTENSOMETER",
        description="""Metadata / Measuring and test equipment / Extension values / Contacting extensometer // Metadaten / Mess- und Prüfmittel / Dehnungswerte / kontaktierendes Extensometer""",
        generated_code_prefix="EXP.MECH.CREEP.METADATA.MEASURIN.EXTENSIO.CONTACTI",
    )

    creep_test_measurement_set_up = PropertyTypeAssignment(
        code="CREEP_TEST_MEASUREMENT_SET_UP",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_MEASUREMENT_SET_UP",
        property_label="Measurement set-up // Messaufbau",
        description="""Measurement set-up - Measurement one-sided or two-sided? // Messaufbau – Einseitige oder beidseitige Messung?""",
        mandatory=True,
        show_in_edit_views=False,
        section="Contacting extensometer",
    )

    creep_test_extension_averaging = PropertyTypeAssignment(
        code="CREEP_TEST_EXTENSION_AVERAGING",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_EXTENSION_AVERAGING",
        property_label="Extension averaging // Dehnungsmittelung",
        description="""Extension averaging - Was there an averaging of the extension values? (two-sided extensometer) // Dehnungsmittelung – Wurden die Dehnungswerte gemittelt? (beidseitiger Dehnungsmesser)""",
        mandatory=True,
        show_in_edit_views=False,
        section="Contacting extensometer",
    )

    creep_test_measurement_direction = PropertyTypeAssignment(
        code="CREEP_TEST_MEASUREMENT_DIRECTION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_EXTENSION_MEASUREMENT_DIRECTION",
        property_label="Measurement direction // Messrichtung",
        description="""Measurement direction // Messrichtung""",
        mandatory=True,
        show_in_edit_views=False,
        section="Contacting extensometer",
    )

    creep_test_mounting_type = PropertyTypeAssignment(
        code="CREEP_TEST_MOUNTING_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_EXTENSOMETER_MOUNTING_TYPE",
        property_label="Mounting type // Montageart",
        description="""Mounting type // Montageart""",
        mandatory=True,
        show_in_edit_views=False,
        section="Contacting extensometer",
    )

    creep_test_extensometer_model_information = PropertyTypeAssignment(
        code="CREEP_TEST_EXTENSOMETER_MODEL_INFORMATION",
        data_type="VARCHAR",
        property_label="Extensometer model information // Extensometer-Modellinformationen",
        description="""Extensometer model information // Extensometer-Modellinformationen""",
        mandatory=False,
        show_in_edit_views=False,
        section="Contacting extensometer",
    )

    creep_test_extensometer_id = PropertyTypeAssignment(
        code="CREEP_TEST.EXTENSOMETER_ID",
        data_type="VARCHAR",
        property_label="Extensometer ID // Extensometer-ID",
        description="""Extensometer ID - The ID used for identification in the laboratory // Extensometer-ID – ID zur Identifikation im Labor""",
        mandatory=False,
        show_in_edit_views=False,
        section="Contacting extensometer",
    )

    creep_test_extensometer_leg_material = PropertyTypeAssignment(
        code="CREEP_TEST_EXTENSOMETER_LEG_MATERIAL",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_EXTENSOMETER_LEG_MATERIAL",
        property_label="Extensometer leg material // Material der Extensometerschenkel",
        description="""Extensometer leg material - Material of upper/lower legs, e.g., in LVDT systems // Material der Extensometerschenkel – Material der Ober-/Unterbeine, z. B. in LVDT-Systemen""",
        mandatory=False,
        show_in_edit_views=False,
        section="Contacting extensometer",
    )

    creep_test_measuring_amplifier_model_information = PropertyTypeAssignment(
        code="CREEP_TEST_MEASURING_AMPLIFIER_MODEL_INFORMATION",
        data_type="VARCHAR",
        property_label="Measuring amplifier - Model information // Messverstärker – Modellinformationen",
        description="""Measuring amplifier - Model information // Messverstärker – Modellinformationen""",
        mandatory=False,
        show_in_edit_views=False,
        section="Contacting extensometer",
    )

    creep_test_extension_range_upper_limit = PropertyTypeAssignment(
        code="CREEP_TEST_EXTENSION_RANGE_UPPER_LIMIT",
        data_type="REAL",
        property_label="Extension range - Upper limit [% / mm] // Dehnmessbereich – Obergrenze [% / mm]",
        description="""Extension range - Upper limit // Dehnmessbereich – Obergrenze [% / mm]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Contacting extensometer",
    )

    creep_test_extension_range_lower_limit = PropertyTypeAssignment(
        code="CREEP_TEST_EXTENSION_RANGE_LOWER_LIMIT",
        data_type="REAL",
        property_label="Extension range - Lower limit [%  / mm] // Dehnmessbereich – Untergrenze [%  / mm]",
        description="""Extension range - Lower limit // Dehnmessbereich – Untergrenze [%  / mm]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Contacting extensometer",
    )

    creep_test_nominal_gauge_length = PropertyTypeAssignment(
        code="CREEP_TEST_NOMINAL_GAUGE_LENGTH",
        data_type="REAL",
        property_label="Nominal gauge length [mm] // Nennmesslänge [mm]",
        description="""Nominal gauge length - If applicable // Nennmesslänge [mm] – If applicable""",
        mandatory=True,
        show_in_edit_views=False,
        section="Contacting extensometer",
    )

    creep_test_is_the_extensometer_incl_the_data_acquisition_calibrated = PropertyTypeAssignment(
        code="CREEP_TEST_IS_THE_EXTENSOMETER_INCL_THE_DATA_ACQUISITION_CALIBRATED",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_EXTENSOMETER_CALIBRATION_STATUS",
        property_label="Is the extensometer incl. the data acquisition calibrated? // Extensometer inkl. Datenerfassung kalibriert?",
        description="""Is the extensometer incl. the data acquisition calibrated? - Is the extensometer incl. the data acquisition calibrated? // Extensometer inkl. Datenerfassung kalibriert? – Ist/War das Extensometer inkl. Datenerfassung kalibriert?""",
        mandatory=True,
        show_in_edit_views=False,
        section="Contacting extensometer",
    )

    creep_test_calibration_certificate = PropertyTypeAssignment(
        code="CALIBRATION_CERTIFICATE_NUMBER",
        data_type="VARCHAR",
        property_label="Calibration certificate // Kalibrierzertifikat",
        description="""Calibration certificate - Link to file, preferably with machine-readable (meta)data. // Kalibrierzertifikat – Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=False,
        show_in_edit_views=False,
        section="Contacting extensometer",
    )

    creep_test_calibration_date = PropertyTypeAssignment(
        code="CALIBRATION_DATE",
        data_type="DATE",
        property_label="Calibration date // Kalibrierdatum",
        description="""Calibration date // Kalibrierdatum""",
        mandatory=True,
        show_in_edit_views=False,
        section="Contacting extensometer",
    )

    creep_test_calibration_validity_time_period = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_VALIDITY_TIME_PERIOD",
        data_type="VARCHAR",
        property_label="Calibration validity time period // Gültigkeitszeitraum der Kalibrierung",
        description="""Calibration validity time period // Gültigkeitszeitraum der Kalibrierung""",
        mandatory=True,
        show_in_edit_views=False,
        section="Contacting extensometer",
    )

    creep_test_calibration_class = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_CLASS",
        data_type="VARCHAR",
        property_label="Calibration class // Calibration class",
        description="""Calibration class // Calibration class""",
        mandatory=True,
        show_in_edit_views=False,
        section="Contacting extensometer",
    )

    creep_test_calibration_range = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_RANGE",
        data_type="VARCHAR",
        property_label="Calibration Range [% (mm)] // Kalibrierbereich [% (mm)]",
        description="""Calibration Range // Kalibrierbereich [% (mm)]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Contacting extensometer",
    )

    creep_test_calibration_standard = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_STANDARD",
        data_type="VARCHAR",
        property_label="Calibration standard // Kalibrierstandard",
        description="""Calibration standard // Kalibrierstandard""",
        mandatory=True,
        show_in_edit_views=False,
        section="Contacting extensometer",
    )


# Section: Elongation values and cross-sectional dimensions
class CreepTestMetadataMeasuringAndTestEquipmentElongationValuesAndCrossSectionalDimensions(
    ObjectType
):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.METADATA.MEASURING_AND_TEST_EQUIPMENT.ELONGATION_VALUES_AND_CROSS_SECTIONAL_DIMENSIONS",
        description="""Metadata / Measuring and test equipment / Elongation values and cross-sectional dimensions // Metadaten / Mess- und Prüfmittel / Verlängerungswerte und Querschnittsabmessungen""",
        generated_code_prefix="EXP.MECH.CREEP.METADATA.MEASURIN.ELONGATI",
    )

    creep_test_measuring_equipment = PropertyTypeAssignment(
        code="CREEP_TEST_MEASURING_EQUIPMENT",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_MEASURING_EQUIPMENT",
        property_label="Measuring equipment // Messgerät",
        description="""Measuring equipment // Messgerät""",
        mandatory=True,
        show_in_edit_views=False,
        section="Elongation values and cross-sectional dimensions",
    )

    creep_test_measuring_equipment_s_usage = PropertyTypeAssignment(
        code="CREEP_TEST_MEASURING_EQUIPMENT_S_USAGE",
        data_type="VARCHAR",
        property_label="Measuring equipment's usage // Verwendung des Messgeräts",
        description="""Measuring equipment's usage // Verwendung des Messgeräts""",
        mandatory=True,
        show_in_edit_views=False,
        section="Elongation values and cross-sectional dimensions",
    )

    creep_test_resolution = PropertyTypeAssignment(
        code="FTIR.RESOLUTION",
        data_type="INTEGER",
        property_label="Resolution [mm] // Auflösung [mm]",
        description="""Resolution // Auflösung [mm]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Elongation values and cross-sectional dimensions",
    )

    creep_test_type = PropertyTypeAssignment(
        code="CREEP_TEST_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_MEASURING_EQUIPMENT_TYPE",
        property_label="Type // Typ",
        description="""Type // Typ""",
        mandatory=False,
        show_in_edit_views=False,
        section="Elongation values and cross-sectional dimensions",
    )

    creep_test_equipment_model_information = PropertyTypeAssignment(
        code="DEVICE_MODEL_NAME",
        data_type="VARCHAR",
        property_label="Equipment model information // Gerätemodellinformationen",
        description="""Equipment model information // Gerätemodellinformationen""",
        mandatory=False,
        show_in_edit_views=False,
        section="Elongation values and cross-sectional dimensions",
    )

    creep_test_equipment_id = PropertyTypeAssignment(
        code="CREEP_TEST_EQUIPMENT_ID",
        data_type="VARCHAR",
        property_label="Equipment ID // Geräte-ID",
        description="""Equipment ID - The ID used for identification in the laboratory // Geräte-ID – ID zur Identifikation im Labor""",
        mandatory=False,
        show_in_edit_views=False,
        section="Elongation values and cross-sectional dimensions",
    )

    creep_test_calibration_status = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_STATUS",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_MEASURING_EQUIPMENT_CALIBRATION_STATUS",
        property_label="Calibration status // Kalibrierstatus",
        description="""Calibration status - Is the measuring equipment calibrated? // Kalibrierstatus – Sind/Waren die Messgeräte kalibriert?""",
        mandatory=True,
        show_in_edit_views=False,
        section="Elongation values and cross-sectional dimensions",
    )

    creep_test_calibration_certificate = PropertyTypeAssignment(
        code="CALIBRATION_CERTIFICATE_NUMBER",
        data_type="VARCHAR",
        property_label="Calibration certificate // Kalibrierzertifikat",
        description="""Calibration certificate - Link to file, preferably with machine-readable (meta)data. // Kalibrierzertifikat – Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=False,
        show_in_edit_views=False,
        section="Elongation values and cross-sectional dimensions",
    )

    creep_test_calibration_date = PropertyTypeAssignment(
        code="CALIBRATION_DATE",
        data_type="DATE",
        property_label="Calibration date // Kalibrierdatum",
        description="""Calibration date // Kalibrierdatum""",
        mandatory=True,
        show_in_edit_views=False,
        section="Elongation values and cross-sectional dimensions",
    )

    creep_test_calibration_validity_time_period = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_VALIDITY_TIME_PERIOD",
        data_type="VARCHAR",
        property_label="Calibration validity time period // Gültigkeitszeitraum der Kalibrierung",
        description="""Calibration validity time period // Gültigkeitszeitraum der Kalibrierung""",
        mandatory=True,
        show_in_edit_views=False,
        section="Elongation values and cross-sectional dimensions",
    )

    creep_test_calibration_result = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_RESULT",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_MEASURING_EQUIPMENT_CALIBRATION_RESULT",
        property_label="Calibration result // Kalibrierergebnis",
        description="""Calibration result // Kalibrierergebnis""",
        mandatory=True,
        show_in_edit_views=False,
        section="Elongation values and cross-sectional dimensions",
    )

    creep_test_calibration_range = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_RANGE",
        data_type="REAL",
        property_label="Calibration range [mm] // Kalibrierbereich [mm]",
        description="""Calibration range // Kalibrierbereich [mm]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Elongation values and cross-sectional dimensions",
    )

    creep_test_calibration_standard = PropertyTypeAssignment(
        code="CREEP_TEST_CALIBRATION_STANDARD",
        data_type="VARCHAR",
        property_label="Calibration standard // Kalibrierstandard",
        description="""Calibration standard // Kalibrierstandard""",
        mandatory=True,
        show_in_edit_views=False,
        section="Elongation values and cross-sectional dimensions",
    )


# --------------------------------
# Section: Metadata - Data processing procedures
# --------------------------------


class CreepTestMetadataDataProcessingProcedures(ObjectType):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.METADATA.DATA_PROCESSING_PROCEDURES",
        description="""Metadata / Data processing procedures // Metadaten / Datenverarbeitungsverfahren""",
        generated_code_prefix="EXP.MECH.CREEP.METADATA.DATA_PRO",
    )

    creep_test_primary_data_series = PropertyTypeAssignment(
        code="CREEP_TEST_PRIMARY_DATA_SERIES",
        data_type="VARCHAR",
        property_label="Primary data series // Primärdatenreihen",
        description="""Primary data series - Primary data is data that is directly acquired by sensors or measuring instruments during or after a test. Please add a list of the measured quantities and their corresponsing units. // Primärdatenreihen – Primärdaten sind Daten, die während oder nach einer Prüfung direkt von Sensoren oder Messgeräten erfasst werden. Bitte fügen Sie eine Liste der gemessenen Größen und der zugehörigen Einheiten hinzu.""",
        mandatory=True,
        show_in_edit_views=False,
        section="Data processing procedures",
    )

    creep_test_processed_data_series = PropertyTypeAssignment(
        code="CREEP_TEST_PROCESSED_DATA_SERIES",
        data_type="VARCHAR",
        property_label="Processed data series // Verarbeitete Datenreihen",
        description="""Processed data series - Processed data is obtained as a result of using procedures (equations, algorithms, methods, unit conversions, averaging, smoothing) to transform primary data. Please describe the transformed quantities, their corresponsing units, and the applied procedures. // Verarbeitete Datenreihen – Verarbeitete Daten entstehen durch Verfahren (Gleichungen, Algorithmen, Methoden, Einheitenumrechnungen, Mittelung, Glättung), die Primärdaten transformieren. Bitte beschreiben Sie die transformierten Größen, deren Einheiten sowie die angewandten Verfahren.""",
        mandatory=True,
        show_in_edit_views=False,
        section="Data processing procedures",
    )

    creep_test_data_analysis_procedures = PropertyTypeAssignment(
        code="CREEP_TEST_DATA_ANALYSIS_PROCEDURES",
        data_type="VARCHAR",
        property_label="Data analysis procedures // Datenanalyseverfahren",
        description="""Data analysis procedures - Description of the data processing and analysis procedures used to obtain specific test results, e.g. percentage elastic extension, ee // Datenanalyseverfahren – Beschreibung der Datenverarbeitungs- und Analyseverfahren zur Ermittlung spezifischer Prüfergebnisse, z. B. prozentuale elastische Dehnung (ee).""",
        mandatory=True,
        show_in_edit_views=False,
        section="Data processing procedures",
    )

    creep_test_workflow_usage = PropertyTypeAssignment(
        code="CREEP_TEST_WORKFLOW_USAGE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_WORKFLOW_USAGE",
        property_label="Workflow usage // Workflow-Nutzung",
        description="""Workflow usage - Were automated (user-independent) analysis workflows used? // Workflow-Nutzung – Wurden automatisierte (benutzerunabhängige) Analyse-Workflows verwendet?""",
        mandatory=True,
        show_in_edit_views=False,
        section="Data processing procedures",
    )

    creep_test_software = PropertyTypeAssignment(
        code="CREEP_TEST_SOFTWARE",
        data_type="VARCHAR",
        property_label="Software // Software",
        description="""Software - If applicable, please list the used software/workflow, including product and version // Software – Falls zutreffend, bitte die verwendete Software bzw. den Workflow mit Produkt und Version angeben.""",
        mandatory=True,
        show_in_edit_views=False,
        section="Data processing procedures",
    )

    creep_test_related_publications = PropertyTypeAssignment(
        code="CREEP_TEST_RELATED_PUBLICATIONS",
        data_type="VARCHAR",
        property_label="Related publications // Zugehörige Publikationen",
        description="""Related publications - If applicable, please list publications related to the data analysis procedure/software used // Zugehörige Publikationen – Falls zutreffend, bitte Publikationen nennen, die sich auf das verwendete Datenanalyseverfahren bzw. die Software beziehen.""",
        mandatory=False,
        show_in_edit_views=False,
        section="Data processing procedures",
    )


# --------------------------------
# Section: Primary data - Test result
# --------------------------------


# Section: Values recorded at test start
class CreepTestPrimaryDataTestResultValuesRecordedAtTestStart(ObjectType):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.PRIMARY_DATA.TEST_RESULT.VALUES_RECORDED_AT_TEST_START",
        description="""Primary data / Test result / Values recorded at test start // Primärdaten / Prüfergebnis / Zu Testbeginn erfasste Werte""",
        generated_code_prefix="EXP.MECH.CREEP.PRIMARY_.TEST_RES.VALUES_R",
    )

    creep_test_minimum_test_piece_diameter_at_room_temperature = PropertyTypeAssignment(
        code="CREEP_TEST_MINIMUM_TEST_PIECE_DIAMETER_AT_ROOM_TEMPERATURE",
        data_type="REAL",
        property_label="Minimum test piece diameter at room temperature [mm] // Minimaler Proben-Durchmesser bei Raumtemperatur [mm]",
        description="""Minimum test piece diameter at room temperature // Minimaler Proben-Durchmesser bei Raumtemperatur [mm]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Values recorded at test start",
    )

    creep_test_original_gauge_length = PropertyTypeAssignment(
        code="CREEP_TEST_ORIGINAL_GAUGE_LENGTH",
        data_type="REAL",
        property_label="Original gauge length [mm] // Ursprüngliche Messlänge [mm]",
        description="""Original gauge length // Ursprüngliche Messlänge [mm]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Values recorded at test start",
    )

    creep_test_parallel_length = PropertyTypeAssignment(
        code="CREEP_TEST_PARALLEL_LENGTH",
        data_type="REAL",
        property_label="Parallel length [mm] // Parallele Länge [mm]",
        description="""Parallel length // Parallele Länge [mm]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Values recorded at test start",
    )

    creep_test_extensometer_gauge_length = PropertyTypeAssignment(
        code="CREEP_TEST_EXTENSOMETER_GAUGE_LENGTH",
        data_type="REAL",
        property_label="Extensometer gauge length [mm] // Extensometer-Messlänge [mm]",
        description="""Extensometer gauge length // Extensometer-Messlänge [mm]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Values recorded at test start",
    )

    creep_test_determination_of_reference_length = PropertyTypeAssignment(
        code="CREEP_TEST_DETERMINATION_OF_REFERENCE_LENGTH",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_DETERMINATION_OF_REFERENCE_LENGTH",
        property_label="Determination of reference length // Bestimmung der Referenzlänge",
        description="""Determination of reference length - Case 1: Reference length for calculation of percentage extensions/elongations if the original gauge length Lo and/or extensometer Le are inside the parallel length, Lc. In this case Lr = Le (percentage extensions) or Lr = Lo (percentage elongations). Case 2: Reference length for calculation of percentage extensions/elongations if the original gauge length Lo and/or extensometer Le are outside the parallel length, Lc. In this case, Lr, for calculation of percentage is corrected to consider the strain contributions of the shoulders/ridges. // Bestimmung der Referenzlänge – Case 1: Reference length for calculation of percentage extensions/elongations if the original gauge length Lo and/or extensometer Le are inside the parallel length, Lc. In this case Lr = Le (percentage extensions) or Lr = Lo (percentage elongations). Case 2: Reference length for calculation of percentage extensions/elongations if the original gauge length Lo and/or extensometer Le are outside the parallel length, Lc. In this case, Lr, for calculation of percentage is corrected to consider the strain contributions of the shoulders/ridges.""",
        mandatory=True,
        show_in_edit_views=False,
        section="Values recorded at test start",
    )

    creep_test_reference_length_to_calculate_percentage_elongations = PropertyTypeAssignment(
        code="CREEP_TEST_REFERENCE_LENGTH_TO_CALCULATE_PERCENTAGE_ELONGATIONS",
        data_type="REAL",
        property_label="Reference length to calculate percentage elongations [mm] // Referenzlänge zur Berechnung prozentualer Verlängerungen [mm]",
        description="""Reference length to calculate percentage elongations // Referenzlänge zur Berechnung prozentualer Verlängerungen [mm]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Values recorded at test start",
    )

    creep_test_reference_length_to_calculate_percentage_extensions = PropertyTypeAssignment(
        code="CREEP_TEST_REFERENCE_LENGTH_TO_CALCULATE_PERCENTAGE_EXTENSIONS",
        data_type="REAL",
        property_label="Reference length to calculate percentage extensions [mm] // Referenzlänge zur Berechnung prozentualer Dehnungen [mm]",
        description="""Reference length to calculate percentage extensions // Referenzlänge zur Berechnung prozentualer Dehnungen [mm]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Values recorded at test start",
    )

    creep_test_k_value = PropertyTypeAssignment(
        code="CREEP_TEST_K_VALUE",
        data_type="REAL",
        property_label="k-Value [mm] // k-Wert [mm]",
        description="""k-Value - Lr / ?So // k-Wert [mm] – Lr / ?So""",
        mandatory=True,
        show_in_edit_views=False,
        section="Values recorded at test start",
    )

    creep_test_ratio_reference_length_to_diameter = PropertyTypeAssignment(
        code="CREEP_TEST_RATIO_REFERENCE_LENGTH_TO_DIAMETER",
        data_type="REAL",
        property_label="Ratio reference length to diameter [mm] // Verhältnis Referenzlänge zu Durchmesser [mm]",
        description="""Ratio reference length to diameter - Lr / D // Verhältnis Referenzlänge zu Durchmesser [mm] – Lr / D""",
        mandatory=True,
        show_in_edit_views=False,
        section="Values recorded at test start",
    )


# Section: Values recorded during test run
class CreepTestPrimaryDataTestResultValuesRecordedDuringTestRun(ObjectType):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.PRIMARY_DATA.TEST_RESULT.VALUES_RECORDED_DURING_TEST_RUN",
        description="""Primary data / Test result / Values recorded during test run // Primärdaten / Prüfergebnis / Während des Versuchs erfasste Werte""",
        generated_code_prefix="EXP.MECH.CREEP.PRIMARY_.TEST_RES.VALUES_R",
    )

    creep_test_elapsed_time_from_end_of_loading = PropertyTypeAssignment(
        code="CREEP_TEST_ELAPSED_TIME_FROM_END_OF_LOADING",
        data_type="VARCHAR",
        property_label="Elapsed time from end of loading [s / h] // Verstrichene Zeit seit Ende der Belastung [s / h]",
        description="""Elapsed time from end of loading - Link to file, preferably with machine-readable (meta)data. // Verstrichene Zeit seit Ende der Belastung [s / h] – Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=True,
        show_in_edit_views=False,
        section="Values recorded during test run",
    )

    creep_test_force = PropertyTypeAssignment(
        code="CREEP_TEST_FORCE",
        data_type="REAL",
        property_label="Force [kN] // Kraft [kN]",
        description="""Force // Kraft [kN]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Values recorded during test run",
    )

    creep_test_extension = PropertyTypeAssignment(
        code="CREEP_TEST_EXTENSION",
        data_type="VARCHAR",
        property_label="Extension [mm] // Dehnung [mm]",
        description="""Extension - Link to file, preferably with machine-readable (meta)data. // Dehnung [mm] – Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=False,
        show_in_edit_views=False,
        section="Values recorded during test run",
    )

    creep_test_elongation = PropertyTypeAssignment(
        code="CREEP_TEST_ELONGATION",
        data_type="VARCHAR",
        property_label="Elongation [mm] // Verlängerung [mm]",
        description="""Elongation - Link to file, preferably with machine-readable (meta)data. // Verlängerung [mm] – Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=False,
        show_in_edit_views=False,
        section="Values recorded during test run",
    )

    creep_test_heating_time = PropertyTypeAssignment(
        code="CREEP_TEST_HEATING_TIME",
        data_type="REAL",
        property_label="Heating time [h] // Aufheizzeit [h]",
        description="""Heating time // Aufheizzeit [h]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Values recorded during test run",
    )

    creep_test_soak_time = PropertyTypeAssignment(
        code="CREEP_TEST_SOAK_TIME",
        data_type="REAL",
        property_label="Soak time [h] // Haltezeit [h]",
        description="""Soak time - Soak time before the test // Haltezeit [h] – Haltezeit vor der Prüfung""",
        mandatory=True,
        show_in_edit_views=False,
        section="Values recorded during test run",
    )

    creep_test_test_duration = PropertyTypeAssignment(
        code="CREEP_TEST_TEST_DURATION",
        data_type="REAL",
        property_label="Test duration [h] // Prüfdauer [h]",
        description="""Test duration // Prüfdauer [h]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Values recorded during test run",
    )


# Section: Values recorded after end of test
class CreepTestPrimaryDataTestResultValuesRecordedAfterEndOfTest(ObjectType):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.PRIMARY_DATA.TEST_RESULT.VALUES_RECORDED_AFTER_END_OF_TEST",
        description="""Primary data / Test result / Values recorded after end of test // Primärdaten / Prüfergebnis / Nach Testende erfasste Werte""",
        generated_code_prefix="EXP.MECH.CREEP.PRIMARY_.TEST_RES.VALUES_R",
    )

    creep_test_creep_rupture_time = PropertyTypeAssignment(
        code="CREEP_TEST_CREEP_RUPTURE_TIME",
        data_type="REAL",
        property_label="Creep rupture time [h] // Kriechbruchzeit [h]",
        description="""Creep rupture time // Kriechbruchzeit [h]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Values recorded after end of test",
    )

    creep_test_fracture_position = PropertyTypeAssignment(
        code="CREEP_TEST_FRACTURE_POSITION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_FRACTURE_POSITION",
        property_label="Fracture position // Bruchposition",
        description="""Fracture position // Bruchposition""",
        mandatory=True,
        show_in_edit_views=False,
        section="Values recorded after end of test",
    )

    creep_test_final_gauge_length_after_fracture = PropertyTypeAssignment(
        code="CREEP_TEST_FINAL_GAUGE_LENGTH_AFTER_FRACTURE",
        data_type="REAL",
        property_label="Final gauge length after fracture [mm] // Endmesslänge nach Bruch [mm]",
        description="""Final gauge length after fracture // Endmesslänge nach Bruch [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Values recorded after end of test",
    )


# --------------------------------
# Section: Secondary data - Test result
# --------------------------------


# Section: Values recorded during test run
class CreepTestSecondaryDataTestResultValuesRecordedDuringTestRun(ObjectType):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.SECONDARY_DATA.TEST_RESULT.VALUES_RECORDED_DURING_TEST_RUN",
        description="""Secondary data / Test result / Values recorded during test run // Sekundärdaten / Prüfergebnis / Während des Versuchs erfasste Werte""",
        generated_code_prefix="EXP.MECH.CREEP.SECONDAR.TEST_RES.VALUES_R",
    )

    creep_test_corrected_measured_temperature = PropertyTypeAssignment(
        code="CREEP_TEST_CORRECTED_MEASURED_TEMPERATURE",
        data_type="VARCHAR",
        property_label="Corrected measured temperature [?] // Korrigierte gemessene Temperatur [?]",
        description="""Corrected measured temperature - Link to file, preferably with machine-readable (meta)data. // Korrigierte gemessene Temperatur [?] – Link zu einer Datei, vorzugsweise mit maschinenlesbaren (Meta-)Daten.""",
        mandatory=True,
        show_in_edit_views=False,
        section="Values recorded during test run",
    )

    creep_test_loading_rate = PropertyTypeAssignment(
        code="CREEP_TEST_LOADING_RATE",
        data_type="REAL",
        property_label="Loading rate [MPa/s] // Belastungsrate [MPa/s]",
        description="""Loading rate // Belastungsrate [MPa/s]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Values recorded during test run",
    )

    creep_test_unloading_rate = PropertyTypeAssignment(
        code="CREEP_TEST_UNLOADING_RATE",
        data_type="REAL",
        property_label="Unloading rate [MPa/s] // Entlastungsrate [MPa/s]",
        description="""Unloading rate // Entlastungsrate [MPa/s]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Values recorded during test run",
    )

    creep_test_heating_speed = PropertyTypeAssignment(
        code="CREEP_TEST_HEATING_SPEED",
        data_type="REAL",
        property_label="Heating speed [?/min] // Aufheizgeschwindigkeit [?/min]",
        description="""Heating speed // Aufheizgeschwindigkeit [?/min]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Values recorded during test run",
    )

    creep_test_cooling_speed = PropertyTypeAssignment(
        code="CREEP_TEST_COOLING_SPEED",
        data_type="REAL",
        property_label="Cooling speed [?/min] // Abkühlgeschwindigkeit [?/min]",
        description="""Cooling speed // Abkühlgeschwindigkeit [?/min]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Values recorded during test run",
    )

    creep_test_percentage_extension = PropertyTypeAssignment(
        code="CREEP_TEST_PERCENTAGE_EXTENSION",
        data_type="VARCHAR",
        property_label="Percentage extension [%] // Prozentuale Dehnung [%]",
        description="""Percentage extension - Link to file, preferably with machine-readable (meta)data. Data series corresponds to the percentage plastic extension from end of loading. If the percentage initial plastic extension is not zero, these data series coresponds to the percentage creep extension from end of loading. // Prozentuale Dehnung [%] – Link to file, preferably with machine-readable (meta)data. Data series corresponds to the percentage plastic extension from end of loading. If the percentage initial plastic extension is not zero, these data series coresponds to the percentage creep extension from end of loading.""",
        mandatory=True,
        show_in_edit_views=False,
        section="Values recorded during test run",
    )


# Section: Elongation values
class CreepTestSecondaryDataTestResultElongationValues(ObjectType):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.SECONDARY_DATA.TEST_RESULT.ELONGATION_VALUES",
        description="""Secondary data / Test result / Elongation values // Sekundärdaten / Prüfergebnis / Verlängerungswerte""",
        generated_code_prefix="EXP.MECH.CREEP.SECONDAR.TEST_RES.ELONGATI",
    )

    creep_test_percentage_permanent_elongation = PropertyTypeAssignment(
        code="CREEP_TEST_PERCENTAGE_PERMANENT_ELONGATION",
        data_type="REAL",
        property_label="Percentage permanent elongation [%] // Prozentuale bleibende Verlängerung [%]",
        description="""Percentage permanent elongation // Prozentuale bleibende Verlängerung [%]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Elongation values",
    )

    creep_test_percentage_elongation_after_creep_fracture = PropertyTypeAssignment(
        code="CREEP_TEST_PERCENTAGE_ELONGATION_AFTER_CREEP_FRACTURE",
        data_type="REAL",
        property_label="Percentage elongation after creep fracture [%] // Prozentuale Bruchverlängerung nach Kriechbruch [%]",
        description="""Percentage elongation after creep fracture // Prozentuale Bruchverlängerung nach Kriechbruch [%]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Elongation values",
    )

    creep_test_percentage_reduction_of_area_after_creep_fracture = PropertyTypeAssignment(
        code="CREEP_TEST_PERCENTAGE_REDUCTION_OF_AREA_AFTER_CREEP_FRACTURE",
        data_type="REAL",
        property_label="Percentage reduction of area after creep fracture [%] // Prozentuale Brucheinschnürung nach Kriechbruch [%]",
        description="""Percentage reduction of area after creep fracture // Prozentuale Brucheinschnürung nach Kriechbruch [%]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Elongation values",
    )


# Section: Extension values
class CreepTestSecondaryDataTestResultExtensionValues(ObjectType):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MECHANICAL_TEST.CREEP_TEST.SECONDARY_DATA.TEST_RESULT.EXTENSION_VALUES",
        description="""Secondary data / Test result / Extension values // Sekundärdaten / Prüfergebnis / Dehnungswerte""",
        generated_code_prefix="EXP.MECH.CREEP.SECONDAR.TEST_RES.EXTENSIO",
    )

    creep_test_percentage_total_extension = PropertyTypeAssignment(
        code="CREEP_TEST_PERCENTAGE_TOTAL_EXTENSION",
        data_type="REAL",
        property_label="Percentage total extension [%] // Prozentuale Gesamtdehnung [%]",
        description="""Percentage total extension // Prozentuale Gesamtdehnung [%]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Extension values",
    )

    creep_test_percentage_initial_total_extension = PropertyTypeAssignment(
        code="CREEP_TEST_PERCENTAGE_INITIAL_TOTAL_EXTENSION",
        data_type="REAL",
        property_label="Percentage initial total extension [%] // Prozentuale anfängliche Gesamtdehnung [%]",
        description="""Percentage initial total extension // Prozentuale anfängliche Gesamtdehnung [%]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Extension values",
    )

    creep_test_percentage_elastic_extension = PropertyTypeAssignment(
        code="CREEP_TEST_PERCENTAGE_ELASTIC_EXTENSION",
        data_type="REAL",
        property_label="Percentage elastic extension [%] // Prozentuale elastische Dehnung [%]",
        description="""Percentage elastic extension // Prozentuale elastische Dehnung [%]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Extension values",
    )

    creep_test_percentage_initial_plastic_extension = PropertyTypeAssignment(
        code="CREEP_TEST_PERCENTAGE_INITIAL_PLASTIC_EXTENSION",
        data_type="REAL",
        property_label="Percentage initial plastic extension [%] // Prozentuale anfängliche plastische Dehnung [%]",
        description="""Percentage initial plastic extension // Prozentuale anfängliche plastische Dehnung [%]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Extension values",
    )

    creep_test_percentage_plastic_extension = PropertyTypeAssignment(
        code="CREEP_TEST_PERCENTAGE_PLASTIC_EXTENSION",
        data_type="REAL",
        property_label="Percentage plastic extension [%] // Prozentuale plastische Dehnung [%]",
        description="""Percentage plastic extension // Prozentuale plastische Dehnung [%]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Extension values",
    )

    creep_test_percentage_creep_extension = PropertyTypeAssignment(
        code="CREEP_TEST_PERCENTAGE_CREEP_EXTENSION",
        data_type="REAL",
        property_label="Percentage creep extension [%] // Prozentuale Kriechdehnung [%]",
        description="""Percentage creep extension // Prozentuale Kriechdehnung [%]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Extension values",
    )
