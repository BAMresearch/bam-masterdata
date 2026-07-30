from bam_masterdata.datamodel.activities import ExperimentalStep
from bam_masterdata.datamodel.object_types import Instrument
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment


class MsBatch(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MS_BATCH",
        description="""MS sample batch with attached raw data//MS Proben-Batch mit verknüpften Rohdaten""",
        generated_code_prefix="EXP.MSB",
    )

    ms_resolution = PropertyTypeAssignment(
        code="MS_RESOLUTION",
        data_type="REAL",
        property_label="Resolution",
        description="""Approximate mass resolving power (m/Δm). Indicates the ability to separate two closely spaced m/z peaks; higher values mean better peak separation. Resolution depends on instrument type and measured mass.//Ungefähres Massenauflösungsvermögen (m/Δm). Beschreibt die Fähigkeit, zwei nahe beieinander liegende m/z-Peaks zu trennen; höhere Werte bedeuten eine bessere Peak-Trennung. Die Auflösung hängt vom Instrumententyp und der gemessenen Masse ab.""",
        mandatory=False,
        section="MS Parameters",
    )

    # TODO change to REAL + multivalued when implemented in openBIS 7
    ms_intensity_range = PropertyTypeAssignment(
        code="MS_INTENSITY_RANGE",
        data_type="VARCHAR",
        property_label="Intensity range",
        description="""Ion intensity range in [min-max]//Ionen-Intensitätsbereich in [min-max]""",
        mandatory=False,
        section="MS Parameters",
    )

    ms_scan_rate = PropertyTypeAssignment(
        code="MS_SCAN_RATE",
        data_type="REAL",
        property_label="Scan rate",
        description="""Sample scan rate in [Hz]//Sample Scan-Rate in [Hz]""",
        mandatory=False,
        section="MS Parameters",
        units="Hz",
    )

    ms_acquisition_mode = PropertyTypeAssignment(
        code="MS_ACQUISITION_MODE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="MS_ACQUISITION_MODE",
        property_label="Aquisition mode",
        description="""Aquisition mode//Aufnahme-Modus""",
        mandatory=False,
        section="MS Parameters",
    )

    ms_ion_polarity = PropertyTypeAssignment(
        code="MS_ION_POLARITY",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="MS_ION_POLARITY",
        property_label="Polarity",
        description="""Ionization Polarity//Polarität der Ionisierung""",
        mandatory=False,
        section="MS Parameters",
    )

    # TODO change to REAL + multivalued when implemented in openBIS 7
    ms_mass_range = PropertyTypeAssignment(
        code="MS_MASS_RANGE",
        data_type="VARCHAR",
        property_label="Mass range",
        description="""Sample mass range in [min-max]//Massenbereich der Messung in [min-max]""",
        mandatory=False,
        section="MS Parameters",
    )


class MassSpec(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.MASS_SPEC",
        description="""Mass Spectrometer//Massenspektrometer""",
        generated_code_prefix="INS.MS",
    )

    mass_spec_type = PropertyTypeAssignment(
        code="MASS_SPEC_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="MASS_SPEC_TYPE",
        property_label="MS Type",
        description="""Mass Spectrometer Type//Massenspektrometer-Typ""",
        mandatory=False,
        section="Technical Details",
    )

    ion_source = PropertyTypeAssignment(
        code="IONIZATION_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="IONIZATION_TYPE",
        property_label="Ion source",
        description="""Ionization Type//Ionenquelle""",
        mandatory=False,
        section="Technical Details",
    )

    chromatography = PropertyTypeAssignment(
        code="CHROMATOGRAPHY_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CHROMATOGRAPHY_TYPE",
        property_label="Chromatography",
        description="""Separator Type//Trennverfahren""",
        mandatory=False,
        section="Technical Details",
    )

    detector = PropertyTypeAssignment(
        code="DETECTOR_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DETECTOR_TYPE",
        property_label="Detector",
        description="""Detector Type//Analysator""",
        mandatory=False,
        section="Technical Details",
    )


class LcSystem(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.LC_SYSTEM",
        description="""LC-System//LC-System""",
        generated_code_prefix="INS.LC",
    )

    detector_type = PropertyTypeAssignment(
        code="DETECTOR_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DETECTOR_TYPE",
        property_label="Detector",
        description="""Detector Type//Analysator""",
        mandatory=False,
        section="Technical Details",
    )

    detector_type_secondary = PropertyTypeAssignment(
        code="DETECTOR_TYPE_SECONDARY",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DETECTOR_TYPE",
        property_label="Detector",
        description="""Detector Type//Analysator""",
        mandatory=False,
        section="Technical Details",
    )


class GcSystem(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.GC_SYSTEM",
        description="""GC-System//GC-System""",
        generated_code_prefix="INS.GC",
    )

    detector_type = PropertyTypeAssignment(
        code="DETECTOR_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DETECTOR_TYPE",
        property_label="Detector",
        description="""Detector Type//Analysator""",
        mandatory=False,
        section="Technical Details",
    )

    detector_type_secondary = PropertyTypeAssignment(
        code="DETECTOR_TYPE_SECONDARY",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DETECTOR_TYPE",
        property_label="Detector",
        description="""Detector Type//Analysator""",
        mandatory=False,
        section="Technical Details",
    )


class SIMS(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.SIMS",
        description="""Experimental step for a Time-of-Flight Secondary-Ion-Mass-Spectrometry (ToF-SIMS) analysis in spectrometry, depth profiling or imaging mode//Experimenteller Schritt für eine Time-of-Flight Sekundärionen-Massenspektrometrie (ToF-SIMS) Analyse im Spektrometrie-, Tiefenprofil- oder Imaging-Modus""",
        generated_code_prefix="EXP.SIMS",
    )

    # TODO check if this property should be moved to the ExperimentalStep type
    customer = PropertyTypeAssignment(
        code="CUSTOMER",
        data_type="VARCHAR",
        property_label="Customer",
        description="""Name of the person for whom the measurement is performed""",
        mandatory=False,
        section="General Information",
    )

    sims_lmig_setting = PropertyTypeAssignment(
        code="SIMS_LMIG_SETTING",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="SIMS_LMIG_SETTING",
        property_label="LMIG Setting",
        description="""LMIG setting used for measurement""",
        mandatory=False,
        section="Experimental Settings",
    )

    sims_primary_ion = PropertyTypeAssignment(
        code="SIMS_PRIMARY_ION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="SIMS_PRIMARY_ION",
        property_label="Primary Ion",
        description="""Primary ion used for analysis""",
        mandatory=False,
        section="Experimental Settings",
    )

    sims_polarity = PropertyTypeAssignment(
        code="SIMS_POLARITY",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="MS_ION_POLARITY",
        property_label="Polarity",
        description="""Polarity""",
        mandatory=False,
        section="Experimental Settings",
    )

    sims_lmig_voltage_dc = PropertyTypeAssignment(
        code="SIMS_LMIG_VOLTAGE_DC",
        data_type="REAL",
        units="nA",
        property_label="LMIG Voltage DC",
        description="""LMIG Voltage direct current (DC) in nA""",
        mandatory=False,
        section="Experimental Settings",
    )

    sims_lmig_voltage_p = PropertyTypeAssignment(
        code="SIMS_LMIG_VOLTAGE_P",
        data_type="REAL",
        units="pA",
        property_label="LMIG Voltage P",
        description="""LMIG Voltage pulsed (P) in pA""",
        mandatory=False,
        section="Experimental Settings",
    )

    sims_lmig_pulse_width = PropertyTypeAssignment(
        code="SIMS_LMIG_PULSE_WIDTH",
        data_type="REAL",
        units="ns",
        property_label="Primary ion beam pulse width",
        description="""Primary ion beam pulse width in ns""",
        mandatory=False,
        section="Experimental Settings",
    )

    sims_lmig_raster_size = PropertyTypeAssignment(
        code="SIMS_LMIG_RASTER_SIZE",
        data_type="REAL",
        units="µm",
        property_label="Primary ion beam raster size",
        description="""Primary ion beam raster size in µm""",
        mandatory=False,
        section="Experimental Settings",
    )

    sims_sputter_source = PropertyTypeAssignment(
        code="SIMS_SPUTTER_SOURCE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="SIMS_SPUTTER_SOURCE",
        property_label="Sputter Source",
        description="""Sputter Source""",
        mandatory=False,
        section="Experimental Settings",
    )

    sims_dsc_voltage = PropertyTypeAssignment(
        code="SIMS_DSC_VOLTAGE",
        data_type="REAL",
        units="nA",
        property_label="DSC Voltage",
        description="""DSC Voltage in nA""",
        mandatory=False,
        section="Experimental Settings",
    )

    sims_dsc_raster_size = PropertyTypeAssignment(
        code="SIMS_DSC_RASTER_SIZE",
        data_type="REAL",
        units="µm",
        property_label="Secondary ion beam raster size",
        description="""Secondary (Sputter) ion beam raster size in µm""",
        mandatory=False,
        section="Experimental Settings",
    )

    sims_charge_compensation = PropertyTypeAssignment(
        code="SIMS_CHARGE_COMPENSATION",
        data_type="REAL",
        units="V",
        property_label="Charge compensation",
        description="""Charge compensation in V""",
        mandatory=False,
        section="Experimental Settings",
    )
