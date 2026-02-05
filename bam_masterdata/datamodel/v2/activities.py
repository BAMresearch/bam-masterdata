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


class FcgEvaluation(Analysis):
    defs = ObjectTypeDef(
        code="FCG_EVALUATION",
        description="""
        An Analysis is an activity that interprets existing data to derive new data, such
        as properties, patterns, or parameters
        Fatigue Crack Growth Data Evaluation
        """,
        iri="https://bam.de/masterdata/FcgEvaluation",
        references=[],
        generated_code_prefix="FCG_EVALU",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.FCG_EVALUATION"],
    )


class Dcpd(Measurement):
    defs = ObjectTypeDef(
        code="DCPD",
        description="""
        A Measurement is an activity that uses an experimental device to produce quantitative
        or qualitative data about the properties of a material.
        Direct Current Potential Drop Measurement
        """,
        iri="https://bam.de/masterdata/Dcpd",
        references=[],
        generated_code_prefix="DCPD",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.DCPD"],
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


class MicroscopyFcgFractureSurfaceCracklength(Measurement):
    defs = ObjectTypeDef(
        code="MICROSCOPY_FCG_FRACTURE_SURFACE_CRACKLENGTH",
        description="""
        A Measurement is an activity that uses an experimental device to produce quantitative
        or qualitative data about the properties of a material.
        Optical Measurement of Cracklength on the Fracture Surface of an FCG Specimen
        """,
        iri="https://bam.de/masterdata/MicroscopyFcgFractureSurfaceCracklength",
        references=[],
        generated_code_prefix="MICRO_FCG_FRACT_SURFA_CRACK",
        aliases=[],
        previous_versions=[
            "EXPERIMENTAL_STEP.MICROSCOPY_FCG_FRACTURE_SURFACE_CRACKLENGTH"
        ],
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
        A Processing is an activity that alters the structure, composition, or form of a
        material.
        Razorblade Notching
        """,
        iri="https://bam.de/masterdata/RazorbladeNotching",
        references=[],
        generated_code_prefix="RAZOR_NOTCH",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.RAZORBLADE_NOTCHING"],
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


class GmawBase(Weldment):
    defs = ObjectTypeDef(
        code="GMAW_BASE",
        description="""
        A simple gas metal arc welding (GMAW) experiment
        """,
        iri="https://bam.de/masterdata/GmawBase",
        references=[],
        generated_code_prefix="GMAW_BASE",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.WELDMENT.GMAW_BASE"],
    )


class LaserHybridMagnet(Weldment):
    defs = ObjectTypeDef(
        code="LASER_HYBRID_MAGNET",
        description="""
        A welding experiment using laser-hybrid welding with magnetic support
        """,
        iri="https://bam.de/masterdata/LaserHybridMagnet",
        references=[],
        generated_code_prefix="LASER_HYBRI_MAGNE",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.WELDMENT.LASER_HYBRID_MAGNET"],
    )


class FcgTest(Test):
    defs = ObjectTypeDef(
        code="FCG_TEST",
        description="""
        A Test is an activity that subjects a material or component to controlled conditions
        to evaluate its performance, properties, or behavior.
        Fatigue Crack Growth Test
        """,
        iri="https://bam.de/masterdata/FcgTest",
        references=[],
        generated_code_prefix="FCG_TEST",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP.FCG_TEST"],
    )
