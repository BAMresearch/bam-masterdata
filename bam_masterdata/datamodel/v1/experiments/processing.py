# AUTO-GENERATED CLASS HIERARCHY — DO NOT EDIT
#
# Processing*
# ├── AdditiveManufacturing
# │   ├── TwoPhotonPolymerization
# │   ├── MSLA
# │   └── Xolography
# ├── ThermalTreatment
# │   ├── Debinding
# │   └── Sintering
# ├── Welding
# │   ├── GMAWBase
# │   ├── LaserHybridMagnet
# │   └── LaserMagnet
# └── RazorbladeNotching
#
# END AUTO-GENERATED CLASS HIERARCHY


from bam_masterdata.datamodel.v1.activities import Processing
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment


class AdditiveManufacturing(Processing):
    defs = ObjectTypeDef(
        code="ADDITIVE_MANUFACTURING",
        description="An AdditiveManufacturing is a processing that builds an object "
        "layer by layer from a digital model by selectively adding "
        "material.",
        generated_code_prefix="ADD_MANUF",
    )


class TwoPhotonPolymerization(AdditiveManufacturing):
    defs = ObjectTypeDef(
        code="TWO_PHOTON_POLYMERIZATION",
        description="A TwoPhotonPolymerization (2PP) is an additive manufacturing that "
        "cures a photoresist through two-photon absorption in the focus of "
        "a pulsed laser to build micro- and nanoscale structures.",
        generated_code_prefix="TPP",
    )


class MSLA(AdditiveManufacturing):
    defs = ObjectTypeDef(
        code="MSLA",
        description="An MSLA is an additive manufacturing that cures a liquid "
        "photopolymer resin layer by layer with light projected through a "
        "masking display (masked stereolithography).",
        generated_code_prefix="MSLA",
    )


class Xolography(AdditiveManufacturing):
    defs = ObjectTypeDef(
        code="XOLOGRAPHY",
        description="A Xolography is an additive manufacturing that solidifies a "
        "photopolymer resin volume where two light beams of different "
        "wavelengths intersect.",
        generated_code_prefix="XOLO",
    )


class ThermalTreatment(Processing):
    defs = ObjectTypeDef(
        code="THERMAL_TREATMENT",
        description="A ThermalTreatment is a processing that subjects a material to a "
        "controlled temperature program to change its structure or "
        "properties.",
        generated_code_prefix="THERM_TREAT",
    )


class Debinding(ThermalTreatment):
    defs = ObjectTypeDef(
        code="DEBINDING",
        description="A Debinding is a thermal treatment that removes the binder from a "
        "shaped part before sintering.",
        generated_code_prefix="DEBIND",
    )


class Sintering(ThermalTreatment):
    defs = ObjectTypeDef(
        code="SINTERING",
        description="A Sintering is a thermal treatment that densifies a powder or "
        "porous body by heating it below its melting point.",
        generated_code_prefix="SINTER",
    )


class Welding(Processing):
    defs = ObjectTypeDef(
        code="WELDING",
        description="A Welding is a processing that joins workpieces by fusing them, "
        "with or without a filler material.",
        generated_code_prefix="WELD",
        prev_versions=["EXPERIMENTAL_STEP.WELDMENT:v0"],
    )

    # Properties shared by all welding subtypes in v0 are defined here once.

    workpiece_thickness = PropertyTypeAssignment(
        code="WORKPIECE_THICKNESS",
        data_type="REAL",
        property_label="Thickness of the workpiece",
        units="mm",
        description="Workpiece thickness",
        mandatory=False,
        section="Workpiece Parameters",
        prev_versions=[
            "EXPERIMENTAL_STEP.WELDMENT.WORKPIECE_THICKNESS:v0",
            "WORKPIECE_THICKNESS:v0",
        ],
    )

    groove_preparation = PropertyTypeAssignment(
        code="GROOVE_PREPARATION",
        data_type="VARCHAR",
        property_label="Groove preparation",
        description="Groove or Joint preparation description",
        mandatory=False,
        section="Workpiece Parameters",
        prev_versions=[
            "EXPERIMENTAL_STEP.WELDMENT.GROOVE_PREPARATION:v0",
            "WELDMENT_GROOVE_PREPARATION:v0",
        ],
    )

    weld_travel_speed = PropertyTypeAssignment(
        code="WELD_TRAVEL_SPEED",
        data_type="REAL",
        property_label="Welding travel speed",
        units="cm/min",
        description="Welding travel speed",
        mandatory=False,
        section="Welding Parameters",
        prev_versions=[
            "EXPERIMENTAL_STEP.WELDMENT.WELD_TRAVEL_SPEED:v0",
            "WELDING_TRAVEL_SPEED:v0",
        ],
    )

    shielding_gas_flow = PropertyTypeAssignment(
        code="SHIELDING_GAS_FLOW",
        data_type="REAL",
        property_label="Shielding gas flowrate",
        units="l/min",
        description="Shielding gas flowrate",
        mandatory=False,
        section="Welding Parameters",
        prev_versions=[
            "EXPERIMENTAL_STEP.WELDMENT.SHIELDING_GAS_FLOW:v0",
            "SHIELDING_GAS_FLOWRATE:v0",
        ],
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

    weld_joint_number = PropertyTypeAssignment(
        code="WELD_JOINT_NUMBER",
        data_type="INTEGER",
        property_label="Joint Number",
        description="Consecutive numbering of weld joints of a workpiece or component",
        mandatory=False,
        section="Identifiers",
        prev_versions=["WELD_JOINT_NUMBER:v0"],
    )

    weld_layer_number = PropertyTypeAssignment(
        code="WELD_LAYER_NUMBER",
        data_type="INTEGER",
        property_label="Layer Number",
        description="Consecutive numbering of weld layers for a parent joint",
        mandatory=False,
        section="Identifiers",
        prev_versions=["WELD_LAYER_NUMBER:v0"],
    )

    weld_bead_number = PropertyTypeAssignment(
        code="WELD_BEAD_NUMBER",
        data_type="INTEGER",
        property_label="Bead Number",
        description="Consecutive numbering of weld beads or tracks for a parent layer",
        mandatory=False,
        section="Identifiers",
        prev_versions=["WELD_BEAD_NUMBER:v0"],
    )

    weld_weldment_number = PropertyTypeAssignment(
        code="WELD_WELDMENT_NUMBER",
        data_type="INTEGER",
        property_label="Weldment Number",
        description="Consecutive numbering of uninterrupted weldments in a single bead",
        mandatory=False,
        section="Identifiers",
        prev_versions=["WELD_WELDMENT_NUMBER:v0"],
    )

    weldment_type = PropertyTypeAssignment(
        code="WELDMENT_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="WELD_TYPE",
        property_label="Type of weld",
        description="Type of weldment made",
        mandatory=False,
        section="Weldment Information",
        prev_versions=["EXPERIMENTAL_STEP.WELDMENT_TYPE:v0"],
    )


class GMAWBase(Welding):
    defs = ObjectTypeDef(
        code="GMAW_BASE",
        description="A GMAWBase is a welding that uses a simple gas metal arc welding "
        "(GMAW) setup.",
        generated_code_prefix="GMAW",
        prev_versions=["EXPERIMENTAL_STEP.WELDMENT.GMAW_BASE:v0"],
    )

    arc_process = PropertyTypeAssignment(
        code="ARC_PROCESS",
        data_type="VARCHAR",
        property_label="Arc welding process",
        description="Name of the selected arc welding process",
        mandatory=False,
        section="Arc Welding Parameters",
        prev_versions=["EXPERIMENTAL_STEP.WELDMENT.ARC_PROCESS:v0"],
    )

    arc_voltage = PropertyTypeAssignment(
        code="ARC_VOLTAGE",
        data_type="REAL",
        property_label="Arc voltage",
        units="V",
        description="Welding arc voltage",
        mandatory=False,
        section="Arc Welding Parameters",
        prev_versions=["EXPERIMENTAL_STEP.WELDMENT.ARC_VOLTAGE:v0"],
    )

    arc_current = PropertyTypeAssignment(
        code="ARC_CURRENT",
        data_type="REAL",
        property_label="Arc current",
        units="A",
        description="Welding arc current",
        mandatory=False,
        section="Arc Welding Parameters",
        prev_versions=["EXPERIMENTAL_STEP.WELDMENT.ARC_CURRENT:v0"],
    )

    wire_stickout_length = PropertyTypeAssignment(
        code="WIRE_STICKOUT_LENGTH",
        data_type="REAL",
        property_label="Wire stickout",
        units="mm",
        description="Length of the wire stickout",
        mandatory=False,
        section="Arc Welding Parameters",
        prev_versions=["EXPERIMENTAL_STEP.WELDMENT.WIRE_STICKOUT_LENGTH:v0"],
    )

    wire_feed_rate = PropertyTypeAssignment(
        code="WIRE_FEED_RATE",
        data_type="REAL",
        property_label="Wire feed rate",
        units="m/min",
        description="Welding wire feed rate",
        mandatory=False,
        section="Arc Welding Parameters",
        prev_versions=["EXPERIMENTAL_STEP.WELDMENT.WIRE_FEED_RATE:v0"],
    )


class LaserHybridMagnet(Welding):
    defs = ObjectTypeDef(
        code="LASER_HYBRID_MAGNET",
        description="A LaserHybridMagnet is a welding that combines laser beam and arc "
        "welding with magnetic weld pool support.",
        generated_code_prefix="LASER_HYB_MAG",
        prev_versions=["EXPERIMENTAL_STEP.WELDMENT.LASER_HYBRID_MAGNET:v0"],
    )

    laser_wire_offset = PropertyTypeAssignment(
        code="LASER_WIRE_OFFSET",
        data_type="REAL",
        property_label="Laser distance to wire",
        units="mm",
        description="Distance from laser spot to wire feed",
        mandatory=False,
        section="Laser Parameters",
        prev_versions=["EXPERIMENTAL_STEP.WELDMENT.LASER_WIRE_OFFSET:v0"],
    )

    laser_power = PropertyTypeAssignment(
        code="LASER_POWER",
        data_type="REAL",
        property_label="Laser power",
        units="kW",
        description="Laser power",
        mandatory=False,
        section="Laser Parameters",
        prev_versions=["EXPERIMENTAL_STEP.WELDMENT.LASER_POWER:v0"],
    )

    laser_focus = PropertyTypeAssignment(
        code="LASER_FOCUS",
        data_type="REAL",
        property_label="Laser focus",
        units="mm",
        description="Laser focus position",
        mandatory=False,
        section="Laser Parameters",
        prev_versions=["EXPERIMENTAL_STEP.WELDMENT.LASER_FOCUS:v0"],
    )

    magnet_capacitance = PropertyTypeAssignment(
        code="MAGNET_CAPACITANCE",
        data_type="REAL",
        property_label="Capacitance C",
        units="microfarad",
        description="Capacitance",
        mandatory=False,
        section="Magnet Parameters",
        prev_versions=["EXPERIMENTAL_STEP.WELDMENT.MAGNET_CAPACITANCE:v0"],
    )

    magnet_frequency = PropertyTypeAssignment(
        code="MAGNET_FREQUENCY",
        data_type="REAL",
        property_label="Frequency F",
        units="Hz",
        description="Frequency",
        mandatory=False,
        section="Magnet Parameters",
        prev_versions=["EXPERIMENTAL_STEP.WELDMENT.MAGNET_FREQUENCY:v0"],
    )

    current_transformer = PropertyTypeAssignment(
        code="CURRENT_TRANSFORMER",
        data_type="REAL",
        property_label="Current transformer HAS 50-S",
        units="mV/A",
        description="Current transformer HAS 50-S",
        mandatory=False,
        section="Magnet Parameters",
        prev_versions=["EXPERIMENTAL_STEP.WELDMENT.CURRENT_TRANSFORMER:v0"],
    )

    magnet_u_1 = PropertyTypeAssignment(
        code="MAGNET_U_1",
        data_type="REAL",
        property_label="U_1",
        units="mV",
        description="Magnet U_1 value",
        mandatory=False,
        section="Magnet Parameters",
        prev_versions=["EXPERIMENTAL_STEP.WELDMENT.MAGNET_U_1:v0"],
    )

    magnet_i_1 = PropertyTypeAssignment(
        code="MAGNET_I_1",
        data_type="REAL",
        property_label="I_1",
        units="A",
        description="Magnet I_1 value",
        mandatory=False,
        section="Magnet Parameters",
        prev_versions=["EXPERIMENTAL_STEP.WELDMENT.MAGNET_I_1:v0"],
    )

    arc_process = PropertyTypeAssignment(
        code="ARC_PROCESS",
        data_type="VARCHAR",
        property_label="Arc welding process",
        description="Name of the selected arc welding process",
        mandatory=False,
        section="Arc Welding Parameters",
        prev_versions=["EXPERIMENTAL_STEP.WELDMENT.ARC_PROCESS:v0"],
    )

    arc_voltage = PropertyTypeAssignment(
        code="ARC_VOLTAGE",
        data_type="REAL",
        property_label="Arc voltage",
        units="V",
        description="Welding arc voltage",
        mandatory=False,
        section="Arc Welding Parameters",
        prev_versions=["EXPERIMENTAL_STEP.WELDMENT.ARC_VOLTAGE:v0"],
    )

    arc_current = PropertyTypeAssignment(
        code="ARC_CURRENT",
        data_type="REAL",
        property_label="Arc current",
        units="A",
        description="Welding arc current",
        mandatory=False,
        section="Arc Welding Parameters",
        prev_versions=["EXPERIMENTAL_STEP.WELDMENT.ARC_CURRENT:v0"],
    )

    wire_stickout_length = PropertyTypeAssignment(
        code="WIRE_STICKOUT_LENGTH",
        data_type="REAL",
        property_label="Wire stickout",
        units="mm",
        description="Length of the wire stickout",
        mandatory=False,
        section="Arc Welding Parameters",
        prev_versions=["EXPERIMENTAL_STEP.WELDMENT.WIRE_STICKOUT_LENGTH:v0"],
    )

    wire_feed_rate = PropertyTypeAssignment(
        code="WIRE_FEED_RATE",
        data_type="REAL",
        property_label="Wire feed rate",
        units="m/min",
        description="Welding wire feed rate",
        mandatory=False,
        section="Arc Welding Parameters",
        prev_versions=["EXPERIMENTAL_STEP.WELDMENT.WIRE_FEED_RATE:v0"],
    )


class LaserMagnet(Welding):
    defs = ObjectTypeDef(
        code="LASER_MAGNET",
        description="A LaserMagnet is a welding that uses laser beam welding with "
        "magnetic weld pool support.",
        generated_code_prefix="LASER_MAG",
        prev_versions=["EXPERIMENTAL_STEP.WELDMENT.LASER_MAGNET:v0"],
    )

    workpiece_material = PropertyTypeAssignment(
        code="WORKPIECE_MATERIAL",
        data_type="VARCHAR",
        property_label="Material",
        description="Material classification of the workpiece base material",
        mandatory=False,
        section="Workpiece",
        prev_versions=["WORKPIECE_MATERIAL:v0"],
    )

    workpiece_material_treatments = PropertyTypeAssignment(
        code="WORKPIECE_MATERIAL_TREATMENTS",
        data_type="VARCHAR",
        property_label="Material Treatments",
        description="Additional material treatments (heat treatments, rolling etc.)",
        mandatory=False,
        section="Workpiece",
        prev_versions=["WORKPIECE_MATERIAL_TREATMENTS:v0"],
    )

    workpiece_width = PropertyTypeAssignment(
        code="WORKPIECE_WIDTH",
        data_type="REAL",
        property_label="Workpiece Width",
        units="mm",
        description="Width of workpiece perpendicular to weld seam direction in [mm]",
        mandatory=False,
        section="Workpiece",
        prev_versions=["WORKPIECE_WIDTH:v0"],
    )

    workpiece_length = PropertyTypeAssignment(
        code="WORKPIECE_LENGTH",
        data_type="REAL",
        property_label="Workpiece Length",
        units="mm",
        description="Length of Workpiece in weld seam direction in [mm]",
        mandatory=False,
        section="Workpiece",
        prev_versions=["WORKPIECE_LENGTH:v0"],
    )

    surface_preparation = PropertyTypeAssignment(
        code="SURFACE_PREPARATION",
        data_type="VARCHAR",
        property_label="Surface Preparation",
        description="Surface preparation",
        mandatory=False,
        section="Workpiece",
        prev_versions=["SURFACE_PREPARATION:v0"],
    )

    weldment_full_penetration = PropertyTypeAssignment(
        code="WELDMENT_FULL_PENETRATION",
        data_type="BOOLEAN",
        property_label="Full penetration",
        description="Full penetration",
        mandatory=False,
        section="Joint Configuration",
        prev_versions=["WELDMENT_FULL_PENETRATION:v0"],
    )

    weld_seam_length = PropertyTypeAssignment(
        code="WELD_SEAM_LENGTH",
        data_type="REAL",
        property_label="Weld seam length",
        units="mm",
        description="Weld seam length in [mm]",
        mandatory=False,
        section="Welding Parameters",
        prev_versions=["WELD_SEAM_LENGTH:v0"],
    )

    shielding_gas_composition = PropertyTypeAssignment(
        code="SHIELDING_GAS_COMPOSITION",
        data_type="VARCHAR",
        property_label="Shielding gas composition",
        description="Shielding gas composition listing all components with their "
        "volume percentage, e.g., '82% Ar, 18% CO2'",
        mandatory=False,
        section="Welding Parameters",
        prev_versions=["SHIELDING_GAS_COMPOSITION:v0"],
    )

    shielding_gas_nozzle_distance = PropertyTypeAssignment(
        code="SHIELDING_GAS_NOZZLE_DISTANCE",
        data_type="REAL",
        property_label="Shielding gas nozzle distance",
        units="mm",
        description="Shielding gas nozzle distance in vertical direction in [mm]",
        mandatory=False,
        section="Welding Parameters",
        prev_versions=["SHIELDING_GAS_NOZZLE_DISTANCE:v0"],
    )

    shielding_gas_nozzle_angle = PropertyTypeAssignment(
        code="SHIELDING_GAS_NOZZLE_ANGLE",
        data_type="REAL",
        property_label="Shielding gas nozzle angle",
        units="degree",
        description="Shielding gas nozzle angle in [deg]",
        mandatory=False,
        section="Welding Parameters",
        prev_versions=["SHIELDING_GAS_NOZZLE_ANGLE:v0"],
    )

    laser_power = PropertyTypeAssignment(
        code="LASER_POWER",
        data_type="REAL",
        property_label="Laser power",
        units="kW",
        description="Laser power",
        mandatory=False,
        section="Laser Parameters",
        prev_versions=["LASER_POWER:v0"],
    )

    laser_angle = PropertyTypeAssignment(
        code="LASER_ANGLE",
        data_type="REAL",
        property_label="Laser angle",
        units="degree",
        description="Laser angle in [deg]",
        mandatory=False,
        section="Laser Parameters",
        prev_versions=["LASER_ANGLE:v0"],
    )

    laser_focal_length = PropertyTypeAssignment(
        code="LASER_FOCAL_LENGTH",
        data_type="REAL",
        property_label="Focal length",
        units="mm",
        description="Laser focal length in [mm]",
        mandatory=False,
        section="Laser Parameters",
        prev_versions=["LASER_FOCAL_LENGTH:v0"],
    )

    laser_focal_position = PropertyTypeAssignment(
        code="LASER_FOCAL_POSITION",
        data_type="REAL",
        property_label="Focal position",
        units="mm",
        description="Laser focal position in [mm]",
        mandatory=False,
        section="Laser Parameters",
        prev_versions=["LASER_FOCAL_POSITION:v0"],
    )

    laser_focal_diameter = PropertyTypeAssignment(
        code="LASER_FOCAL_DIAMETER",
        data_type="REAL",
        property_label="Focal diameter",
        units="mm",
        description="Laser focal diameter in [mm]",
        mandatory=False,
        section="Laser Parameters",
        prev_versions=["LASER_FOCAL_DIAMETER:v0"],
    )

    laser_beam_parameter_prod = PropertyTypeAssignment(
        code="LASER_BEAM_PARAMETER_PROD",
        data_type="REAL",
        property_label="Beam parameter product",
        units="mm*mrad",
        description="Beam parameter product in [mm*mrad]",
        mandatory=False,
        section="Laser Parameters",
        prev_versions=["LASER_BEAM_PARAMETER_PROD:v0"],
    )

    laser_rayleigh_length = PropertyTypeAssignment(
        code="LASER_RAYLEIGH_LENGTH",
        data_type="REAL",
        property_label="Rayleigh length",
        units="mm",
        description="Rayleigh length in [mm]",
        mandatory=False,
        section="Laser Parameters",
        prev_versions=["LASER_RAYLEIGH_LENGTH:v0"],
    )

    magnet_max_flux_density = PropertyTypeAssignment(
        code="MAGNET_MAX_FLUX_DENSITY",
        data_type="REAL",
        property_label="Max flux density",
        units="mT",
        description="Maximum flux density in [mT]",
        mandatory=False,
        section="Magnet Parameters",
        prev_versions=["MAGNET_MAX_FLUX_DENSITY:v0"],
    )

    magnet_frequency = PropertyTypeAssignment(
        code="MAGNET_FREQUENCY",
        data_type="REAL",
        property_label="Frequency F",
        units="Hz",
        description="Frequency",
        mandatory=False,
        section="Magnet Parameters",
        prev_versions=["MAGNET_FREQUENCY:v0"],
    )

    magnet_primary_circuit_voltage = PropertyTypeAssignment(
        code="MAGNET_PRIMARY_CIRCUIT_VOLTAGE",
        data_type="REAL",
        property_label="Primary Circuit Voltage",
        units="mV",
        description="Voltage set in the primary magnet circuit (U_1) in [mV]",
        mandatory=False,
        section="Magnet Parameters",
        prev_versions=["MAGNET_PRIMARY_CIRCUIT_VOLTAGE:v0"],
    )

    magnet_primary_circuit_current = PropertyTypeAssignment(
        code="MAGNET_PRIMARY_CIRCUIT_CURRENT",
        data_type="REAL",
        property_label="Primary Circuit Current",
        units="A",
        description="Current measured in the primary magnet circuit (I_1) in [A]",
        mandatory=False,
        section="Magnet Parameters",
        prev_versions=["MAGNET_PRIMARY_CIRCUIT_CURRENT:v0"],
    )

    tlc_laser_program_name = PropertyTypeAssignment(
        code="TLC_LASER_PROGRAM_NAME",
        data_type="VARCHAR",
        property_label="Laser Program Name",
        description="Name of the laser program used for welding",
        mandatory=False,
        section="TLC 1005",
        prev_versions=["TLC_LASER_PROGRAM_NAME:v0"],
    )

    tlc_robot_program_name = PropertyTypeAssignment(
        code="TLC_ROBOT_PROGRAM_NAME",
        data_type="VARCHAR",
        property_label="Robot Program Name",
        description="Name of the robot program used for welding",
        mandatory=False,
        section="TLC 1005",
        prev_versions=["TLC_ROBOT_PROGRAM_NAME:v0"],
    )

    thermocouples_setup = PropertyTypeAssignment(
        code="THERMOCOUPLES_SETUP",
        data_type="XML",
        property_label="Thermocouples setup",
        description="Structured description of all Thermocouples measurement and "
        "positioning along the workpiece",
        mandatory=False,
        section="Measurements",
        prev_versions=["THERMOCOUPLES_SETUP:v0"],
    )

    cameras_setup = PropertyTypeAssignment(
        code="CAMERAS_SETUP",
        data_type="XML",
        property_label="Camera setup",
        description="Structured description of the Camera setup used",
        mandatory=False,
        section="Measurements",
        prev_versions=["CAMERAS_SETUP:v0"],
    )


class RazorbladeNotching(Processing):
    defs = ObjectTypeDef(
        code="RAZORBLADE_NOTCHING",
        description="A RazorbladeNotching is a processing that sharpens or introduces "
        "a notch in a specimen with repeated strokes of a razor blade.",
        generated_code_prefix="RAZOR_NOTCH",
        prev_versions=["EXPERIMENTAL_STEP.RAZORBLADE_NOTCHING:v0"],
    )

    razor_strokelength = PropertyTypeAssignment(
        code="RAZOR_STROKELENGTH",
        data_type="REAL",
        property_label="Stroke Length",
        units="mm",
        description="Stroke Length [mm]",
        mandatory=False,
        section="Process Parameters",
        prev_versions=["RAZOR_STROKELENGTH:v0"],
    )

    razor_strokespeed = PropertyTypeAssignment(
        code="RAZOR_STROKESPEED",
        data_type="REAL",
        property_label="Stroke Speed",
        units="mm/s",
        description="Stroke Speed [mm/s]",
        mandatory=False,
        section="Process Parameters",
        prev_versions=["RAZOR_STROKESPEED:v0"],
    )

    razor_strokecount = PropertyTypeAssignment(
        code="RAZOR_STROKECOUNT",
        data_type="REAL",
        property_label="Stroke Count",
        description="Stroke Count",
        mandatory=False,
        section="Process Parameters",
        prev_versions=["RAZOR_STROKECOUNT:v0"],
    )

    razor_depth = PropertyTypeAssignment(
        code="RAZOR_DEPTH",
        data_type="REAL",
        property_label="Notch Depth Increase according to Gauge",
        units="micrometer",
        description="Notch Depth Increase according to Gauge [µm]",
        mandatory=False,
        section="Results",
        prev_versions=["RAZOR_DEPTH:v0"],
    )
