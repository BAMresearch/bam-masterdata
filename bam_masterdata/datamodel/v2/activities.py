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


class Dls(Measurement):
    defs = ObjectTypeDef(
        code="DLS",
        description="""
        A Measurement is an activity that uses an experimental device to produce quantitative
        or qualitative data about the properties of a material.
        Dynamic and electrophoretic light scattering
        """,
        iri="https://bam.de/masterdata/Dls",
        references=[],
        generated_code_prefix="DLS",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.DLS"],
    )


class Ftir(Measurement):
    defs = ObjectTypeDef(
        code="FTIR",
        description="""
        A Measurement is an activity that uses an experimental device to produce quantitative
        or qualitative data about the properties of a material.
        Fourier Transform Infrared Spectroscopy
        """,
        iri="https://bam.de/masterdata/Ftir",
        references=[],
        generated_code_prefix="FTIR",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.FTIR"],
    )


class ImageSeries(Measurement):
    defs = ObjectTypeDef(
        code="IMAGE_SERIES",
        description="""
        A Measurement is an activity that uses an experimental device to produce quantitative
        or qualitative data about the properties of a material.
        A series of one or more still image recordings
        """,
        iri="https://bam.de/masterdata/ImageSeries",
        references=[],
        generated_code_prefix="IMAGE_SERIE",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.IMAGE_SERIES"],
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


class Nmr(Measurement):
    defs = ObjectTypeDef(
        code="NMR",
        description="""
        A Measurement is an activity that uses an experimental device to produce quantitative
        or qualitative data about the properties of a material.
        Nuclear Magnetic Resonance Spectroscopy
        """,
        iri="https://bam.de/masterdata/Nmr",
        references=[],
        generated_code_prefix="NMR",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.NMR"],
    )


class ProfileScan(Measurement):
    defs = ObjectTypeDef(
        code="PROFILE_SCAN",
        description="""
        A Measurement is an activity that uses an experimental device to produce quantitative
        or qualitative data about the properties of a material.
        A series of 2D line sensor readings
        """,
        iri="https://bam.de/masterdata/ProfileScan",
        references=[],
        generated_code_prefix="PROFI_SCAN",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.PROFILE_SCAN"],
    )


class SaxsMeasurement(Measurement):
    defs = ObjectTypeDef(
        code="SAXS_MEASUREMENT",
        description="""
        A Measurement is an activity that uses an experimental device to produce quantitative
        or qualitative data about the properties of a material.
        Metadata of a single Small-Angle X-Ray Scattering (SAXS) measurement
        """,
        iri="https://bam.de/masterdata/SaxsMeasurement",
        references=[],
        generated_code_prefix="SAXS",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.SAXS_MEASUREMENT"],
    )


class Sem(Measurement):
    defs = ObjectTypeDef(
        code="SEM",
        description="""
        A Measurement is an activity that uses an experimental device to produce quantitative
        or qualitative data about the properties of a material.
        Scanning Electron Microscopy
        """,
        iri="https://bam.de/masterdata/Sem",
        references=[],
        generated_code_prefix="SEM",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.SEM"],
    )


class Tem(Measurement):
    defs = ObjectTypeDef(
        code="TEM",
        description="""
        A Measurement is an activity that uses an experimental device to produce quantitative
        or qualitative data about the properties of a material.
        Transmission Electron Microscopy
        """,
        iri="https://bam.de/masterdata/Tem",
        references=[],
        generated_code_prefix="TEM",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.TEM"],
    )


class ThermographicMeasurement(Measurement):
    defs = ObjectTypeDef(
        code="THERMOGRAPHIC_MEASUREMENT",
        description="""
        A Measurement is an activity that uses an experimental device to produce quantitative
        or qualitative data about the properties of a material.
        Thermographic Measurement
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
        An experimental step describing a video recording
        """,
        iri="https://bam.de/masterdata/VideoRecording",
        references=[],
        generated_code_prefix="VIDEO_RECOR",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.VIDEO_RECORDING"],
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
        Measurement of particle size distribution (PSD) by laser diffraction method.
        """,
        iri="https://bam.de/masterdata/LaserDiffPSD",
        references=[],
        generated_code_prefix="LASER_DIFF_PSD",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.LASER_DIFF_PSD_MEASUREMENT"],
    )
