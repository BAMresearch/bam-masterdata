"""Object types for representing the v1 welding workflow in the v0 datamodel."""

from bam_masterdata.datamodel.v0.object_types import (
    ExperimentalStep,
    GasBottle,
    Instrument,
    MaterialV1,
    ParameterSet,
    RawMaterialCode,
    Sample,
)
from bam_masterdata.datamodel.v0.welding.object_types import LaserMagnet
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment


class CuttingProcess(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.CUTTING_PROCESS",
        description="A reusable definition of a cutting method.",
        generated_code_prefix="CUT_PROC",
    )

    process_number = PropertyTypeAssignment(
        code="PROCESS_NUMBER",
        data_type="VARCHAR",
        property_label="Process number",
        description="ISO 4063 number identifying the process.",
        section="Process Identification",
        mandatory=False,
    )

    standard_edition = PropertyTypeAssignment(
        code="STANDARD_EDITION",
        data_type="VARCHAR",
        property_label="Standard edition",
        description="Edition of ISO 4063 used to identify the process.",
        section="Process Identification",
        mandatory=False,
    )


class Cutting(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.CUTTING",
        description="A cutting operation that produces workpieces from stock material.",
        generated_code_prefix="CUT",
    )


class WeldingProcess(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.WELDING_PROCESS",
        description="A reusable definition of a welding method.",
        generated_code_prefix="WELD_PROC",
    )

    process_number = PropertyTypeAssignment(
        code="PROCESS_NUMBER",
        data_type="VARCHAR",
        property_label="Process number",
        description="ISO 4063 number identifying the process.",
        section="Process Identification",
        mandatory=False,
    )

    standard_edition = PropertyTypeAssignment(
        code="STANDARD_EDITION",
        data_type="VARCHAR",
        property_label="Standard edition",
        description="Edition of ISO 4063 used to identify the process.",
        section="Process Identification",
        mandatory=False,
    )


class WeldingJoint(Sample):
    defs = ObjectTypeDef(
        code="SAMPLE.WELDING_JOINT",
        description="The arrangement and preparation of workpieces at the location to be welded.",
        generated_code_prefix="WELD_JOINT",
    )

    joint_status = PropertyTypeAssignment(
        code="JOINT_STATUS",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="WELDING.JOINT_STATES",
        property_label="Joint status",
        description="Current state of the welding joint.",
        section="Joint Details",
        mandatory=False,
    )

    joint_type = PropertyTypeAssignment(
        code="JOINT_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="WELDING.JOINT_TYPES",
        property_label="Joint type",
        description="Arrangement of the workpieces in the welding joint.",
        section="Joint Details",
        mandatory=False,
    )

    groove_type = PropertyTypeAssignment(
        code="GROOVE_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="WELDING.GROOVE_TYPES",
        property_label="Groove type",
        description="Groove preparation identified by its unique code number and type name.",
        section="Groove Preparation",
        mandatory=False,
    )

    workpiece_thickness = LaserMagnet.workpiece_thickness.model_copy(
        update={"section": "Groove Preparation"}
    )

    workpiece_thickness2 = PropertyTypeAssignment(
        code="WORKPIECE_THICKNESS_2",
        data_type="REAL",
        property_label="Workpiece thickness 2",
        description="Thickness of the second workpiece.",
        units="mm",
        section="Groove Preparation",
        mandatory=False,
    )

    root_gap = PropertyTypeAssignment(
        code="ROOT_GAP",
        data_type="REAL",
        property_label="Root gap",
        description="Gap between the workpieces at the joint root.",
        units="mm",
        section="Groove Preparation",
        mandatory=False,
    )

    root_face = PropertyTypeAssignment(
        code="ROOT_FACE",
        data_type="REAL",
        property_label="Root face",
        description="Dimension of the root face of the joint preparation.",
        units="mm",
        section="Groove Preparation",
        mandatory=False,
    )

    root_face2 = PropertyTypeAssignment(
        code="ROOT_FACE_2",
        data_type="REAL",
        property_label="Root face 2",
        description="Dimension of the second root face of the joint preparation.",
        units="mm",
        section="Groove Preparation",
        mandatory=False,
    )

    root_face3 = PropertyTypeAssignment(
        code="ROOT_FACE_3",
        data_type="REAL",
        property_label="Root face 3",
        description="Dimension of the third root face of the joint preparation.",
        units="mm",
        section="Groove Preparation",
        mandatory=False,
    )

    bevel_radius = PropertyTypeAssignment(
        code="BEVEL_RADIUS",
        data_type="REAL",
        property_label="Bevel radius",
        description="Radius of the bevel in the joint preparation.",
        units="mm",
        section="Groove Preparation",
        mandatory=False,
    )

    bevel_radius2 = PropertyTypeAssignment(
        code="BEVEL_RADIUS_2",
        data_type="REAL",
        property_label="Bevel radius 2",
        description="Radius of the second bevel in the joint preparation.",
        units="mm",
        section="Groove Preparation",
        mandatory=False,
    )

    bevel_angle = PropertyTypeAssignment(
        code="BEVEL_ANGLE",
        data_type="REAL",
        property_label="Bevel angle",
        description="Angle of the bevel in the joint preparation.",
        units="deg",
        section="Groove Preparation",
        mandatory=False,
    )

    bevel_angle2 = PropertyTypeAssignment(
        code="BEVEL_ANGLE_2",
        data_type="REAL",
        property_label="Bevel angle 2",
        description="Angle of the second bevel in the joint preparation.",
        units="deg",
        section="Groove Preparation",
        mandatory=False,
    )

    groove_angle = PropertyTypeAssignment(
        code="GROOVE_ANGLE",
        data_type="REAL",
        property_label="Groove angle",
        description="Angle of the groove in the joint preparation.",
        units="deg",
        section="Groove Preparation",
        mandatory=False,
    )

    groove_angle2 = PropertyTypeAssignment(
        code="GROOVE_ANGLE_2",
        data_type="REAL",
        property_label="Groove angle 2",
        description="Angle of the second groove in the joint preparation.",
        units="deg",
        section="Groove Preparation",
        mandatory=False,
    )

    special_depth = PropertyTypeAssignment(
        code="SPECIAL_DEPTH",
        data_type="REAL",
        property_label="Special depth",
        description="Special depth used for the 4.1.2 Frontal-Face-Groove type.",
        units="mm",
        section="Groove Preparation",
        mandatory=False,
    )


class WeldingWireAlloy(MaterialV1):
    defs = ObjectTypeDef(
        code="MATERIAL_V1.WELDING_WIRE_ALLOY",
        description="A reusable alloy specification for welding wire.",
        generated_code_prefix="WIRE_ALLOY",
    )

    alias = RawMaterialCode.alias

    material_group = RawMaterialCode.material_group

    characteristics = RawMaterialCode.characteristics

    alloy_standard = PropertyTypeAssignment(
        code="ALLOY_STANDARD",
        data_type="VARCHAR",
        property_label="Alloy standard",
        description="Standard and edition used to classify the welding wire alloy.",
        section="Alloy Identification",
        mandatory=False,
    )

    alloy_designation = PropertyTypeAssignment(
        code="ALLOY_DESIGNATION",
        data_type="VARCHAR",
        property_label="Alloy designation",
        description="Designation of the welding wire alloy according to the specified standard.",
        section="Alloy Identification",
        mandatory=False,
    )


class GasMixture(MaterialV1):
    defs = ObjectTypeDef(
        code="MATERIAL_V1.GAS_MIXTURE",
        description="A reusable gas composition for welding.",
        generated_code_prefix="GAS_MIX",
    )

    volume_percent_argon = GasBottle.volume_percent_argon

    volume_percent_helium = GasBottle.volume_percent_helium

    volume_percent_carbon_dioxide = GasBottle.volume_percent_carbon_dioxide

    volume_percent_oxygen = GasBottle.volume_percent_oxygen

    volume_percent_nitrogen = GasBottle.volume_percent_nitrogen

    volume_percent_hydrogen = GasBottle.volume_percent_hydrogen

    mixture_standard = PropertyTypeAssignment(
        code="MIXTURE_STANDARD",
        data_type="VARCHAR",
        property_label="Mixture standard",
        description="Standard and edition used to classify the mixture.",
        section="Mixture Identification",
        mandatory=False,
    )

    mixture_designation = PropertyTypeAssignment(
        code="MIXTURE_DESIGNATION",
        data_type="VARCHAR",
        property_label="Mixture designation",
        description="Designation of the mixture according to the specified standard.",
        section="Mixture Identification",
        mandatory=False,
    )


class Weld(Sample):
    defs = ObjectTypeDef(
        code="SAMPLE.WELD",
        description="The physical result of a welding operation.",
        generated_code_prefix="WELD",
    )


class Weldment(Sample):
    defs = ObjectTypeDef(
        code="SAMPLE.WELDMENT",
        description="An assembly incorporating one or more welded joints.",
        generated_code_prefix="WELDMENT",
    )


class Component(Sample):
    defs = ObjectTypeDef(
        code="SAMPLE.COMPONENT",
        description="An assembly that can contain multiple weldments.",
        generated_code_prefix="COMPONENT",
    )


class RobotExecution(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.ROBOT_EXECUTION",
        description="One execution of a robot program or subprogram.",
        generated_code_prefix="ROBOT_EXEC",
    )


class WeldingTorchNeck(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.WELDING_TORCH_NECK",
        description="The neck component of an arc welding torch.",
        generated_code_prefix="TORCH_NECK",
    )


class WeldingGasNozzel(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.WELDING_GAS_NOZZEL",
        description="The gas nozzle component of an arc welding torch.",
        generated_code_prefix="GAS_NOZZLE",
    )


class WeldingContactTip(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.WELDING_CONTACT_TIP",
        description="The contact tip component of an arc welding torch.",
        generated_code_prefix="CONTACT_TIP",
    )


class CameraCalibration(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.CAMERA_CALIBRATION",
        description="A camera calibration run that estimates camera and lens parameters.",
        generated_code_prefix="CAM_CAL",
    )


class CameraCalibrationParameters(ParameterSet):
    defs = ObjectTypeDef(
        code="PARAMETER_SET.CAMERA_CALIBRATION_PARAMETERS",
        description="Parameters obtained from a camera calibration run.",
        generated_code_prefix="CAM_CAL_PARAMS",
    )

    focal_length_fx = PropertyTypeAssignment(
        code="FOCAL_LENGTH_FX",
        data_type="REAL",
        property_label="Focal length fx",
        description="Horizontal focal length in image coordinates.",
        units="pixel",
        section="Camera Intrinsics",
        mandatory=False,
    )

    focal_length_fy = PropertyTypeAssignment(
        code="FOCAL_LENGTH_FY",
        data_type="REAL",
        property_label="Focal length fy",
        description="Vertical focal length in image coordinates.",
        units="pixel",
        section="Camera Intrinsics",
        mandatory=False,
    )

    principal_point_cx = PropertyTypeAssignment(
        code="PRINCIPAL_POINT_CX",
        data_type="REAL",
        property_label="Principal point cx",
        description="Horizontal coordinate of the principal point.",
        units="pixel",
        section="Camera Intrinsics",
        mandatory=False,
    )

    principal_point_cy = PropertyTypeAssignment(
        code="PRINCIPAL_POINT_CY",
        data_type="REAL",
        property_label="Principal point cy",
        description="Vertical coordinate of the principal point.",
        units="pixel",
        section="Camera Intrinsics",
        mandatory=False,
    )

    skew = PropertyTypeAssignment(
        code="CAMERA_SKEW",
        data_type="REAL",
        property_label="Skew",
        description="Skew term in the camera intrinsic matrix.",
        units="pixel",
        section="Camera Intrinsics",
        mandatory=False,
    )

    radial_distortion_k1 = PropertyTypeAssignment(
        code="RADIAL_DISTORTION_K1",
        data_type="REAL",
        property_label="Radial distortion k1",
        description="First radial distortion coefficient.",
        section="Lens Distortion",
        mandatory=False,
    )

    radial_distortion_k2 = PropertyTypeAssignment(
        code="RADIAL_DISTORTION_K2",
        data_type="REAL",
        property_label="Radial distortion k2",
        description="Second radial distortion coefficient.",
        section="Lens Distortion",
        mandatory=False,
    )

    radial_distortion_k3 = PropertyTypeAssignment(
        code="RADIAL_DISTORTION_K3",
        data_type="REAL",
        property_label="Radial distortion k3",
        description="Third radial distortion coefficient.",
        section="Lens Distortion",
        mandatory=False,
    )

    radial_distortion_k4 = PropertyTypeAssignment(
        code="RADIAL_DISTORTION_K4",
        data_type="REAL",
        property_label="Radial distortion k4",
        description="Fourth radial distortion coefficient, used by the rational model.",
        section="Lens Distortion",
        mandatory=False,
    )

    radial_distortion_k5 = PropertyTypeAssignment(
        code="RADIAL_DISTORTION_K5",
        data_type="REAL",
        property_label="Radial distortion k5",
        description="Fifth radial distortion coefficient, used by the rational model.",
        section="Lens Distortion",
        mandatory=False,
    )

    radial_distortion_k6 = PropertyTypeAssignment(
        code="RADIAL_DISTORTION_K6",
        data_type="REAL",
        property_label="Radial distortion k6",
        description="Sixth radial distortion coefficient, used by the rational model.",
        section="Lens Distortion",
        mandatory=False,
    )

    tangential_distortion_p1 = PropertyTypeAssignment(
        code="TANGENTIAL_DISTORTION_P1",
        data_type="REAL",
        property_label="Tangential distortion p1",
        description="First tangential distortion coefficient.",
        section="Lens Distortion",
        mandatory=False,
    )

    tangential_distortion_p2 = PropertyTypeAssignment(
        code="TANGENTIAL_DISTORTION_P2",
        data_type="REAL",
        property_label="Tangential distortion p2",
        description="Second tangential distortion coefficient.",
        section="Lens Distortion",
        mandatory=False,
    )

    thin_prism_distortion_s1 = PropertyTypeAssignment(
        code="THIN_PRISM_DISTORTION_S1",
        data_type="REAL",
        property_label="Thin-prism distortion s1",
        description="First thin-prism distortion coefficient.",
        section="Lens Distortion",
        mandatory=False,
    )

    thin_prism_distortion_s2 = PropertyTypeAssignment(
        code="THIN_PRISM_DISTORTION_S2",
        data_type="REAL",
        property_label="Thin-prism distortion s2",
        description="Second thin-prism distortion coefficient.",
        section="Lens Distortion",
        mandatory=False,
    )

    thin_prism_distortion_s3 = PropertyTypeAssignment(
        code="THIN_PRISM_DISTORTION_S3",
        data_type="REAL",
        property_label="Thin-prism distortion s3",
        description="Third thin-prism distortion coefficient.",
        section="Lens Distortion",
        mandatory=False,
    )

    thin_prism_distortion_s4 = PropertyTypeAssignment(
        code="THIN_PRISM_DISTORTION_S4",
        data_type="REAL",
        property_label="Thin-prism distortion s4",
        description="Fourth thin-prism distortion coefficient.",
        section="Lens Distortion",
        mandatory=False,
    )

    sensor_tilt_tau_x = PropertyTypeAssignment(
        code="SENSOR_TILT_TAU_X",
        data_type="REAL",
        property_label="Sensor tilt tau x",
        description="Sensor tilt parameter about the x-axis.",
        units="rad",
        section="Lens Distortion",
        mandatory=False,
    )

    sensor_tilt_tau_y = PropertyTypeAssignment(
        code="SENSOR_TILT_TAU_Y",
        data_type="REAL",
        property_label="Sensor tilt tau y",
        description="Sensor tilt parameter about the y-axis.",
        units="rad",
        section="Lens Distortion",
        mandatory=False,
    )

    image_width = PropertyTypeAssignment(
        code="CALIBRATION_IMAGE_WIDTH",
        data_type="INTEGER",
        property_label="Image width",
        description="Width of the images used for calibration.",
        units="pixel",
        section="Calibration Details",
        mandatory=False,
    )

    image_height = PropertyTypeAssignment(
        code="CALIBRATION_IMAGE_HEIGHT",
        data_type="INTEGER",
        property_label="Image height",
        description="Height of the images used for calibration.",
        units="pixel",
        section="Calibration Details",
        mandatory=False,
    )

    rms_reprojection_error = PropertyTypeAssignment(
        code="RMS_REPROJECTION_ERROR",
        data_type="REAL",
        property_label="RMS reprojection error",
        description="Overall root-mean-square reprojection error.",
        units="pixel",
        section="Calibration Details",
        mandatory=False,
    )
