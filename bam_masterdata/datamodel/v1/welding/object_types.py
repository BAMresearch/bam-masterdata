# AUTO-GENERATED CLASS HIERARCHY — DO NOT EDIT
#
# PhysicalObject*
# └── WeldingWire
#
# Activity*
# └── RobotExecution
#
# Context*
# ├── WeldingProcess
# ├── CuttingProcess
# ├── WeldSegment
# ├── SimulationDomain
# └── MaterialData
#
# Processing*
# ├── Welding
# │   └── LaserCTW
# └── Cutting
#
# ParameterSet*
# └── CameraCalibrationParameters
#
# Sample*
# ├── Component
# ├── Weldment
# ├── WeldingJoint
# ├── Workpiece
# └── Weld
#
# Material*
# ├── MetallicAlloy
# ├── GasMixture
# └── WeldingWireAlloy
#
# Instrument*
# ├── GmawWeldingPowerSource
# ├── Robot
# ├── LaserSource
# ├── Pyrometer
# └── LoadCell
#
# Equipment*
# ├── Positioner
# ├── RobotController
# ├── StationLayout
# ├── TorchHead
# ├── WeldingTorchNeck
# ├── WeldingGasNozzel
# ├── WeldingContactTip
# ├── Lens
# ├── LaserWeldOptic
# ├── LaserFiber
# └── HydraulicTable
#
# Sensor*
# ├── Camera
# └── LaserLineScanner
#
# Measurement*
# ├── ProfileScan
# ├── ImageSeries
# └── VideoRecording
#
# Analysis*
# └── CameraCalibration
#
# Computation*
# ├── Meshing
# └── AnsisFluentRun
#
# Software*
# ├── UDFModel
# └── AnsisFluent
#
# END AUTO-GENERATED CLASS HIERARCHY

"""Object type definitions related to welding experiments and simulation."""

from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment

from ..activities import (
    Analysis,
    Calibration,
    Computation,
    Experiment,
    Measurement,
    Processing,
)
from ..base_objects import (
    Activity,
)
from ..entities import (
    Context,
    Device,
    Entity,
    Equipment,
    Instrument,
    Material,
    ParameterSet,
    PhysicalObject,
    Sample,
    Sensor,
    Software,
)


class WeldingWire(PhysicalObject):
    defs = ObjectTypeDef(
        code="WELDING_WIRE",
        description="A WeldingWire is a material supplied in wire form for use as a consumable electrode "
        "or filler material in welding.",
        generated_code_prefix="WELD_WIRE",
        prev_versions=["CONSUMABLE.WELDING.WIRE_SOLID:v0"],
    )

    # Preserve the legacy batch number mapping for welding wire.
    lot_number = PhysicalObject.lot_number.model_copy(
        update={"prev_versions": ["LOT_NUMBER:v0", "BATCH_NUMBER:v0"]},
    )

    diameter_mm = PropertyTypeAssignment(
        code="DIAMETER_MM",
        data_type="REAL",
        property_label="Diameter",
        description="""Diameter""",
        units="mm",
        section="Wire Information",
        mandatory=False,
        prev_versions=["WELDING_WIRE.DIAMETER:v0"],
    )

    mass_kg = PropertyTypeAssignment(
        code="MASS_KG",
        data_type="REAL",
        property_label="Mass",
        description="""Mass""",
        units="kg",
        section="Wire Information",
        mandatory=False,
        prev_versions=["WELDING_WIRE.WEIGHT:v0"],
    )

    welding_wire_alloy = PropertyTypeAssignment(
        code="WELDING_WIRE_ALLOY",
        data_type="OBJECT",
        object_code="WELDING_WIRE_ALLOY",
        property_label="Welding wire alloy",
        description="The alloy specification of the welding wire.",
        section="Wire Information",
        mandatory=False,
    )

    wire_type = PropertyTypeAssignment(
        code="WIRE_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="WELDING_WIRE_TYPES",
        property_label="Wire type",
        description="Form or intended use of the welding wire.",
        section="Wire Information",
        mandatory=False,
    )


# -------------------------
# GENERAL
# -------------------------


# ----- Activity
class RobotExecution(Activity):
    defs = ObjectTypeDef(
        code="ROBOT_EXECUTION",
        description="""Execution of a robot program""",
        generated_code_prefix="",
    )


class WeldingProcess(Context):
    # GLOBAL VOCABULARY
    defs = ObjectTypeDef(
        code="WELDING_PROCESS",
        description="""Welding process identified by process names and numbers (ISO 4063)""",
        generated_code_prefix="",
    )

    process_number = PropertyTypeAssignment(
        code="PROCESS_NUMBER",
        data_type="VARCHAR",
        property_label="Process number",
        description="ISO 4063 number identifying the process.",
        section="Process Identification",
        mandatory=False,
        prev_versions=["PROCESS_NUMBER:v0"],
    )

    standard_edition = PropertyTypeAssignment(
        code="STANDARD_EDITION",
        data_type="VARCHAR",
        property_label="Standard edition",
        description="Edition of ISO 4063 used to identify the process.",
        section="Process Identification",
        mandatory=False,
        prev_versions=["STANDARD_EDITION:v0"],
    )


class CuttingProcess(Context):
    # GLOBAL VOCABULARY
    defs = ObjectTypeDef(
        code="CUTTING_PROCESS",
        description="""Cutting process identified by process names and numbers (ISO 4063)""",
        generated_code_prefix="",
    )

    process_number = PropertyTypeAssignment(
        code="PROCESS_NUMBER",
        data_type="VARCHAR",
        property_label="Process number",
        description="ISO 4063 number identifying the process.",
        section="Process Identification",
        mandatory=False,
        prev_versions=["PROCESS_NUMBER:v0"],
    )

    standard_edition = PropertyTypeAssignment(
        code="STANDARD_EDITION",
        data_type="VARCHAR",
        property_label="Standard edition",
        description="Edition of ISO 4063 used to identify the process.",
        section="Process Identification",
        mandatory=False,
        prev_versions=["STANDARD_EDITION:v0"],
    )


class WeldSegment(Context):
    defs = ObjectTypeDef(
        code="WELD_SEGMENT",
        description="""abstract segmentation of a welded joint into hierarchical structure""",
        generated_code_prefix="",
    )
    layer = PropertyTypeAssignment(
        code="LAYER",
        data_type="INTEGER",
        property_label="Layer",
        description="Number identifying the layer of the weld segment.",
        section="Segment Identification",
        mandatory=False,
    )

    bead = PropertyTypeAssignment(
        code="BEAD",
        data_type="INTEGER",
        property_label="Bead",
        description="Number identifying the bead of the weld segment.",
        section="Segment Identification",
        mandatory=False,
    )

    weld = PropertyTypeAssignment(
        code="WELD",
        data_type="INTEGER",
        property_label="Weld",
        description="Number identifying the weld of the weld segment.",
        section="Segment Identification",
        mandatory=False,
    )

    section = PropertyTypeAssignment(
        code="SECTION",
        data_type="INTEGER",
        property_label="Section",
        description="Number identifying the section of the weld segment.",
        section="Segment Identification",
        mandatory=False,
    )


# ----- Processing
class Welding(Processing):
    defs = ObjectTypeDef(
        code="WELDING",
        description="""ISO/TR 25901-1:2016 2.1.1.1 welding""",
        generated_code_prefix="",
    )

    # TODO: Model the welding joint, weld segment, weld, filler material, and
    # shielding gas as parent/child relations.

    welding_process = PropertyTypeAssignment(
        code="WELDING_PROCESS",
        data_type="OBJECT",
        object_code="WELDING_PROCESS",
        property_label="Welding process",
        description="Welding process used for the activity.",
        section="Welding Details",
        mandatory=False,
    )

    welding_position = PropertyTypeAssignment(
        code="WELDING_POSITION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="WELDING_POSITIONS",
        property_label="Welding position",
        description="Position in which welding is performed.",
        section="Welding Details",
        mandatory=False,
    )

    welding_procedure_specification = PropertyTypeAssignment(
        code="WELDING_PROCEDURE_SPECIFICATION",
        data_type="VARCHAR",
        property_label="Welding procedure specification",
        description="Identifier of the welding procedure specification used.",
        section="Welding Details",
        mandatory=False,
    )


class LaserCTW(Welding):
    defs = ObjectTypeDef(
        code="LASER_CTW",
        description="Laser welding with an externally applied strain.",
        generated_code_prefix="",
    )

    # TODO: Model the joint and workpiece as parent/child relations.
    # TODO: Add the missing preparation information; clarify whether it describes
    # groove preparation or surface preparation.

    weld_travel_speed = PropertyTypeAssignment(
        code="WELD_TRAVEL_SPEED",
        data_type="REAL",
        property_label="Welding travel speed",
        description="Travel speed along the weld.",
        units="cm/min",
        section="Welding Parameters",
        mandatory=False,
    )

    shielding_gas_flow = PropertyTypeAssignment(
        code="SHIELDING_GAS_FLOW",
        data_type="REAL",
        property_label="Shielding gas flow rate",
        description="Shielding gas flow rate.",
        units="L/min",
        section="Shielding Gas",
        mandatory=False,
    )

    shielding_gas_angle = PropertyTypeAssignment(
        code="SHIELDING_GAS_ANGLE",
        data_type="REAL",
        property_label="Shielding gas angle",
        description="Nozzle angle relative to the horizontal.",
        units="deg",
        section="Shielding Gas",
        mandatory=False,
    )

    backing_gas = PropertyTypeAssignment(
        code="BACKING_GAS",
        data_type="BOOLEAN",
        property_label="Backing gas used",
        description="Whether backing gas is used.",
        section="Shielding Gas",
        mandatory=False,
    )

    laser_power = PropertyTypeAssignment(
        code="LASER_POWER",
        data_type="REAL",
        property_label="Laser power",
        description="Laser power used for welding.",
        units="kW",
        section="Laser Parameters",
        mandatory=False,
    )

    laser_focus = PropertyTypeAssignment(
        code="LASER_FOCUS",
        data_type="REAL",
        property_label="Laser focus position",
        description="Laser focus position.",
        units="mm",
        section="Laser Parameters",
        mandatory=False,
    )

    laser_ramp_up = PropertyTypeAssignment(
        code="LASER_RAMP_UP",
        data_type="BOOLEAN",
        property_label="Laser ramp-up used",
        description="Whether a power ramp is used when turning on the laser.",
        section="Laser Parameters",
        mandatory=False,
    )

    laser_illumination_power = PropertyTypeAssignment(
        code="LASER_ILLUMINATION_POWER",
        data_type="REAL",
        property_label="Illumination laser power",
        description="Power of the illumination laser.",
        units="W",
        section="Illumination Parameters",
        mandatory=False,
    )

    laser_illumination_spot_size = PropertyTypeAssignment(
        code="LASER_ILLUMINATION_SPOT_SIZE",
        data_type="REAL",
        property_label="Illumination spot diameter",
        description="Diameter of the illuminated spot.",
        units="mm",
        section="Illumination Parameters",
        mandatory=False,
    )

    laser_illumination_spot_angle = PropertyTypeAssignment(
        code="LASER_ILLUMINATION_SPOT_ANGLE",
        data_type="REAL",
        property_label="Illumination angle",
        description="Illumination optics angle relative to the horizontal.",
        units="deg",
        section="Illumination Parameters",
        mandatory=False,
    )

    laser_illumination_filter = PropertyTypeAssignment(
        code="LASER_ILLUMINATION_FILTER",
        data_type="VARCHAR",
        property_label="Optical filters",
        description="Optical filters used in front of the camera.",
        section="Illumination Parameters",
        mandatory=False,
    )

    strain_rate = PropertyTypeAssignment(
        code="STRAIN_RATE",
        data_type="REAL",
        property_label="Strain rate",
        description="Strain rate applied to the specimen.",
        units="percent/s",
        section="Strain Settings",
        mandatory=False,
    )

    strain_max = PropertyTypeAssignment(
        code="STRAIN_MAX",
        data_type="REAL",
        property_label="Maximum strain",
        description="Maximum strain applied to the specimen.",
        units="percent",
        section="Strain Settings",
        mandatory=False,
    )

    strain_direction = PropertyTypeAssignment(
        code="STRAIN_DIRECTION",
        data_type="REAL",
        property_label="Strain direction",
        description="Strain direction relative to the welding direction.",
        units="deg",
        section="Strain Settings",
        mandatory=False,
    )

    strain_starting_point = PropertyTypeAssignment(
        code="STRAIN_STARTING_POINT",
        data_type="REAL",
        property_label="Strain starting point",
        description="Starting point of strain application along the weld.",
        units="mm",
        section="Strain Settings",
        mandatory=False,
    )

    strain_preload = PropertyTypeAssignment(
        code="STRAIN_PRELOAD",
        data_type="REAL",
        property_label="Preload strain",
        description="Strain applied before the main loading.",
        units="percent",
        section="Strain Settings",
        mandatory=False,
    )

    robot_program = PropertyTypeAssignment(
        code="ROBOT_PROGRAM",
        data_type="VARCHAR",
        property_label="Robot program",
        description="Robot control program.",
        section="Control Programs",
        mandatory=False,
    )

    laser_program = PropertyTypeAssignment(
        code="LASER_PROGRAM",
        data_type="VARCHAR",
        property_label="Laser program",
        description="Laser control program.",
        section="Control Programs",
        mandatory=False,
    )


class Cutting(Processing):
    defs = ObjectTypeDef(
        code="CUTTING",
        description="""A cutting step""",
        generated_code_prefix="",
    )


# ----- ParameterSet
class CameraCalibrationParameters(ParameterSet):
    defs = ObjectTypeDef(
        code="CAMERA_CALIBRATION_PARAMETERS",
        description="""intrinsic (and extrinsic?) camera calibration parameters derived from a calibration run""",
        generated_code_prefix="",
    )

    focal_length_fx = PropertyTypeAssignment(
        code="FOCAL_LENGTH_FX",
        data_type="REAL",
        property_label="Focal length fx",
        description="Horizontal focal length in image coordinates.",
        units="pixel",
        section="Camera Intrinsics",
        mandatory=False,
        prev_versions=["FOCAL_LENGTH_FX:v0"],
    )

    focal_length_fy = PropertyTypeAssignment(
        code="FOCAL_LENGTH_FY",
        data_type="REAL",
        property_label="Focal length fy",
        description="Vertical focal length in image coordinates.",
        units="pixel",
        section="Camera Intrinsics",
        mandatory=False,
        prev_versions=["FOCAL_LENGTH_FY:v0"],
    )

    principal_point_cx = PropertyTypeAssignment(
        code="PRINCIPAL_POINT_CX",
        data_type="REAL",
        property_label="Principal point cx",
        description="Horizontal coordinate of the principal point.",
        units="pixel",
        section="Camera Intrinsics",
        mandatory=False,
        prev_versions=["PRINCIPAL_POINT_CX:v0"],
    )

    principal_point_cy = PropertyTypeAssignment(
        code="PRINCIPAL_POINT_CY",
        data_type="REAL",
        property_label="Principal point cy",
        description="Vertical coordinate of the principal point.",
        units="pixel",
        section="Camera Intrinsics",
        mandatory=False,
        prev_versions=["PRINCIPAL_POINT_CY:v0"],
    )

    skew = PropertyTypeAssignment(
        code="CAMERA_SKEW",
        data_type="REAL",
        property_label="Skew",
        description="Skew term in the camera intrinsic matrix.",
        units="pixel",
        section="Camera Intrinsics",
        mandatory=False,
        prev_versions=["CAMERA_SKEW:v0"],
    )

    radial_distortion_k1 = PropertyTypeAssignment(
        code="RADIAL_DISTORTION_K1",
        data_type="REAL",
        property_label="Radial distortion k1",
        description="First radial distortion coefficient.",
        section="Lens Distortion",
        mandatory=False,
        prev_versions=["RADIAL_DISTORTION_K1:v0"],
    )

    radial_distortion_k2 = PropertyTypeAssignment(
        code="RADIAL_DISTORTION_K2",
        data_type="REAL",
        property_label="Radial distortion k2",
        description="Second radial distortion coefficient.",
        section="Lens Distortion",
        mandatory=False,
        prev_versions=["RADIAL_DISTORTION_K2:v0"],
    )

    radial_distortion_k3 = PropertyTypeAssignment(
        code="RADIAL_DISTORTION_K3",
        data_type="REAL",
        property_label="Radial distortion k3",
        description="Third radial distortion coefficient.",
        section="Lens Distortion",
        mandatory=False,
        prev_versions=["RADIAL_DISTORTION_K3:v0"],
    )

    radial_distortion_k4 = PropertyTypeAssignment(
        code="RADIAL_DISTORTION_K4",
        data_type="REAL",
        property_label="Radial distortion k4",
        description="Fourth radial distortion coefficient, used by the rational model.",
        section="Lens Distortion",
        mandatory=False,
        prev_versions=["RADIAL_DISTORTION_K4:v0"],
    )

    radial_distortion_k5 = PropertyTypeAssignment(
        code="RADIAL_DISTORTION_K5",
        data_type="REAL",
        property_label="Radial distortion k5",
        description="Fifth radial distortion coefficient, used by the rational model.",
        section="Lens Distortion",
        mandatory=False,
        prev_versions=["RADIAL_DISTORTION_K5:v0"],
    )

    radial_distortion_k6 = PropertyTypeAssignment(
        code="RADIAL_DISTORTION_K6",
        data_type="REAL",
        property_label="Radial distortion k6",
        description="Sixth radial distortion coefficient, used by the rational model.",
        section="Lens Distortion",
        mandatory=False,
        prev_versions=["RADIAL_DISTORTION_K6:v0"],
    )

    tangential_distortion_p1 = PropertyTypeAssignment(
        code="TANGENTIAL_DISTORTION_P1",
        data_type="REAL",
        property_label="Tangential distortion p1",
        description="First tangential distortion coefficient.",
        section="Lens Distortion",
        mandatory=False,
        prev_versions=["TANGENTIAL_DISTORTION_P1:v0"],
    )

    tangential_distortion_p2 = PropertyTypeAssignment(
        code="TANGENTIAL_DISTORTION_P2",
        data_type="REAL",
        property_label="Tangential distortion p2",
        description="Second tangential distortion coefficient.",
        section="Lens Distortion",
        mandatory=False,
        prev_versions=["TANGENTIAL_DISTORTION_P2:v0"],
    )

    thin_prism_distortion_s1 = PropertyTypeAssignment(
        code="THIN_PRISM_DISTORTION_S1",
        data_type="REAL",
        property_label="Thin-prism distortion s1",
        description="First thin-prism distortion coefficient.",
        section="Lens Distortion",
        mandatory=False,
        prev_versions=["THIN_PRISM_DISTORTION_S1:v0"],
    )

    thin_prism_distortion_s2 = PropertyTypeAssignment(
        code="THIN_PRISM_DISTORTION_S2",
        data_type="REAL",
        property_label="Thin-prism distortion s2",
        description="Second thin-prism distortion coefficient.",
        section="Lens Distortion",
        mandatory=False,
        prev_versions=["THIN_PRISM_DISTORTION_S2:v0"],
    )

    thin_prism_distortion_s3 = PropertyTypeAssignment(
        code="THIN_PRISM_DISTORTION_S3",
        data_type="REAL",
        property_label="Thin-prism distortion s3",
        description="Third thin-prism distortion coefficient.",
        section="Lens Distortion",
        mandatory=False,
        prev_versions=["THIN_PRISM_DISTORTION_S3:v0"],
    )

    thin_prism_distortion_s4 = PropertyTypeAssignment(
        code="THIN_PRISM_DISTORTION_S4",
        data_type="REAL",
        property_label="Thin-prism distortion s4",
        description="Fourth thin-prism distortion coefficient.",
        section="Lens Distortion",
        mandatory=False,
        prev_versions=["THIN_PRISM_DISTORTION_S4:v0"],
    )

    sensor_tilt_tau_x = PropertyTypeAssignment(
        code="SENSOR_TILT_TAU_X",
        data_type="REAL",
        property_label="Sensor tilt tau x",
        description="Sensor tilt parameter about the x-axis.",
        units="rad",
        section="Lens Distortion",
        mandatory=False,
        prev_versions=["SENSOR_TILT_TAU_X:v0"],
    )

    sensor_tilt_tau_y = PropertyTypeAssignment(
        code="SENSOR_TILT_TAU_Y",
        data_type="REAL",
        property_label="Sensor tilt tau y",
        description="Sensor tilt parameter about the y-axis.",
        units="rad",
        section="Lens Distortion",
        mandatory=False,
        prev_versions=["SENSOR_TILT_TAU_Y:v0"],
    )

    image_width = PropertyTypeAssignment(
        code="CALIBRATION_IMAGE_WIDTH",
        data_type="INTEGER",
        property_label="Image width",
        description="Width of the images used for calibration.",
        units="pixel",
        section="Calibration Details",
        mandatory=False,
        prev_versions=["CALIBRATION_IMAGE_WIDTH:v0"],
    )

    image_height = PropertyTypeAssignment(
        code="CALIBRATION_IMAGE_HEIGHT",
        data_type="INTEGER",
        property_label="Image height",
        description="Height of the images used for calibration.",
        units="pixel",
        section="Calibration Details",
        mandatory=False,
        prev_versions=["CALIBRATION_IMAGE_HEIGHT:v0"],
    )

    rms_reprojection_error = PropertyTypeAssignment(
        code="RMS_REPROJECTION_ERROR",
        data_type="REAL",
        property_label="RMS reprojection error",
        description="Overall root-mean-square reprojection error.",
        units="pixel",
        section="Calibration Details",
        mandatory=False,
        prev_versions=["RMS_REPROJECTION_ERROR:v0"],
    )


# ----- Sample
class Component(Sample):
    defs = ObjectTypeDef(
        code="COMPONENT",
        description="An assembly that can contain multiple weldments.",
        generated_code_prefix="",
    )


class Weldment(Sample):
    defs = ObjectTypeDef(
        code="WELDMENT",
        description="An assembly incorporating one or more welded joints that can form part of a component.",
        generated_code_prefix="WELDMENT",
    )


class WeldingJoint(Sample):
    defs = ObjectTypeDef(
        code="WELDING_JOINT",
        description="""physical layout of the workpieces AND resulting groove preparation (e.g. Butt joint + V-Groove), ISO/TR 25901-1:2016  joint (2.1.4.1)""",
        generated_code_prefix="",
    )

    joint_status = PropertyTypeAssignment(
        code="JOINT_STATUS",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="WELDING_JOINT_STATES",
        property_label="Joint status",
        description="Current state of the welding joint.",
        section="Joint Details",
        mandatory=False,
        prev_versions=["JOINT_STATUS:v0"],
    )

    joint_type = PropertyTypeAssignment(
        code="JOINT_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="JOINT_TYPES",
        property_label="Joint type",
        description="Arrangement of the workpieces in the welding joint.",
        section="Joint Details",
        mandatory=False,
        prev_versions=["JOINT_TYPE:v0"],
    )

    groove_type = PropertyTypeAssignment(
        code="GROOVE_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="GROOVE_TYPES",
        property_label="Groove type",
        description="Groove preparation identified by its unique code number and type name.",
        section="Groove Preparation",
        mandatory=False,
        prev_versions=["GROOVE_TYPE:v0"],
    )

    workpiece_thickness = PropertyTypeAssignment(
        code="WORKPIECE_THICKNESS",
        data_type="REAL",
        property_label="Workpiece thickness",
        description="Thickness of the first workpiece.",
        units="mm",
        section="Groove Preparation",
        mandatory=False,
        prev_versions=["WORKPIECE_THICKNESS:v0"],
    )

    workpiece_thickness2 = PropertyTypeAssignment(
        code="WORKPIECE_THICKNESS_2",
        data_type="REAL",
        property_label="Workpiece thickness 2",
        description="Thickness of the second workpiece.",
        units="mm",
        section="Groove Preparation",
        mandatory=False,
        prev_versions=["WORKPIECE_THICKNESS_2:v0"],
    )

    root_gap = PropertyTypeAssignment(
        code="ROOT_GAP",
        data_type="REAL",
        property_label="Root gap",
        description="Gap between the workpieces at the joint root.",
        units="mm",
        section="Groove Preparation",
        mandatory=False,
        prev_versions=["ROOT_GAP:v0"],
    )

    root_face = PropertyTypeAssignment(
        code="ROOT_FACE",
        data_type="REAL",
        property_label="Root face",
        description="Dimension of the root face of the joint preparation.",
        units="mm",
        section="Groove Preparation",
        mandatory=False,
        prev_versions=["ROOT_FACE:v0"],
    )

    root_face2 = PropertyTypeAssignment(
        code="ROOT_FACE_2",
        data_type="REAL",
        property_label="Root face 2",
        description="Dimension of the second root face of the joint preparation.",
        units="mm",
        section="Groove Preparation",
        mandatory=False,
        prev_versions=["ROOT_FACE_2:v0"],
    )

    root_face3 = PropertyTypeAssignment(
        code="ROOT_FACE_3",
        data_type="REAL",
        property_label="Root face 3",
        description="Dimension of the third root face of the joint preparation.",
        units="mm",
        section="Groove Preparation",
        mandatory=False,
        prev_versions=["ROOT_FACE_3:v0"],
    )

    bevel_radius = PropertyTypeAssignment(
        code="BEVEL_RADIUS",
        data_type="REAL",
        property_label="Bevel radius",
        description="Radius of the bevel in the joint preparation.",
        units="mm",
        section="Groove Preparation",
        mandatory=False,
        prev_versions=["BEVEL_RADIUS:v0"],
    )

    bevel_radius2 = PropertyTypeAssignment(
        code="BEVEL_RADIUS_2",
        data_type="REAL",
        property_label="Bevel radius 2",
        description="Radius of the second bevel in the joint preparation.",
        units="mm",
        section="Groove Preparation",
        mandatory=False,
        prev_versions=["BEVEL_RADIUS_2:v0"],
    )

    bevel_angle = PropertyTypeAssignment(
        code="BEVEL_ANGLE",
        data_type="REAL",
        property_label="Bevel angle",
        description="Angle of the bevel in the joint preparation.",
        units="deg",
        section="Groove Preparation",
        mandatory=False,
        prev_versions=["BEVEL_ANGLE:v0"],
    )

    bevel_angle2 = PropertyTypeAssignment(
        code="BEVEL_ANGLE_2",
        data_type="REAL",
        property_label="Bevel angle 2",
        description="Angle of the second bevel in the joint preparation.",
        units="deg",
        section="Groove Preparation",
        mandatory=False,
        prev_versions=["BEVEL_ANGLE_2:v0"],
    )

    groove_angle = PropertyTypeAssignment(
        code="GROOVE_ANGLE",
        data_type="REAL",
        property_label="Groove angle",
        description="Angle of the groove in the joint preparation.",
        units="deg",
        section="Groove Preparation",
        mandatory=False,
        prev_versions=["GROOVE_ANGLE:v0"],
    )

    groove_angle2 = PropertyTypeAssignment(
        code="GROOVE_ANGLE_2",
        data_type="REAL",
        property_label="Groove angle 2",
        description="Angle of the second groove in the joint preparation.",
        units="deg",
        section="Groove Preparation",
        mandatory=False,
        prev_versions=["GROOVE_ANGLE_2:v0"],
    )

    special_depth = PropertyTypeAssignment(
        code="SPECIAL_DEPTH",
        data_type="REAL",
        property_label="Special depth",
        description="Special depth used for the 4.1.2 Frontal-Face-Groove type.",
        units="mm",
        section="Groove Preparation",
        mandatory=False,
        prev_versions=["SPECIAL_DEPTH:v0"],
    )


class Workpiece(Sample):
    defs = ObjectTypeDef(
        code="WORKPIECE",
        description="""a single metallic plate, sheet, tube or similarly shaped sample""",
        generated_code_prefix="",
        prev_versions=["RAW_MATERIAL.STEEL:v0", "RAW_MATERIAL.ALUMINIUM:v0"],
    )

    lot_number = Sample.lot_number.model_copy(
        update={"prev_versions": ["LOT_NUMBER:v0", "RAW_MAT_BATCH_NUMBER:v0"]},
    )

    workpiece_alloy = PropertyTypeAssignment(
        code="WORKPIECE_ALLOY",
        data_type="OBJECT",
        object_code="METALLIC_ALLOY",
        property_label="Workpiece alloy",
        description="Alloy grade of the workpiece.",
        section="Material",
        mandatory=False,
        prev_versions=["MAT_CODE:v0"],
    )

    workpiece_form = PropertyTypeAssignment(
        code="WORKPIECE_FORM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="RAW_MAT_FORM",
        property_label="Workpiece form",
        description="Product form of the workpiece, such as plate, sheet, pipe, or bar.",
        section="Geometry",
        mandatory=False,
        prev_versions=["RAW_MAT_FORM:v0"],
    )

    workpiece_length = PropertyTypeAssignment(
        code="WORKPIECE_LENGTH",
        data_type="REAL",
        property_label="Workpiece length",
        description="Length of the individual workpiece.",
        units="mm",
        section="Geometry",
        mandatory=False,
        prev_versions=["RAW_MAT_LENGTH:v0"],
    )

    workpiece_width = PropertyTypeAssignment(
        code="WORKPIECE_WIDTH",
        data_type="REAL",
        property_label="Workpiece width",
        description="Width of the individual workpiece.",
        units="mm",
        section="Geometry",
        mandatory=False,
        prev_versions=["RAW_MAT_WIDTH:v0"],
    )

    workpiece_section_thickness = PropertyTypeAssignment(
        code="WORKPIECE_SECTION_THICKNESS",
        data_type="REAL",
        property_label="Workpiece section thickness",
        description="Plate or sheet thickness, or wall thickness for a hollow workpiece.",
        units="mm",
        section="Geometry",
        mandatory=False,
        prev_versions=["RAW_MAT_THICKNESS:v0"],
    )

    workpiece_outer_diameter = PropertyTypeAssignment(
        code="WORKPIECE_OUTER_DIAMETER",
        data_type="REAL",
        property_label="Workpiece outer diameter",
        description="Outside diameter of a round or tubular workpiece.",
        units="mm",
        section="Geometry",
        mandatory=False,
        prev_versions=["RAW_MAT_DIAMETER:v0"],
    )

    # TODO: Combine the treatment slots when multivalued properties are supported.

    workpiece_treatment_first = PropertyTypeAssignment(
        code="WORKPIECE_TREATMENT_FIRST",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="WORKPIECE_TREATMENT",
        property_label="First treatment",
        description="First treatment recorded for the workpiece.",
        section="Delivery Condition",
        mandatory=False,
        prev_versions=["STEEL_TREATMENT_FIRST:v0", "ALU_TREATMENT_FIRST:v0"],
    )

    workpiece_treatment_second = PropertyTypeAssignment(
        code="WORKPIECE_TREATMENT_SECOND",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="WORKPIECE_TREATMENT",
        property_label="Second treatment",
        description="Second treatment recorded for the workpiece.",
        section="Delivery Condition",
        mandatory=False,
        prev_versions=["STEEL_TREATMENT_SECOND:v0", "ALU_TREATMENT_SECOND:v0"],
    )

    workpiece_treatment_third = PropertyTypeAssignment(
        code="WORKPIECE_TREATMENT_THIRD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="WORKPIECE_TREATMENT",
        property_label="Third treatment",
        description="Third treatment recorded for the workpiece.",
        section="Delivery Condition",
        mandatory=False,
        prev_versions=["STEEL_TREATMENT_THIRD:v0", "ALU_TREATMENT_THIRD:v0"],
    )

    workpiece_treatment_fourth = PropertyTypeAssignment(
        code="WORKPIECE_TREATMENT_FOURTH",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="WORKPIECE_TREATMENT",
        property_label="Fourth treatment",
        description="Fourth treatment recorded for the workpiece.",
        section="Delivery Condition",
        mandatory=False,
        prev_versions=["STEEL_TREATMENT_FOURTH:v0", "ALU_TREATMENT_FOURTH:v0"],
    )


class Weld(Sample):
    defs = ObjectTypeDef(
        code="WELD",
        description="""result of welding (2.1.1.1) Note 1 to entry: The weld includes the weld metal (2.1.2.1) and the heat-affected zone (2.1.2.2).""",
        generated_code_prefix="",
    )


# ----- Material
class MetallicAlloy(Material):
    defs = ObjectTypeDef(
        code="METALLIC_ALLOY",
        description="""A general metallic alloy with material numbers, name and additional treatment specifiers according to ISO standards or VDEh""",
        generated_code_prefix="",
        prev_versions=["RAW_MATERIAL_CODE:v0"],
    )
    # Legacy MATERIAL_NUMBER is represented by the inherited MATERIAL_ID.
    # Standards used:
    # aluminium (DIN EN 573 / Teal Sheets)
    # steel (EN 10027-2)
    # nickel (EN 10269)
    # titanium (DIN 17860 ?)

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative name",
        description="Alternative name, abbreviation, or nickname for the alloy.",
        section="Material Details",
        mandatory=False,
    )

    material_group = PropertyTypeAssignment(
        code="MATERIAL_GROUP",
        data_type="VARCHAR",
        property_label="Material group",
        description="Material group.",
        section="Material Details",
        mandatory=False,
    )

    characteristics = PropertyTypeAssignment(
        code="CHARACTERISTICS",
        data_type="VARCHAR",
        property_label="Characteristics",
        description="Characteristics of the alloy.",
        section="Material Details",
        mandatory=False,
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="Additional notes about the alloy.",
        section="Additional Information",
        mandatory=False,
    )


class GasMixture(Material):
    defs = ObjectTypeDef(
        code="GAS_MIXTURE",
        description="""Generic gas mixture [vol-%] e.g. shielding gas EN ISO 14175""",
        generated_code_prefix="",
    )

    argon = PropertyTypeAssignment(
        code="ARGON",
        data_type="REAL",
        property_label="Argon",
        description="Volume fraction of argon (Ar) in the mixture.",
        units="percent",
        section="Gas Composition",
        mandatory=False,
        prev_versions=["VOLUME_PERCENT_ARGON:v0"],
    )

    helium = PropertyTypeAssignment(
        code="HELIUM",
        data_type="REAL",
        property_label="Helium",
        description="Volume fraction of helium (He) in the mixture.",
        units="percent",
        section="Gas Composition",
        mandatory=False,
        prev_versions=["VOLUME_PERCENT_HELIUM:v0"],
    )

    carbon_dioxide = PropertyTypeAssignment(
        code="CARBON_DIOXIDE",
        data_type="REAL",
        property_label="Carbon dioxide",
        description="Volume fraction of carbon dioxide (CO2) in the mixture.",
        units="percent",
        section="Gas Composition",
        mandatory=False,
        prev_versions=["VOLUME_PERCENT_CARBON_DIOXIDE:v0"],
    )

    oxygen = PropertyTypeAssignment(
        code="OXYGEN",
        data_type="REAL",
        property_label="Oxygen",
        description="Volume fraction of oxygen (O2) in the mixture.",
        units="percent",
        section="Gas Composition",
        mandatory=False,
        prev_versions=["VOLUME_PERCENT_OXYGEN:v0"],
    )

    nitrogen = PropertyTypeAssignment(
        code="NITROGEN",
        data_type="REAL",
        property_label="Nitrogen",
        description="Volume fraction of nitrogen (N2) in the mixture.",
        units="percent",
        section="Gas Composition",
        mandatory=False,
        prev_versions=["VOLUME_PERCENT_NITROGEN:v0"],
    )

    hydrogen = PropertyTypeAssignment(
        code="HYDROGEN",
        data_type="REAL",
        property_label="Hydrogen",
        description="Volume fraction of hydrogen (H2) in the mixture.",
        units="percent",
        section="Gas Composition",
        mandatory=False,
        prev_versions=["VOLUME_PERCENT_HYDROGEN:v0"],
    )

    mixture_standard = PropertyTypeAssignment(
        code="MIXTURE_STANDARD",
        data_type="VARCHAR",
        property_label="Mixture standard",
        description="Standard and edition used to classify the mixture.",
        section="Mixture Identification",
        mandatory=False,
        prev_versions=["MIXTURE_STANDARD:v0"],
    )

    mixture_designation = PropertyTypeAssignment(
        code="MIXTURE_DESIGNATION",
        data_type="VARCHAR",
        property_label="Mixture designation",
        description="Designation of the mixture according to the specified standard.",
        section="Mixture Identification",
        mandatory=False,
        prev_versions=["MIXTURE_DESIGNATION:v0"],
    )


class WeldingWireAlloy(Material):
    defs = ObjectTypeDef(
        code="WELDING_WIRE_ALLOY",
        description="""Standardized welding wire alloy names (all materials)""",
        generated_code_prefix="",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative name",
        description="Alternative name, abbreviation, or nickname for the alloy.",
        section="Material Details",
        mandatory=False,
        prev_versions=["ALIAS:v0"],
    )

    material_group = PropertyTypeAssignment(
        code="MATERIAL_GROUP",
        data_type="VARCHAR",
        property_label="Material group",
        description="Material group.",
        section="Material Details",
        mandatory=False,
        prev_versions=["MATERIAL_GROUP:v0"],
    )

    characteristics = PropertyTypeAssignment(
        code="CHARACTERISTICS",
        data_type="VARCHAR",
        property_label="Characteristics",
        description="Characteristics of the alloy.",
        section="Material Details",
        mandatory=False,
        prev_versions=["CHARACTERISTICS:v0"],
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="Additional notes about the alloy.",
        section="Additional Information",
        mandatory=False,
        prev_versions=["NOTES:v0"],
    )

    alloy_standard = PropertyTypeAssignment(
        code="ALLOY_STANDARD",
        data_type="VARCHAR",
        property_label="Alloy standard",
        description="Standard and edition used to classify the welding wire alloy.",
        section="Alloy Identification",
        mandatory=False,
        prev_versions=["ALLOY_STANDARD:v0"],
    )

    alloy_designation = PropertyTypeAssignment(
        code="ALLOY_DESIGNATION",
        data_type="VARCHAR",
        property_label="Alloy designation",
        description="Designation of the welding wire alloy according to the specified standard.",
        section="Alloy Identification",
        mandatory=False,
        prev_versions=["ALLOY_DESIGNATION:v0"],
    )


# Equipment
class GmawWeldingPowerSource(Instrument):
    defs = ObjectTypeDef(
        code="GMAW_WELDING_POWER_SOURCE",
        prev_versions=["INSTRUMENT.WELDING_EQUIPMENT.GMAW_WELDING_POWER_SOURCE:v0"],
        description="""Power source for gas metal arc welding (GMAW) applications""",
        generated_code_prefix="GMAW_WELDING_POWER_SOURCE",
    )

    welding_arc_current_min = PropertyTypeAssignment(
        code="ARC_CURRENT_MIN",
        data_type="REAL",
        property_label="Arc current minimum",
        description="""Minimum arc current""",
        units="A",
        section="Power Source Information",
        mandatory=False,
        prev_versions=["WELDING.ARC_CURRENT_MIN:v0"],
    )

    welding_arc_current_max = PropertyTypeAssignment(
        code="ARC_CURRENT_MAX",
        data_type="REAL",
        property_label="Arc current maximum",
        description="""Maximum arc current""",
        units="A",
        section="Power Source Information",
        mandatory=False,
        prev_versions=["WELDING.ARC_CURRENT_MAX:v0"],
    )

    welding_arc_current_continuous = PropertyTypeAssignment(
        code="ARC_CURRENT_CONTINUOUS",
        data_type="REAL",
        property_label="Maximum continuous arc current",
        description="""Maximum continuous arc current at 100% duty cycle""",
        units="A",
        section="Power Source Information",
        mandatory=False,
        prev_versions=["WELDING.ARC_CURRENT_CONTINUOUS:v0"],
    )

    firmware_version = PropertyTypeAssignment(
        code="FIRMWARE_VERSION",
        data_type="VARCHAR",
        property_label="Firmware version",
        description="Currently installed firmware version.",
        section="Software Information",
        mandatory=False,
        prev_versions=["FIRMWARE_VERSION:v0"],
    )

    last_systemcheck = PropertyTypeAssignment(
        code="LAST_SYSTEMCHECK",
        data_type="DATE",
        property_label="Last system check",
        description="Date of the most recent system check.",
        section="Additional Information",
        mandatory=False,
        prev_versions=["LAST_SYSTEMCHECK:v0"],
    )


class Positioner(Equipment):
    defs = ObjectTypeDef(
        code="POSITIONER",
        prev_versions=["INSTRUMENT.WELDING_EQUIPMENT.POSITIONER:v0"],
        description="""A generic welding table or handling device""",
        generated_code_prefix="POSITIONER",
    )

    positioner_type = PropertyTypeAssignment(
        code="POSITIONER_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="POSITIONER_TYPE",
        property_label="Positioner type",
        description="""Positioner type""",
        section="Positioner Information",
        mandatory=False,
        prev_versions=["POSITIONER_TYPE:v0"],
    )

    positioner_axis_count = PropertyTypeAssignment(
        code="POSITIONER_AXIS_COUNT",
        data_type="INTEGER",
        property_label="Number of axis",
        description="""The number of controllable axis of the positioner (a value of 0 indicates static positioner)""",
        section="Positioner Information",
        mandatory=False,
        prev_versions=["POSITIONER_AXIS_COUNT:v0"],
    )

    positioner_payload_max = PropertyTypeAssignment(
        code="POSITIONER_PAYLOAD_MAX",
        data_type="REAL",
        property_label="Maximum payload",
        description="""The maximum payload to be handled by the positioner""",
        units="kg",
        section="Positioner Information",
        mandatory=False,
        prev_versions=["POSITIONER_PAYLOAD_MAX:v0"],
    )

    last_systemcheck = PropertyTypeAssignment(
        code="LAST_SYSTEMCHECK",
        data_type="DATE",
        property_label="Last system check",
        description="Date of the most recent system check.",
        section="Additional Information",
        mandatory=False,
        prev_versions=["LAST_SYSTEMCHECK:v0"],
    )


class RobotController(Equipment):
    defs = ObjectTypeDef(
        code="ROBOT_CONTROLLER",
        prev_versions=["INSTRUMENT.WELDING_EQUIPMENT.ROBOT_CONTROLLER:v0"],
        description="""Controller connected to a welding robot""",
        generated_code_prefix="ROBOT_CONTROLLER",
    )

    robot_controller_axis_count = PropertyTypeAssignment(
        code="ROBOT_CONTROLLER_AXIS_COUNT",
        data_type="INTEGER",
        property_label="Number of robot axis",
        description="""The number of robot axis the controller can operate""",
        section="Controller Information",
        mandatory=False,
        prev_versions=["ROBOT_CONTROLLER_AXIS_COUNT:v0"],
    )

    robot_controller_axis_count_external = PropertyTypeAssignment(
        code="ROBOT_CONTROLLER_AXIS_COUNT_EXTERNAL",
        data_type="INTEGER",
        property_label="Number of external axis",
        description="""The number of external axis the controller can operate""",
        section="Controller Information",
        mandatory=False,
        prev_versions=["ROBOT_CONTROLLER_AXIS_COUNT_EXTERNAL:v0"],
    )

    firmware_version = PropertyTypeAssignment(
        code="FIRMWARE_VERSION",
        data_type="VARCHAR",
        property_label="Firmware version",
        description="Currently installed firmware version.",
        section="Software Information",
        mandatory=False,
        prev_versions=["FIRMWARE_VERSION:v0"],
    )

    last_systemcheck = PropertyTypeAssignment(
        code="LAST_SYSTEMCHECK",
        data_type="DATE",
        property_label="Last system check",
        description="Date of the most recent system check.",
        section="Additional Information",
        mandatory=False,
        prev_versions=["LAST_SYSTEMCHECK:v0"],
    )


class Robot(Instrument):
    defs = ObjectTypeDef(
        code="ROBOT",
        prev_versions=["INSTRUMENT.WELDING_EQUIPMENT.ROBOT:v0"],
        description="""A generic robot used for welding""",
        generated_code_prefix="ROBOT",
    )

    robot_type = PropertyTypeAssignment(
        code="ROBOT_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="ROBOT_TYPE",
        property_label="Type of Robot",
        description="""Type of Robot""",
        section="Robot Information",
        mandatory=False,
        prev_versions=["ROBOT_TYPE:v0"],
    )

    robot_payload_max = PropertyTypeAssignment(
        code="ROBOT_PAYLOAD_MAX",
        data_type="INTEGER",
        property_label="Robot maximum payload",
        description="""The maximum allowable payload of the robot""",
        units="kg",
        section="Robot Information",
        mandatory=False,
        prev_versions=["ROBOT_PAYLOAD_MAX:v0"],
    )

    robot_working_range = PropertyTypeAssignment(
        code="ROBOT_WORKING_RANGE",
        data_type="REAL",
        property_label="Maximum working range",
        description="""The maximum specified working range of the robot (in mm)""",
        units="mm",
        section="Robot Information",
        mandatory=False,
        prev_versions=["ROBOT_WORKING_RANGE:v0"],
    )

    robot_axis_count = PropertyTypeAssignment(
        code="ROBOT_AXIS_COUNT",
        data_type="INTEGER",
        property_label="Number of robot axis",
        description="""The number of a axis on the robot""",
        section="Robot Information",
        mandatory=False,
        prev_versions=["ROBOT_AXIS_COUNT:v0"],
    )

    last_systemcheck = PropertyTypeAssignment(
        code="LAST_SYSTEMCHECK",
        data_type="DATE",
        property_label="Last system check",
        description="Date of the most recent system check.",
        section="Additional Information",
        mandatory=False,
        prev_versions=["LAST_SYSTEMCHECK:v0"],
    )


class StationLayout(Equipment):
    defs = ObjectTypeDef(
        code="STATION_LAYOUT",
        prev_versions=["INSTRUMENT.WELDING_EQUIPMENT.STATION_LAYOUT:v0"],
        description="""Layout and configuration of a welding station""",
        generated_code_prefix="STATION_LAYOUT",
    )

    last_systemcheck = PropertyTypeAssignment(
        code="LAST_SYSTEMCHECK",
        data_type="DATE",
        property_label="Last system check",
        description="Date of the most recent system check.",
        section="Additional Information",
        mandatory=False,
        prev_versions=["LAST_SYSTEMCHECK:v0"],
    )


class TorchHead(Equipment):
    defs = ObjectTypeDef(
        code="TORCH_HEAD",
        description="A torch head used for gas metal arc welding.",
        generated_code_prefix="TORCH_HEAD",
        prev_versions=["INSTRUMENT.WELDING_EQUIPMENT.GMAW_TORCH:v0"],
    )

    welding_torch_type = PropertyTypeAssignment(
        code="WELDING_TORCH_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="GMAW_TORCH_TYPE",
        property_label="Torch type",
        description="Type of gas metal arc welding torch.",
        section="General Information",
        mandatory=False,
        prev_versions=["WELDING.TORCH_TYPE:v0"],
    )

    last_systemcheck = PropertyTypeAssignment(
        code="LAST_SYSTEMCHECK",
        data_type="DATE",
        property_label="Last system check",
        description="Date of the most recent system check.",
        section="Additional Information",
        mandatory=False,
        prev_versions=["LAST_SYSTEMCHECK:v0"],
    )


class WeldingTorchNeck(Equipment):
    defs = ObjectTypeDef(
        code="WELDING_TORCH_NECK",
        description="""arc welding torch neck component (can be generic type or specific)""",
        generated_code_prefix="",
    )


class WeldingGasNozzel(Equipment):
    defs = ObjectTypeDef(
        code="WELDING_GAS_NOZZEL",
        description="""arc welding torch gas nozzel (can be generic type or specific)""",
        generated_code_prefix="",
    )


class WeldingContactTip(Equipment):
    defs = ObjectTypeDef(
        code="WELDING_CONTACT_TIP",
        description="""arc welding or wire contact tip (can be generic type or specific)""",
        generated_code_prefix="",
    )


# -------------------------
# LASER
# -------------------------


class Camera(Sensor):
    defs = ObjectTypeDef(
        code="CAMERA",
        description="A camera for recording still images or video.",
        generated_code_prefix="CAMERA",
        prev_versions=["INSTRUMENT.CAMERA:v0"],
    )

    image_sensor_name = PropertyTypeAssignment(
        code="IMAGE_SENSOR_NAME",
        data_type="VARCHAR",
        property_label="Image sensor model",
        description="Model designation of the image sensor.",
        section="Camera Information",
        mandatory=False,
        prev_versions=["IMAGE_SENSOR_NAME:v0"],
    )

    image_sensor_size = PropertyTypeAssignment(
        code="IMAGE_SENSOR_SIZE",
        data_type="VARCHAR",
        property_label="Image sensor size",
        description="Size or format designation of the image sensor.",
        section="Camera Information",
        mandatory=False,
        prev_versions=["IMAGE_SENSOR_SIZE:v0"],
    )

    image_sensor_resolution_horizontal = PropertyTypeAssignment(
        code="IMAGE_SENSOR_RESOLUTION_HORIZONTAL",
        data_type="INTEGER",
        property_label="Horizontal sensor resolution",
        description="Number of pixels across the sensor image.",
        units="pixel",
        section="Camera Information",
        mandatory=False,
        prev_versions=["IMAGE_SENSOR_RESOLUTION_HORIZONTAL:v0"],
    )

    image_sensor_resolution_vertical = PropertyTypeAssignment(
        code="IMAGE_SENSOR_RESOLUTION_VERTICAL",
        data_type="INTEGER",
        property_label="Vertical sensor resolution",
        description="Number of pixels down the sensor image.",
        units="pixel",
        section="Camera Information",
        mandatory=False,
        prev_versions=["IMAGE_SENSOR_RESOLUTION_VERTICAL:v0"],
    )

    image_sensor_framerate = PropertyTypeAssignment(
        code="IMAGE_SENSOR_FRAMERATE",
        data_type="REAL",
        property_label="Frame rate at full resolution",
        description="Maximum frame rate at full sensor resolution, expressed in frames per second.",
        units="Hz",
        section="Camera Information",
        mandatory=False,
        prev_versions=["IMAGE_SENSOR_FRAMERATE:v0"],
    )

    lens_mount_type = PropertyTypeAssignment(
        code="LENS_MOUNT_TYPE",
        data_type="VARCHAR",
        property_label="Lens mount",
        description="Mount type used to connect the lens and camera.",
        section="Optics",
        mandatory=False,
        prev_versions=["LENS_MOUNT_TYPE:v0"],
    )

    firmware_version = PropertyTypeAssignment(
        code="FIRMWARE_VERSION",
        data_type="VARCHAR",
        property_label="Firmware version",
        description="Currently installed firmware version.",
        section="Software Information",
        mandatory=False,
        prev_versions=["FIRMWARE_VERSION:v0"],
    )

    last_systemcheck = PropertyTypeAssignment(
        code="LAST_SYSTEMCHECK",
        data_type="DATE",
        property_label="Last system check",
        description="Date of the most recent system check.",
        section="Additional Information",
        mandatory=False,
        prev_versions=["LAST_SYSTEMCHECK:v0"],
    )


class Lens(Equipment):
    defs = ObjectTypeDef(
        code="LENS",
        description="An optical lens used with an imaging camera.",
        generated_code_prefix="LENS",
        prev_versions=["INSTRUMENT.CAMERA.LENS:v0"],
    )

    lens_mount_type = PropertyTypeAssignment(
        code="LENS_MOUNT_TYPE",
        data_type="VARCHAR",
        property_label="Lens mount",
        description="Mount type used to connect the lens and camera.",
        section="Optics",
        mandatory=False,
        prev_versions=["LENS_MOUNT_TYPE:v0"],
    )

    lens_focallength = PropertyTypeAssignment(
        code="LENS_FOCALLENGTH",
        data_type="REAL",
        property_label="Focal length",
        description="Focal length of the lens.",
        units="mm",
        section="Lens Information",
        mandatory=False,
        prev_versions=["LENS_FOCALLENGTH:v0"],
    )

    lens_aperture_max = PropertyTypeAssignment(
        code="LENS_APERTURE_MAX",
        data_type="REAL",
        property_label="Maximum aperture",
        description="F-number at the widest aperture.",
        section="Lens Information",
        mandatory=False,
        prev_versions=["LENS_APERTURE_MAX:v0"],
    )

    lens_aperture_min = PropertyTypeAssignment(
        code="LENS_APERTURE_MIN",
        data_type="REAL",
        property_label="Minimum aperture",
        description="F-number at the narrowest aperture.",
        section="Lens Information",
        mandatory=False,
        prev_versions=["LENS_APERTURE_MIN:v0"],
    )

    lens_confocal = PropertyTypeAssignment(
        code="LENS_CONFOCAL",
        data_type="BOOLEAN",
        property_label="Confocal optics",
        description="Whether the lens uses confocal optics.",
        section="Lens Information",
        mandatory=False,
        prev_versions=["LENS_CONFOCAL:v0"],
    )


class LaserLineScanner(Sensor):
    defs = ObjectTypeDef(
        code="LASER_LINE_SCANNER",
        description="A scanner that measures two-dimensional profiles along a laser line.",
        generated_code_prefix="LASER_LINE_SCANNER",
        prev_versions=["INSTRUMENT.LASER_LINE_SCANNER:v0"],
    )

    z_min = PropertyTypeAssignment(
        code="LASER_SCANNER_Z_MIN",
        data_type="REAL",
        property_label="Minimum Z distance",
        description="Lower measurement distance along the depth axis.",
        units="mm",
        section="Measurement Range",
        mandatory=False,
        prev_versions=["INSTRUMENT.LASER_SCANNER.Z_MIN:v0"],
    )

    z_max = PropertyTypeAssignment(
        code="LASER_SCANNER_Z_MAX",
        data_type="REAL",
        property_label="Maximum Z distance",
        description="Upper measurement distance along the depth axis.",
        units="mm",
        section="Measurement Range",
        mandatory=False,
        prev_versions=["INSTRUMENT.LASER_SCANNER.Z_MAX:v0"],
    )

    x_min = PropertyTypeAssignment(
        code="LASER_SCANNER_X_MIN",
        data_type="REAL",
        property_label="Minimum X position",
        description="Lower lateral measurement limit along the laser line.",
        units="mm",
        section="Measurement Range",
        mandatory=False,
        prev_versions=["INSTRUMENT.LASER_SCANNER.X_MIN:v0"],
    )

    x_max = PropertyTypeAssignment(
        code="LASER_SCANNER_X_MAX",
        data_type="REAL",
        property_label="Maximum X position",
        description="Upper lateral measurement limit along the laser line.",
        units="mm",
        section="Measurement Range",
        mandatory=False,
        prev_versions=["INSTRUMENT.LASER_SCANNER.X_MAX:v0"],
    )

    line_resolution = PropertyTypeAssignment(
        code="LASER_SCANNER_LINE_RESOLUTION",
        data_type="INTEGER",
        property_label="Maximum line resolution",
        description="Maximum number of measurement points per profile.",
        section="Scanner Specifications",
        mandatory=False,
        prev_versions=["INSTRUMENT.LASER_SCANNER.LINE_RESOLUTION:v0"],
    )

    laser_wavelength = PropertyTypeAssignment(
        code="LASER_WAVELENGTH",
        data_type="VARCHAR",
        property_label="Laser wavelength",
        description="Emitted wavelength in nm, recorded as text.",
        section="Scanner Specifications",
        mandatory=False,
        prev_versions=["LASER_WAVELENGTH:v0"],
    )

    laser_class = PropertyTypeAssignment(
        code="LASER_CLASS",
        data_type="VARCHAR",
        property_label="Laser class",
        description="Laser safety classification recorded for the scanner.",
        section="Scanner Specifications",
        mandatory=False,
        prev_versions=["LASER_CLASS:v0"],
    )

    firmware_version = PropertyTypeAssignment(
        code="FIRMWARE_VERSION",
        data_type="VARCHAR",
        property_label="Firmware version",
        description="Currently installed firmware version.",
        section="Software Information",
        mandatory=False,
        prev_versions=["FIRMWARE_VERSION:v0"],
    )

    last_systemcheck = PropertyTypeAssignment(
        code="LAST_SYSTEMCHECK",
        data_type="DATE",
        property_label="Last system check",
        description="Date of the most recent system check.",
        section="Additional Information",
        mandatory=False,
        prev_versions=["LAST_SYSTEMCHECK:v0"],
    )


class LaserSource(Instrument):
    defs = ObjectTypeDef(
        code="LASER_SOURCE",
        description="""Laser beam generator""",
        generated_code_prefix="",
    )

    laser_type = PropertyTypeAssignment(
        code="LASER_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="LASER_TYPES",
        property_label="Laser type",
        description="Type of laser source.",
        section="Laser Specifications",
        mandatory=False,
    )

    laser_gain_medium = PropertyTypeAssignment(
        code="LASER_GAIN_MEDIUM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="LASER_GAIN_MEDIUM",
        property_label="Laser gain medium",
        description="Material that provides optical gain in the laser.",
        section="Laser Specifications",
        mandatory=False,
        prev_versions=["LASER_GAIN_MEDIUM:v0"],
    )

    wavelength = PropertyTypeAssignment(
        code="WAVELENGTH",
        data_type="REAL",
        property_label="Wavelength",
        description="Emission wavelength of the laser.",
        units="nm",
        section="Laser Specifications",
        mandatory=False,
    )

    output_power_max = PropertyTypeAssignment(
        code="OUTPUT_POWER_MAX",
        data_type="REAL",
        property_label="Maximum output power",
        description="Maximum continuous-wave optical output power.",
        units="kW",
        section="Laser Specifications",
        mandatory=False,
    )

    output_power_min = PropertyTypeAssignment(
        code="OUTPUT_POWER_MIN",
        data_type="REAL",
        property_label="Minimum output power",
        description="Minimum continuous-wave optical output power.",
        units="kW",
        section="Laser Specifications",
        mandatory=False,
    )

    bpp = PropertyTypeAssignment(
        code="BPP",
        data_type="REAL",
        property_label="Beam parameter product",
        description="Measure of the quality and focusability of the laser beam.",
        units="mm*mrad",
        section="Laser Specifications",
        mandatory=False,
    )


class Pyrometer(Instrument):
    defs = ObjectTypeDef(
        code="PYROMETER",
        description="""A pyrometer""",
        generated_code_prefix="",
    )

    pyrometer_type = PropertyTypeAssignment(
        code="PYROMETER_TYPE",
        data_type="VARCHAR",
        property_label="Pyrometer type",
        description="Measuring principle, such as single-color or two-color.",
        section="Pyrometer Specifications",
        mandatory=False,
    )

    temperature_min = PropertyTypeAssignment(
        code="TEMPERATURE_MIN",
        data_type="REAL",
        property_label="Minimum temperature",
        description="Lower limit of the measurable temperature range.",
        units="degC",
        section="Pyrometer Specifications",
        mandatory=False,
    )

    temperature_max = PropertyTypeAssignment(
        code="TEMPERATURE_MAX",
        data_type="REAL",
        property_label="Maximum temperature",
        description="Upper limit of the measurable temperature range.",
        units="degC",
        section="Pyrometer Specifications",
        mandatory=False,
    )

    spectral_range_min = PropertyTypeAssignment(
        code="SPECTRAL_RANGE_MIN",
        data_type="REAL",
        property_label="Minimum spectral range",
        description="Lower wavelength limit used for measurement.",
        units="µm",
        section="Pyrometer Specifications",
        mandatory=False,
    )

    spectral_range_max = PropertyTypeAssignment(
        code="SPECTRAL_RANGE_MAX",
        data_type="REAL",
        property_label="Maximum spectral range",
        description="Upper wavelength limit used for measurement.",
        units="µm",
        section="Pyrometer Specifications",
        mandatory=False,
    )

    response_time = PropertyTypeAssignment(
        code="RESPONSE_TIME",
        data_type="REAL",
        property_label="Response time",
        description="Time required to respond to a temperature change.",
        units="ms",
        section="Pyrometer Specifications",
        mandatory=False,
    )

    emissivity_range_min = PropertyTypeAssignment(
        code="EMISSIVITY_RANGE_MIN",
        data_type="REAL",
        property_label="Minimum emissivity",
        description="Lower limit of the adjustable emissivity range.",
        units="percent",
        section="Pyrometer Specifications",
        mandatory=False,
    )

    emissivity_range_max = PropertyTypeAssignment(
        code="EMISSIVITY_RANGE_MAX",
        data_type="REAL",
        property_label="Maximum emissivity",
        description="Upper limit of the adjustable emissivity range.",
        units="percent",
        section="Pyrometer Specifications",
        mandatory=False,
    )


class LoadCell(Instrument):
    defs = ObjectTypeDef(
        code="LOAD_CELL",
        description="An instrument for measuring force.",
        generated_code_prefix="",
    )

    sensor_principle = PropertyTypeAssignment(
        code="SENSOR_PRINCIPLE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="SENSOR_PRINCIPLES",
        property_label="Measurement principle",
        description="Physical principle used to measure force.",
        section="Load Cell Specifications",
        mandatory=False,
    )

    nominal_force = PropertyTypeAssignment(
        code="NOMINAL_FORCE",
        data_type="REAL",
        property_label="Nominal force",
        description="Rated force the load cell is designed to measure.",
        units="kN",
        section="Load Cell Specifications",
        mandatory=False,
    )

    force_direction = PropertyTypeAssignment(
        code="FORCE_DIRECTION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="FORCE_DIRECTIONS",
        property_label="Force direction",
        description="Permissible force measurement direction.",
        section="Load Cell Specifications",
        mandatory=False,
    )


class LaserWeldOptic(Equipment):
    defs = ObjectTypeDef(
        code="LASER_WELD_OPTIC",
        description="""Welding head optic used for laser welding or cutting""",
        generated_code_prefix="",
    )

    collimation_focal_length = PropertyTypeAssignment(
        code="COLLIMATION_FOCAL_LENGTH",
        data_type="REAL",
        property_label="Collimation focal length",
        description="Focal length of the lens that collimates the beam from the fiber.",
        units="mm",
        section="Optical Specifications",
        mandatory=False,
    )

    focus_focal_length = PropertyTypeAssignment(
        code="FOCUS_FOCAL_LENGTH",
        data_type="REAL",
        property_label="Focusing focal length",
        description="Focal length of the lens that focuses the beam onto the workpiece.",
        units="mm",
        section="Optical Specifications",
        mandatory=False,
    )

    magnification_ratio = PropertyTypeAssignment(
        code="MAGNIFICATION_RATIO",
        data_type="REAL",
        property_label="Magnification ratio",
        description="Ratio of focusing to collimation focal length.",
        section="Optical Specifications",
        mandatory=False,
    )

    power_max = PropertyTypeAssignment(
        code="POWER_MAX",
        data_type="REAL",
        property_label="Maximum laser power",
        description="Maximum continuous optical power permitted for the optic.",
        units="kW",
        section="Optical Specifications",
        mandatory=False,
    )

    wavelength_range_min = PropertyTypeAssignment(
        code="WAVELENGTH_RANGE_MIN",
        data_type="REAL",
        property_label="Minimum wavelength",
        description="Lower limit of the wavelength range for which the optic is optimized.",
        units="nm",
        section="Optical Specifications",
        mandatory=False,
    )

    wavelength_range_max = PropertyTypeAssignment(
        code="WAVELENGTH_RANGE_MAX",
        data_type="REAL",
        property_label="Maximum wavelength",
        description="Upper limit of the wavelength range for which the optic is optimized.",
        units="nm",
        section="Optical Specifications",
        mandatory=False,
    )

    protective_window = PropertyTypeAssignment(
        code="PROTECTIVE_WINDOW",
        data_type="BOOLEAN",
        property_label="Protective window",
        description="Whether a protective window is installed.",
        section="Components and Connections",
        mandatory=False,
    )

    protective_window_monitoring = PropertyTypeAssignment(
        code="PROTECTIVE_WINDOW_MONITORING",
        data_type="BOOLEAN",
        property_label="Protective window monitoring",
        description="Whether protective window monitoring is available.",
        section="Components and Connections",
        mandatory=False,
    )

    crossjet = PropertyTypeAssignment(
        code="CROSSJET",
        data_type="BOOLEAN",
        property_label="Crossjet",
        description="Whether a pneumatic crossjet is installed.",
        section="Components and Connections",
        mandatory=False,
    )

    camera_mount = PropertyTypeAssignment(
        code="CAMERA_MOUNT",
        data_type="VARCHAR",
        property_label="Camera mount",
        description="Type of camera connection, such as C-mount.",
        section="Components and Connections",
        mandatory=False,
    )

    fiber_connector_type = PropertyTypeAssignment(
        code="FIBER_CONNECTOR_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="FIBER_CONNECTOR_TYPES",
        property_label="Fiber connector type",
        description="Type of laser fiber connector.",
        section="Components and Connections",
        mandatory=False,
    )


class LaserFiber(Equipment):
    defs = ObjectTypeDef(
        code="LASER_FIBER",
        description="""fiber for transporting a laser beam""",
        generated_code_prefix="",
    )

    fiber_diameter = PropertyTypeAssignment(
        code="FIBER_DIAMETER",
        data_type="REAL",
        property_label="Fiber diameter",
        description="Core diameter of the laser fiber.",
        units="µm",
        section="Fiber Specifications",
        mandatory=False,
    )

    fiber_type = PropertyTypeAssignment(
        code="FIBER_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="FIBER_TYPES",
        property_label="Fiber type",
        description="Type of laser fiber.",
        section="Fiber Specifications",
        mandatory=False,
    )

    connector_1 = PropertyTypeAssignment(
        code="CONNECTOR_1",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="FIBER_CONNECTOR_TYPES",
        property_label="Input connector",
        description="Type of the input connector.",
        section="Connections",
        mandatory=False,
    )

    connector_2 = PropertyTypeAssignment(
        code="CONNECTOR_2",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="FIBER_CONNECTOR_TYPES",
        property_label="Output connector",
        description="Type of the output connector.",
        section="Connections",
        mandatory=False,
    )

    numerical_aperture = PropertyTypeAssignment(
        code="NUMERICAL_APERTURE",
        data_type="REAL",
        property_label="Numerical aperture",
        description="Measure of the fiber's acceptance angle.",
        section="Fiber Specifications",
        mandatory=False,
    )

    attenuation = PropertyTypeAssignment(
        code="ATTENUATION",
        data_type="REAL",
        property_label="Attenuation",
        description="Optical power loss per unit length, in dB/km.",
        section="Fiber Specifications",
        mandatory=False,
    )

    material = PropertyTypeAssignment(
        code="MATERIAL",
        data_type="VARCHAR",
        property_label="Material",
        description="Base material of the fiber core or its doping.",
        section="Fiber Specifications",
        mandatory=False,
    )

    length = PropertyTypeAssignment(
        code="LENGTH",
        data_type="REAL",
        property_label="Fiber length",
        description="Length of the laser fiber.",
        units="m",
        section="Fiber Specifications",
        mandatory=False,
    )


class HydraulicTable(Equipment):
    defs = ObjectTypeDef(
        code="HYDRAULIC_TABLE",
        description="""sample holder with hydraulic setup for strain application""",
        generated_code_prefix="",
    )


# -------------------------
# SIMULATION
# -------------------------


class ProfileScan(Measurement):
    defs = ObjectTypeDef(
        code="PROFILE_SCAN",
        description="A series of two-dimensional line sensor readings.",
        generated_code_prefix="PROFILE_SCAN",
        prev_versions=["EXPERIMENTAL_STEP.PROFILE_SCAN:v0"],
    )

    scan_line_count = PropertyTypeAssignment(
        code="SCAN_LINE_COUNT",
        data_type="INTEGER",
        property_label="Scan line count",
        description="Number of scan lines recorded.",
        section="Scan Information",
        mandatory=False,
        prev_versions=["SCAN_LINE_COUNT:v0"],
    )

    scan_line_resolution = PropertyTypeAssignment(
        code="SCAN_LINE_RESOLUTION",
        data_type="INTEGER",
        property_label="Scan line resolution",
        description="Number of measurement points per scan line.",
        units="pixel",
        section="Scan Information",
        mandatory=False,
        prev_versions=["SCAN_LINE_RESOLUTION:v0"],
    )


class ImageSeries(Measurement):
    defs = ObjectTypeDef(
        code="IMAGE_SERIES",
        description="A series of one or more still image recordings.",
        generated_code_prefix="IMAGE_SERIES",
        prev_versions=["EXPERIMENTAL_STEP.IMAGE_SERIES:v0"],
    )

    image_horizontal_resolution = PropertyTypeAssignment(
        code="IMAGE_HORIZONTAL_RESOLUTION",
        data_type="INTEGER",
        property_label="Horizontal image resolution",
        description="Number of pixels across each image.",
        units="pixel",
        section="Image Series Information",
        mandatory=False,
        prev_versions=["IMAGE_HORIZONTAL_RESOLUTION:v0"],
    )

    image_vertical_resolution = PropertyTypeAssignment(
        code="IMAGE_VERTICAL_RESOLUTION",
        data_type="INTEGER",
        property_label="Vertical image resolution",
        description="Number of pixels down each image.",
        units="pixel",
        section="Image Series Information",
        mandatory=False,
        prev_versions=["IMAGE_VERTICAL_RESOLUTION:v0"],
    )

    image_series_count = PropertyTypeAssignment(
        code="IMAGE_SERIES_COUNT",
        data_type="INTEGER",
        property_label="Number of images recorded",
        description="Number of still images in the series.",
        section="Image Series Information",
        mandatory=False,
        prev_versions=["IMAGE_SERIES_COUNT:v0"],
    )


class VideoRecording(Measurement):
    defs = ObjectTypeDef(
        code="VIDEO_RECORDING",
        prev_versions=["EXPERIMENTAL_STEP.VIDEO_RECORDING:v0"],
        description="""An experimental step describing a video recording""",
        generated_code_prefix="VIDEO_RECORDING",
    )

    video_horizontal_resolution = PropertyTypeAssignment(
        code="VIDEO_HORIZONTAL_RESOLUTION",
        data_type="INTEGER",
        property_label="Horizontal video resolution",
        description="Number of pixels across each video frame.",
        units="pixel",
        section="Video Information",
        mandatory=False,
        prev_versions=["IMAGE_HORIZONTAL_RESOLUTION:v0"],
    )

    video_vertical_resolution = PropertyTypeAssignment(
        code="VIDEO_VERTICAL_RESOLUTION",
        data_type="INTEGER",
        property_label="Vertical video resolution",
        description="Number of pixels down each video frame.",
        units="pixel",
        section="Video Information",
        mandatory=False,
        prev_versions=["IMAGE_VERTICAL_RESOLUTION:v0"],
    )

    video_frame_per_seconds = PropertyTypeAssignment(
        code="VIDEO_FRAME_PER_SECONDS",
        data_type="INTEGER",
        property_label="Average frame rate",
        description="""Average video framerate""",
        units="Hz",
        section="Video Information",
        mandatory=False,
        prev_versions=["VIDEO_FRAME_PER_SECONDS:v0"],
    )

    video_codec = PropertyTypeAssignment(
        code="VIDEO_CODEC",
        data_type="VARCHAR",
        property_label="Video codec",
        description="""Video codec used during recording (if applicable)""",
        section="Video Information",
        mandatory=False,
        prev_versions=["VIDEO_CODEC:v0"],
    )

    video_dynamic_framerate = PropertyTypeAssignment(
        code="VIDEO_DYNAMIC_FRAMERATE",
        data_type="BOOLEAN",
        property_label="Variable frame rate",
        description="""Flag to indicate that the video frame rate varies over time""",
        section="Video Information",
        mandatory=False,
        prev_versions=["VIDEO_DYNAMIC_FRAMERATE:v0"],
    )

    camera_shutter_mode = PropertyTypeAssignment(
        code="CAMERA_SHUTTER_MODE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CAMERA_SHUTTER_MODE",
        property_label="Shutter mode",
        description="""The shutter mode used for video recording""",
        section="Video Information",
        mandatory=False,
        prev_versions=["CAMERA_SHUTTER_MODE:v0"],
    )


class CameraCalibration(Analysis):
    defs = ObjectTypeDef(
        code="CAMERA_CALIBRATION",
        description="""calibrating a camera setup for intrinsic (and extrinsic) parameters using checkerboards, charuco or similar.""",
        generated_code_prefix="",
    )


class Meshing(Computation):
    defs = ObjectTypeDef(
        code="MESHING",
        description="""Calculating a mesh for simulations""",
        generated_code_prefix="",
    )


class AnsisFluentRun(Computation):
    defs = ObjectTypeDef(
        code="ANSIS_FLUENT_RUN",
        description="""A simulation performed with Ansis Fluent""",
        generated_code_prefix="",
    )


class UDFModel(Software):
    defs = ObjectTypeDef(
        code="UDF_MODEL",
        description="""A UDF Model""",
        generated_code_prefix="",
    )


class AnsisFluent(Software):
    defs = ObjectTypeDef(
        code="ANSIS_FLUENT",
        description="""Ansis Fluent Software""",
        generated_code_prefix="",
    )


class SimulationDomain(Context):
    defs = ObjectTypeDef(
        code="SIMULATION_DOMAIN",
        description="""Describes the domain over which the simulation is defined (e.g. subdomain of a workpiece)""",
        generated_code_prefix="",
    )


class MaterialData(Context):
    defs = ObjectTypeDef(
        code="MATERIAL_DATA",
        description="""Describes material properties as used for simulations""",
        generated_code_prefix="",
    )
    # material (object, MetallicAlloy)
    # source (string)
    # temperature dependent properties (json)
