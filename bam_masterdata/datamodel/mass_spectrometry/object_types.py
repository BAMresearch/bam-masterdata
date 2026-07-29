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
