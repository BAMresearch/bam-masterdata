from bam_masterdata.datamodel.v2.base import (
    Analysis,
    Calibration,
    Measurement,
    Processing,
    Simulation,
    Synthesis,
    Test,
)
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment


class DCPD(Measurement):
    # ! check whether keeping the Results here
    defs = ObjectTypeDef(
        code="DCPD",
        description="""
        A Direct Current Potential Drop Measurement (DCPD) is a measurement that applies a controlled
        direct current to a sample and records the resulting potential drop in order to infer
        changes in the electrical resistance. This is often use to monitor crack growth or
        damage evolution in materials, as the presence of a crack can increase the resistance
        and thus the potential drop.
        """,
        iri="https://bam.de/masterdata/DCPD",
        references=[],
        generated_code_prefix="DCPD",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.DCPD"],
    )

    pot_drop_calibration = PropertyTypeAssignment(
        code="DCPD_POT_DROP_CALIBRATION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DCPD_POT_DROP_CALIBRATION",
        property_label="Potential drop calibration",
        description="""
        Calibration method used to relate potential drop to crack length (or resistance) in
        DCPD measurements: FEM_FIT, JOHNSON
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["DCPD_POT_DROP_CAL"],
    )

    current = PropertyTypeAssignment(
        code="DCPD_CURRENT",
        data_type="REAL",
        property_label="Current",
        units="amp",
        description="""
        Applied DC current during the DCPD measurment in amperes [A].
        """,
        mandatory=False,
        section="Setup",
    )

    initial_crack_length = PropertyTypeAssignment(
        code="DCPD_INITIAL_CRACK_LENGTH",
        data_type="REAL",
        property_label="Initial crack length",
        units="mm",
        description="""
        Initial crack length measured optically before DCPD-based evaluation in millimeters [mm].
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["DCPD_INITIAL_CRACKLENGTH"],
    )

    yzero_fitted = PropertyTypeAssignment(
        code="DCPD_YZERO_FITTED",
        data_type="REAL",
        property_label="Johnson formula Y0",
        units="mm",
        description="""
        Fitted Y0 parameter for the Johnson relation, adapted to the notch geometry and specimen
        dimensions, in millimeters [mm].
        """,
        mandatory=False,
        section="Setup",
    )

    fem_fit_eq = PropertyTypeAssignment(  # ! clarify with experts
        code="FEM_FIT_EQ",
        data_type="VARCHAR",
        property_label="FEM fit equation",
        description="""
        Identifier or short representation of the FEM-based fit used (a = f(U)); you can also
        link to the full definition as a file or script.
        """,
        mandatory=False,
        section="Setup",
    )


class DLS(Measurement):
    defs = ObjectTypeDef(
        code="DLS",
        description="""
        A Measurement is an activity that uses an experimental device to produce quantitative
        or qualitative data about the properties of a material.
        Dynamic and electrophoretic light scattering that derives hydrodynamic diameter distributions,
        zeta potential, and stability metrics from colloidal suspensions.
        """,
        iri="https://bam.de/masterdata/DLS",
        references=[],
        generated_code_prefix="DLS",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.DLS"],
    )

    dispersant = PropertyTypeAssignment(
        code="DLS_DISPERSANT",
        data_type="VARCHAR",
        property_label="Dispersant",
        description="""
        Dispersing medium used for the DLS measurement.
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["DLS.DISPERSANT"],
    )

    temperature = PropertyTypeAssignment(
        code="DLS_TEMPERATURE",
        data_type="REAL",
        property_label="Temperature",
        units="celsius",
        description="""
        Measurement temperature in degrees Celsius [C].
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["DLS.TEMPERATURE"],
    )

    cell_description = PropertyTypeAssignment(
        code="DLS_CELL_DESCRIPTION",
        data_type="VARCHAR",
        property_label="Cell description",
        description="""
        Description of the measurement cell or cuvette used for DLS.
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["DLS.CELLDESCRIPTION"],
    )

    attenuator = PropertyTypeAssignment(
        code="DLS_ATTENUATOR",
        data_type="INTEGER",
        property_label="Attenuator",
        description="""
        Attenuator setting used during DLS acquisition.
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["DLS.ATTENUATOR"],
    )

    z_average = PropertyTypeAssignment(
        code="DLS_Z_AVERAGE",
        data_type="REAL",
        property_label="Z-average",
        units="nm",
        description="""
        Z-average hydrodynamic diameter derived from the DLS measurement in nanometers [nm].
        """,
        mandatory=False,
        section="Results",
        previous_versions=["DLS.ZAVG"],
    )

    polydispersity_index = PropertyTypeAssignment(
        code="DLS_PDI",
        data_type="REAL",
        property_label="Polydispersity index",
        description="""
        Polydispersity index (PDI) of the measured particle size distribution.
        """,
        mandatory=False,
        section="Results",
        previous_versions=["DLS.PDI"],
    )

    zeta_potential = PropertyTypeAssignment(
        code="DLS_ZETA_POTENTIAL",
        data_type="REAL",
        property_label="Zeta potential",
        units="mV",
        description="""
        Zeta potential measured for the sample in millivolts [mV].
        """,
        mandatory=False,
        section="Results",
        previous_versions=["DLS.ZETA"],
    )

    conductivity = PropertyTypeAssignment(
        code="DLS_CONDUCTIVITY",
        data_type="REAL",
        property_label="Conductivity",
        units="mS/cm",
        description="""
        Conductivity of the measured dispersion in millisiemens per centimeter [mS/cm].
        """,
        mandatory=False,
        section="Results",
        previous_versions=["DLS.COND"],
    )

    # ! check other properties in old schema


class FTIR(Measurement):
    defs = ObjectTypeDef(
        code="FTIR",
        description="""
        A Measurement is an activity that uses an experimental device to produce quantitative
        or qualitative data about the properties of a material.
        Fourier transform infrared spectroscopy probing vibrational modes to fingerprint
        molecular composition and surface bonds.
        """,
        iri="https://bam.de/masterdata/FTIR",
        references=[],
        generated_code_prefix="FTIR",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.FTIR"],
    )

    start_wavenumber = PropertyTypeAssignment(
        code="FTIR_START_WAVENUMBER",
        data_type="REAL",
        property_label="Start wavenumber",
        units="1/cm",
        description="""
        Start of the acquired FTIR wavenumber range in reciprocal centimeters [1/cm].
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["FTIR.START_WAVENUMBER"],
    )

    end_wavenumber = PropertyTypeAssignment(
        code="FTIR_END_WAVENUMBER",
        data_type="REAL",
        property_label="End wavenumber",
        units="1/cm",
        description="""
        End of the acquired FTIR wavenumber range in reciprocal centimeters [1/cm].
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["FTIR.END_WAVENUMBER"],
    )

    resolution = PropertyTypeAssignment(
        code="FTIR_RESOLUTION",
        data_type="INTEGER",
        property_label="Resolution",
        units="1/cm",
        description="""
        Spectral resolution used for FTIR acquisition in reciprocal centimeters [1/cm].
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["FTIR.RESOLUTION"],
    )

    scan_count = PropertyTypeAssignment(
        code="FTIR_SCAN_COUNT",
        data_type="INTEGER",
        property_label="Scan count",
        description="""
        Number of scans collected for the FTIR spectrum.
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["FTIR.SCANS"],
    )

    accessory = PropertyTypeAssignment(
        code="FTIR_ACCESSORY",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="FTIR_ACCESSORIES",
        property_label="Accessory",
        description="""
        Accessory configuration used for the FTIR measurement (for example ATR).
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["FTIR.ACCESSORY"],
    )

    flushed_with_nitrogen = PropertyTypeAssignment(
        code="FTIR_FLUSHED_WITH_NITROGEN",
        data_type="BOOLEAN",
        property_label="Flushed with nitrogen?",
        description="""
        Indicates whether the FTIR optical path or chamber was flushed with nitrogen.
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["FTIR.IS_FLUSHED"],
    )


class ImageSeries(Measurement):
    defs = ObjectTypeDef(
        code="IMAGE_SERIES",
        description="""
        A Measurement is an activity that uses an experimental device to produce quantitative
        or qualitative data about the properties of a material.
        A structured series of still images documenting morphology change, defects, or process evolution
        on material surfaces or cross sections.
        """,
        iri="https://bam.de/masterdata/ImageSeries",
        references=[],
        generated_code_prefix="IMAGE_SERIE",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.IMAGE_SERIES"],
    )

    image_horizontal_resolution = PropertyTypeAssignment(
        code="IMAGE_HORIZONTAL_RESOLUTION",
        data_type="INTEGER",
        property_label="Horizontal resolution in [pixel]",  # ! pixel is not defined in pint
        description="""
        Horizontal pixel resolution of each recorded image.
        """,
        mandatory=False,
        section="Acquisition",
    )

    image_vertical_resolution = PropertyTypeAssignment(
        code="IMAGE_VERTICAL_RESOLUTION",
        data_type="INTEGER",
        property_label="Vertical resolution in [pixel]",  # ! pixel is not defined in pint
        description="""
        Vertical pixel resolution of each recorded image.
        """,
        mandatory=False,
        section="Acquisition",
    )

    image_count = PropertyTypeAssignment(
        code="IMAGE_SERIES_COUNT",
        data_type="INTEGER",
        property_label="Image count",
        description="""
        Number of still images recorded in the series.
        """,
        mandatory=False,
        section="Acquisition",
        previous_versions=["IMAGE_SERIES_COUNT"],
    )


class MicroscopyFractureSurface(Measurement):
    defs = ObjectTypeDef(
        code="MICROSCOPY_FRACTURE_SURFACE",
        description="""
        A Microscopy Fracture Surface is a measurement that determines crack length on the
        fracture surface of a fatigue crack growth sample using optical microscopy.
        """,
        iri="https://bam.de/masterdata/MicroscopyFractureSurface",
        references=[],
        generated_code_prefix="MICRO_FRACT_SURF",
        aliases=[],
        previous_versions=[
            "EXPERIMENTAL_STEP.MICROSCOPY_FCG_FRACTURE_SURFACE_CRACKLENGTH"
        ],
    )

    microscopy_fracture_surface_type = PropertyTypeAssignment(
        code="MICROSCOPY_FRACTURE_SURFACE_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="MICROSCOPY_FRACTURE_SURFACE_TYPE",
        property_label="Crack length type",
        description="""
        Category of crack length measured on the fracture surface: BEACHMARK, FINAL, NOTCH.
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["MIC_FCG_FRACSURF_CRACKLENGTH_TYPE"],
    )

    microscopy_fracture_surface_crack_length = PropertyTypeAssignment(
        code="MICROSCOPY_FRACTURE_SURFACE_CRACK_LENGTH",
        data_type="REAL",
        property_label="Crack length",
        units="mm",
        description="""
        Crack length measured on the fracture surface in millimeters [mm].
        """,
        mandatory=False,
        section="Results",
        previous_versions=["MIC_FCG_FRACSURF_CRACKLENGTH_VALUE"],
    )

    microscopy_fracture_surface_cycle_count = PropertyTypeAssignment(
        code="MICROSCOPY_FRACTURE_SURFACE_CYCLE_COUNT",
        data_type="INTEGER",
        property_label="Cycle count",
        description="""
        Cycle count associated with the fracture-surface crack length measurement.
        """,
        mandatory=False,
        section="Results",
        previous_versions=["MIC_FCG_FRACSURF_CRACKLENGTH_CYCLES"],
    )


class NMR(Measurement):
    defs = ObjectTypeDef(
        code="NMR",
        description="""
        A Measurement is an activity that uses an experimental device to produce quantitative
        or qualitative data about the properties of a material.
        Nuclear magnetic resonance spectroscopy targeting nuclei-specific resonances to reveal
        structural and compositional information of materials.
        """,
        iri="https://bam.de/masterdata/NMR",
        references=[],
        generated_code_prefix="NMR",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.NMR"],
    )

    nucleus_direct = PropertyTypeAssignment(
        code="NMR_NUCLEUS_DIRECT",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="NMR_NUCLEI",
        property_label="Direct nucleus",
        description="""
        Nucleus observed in the direct detection channel (for example 1H, 13C).
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["NMR.NUCLEUS_DIRECT"],
    )

    nucleus_indirect = PropertyTypeAssignment(
        code="NMR_NUCLEUS_INDIRECT",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="NMR_NUCLEI",
        property_label="Indirect nucleus",
        description="""
        Nucleus observed in the indirect dimension for multidimensional NMR experiments.
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["NMR.NUCLEUS_INDIRECT"],
    )

    solvent = PropertyTypeAssignment(
        code="NMR_SOLVENT",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="NMR_SOLVENTS",
        property_label="Solvent",
        description="""
        Solvent used for sample preparation and acquisition.
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["NMR.SOLVENT"],
    )

    frequency = PropertyTypeAssignment(
        code="NMR_FREQUENCY",
        data_type="REAL",
        property_label="Frequency",
        units="MHz",
        description="""
        Operating frequency of the NMR experiment in megahertz [MHz].
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["NMR.FREQUENCY"],
    )

    type = PropertyTypeAssignment(
        code="NMR_EXPERIMENT_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="NMR_EXPERIMENT_TYPES",
        property_label="Experiment type",
        description="""
        NMR experiment type or pulse program identifier.
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["NMR.EXPERIMENT"],
    )

    scan_count = PropertyTypeAssignment(
        code="NMR_SCAN_COUNT",
        data_type="INTEGER",
        property_label="Scan count",
        description="""
        Number of scans acquired for the NMR experiment.
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["NMR.SCANS"],
    )

    start_chemical_shift = PropertyTypeAssignment(
        code="NMR_START_CHEMICAL_SHIFT",
        data_type="REAL",
        property_label="Start chemical shift",
        units="ppm",
        description="""
        Lower bound of the acquired chemical shift range in parts per million [ppm].
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["NMR.START_CHEMICAL_SHIFT"],
    )

    end_chemical_shift = PropertyTypeAssignment(
        code="NMR_END_CHEMICAL_SHIFT",
        data_type="REAL",
        property_label="End chemical shift",
        units="ppm",
        description="""
        Upper bound of the acquired chemical shift range in parts per million [ppm].
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["NMR.END_CHEMICAL_SHIFT"],
    )

    is_quantitative_nmr = PropertyTypeAssignment(
        code="NMR_IS_QUANTITATIVE",
        data_type="BOOLEAN",
        property_label="Quantitative NMR?",
        description="""
        Indicates whether the acquisition and processing were performed as quantitative NMR (qNMR).
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["NMR.IS_QNMR"],
    )

    pulse_angle = PropertyTypeAssignment(
        code="NMR_PULSE_ANGLE",
        data_type="REAL",
        property_label="Pulse angle",
        units="degree",
        description="""
        Excitation pulse flip angle in degrees.
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["NMR.PULSE_ANGLE"],
    )

    interpulse_delay = PropertyTypeAssignment(
        code="NMR_INTERPULSE_DELAY",
        data_type="REAL",
        property_label="Interpulse delay",
        units="s",
        description="""
        Delay between pulses in seconds [s].
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["NMR.INTERPULSE_DELAY"],
    )

    acquisition_time = PropertyTypeAssignment(
        code="NMR_ACQUISITION_TIME",
        data_type="REAL",
        property_label="Acquisition time",
        units="s",
        description="""
        Acquisition duration in seconds [s].
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["NMR.ACQUISITION_TIME"],
    )


class ProfileScan(Measurement):
    defs = ObjectTypeDef(
        code="PROFILE_SCAN",
        description="""
        A Measurement is an activity that uses an experimental device to produce quantitative
        or qualitative data about the properties of a material.
        A sequence of 2D line sensor readings used to capture surface height profiles, edge geometries,
        or deformation along a flight path.
        """,
        iri="https://bam.de/masterdata/ProfileScan",
        references=[],
        generated_code_prefix="PROFI_SCAN",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.PROFILE_SCAN"],
    )

    scan_line_count = PropertyTypeAssignment(
        code="SCAN_LINE_COUNT",
        data_type="INTEGER",
        property_label="Scan line count",
        description="""
        Number of individual scan lines captured in the profile scan series.
        """,
        mandatory=False,
        section="Acquisition",
    )

    scan_line_resolution = PropertyTypeAssignment(
        code="SCAN_LINE_RESOLUTION",
        data_type="INTEGER",
        property_label="Scan line resolution in [pixel]",  # ! pixel is not defined in pint
        description="""
        Number of pixels sampled for each scan line.
        """,
        mandatory=False,
        section="Acquisition",
    )


class SaxsMeasurement(Measurement):
    defs = ObjectTypeDef(
        code="SAXS_MEASUREMENT",
        description="""
        A Measurement is an activity that uses an experimental device to produce quantitative
        or qualitative data about the properties of a material.
        Metadata describing a small-angle X-ray scattering measurement for accessing nanoscale
        structural features and orientation distributions.
        """,
        iri="https://bam.de/masterdata/SaxsMeasurement",
        references=[],
        generated_code_prefix="SAXS",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.SAXS_MEASUREMENT"],
    )

    cell_temperature = PropertyTypeAssignment(
        code="SAXS_CELL_TEMPERATURE",
        data_type="REAL",
        property_label="Cell temperature",
        units="celsius",
        description="""
        Temperature of the measurement cell during SAXS acquisition in degrees Celsius [C].
        """,
        mandatory=True,
        section="Setup",
        previous_versions=["CELL_TEMPERATURE_IN_CELSIUS"],
    )

    exposure_time = PropertyTypeAssignment(
        code="SAXS_EXPOSURE_TIME",
        data_type="REAL",
        property_label="Exposure time",
        units="s",
        description="""
        Exposure time of a single SAXS frame in seconds [s].
        """,
        mandatory=True,
        section="Setup",
        previous_versions=["EXPOSURE_TIME_IN_SECONDS"],
    )

    frame_count = PropertyTypeAssignment(
        code="SAXS_FRAME_COUNT",
        data_type="INTEGER",
        property_label="Frame count",
        description="""
        Number of frames acquired for this SAXS measurement.
        """,
        mandatory=True,
        section="Setup",
        previous_versions=["FRAME_COUNT"],
    )


class SEM(Measurement):
    defs = ObjectTypeDef(
        code="SEM",
        description="""
        A Measurement is an activity that uses an experimental device to produce quantitative
        or qualitative data about the properties of a material.
        Scanning electron microscopy that documents surfaces, microstructure, and defect populations
        through secondary/backscattered contrast and high magnification imaging.
        """,
        iri="https://bam.de/masterdata/SEM",
        references=[],
        generated_code_prefix="SEM",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.SEM"],
    )

    operating_mode = PropertyTypeAssignment(
        code="SEM_OPERATING_MODE",
        data_type="VARCHAR",
        property_label="Operating mode",
        description="""
        Operating mode selected on the SEM.
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["SEM.OPERATINGMODE"],
    )

    detector = PropertyTypeAssignment(
        code="SEM_DETECTOR",
        data_type="VARCHAR",
        property_label="Detector",
        description="""
        Detector configuration used for image acquisition.
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["SEM.DETECTOR"],
    )

    acceleration_voltage = PropertyTypeAssignment(
        code="SEM_ACCELERATION_VOLTAGE",
        data_type="REAL",
        property_label="Acceleration voltage",
        units="kV",
        description="""
        Electron acceleration voltage used in the SEM measurement.
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["SEM.ACCELERATIONVOLTAGE"],
    )

    magnification = PropertyTypeAssignment(
        code="SEM_MAGNIFICATION",
        data_type="VARCHAR",
        property_label="Magnification",
        description="""
        Magnification used during SEM image acquisition.
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["SEM.MAGNIFICATION"],
    )

    working_distance = PropertyTypeAssignment(
        code="SEM_WORKING_DISTANCE",
        data_type="VARCHAR",
        property_label="Working distance",
        description="""
        Working distance between specimen and objective during SEM acquisition.
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["SEM.WORKINGDISTANCE"],
    )

    # ! is this correct or should we use another property?
    image_horizontal_resolution = PropertyTypeAssignment(
        code="IMAGE_HORIZONTAL_RESOLUTION",
        data_type="INTEGER",
        property_label="Horizontal resolution in [pixel]",  # ! pixel is not defined in pint
        description="""
        Horizontal pixel resolution of each recorded image.
        """,
        mandatory=False,
        section="Acquisition",
        previous_versions=["SEM.PIXELSIZEX", "SEM.IMAGESIZEX"],
    )

    # ! is this correct or should we use another property?
    image_vertical_resolution = PropertyTypeAssignment(
        code="IMAGE_VERTICAL_RESOLUTION",
        data_type="INTEGER",
        property_label="Vertical resolution in [pixel]",  # ! pixel is not defined in pint
        description="""
        Vertical pixel resolution of each recorded image.
        """,
        mandatory=False,
        section="Acquisition",
        previous_versions=["SEM.PIXELSIZEY", "SEM.IMAGESIZEY"],
    )


class TEM(Measurement):
    defs = ObjectTypeDef(
        code="TEM",
        description="""
        A Measurement is an activity that uses an experimental device to produce quantitative
        or qualitative data about the properties of a material.
        Transmission electron microscopy that traverses thin sections with a focused beam to expose
        internal crystallographic structure and contrast mechanisms.
        """,
        iri="https://bam.de/masterdata/TEM",
        references=[],
        generated_code_prefix="TEM",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.TEM"],
    )

    operating_mode = PropertyTypeAssignment(
        code="TEM_OPERATING_MODE",
        data_type="VARCHAR",
        property_label="Operating mode",
        description="""
        Operating mode selected on the TEM.
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["TEM.OPERATINGMODE"],
    )

    detector = PropertyTypeAssignment(
        code="TEM_DETECTOR",
        data_type="VARCHAR",
        property_label="Detector",
        description="""
        Detector configuration used during TEM acquisition.
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["TEM.DETECTOR"],
    )

    acceleration_voltage = PropertyTypeAssignment(
        code="TEM_ACCELERATION_VOLTAGE",
        data_type="REAL",
        units="kV",
        property_label="Acceleration voltage",
        description="""
        Electron acceleration voltage used during TEM acquisition.
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["TEM.ACCELERATIONVOLTAGE"],
    )

    magnification = PropertyTypeAssignment(
        code="TEM_MAGNIFICATION",
        data_type="VARCHAR",
        property_label="Magnification",
        description="""
        Magnification used for TEM image acquisition.
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["TEM.MAGNIFICATION"],
    )

    camera_length = PropertyTypeAssignment(
        code="TEM_CAMERA_LENGTH",
        data_type="VARCHAR",  # ! this should be REAL with units mm?
        property_label="Camera length",
        description="""
        Camera length setting used during TEM measurement.
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["TEM.CAMERALENGTH"],
    )

    # ! is this correct or should we use another property?
    image_horizontal_resolution = PropertyTypeAssignment(
        code="IMAGE_HORIZONTAL_RESOLUTION",
        data_type="INTEGER",
        property_label="Horizontal resolution in [pixel]",  # ! pixel is not defined in pint
        description="""
        Horizontal pixel resolution of each recorded image.
        """,
        mandatory=False,
        section="Acquisition",
        previous_versions=["SEM.PIXELSIZEX", "SEM.IMAGESIZEX"],
    )

    # ! is this correct or should we use another property?
    image_vertical_resolution = PropertyTypeAssignment(
        code="IMAGE_VERTICAL_RESOLUTION",
        data_type="INTEGER",
        property_label="Vertical resolution in [pixel]",  # ! pixel is not defined in pint
        description="""
        Vertical pixel resolution of each recorded image.
        """,
        mandatory=False,
        section="Acquisition",
        previous_versions=["SEM.PIXELSIZEY", "SEM.IMAGESIZEY"],
    )

    # ! there are some missing properties I don't know about


class ThermographicMeasurement(Measurement):
    defs = ObjectTypeDef(
        code="THERMOGRAPHIC_MEASUREMENT",
        description="""
        A Measurement is an activity that uses an experimental device to produce quantitative
        or qualitative data about the properties of a material.
        Thermographic measurement capturing infrared maps to monitor thermal gradients, defects,
        and material response to heating or cooling cycles.
        """,
        iri="https://bam.de/masterdata/ThermographicMeasurement",
        references=[],
        generated_code_prefix="THERM_MEASU",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.THERMOGRAPHIC_MEASUREMENT"],
    )


class VideoRecording(Measurement):
    defs = ObjectTypeDef(
        code="VIDEO_RECORDING",
        description="""
        A Measurement is an activity that uses an experimental device to produce quantitative
        or qualitative data about the properties of a material.
        Documentary video capturing dynamic tests, process evolution, or damage progression with
        frame data appended as measurement metadata.
        """,
        iri="https://bam.de/masterdata/VideoRecording",
        references=[],
        generated_code_prefix="VIDEO_RECOR",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.VIDEO_RECORDING"],
    )

    image_horizontal_resolution = PropertyTypeAssignment(
        code="IMAGE_HORIZONTAL_RESOLUTION",
        data_type="INTEGER",
        property_label="Horizontal resolution in [pixel]",  # ! pixel is not defined in pint
        description="""
        Horizontal pixel resolution of recorded video frames.
        """,
        mandatory=False,
        section="Acquisition",
    )

    image_vertical_resolution = PropertyTypeAssignment(
        code="IMAGE_VERTICAL_RESOLUTION",
        data_type="INTEGER",
        property_label="Vertical resolution in [pixel]",  # ! pixel is not defined in pint
        description="""
        Vertical pixel resolution of recorded video frames.
        """,
        mandatory=False,
        section="Acquisition",
    )

    frame_rate = PropertyTypeAssignment(
        code="VIDEO_FRAME_PER_SECONDS",
        data_type="INTEGER",
        property_label="Frame rate",
        units="1/s",
        description="""
        Average video frame rate in frames per second [1/s].
        """,
        mandatory=False,
        section="Acquisition",
    )

    codec = PropertyTypeAssignment(
        code="VIDEO_CODEC",
        data_type="VARCHAR",
        property_label="Codec",
        description="""
        Video codec used during recording, if compression was applied.
        """,
        mandatory=False,
        section="Acquisition",
    )

    dynamic_frame_rate = PropertyTypeAssignment(
        code="VIDEO_DYNAMIC_FRAMERATE",
        data_type="BOOLEAN",
        property_label="Dynamic frame rate",
        description="""
        Indicates whether the video frame rate changed over time.
        """,
        mandatory=False,
        section="Acquisition",
    )

    camera_shutter_mode = PropertyTypeAssignment(
        code="CAMERA_SHUTTER_MODE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CAMERA_SHUTTER_MODE",
        property_label="Shutter mode",
        description="""
        Shutter mode used for video recording
        """,
        mandatory=False,
        section="Acquisition",
    )


class RazorbladeNotching(Processing):
    defs = ObjectTypeDef(
        code="RAZORBLADE_NOTCHING",
        description="""
        A Razorblade Notching is a processing activity that introduces or extends a notch or
        crack starter in a sample by repeatedly drawing a razorblade across its surface under
        controlled conditions.
        """,
        iri="https://bam.de/masterdata/RazorbladeNotching",
        references=[],
        generated_code_prefix="RAZOR_NOTCH",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.RAZORBLADE_NOTCHING"],
    )

    razor_stroke_length = PropertyTypeAssignment(
        code="RAZOR_STROKE_LENGTH",
        data_type="REAL",
        property_label="Stroke length",
        units="mm",
        description="""
        Length of a single razor blade stroke applied to the sample surface in millimeters [mm].
        """,
        mandatory=False,
        section="Process Parameters",
        previous_versions=["RAZOR_STROKELENGTH"],
    )

    razor_stroke_speed = PropertyTypeAssignment(
        code="RAZOR_STROKE_SPEED",
        data_type="REAL",
        property_label="Stroke speed",
        units="mm/s",
        description="""
        Speed of the razor blade during a stroke in millimeters per second [mm/s].
        """,
        mandatory=False,
        section="Process Parameters",
        previous_versions=["RAZOR_STROKESPEED"],
    )

    razor_stroke_count = PropertyTypeAssignment(
        code="RAZOR_STROKE_COUNT",
        data_type="INTEGER",
        property_label="Stroke count",
        description="""
        Total number of razor blade strokes applied during notching.
        """,
        mandatory=False,
        section="Process Parameters",
        previous_versions=["RAZOR_STROKECOUNT"],
    )

    razor_depth = PropertyTypeAssignment(
        code="RAZOR_DEPTH",
        data_type="REAL",
        property_label="Notch depth increase",
        units="µm",
        description="""
        Increase in notch depth measured after the notching process in micrometers [µm].
        """,
        mandatory=False,
        section="Results",
    )


class SamplePretreatment(Processing):
    defs = ObjectTypeDef(
        code="SAMPLE_PRETREATMENT",
        description="""
        A Processing is an activity that alters the structure, composition, or form of a
        material.
        Treatment of a Sample before measurement
        """,
        iri="https://bam.de/masterdata/SamplePretreatment",
        references=[],
        generated_code_prefix="SAMPL_PRETR",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.SAMPLE_PRETREATMENT"],
    )


class Weldment(Processing):
    defs = ObjectTypeDef(
        code="WELDMENT",
        description="""
        A Processing is an activity that alters the structure, composition, or form of a
        material.
        An experimental step describing a welding experiment
        """,
        iri="https://bam.de/masterdata/Weldment",
        references=[],
        generated_code_prefix="WELDM",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.WELDMENT"],
    )

    weld_joint_number = PropertyTypeAssignment(
        code="WELD_JOINT_NUMBER",
        data_type="INTEGER",
        property_label="Joint Number",
        description="""
        Consecutive numbering of weld joints of a workpiece or component//Fortlaufende Numerierung von Schweißnähten an Werkstücken und Bauteilen
        """,
        mandatory=False,
        section="Identifiers",
    )

    weld_layer_number = PropertyTypeAssignment(
        code="WELD_LAYER_NUMBER",
        data_type="INTEGER",
        property_label="Layer Number",
        description="""
        Consecutive numbering of weld layers for a parent joint//Fortlaufende Numerierung von Schweißlagen der übergeordneten Schweißnaht
        """,
        mandatory=False,
        section="Identifiers",
    )

    weld_bead_number = PropertyTypeAssignment(
        code="WELD_BEAD_NUMBER",
        data_type="INTEGER",
        property_label="Bead Number",
        description="""
        Consecutive numbering of weld beads or tracks for a parent layer//Fortlaufende Numerierung von Schweißraupen der übergeordneten Schweißlage
        """,
        mandatory=False,
        section="Identifiers",
    )

    weld_weldment_number = PropertyTypeAssignment(
        code="WELD_WELDMENT_NUMBER",
        data_type="INTEGER",
        property_label="Weldment Number",
        description="""
        Consecutive numbering of uninterrupted weldments in a single bead//Fortlaufende Numerierung von ununterbrochenen Schweißungen einer einzelnen Schweißraupe
        """,
        mandatory=False,
        section="Identifiers",
    )

    weldment_type = PropertyTypeAssignment(
        code="WELDMENT_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="WELD_TYPE",
        property_label="Type of weld",
        description="""
        Type of weldment made//Art der Schweißverbindung
        """,
        mandatory=False,
        show_in_edit_views=False,
        section="Weldment Information",
    )


class FCGTest(Test):
    # ! add results from former FCG_TEST
    # ! check which properties are necessary from FCG_STEP
    defs = ObjectTypeDef(
        code="FCG_TEST",
        description="""
        A Fatigue Crack Growth Test (FCG Test) is a test activity in which a pre-cracked sample
        is cyclically loaded to measure crack growth behavior as a function of loading parameters
        and number of cycles.
        """,
        iri="https://bam.de/masterdata/FCGTest",
        references=[],
        generated_code_prefix="FCG_TEST",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.FCG_TEST", "EXPERIMENTAL_STEP.FCG_STEP"],
    )

    fcg_nominal_r = PropertyTypeAssignment(
        code="FCG_NOMINAL_R",
        data_type="REAL",
        property_label="Nominal R-ratio",
        description="""
        Nominal load ratio R used for the test (R = F_min / F_max).
        """,
        mandatory=True,
        section="Setup",
    )

    initial_cycles = PropertyTypeAssignment(
        code="INITIAL_CYCLES",
        data_type="INTEGER",
        property_label="Initial cycle count",
        description="""
        Cycle count at the start of the test or at the start of the recorded interval.
        """,
        mandatory=False,
        section="Setup",
    )

    initial_crack_length = PropertyTypeAssignment(
        code="INITIAL_CRACK_LENGTH",
        data_type="REAL",
        property_label="Initial crack length",
        units="mm",
        description="""
        Crack length at the start of the test (typically measured optically or defined from
        pre-cracking) in millimeters [mm].
        """,
        mandatory=True,
        section="Setup",
        previous_versions=["INITIAL_CRACKLENGTH"],
    )

    fcg_threshold_eval = PropertyTypeAssignment(
        code="FCG_THRESHOLD_EVAL",
        data_type="BOOLEAN",
        property_label="Threshold evaluation performed?",
        description="""
        Whether a threshold evaluation (ΔK_th or equivalent) was performed for this test.
        """,
        mandatory=False,
        section="Evaluation",
        previous_versions=["FCG_THRSHLD"],
    )

    fcg_paris_eval = PropertyTypeAssignment(
        code="FCG_PARIS_EVAL",
        data_type="BOOLEAN",
        property_label="Paris parameters evaluation performed?",
        description="""
        Whether Paris-law parameters were evaluated for this test.
        """,
        mandatory=False,
        section="Evaluation",
        previous_versions=["FCG_PARIS"],
    )

    fcg_cyclic_r_eval = PropertyTypeAssignment(
        code="FCG_CYCLIC_R_EVAL",
        data_type="BOOLEAN",
        property_label="Cyclic R-curve evaluation performed?",
        description="""
        Whether a cyclic R-curve evaluation was performed for this test.
        """,
        mandatory=False,
        section="Evaluation",
        previous_versions=["FCG_CYCLIC_R"],
    )

    final_cycles = PropertyTypeAssignment(
        code="FINAL_CYCLES",
        data_type="INTEGER",
        property_label="Final cycle count",
        description="""
        Cycle count at the end of the test or at the end of the recorded interval.
        """,
        mandatory=False,
        section="Results",
    )

    final_crack_length = PropertyTypeAssignment(
        code="FINAL_CRACK_LENGTH",
        data_type="REAL",
        property_label="Final crack length",
        units="mm",
        description="""
        Crack length at the end of the test or at the end of the recorded interval in millimeters [mm].
        """,
        mandatory=False,
        section="Results",
        previous_versions=["FINAL_CRACKLENGTH"],
    )


class LaserDiffPSD(Measurement):
    defs = ObjectTypeDef(
        code="LaserDiffPSD",
        description="""
        Measurement of particle size distribution (PSD) by laser diffraction capturing ensemble
        diameter statistics across the full sample volume using scattering profiles.
        """,
        iri="https://bam.de/masterdata/LaserDiffPSD",
        references=[],
        generated_code_prefix="LASER_DIFF_PSD",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.LASER_DIFF_PSD_MEASUREMENT"],
    )

    dispersing_medium = PropertyTypeAssignment(
        code="DISPERSING_MEDIUM",
        data_type="VARCHAR",
        property_label="Dispersing medium",
        description="""
        Medium in which particles are dispersed for the laser diffraction measurement.
        """,
        mandatory=True,
        section="Setup",
    )

    scattering_model = PropertyTypeAssignment(
        code="SCATTERING_MODEL_PSD_LD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="SCATTERING_MODEL_PSD_LD",
        property_label="Scattering model",
        description="""
        Light scattering model used for PSD evaluation (for example Mie or Fraunhofer).
        """,
        mandatory=True,
        section="Setup",
    )

    refractive_index_sample = PropertyTypeAssignment(
        code="REFRACTIVE_INDEX_SAMPLE",
        data_type="REAL",
        property_label="Refractive index of sample",
        description="""
        Refractive index value used for the sample in the scattering model.
        """,
        mandatory=False,
        section="Setup",
    )

    absorption_coefficient_sample = PropertyTypeAssignment(
        code="ABSORPTION_COEFFICIENT_SAMPLE",
        data_type="REAL",
        property_label="Absorption coefficient of sample",
        description="""
        Absorption coefficient value used for the sample in the scattering model.
        """,
        mandatory=False,
        section="Setup",
        previous_versions=["ABSORPTION_COEFF_SAMPLE"],
    )

    refractive_index_blue_sample = PropertyTypeAssignment(
        code="REFRACTIVE_INDEX_BLUE_SAMPLE",
        data_type="REAL",
        property_label="Refractive index for blue light of sample",
        description="""
        Refractive index of the sample for blue light, if the measuring device has such a second light source//Brechungsindex der Probe für blaues Licht, wenn das Messgerät eine derartige zweite Lichtquelle aufweist
        """,
        mandatory=False,
        section="Setup",
    )

    absorption_coeff_blue_sample = PropertyTypeAssignment(
        code="ABSORPTION_COEFF_BLUE_SAMPLE",
        data_type="REAL",
        property_label="Absorption coefficient for blue light of sample",
        description="""
        Absorption coefficient of the sample for blue light//Absorptionskoeffizient der Probe für blaues Licht
        """,
        mandatory=False,
        section="Setup",
    )

    laser_obscuration = PropertyTypeAssignment(
        code="LASER_OBSCURATION",
        data_type="REAL",
        property_label="Laser obscuration",
        description="""
        Laser obscuration measured during acquisition.
        """,
        mandatory=False,
        section="Results",
    )

    laser_transmission = PropertyTypeAssignment(
        code="LASER_TRANSMISSION",
        data_type="REAL",
        property_label="Laser transmission",
        description="""
        Laser transmission measured during acquisition.
        """,
        mandatory=False,
        section="Results",
    )

    measurement_medium_temperature = PropertyTypeAssignment(
        code="MEASUREMENT_MEDIUM_TEMPERATURE",
        data_type="REAL",
        property_label="Measurement medium temperature",
        units="celsius",
        description="""
        Temperature of the dispersing medium during measurement in degrees Celsius [C].
        """,
        mandatory=False,
        section="Results",
        previous_versions=["MEAS_MEDIUM_TEMPERATURE_IN_CELSIUS"],
    )

    d10 = PropertyTypeAssignment(
        code="PSD_D10",
        data_type="REAL",
        property_label="D10 particle size",
        units="um",
        description="""
        D10 particle size percentile from the measured distribution in micrometers [um].
        """,
        mandatory=False,
        section="Results",
        previous_versions=["D_10_IN_MICROMETERS"],
    )

    d50 = PropertyTypeAssignment(
        code="PSD_D50",
        data_type="REAL",
        property_label="D50 particle size",
        units="um",
        description="""
        D50 particle size percentile from the measured distribution in micrometers [um].
        """,
        mandatory=True,
        section="Results",
        previous_versions=["D_50_IN_MICROMETERS"],
    )

    d90 = PropertyTypeAssignment(
        code="PSD_D90",
        data_type="REAL",
        property_label="D90 particle size",
        units="um",
        description="""
        D90 particle size percentile from the measured distribution in micrometers [um].
        """,
        mandatory=False,
        section="Results",
        previous_versions=["D_90_IN_MICROMETERS"],
    )

    mode_count = PropertyTypeAssignment(
        code="MODE_COUNT",
        data_type="INTEGER",
        property_label="Mode count",
        description="""
        Number of identified distribution modes in the PSD result.
        """,
        mandatory=False,
        section="Results",
    )


# ! Hidden inherited properties: EXPERIMENTAL_DESCRIPTION, EXPERIMENTAL_RESULTS,
# ! EXPERIMENTAL_GOALS, SPREADSHEET, REFERENCE, PUBLICATION, COMMENTS
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
        show_in_edit_views=True,
        section="General Information",
    )

    sample_position = PropertyTypeAssignment(
        code="SAMPLE_POSITION",
        data_type="VARCHAR",
        property_label="Sample Position // Position der Probe",
        description="""The sample position ID in the sample holder. Used to record the spatial/orientational position of the sample within the holder or setup. Different sample holders might get new names, or one-off sample holders might have a temporary ID.//Die Position der Probe (ID) im Probenhalter. Sie dient zur Erfassung der räumlichen/orientierungsmäßigen Position der Probe innerhalb des Halters oder der Versuchsanordnung. Verschiedene Probenhalter können unterschiedliche Namen erhalten, oder einmalige Probenhalter können eine temporäre ID haben.""",
        mandatory=False,
        show_in_edit_views=True,
        section="Experiment Details",
    )

    measurement_protocol_file = PropertyTypeAssignment(
        code="MEASUREMENT_PROTOCOL_FILE",
        data_type="MULTILINE_VARCHAR",
        property_label="Measurement Protocol // Messprotokoll",
        description="""Location of the measurement script // Ort des Messprotokollskripts""",
        mandatory=False,
        show_in_edit_views=True,
        section="Experiment Details",
    )

    # TODO revisit this property when JSON is integrated in openBIS
    measurement_protocol_options = PropertyTypeAssignment(
        code="MEASUREMENT_PROTOCOL_OPTIONS",
        data_type="VARCHAR",
        property_label="Measurement protocol options // Messprotokolloptionen",
        description="""JSON with key-value combinations // JSON mit Schlüssel-Werte-Paaren""",
        mandatory=False,
        show_in_edit_views=True,
        section="Experiment Details",
    )

    size_thickness_in_millimeter = PropertyTypeAssignment(
        code="SIZE_THICKNESS_IN_MILLIMETER",
        data_type="REAL",
        property_label="Thickness [mm]",
        description="""Thickness in mm//Dicke in mm""",
        mandatory=False,
        show_in_edit_views=True,
        section="Data Processing",
    )

    processing_protocol_file = PropertyTypeAssignment(
        code="PROCESSING_PROTOCOL_FILE",
        data_type="MULTILINE_VARCHAR",
        property_label="Data processing protocol // Datenverarbeitungsprotokoll",
        description="""Location of the data processing protocol // Ort des Datenverarbeitungsprotokolls""",
        mandatory=False,
        show_in_edit_views=True,
        section="Data Processing",
    )
