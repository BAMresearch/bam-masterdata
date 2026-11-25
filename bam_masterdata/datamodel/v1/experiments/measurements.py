# AUTO-GENERATED CLASS HIERARCHY — DO NOT EDIT
#
# Measurement*
# ├── MicroscopyFractureSurface
# ├── VideoRecording
# ├── ProfileScan
# ├── LaserDiffPSD
# ├── MSBatch
# ├── FTIR
# ├── DLS
# ├── DCPD
# ├── SIMS
# ├── NMR
# ├── ThermographicMeasurement
# ├── ImageSeries
# ├── SEM
# ├── TEM
# ├── XRD
# │   └── PXRD
# ├── UVVis
# ├── SAXSMeasurement
# │   └── MouseMeasurement
# └── ThermalAnalysis
#     ├── DSC
#     └── TGA
#
# END AUTO-GENERATED CLASS HIERARCHY

from bam_masterdata.datamodel.v1.activities import Measurement
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment


class MicroscopyFractureSurface(Measurement):
    defs = ObjectTypeDef(
        code="MICROSCOPY_FRACTURE_SURFACE",
        description="A MicroscopyFractureSurface is a measurement that determines a "
        "crack length optically on the fracture surface of a fatigue crack "
        "growth (FCG) specimen.",
        generated_code_prefix="MIC_FRAC_SURF",
        prev_versions=[
            "EXPERIMENTAL_STEP.MICROSCOPY_FCG_FRACTURE_SURFACE_CRACKLENGTH:v0"
        ],
    )

    mic_fcg_fracsurf_cracklength_type = PropertyTypeAssignment(
        code="MIC_FCG_FRACSURF_CRACKLENGTH_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="MICROSCOPY_FCG_CRACKLENGTH_TYPE",
        property_label="Type of Cracklength measured on Fracture Surface",
        description="Type of Cracklength measured on Fracture Surface",
        mandatory=False,
        section="Experimental Details",
        prev_versions=["MIC_FCG_FRACSURF_CRACKLENGTH_TYPE:v0"],
    )

    mic_fcg_fracsurf_cracklength_value = PropertyTypeAssignment(
        code="MIC_FCG_FRACSURF_CRACKLENGTH_VALUE",
        data_type="REAL",
        property_label="Value of Cracklength measured on Fracture Surface",
        units="mm",
        description="Value of Cracklength measured on Fracture Surface [mm]",
        mandatory=False,
        section="Experimental Details",
        prev_versions=["MIC_FCG_FRACSURF_CRACKLENGTH_VALUE:v0"],
    )

    mic_fcg_fracsurf_cracklength_cycles = PropertyTypeAssignment(
        code="MIC_FCG_FRACSURF_CRACKLENGTH_CYCLES",
        data_type="INTEGER",
        property_label="Cycle Count corresponding with Cracklength measured on Fracture Surface",
        description="Cycle Count corresponding with Cracklength measured on Fracture "
        "Surface",
        mandatory=False,
        section="Experimental Details",
        prev_versions=["MIC_FCG_FRACSURF_CRACKLENGTH_CYCLES:v0"],
    )


class VideoRecording(Measurement):
    defs = ObjectTypeDef(
        code="VIDEO_RECORDING",
        description="A VideoRecording is a measurement that records a sequence of "
        "images as a video.",
        generated_code_prefix="VIDEO_REC",
        prev_versions=["EXPERIMENTAL_STEP.VIDEO_RECORDING:v0"],
    )

    uuid = PropertyTypeAssignment(
        code="UUID",
        data_type="VARCHAR",
        property_label="UUID",
        description="A Universally Unique IDentifier (UUID/GUID) according to RFC 4122",
        mandatory=False,
        section="Identifiers",
        prev_versions=["UUID:v0"],
    )

    image_horizontal_resolution = PropertyTypeAssignment(
        code="IMAGE_HORIZONTAL_RESOLUTION",
        data_type="INTEGER",
        property_label="Horizontal resolution",
        units="pixels",
        description="Horizontal resolution of the image [pixel]",
        mandatory=False,
        section="Video Information",
        prev_versions=["IMAGE_HORIZONTAL_RESOLUTION:v0"],
    )

    image_vertical_resolution = PropertyTypeAssignment(
        code="IMAGE_VERTICAL_RESOLUTION",
        data_type="INTEGER",
        property_label="Vertical resolution",
        units="pixels",
        description="Vertical resolution of the image [pixel]",
        mandatory=False,
        section="Video Information",
        prev_versions=["IMAGE_VERTICAL_RESOLUTION:v0"],
    )

    video_frame_per_seconds = PropertyTypeAssignment(
        code="VIDEO_FRAME_PER_SECONDS",
        data_type="INTEGER",
        property_label="Average video framerate (frames per second)",
        description="Average video framerate [frames per second]",
        mandatory=False,
        section="Video Information",
        prev_versions=["VIDEO_FRAME_PER_SECONDS:v0"],
    )

    video_codec = PropertyTypeAssignment(
        code="VIDEO_CODEC",
        data_type="VARCHAR",
        property_label="Video codec used during recording",
        description="Video codec used during recording (if applicable)",
        mandatory=False,
        section="Video Information",
        prev_versions=["VIDEO_CODEC:v0"],
    )

    video_dynamic_framerate = PropertyTypeAssignment(
        code="VIDEO_DYNAMIC_FRAMERATE",
        data_type="BOOLEAN",
        property_label="Dynamic video frame rate",
        description="Flag to indicate that the video frame rate varies over time",
        mandatory=False,
        section="Video Information",
        prev_versions=["VIDEO_DYNAMIC_FRAMERATE:v0"],
    )

    camera_shutter_mode = PropertyTypeAssignment(
        code="CAMERA_SHUTTER_MODE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CAMERA_SHUTTER_MODE",
        property_label="Shutter mode",
        description="The shutter mode used for video recording",
        mandatory=False,
        section="Video Information",
        prev_versions=["CAMERA_SHUTTER_MODE:v0"],
    )


class ProfileScan(Measurement):
    defs = ObjectTypeDef(
        code="PROFILE_SCAN",
        description="A ProfileScan is a measurement that records a series of 2D line "
        "sensor readings.",
        generated_code_prefix="PROFILE_SCAN",
        prev_versions=["EXPERIMENTAL_STEP.PROFILE_SCAN:v0"],
    )

    uuid = PropertyTypeAssignment(
        code="UUID",
        data_type="VARCHAR",
        property_label="UUID",
        description="A Universally Unique IDentifier (UUID/GUID) according to RFC 4122",
        mandatory=False,
        section="Identifiers",
        prev_versions=["UUID:v0"],
    )

    scan_line_count = PropertyTypeAssignment(
        code="SCAN_LINE_COUNT",
        data_type="INTEGER",
        property_label="Scan line count",
        description="Number of individual scan lines recorded",
        mandatory=False,
        section="Scan Information",
        prev_versions=["SCAN_LINE_COUNT:v0"],
    )

    scan_line_resolution = PropertyTypeAssignment(
        code="SCAN_LINE_RESOLUTION",
        data_type="INTEGER",
        property_label="Scan line resolution",
        units="pixels",
        description="Number of pixels recorded for each scan line",
        mandatory=False,
        section="Scan Information",
        prev_versions=["SCAN_LINE_RESOLUTION:v0"],
    )


class LaserDiffPSD(Measurement):
    defs = ObjectTypeDef(
        code="LASER_DIFF_PSD",
        description="A LaserDiffPSD is a measurement that determines the particle size "
        "distribution (PSD) of a sample by laser diffraction.",
        generated_code_prefix="LD_PSD",
        prev_versions=["EXPERIMENTAL_STEP.LASER_DIFF_PSD_MEASUREMENT:v0"],
    )

    measurement_id = PropertyTypeAssignment(
        code="MEASUREMENT_ID",
        data_type="INTEGER",
        property_label="Measurement ID",
        description="Div. internal measurement ID",
        mandatory=False,
        section="General Information",
        prev_versions=["MEASUREMENT_ID:v0"],
    )

    dispersing_medium = PropertyTypeAssignment(
        code="DISPERSING_MEDIUM",
        data_type="VARCHAR",
        property_label="Dispersing medium",
        description="Medium in which the particles are dispersed for the measurement. "
        "Could be a liquid solvent (water, ethanol) or air. If the solvent "
        "contains additional dispersing agent, the respective type and "
        "concentration can also be stored in this field.",
        mandatory=True,
        section="Experimental Details",
        prev_versions=["DISPERSING_MEDIUM:v0"],
    )

    scattering_model_psd_ld = PropertyTypeAssignment(
        code="SCATTERING_MODEL_PSD_LD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="SCATTERING_MODEL_PSD_LD",
        property_label="Light scattering model",
        description="Light scattering model for the analysis of particle size by laser "
        "diffraction methods according to ISO 13220. Could be Mie or "
        "Fraunhofer, depending on the actual particle size.",
        mandatory=True,
        section="Experimental Details",
        prev_versions=["SCATTERING_MODEL_PSD_LD:v0"],
    )

    name_optical_parameterset_sample = PropertyTypeAssignment(
        code="NAME_OPTICAL_PARAMETERSET_SAMPLE",
        data_type="VARCHAR",
        property_label="Optical parameters designation",
        description="Designation of the dataset of optical parameters of the sample",
        mandatory=False,
        section="Experimental Details",
        prev_versions=["NAME_OPTICAL_PARAMETERSET_SAMPLE:v0"],
    )

    refractive_index_sample = PropertyTypeAssignment(
        code="REFRACTIVE_INDEX_SAMPLE",
        data_type="REAL",
        property_label="Refractive index of sample",
        description="Refractive index of the sample",
        mandatory=False,
        section="Experimental Details",
        prev_versions=["REFRACTIVE_INDEX_SAMPLE:v0"],
    )

    absorption_coeff_sample = PropertyTypeAssignment(
        code="ABSORPTION_COEFF_SAMPLE",
        data_type="REAL",
        property_label="Absorption coefficient of sample",
        description="Absorption coefficient of the sample for blue light, if the "
        "measuring device has such a second light source",
        mandatory=False,
        section="Experimental Details",
        prev_versions=["ABSORPTION_COEFF_SAMPLE:v0"],
    )

    refractive_index_blue_sample = PropertyTypeAssignment(
        code="REFRACTIVE_INDEX_BLUE_SAMPLE",
        data_type="REAL",
        property_label="Refractive index for blue light of sample",
        description="Refractive index of the sample for blue light, if the measuring "
        "device has such a second light source",
        mandatory=False,
        section="Experimental Details",
        prev_versions=["REFRACTIVE_INDEX_BLUE_SAMPLE:v0"],
    )

    absorption_coeff_blue_sample = PropertyTypeAssignment(
        code="ABSORPTION_COEFF_BLUE_SAMPLE",
        data_type="REAL",
        property_label="Absorption coefficient for blue light of sample",
        description="Absorption coefficient of the sample for blue light",
        mandatory=False,
        section="Experimental Details",
        prev_versions=["ABSORPTION_COEFF_BLUE_SAMPLE:v0"],
    )

    laser_obscuration = PropertyTypeAssignment(
        code="LASER_OBSCURATION",
        data_type="REAL",
        property_label="Laser obscuration",
        description="Laser obscuration",
        mandatory=False,
        section="Results",
        prev_versions=["LASER_OBSCURATION:v0"],
    )

    laser_transmission = PropertyTypeAssignment(
        code="LASER_TRANSMISSION",
        data_type="REAL",
        property_label="Laser transmission",
        description="Laser transmission",
        mandatory=False,
        section="Results",
        prev_versions=["LASER_TRANSMISSION:v0"],
    )

    weighted_deviation = PropertyTypeAssignment(
        code="WEIGHTED_DEVIATION",
        data_type="REAL",
        property_label="Weighted deviation of fit",
        description="In the context of fitted data, the weighted deviation describes "
        "how much the individual measurement points deviate from the curve "
        "predicted by the model, taking into account their respective "
        "weights (e.g. uncertainties or relevance).",
        mandatory=False,
        section="Results",
        prev_versions=["WEIGHTED_DEVIATION:v0"],
    )

    absolute_deviation = PropertyTypeAssignment(
        code="ABSOLUTE_DEVIATION",
        data_type="REAL",
        property_label="Absolute deviation of fit",
        description="The absolute deviation for fitted data describes the sum (or mean "
        "value) of the differences in magnitude between the measured "
        "values and the values predicted by the model without squaring and "
        "without weighting.",
        mandatory=False,
        section="Results",
        prev_versions=["ABSOLUTE_DEVIATION:v0"],
    )

    meas_medium_temperature = PropertyTypeAssignment(
        code="MEAS_MEDIUM_TEMPERATURE",
        data_type="REAL",
        property_label="Temperature of dispersing medium",
        units="celsius",
        description="Temperature of measurement medium in °C",
        mandatory=False,
        section="Results",
        prev_versions=["MEAS_MEDIUM_TEMPERATURE_IN_CELSIUS:v0"],
    )

    d_10 = PropertyTypeAssignment(
        code="D_10",
        data_type="REAL",
        property_label="Particle size D_10",
        units="micrometer",
        description="Particle size D_10 in µm",
        mandatory=False,
        section="Results",
        prev_versions=["D_10_IN_MICROMETERS:v0"],
    )

    d_50 = PropertyTypeAssignment(
        code="D_50",
        data_type="REAL",
        property_label="Particle size D_50",
        units="micrometer",
        description="Particle size D_50 in µm",
        mandatory=True,
        section="Results",
        prev_versions=["D_50_IN_MICROMETERS:v0"],
    )

    d_90 = PropertyTypeAssignment(
        code="D_90",
        data_type="REAL",
        property_label="Particle size D_90",
        units="micrometer",
        description="Particle size D_90 in µm",
        mandatory=False,
        section="Results",
        prev_versions=["D_90_IN_MICROMETERS:v0"],
    )

    mode_count = PropertyTypeAssignment(
        code="MODE_COUNT",
        data_type="INTEGER",
        property_label="Number of modes",
        description="Number of modes",
        mandatory=False,
        section="Results",
        prev_versions=["MODE_COUNT:v0"],
    )

    # v0 properties of EXPERIMENTAL_STEP.LASER_DIFF_PSD_MEASUREMENT not redefined here:
    # SAMPLE_ID: already migrated to v1 Sample (SAMPLE_ID); link the sample via Activity INPUT


class MSBatch(Measurement):
    defs = ObjectTypeDef(
        code="MS_BATCH",
        description="An MSBatch is a measurement that records mass spectrometry (MS) "
        "data for a batch of samples.",
        generated_code_prefix="MS_BATCH",
        prev_versions=["EXPERIMENTAL_STEP.MS_BATCH:v0"],
    )

    ms_resolution = PropertyTypeAssignment(
        code="MS_RESOLUTION",
        data_type="REAL",
        property_label="Resolution",
        description="Approximate mass resolving power (m/Δm). Indicates the ability to "
        "separate two closely spaced m/z peaks; higher values mean better "
        "peak separation. Resolution depends on instrument type and "
        "measured mass.",
        mandatory=False,
        section="MS Parameters",
        prev_versions=["MS_RESOLUTION:v0"],
    )

    ms_intensity_range = PropertyTypeAssignment(
        code="MS_INTENSITY_RANGE",
        data_type="VARCHAR",
        property_label="Intensity range",
        description="Ion intensity range in [min-max]",
        mandatory=False,
        section="MS Parameters",
        prev_versions=["MS_INTENSITY_RANGE:v0"],
    )

    ms_scan_rate = PropertyTypeAssignment(
        code="MS_SCAN_RATE",
        data_type="REAL",
        property_label="Scan rate",
        units="Hz",
        description="Sample scan rate in [Hz]",
        mandatory=False,
        section="MS Parameters",
        prev_versions=["MS_SCAN_RATE:v0"],
    )

    ms_acquisition_mode = PropertyTypeAssignment(
        code="MS_ACQUISITION_MODE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="MS_ACQUISITION_MODE",
        property_label="Aquisition mode",
        description="Aquisition mode",
        mandatory=False,
        section="MS Parameters",
        prev_versions=["MS_ACQUISITION_MODE:v0"],
    )

    ms_ion_polarity = PropertyTypeAssignment(
        code="MS_ION_POLARITY",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="MS_ION_POLARITY",
        property_label="Polarity",
        description="Ionization Polarity",
        mandatory=False,
        section="MS Parameters",
        prev_versions=["MS_ION_POLARITY:v0"],
    )

    ms_mass_range = PropertyTypeAssignment(
        code="MS_MASS_RANGE",
        data_type="VARCHAR",
        property_label="Mass range",
        description="Sample mass range in [min-max]",
        mandatory=False,
        section="MS Parameters",
        prev_versions=["MS_MASS_RANGE:v0"],
    )


class FTIR(Measurement):
    defs = ObjectTypeDef(
        code="FTIR",
        description="An FTIR is a measurement that records the infrared spectrum of a "
        "sample by Fourier-transform infrared spectroscopy.",
        generated_code_prefix="FTIR",
        prev_versions=["EXPERIMENTAL_STEP.FTIR:v0"],
    )

    ftir_instrument = PropertyTypeAssignment(
        code="FTIR_INSTRUMENT",
        data_type="VARCHAR",
        property_label="Instrument",
        description="FT-IR Instrument",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["FTIR.INSTRUMENT:v0"],
    )

    ftir_start_wavenumber = PropertyTypeAssignment(
        code="FTIR_START_WAVENUMBER",
        data_type="REAL",
        property_label="Start Wavenumber",
        units="1/cm",
        description="Start Wavenumber [1/cm]",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["FTIR.START_WAVENUMBER:v0"],
    )

    ftir_end_wavenumber = PropertyTypeAssignment(
        code="FTIR_END_WAVENUMBER",
        data_type="REAL",
        property_label="End Wavenumber",
        units="1/cm",
        description="End Wavenumber [1/cm]",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["FTIR.END_WAVENUMBER:v0"],
    )

    ftir_resolution = PropertyTypeAssignment(
        code="FTIR_RESOLUTION",
        data_type="INTEGER",
        property_label="Resolution",
        units="1/cm",
        description="Resolution [1/cm]",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["FTIR.RESOLUTION:v0"],
    )

    ftir_scans = PropertyTypeAssignment(
        code="FTIR_SCANS",
        data_type="INTEGER",
        property_label="Number of Scans",
        description="Number of FTIR Scans",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["FTIR.SCANS:v0"],
    )

    ftir_accessory = PropertyTypeAssignment(
        code="FTIR_ACCESSORY",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="FTIR_ACCESSORIES",
        property_label="Accessory",
        description="FTIR Accessory",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["FTIR.ACCESSORY:v0"],
    )

    ftir_is_flushed = PropertyTypeAssignment(
        code="FTIR_IS_FLUSHED",
        data_type="BOOLEAN",
        property_label="Flushed with Nitrogen",
        description="Flushed with Nitrogen",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["FTIR.IS_FLUSHED:v0"],
    )


class DLS(Measurement):
    defs = ObjectTypeDef(
        code="DLS",
        description="A DLS is a measurement that determines the size distribution and "
        "zeta potential of particles in a dispersion by dynamic and "
        "electrophoretic light scattering.",
        generated_code_prefix="DLS",
        prev_versions=["EXPERIMENTAL_STEP.DLS:v0"],
    )

    dls_material = PropertyTypeAssignment(
        code="DLS_MATERIAL",
        data_type="VARCHAR",
        property_label="Material Name",
        description="Material Name for DLS Measurement",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["DLS.MATERIAL:v0"],
    )

    dls_dispersant = PropertyTypeAssignment(
        code="DLS_DISPERSANT",
        data_type="VARCHAR",
        property_label="Dispersant",
        description="Dispersant for DLS Measurement",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["DLS.DISPERSANT:v0"],
    )

    dls_temperature = PropertyTypeAssignment(
        code="DLS_TEMPERATURE",
        data_type="REAL",
        property_label="Temperature",
        units="celsius",
        description="Temperature [°C]",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["DLS.TEMPERATURE:v0"],
    )

    dls_celldescription = PropertyTypeAssignment(
        code="DLS_CELLDESCRIPTION",
        data_type="VARCHAR",
        property_label="Cell Description",
        description="DLS Cell Description",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["DLS.CELLDESCRIPTION:v0"],
    )

    dls_attenuator = PropertyTypeAssignment(
        code="DLS_ATTENUATOR",
        data_type="INTEGER",
        property_label="Attenuator",
        description="Attenuator for DLS Measurement",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["DLS.ATTENUATOR:v0"],
    )

    dls_zavg = PropertyTypeAssignment(
        code="DLS_ZAVG",
        data_type="REAL",
        property_label="Z-Average",
        description="Z-Average",
        mandatory=False,
        section="Measurement Results",
        prev_versions=["DLS.ZAVG:v0"],
    )

    dls_pdi = PropertyTypeAssignment(
        code="DLS_PDI",
        data_type="REAL",
        property_label="PDI",
        description="Polydispersity Index",
        mandatory=False,
        section="Measurement Results",
        prev_versions=["DLS.PDI:v0"],
    )

    dls_zeta = PropertyTypeAssignment(
        code="DLS_ZETA",
        data_type="REAL",
        property_label="Zeta Potential",
        units="mV",
        description="Zeta Potential [mV]",
        mandatory=False,
        section="Measurement Results",
        prev_versions=["DLS.ZETA:v0"],
    )

    dls_pk1int = PropertyTypeAssignment(
        code="DLS_PK1INT",
        data_type="REAL",
        property_label="Peak 1 (Intensity)",
        units="nm",
        description="Peak 1 (Intensity) [nm]",
        mandatory=False,
        section="Measurement Results (Intensity Distribution)",
        prev_versions=["DLS.PK1INT:v0"],
    )

    dls_pk1intwidth = PropertyTypeAssignment(
        code="DLS_PK1INTWIDTH",
        data_type="REAL",
        property_label="Peak 1 Width (Intensity)",
        units="nm",
        description="Peak 1 Width (Intensity) [nm]",
        mandatory=False,
        section="Measurement Results (Intensity Distribution)",
        prev_versions=["DLS.PK1INTWIDTH:v0"],
    )

    dls_pk1intpd = PropertyTypeAssignment(
        code="DLS_PK1INTPD",
        data_type="REAL",
        property_label="Peak 1 Polydispersity (Intensity)",
        description="Peak 1 Polydispersity (Intensity)",
        mandatory=False,
        section="Measurement Results (Intensity Distribution)",
        prev_versions=["DLS.PK1INTPD:v0"],
    )

    dls_pk2int = PropertyTypeAssignment(
        code="DLS_PK2INT",
        data_type="REAL",
        property_label="Peak 2 (Intensity)",
        units="nm",
        description="Peak 2 (Intensity) [nm]",
        mandatory=False,
        section="Measurement Results (Intensity Distribution)",
        prev_versions=["DLS.PK2INT:v0"],
    )

    dls_pk2intwidth = PropertyTypeAssignment(
        code="DLS_PK2INTWIDTH",
        data_type="REAL",
        property_label="Peak 2 Width (Intensity)",
        units="nm",
        description="Peak 2 Width (Intensity) [nm]",
        mandatory=False,
        section="Measurement Results (Intensity Distribution)",
        prev_versions=["DLS.PK2INTWIDTH:v0"],
    )

    dls_pk2intpd = PropertyTypeAssignment(
        code="DLS_PK2INTPD",
        data_type="REAL",
        property_label="Peak 2 Polydispersity (Intensity)",
        description="Peak 2 Polydispersity (Intensity)",
        mandatory=False,
        section="Measurement Results (Intensity Distribution)",
        prev_versions=["DLS.PK2INTPD:v0"],
    )

    dls_pk3int = PropertyTypeAssignment(
        code="DLS_PK3INT",
        data_type="REAL",
        property_label="Peak 3 (Intensity)",
        units="nm",
        description="Peak 3 (Intensity) [nm]",
        mandatory=False,
        section="Measurement Results (Intensity Distribution)",
        prev_versions=["DLS.PK3INT:v0"],
    )

    dls_pk3intwidth = PropertyTypeAssignment(
        code="DLS_PK3INTWIDTH",
        data_type="REAL",
        property_label="Peak 3 Width (Intensity)",
        units="nm",
        description="Peak 3 Width (Intensity) [nm]",
        mandatory=False,
        section="Measurement Results (Intensity Distribution)",
        prev_versions=["DLS.PK3INTWIDTH:v0"],
    )

    dls_pk3intpd = PropertyTypeAssignment(
        code="DLS_PK3INTPD",
        data_type="REAL",
        property_label="Peak 3 Polydispersity (Intensity)",
        description="Peak 3 Polydispersity (Intensity)",
        mandatory=False,
        section="Measurement Results (Intensity Distribution)",
        prev_versions=["DLS.PK3INTPD:v0"],
    )

    dls_pk1vol = PropertyTypeAssignment(
        code="DLS_PK1VOL",
        data_type="REAL",
        property_label="Peak 1 (Volume)",
        units="nm",
        description="Peak 1 (Volume) [nm]",
        mandatory=False,
        section="Measurement Results (Volume Distribution)",
        prev_versions=["DLS.PK1VOL:v0"],
    )

    dls_pk1volwidth = PropertyTypeAssignment(
        code="DLS_PK1VOLWIDTH",
        data_type="REAL",
        property_label="Peak 1 Width (Volume)",
        units="nm",
        description="Peak 1 Width (Volume) [nm]",
        mandatory=False,
        section="Measurement Results (Volume Distribution)",
        prev_versions=["DLS.PK1VOLWIDTH:v0"],
    )

    dls_pk1volpd = PropertyTypeAssignment(
        code="DLS_PK1VOLPD",
        data_type="REAL",
        property_label="Peak 1 Polydispersity (Volume)",
        description="Peak 1 Polydispersity (Volume)",
        mandatory=False,
        section="Measurement Results (Volume Distribution)",
        prev_versions=["DLS.PK1VOLPD:v0"],
    )

    dls_pk2vol = PropertyTypeAssignment(
        code="DLS_PK2VOL",
        data_type="REAL",
        property_label="Peak 2 (Volume)",
        units="nm",
        description="Peak 2 (Volume) [nm]",
        mandatory=False,
        section="Measurement Results (Volume Distribution)",
        prev_versions=["DLS.PK2VOL:v0"],
    )

    dls_pk2volwidth = PropertyTypeAssignment(
        code="DLS_PK2VOLWIDTH",
        data_type="REAL",
        property_label="Peak 2 Width (Volume)",
        units="nm",
        description="Peak 2 Width (Volume) [nm]",
        mandatory=False,
        section="Measurement Results (Volume Distribution)",
        prev_versions=["DLS.PK2VOLWIDTH:v0"],
    )

    dls_pk2volpd = PropertyTypeAssignment(
        code="DLS_PK2VOLPD",
        data_type="REAL",
        property_label="Peak 2 Polydispersity (Volume)",
        description="Peak 2 Polydispersity (Volume)",
        mandatory=False,
        section="Measurement Results (Volume Distribution)",
        prev_versions=["DLS.PK2VOLPD:v0"],
    )

    dls_pk3vol = PropertyTypeAssignment(
        code="DLS_PK3VOL",
        data_type="REAL",
        property_label="Peak 3 (Volume)",
        units="nm",
        description="Peak 3 (Volume) [nm]",
        mandatory=False,
        section="Measurement Results (Volume Distribution)",
        prev_versions=["DLS.PK3VOL:v0"],
    )

    dls_pk3volwidth = PropertyTypeAssignment(
        code="DLS_PK3VOLWIDTH",
        data_type="REAL",
        property_label="Peak 3 Width (Volume)",
        units="nm",
        description="Peak 3 Width (Volume) [nm]",
        mandatory=False,
        section="Measurement Results (Volume Distribution)",
        prev_versions=["DLS.PK3VOLWIDTH:v0"],
    )

    dls_pk3volpd = PropertyTypeAssignment(
        code="DLS_PK3VOLPD",
        data_type="REAL",
        property_label="Peak 3 Polydispersity (Volume)",
        description="Peak 3 Polydispersity (Volume)",
        mandatory=False,
        section="Measurement Results (Volume Distribution)",
        prev_versions=["DLS.PK3VOLPD:v0"],
    )

    dls_pk1num = PropertyTypeAssignment(
        code="DLS_PK1NUM",
        data_type="REAL",
        property_label="Peak 1 (Number)",
        units="nm",
        description="Peak 1 (Number) [nm]",
        mandatory=False,
        section="Measurement Results (Number Distribution)",
        prev_versions=["DLS.PK1NUM:v0"],
    )

    dls_pk1numwidth = PropertyTypeAssignment(
        code="DLS_PK1NUMWIDTH",
        data_type="REAL",
        property_label="Peak 1 Width (Number)",
        units="nm",
        description="Peak 1 Width (Number) [nm]",
        mandatory=False,
        section="Measurement Results (Number Distribution)",
        prev_versions=["DLS.PK1NUMWIDTH:v0"],
    )

    dls_pk1numpd = PropertyTypeAssignment(
        code="DLS_PK1NUMPD",
        data_type="REAL",
        property_label="Peak 1 Polydispersity (Number)",
        description="Peak 1 Polydispersity (Number)",
        mandatory=False,
        section="Measurement Results (Number Distribution)",
        prev_versions=["DLS.PK1NUMPD:v0"],
    )

    dls_pk2num = PropertyTypeAssignment(
        code="DLS_PK2NUM",
        data_type="REAL",
        property_label="Peak 2 (Number)",
        units="nm",
        description="Peak 2 (Number) [nm]",
        mandatory=False,
        section="Measurement Results (Number Distribution)",
        prev_versions=["DLS.PK2NUM:v0"],
    )

    dls_pk2numwidth = PropertyTypeAssignment(
        code="DLS_PK2NUMWIDTH",
        data_type="REAL",
        property_label="Peak 2 Width (Number)",
        units="nm",
        description="Peak 2 Width (Number) [nm]",
        mandatory=False,
        section="Measurement Results (Number Distribution)",
        prev_versions=["DLS.PK2NUMWIDTH:v0"],
    )

    dls_pk2numpd = PropertyTypeAssignment(
        code="DLS_PK2NUMPD",
        data_type="REAL",
        property_label="Peak 2 Polydispersity (Number)",
        description="Peak 2 Polydispersity (Number)",
        mandatory=False,
        section="Measurement Results (Number Distribution)",
        prev_versions=["DLS.PK2NUMPD:v0"],
    )

    dls_pk3num = PropertyTypeAssignment(
        code="DLS_PK3NUM",
        data_type="REAL",
        property_label="Peak 3 (Number)",
        units="nm",
        description="Peak 3 (Number) [nm]",
        mandatory=False,
        section="Measurement Results (Number Distribution)",
        prev_versions=["DLS.PK3NUM:v0"],
    )

    dls_pk3numwidth = PropertyTypeAssignment(
        code="DLS_PK3NUMWIDTH",
        data_type="REAL",
        property_label="Peak 3 Width (Number)",
        units="nm",
        description="Peak 3 Width (Number) [nm]",
        mandatory=False,
        section="Measurement Results (Number Distribution)",
        prev_versions=["DLS.PK3NUMWIDTH:v0"],
    )

    dls_pk3numpd = PropertyTypeAssignment(
        code="DLS_PK3NUMPD",
        data_type="REAL",
        property_label="Peak 3 Polydispersity (Number)",
        description="Peak 3 Polydispersity (Number)",
        mandatory=False,
        section="Measurement Results (Number Distribution)",
        prev_versions=["DLS.PK3NUMPD:v0"],
    )

    dls_pk1zeta = PropertyTypeAssignment(
        code="DLS_PK1ZETA",
        data_type="REAL",
        property_label="Peak 1 (Zeta)",
        units="mV",
        description="Peak 1 (Zetapotential) [mV]",
        mandatory=False,
        section="Measurement Results (Zeta Potential)",
        prev_versions=["DLS.PK1ZETA:v0"],
    )

    dls_pk1zetawidth = PropertyTypeAssignment(
        code="DLS_PK1ZETAWIDTH",
        data_type="REAL",
        property_label="Peak 1 Width (Zeta)",
        units="mV",
        description="Peak 1 Width (Zetapotential) [mV]",
        mandatory=False,
        section="Measurement Results (Zeta Potential)",
        prev_versions=["DLS.PK1ZETAWIDTH:v0"],
    )

    dls_pk2zeta = PropertyTypeAssignment(
        code="DLS_PK2ZETA",
        data_type="REAL",
        property_label="Peak 2 (Zeta)",
        units="mV",
        description="Peak 2 (Zetapotential) [mV]",
        mandatory=False,
        section="Measurement Results (Zeta Potential)",
        prev_versions=["DLS.PK2ZETA:v0"],
    )

    dls_pk2zetawidth = PropertyTypeAssignment(
        code="DLS_PK2ZETAWIDTH",
        data_type="REAL",
        property_label="Peak 2 Width (Zeta)",
        units="mV",
        description="Peak 2 Width (Zetapotential) [mV]",
        mandatory=False,
        section="Measurement Results (Zeta Potential)",
        prev_versions=["DLS.PK2ZETAWIDTH:v0"],
    )

    dls_pk3zeta = PropertyTypeAssignment(
        code="DLS_PK3ZETA",
        data_type="REAL",
        property_label="Peak 3 (Zeta)",
        units="mV",
        description="Peak 3 (Zetapotential) [mV]",
        mandatory=False,
        section="Measurement Results (Zeta Potential)",
        prev_versions=["DLS.PK3ZETA:v0"],
    )

    dls_pk3zetawidth = PropertyTypeAssignment(
        code="DLS_PK3ZETAWIDTH",
        data_type="REAL",
        property_label="Peak 3 Width (Zeta)",
        units="mV",
        description="Peak 3 Width (Zetapotential) [mV]",
        mandatory=False,
        section="Measurement Results (Zeta Potential)",
        prev_versions=["DLS.PK3ZETAWIDTH:v0"],
    )

    dls_analysismodel = PropertyTypeAssignment(
        code="DLS_ANALYSISMODEL",
        data_type="VARCHAR",
        property_label="Analysis Model",
        description="Analysis Model",
        mandatory=False,
        section="Measurement Information",
        prev_versions=["DLS.ANALYSISMODEL:v0"],
    )

    dls_intercept = PropertyTypeAssignment(
        code="DLS_INTERCEPT",
        data_type="REAL",
        property_label="Measured Intercept",
        description="Measured Intercept",
        mandatory=False,
        section="Measurement Information",
        prev_versions=["DLS.INTERCEPT:v0"],
    )

    dls_sizemerit = PropertyTypeAssignment(
        code="DLS_SIZEMERIT",
        data_type="REAL",
        property_label="Size Merit",
        description="Size Merit",
        mandatory=False,
        section="Measurement Information",
        prev_versions=["DLS.SIZEMERIT:v0"],
    )

    dls_cumulantsfiterror = PropertyTypeAssignment(
        code="DLS_CUMULANTSFITERROR",
        data_type="REAL",
        property_label="Cumulants Fit Error",
        description="Cumulants Fit Error",
        mandatory=False,
        section="Measurement Information",
        prev_versions=["DLS.CUMULANTSFITERROR:v0"],
    )

    dls_multimodalfiterror = PropertyTypeAssignment(
        code="DLS_MULTIMODALFITERROR",
        data_type="REAL",
        property_label="Multimodal Fit Error",
        description="Multimodal Fit Error",
        mandatory=False,
        section="Measurement Information",
        prev_versions=["DLS.MULTIMODALFITERROR:v0"],
    )

    dls_fkamodel = PropertyTypeAssignment(
        code="DLS_FKAMODEL",
        data_type="VARCHAR",
        property_label="Fka Model",
        description="Fka Model",
        mandatory=False,
        section="Measurement Information",
        prev_versions=["DLS.FKAMODEL:v0"],
    )

    dls_volt = PropertyTypeAssignment(
        code="DLS_VOLT",
        data_type="REAL",
        property_label="Measured Voltage",
        units="V",
        description="Measured Voltage [V]",
        mandatory=False,
        section="Measurement Information",
        prev_versions=["DLS.VOLT:v0"],
    )

    dls_cond = PropertyTypeAssignment(
        code="DLS_COND",
        data_type="REAL",
        property_label="Conductivity",
        units="mS/cm",
        description="Conductivity [mS/cm]",
        mandatory=False,
        section="Measurement Information",
        prev_versions=["DLS.COND:v0"],
    )


class DCPD(Measurement):
    defs = ObjectTypeDef(
        code="DCPD",
        description="A DCPD is a measurement that monitors the crack length in a "
        "specimen from the drop in electrical potential under a direct "
        "current (direct current potential drop method).",
        generated_code_prefix="DCPD",
        prev_versions=["EXPERIMENTAL_STEP.DCPD:v0"],
    )

    dcpd_pot_drop_cal = PropertyTypeAssignment(
        code="DCPD_POT_DROP_CAL",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DCPD_POT_CAL",
        property_label="Potential Drop Calibration",
        description="Potential Drop Calibration",
        mandatory=False,
        section="Setup",
        prev_versions=["DCPD_POT_DROP_CAL:v0"],
    )

    dcpd_current = PropertyTypeAssignment(
        code="DCPD_CURRENT",
        data_type="REAL",
        property_label="Current",
        units="A",
        description="DCPD Current [A]",
        mandatory=False,
        section="Setup",
        prev_versions=["DCPD_CURRENT:v0"],
    )

    dcpd_initial_cracklength = PropertyTypeAssignment(
        code="DCPD_INITIAL_CRACKLENGTH",
        data_type="REAL",
        property_label="Initial Cracklength (measured optically)",
        units="mm",
        description="Initial Cracklength (measured optically) [mm]",
        mandatory=False,
        section="Setup",
        prev_versions=["DCPD_INITIAL_CRACKLENGTH:v0"],
    )

    dcpd_yzero_fitted = PropertyTypeAssignment(
        code="DCPD_YZERO_FITTED",
        data_type="REAL",
        property_label="Y0 in Johnson Formula fitted for Notch Geometry",
        units="mm",
        description="Y0 in Johnson Formula fitted for Notch Geometry [mm]",
        mandatory=False,
        section="Setup",
        prev_versions=["DCPD_YZERO_FITTED:v0"],
    )

    fem_fit_eq = PropertyTypeAssignment(
        code="FEM_FIT_EQ",
        data_type="VARCHAR",
        property_label="Equation of FEM Fit a = f(U)",
        description="Equation of FEM Fit a = f(U)",
        mandatory=False,
        section="Setup",
        prev_versions=["FEM_FIT_EQ:v0"],
    )

    dcpd_proportional_potential = PropertyTypeAssignment(
        code="DCPD_PROPORTIONAL_POTENTIAL",
        data_type="BOOLEAN",
        property_label="Output Signal proportional to Potential Drop",
        description="Output Signal proportional to Potential Drop",
        mandatory=False,
        section="Direct Amplification of Corrected Potential Drop",
        prev_versions=["DCPD_PROPORTIONAL_POTENTIAL:v0"],
    )

    dcpd_initial_potential_drop = PropertyTypeAssignment(
        code="DCPD_INITIAL_POTENTIAL_DROP",
        data_type="REAL",
        property_label="Initial Potential Drop (amplified)",
        units="V",
        description="Initial Potential Drop (amplified) [V]",
        mandatory=False,
        section="Direct Amplification of Corrected Potential Drop",
        prev_versions=["DCPD_INITIAL_POTENTIAL_DROP:v0"],
    )

    dcpd_amplification_factor = PropertyTypeAssignment(
        code="DCPD_AMPLIFICATION_FACTOR",
        data_type="REAL",
        property_label="Amplification Factor",
        description="Amplification Factor",
        mandatory=False,
        section="Direct Amplification of Corrected Potential Drop",
        prev_versions=["DCPD_AMPLIFICATION_FACTOR:v0"],
    )

    dcpd_linearised_potential = PropertyTypeAssignment(
        code="DCPD_LINEARISED_POTENTIAL",
        data_type="BOOLEAN",
        property_label="Output Signal Proportional to Cracklength",
        description="Output Signal Proportional to Cracklength",
        mandatory=False,
        section="Output Potential Proportional to Cracklength",
        prev_versions=["DCPD_LINEARISED_POTENTIAL:v0"],
    )

    dcpd_temp_comp = PropertyTypeAssignment(
        code="DCPD_TEMP_COMP",
        data_type="BOOLEAN",
        property_label="Temperature Compensation",
        description="Temperature Compensation",
        mandatory=False,
        section="Temperature Compensation",
        prev_versions=["DCPD_TEMP_COMP:v0"],
    )

    dcpd_initial_temp = PropertyTypeAssignment(
        code="DCPD_INITIAL_TEMP",
        data_type="REAL",
        property_label="Initial Temperature",
        units="celsius",
        description="Initial Temperature [°C]",
        mandatory=False,
        section="Temperature Compensation",
        prev_versions=["DCPD_INITIAL_TEMP:v0"],
    )

    dcpd_temp_coeff = PropertyTypeAssignment(
        code="DCPD_TEMP_COEFF",
        data_type="REAL",
        property_label="Temperature Coefficient of Resistivity",
        units="1/delta_degC",
        description="Temperature Coefficient of Resistivity [°C^-1]",
        mandatory=False,
        section="Temperature Compensation",
        prev_versions=["DCPD_TEMP_COEFF:v0"],
    )


class SIMS(Measurement):
    defs = ObjectTypeDef(
        code="SIMS",
        description="A SIMS is a measurement that analyses a surface by time-of-flight "
        "secondary ion mass spectrometry (ToF-SIMS) in spectrometry, depth "
        "profiling or imaging mode.",
        generated_code_prefix="SIMS",
        prev_versions=["EXPERIMENTAL_STEP.SIMS:v0"],
    )

    customer = PropertyTypeAssignment(
        code="CUSTOMER",
        data_type="VARCHAR",
        property_label="Customer",
        description="Name of the person for whom the measurement is performed",
        mandatory=False,
        section="General Information",
        prev_versions=["CUSTOMER:v0"],
    )

    measurement_mode = PropertyTypeAssignment(
        code="MEASUREMENT_MODE",
        data_type="VARCHAR",
        property_label="Measurement Mode",
        description="Which measurement mode was used?",
        mandatory=False,
        section="Experimental Settings",
        prev_versions=["MEASUREMENT_MODE:v0"],
    )

    sims_primary_ion = PropertyTypeAssignment(
        code="SIMS_PRIMARY_ION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="SIMS_PRIMARY_ION",
        property_label="Primary Ion",
        description="Primary ion used for analysis",
        mandatory=False,
        section="Experimental Settings",
        prev_versions=["SIMS_PRIMARY_ION:v0"],
    )

    sims_polarity = PropertyTypeAssignment(
        code="SIMS_POLARITY",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="MS_ION_POLARITY",
        property_label="Polarity",
        description="Polarity",
        mandatory=False,
        section="Experimental Settings",
        prev_versions=["SIMS_POLARITY:v0"],
    )

    sims_lmig_current_dc = PropertyTypeAssignment(
        code="SIMS_LMIG_CURRENT_DC",
        data_type="REAL",
        property_label="LMIG Current DC",
        units="nA",
        description="LMIG Current direct current (DC) in nA",
        mandatory=False,
        section="Experimental Settings",
        prev_versions=["SIMS_LMIG_CURRENT_DC:v0"],
    )

    sims_lmig_current_p = PropertyTypeAssignment(
        code="SIMS_LMIG_CURRENT_P",
        data_type="REAL",
        property_label="LMIG Current P",
        units="pA",
        description="LMIG Current pulsed (P) in pA",
        mandatory=False,
        section="Experimental Settings",
        prev_versions=["SIMS_LMIG_CURRENT_P:v0"],
    )

    sims_lmig_pulse_width = PropertyTypeAssignment(
        code="SIMS_LMIG_PULSE_WIDTH",
        data_type="REAL",
        property_label="Primary ion beam pulse width",
        units="ns",
        description="Primary ion beam pulse width in ns",
        mandatory=False,
        section="Experimental Settings",
        prev_versions=["SIMS_LMIG_PULSE_WIDTH:v0"],
    )

    sims_lmig_raster_size = PropertyTypeAssignment(
        code="SIMS_LMIG_RASTER_SIZE",
        data_type="REAL",
        property_label="Primary ion beam raster size",
        units="micrometer",
        description="Primary ion beam raster size in µm",
        mandatory=False,
        section="Experimental Settings",
        prev_versions=["SIMS_LMIG_RASTER_SIZE:v0"],
    )

    charge_compensation = PropertyTypeAssignment(
        code="CHARGE_COMPENSATION",
        data_type="REAL",
        property_label="Charge compensation",
        units="V",
        description="Charge compensation in V",
        mandatory=False,
        section="Experimental Settings",
        prev_versions=["CHARGE_COMPENSATION:v0"],
    )

    delayed_extraction = PropertyTypeAssignment(
        code="DELAYED_EXTRACTION",
        data_type="BOOLEAN",
        property_label="Was delayed extraction used?",
        description="Indicates whether delayed extraction is used",
        mandatory=False,
        section="Experimental Settings",
        prev_versions=["DELAYED_EXTRACTION:v0"],
    )

    gas_flooding = PropertyTypeAssignment(
        code="GAS_FLOODING",
        data_type="BOOLEAN",
        property_label="Was gas flooding used?",
        description="Indicates whether gas flooding is used",
        mandatory=False,
        section="Experimental Settings",
        prev_versions=["GAS_FLOODING:v0"],
    )

    stop_condition = PropertyTypeAssignment(
        code="STOP_CONDITION",
        data_type="VARCHAR",
        property_label="Stop Condition",
        description="Stop condition for acquisition",
        mandatory=False,
        section="Experimental Settings",
        prev_versions=["STOP_CONDITION:v0"],
    )

    sputter_source = PropertyTypeAssignment(
        code="SPUTTER_SOURCE",
        data_type="VARCHAR",
        property_label="Sputter Source",
        description="Sputter Source",
        mandatory=False,
        section="Depth Profiling",
        prev_versions=["SPUTTER_SOURCE:v0"],
    )

    sims_dsc_voltage = PropertyTypeAssignment(
        code="SIMS_DSC_VOLTAGE",
        data_type="REAL",
        property_label="DSC Voltage",
        units="kV",
        description="DSC Voltage in kV",
        mandatory=False,
        section="Depth Profiling",
        prev_versions=["SIMS_DSC_VOLTAGE:v0"],
    )

    sims_dsc_current = PropertyTypeAssignment(
        code="SIMS_DSC_CURRENT",
        data_type="REAL",
        property_label="DSC Current",
        units="nA",
        description="DSC Current in nA",
        mandatory=False,
        section="Depth Profiling",
        prev_versions=["SIMS_DSC_CURRENT:v0"],
    )

    sims_dsc_raster_size = PropertyTypeAssignment(
        code="SIMS_DSC_RASTER_SIZE",
        data_type="REAL",
        property_label="Secondary ion beam raster size",
        units="micrometer",
        description="Secondary (Sputter) ion beam raster size in µm",
        mandatory=False,
        section="Depth Profiling",
        prev_versions=["SIMS_DSC_RASTER_SIZE:v0"],
    )

    stitching = PropertyTypeAssignment(
        code="STITCHING",
        data_type="BOOLEAN",
        property_label="Stitching",
        description="Indicates whether the image was acquired by stitching",
        mandatory=False,
        section="Imaging",
        prev_versions=["STITCHING:v0"],
    )

    stitching_total_area = PropertyTypeAssignment(
        code="STITCHING_TOTAL_AREA",
        data_type="VARCHAR",
        property_label="Total stitching area (mm x mm)",
        description="Total area of the stitched image in mm x mm",
        mandatory=False,
        section="Imaging",
        prev_versions=["STITCHING_TOTAL_AREA:v0"],
    )

    stitching_frames_per_patch = PropertyTypeAssignment(
        code="STITCHING_FRAMES_PER_PATCH",
        data_type="INTEGER",
        property_label="Frames per Patch",
        description="Number of frames acquired for each patch",
        mandatory=False,
        section="Imaging",
        prev_versions=["STITCHING_FRAMES_PER_PATCH:v0"],
    )

    stitching_pixel_density = PropertyTypeAssignment(
        code="STITCHING_PIXEL_DENSITY",
        data_type="REAL",
        property_label="Pixel Density",
        units="pixels/mm",
        description="Pixel density of the stitched image in pixel/mm",
        mandatory=False,
        section="Imaging",
        prev_versions=["STITCHING_PIXEL_DENSITY:v0"],
    )


class NMR(Measurement):
    defs = ObjectTypeDef(
        code="NMR",
        description="An NMR is a measurement that records nuclear magnetic resonance "
        "spectra of a sample.",
        generated_code_prefix="NMR",
        prev_versions=["EXPERIMENTAL_STEP.NMR:v0"],
    )

    nmr_instrument = PropertyTypeAssignment(
        code="NMR_INSTRUMENT",
        data_type="VARCHAR",
        property_label="Instrument",
        description="NMR Instrument",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["NMR.INSTRUMENT:v0"],
    )

    nmr_nucleus_direct = PropertyTypeAssignment(
        code="NMR_NUCLEUS_DIRECT",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="NMR_NUCLEI",
        property_label="Nucleus (direct)",
        description="Nucleus (direct)",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["NMR.NUCLEUS_DIRECT:v0"],
    )

    nmr_nucleus_indirect = PropertyTypeAssignment(
        code="NMR_NUCLEUS_INDIRECT",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="NMR_NUCLEI",
        property_label="Nucleus (indirect, 2D only)",
        description="Nucleus (indirect, 2D only)",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["NMR.NUCLEUS_INDIRECT:v0"],
    )

    nmr_solvent = PropertyTypeAssignment(
        code="NMR_SOLVENT",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="NMR_SOLVENTS",
        property_label="Solvent",
        description="NMR Solvent",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["NMR.SOLVENT:v0"],
    )

    nmr_frequency = PropertyTypeAssignment(
        code="NMR_FREQUENCY",
        data_type="REAL",
        property_label="Frequency",
        units="MHz",
        description="NMR Frequency [MHz]",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["NMR.FREQUENCY:v0"],
    )

    nmr_experiment = PropertyTypeAssignment(
        code="NMR_EXPERIMENT",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="NMR_EXPERIMENT_TYPES",
        property_label="Experiment",
        description="NMR Experiment",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["NMR.EXPERIMENT:v0"],
    )

    nmr_scans = PropertyTypeAssignment(
        code="NMR_SCANS",
        data_type="INTEGER",
        property_label="Number of Scans",
        description="Number of NMR Scans",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["NMR.SCANS:v0"],
    )

    nmr_start_chemical_shift = PropertyTypeAssignment(
        code="NMR_START_CHEMICAL_SHIFT",
        data_type="REAL",
        property_label="Start Chemical Shift",
        units="ppm",
        description="Start Chemical Shift [ppm]",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["NMR.START_CHEMICAL_SHIFT:v0"],
    )

    nmr_end_chemical_shift = PropertyTypeAssignment(
        code="NMR_END_CHEMICAL_SHIFT",
        data_type="REAL",
        property_label="End Chemical Shift",
        units="ppm",
        description="End Chemical Shift [ppm]",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["NMR.END_CHEMICAL_SHIFT:v0"],
    )

    nmr_is_qnmr = PropertyTypeAssignment(
        code="NMR_IS_QNMR",
        data_type="BOOLEAN",
        property_label="Quantitative NMR",
        description="Quantitative NMR",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["NMR.IS_QNMR:v0"],
    )

    nmr_pulse_angle = PropertyTypeAssignment(
        code="NMR_PULSE_ANGLE",
        data_type="REAL",
        property_label="Pulse Angle",
        units="degree",
        description="Pulse Angle [degree]",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["NMR.PULSE_ANGLE:v0"],
    )

    nmr_interpulse_delay = PropertyTypeAssignment(
        code="NMR_INTERPULSE_DELAY",
        data_type="REAL",
        property_label="Interpulse Delay",
        units="s",
        description="Interpulse Delay [s]",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["NMR.INTERPULSE_DELAY:v0"],
    )

    nmr_acquisition_time = PropertyTypeAssignment(
        code="NMR_ACQUISITION_TIME",
        data_type="REAL",
        property_label="Acquisition Time",
        units="s",
        description="Acquisition Time [s]",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["NMR.ACQUISITION_TIME:v0"],
    )


class ThermographicMeasurement(Measurement):
    defs = ObjectTypeDef(
        code="THERMOGRAPHIC_MEASUREMENT",
        description="A ThermographicMeasurement is a measurement that records the "
        "infrared radiation emitted by an object to determine its surface "
        "temperature distribution.",
        generated_code_prefix="THERMOGR",
        prev_versions=["EXPERIMENTAL_STEP.THERMOGRAPHIC_MEASUREMENT:v0"],
    )

    # Properties from v0 that need to be migrated to v1 (from EXPERIMENTAL_STEP.THERMOGRAPHIC_MEASUREMENT:v0):
    # ASSOCIATED_PROJECT  (OBJECT reference to PROJECT, which has no v1 object type yet)


class ImageSeries(Measurement):
    defs = ObjectTypeDef(
        code="IMAGE_SERIES",
        description="An ImageSeries is a measurement that records a series of one or "
        "more still images.",
        generated_code_prefix="IMG_SERIES",
        prev_versions=["EXPERIMENTAL_STEP.IMAGE_SERIES:v0"],
    )

    uuid = PropertyTypeAssignment(
        code="UUID",
        data_type="VARCHAR",
        property_label="UUID",
        description="A Universally Unique IDentifier (UUID/GUID) according to RFC 4122",
        mandatory=False,
        section="Identifiers",
        prev_versions=["UUID:v0"],
    )

    image_horizontal_resolution = PropertyTypeAssignment(
        code="IMAGE_HORIZONTAL_RESOLUTION",
        data_type="INTEGER",
        property_label="Horizontal resolution",
        units="pixels",
        description="Horizontal resolution of the image [pixel]",
        mandatory=False,
        section="Image Series Information",
        prev_versions=["IMAGE_HORIZONTAL_RESOLUTION:v0"],
    )

    image_vertical_resolution = PropertyTypeAssignment(
        code="IMAGE_VERTICAL_RESOLUTION",
        data_type="INTEGER",
        property_label="Vertical resolution",
        units="pixels",
        description="Vertical resolution of the image [pixel]",
        mandatory=False,
        section="Image Series Information",
        prev_versions=["IMAGE_VERTICAL_RESOLUTION:v0"],
    )

    image_series_count = PropertyTypeAssignment(
        code="IMAGE_SERIES_COUNT",
        data_type="INTEGER",
        property_label="Number of images recorded",
        description="Number of images recorded",
        mandatory=False,
        section="Image Series Information",
        prev_versions=["IMAGE_SERIES_COUNT:v0"],
    )


class SEM(Measurement):
    defs = ObjectTypeDef(
        code="SEM",
        description="An SEM is a measurement that images a sample surface by scanning "
        "it with a focused electron beam (scanning electron microscopy).",
        generated_code_prefix="SEM",
        prev_versions=["EXPERIMENTAL_STEP.SEM:v0"],
    )

    sem_instrument = PropertyTypeAssignment(
        code="SEM_INSTRUMENT",
        data_type="VARCHAR",
        property_label="Instrument",
        description="SEM Instrument",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["SEM.INSTRUMENT:v0"],
    )

    sem_imagesizex = PropertyTypeAssignment(
        code="SEM_IMAGESIZEX",
        data_type="VARCHAR",
        property_label="Image Size X",
        description="Image Size X",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["SEM.IMAGESIZEX:v0"],
    )

    sem_imagesizey = PropertyTypeAssignment(
        code="SEM_IMAGESIZEY",
        data_type="VARCHAR",
        property_label="Image Size Y",
        description="Image Size Y",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["SEM.IMAGESIZEY:v0"],
    )

    sem_operatingmode = PropertyTypeAssignment(
        code="SEM_OPERATINGMODE",
        data_type="VARCHAR",
        property_label="Operating Mode",
        description="Operating Mode",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["SEM.OPERATINGMODE:v0"],
    )

    sem_detector = PropertyTypeAssignment(
        code="SEM_DETECTOR",
        data_type="VARCHAR",
        property_label="Detector",
        description="Detector",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["SEM.DETECTOR:v0"],
    )

    sem_projectormode = PropertyTypeAssignment(
        code="SEM_PROJECTORMODE",
        data_type="VARCHAR",
        property_label="Projector Mode",
        description="Projector Mode",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["SEM.PROJECTORMODE:v0"],
    )

    sem_pixelsizex = PropertyTypeAssignment(
        code="SEM_PIXELSIZEX",
        data_type="VARCHAR",
        property_label="Pixel Size X",
        description="Pixel Size X",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["SEM.PIXELSIZEX:v0"],
    )

    sem_pixelsizey = PropertyTypeAssignment(
        code="SEM_PIXELSIZEY",
        data_type="VARCHAR",
        property_label="Pixel Size Y",
        description="Pixel Size Y",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["SEM.PIXELSIZEY:v0"],
    )

    sem_accelerationvoltage = PropertyTypeAssignment(
        code="SEM_ACCELERATIONVOLTAGE",
        data_type="VARCHAR",
        property_label="Acceleration Voltage (keV)",
        description="Acceleration Voltage [keV]",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["SEM.ACCELERATIONVOLTAGE:v0"],
    )

    sem_magnification = PropertyTypeAssignment(
        code="SEM_MAGNIFICATION",
        data_type="VARCHAR",
        property_label="Magnification",
        description="Magnificaiton",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["SEM.MAGNIFICATION:v0"],
    )

    sem_workingdistance = PropertyTypeAssignment(
        code="SEM_WORKINGDISTANCE",
        data_type="VARCHAR",
        property_label="Working Distance (mm)",
        description="Working Distance [mm]",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["SEM.WORKINGDISTANCE:v0"],
    )


class TEM(Measurement):
    defs = ObjectTypeDef(
        code="TEM",
        description="A TEM is a measurement that images or analyses a thin sample with "
        "an electron beam transmitted through it (transmission electron "
        "microscopy).",
        generated_code_prefix="TEM",
        prev_versions=["EXPERIMENTAL_STEP.TEM:v0"],
    )

    tem_instrument = PropertyTypeAssignment(
        code="TEM_INSTRUMENT",
        data_type="VARCHAR",
        property_label="Instrument",
        description="TEM Instrument",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["TEM.INSTRUMENT:v0"],
    )

    tem_imagesizex = PropertyTypeAssignment(
        code="TEM_IMAGESIZEX",
        data_type="VARCHAR",
        property_label="Image Size X",
        description="Image Size X",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["TEM.IMAGESIZEX:v0"],
    )

    tem_imagesizey = PropertyTypeAssignment(
        code="TEM_IMAGESIZEY",
        data_type="VARCHAR",
        property_label="Image Size Y",
        description="Image Size Y",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["TEM.IMAGESIZEY:v0"],
    )

    tem_operatingmode = PropertyTypeAssignment(
        code="TEM_OPERATINGMODE",
        data_type="VARCHAR",
        property_label="Operating Mode",
        description="Operating Mode",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["TEM.OPERATINGMODE:v0"],
    )

    tem_detector = PropertyTypeAssignment(
        code="TEM_DETECTOR",
        data_type="VARCHAR",
        property_label="Detector",
        description="Detector",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["TEM.DETECTOR:v0"],
    )

    tem_projectormode = PropertyTypeAssignment(
        code="TEM_PROJECTORMODE",
        data_type="VARCHAR",
        property_label="Projector Mode",
        description="Projector Mode",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["TEM.PROJECTORMODE:v0"],
    )

    tem_pixelsizex = PropertyTypeAssignment(
        code="TEM_PIXELSIZEX",
        data_type="VARCHAR",
        property_label="Pixel Size X",
        description="Pixel Size X",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["TEM.PIXELSIZEX:v0"],
    )

    tem_pixelsizey = PropertyTypeAssignment(
        code="TEM_PIXELSIZEY",
        data_type="VARCHAR",
        property_label="Pixel Size Y",
        description="Pixel Size Y",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["TEM.PIXELSIZEY:v0"],
    )

    tem_accelerationvoltage = PropertyTypeAssignment(
        code="TEM_ACCELERATIONVOLTAGE",
        data_type="VARCHAR",
        property_label="Acceleration Voltage (keV)",
        description="Acceleration Voltage [keV]",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["TEM.ACCELERATIONVOLTAGE:v0"],
    )

    tem_magnification = PropertyTypeAssignment(
        code="TEM_MAGNIFICATION",
        data_type="VARCHAR",
        property_label="Magnification",
        description="Magnification",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["TEM.MAGNIFICATION:v0"],
    )

    tem_cameralength = PropertyTypeAssignment(
        code="TEM_CAMERALENGTH",
        data_type="VARCHAR",
        property_label="Camera Length",
        description="Camera Length",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["TEM.CAMERALENGTH:v0"],
    )

    tem_spot_index = PropertyTypeAssignment(
        code="TEM_SPOT_INDEX",
        data_type="VARCHAR",
        property_label="Spot Index",
        description="Spot Index",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["TEM.SPOT_INDEX:v0"],
    )

    tem_gun_lens_setting = PropertyTypeAssignment(
        code="TEM_GUN_LENS_SETTING",
        data_type="VARCHAR",
        property_label="Gun Lens Setting",
        description="Gun Lens Setting",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["TEM.GUN_LENS_SETTING:v0"],
    )

    tem_c2_aperture_name = PropertyTypeAssignment(
        code="TEM_C2_APERTURE_NAME",
        data_type="VARCHAR",
        property_label="C2 Aperture",
        description="C2 Aperture",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["TEM.C2_APERTURE_NAME:v0"],
    )

    tem_obj_aperture_name = PropertyTypeAssignment(
        code="TEM_OBJ_APERTURE_NAME",
        data_type="VARCHAR",
        property_label="Objective Aperture",
        description="Objective Aperture",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["TEM.OBJ_APERTURE_NAME:v0"],
    )

    tem_saed_aperturediameter = PropertyTypeAssignment(
        code="TEM_SAED_APERTUREDIAMETER",
        data_type="VARCHAR",
        property_label="SAED Aperture Diameter",
        description="SAED Aperture Diameter",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["TEM.SAED_APERTUREDIAMETER:v0"],
    )

    tem_saed_apertureposx = PropertyTypeAssignment(
        code="TEM_SAED_APERTUREPOSX",
        data_type="VARCHAR",
        property_label="SAED Aperture Pos X",
        description="SAED Aperture Pos X",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["TEM.SAED_APERTUREPOSX:v0"],
    )

    tem_saed_apertureposy = PropertyTypeAssignment(
        code="TEM_SAED_APERTUREPOSY",
        data_type="VARCHAR",
        property_label="SAED Aperture PosY",
        description="SAED Aperture Pos Y",
        mandatory=False,
        section="Measurement Parameters",
        prev_versions=["TEM.SAED_APERTUREPOSY:v0"],
    )


class XRD(Measurement):
    defs = ObjectTypeDef(
        code="XRD",
        description="An XRD is a measurement that records the diffraction of X-rays by "
        "a sample to determine its crystal structure (X-ray diffraction).",
        generated_code_prefix="XRD",
    )


class PXRD(XRD):
    defs = ObjectTypeDef(
        code="PXRD",
        description="A PXRD is an XRD that records the X-ray diffraction pattern of a "
        "powder sample.",
        generated_code_prefix="PXRD",
        prev_versions=["EXPERIMENTAL_STEP.PXRD_MEASUREMENT:v0"],
    )

    time_per_step = PropertyTypeAssignment(
        code="TIME_PER_STEP",
        data_type="REAL",
        property_label="Time per step",
        units="s",
        description="Time per step in seconds",
        mandatory=False,
        section="Experimental Details",
        prev_versions=["TIME_PER_STEP:v0"],
    )

    rotation_speed = PropertyTypeAssignment(
        code="ROTATION_SPEED",
        data_type="REAL",
        property_label="Rotation speed",
        units="rpm",
        description="Sample rotation speed in revolutions per minute (rpm)",
        mandatory=False,
        section="Experimental Details",
        prev_versions=["ROTATION_SPEED:v0"],
    )

    voltage = PropertyTypeAssignment(
        code="VOLTAGE",
        data_type="REAL",
        property_label="Voltage",
        units="kV",
        description="Acceleration voltage of the X-ray tube in kilovolts (kV)",
        mandatory=False,
        section="Experimental Details",
        prev_versions=["VOLTAGE:v0"],
    )

    current = PropertyTypeAssignment(
        code="CURRENT",
        data_type="REAL",
        property_label="Current",
        units="mA",
        description="Tube current of the X-ray source in milliamperes (mA)",
        mandatory=False,
        section="Experimental Details",
        prev_versions=["CURRENT:v0"],
    )

    tube_material = PropertyTypeAssignment(
        code="TUBE_MATERIAL",
        data_type="VARCHAR",
        property_label="X-ray tube material",
        description="Material of the X-ray tube anode (e.g. Cu, Co, Mo)",
        mandatory=False,
        section="Experimental Details",
        prev_versions=["TUBE_MATERIAL:v0"],
    )

    xray_wavelength = PropertyTypeAssignment(
        code="XRAY_WAVELENGTH",
        data_type="REAL",
        property_label="X-ray wavelength",
        units="angstrom",
        description="Wavelength of the X-ray radiation in Angstrom (Å). This "
        "wavelength is associated\n        with the tube, and it can refer "
        "to alpha 1 or to the average depending on the tube configuration",
        mandatory=False,
        section="Experimental Details",
        prev_versions=["XRAY_WAVELENGTH:v0"],
    )

    tube_configuration_name = PropertyTypeAssignment(
        code="TUBE_CONFIGURATION_NAME",
        data_type="VARCHAR",
        property_label="X-ray tube configuration",
        description="Instrument-specific X-ray tube configuration identifier",
        mandatory=False,
        section="Experimental Details",
        prev_versions=["TUBE_CONFIGURATION_NAME:v0"],
    )

    goniometer_type = PropertyTypeAssignment(
        code="GONIOMETER_TYPE",
        data_type="VARCHAR",
        property_label="Goniometer type",
        description="Type of goniometer used for the measurement",
        mandatory=False,
        section="Experimental Details",
        prev_versions=["GONIOMETER_TYPE:v0"],
    )

    start_2theta = PropertyTypeAssignment(
        code="START_2THETA",
        data_type="REAL",
        property_label="Start 2Theta",
        units="degree",
        description="Starting angle of the 2Theta range in degrees",
        mandatory=False,
        section="Experimental Details",
        prev_versions=["START_2THETA:v0"],
    )

    end_2theta = PropertyTypeAssignment(
        code="END_2THETA",
        data_type="REAL",
        property_label="End 2Theta",
        units="degree",
        description="Ending angle of the 2Theta range in degrees",
        mandatory=False,
        section="Experimental Details",
        prev_versions=["END_2THETA:v0"],
    )

    step_size_2theta = PropertyTypeAssignment(
        code="STEP_SIZE_2THETA",
        data_type="REAL",
        property_label="Step size 2Theta",
        units="degree",
        description="Step size of the 2Theta range in degrees",
        mandatory=False,
        section="Experimental Details",
        prev_versions=["STEP_SIZE_2THETA:v0"],
    )


class UVVis(Measurement):
    defs = ObjectTypeDef(
        code="UV_VIS",
        description="A UVVis is a measurement that records the absorption or "
        "transmission of ultraviolet and visible light by a sample (UV-vis "
        "spectroscopy).",
        generated_code_prefix="UV_VIS",
    )

    # New in v1, no v0 equivalent. Stored as a percentage (0-100 %).
    transparency = PropertyTypeAssignment(
        code="TRANSPARENCY",
        data_type="REAL",
        property_label="Transparency",
        units="%",
        description="Share of the incident ultraviolet or visible light transmitted "
        "through the sample.",
        mandatory=False,
        section="Measurement Results",
    )


class SAXSMeasurement(Measurement):
    defs = ObjectTypeDef(
        code="SAXS_MEASUREMENT",
        description="A SAXSMeasurement is a measurement that records the small-angle "
        "X-ray scattering (SAXS) of a sample to characterise its nanoscale "
        "structure.",
        generated_code_prefix="SAXS",
        prev_versions=["EXPERIMENTAL_STEP.SAXS_MEASUREMENT:v0"],
    )

    measurement_id = PropertyTypeAssignment(
        code="MEASUREMENT_ID",
        data_type="INTEGER",
        property_label="Measurement ID",
        description="Div. internal measurement ID",
        mandatory=False,
        section="Experiment Details",
        prev_versions=["MEASUREMENT_ID:v0"],
    )

    measurement_date = PropertyTypeAssignment(
        code="MEASUREMENT_DATE",
        data_type="DATE",
        property_label="Measurement Date",
        description="Measurement Date",
        mandatory=True,
        section="Experiment Details",
        prev_versions=["MEASUREMENT_DATE:v0"],
    )

    cell_temperature = PropertyTypeAssignment(
        code="CELL_TEMPERATURE",
        data_type="REAL",
        property_label="Cell Temperature",
        units="celsius",
        description="Measurement cell temperature in °C",
        mandatory=True,
        section="Experiment Details",
        prev_versions=["CELL_TEMPERATURE_IN_CELSIUS:v0"],
    )

    exposure_time = PropertyTypeAssignment(
        code="EXPOSURE_TIME",
        data_type="REAL",
        property_label="Exposure time",
        units="s",
        description="Exposure time in seconds",
        mandatory=True,
        section="Experiment Details",
        prev_versions=["EXPOSURE_TIME_IN_SECONDS:v0"],
    )

    frame_count = PropertyTypeAssignment(
        code="FRAME_COUNT",
        data_type="INTEGER",
        property_label="Number of frames",
        description="Number of frames",
        mandatory=True,
        section="Experiment Details",
        prev_versions=["FRAME_COUNT:v0"],
    )


class MouseMeasurement(SAXSMeasurement):
    defs = ObjectTypeDef(
        code="MOUSE_MEASUREMENT",
        description="A MouseMeasurement is a SAXS measurement performed with the MOUSE "
        "instrument.",
        generated_code_prefix="MOUSE",
        prev_versions=["EXPERIMENTAL_STEP.SAXS_MEASUREMENT.MOUSE_MEASUREMENT:v0"],
    )

    sample_position = PropertyTypeAssignment(
        code="SAMPLE_POSITION",
        data_type="VARCHAR",
        property_label="Sample Position",
        description="The sample position ID in the sample holder. Used to record the "
        "spatial/orientational position of the sample within the holder or "
        "setup. Different sample holders might get new names, or one-off "
        "sample holders might have a temporary ID.",
        mandatory=False,
        section="Experiment Details",
        prev_versions=["SAMPLE_POSITION:v0"],
    )

    measurement_protocol_file = PropertyTypeAssignment(
        code="MEASUREMENT_PROTOCOL_FILE",
        data_type="MULTILINE_VARCHAR",
        property_label="Measurement Protocol",
        description="Location of the measurement script",
        mandatory=False,
        section="Experiment Details",
        prev_versions=["MEASUREMENT_PROTOCOL_FILE:v0"],
    )

    measurement_protocol_options = PropertyTypeAssignment(
        code="MEASUREMENT_PROTOCOL_OPTIONS",
        data_type="VARCHAR",
        property_label="Measurement protocol options",
        description="JSON with key-value combinations",
        mandatory=False,
        section="Experiment Details",
        prev_versions=["MEASUREMENT_PROTOCOL_OPTIONS:v0"],
    )

    size_thickness = PropertyTypeAssignment(
        code="SIZE_THICKNESS",
        data_type="REAL",
        property_label="Thickness",
        units="mm",
        description="Thickness in mm",
        mandatory=False,
        section="Data Processing",
        prev_versions=["SIZE_THICKNESS_IN_MILLIMETER:v0"],
    )

    processing_protocol_file = PropertyTypeAssignment(
        code="PROCESSING_PROTOCOL_FILE",
        data_type="MULTILINE_VARCHAR",
        property_label="Data processing protocol",
        description="Location of the data processing protocol",
        mandatory=False,
        section="Data Processing",
        prev_versions=["PROCESSING_PROTOCOL_FILE:v0"],
    )

    # v0 properties of EXPERIMENTAL_STEP.SAXS_MEASUREMENT.MOUSE_MEASUREMENT not redefined here:
    # RESPONSIBLE_PERSON: inherited from Activity (RESPONSIBLE_PERSON)


class ThermalAnalysis(Measurement):
    defs = ObjectTypeDef(
        code="THERMAL_ANALYSIS",
        description="A ThermalAnalysis is a measurement that determines how a property "
        "of a sample changes under a controlled temperature program.",
        generated_code_prefix="THERM_ANAL",
    )


class DSC(ThermalAnalysis):
    defs = ObjectTypeDef(
        code="DSC",
        description="A DSC is a thermal analysis that measures the heat flow into or "
        "out of a sample relative to a reference (differential scanning "
        "calorimetry).",
        generated_code_prefix="DSC",
    )


class TGA(ThermalAnalysis):
    defs = ObjectTypeDef(
        code="TGA",
        description="A TGA is a thermal analysis that measures the change in mass of a "
        "sample as a function of temperature or time (thermogravimetric "
        "analysis).",
        generated_code_prefix="TGA",
    )
