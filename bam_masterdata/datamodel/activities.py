from bam_masterdata.datamodel.object_types import ExperimentalStep
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.entities import ObjectType


class Dcpd(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.DCPD",
        description="""Direct Current Potential Drop (DCPD) Method//DC-Spannungsabfall (DCPD)-Methode""",
        generated_code_prefix="EXP.DCPD",
    )

    dcpd_pot_drop_cal = PropertyTypeAssignment(
        code="DCPD_POT_DROP_CAL",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DCPD_POT_CAL",
        property_label="Potential Drop Calibration",
        description="""Potential Drop Calibration//Kalibrierung des Potentialabfalls""",
        mandatory=False,
        section="Setup",
    )

    dcpd_current = PropertyTypeAssignment(
        code="DCPD_CURRENT",
        data_type="REAL",
        property_label="Current [A]",
        description="""DCPD Current [A]//DCPD Stromstärke [A]""",
        mandatory=False,
        section="Setup",
    )

    dcpd_initial_cracklength = PropertyTypeAssignment(
        code="DCPD_INITIAL_CRACKLENGTH",
        data_type="REAL",
        property_label="Initial Cracklength (measured optically) [mm]",
        description="""Initial Cracklength (measured optically) [mm]// Initiale Risslänge (optisch vermessen) [mm]""",
        mandatory=False,
        section="Setup",
    )

    dcpd_yzero_fitted = PropertyTypeAssignment(
        code="DCPD_YZERO_FITTED",
        data_type="REAL",
        property_label="Y0 in Johnson Formula fitted for Notch Geometry [mm]",
        description="""Y0 in Johnson Formula fitted for Notch Geometry [mm]//Y0 in Johnson Formel angepasst an die Kerbgeometrie [mm]""",
        mandatory=False,
        section="Setup",
    )

    fem_fit_eq = PropertyTypeAssignment(
        code="FEM_FIT_EQ",
        data_type="VARCHAR",
        property_label="Equation of FEM Fit a = f(U)",
        description="""Equation of FEM Fit a = f(U)//Gleichung für FEM Fit a = f(U)""",
        mandatory=False,
        section="Setup",
    )

    dcpd_proportional_potential = PropertyTypeAssignment(
        code="DCPD_PROPORTIONAL_POTENTIAL",
        data_type="BOOLEAN",
        property_label="Output Signal proportional to Potential Drop",
        description="""Output Signal proportional to Potential Drop//Ausgangssignal proportional zum Potentialabfall""",
        mandatory=False,
        section="Direct Amplification of Corrected Potential Drop",
    )

    dcpd_initial_potential_drop = PropertyTypeAssignment(
        code="DCPD_INITIAL_POTENTIAL_DROP",
        data_type="REAL",
        property_label="Initial Potential Drop (amplified) [V]",
        description="""Initial Potential Drop (amplified) [V]//Initiale Potentialabfall (verstärkt) [V]""",
        mandatory=False,
        section="Direct Amplification of Corrected Potential Drop",
    )

    dcpd_amplification_factor = PropertyTypeAssignment(
        code="DCPD_AMPLIFICATION_FACTOR",
        data_type="REAL",
        property_label="Amplification Factor",
        description="""Amplification Factor//Verstärkungsfaktor""",
        mandatory=False,
        section="Direct Amplification of Corrected Potential Drop",
    )

    dcpd_linearised_potential = PropertyTypeAssignment(
        code="DCPD_LINEARISED_POTENTIAL",
        data_type="BOOLEAN",
        property_label="Output Signal Proportional to Cracklength",
        description="""Output Signal Proportional to Cracklength//Ausgangssignal proportional zur Risslänge""",
        mandatory=False,
        section="Output Potential Proportional to Cracklength",
    )

    dcpd_temp_comp = PropertyTypeAssignment(
        code="DCPD_TEMP_COMP",
        data_type="BOOLEAN",
        property_label="Temperature Compensation",
        description="""Temperature Compensation//Temperaturkompensation""",
        mandatory=False,
        section="Temperature Compensation",
    )

    dcpd_initial_temp = PropertyTypeAssignment(
        code="DCPD_INITIAL_TEMP",
        data_type="REAL",
        property_label="Initial Temperature [°C]",
        description="""Initial Temperature [°C]//Anfangstemperatur [°C]""",
        mandatory=False,
        section="Temperature Compensation",
    )

    dcpd_temp_coeff = PropertyTypeAssignment(
        code="DCPD_TEMP_COEFF",
        data_type="REAL",
        property_label="Temperature Coefficient of Resistivity [°C^-1]",
        description="""Temperature Coefficient of Resistivity [°C^-1]//Temperaturkoeffizient der Resistivität [°C^-1]""",
        mandatory=False,
        section="Temperature Compensation",
    )


class FcgTest(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.FCG_TEST",
        description="""Fatigue Crack Growth Test//Rissfortschrittsversuch""",
        generated_code_prefix="EXP.FCG_TEST",
    )

    fcg_nominal_r = PropertyTypeAssignment(
        code="FCG_NOMINAL_R",
        data_type="REAL",
        property_label="Test Nominal R-Ratio",
        description="""Test Nominal R-Ratio//Nominelles R-Verhältnis des Tests""",
        mandatory=True,
        section="Experimental Details FCG",
    )

    fcg_thrshld = PropertyTypeAssignment(
        code="FCG_THRSHLD",
        data_type="BOOLEAN",
        property_label="Threshold Determination",
        description="""Threshold Stress Intensity Factor Range Determination//Ermittlung des Schwellenwertes gegen Ermüdungsrissausbreitung""",
        mandatory=False,
        section="Experimental Details FCG",
    )

    fcg_paris = PropertyTypeAssignment(
        code="FCG_PARIS",
        data_type="BOOLEAN",
        property_label="PARIS Parameters Determination",
        description="""PARIS Regime Parameters Determination//Ermittlung der PARIS-Parameter""",
        mandatory=False,
        section="Experimental Details FCG",
    )

    fcg_cyclic_r = PropertyTypeAssignment(
        code="FCG_CYCLIC_R",
        data_type="BOOLEAN",
        property_label="Cyclic R-Curve",
        description="""Cyclic R-Curve Determination//Ermittlung der zyklischen R-Kurve""",
        mandatory=False,
        section="Experimental Details FCG",
    )

    fcg_result_thrshld = PropertyTypeAssignment(
        code="FCG_RESULT_THRSHLD",
        data_type="REAL",
        property_label="Threshold Stress intensity Factor Range",
        description="""Threshold Stress Intensity Factor Range//Schwellenwert gegen Ermüdungsrissausbreitung""",
        mandatory=False,
        section="Experimental Results",
    )

    fcg_result_paris_c = PropertyTypeAssignment(
        code="FCG_RESULT_PARIS_C",
        data_type="REAL",
        property_label="PARIS Parameter C",
        description="""PARIS Parameter C//PARIS Parameter C""",
        mandatory=False,
        section="Experimental Results",
    )

    fcg_result_paris_m = PropertyTypeAssignment(
        code="FCG_RESULT_PARIS_M",
        data_type="REAL",
        property_label="PARIS Parameter m",
        description="""PARIS Parameter m//PARIS Parameter m""",
        mandatory=False,
        section="Experimental Results",
    )

    fcg_result_cyclicr_a = PropertyTypeAssignment(
        code="FCG_RESULT_CYCLICR_A",
        data_type="REAL",
        property_label="Cyclic R-Curve Parameter A",
        description="""Cyclic R-Curve Parameter A//Zyklische R-Kurve Parameter A""",
        mandatory=False,
        section="Experimental Results",
    )

    fcg_result_cyclicr_b = PropertyTypeAssignment(
        code="FCG_RESULT_CYCLICR_B",
        data_type="REAL",
        property_label="Cyclic R-Curve Parameter b",
        description="""Cyclic R-Curve Parameter b//Zyklische R-Kurve Parameter b""",
        mandatory=False,
        section="Experimental Results",
    )


class RazorbladeNotching(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.RAZORBLADE_NOTCHING",
        description="""Razorblade Notching//Kerbeinbringung mittels Rasierklinge""",
        generated_code_prefix="EXP.FCG_RAZOR",
    )

    razor_strokelength = PropertyTypeAssignment(
        code="RAZOR_STROKELENGTH",
        data_type="REAL",
        property_label="Stroke Length [mm]",
        description="""Stroke Length [mm]//Klingenhub [mm]""",
        mandatory=False,
        section="Process Parameters",
    )

    razor_strokespeed = PropertyTypeAssignment(
        code="RAZOR_STROKESPEED",
        data_type="REAL",
        property_label="Stroke Speed [mm/s]",
        description="""Stroke Speed [mm/s]//Hubgeschwindigkeit [mm/s]""",
        mandatory=False,
        section="Process Parameters",
    )

    razor_strokecount = PropertyTypeAssignment(
        code="RAZOR_STROKECOUNT",
        data_type="REAL",
        property_label="Stroke Count",
        description="""Stroke Count//Anzahl der Klingenhuebe""",
        mandatory=False,
        section="Process Parameters",
    )

    razor_depth = PropertyTypeAssignment(
        code="RAZOR_DEPTH",
        data_type="REAL",
        property_label="Notch Depth Increase according to Gauge [µm]",
        description="""Notch Depth Increase according to Gauge [µm]//Kerbvertiefenzunahme nach Messuhr [µm]""",
        mandatory=False,
        section="Results",
    )


class FcgStep(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.FCG_STEP",
        description="""Single Step of a Fatigue Crack Growth (FCG) Test//Einzelner Schritt eines Rissfortschritt-Tests""",
        generated_code_prefix="EXP.FCG_STEP",
    )

    step_no = PropertyTypeAssignment(
        code="STEP_NO",
        data_type="INTEGER",
        property_label="Step No.",
        description="""Step Number//Schrittnummer""",
        mandatory=True,
        section="Step Information",
    )

    fcg_step_type = PropertyTypeAssignment(
        code="FCG_STEP_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="FCG_STEP_TYPE",
        property_label="Step Type",
        description="""Step Type//Versuchsschritt-Typ""",
        mandatory=False,
        section="Step Information",
    )

    fcg_step_precrack = PropertyTypeAssignment(
        code="FCG_STEP_PRECRACK",
        data_type="BOOLEAN",
        property_label="Precracking Step",
        description="""Precracking Step//Precracking-Schritt""",
        mandatory=False,
        section="Step Information",
    )

    initial_cycles = PropertyTypeAssignment(
        code="INITIAL_CYCLES",
        data_type="INTEGER",
        property_label="Initial Cycle Count",
        description="""Initial Cycle Count//Initiale Zyklenzahl""",
        mandatory=False,
        section="Step Initial Parameters (Manual Input)",
    )

    initial_cracklength = PropertyTypeAssignment(
        code="INITIAL_CRACKLENGTH",
        data_type="REAL",
        property_label="Initial Cracklength [mm]",
        description="""Initial Cracklength [mm]//Initiale Risslänge [mm]""",
        mandatory=True,
        section="Step Initial Parameters (Manual Input)",
    )

    initial_r_ratio = PropertyTypeAssignment(
        code="INITIAL_R_RATIO",
        data_type="REAL",
        property_label="Initial R-Ratio",
        description="""Initial R-Ratio//Initiales R-Verhältnis""",
        mandatory=False,
        section="Step Initial Parameters (Manual Input)",
    )

    initial_deltak = PropertyTypeAssignment(
        code="INITIAL_DELTAK",
        data_type="REAL",
        property_label="Initial Delta K [MPa*m^0,5]",
        description="""Initial Delta K [MPa*m^0,5]//Initiales Delta K [MPa*m^0,5]""",
        mandatory=False,
        section="Step Initial Parameters (Manual Input)",
    )

    deltak_exponent = PropertyTypeAssignment(
        code="DELTAK_EXPONENT",
        data_type="REAL",
        property_label="Exponent for Delta K increase or decrease [mm^-1]",
        description="""Exponent for Delta K increase or decrease [mm^-1]//Exponent für Lastabsenkung oder -erhöhung [mm^-1]""",
        mandatory=False,
        section="Step Initial Parameters (Manual Input)",
    )

    increment_dadn = PropertyTypeAssignment(
        code="INCREMENT_DADN",
        data_type="REAL",
        property_label="Increment for da/dN calculation [mm]",
        description="""Increment for da/dN calculation [mm]//Inkrement für die Rissfortschrittsratenbestimmung [mm]""",
        mandatory=False,
        section="Step Initial Parameters (Manual Input)",
    )

    final_cycles = PropertyTypeAssignment(
        code="FINAL_CYCLES",
        data_type="REAL",
        property_label="Final Cycle Count",
        description="""Final Cycle Count//Finale Zyklenzahl""",
        mandatory=False,
        section="Step Final Parameters (Manual Input)",
    )

    final_cracklength = PropertyTypeAssignment(
        code="FINAL_CRACKLENGTH",
        data_type="REAL",
        property_label="Final Cracklength [mm]",
        description="""Final Cracklength [mm]//Finale Risslänge [mm]""",
        mandatory=False,
        section="Step Final Parameters (Manual Input)",
    )

    final_r_ratio = PropertyTypeAssignment(
        code="FINAL_R_RATIO",
        data_type="REAL",
        property_label="Final R-Ratio",
        description="""Final R-Ratio//Finales R-Verhältnis""",
        mandatory=False,
        section="Step Final Parameters (Manual Input)",
    )

    final_deltak = PropertyTypeAssignment(
        code="FINAL_DELTAK",
        data_type="REAL",
        property_label="Final Delta K [MPa*m^0,5]",
        description="""Final Delta K [MPa*m^0,5]//Finales Delta K [MPa*m^0,5]""",
        mandatory=False,
        section="Step Final Parameters (Manual Input)",
    )

    propagation = PropertyTypeAssignment(
        code="PROPAGATION",
        data_type="BOOLEAN",
        property_label="Crack Propagation during Step",
        description="""Crack Propagation during Step//Risserweiterung während des Versuchschrittes""",
        mandatory=False,
        section="Propagation/Arrest",
    )

    arrest = PropertyTypeAssignment(
        code="ARREST",
        data_type="BOOLEAN",
        property_label="Crack Arrest during Step",
        description="""Crack Arrest during Step//Rissarrest während des Versuchschrittes""",
        mandatory=False,
        section="Propagation/Arrest",
    )

    initial_kmax = PropertyTypeAssignment(
        code="INITIAL_KMAX",
        data_type="REAL",
        property_label="Initial K_max [MPa*m^0,5]",
        description="""Initial K_max [MPa*m^0,5]//Initiales K_max [MPa*m^0,5]""",
        mandatory=False,
        section="Derived Parameters (Automatic Input)",
    )

    initial_kmin = PropertyTypeAssignment(
        code="INITIAL_KMIN",
        data_type="REAL",
        property_label="Initial K_min [MPa*m^0,5]",
        description="""Initial K_min [MPa*m^0,5]//Initiales K_min [MPa*m^0,5]""",
        mandatory=False,
        section="Derived Parameters (Automatic Input)",
    )

    initial_kamp = PropertyTypeAssignment(
        code="INITIAL_KAMP",
        data_type="REAL",
        property_label="Initial K_amp [MPa*m^0,5]",
        description="""Initial K_amp [MPa*m^0,5]//Initiales K_amp [MPa*m^0,5]""",
        mandatory=False,
        section="Derived Parameters (Automatic Input)",
    )

    initial_kmean = PropertyTypeAssignment(
        code="INITIAL_KMEAN",
        data_type="REAL",
        property_label="Initial K_mean [MPa*m^0,5]",
        description="""Initial K_mean [MPa*m^0,5]//Initiales K_mean [MPa*m^0,5]""",
        mandatory=False,
        section="Derived Parameters (Automatic Input)",
    )

    initial_geomfun = PropertyTypeAssignment(
        code="INITIAL_GEOMFUN",
        data_type="REAL",
        property_label="Initial Stress Intensity Factor Geometry Function",
        description="""Initial Stress Intensity Factor Geometry Function//Initiale Geometriefunktion des Spannungsintensitätsfaktors""",
        mandatory=False,
        section="Derived Parameters (Automatic Input)",
    )

    initial_deltaf = PropertyTypeAssignment(
        code="INITIAL_DELTAF",
        data_type="REAL",
        property_label="Initial Delta F [kN]",
        description="""Initial Delta F [kN]//Initiales Delta F [kN]""",
        mandatory=False,
        section="Derived Parameters (Automatic Input)",
    )

    initial_fmax = PropertyTypeAssignment(
        code="INITIAL_FMAX",
        data_type="REAL",
        property_label="Initial F_max [kN]",
        description="""Initial F_max [kN]//Initiales F_max [kN]""",
        mandatory=False,
        section="Derived Parameters (Automatic Input)",
    )

    initial_fmin = PropertyTypeAssignment(
        code="INITIAL_FMIN",
        data_type="REAL",
        property_label="Initial F_min [kN]",
        description="""Initial F_min [kN]//Initiales F_min [kN]""",
        mandatory=False,
        section="Derived Parameters (Automatic Input)",
    )

    initial_famp = PropertyTypeAssignment(
        code="INITIAL_FAMP",
        data_type="REAL",
        property_label="Initial F_amp [kN]",
        description="""Initial F_amp [kN]//Initiales F_amp [kN]""",
        mandatory=False,
        section="Derived Parameters (Automatic Input)",
    )

    initial_fmean = PropertyTypeAssignment(
        code="INITIAL_FMEAN",
        data_type="REAL",
        property_label="Initial F_mean [kN]",
        description="""Initial F_mean [kN]//Initiales F_mean [kN]""",
        mandatory=False,
        section="Derived Parameters (Automatic Input)",
    )

    initial_ssy_ratio = PropertyTypeAssignment(
        code="INITIAL_SSY_RATIO",
        data_type="REAL",
        property_label="Ratio of Ligament Length to critical Ligament Length",
        description="""Ratio of Ligament Length to critical Ligament Length//Verhältnis von Ligamentlänge zu kritischer Ligamentlänge""",
        mandatory=False,
        section="Derived Parameters (Automatic Input)",
    )

    delta_a = PropertyTypeAssignment(
        code="DELTA_A",
        data_type="REAL",
        property_label="Crack Extension [mm]",
        description="""Crack Extension [mm]//Risserweiterung [mm]""",
        mandatory=False,
        section="Derived Parameters (Automatic Input)",
    )

    delta_n = PropertyTypeAssignment(
        code="DELTA_N",
        data_type="INTEGER",
        property_label="Elapsed Cycles in Step",
        description="""Elapsed Cycles in Step//Im Versuchsschritt gefahrene Zyklen""",
        mandatory=False,
        section="Derived Parameters (Automatic Input)",
    )

    final_geomfun = PropertyTypeAssignment(
        code="FINAL_GEOMFUN",
        data_type="REAL",
        property_label="Final Stress Intensity Factor Geometry Function",
        description="""Final Stress Intensity Factor Geometry Function//Finale Geometriefunktion des Spannungsintensitätsfaktors""",
        mandatory=False,
        section="Derived Parameters (Automatic Input)",
    )

    final_deltaf = PropertyTypeAssignment(
        code="FINAL_DELTAF",
        data_type="REAL",
        property_label="Final Delta F [kN]",
        description="""Final Delta F [kN]//Finales Delta F [kN]""",
        mandatory=False,
        section="Derived Parameters (Automatic Input)",
    )

    final_fmax = PropertyTypeAssignment(
        code="FINAL_FMAX",
        data_type="REAL",
        property_label="Final F_max [kN]",
        description="""Final F_max [kN]//Finales F_max [kN]""",
        mandatory=False,
        section="Derived Parameters (Automatic Input)",
    )

    final_fmin = PropertyTypeAssignment(
        code="FINAL_FMIN",
        data_type="REAL",
        property_label="Final F_min [kN]",
        description="""Final F_min [kN]//Finales F_min [kN]""",
        mandatory=False,
        section="Derived Parameters (Automatic Input)",
    )

    final_famp = PropertyTypeAssignment(
        code="FINAL_FAMP",
        data_type="REAL",
        property_label="Final F_amp [kN]",
        description="""Final F_amp [kN]//Finales F_amp [kN]""",
        mandatory=False,
        section="Derived Parameters (Automatic Input)",
    )

    final_fmean = PropertyTypeAssignment(
        code="FINAL_FMEAN",
        data_type="REAL",
        property_label="Final F_mean [kN]",
        description="""Final F_mean [kN]//Finales F_mean [kN]""",
        mandatory=False,
        section="Derived Parameters (Automatic Input)",
    )

    final_ssy_ratio = PropertyTypeAssignment(
        code="FINAL_SSY_RATIO",
        data_type="REAL",
        property_label="Ratio of Ligament Length to critical Ligament Length",
        description="""Ratio of Ligament Length to critical Ligament Length//Verhältnis von Ligamentlänge zu kritischer Ligamentlänge""",
        mandatory=False,
        section="Derived Parameters (Automatic Input)",
    )


class MicroscopyFcgFractureSurfaceCracklength(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MICROSCOPY_FCG_FRACTURE_SURFACE_CRACKLENGTH",
        description="""Optical Measurement of Cracklength on the Fracture Surface of an FCG Specimen//Lichtmikroskopische Messung einer Risslänge auf der Bruchfläche einer Ermüdungsrissfortschrittsprobe""",
        generated_code_prefix="EXP.MIC_FCG_FRACSURF_CRACKLENGTH",
    )

    mic_fcg_fracsurf_cracklength_type = PropertyTypeAssignment(
        code="MIC_FCG_FRACSURF_CRACKLENGTH_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="MICROSCOPY_FCG_CRACKLENGTH_TYPE",
        property_label="Type of Cracklength measured on Fracture Surface",
        description="""Type of Cracklength measured on Fracture Surface//Art der auf der Bruchfläche gemessenen Risslänge""",
        mandatory=False,
        section="Experimental Details",
    )

    mic_fcg_fracsurf_cracklength_value = PropertyTypeAssignment(
        code="MIC_FCG_FRACSURF_CRACKLENGTH_VALUE",
        data_type="REAL",
        property_label="Value of Cracklength measured on Fracture Surface [mm]",
        description="""Value of Cracklength measured on Fracture Surface [mm]//Wert der auf der Bruchfläche gemessenen Risslänge [mm]""",
        mandatory=False,
        section="Experimental Details",
    )

    mic_fcg_fracsurf_cracklength_cycles = PropertyTypeAssignment(
        code="MIC_FCG_FRACSURF_CRACKLENGTH_CYCLES",
        data_type="INTEGER",
        property_label="Cycle Count corresponding with Cracklength measured on Fracture Surface",
        description="""Cycle Count corresponding with Cracklength measured on Fracture Surface//Mit der auf der Bruchfläche gemessenen Länge korrespondierende Zyklenzahl""",
        mandatory=False,
        section="Experimental Details",
    )


class FcgEvaluation(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.FCG_EVALUATION",
        description="""Fatigue Crack Growth Data Evaluation//Rissfortschrittsversuch Datenauswertung""",
        generated_code_prefix="EXP.FCG_EVAL",
    )

    test_type = PropertyTypeAssignment(
        code="TEST_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TEST_PROGRAM_TYPE",
        property_label="Test Type",
        description="""Test Type//Art des Versuchs""",
        mandatory=False,
        section="Experimental Details",
    )


class ImageSeries(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.IMAGE_SERIES",
        description="""A series of one or more still image recordings//Eine Serie aus einer oder mehrerer Einzelbildaufnahmen""",
        generated_code_prefix="EXP.IMG_SRS",
    )

    uuid = PropertyTypeAssignment(
        code="UUID",
        data_type="VARCHAR",
        property_label="UUID",
        description="""A Universally Unique IDentifier (UUID/GUID) according to RFC 4122//Ein Universally Unique IDentifier (UUID/GUID) nach RFC 4122""",
        mandatory=False,
        section="Identifiers",
    )

    image_horizontal_resolution = PropertyTypeAssignment(
        code="IMAGE_HORIZONTAL_RESOLUTION",
        data_type="INTEGER",
        property_label="Horizontal resolution [pixel]",
        description="""Horizontal resolution of the image [pixel]//Horizonzale Auflösung des Bildes [Pixel]""",
        mandatory=False,
        section="Image Series Information",
    )

    image_vertical_resolution = PropertyTypeAssignment(
        code="IMAGE_VERTICAL_RESOLUTION",
        data_type="INTEGER",
        property_label="Vertical resolution [pixel]",
        description="""Vertical resolution of the image [pixel]////Vertikale Auflösung des Bildes [Pixel]""",
        mandatory=False,
        section="Image Series Information",
    )

    image_series_count = PropertyTypeAssignment(
        code="IMAGE_SERIES_COUNT",
        data_type="INTEGER",
        property_label="Number of images recorded",
        description="""Number of images recorded//Anzahl der aufgenommenen Bilder""",
        mandatory=False,
        section="Image Series Information",
    )


class ProfileScan(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.PROFILE_SCAN",
        description="""A series of 2D line sensor readings//Eine Reihe von 2D Profillinienaufnahmen""",
        generated_code_prefix="EXP.LINE_SCAN",
    )

    uuid = PropertyTypeAssignment(
        code="UUID",
        data_type="VARCHAR",
        property_label="UUID",
        description="""A Universally Unique IDentifier (UUID/GUID) according to RFC 4122//Ein Universally Unique IDentifier (UUID/GUID) nach RFC 4122""",
        mandatory=False,
        section="Identifiers",
    )

    scan_line_count = PropertyTypeAssignment(
        code="SCAN_LINE_COUNT",
        data_type="INTEGER",
        property_label="Scan line count",
        description="""Number of individual scan lines recorded//Anzahl der aufgenommenen Scanlinien""",
        mandatory=False,
        section="Scan Information",
    )

    scan_line_resolution = PropertyTypeAssignment(
        code="SCAN_LINE_RESOLUTION",
        data_type="INTEGER",
        property_label="Scan line resolution [pixel]",
        description="""Number of pixels recorded for each scan line//Anzahl der Messpunkt einer Scanlinie""",
        mandatory=False,
        section="Scan Information",
    )


class VideoRecording(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.VIDEO_RECORDING",
        description="""An experimental step describing a video recording//Ein experimenteller Schritt zur Erzeugung einer Videoaufnahme""",
        generated_code_prefix="EXP.VID",
    )

    uuid = PropertyTypeAssignment(
        code="UUID",
        data_type="VARCHAR",
        property_label="UUID",
        description="""A Universally Unique IDentifier (UUID/GUID) according to RFC 4122//Ein Universally Unique IDentifier (UUID/GUID) nach RFC 4122""",
        mandatory=False,
        section="Identifiers",
    )

    image_horizontal_resolution = PropertyTypeAssignment(
        code="IMAGE_HORIZONTAL_RESOLUTION",
        data_type="INTEGER",
        property_label="Horizontal resolution [pixel]",
        description="""Horizontal resolution of the image [pixel]//Horizonzale Auflösung des Bildes [Pixel]""",
        mandatory=False,
        section="Video Information",
    )

    image_vertical_resolution = PropertyTypeAssignment(
        code="IMAGE_VERTICAL_RESOLUTION",
        data_type="INTEGER",
        property_label="Vertical resolution [pixel]",
        description="""Vertical resolution of the image [pixel]////Vertikale Auflösung des Bildes [Pixel]""",
        mandatory=False,
        section="Video Information",
    )

    video_frame_per_seconds = PropertyTypeAssignment(
        code="VIDEO_FRAME_PER_SECONDS",
        data_type="INTEGER",
        property_label="Average video framerate [frames per second]",
        description="""Average video framerate [frames per second]//Mittlere Bildrate (in Bilder pro Sekunde)""",
        mandatory=False,
        section="Video Information",
    )

    video_codec = PropertyTypeAssignment(
        code="VIDEO_CODEC",
        data_type="VARCHAR",
        property_label="Video codec used during recording",
        description="""Video codec used during recording (if applicable)//Videocodec (sofern kodiert)""",
        mandatory=False,
        section="Video Information",
    )

    video_dynamic_framerate = PropertyTypeAssignment(
        code="VIDEO_DYNAMIC_FRAMERATE",
        data_type="BOOLEAN",
        property_label="Dynamic video frame rate",
        description="""Flag to indicate that the video frame rate varies over time//Gibt an, dass die Bildrate des Videos nicht konstant ist""",
        mandatory=False,
        section="Video Information",
    )

    camera_shutter_mode = PropertyTypeAssignment(
        code="CAMERA_SHUTTER_MODE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CAMERA_SHUTTER_MODE",
        property_label="Shutter mode",
        description="""The shutter mode used for video recording//Belichtungsprinzip des Bildsensors""",
        mandatory=False,
        section="Video Information",
    )


class Ftir(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.FTIR",
        description="""Fourier-Transfom Infrared Spectroscopy//Fourier-Transfom Infrarotspektroskopie""",
        generated_code_prefix="EXP.FTIR",
    )

    ftir_instrument = PropertyTypeAssignment(
        code="FTIR.INSTRUMENT",
        data_type="VARCHAR",
        property_label="Instrument",
        description="""FT-IR Instrument//FT-IR Instrument""",
        mandatory=False,
        section="Meaurement Parameters",
    )

    ftir_start_wavenumber = PropertyTypeAssignment(
        code="FTIR.START_WAVENUMBER",
        data_type="REAL",
        property_label="Start Wavenumber [1/cm]",
        description="""Start Wavenumber [1/cm]//Start-Wellenzahl [1/cm]""",
        mandatory=False,
        section="Meaurement Parameters",
    )

    ftir_end_wavenumber = PropertyTypeAssignment(
        code="FTIR.END_WAVENUMBER",
        data_type="REAL",
        property_label="End Wavenumber [1/cm]",
        description="""End Wavenumber [1/cm]//End-Wellenzahl [1/cm]""",
        mandatory=False,
        section="Meaurement Parameters",
    )

    ftir_resolution = PropertyTypeAssignment(
        code="FTIR.RESOLUTION",
        data_type="INTEGER",
        property_label="Resolution [1/cm]",
        description="""Resolution [1/cm]//Auflösung [1/cm]""",
        mandatory=False,
        section="Meaurement Parameters",
    )

    ftir_scans = PropertyTypeAssignment(
        code="FTIR.SCANS",
        data_type="INTEGER",
        property_label="Number of Scans",
        description="""Number of FTIR Scans//Anzahl FTIR Scans""",
        mandatory=False,
        section="Meaurement Parameters",
    )

    ftir_accessory = PropertyTypeAssignment(
        code="FTIR.ACCESSORY",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="FTIR_ACCESSORIES",
        property_label="Accessory",
        description="""FTIR Accessory//FTIR Zubehör""",
        mandatory=False,
        section="Meaurement Parameters",
    )

    ftir_is_flushed = PropertyTypeAssignment(
        code="FTIR.IS_FLUSHED",
        data_type="BOOLEAN",
        property_label="Flushed with Nitrogen",
        description="""Flushed with Nitrogen//Gespült mit Sickstoff""",
        mandatory=False,
        section="Meaurement Parameters",
    )


class Sem(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.SEM",
        description="""Scanning Electron Microscopy//Rasterelektronenmikroskopie""",
        generated_code_prefix="EXP.SEM",
    )

    sem_instrument = PropertyTypeAssignment(
        code="SEM.INSTRUMENT",
        data_type="VARCHAR",
        property_label="Instrument",
        description="""SEM Instrument//SEM Instrument""",
        mandatory=False,
        section="Measurement Parameters",
    )

    sem_imagesizex = PropertyTypeAssignment(
        code="SEM.IMAGESIZEX",
        data_type="VARCHAR",
        property_label="Image Size X",
        description="""Image Size X//Bildgröße X""",
        mandatory=False,
        section="Measurement Parameters",
    )

    sem_imagesizey = PropertyTypeAssignment(
        code="SEM.IMAGESIZEY",
        data_type="VARCHAR",
        property_label="Image Size Y",
        description="""Image Size Y//Bildgröße Y""",
        mandatory=False,
        section="Measurement Parameters",
    )

    sem_operatingmode = PropertyTypeAssignment(
        code="SEM.OPERATINGMODE",
        data_type="VARCHAR",
        property_label="Operating Mode",
        description="""Operating Mode//Aufnahmemodus""",
        mandatory=False,
        section="Measurement Parameters",
    )

    sem_detector = PropertyTypeAssignment(
        code="SEM.DETECTOR",
        data_type="VARCHAR",
        property_label="Detector",
        description="""Detector//Detektor""",
        mandatory=False,
        section="Measurement Parameters",
    )

    sem_projectormode = PropertyTypeAssignment(
        code="SEM.PROJECTORMODE",
        data_type="VARCHAR",
        property_label="Projector Mode",
        description="""Projector Mode//Projektionsmodus""",
        mandatory=False,
        section="Measurement Parameters",
    )

    sem_pixelsizex = PropertyTypeAssignment(
        code="SEM.PIXELSIZEX",
        data_type="VARCHAR",
        property_label="Pixel Size X",
        description="""Pixel Size X//Pixelgröße X""",
        mandatory=False,
        section="Measurement Parameters",
    )

    sem_pixelsizey = PropertyTypeAssignment(
        code="SEM.PIXELSIZEY",
        data_type="VARCHAR",
        property_label="Pixel Size Y",
        description="""Pixel Size Y//Pixelgrße Y""",
        mandatory=False,
        section="Measurement Parameters",
    )

    sem_accelerationvoltage = PropertyTypeAssignment(
        code="SEM.ACCELERATIONVOLTAGE",
        data_type="VARCHAR",
        property_label="Acceleration Voltage [keV]",
        description="""Acceleration Voltage [keV]//Beschleunigungsspannung [keV]""",
        mandatory=False,
        section="Measurement Parameters",
    )

    sem_magnification = PropertyTypeAssignment(
        code="SEM.MAGNIFICATION",
        data_type="VARCHAR",
        property_label="Magnification",
        description="""Magnificaiton//Vergrößerung""",
        mandatory=False,
        section="Measurement Parameters",
    )

    sem_workingdistance = PropertyTypeAssignment(
        code="SEM.WORKINGDISTANCE",
        data_type="VARCHAR",
        property_label="Working Distance [mm]",
        description="""Working Distance [mm]//Arbeitsabstand [mm]""",
        mandatory=False,
        section="Measurement Parameters",
    )


class Nmr(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.NMR",
        description="""Nuclear Magnetic Resonance Spectroscopy//Kernspinresonanz-Spektroskopie""",
        generated_code_prefix="EXP.NMR",
    )

    nmr_instrument = PropertyTypeAssignment(
        code="NMR.INSTRUMENT",
        data_type="VARCHAR",
        property_label="Instrument",
        description="""NMR Instrument//NMR Instrument""",
        mandatory=False,
        section="Measurement Parameters",
    )

    nmr_nucleus_direct = PropertyTypeAssignment(
        code="NMR.NUCLEUS_DIRECT",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="NMR_NUCLEI",
        property_label="Nucleus (direct)",
        description="""Nucleus (direct)//Kern (direct)""",
        mandatory=False,
        section="Measurement Parameters",
    )

    nmr_nucleus_indirect = PropertyTypeAssignment(
        code="NMR.NUCLEUS_INDIRECT",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="NMR_NUCLEI",
        property_label="Nucleus (indirect, 2D only)",
        description="""Nucleus (indirect, 2D only)//Kern (indirekt, nur 2D)""",
        mandatory=False,
        section="Measurement Parameters",
    )

    nmr_solvent = PropertyTypeAssignment(
        code="NMR.SOLVENT",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="NMR_SOLVENTS",
        property_label="Solvent",
        description="""NMR Solvent//NMR Lösungsmittel""",
        mandatory=False,
        section="Measurement Parameters",
    )

    nmr_frequency = PropertyTypeAssignment(
        code="NMR.FREQUENCY",
        data_type="REAL",
        property_label="Frequency [MHz]",
        description="""NMR Frequency [MHz]//NMR Frequenz [MHz]""",
        mandatory=False,
        section="Measurement Parameters",
    )

    nmr_experiment = PropertyTypeAssignment(
        code="NMR.EXPERIMENT",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="NMR_EXPERIMENT_TYPES",
        property_label="Experiment",
        description="""NMR Experiment//NMR Experiment""",
        mandatory=False,
        section="Measurement Parameters",
    )

    nmr_scans = PropertyTypeAssignment(
        code="NMR.SCANS",
        data_type="INTEGER",
        property_label="Number of Scans",
        description="""Number of NMR Scans//Anzahl NMR Scans""",
        mandatory=False,
        section="Measurement Parameters",
    )

    nmr_start_chemical_shift = PropertyTypeAssignment(
        code="NMR.START_CHEMICAL_SHIFT",
        data_type="REAL",
        property_label="Start Chemical Shift [ppm]",
        description="""Start Chemical Shift [ppm]//Start Chemische Verschiebung [ppm]""",
        mandatory=False,
        section="Measurement Parameters",
    )

    nmr_end_chemical_shift = PropertyTypeAssignment(
        code="NMR.END_CHEMICAL_SHIFT",
        data_type="REAL",
        property_label="End Chemical Shift [ppm]",
        description="""End Chemical Shift [ppm]//Ende Chemische Verschiebung [ppm]""",
        mandatory=False,
        section="Measurement Parameters",
    )

    nmr_is_qnmr = PropertyTypeAssignment(
        code="NMR.IS_QNMR",
        data_type="BOOLEAN",
        property_label="Quantitative NMR",
        description="""Quantitative NMR//Quantitatives NMR""",
        mandatory=False,
        section="Measurement Parameters",
    )

    nmr_pulse_angle = PropertyTypeAssignment(
        code="NMR.PULSE_ANGLE",
        data_type="REAL",
        property_label="Pulse Angle [degree]",
        description="""Pulse Angle [degree]//Pulswinkel [degree]""",
        mandatory=False,
        section="Measurement Parameters",
    )

    nmr_interpulse_delay = PropertyTypeAssignment(
        code="NMR.INTERPULSE_DELAY",
        data_type="REAL",
        property_label="Interpulse Delay [s]",
        description="""Interpulse Delay [s]//Wartezeit zwischen Pulsen [s]""",
        mandatory=False,
        section="Measurement Parameters",
    )

    nmr_acquisition_time = PropertyTypeAssignment(
        code="NMR.ACQUISITION_TIME",
        data_type="REAL",
        property_label="Acquisition Time [s]",
        description="""Acquisition Time [s]//Akquisitionszeit [s]""",
        mandatory=False,
        section="Measurement Parameters",
    )


class Tem(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.TEM",
        description="""Transmission Electron Microscopy//Transmisisonselektronenmikroskopie""",
        generated_code_prefix="EXP.TEM",
    )

    tem_instrument = PropertyTypeAssignment(
        code="TEM.INSTRUMENT",
        data_type="VARCHAR",
        property_label="Instrument",
        description="""TEM Instrument//TEM Instrument""",
        mandatory=False,
        section="Measurement Parameters",
    )

    tem_imagesizex = PropertyTypeAssignment(
        code="TEM.IMAGESIZEX",
        data_type="VARCHAR",
        property_label="Image Size X",
        description="""Image Size X//Bildgröße X""",
        mandatory=False,
        section="Measurement Parameters",
    )

    tem_imagesizey = PropertyTypeAssignment(
        code="TEM.IMAGESIZEY",
        data_type="VARCHAR",
        property_label="Image Size Y",
        description="""Image Size Y//Bildgröße Y""",
        mandatory=False,
        section="Measurement Parameters",
    )

    tem_operatingmode = PropertyTypeAssignment(
        code="TEM.OPERATINGMODE",
        data_type="VARCHAR",
        property_label="Operating Mode",
        description="""Operating Mode//Aufnahmemodus""",
        mandatory=False,
        section="Measurement Parameters",
    )

    tem_detector = PropertyTypeAssignment(
        code="TEM.DETECTOR",
        data_type="VARCHAR",
        property_label="Detector",
        description="""Detector//Detektor""",
        mandatory=False,
        section="Measurement Parameters",
    )

    tem_projectormode = PropertyTypeAssignment(
        code="TEM.PROJECTORMODE",
        data_type="VARCHAR",
        property_label="Projector Mode",
        description="""Projector Mode//Projektionsmodus""",
        mandatory=False,
        section="Measurement Parameters",
    )

    tem_pixelsizex = PropertyTypeAssignment(
        code="TEM.PIXELSIZEX",
        data_type="VARCHAR",
        property_label="Pixel Size X",
        description="""Pixel Size X//Pixelgröße X""",
        mandatory=False,
        section="Measurement Parameters",
    )

    tem_pixelsizey = PropertyTypeAssignment(
        code="TEM.PIXELSIZEY",
        data_type="VARCHAR",
        property_label="Pixel Size Y",
        description="""Pixel Size Y//Pixelgrße Y""",
        mandatory=False,
        section="Measurement Parameters",
    )

    tem_accelerationvoltage = PropertyTypeAssignment(
        code="TEM.ACCELERATIONVOLTAGE",
        data_type="VARCHAR",
        property_label="Acceleration Voltage  [keV]",
        description="""Acceleration Voltage [keV]//Beschleunigungsspannung [keV]""",
        mandatory=False,
        section="Measurement Parameters",
    )

    tem_magnification = PropertyTypeAssignment(
        code="TEM.MAGNIFICATION",
        data_type="VARCHAR",
        property_label="Magnification",
        description="""Magnification//Vergrößerung""",
        mandatory=False,
        section="Measurement Parameters",
    )

    tem_cameralength = PropertyTypeAssignment(
        code="TEM.CAMERALENGTH",
        data_type="VARCHAR",
        property_label="Camera Length",
        description="""Camera Length//Kamera-Länge""",
        mandatory=False,
        section="Measurement Parameters",
    )

    tem_spot_index = PropertyTypeAssignment(
        code="TEM.SPOT_INDEX",
        data_type="VARCHAR",
        property_label="Spot Index",
        description="""Spot Index//Spot Index""",
        mandatory=False,
        section="Measurement Parameters",
    )

    tem_gun_lens_setting = PropertyTypeAssignment(
        code="TEM.GUN_LENS_SETTING",
        data_type="VARCHAR",
        property_label="Gun Lens Setting",
        description="""Gun Lens Setting//Einstellung der Elektronenquellenlinse""",
        mandatory=False,
        section="Measurement Parameters",
    )

    tem_c2_aperture_name = PropertyTypeAssignment(
        code="TEM.C2_APERTURE_NAME",
        data_type="VARCHAR",
        property_label="C2 Aperture",
        description="""C2 Aperture//C2 Apertur""",
        mandatory=False,
        section="Measurement Parameters",
    )

    tem_obj_aperture_name = PropertyTypeAssignment(
        code="TEM.OBJ_APERTURE_NAME",
        data_type="VARCHAR",
        property_label="Objective Aperture",
        description="""Objective Aperture//Objektiv Apertur""",
        mandatory=False,
        section="Measurement Parameters",
    )

    tem_saed_aperturediameter = PropertyTypeAssignment(
        code="TEM.SAED_APERTUREDIAMETER",
        data_type="VARCHAR",
        property_label="SAED Aperture Diameter",
        description="""SAED Aperture Diameter//SAED Apertur Durchmesser""",
        mandatory=False,
        section="Measurement Parameters",
    )

    tem_saed_apertureposx = PropertyTypeAssignment(
        code="TEM.SAED_APERTUREPOSX",
        data_type="VARCHAR",
        property_label="SAED Aperture Pos X",
        description="""SAED Aperture Pos X//SAED Apertur Position X""",
        mandatory=False,
        section="Measurement Parameters",
    )

    tem_saed_apertureposy = PropertyTypeAssignment(
        code="TEM.SAED_APERTUREPOSY",
        data_type="VARCHAR",
        property_label="SAED Aperture PosY",
        description="""SAED Aperture Pos Y//SAED Apertur Position Y""",
        mandatory=False,
        section="Measurement Parameters",
    )


class Dls(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.DLS",
        description="""Dynamic and electrophoretic light scattering//Dynamische und elektrophoretische Lichtstreuung""",
        generated_code_prefix="EXP.DLS",
    )

    dls_material = PropertyTypeAssignment(
        code="DLS.MATERIAL",
        data_type="VARCHAR",
        property_label="Material Name",
        description="""Material Name for DLS Measurement//Materialname für DLS Messung""",
        mandatory=False,
        section="Measurement Parameters",
    )

    dls_dispersant = PropertyTypeAssignment(
        code="DLS.DISPERSANT",
        data_type="VARCHAR",
        property_label="Dispersant",
        description="""Dispersant for DLS Measurement//Dispersant für DLS Messung""",
        mandatory=False,
        section="Measurement Parameters",
    )

    dls_temperature = PropertyTypeAssignment(
        code="DLS.TEMPERATURE",
        data_type="REAL",
        property_label="Temperature [°C]",
        description="""Temperature [°C]//Temperatur [°C]""",
        mandatory=False,
        section="Measurement Parameters",
    )

    dls_celldescription = PropertyTypeAssignment(
        code="DLS.CELLDESCRIPTION",
        data_type="VARCHAR",
        property_label="Cell Description",
        description="""DLS Cell Description//DLS Messküvette""",
        mandatory=False,
        section="Measurement Parameters",
    )

    dls_attenuator = PropertyTypeAssignment(
        code="DLS.ATTENUATOR",
        data_type="INTEGER",
        property_label="Attenuator",
        description="""Attenuator for DLS Measurement//Abschwächung für DLS Messung""",
        mandatory=False,
        section="Measurement Parameters",
    )

    dls_zavg = PropertyTypeAssignment(
        code="DLS.ZAVG",
        data_type="REAL",
        property_label="Z-Average",
        description="""Z-Average//Z-Durchschnitt""",
        mandatory=False,
        section="Measurement Results",
    )

    dls_pdi = PropertyTypeAssignment(
        code="DLS.PDI",
        data_type="REAL",
        property_label="PDI",
        description="""Polydispersity Index//Polydispersitätsindex""",
        mandatory=False,
        section="Measurement Results",
    )

    dls_zeta = PropertyTypeAssignment(
        code="DLS.ZETA",
        data_type="REAL",
        property_label="Zeta Potential [mV]",
        description="""Zeta Potential [mV]//Zeta Potential [mV]""",
        mandatory=False,
        section="Measurement Results",
    )

    dls_pk1int = PropertyTypeAssignment(
        code="DLS.PK1INT",
        data_type="REAL",
        property_label="Peak 1 (Intensity) [nm]",
        description="""Peak 1 (Intensity) [nm]//Peak 1 (Intensität) [nm]""",
        mandatory=False,
        section="Measurement Results (Intensity Distribution)",
    )

    dls_pk1intwidth = PropertyTypeAssignment(
        code="DLS.PK1INTWIDTH",
        data_type="REAL",
        property_label="Peak 1 Width (Intensity) [nm]",
        description="""Peak 1 Width (Intensity) [nm]//Peak 1 Breite (Intensität) [nm]""",
        mandatory=False,
        section="Measurement Results (Intensity Distribution)",
    )

    dls_pk1intpd = PropertyTypeAssignment(
        code="DLS.PK1INTPD",
        data_type="REAL",
        property_label="Peak 1 Polydispersity (Intensity)",
        description="""Peak 1 Polydispersity (Intensity)//Peak 1 Polydispersität (Intensität)""",
        mandatory=False,
        section="Measurement Results (Intensity Distribution)",
    )

    dls_pk2int = PropertyTypeAssignment(
        code="DLS.PK2INT",
        data_type="REAL",
        property_label="Peak 2 (Intensity) [nm]",
        description="""Peak 2 (Intensity) [nm]//Peak 2 (Intensität) [nm]""",
        mandatory=False,
        section="Measurement Results (Intensity Distribution)",
    )

    dls_pk2intwidth = PropertyTypeAssignment(
        code="DLS.PK2INTWIDTH",
        data_type="REAL",
        property_label="Peak 2 Width (Intensity) [nm]",
        description="""Peak 2 Width (Intensity) [nm]//Peak 2 Breite (Intensität) [nm]""",
        mandatory=False,
        section="Measurement Results (Intensity Distribution)",
    )

    dls_pk2intpd = PropertyTypeAssignment(
        code="DLS.PK2INTPD",
        data_type="REAL",
        property_label="Peak 2 Polydispersity (Intensity)",
        description="""Peak 2 Polydispersity (Intensity)//Peak 2 Polydispersität (Intensität)""",
        mandatory=False,
        section="Measurement Results (Intensity Distribution)",
    )

    dls_pk3int = PropertyTypeAssignment(
        code="DLS.PK3INT",
        data_type="REAL",
        property_label="Peak 3 (Intensity) [nm]",
        description="""Peak 3 (Intensity) [nm]//Peak 3 (Intensität) [nm]""",
        mandatory=False,
        section="Measurement Results (Intensity Distribution)",
    )

    dls_pk3intwidth = PropertyTypeAssignment(
        code="DLS.PK3INTWIDTH",
        data_type="REAL",
        property_label="Peak 3 Width (Intensity) [nm]",
        description="""Peak 3 Width (Intensity) [nm]//Peak 3 Breite (Intensität) [nm]""",
        mandatory=False,
        section="Measurement Results (Intensity Distribution)",
    )

    dls_pk3intpd = PropertyTypeAssignment(
        code="DLS.PK3INTPD",
        data_type="REAL",
        property_label="Peak 3 Polydispersity (Intensity)",
        description="""Peak 3 Polydispersity (Intensity)//Peak 3 Polydispersität (Intensität)""",
        mandatory=False,
        section="Measurement Results (Intensity Distribution)",
    )

    dls_pk1vol = PropertyTypeAssignment(
        code="DLS.PK1VOL",
        data_type="REAL",
        property_label="Peak 1 (Volume) [nm]",
        description="""Peak 1 (Volume) [nm]//Peak 1 (Volumen) [nm]""",
        mandatory=False,
        section="Measurement Results (Volume Distribution)",
    )

    dls_pk1volwidth = PropertyTypeAssignment(
        code="DLS.PK1VOLWIDTH",
        data_type="REAL",
        property_label="Peak 1 Width (Volume) [nm]",
        description="""Peak 1 Width (Volume) [nm]//Peak 1 Breite (Volumen) [nm]""",
        mandatory=False,
        section="Measurement Results (Volume Distribution)",
    )

    dls_pk1volpd = PropertyTypeAssignment(
        code="DLS.PK1VOLPD",
        data_type="REAL",
        property_label="Peak 1 Polydispersity (Volume)",
        description="""Peak 1 Polydispersity (Volume)//Peak 1 Polydispersität (Volumen)""",
        mandatory=False,
        section="Measurement Results (Volume Distribution)",
    )

    dls_pk2vol = PropertyTypeAssignment(
        code="DLS.PK2VOL",
        data_type="REAL",
        property_label="Peak 2 (Volume) [nm]",
        description="""Peak 2 (Volume) [nm]//Peak 2 (Volumen) [nm]""",
        mandatory=False,
        section="Measurement Results (Volume Distribution)",
    )

    dls_pk2volwidth = PropertyTypeAssignment(
        code="DLS.PK2VOLWIDTH",
        data_type="REAL",
        property_label="Peak 2 Width (Volume) [nm]",
        description="""Peak 2 Width (Volume) [nm]//Peak 2 Breite (Volumen) [nm]""",
        mandatory=False,
        section="Measurement Results (Volume Distribution)",
    )

    dls_pk2volpd = PropertyTypeAssignment(
        code="DLS.PK2VOLPD",
        data_type="REAL",
        property_label="Peak 2 Polydispersity (Volume)",
        description="""Peak 2 Polydispersity (Volume)//Peak 2 Polydispersität (Volumen)""",
        mandatory=False,
        section="Measurement Results (Volume Distribution)",
    )

    dls_pk3vol = PropertyTypeAssignment(
        code="DLS.PK3VOL",
        data_type="REAL",
        property_label="Peak 3 (Volume) [nm]",
        description="""Peak 3 (Volume) [nm]//Peak 3 (Volumen) [nm]""",
        mandatory=False,
        section="Measurement Results (Volume Distribution)",
    )

    dls_pk3volwidth = PropertyTypeAssignment(
        code="DLS.PK3VOLWIDTH",
        data_type="REAL",
        property_label="Peak 3 Width (Volume) [nm]",
        description="""Peak 3 Width (Volume) [nm]//Peak 3 Breite (Volumen) [nm]""",
        mandatory=False,
        section="Measurement Results (Volume Distribution)",
    )

    dls_pk3volpd = PropertyTypeAssignment(
        code="DLS.PK3VOLPD",
        data_type="REAL",
        property_label="Peak 3 Polydispersity (Volume)",
        description="""Peak 3 Polydispersity (Volume)//Peak 3 Polydispersität (Volumen)""",
        mandatory=False,
        section="Measurement Results (Volume Distribution)",
    )

    dls_pk1num = PropertyTypeAssignment(
        code="DLS.PK1NUM",
        data_type="REAL",
        property_label="Peak 1 (Number) [nm]",
        description="""Peak 1 (Number) [nm]//Peak 1 (Anzahl) [nm]""",
        mandatory=False,
        section="Measurement Results (Number Distribution)",
    )

    dls_pk1numwidth = PropertyTypeAssignment(
        code="DLS.PK1NUMWIDTH",
        data_type="REAL",
        property_label="Peak 1 Width (Number) [nm]",
        description="""Peak 1 Width (Number) [nm]//Peak 1 Breite (Anzahl) [nm]""",
        mandatory=False,
        section="Measurement Results (Number Distribution)",
    )

    dls_pk1numpd = PropertyTypeAssignment(
        code="DLS.PK1NUMPD",
        data_type="REAL",
        property_label="Peak 1 Polydispersity (Number)",
        description="""Peak 1 Polydispersity (Number)//Peak 1 Polydispersität (Anzahl)""",
        mandatory=False,
        section="Measurement Results (Number Distribution)",
    )

    dls_pk2num = PropertyTypeAssignment(
        code="DLS.PK2NUM",
        data_type="REAL",
        property_label="Peak 2 (Number) [nm]",
        description="""Peak 2 (Number) [nm]//Peak 2 (Anzahl) [nm]""",
        mandatory=False,
        section="Measurement Results (Number Distribution)",
    )

    dls_pk2numwidth = PropertyTypeAssignment(
        code="DLS.PK2NUMWIDTH",
        data_type="REAL",
        property_label="Peak 2 Width (Number) [nm]",
        description="""Peak 2 Width (Number) [nm]//Peak 2 Breite (Anzahl) [nm]""",
        mandatory=False,
        section="Measurement Results (Number Distribution)",
    )

    dls_pk2numpd = PropertyTypeAssignment(
        code="DLS.PK2NUMPD",
        data_type="REAL",
        property_label="Peak 2 Polydispersity (Number)",
        description="""Peak 2 Polydispersity (Number)//Peak 2 Polydispersität (Anzahl)""",
        mandatory=False,
        section="Measurement Results (Number Distribution)",
    )

    dls_pk3num = PropertyTypeAssignment(
        code="DLS.PK3NUM",
        data_type="REAL",
        property_label="Peak 3 (Number) [nm]",
        description="""Peak 3 (Number) [nm]//Peak 3 (Anzahl) [nm]""",
        mandatory=False,
        section="Measurement Results (Number Distribution)",
    )

    dls_pk3numwidth = PropertyTypeAssignment(
        code="DLS.PK3NUMWIDTH",
        data_type="REAL",
        property_label="Peak 3 Width (Number) [nm]",
        description="""Peak 3 Width (Number) [nm]//Peak 3 Breite (Anzahl) [nm]""",
        mandatory=False,
        section="Measurement Results (Number Distribution)",
    )

    dls_pk3numpd = PropertyTypeAssignment(
        code="DLS.PK3NUMPD",
        data_type="REAL",
        property_label="Peak 3 Polydispersity (Number)",
        description="""Peak 3 Polydispersity (Number)//Peak 3 Polydispersität (Anzahl)""",
        mandatory=False,
        section="Measurement Results (Number Distribution)",
    )

    dls_pk1zeta = PropertyTypeAssignment(
        code="DLS.PK1ZETA",
        data_type="REAL",
        property_label="Peak 1 (Zeta) [mV]",
        description="""Peak 1 (Zetapotential) [mV]//Peak 1 (Zetapotential) [mV]""",
        mandatory=False,
        section="Measurement Results (Zeta Potential)",
    )

    dls_pk1zetawidth = PropertyTypeAssignment(
        code="DLS.PK1ZETAWIDTH",
        data_type="REAL",
        property_label="Peak 1 Width (Zeta) [mV]",
        description="""Peak 1 Width (Zetapotential) [mV]//Peak 1 Breite (Zetapotential) [mV]""",
        mandatory=False,
        section="Measurement Results (Zeta Potential)",
    )

    dls_pk2zeta = PropertyTypeAssignment(
        code="DLS.PK2ZETA",
        data_type="REAL",
        property_label="Peak 2 (Zeta) [mV]",
        description="""Peak 2 (Zetapotential) [mV]//Peak 2 (Zetapotential) [mV]""",
        mandatory=False,
        section="Measurement Results (Zeta Potential)",
    )

    dls_pk2zetawidth = PropertyTypeAssignment(
        code="DLS.PK2ZETAWIDTH",
        data_type="REAL",
        property_label="Peak 2 Width (Zeta) [mV]",
        description="""Peak 2 Width (Zetapotential) [mV]//Peak 2 Breite (Zetapotential) [mV]""",
        mandatory=False,
        section="Measurement Results (Zeta Potential)",
    )

    dls_pk3zeta = PropertyTypeAssignment(
        code="DLS.PK3ZETA",
        data_type="REAL",
        property_label="Peak 3 (Zeta) [mV]",
        description="""Peak 3 (Zetapotential) [mV]//Peak 3 (Zetapotential) [mV]""",
        mandatory=False,
        section="Measurement Results (Zeta Potential)",
    )

    dls_pk3zetawidth = PropertyTypeAssignment(
        code="DLS.PK3ZETAWIDTH",
        data_type="REAL",
        property_label="Peak 3 Width (Zeta) [mV]",
        description="""Peak 3 Width (Zetapotential) [mV]//Peak 3 Breite (Zetapotential) [mV]""",
        mandatory=False,
        section="Measurement Results (Zeta Potential)",
    )

    dls_analysismodel = PropertyTypeAssignment(
        code="DLS.ANALYSISMODEL",
        data_type="VARCHAR",
        property_label="Analysis Model",
        description="""Analysis Model//Analysemodell""",
        mandatory=False,
        section="Measurement Information",
    )

    dls_intercept = PropertyTypeAssignment(
        code="DLS.INTERCEPT",
        data_type="REAL",
        property_label="Measured Intercept",
        description="""Measured Intercept//Achsenabschnitt""",
        mandatory=False,
        section="Measurement Information",
    )

    dls_sizemerit = PropertyTypeAssignment(
        code="DLS.SIZEMERIT",
        data_type="REAL",
        property_label="Size Merit",
        description="""Size Merit//Güte""",
        mandatory=False,
        section="Measurement Information",
    )

    dls_cumulantsfiterror = PropertyTypeAssignment(
        code="DLS.CUMULANTSFITERROR",
        data_type="REAL",
        property_label="Cumulants Fit Error",
        description="""Cumulants Fit Error//Fehler des Kummulanten-Fits""",
        mandatory=False,
        section="Measurement Information",
    )

    dls_multimodalfiterror = PropertyTypeAssignment(
        code="DLS.MULTIMODALFITERROR",
        data_type="REAL",
        property_label="Multimodal Fit Error",
        description="""Multimodal Fit Error//Fehler des multimodalen Fits""",
        mandatory=False,
        section="Measurement Information",
    )

    dls_fkamodel = PropertyTypeAssignment(
        code="DLS.FKAMODEL",
        data_type="VARCHAR",
        property_label="Fka Model",
        description="""Fka Model//Fka Modell""",
        mandatory=False,
        section="Measurement Information",
    )

    dls_volt = PropertyTypeAssignment(
        code="DLS.VOLT",
        data_type="REAL",
        property_label="Measured Voltage [V]",
        description="""Measured Voltage [V]//Gemessene Spannung [V]""",
        mandatory=False,
        section="Measurement Information",
    )

    dls_cond = PropertyTypeAssignment(
        code="DLS.COND",
        data_type="REAL",
        property_label="Conductivity [mS/cm]",
        description="""Conductivity [mS/cm]//Leitfähigkeit [mS/cm]""",
        mandatory=False,
        section="Measurement Information",
    )


class MsBatch(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MS_BATCH",
        description="""MS sample batch with attached raw data//MS Proben-Batch mit verknüpften Rohdaten""",
        generated_code_prefix="EXP.MSB",
    )

    ms_ionization_mode = PropertyTypeAssignment(
        code="MS_IONIZATION_MODE",
        data_type="VARCHAR",
        property_label="Ionization mode",
        description="""Ionization mode (pos/neg)//Ionisierung (pos/neg)""",
        mandatory=False,
        section="MS Information",
    )

    ms_hyphenation_method = PropertyTypeAssignment(
        code="MS_HYPHENATION_METHOD",
        data_type="VARCHAR",
        property_label="Hyphenation method",
        description="""Hyphenation (DI, LC, GC, CE)//Probeninjektion (DI, LC, GC, CE)""",
        mandatory=False,
        section="MS Information",
    )


class RmEthanol(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.RM_ETHANOL",
        description="""Experimental Step to generate a reference material Ethanol//Experimenteller Schritt zur Generierung eines Referenzmaterials Ethanol""",
        generated_code_prefix="EXP.ETHANOL",
    )

    purity_in_percentage = PropertyTypeAssignment(
        code="PURITY_IN_PERCENTAGE",
        data_type="REAL",
        property_label="Purity",
        description="""Purity of the substance [ %]// Reinheit der Substanz""",
        mandatory=False,
        section="General Information",
    )

    conductivity_in_ms = PropertyTypeAssignment(
        code="CONDUCTIVITY_IN_MS",
        data_type="REAL",
        property_label="Conductivity",
        description="""Conductivity in mili Siemens (mS)//Leitfähigkeit in Millisiemens (mS)""",
        mandatory=False,
        section="General Information",
    )


class ThermographicMeasurement(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.THERMOGRAPHIC_MEASUREMENT",
        description="""Thermographic Measurement//Thermografiemessung""",
        generated_code_prefix="EXP_STEP.THE_MEA",
    )

    associated_project = PropertyTypeAssignment(
        code="ASSOCIATED_PROJECT",
        data_type="OBJECT",
        object_code="PROJECT",
        property_label="Associated project",
        description="""Associated project//Assoziiertes Projekt""",
        mandatory=False,
        section="References",
    )


class SaxsMeasurement(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.SAXS_MEASUREMENT",
        description="""Metadata of a single Small-Angle Scattering (SAXS) measurement//Metadaten einer einzelnen Kleinwinkelstreuungmessung""",
        generated_code_prefix="EXP.SXSM_",
    )

    measurement_id = PropertyTypeAssignment(
        code="MEASUREMENT_ID",
        data_type="INTEGER",
        property_label="Measurement ID",
        description="""Div. internal measurement ID//FB-interne Messdatennummer""",
        mandatory=False,
        section="Experiment Details",
    )

    measurement_date = PropertyTypeAssignment(
        code="MEASUREMENT_DATE",
        data_type="DATE",
        property_label="Measurement Date",
        description="""Measurement Date//Messdatum""",
        mandatory=True,
        section="Experiment Details",
    )

    cell_temperature_in_celsius = PropertyTypeAssignment(
        code="CELL_TEMPERATURE_IN_CELSIUS",
        data_type="REAL",
        property_label="Cell Temperature [°C]",
        description="""Measurement cell temperature in °C // Temperatur der Messzelle in °C""",
        mandatory=True,
        section="Experiment Details",
    )

    exposure_time_in_seconds = PropertyTypeAssignment(
        code="EXPOSURE_TIME_IN_SECONDS",
        data_type="REAL",
        property_label="Exposure time [s]",
        description="""Exposure time in seconds//Belichtungszeit in Sekunden""",
        mandatory=True,
        section="Experiment Details",
    )

    frame_count = PropertyTypeAssignment(
        code="FRAME_COUNT",
        data_type="INTEGER",
        property_label="Number of frames",
        description="""Number of frames//Anzahl von Aufnahmen""",
        mandatory=True,
        section="Experiment Details",
    )


class MeasurementSession(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MEASUREMENT_SESSION",
        description="""Metadata for a group of measurements from a measurement series or session//Metadaten für eine Gruppe von Messungen aus einer Messreihe oder Sitzung""",
        generated_code_prefix="EXP.MSES_",
    )

    responsible_person = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Responsible person",
        description="""Responsible person//Verantwortliche Person""",
        mandatory=False,
        section="General Information",
    )

    bam_partner = PropertyTypeAssignment(
        code="BAM_PARTNER",
        data_type="VARCHAR",
        property_label="BAM Partner",
        description="""BAM Partner(s)//BAM Partner""",
        mandatory=False,
        section="General Information",
    )


class LaserDiffPSDMeasurement(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.LASER_DIFF_PSD_MEASUREMENT",
        description="""Measurement of particle size distribution (PSD) by laser diffraction method // Messung einer Partikelgrößenverteilung mit einem Laserbeugungsverfahren""",
        auto_generate_codes=True,
        generated_code_prefix="EXP.LAS_DIFF_PSD_MEAS",
    )

    # TODO check if these 3 properties (sample_id, measurement_id, operator) can be moved to a common parent class
    sample_id = PropertyTypeAssignment(
        code="SAMPLE_ID",
        data_type="VARCHAR",
        property_label="Sample ID",
        description="""Sample ID//Identifikationsnummer""",
        mandatory=False,
        section="General Information",
    )

    measurement_id = PropertyTypeAssignment(
        code="MEASUREMENT_ID",
        data_type="INTEGER",
        property_label="Measurement ID",
        description="""Div. internal measurement ID//FB-interne Messdatennummer""",
        mandatory=False,
        section="General Information",
    )

    # TODO check this property: this refers to the DATA_CREATOR during an activity/experimental step
    # TODO it can be a BAM user, an external, or any person. We should have the possibility of creating a list of PERSON in the inventory besides BAM.PERSON
    operator = PropertyTypeAssignment(
        code="OPERATOR",
        data_type="VARCHAR",
        property_label="Operator",
        description="""Name of the person or user performing the measurement//Name der Person oder des Benutzers, der die Messung durchführt""",
        mandatory=True,
        section="General Information",
    )

    dispersing_medium = PropertyTypeAssignment(
        code="DISPERSING_MEDIUM",
        data_type="VARCHAR",
        property_label="Dispersing medium",
        description="""Medium in which the particles are dispersed for the measurement. Could be a liquid solvent (water, ethanol) or air. If the solvent contains additional dispersing agent, the respective type and concentration can also be stored in this field.//Medium, in dem die Partikel für die Messung dispergiert werden. Dies kann ein flüssiges Lösungsmittel (Wasser, Ethanol) oder Luft sein. Enthält das Lösungsmittel ein zusätzliches Dispergiermittel, können dessen Art und Konzentration ebenfalls in diesem Feld gespeichert werden.""",
        mandatory=True,
        section="Experimental Details",
    )

    scattering_model_psd_ld = PropertyTypeAssignment(
        code="SCATTERING_MODEL_PSD_LD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="SCATTERING_MODEL_PSD_LD",
        property_label="Light scattering model",
        description="""Light scattering model for the analysis of particle size by laser diffraction methods according to ISO 13220. Could be Mie or Fraunhofer, depending on the actual particle size.//Lichtstreuungsmodell zur Analyse der Partikelgröße mittels Laserbeugungsmethoden gemäß ISO 13220. Je nach tatsächlicher Partikelgröße kann es sich um das Mie- oder das Fraunhofer-Modell handeln.""",
        mandatory=True,
        section="Experimental Details",
    )

    name_optical_parameterset_sample = PropertyTypeAssignment(
        code="NAME_OPTICAL_PARAMETERSET_SAMPLE",
        data_type="VARCHAR",
        property_label="Optical parameters designation",
        description="""Designation of the dataset of optical parameters of the sample//Bezeichnung des Datensatzes der optischen Parameter der Probe""",
        mandatory=False,
        section="Experimental Details",
    )

    refractive_index_sample = PropertyTypeAssignment(
        code="REFRACTIVE_INDEX_SAMPLE",
        data_type="REAL",
        property_label="Refractive index of sample",
        description="""Refractive index of the sample//Brechungsindex der Probe""",
        mandatory=False,
        section="Experimental Details",
    )

    absorption_coeff_sample = PropertyTypeAssignment(
        code="ABSORPTION_COEFF_SAMPLE",
        data_type="REAL",
        property_label="Absorption coefficient of sample",
        description="""Absorption coefficient of the sample for blue light, if the measuring device has such a second light source//Absorptionskoeffizient der Probe für blaues Licht, wenn das Messgerät eine derartige zweite Lichtquelle aufweist""",
        mandatory=False,
        section="Experimental Details",
    )

    refractive_index_blue_sample = PropertyTypeAssignment(
        code="REFRACTIVE_INDEX_BLUE_SAMPLE",
        data_type="REAL",
        property_label="Refractive index for blue light of sample",
        description="""Refractive index of the sample for blue light, if the measuring device has such a second light source//Brechungsindex der Probe für blaues Licht, wenn das Messgerät eine derartige zweite Lichtquelle aufweist""",
        mandatory=False,
        section="Experimental Details",
    )

    absorption_coeff_blue_sample = PropertyTypeAssignment(
        code="ABSORPTION_COEFF_BLUE_SAMPLE",
        data_type="REAL",
        property_label="Absorption coefficient for blue light of sample",
        description="""Absorption coefficient of the sample for blue light//Absorptionskoeffizient der Probe für blaues Licht""",
        mandatory=False,
        section="Experimental Details",
    )

    laser_obscuration = PropertyTypeAssignment(
        code="LASER_OBSCURATION",
        data_type="REAL",
        property_label="Laser obscuration",
        description="""Laser obscuration//Laserabschattung""",
        mandatory=False,
        section="Results",
    )

    laser_transmission = PropertyTypeAssignment(
        code="LASER_TRANSMISSION",
        data_type="REAL",
        property_label="Laser transmission",
        description="""Laser transmission//Transmission des Lasers""",
        mandatory=False,
        section="Results",
    )

    weighted_deviation = PropertyTypeAssignment(
        code="WEIGHTED_DEVIATION",
        data_type="REAL",
        property_label="Weighted deviation of fit",
        description="""In the context of fitted data, the weighted deviation describes how much the individual measurement points deviate from the curve predicted by the model, taking into account their respective weights (e.g. uncertainties or relevance).//Im Zusammenhang mit gefitteten Daten beschreibt die gewichtete Abweichung, wie stark die einzelnen Messpunkte von der durch das Modell vorhergesagten Kurve abweichen - unter Berücksichtigung ihrer jeweiligen Gewichte (z.B. Unsicherheiten oder Relevanz).""",
        mandatory=False,
        section="Results",
    )

    absolute_deviation = PropertyTypeAssignment(
        code="ABSOLUTE_DEVIATION",
        data_type="REAL",
        property_label="Absolute deviation of fit",
        description="""The absolute deviation for fitted data describes the sum (or mean value) of the differences in magnitude between the measured values and the values predicted by the model without squaring and without weighting.//Die absolute Abweichung bei gefitteten Daten beschreibt die Summe (oder den Mittelwert) der betragsmäßigen Unterschiede zwischen den gemessenen Werten und den durch das Modell vorhergesagten Werten ohne Quadrieren und ohne Gewichtung.""",
        mandatory=False,
        section="Results",
    )

    meas_medium_temperature_in_celsius = PropertyTypeAssignment(
        code="MEAS_MEDIUM_TEMPERATURE_IN_CELSIUS",
        data_type="REAL",
        property_label="Temperature of dispersing medium [°C]",
        description="""Temperature of measurement medium in °C//Temperatur des Messmediums in °C""",
        mandatory=False,
        section="Results",
    )

    d_10_in_micrometers = PropertyTypeAssignment(
        code="D_10_IN_MICROMETERS",
        data_type="REAL",
        property_label="Particle size D_10 [µm]",
        description="""Particle size D_10 in µm//Partikelgröße D_10 in µm""",
        mandatory=False,
        section="Results",
    )

    d_50_in_micrometers = PropertyTypeAssignment(
        code="D_50_IN_MICROMETERS",
        data_type="REAL",
        property_label="Particle size D_50 [µm]",
        description="""Particle size D_50 in µm//Partikelgröße D_50 in µm""",
        mandatory=True,
        section="Results",
    )

    d_90_in_micrometers = PropertyTypeAssignment(
        code="D_90_IN_MICROMETERS",
        data_type="REAL",
        property_label="Particle size D_90 [µm]",
        description="""Particle size D_90 in µm//Partikelgröße D_90 in µm""",
        mandatory=False,
        section="Results",
    )

    mode_count = PropertyTypeAssignment(
        code="MODE_COUNT",
        data_type="INTEGER",
        property_label="Number of modes",
        description="""Number of modes//Anzahl der Modalwerte""",
        mandatory=False,
        section="Results",
    )


class PowderXRDMeasurement(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.PXRD_MEASUREMENT",
        description="""Measurement of powder X-ray diffraction (PXRD) pattern//Messung eines Pulverröntgendiffraktogramms""",
        auto_generate_codes=True,
        generated_code_prefix="EXP.PXRD_MEAS",
    )

    # TODO check if adding `radiation_type` (e.g. Cu Kα, Co Kα), `detector_type` (e.g. LynxEye, SSD160)

    time_per_step = PropertyTypeAssignment(
        code="TIME_PER_STEP",
        data_type="REAL",
        property_label="Time per step",
        units="s",
        description="""Time per step in seconds//Zeit pro Schritt in Sekunden""",
        mandatory=False,
        section="Experimental Details",
    )

    rotation_speed = PropertyTypeAssignment(
        code="ROTATION_SPEED",
        data_type="REAL",
        property_label="Rotation speed",
        units="rpm",
        description="""Sample rotation speed in revolutions per minute (rpm)//Rotationsgeschwindigkeit der Probe in Umdrehungen pro Minute (rpm)""",
        mandatory=False,
        section="Experimental Details",
    )

    voltage = PropertyTypeAssignment(
        code="VOLTAGE",
        data_type="REAL",
        property_label="Voltage",
        units="kV",
        description="""Acceleration voltage of the X-ray tube in kilovolts (kV)//Beschleunigungsspannung der Röntgenröhre in Kilovolt (kV)""",
        mandatory=False,
        section="Experimental Details",
    )

    current = PropertyTypeAssignment(
        code="CURRENT",
        data_type="REAL",
        property_label="Current",
        units="mA",
        description="""Tube current of the X-ray source in milliamperes (mA)//Röhrenstrom der Röntgenquelle in Milliampere (mA)""",
        mandatory=False,
        section="Experimental Details",
    )

    tube_material = PropertyTypeAssignment(
        code="TUBE_MATERIAL",
        data_type="VARCHAR",
        vocabulary_code="TUBE_MATERIAL",
        property_label="X-ray tube material",
        description="""Material of the X-ray tube anode (e.g. Cu, Co, Mo)//Material der Anode der Röntgenröhre (z.B. Cu, Co, Mo)""",
        mandatory=False,
        section="Experimental Details",
    )

    xray_wavelength = PropertyTypeAssignment(
        code="XRAY_WAVELENGTH",
        data_type="REAL",
        property_label="X-ray wavelength",
        units="angstrom",
        description="""Wavelength of the X-ray radiation in Angstrom (Å). This wavelength is associated
        with the tube, and it can refer to alpha 1 or to the average depending on the tube configuration//Wellenlänge
        der Röntgenstrahlung in Angstrom (Å). Diese Wellenlänge ist mit der Röhre verbunden und kann sich je nach
        Röhrenkonfiguration auf alpha 1 oder den Durchschnitt beziehen""",
        mandatory=False,
        section="Experimental Details",
    )

    tube_configuration_name = PropertyTypeAssignment(
        code="TUBE_CONFIGURATION_NAME",
        data_type="VARCHAR",
        property_label="X-ray tube configuration",
        description="""Instrument-specific X-ray tube configuration identifier//Gerätespezifischer Konfigurationsbezeichner der Röntgenröhre""",
        mandatory=False,
        section="Experimental Details",
    )

    goniometer_type = PropertyTypeAssignment(
        code="GONIOMETER_TYPE",
        data_type="VARCHAR",
        property_label="Goniometer type",
        description="""Type of goniometer used for the measurement//Typ des für die Messung verwendeten Goniometers""",
        mandatory=False,
        section="Experimental Details",
    )

    start_2theta = PropertyTypeAssignment(
        code="START_2THETA",
        data_type="REAL",
        property_label="Start 2Theta",
        units="degree",
        description="""Starting angle of the 2Theta range in degrees//Startwinkel des 2Theta-Bereichs in Grad""",
        mandatory=False,
        section="Experimental Details",
    )

    end_2theta = PropertyTypeAssignment(
        code="END_2THETA",
        data_type="REAL",
        property_label="End 2Theta",
        units="degree",
        description="""Ending angle of the 2Theta range in degrees//Endwinkel des 2Theta-Bereichs in Grad""",
        mandatory=False,
        section="Experimental Details",
    )

    step_size_2theta = PropertyTypeAssignment(
        code="STEP_SIZE_2THETA",
        data_type="REAL",
        property_label="Step size 2Theta",
        units="degree",
        description="""Step size of the 2Theta range in degrees//Schrittgröße des 2Theta-Bereichs in Grad""",
        mandatory=False,
        section="Experimental Details",
    )


# Hidden inherited properties: EXPERIMENTAL_DESCRIPTION, EXPERIMENTAL_RESULTS,
#   EXPERIMENTAL_GOALS, SPREADSHEET, REFERENCE, PUBLICATION, COMMENTS
class MouseMeasurement(SaxsMeasurement):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.SAXS_MEASUREMENT.MOUSE_MEASUREMENT",
        description="""Metadata of SAXS measurements of sample at MOUSE // Metadaten der SAXS-Messungen einer Probe mit MOUSE""",
        generated_code_prefix="EXP.MOME_",
    )

    responsible_person = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Responsible person",
        description="""Responsible person//Verantwortliche Person""",
        mandatory=False,
        section="General Information",
    )

    sample_position = PropertyTypeAssignment(
        code="SAMPLE_POSITION",
        data_type="VARCHAR",
        property_label="Sample Position // Position der Probe",
        description="""The sample position ID in the sample holder. Used to record the spatial/orientational position of the sample within the holder or setup. Different sample holders might get new names, or one-off sample holders might have a temporary ID.//Die Position der Probe (ID) im Probenhalter. Sie dient zur Erfassung der räumlichen/orientierungsmäßigen Position der Probe innerhalb des Halters oder der Versuchsanordnung. Verschiedene Probenhalter können unterschiedliche Namen erhalten, oder einmalige Probenhalter können eine temporäre ID haben.""",
        mandatory=False,
        section="Experiment Details",
    )

    measurement_protocol_file = PropertyTypeAssignment(
        code="MEASUREMENT_PROTOCOL_FILE",
        data_type="MULTILINE_VARCHAR",
        property_label="Measurement Protocol // Messprotokoll",
        description="""Location of the measurement script // Ort des Messprotokollskripts""",
        mandatory=False,
        section="Experiment Details",
    )

    # TODO revisit this property when JSON is integrated in openBIS
    measurement_protocol_options = PropertyTypeAssignment(
        code="MEASUREMENT_PROTOCOL_OPTIONS",
        data_type="VARCHAR",
        property_label="Measurement protocol options // Messprotokolloptionen",
        description="""JSON with key-value combinations // JSON mit Schlüssel-Werte-Paaren""",
        mandatory=False,
        section="Experiment Details",
    )

    size_thickness_in_millimeter = PropertyTypeAssignment(
        code="SIZE_THICKNESS_IN_MILLIMETER",
        data_type="REAL",
        property_label="Thickness [mm]",
        description="""Thickness in mm//Dicke in mm""",
        mandatory=False,
        section="Data Processing",
    )

    processing_protocol_file = PropertyTypeAssignment(
        code="PROCESSING_PROTOCOL_FILE",
        data_type="MULTILINE_VARCHAR",
        property_label="Data processing protocol // Datenverarbeitungsprotokoll",
        description="""Location of the data processing protocol // Ort des Datenverarbeitungsprotokolls""",
        mandatory=False,
        section="Data Processing",
    )
