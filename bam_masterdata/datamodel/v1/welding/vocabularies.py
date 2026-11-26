"""Vocabulary type definitions related to welding experiments and simulation."""

from bam_masterdata.metadata.definitions import VocabularyTerm, VocabularyTypeDef
from bam_masterdata.metadata.entities import VocabularyType


class CameraShutterMode(VocabularyType):
    defs = VocabularyTypeDef(
        code="CAMERA_SHUTTER_MODE",
        prev_versions=["CAMERA_SHUTTER_MODE:v0"],
        description="""Shutter modes of digital cameras//Belichtungsmodi digitaler Bildsensoren""",
    )

    camera_shutter_global = VocabularyTerm(
        code="CAMERA_SHUTTER_GLOBAL",
        prev_versions=["CAMERA_SHUTTER_GLOBAL:v0"],
        label="global shutter",
        description="""Global shutter//Global shutter""",
    )

    camera_shutter_rolling = VocabularyTerm(
        code="CAMERA_SHUTTER_ROLLING",
        prev_versions=["CAMERA_SHUTTER_ROLLING:v0"],
        label="rolling shutter",
        description="""Rolling shutter//Rolling shutter""",
    )


class GmawTorchType(VocabularyType):
    defs = VocabularyTypeDef(
        code="GMAW_TORCH_TYPE",
        prev_versions=["WELDING.GMAW_TORCH_TYPE:v0"],
        description="""General types of GMAW torches//Arten von MSG-Schweißbrennern""",
    )

    welding_gmaw_torch_type_ngw_rot = VocabularyTerm(
        code="WELDING_GMAW_TORCH_TYPE_NGW_ROT",
        prev_versions=["WELDING_GMAW_TORCH_TYPE_NGW_ROT:v0"],
        label="narrow gap torch (rotating arc)",
        description="""A generic dual wire tandem torch//generischer Zweidraht-/Tandem-MSG-Brenner""",
    )

    welding_gmaw_torch_type_ngw_swing = VocabularyTerm(
        code="WELDING_GMAW_TORCH_TYPE_NGW_SWING",
        prev_versions=["WELDING_GMAW_TORCH_TYPE_NGW_SWING:v0"],
        label="narrow gap torch (swing arc)",
        description="""A generic dual wire tandem torch//generischer Zweidraht-/Tandem-MSG-Brenner""",
    )

    welding_gmaw_torch_type_single = VocabularyTerm(
        code="WELDING_GMAW_TORCH_TYPE_SINGLE",
        prev_versions=["WELDING_GMAW_TORCH_TYPE_SINGLE:v0"],
        label="single wire torch",
        description="""Generic GMAW torch with a single wire//generischer Eindraht MSG-Brenner""",
    )

    welding_gmaw_torch_type_tandem = VocabularyTerm(
        code="WELDING_GMAW_TORCH_TYPE_TANDEM",
        prev_versions=["WELDING_GMAW_TORCH_TYPE_TANDEM:v0"],
        label="tandem torch",
        description="""A generic dual wire tandem torch//generischer Zweidraht-/Tandem-MSG-Brenner""",
    )


class PositionerType(VocabularyType):
    defs = VocabularyTypeDef(
        code="POSITIONER_TYPE",
        prev_versions=["POSITIONER_TYPE:v0"],
        description="""Types of specimen or workpiece positioners//Arten Positionierer für Proben und Bauteile""",
    )

    positioner_type_fixed = VocabularyTerm(
        code="POSITIONER_TYPE_FIXED",
        prev_versions=["POSITIONER_TYPE_FIXED:v0"],
        label="fixed positioner",
        description="""An unspecified fixed positionier without any movement capabilities//Fester Positionierer ohne Bewegungsmöglichkeiten""",
    )

    positioner_type_linear = VocabularyTerm(
        code="POSITIONER_TYPE_LINEAR",
        prev_versions=["POSITIONER_TYPE_LINEAR:v0"],
        label="linear positioner",
        description="""linear positioner with one or more axis//Linearpositionierer mit einer oder mehr beweglichen Achsen""",
    )

    positioner_type_rotary_tilt_table = VocabularyTerm(
        code="POSITIONER_TYPE_ROTARY_TILT_TABLE",
        prev_versions=["POSITIONER_TYPE_ROTARY_TILT_TABLE:v0"],
        label="rotary tilt table",
        description="""a rotary tilt table, usually with one tilting and one rotating axis//Drehkipptisch mit üblicherweise je einer Kipp- und Drehachse""",
    )

    positioner_type_turntable = VocabularyTerm(
        code="POSITIONER_TYPE_TURNTABLE",
        prev_versions=["POSITIONER_TYPE_TURNTABLE:v0"],
        label="a turntable with rotary axis",
        description="""A turntable with rotary axis//Drehtisch mit Drehachse""",
    )

    positioner_type_weld_table = VocabularyTerm(
        code="POSITIONER_TYPE_WELD_TABLE",
        prev_versions=["POSITIONER_TYPE_WELD_TABLE:v0"],
        label="welding table",
        description="""A welding table without moving axis//Schweißtisch ohne bewegte Achse""",
    )


class RobotType(VocabularyType):
    defs = VocabularyTypeDef(
        code="ROBOT_TYPE",
        prev_versions=["ROBOT_TYPE:v0"],
        description="""Types of industrial robots//Arten von Industrierobotern""",
    )

    robot_type_articulated = VocabularyTerm(
        code="ROBOT_TYPE_ARTICULATED",
        prev_versions=["ROBOT_TYPE_ARTICULATED:v0"],
        label="articulated robot",
        description="""Articulated robot//Knickarmroboter""",
    )

    robot_type_cartesian_coordinate = VocabularyTerm(
        code="ROBOT_TYPE_CARTESIAN_COORDINATE",
        prev_versions=["ROBOT_TYPE_CARTESIAN_COORDINATE:v0"],
        label="cartesian coordinate robot",
        description="""A Cartesian coordinate robot (a.k.a. linear robot)//Roboter aus Linearachsen in rechtwinkliger Anordnung""",
    )

    robot_type_delta = VocabularyTerm(
        code="ROBOT_TYPE_DELTA",
        prev_versions=["ROBOT_TYPE_DELTA:v0"],
        label="delta robot",
        description="""Delta robot (parallel link robot)//Delta-Roboter (Parallelarmroboter mit Stabkinetik)""",
    )

    robot_type_scara = VocabularyTerm(
        code="ROBOT_TYPE_SCARA",
        prev_versions=["ROBOT_TYPE_SCARA:v0"],
        label="SCARA robot",
        description="""Selective Compliance Assembly Robot Arm (SCARA)//SCARA-Roboter (horizontaler Gelenkarmroboter)""",
    )


class WeldingWireTypes(VocabularyType):
    defs = VocabularyTypeDef(
        code="WELDING_WIRE_TYPES",
        description="Types of welding wire by form or intended use.",
    )

    solid_wire = VocabularyTerm(
        code="SOLID_WIRE",
        label="Solid wire",
        description="Welding wire with a solid cross section.",
    )

    filler_wire = VocabularyTerm(
        code="FILLER_WIRE",
        label="Filler wire",
        description="Wire supplied as filler material independently of the electrode.",
    )

    flux_cored_wire = VocabularyTerm(
        code="FLUX_CORED_WIRE",
        label="Flux-cored wire",
        description="Tubular welding wire containing a flux core.",
    )

    metal_cored_wire = VocabularyTerm(
        code="METAL_CORED_WIRE",
        label="Metal-cored wire",
        description="Tubular welding wire with a core made primarily of metal powder.",
    )


class WeldingPositions(VocabularyType):
    defs = VocabularyTypeDef(
        code="WELDING_POSITIONS",
        description="Positions in which welding is performed.",
    )

    pa = VocabularyTerm(code="PA", label="PA", description="Flat position.")

    pb = VocabularyTerm(
        code="PB", label="PB", description="Horizontal-vertical position."
    )

    pc = VocabularyTerm(code="PC", label="PC", description="Horizontal position.")

    pd = VocabularyTerm(
        code="PD", label="PD", description="Horizontal-overhead position."
    )

    pe = VocabularyTerm(code="PE", label="PE", description="Overhead position.")

    pf = VocabularyTerm(
        code="PF", label="PF", description="Vertical position, welding upwards."
    )

    pg = VocabularyTerm(
        code="PG", label="PG", description="Vertical position, welding downwards."
    )

    ph = VocabularyTerm(
        code="PH", label="PH", description="Pipe position, welding upwards."
    )

    pj = VocabularyTerm(
        code="PJ", label="PJ", description="Pipe position, welding downwards."
    )

    pk = VocabularyTerm(
        code="PK", label="PK", description="Pipe position for orbital welding."
    )

    ph_l045 = VocabularyTerm(
        code="PH_L045",
        label="PH-L045",
        description="Inclined pipe axis at 45°, welding upwards.",
    )

    pj_l045 = VocabularyTerm(
        code="PJ_L045",
        label="PJ-L045",
        description="Inclined pipe axis at 45°, welding downwards.",
    )


class FiberConnectorTypes(VocabularyType):
    defs = VocabularyTypeDef(
        code="FIBER_CONNECTOR_TYPES",
        description="Types of laser fiber connectors.",
    )

    llk_d = VocabularyTerm(
        code="LLK_D", label="LLK-D", description="Trumpf LLK-D connector."
    )

    llk_x = VocabularyTerm(
        code="LLK_X", label="LLK-X", description="Trumpf LLK-X connector."
    )

    qbh = VocabularyTerm(code="QBH", label="QBH", description="QBH connector.")

    sma = VocabularyTerm(code="SMA", label="SMA", description="SMA connector.")


class FiberTypes(VocabularyType):
    defs = VocabularyTypeDef(
        code="FIBER_TYPES",
        description="Types of laser fibers.",
    )

    single_core = VocabularyTerm(
        code="SINGLE_CORE", label="Single-core", description="Single-core fiber."
    )

    brightlineweld = VocabularyTerm(
        code="BRIGHTLINEWELD",
        label="BrightLineWeld",
        description="BrightLineWeld fiber.",
    )

    structured = VocabularyTerm(
        code="STRUCTURED", label="Structured", description="Structured fiber."
    )


class LaserTypes(VocabularyType):
    defs = VocabularyTypeDef(
        code="LASER_TYPES",
        description="Types of laser active media.",
    )

    fiber = VocabularyTerm(code="FIBER", label="Fiber", description="Fiber laser.")

    disk = VocabularyTerm(code="DISK", label="Disk", description="Disk laser.")

    diode = VocabularyTerm(code="DIODE", label="Diode", description="Diode laser.")

    nd_yag = VocabularyTerm(code="ND_YAG", label="Nd:YAG", description="Nd:YAG laser.")


class SensorPrinciples(VocabularyType):
    defs = VocabularyTypeDef(
        code="SENSOR_PRINCIPLES",
        description="Physical principles of force measurement.",
    )

    strain_gauge = VocabularyTerm(
        code="STRAIN_GAUGE",
        label="Strain gauge",
        description="Force measurement using strain gauges.",
    )

    piezoelectric = VocabularyTerm(
        code="PIEZOELECTRIC",
        label="Piezoelectric",
        description="Piezoelectric force measurement.",
    )


class ForceDirections(VocabularyType):
    defs = VocabularyTypeDef(
        code="FORCE_DIRECTIONS",
        description="Permissible force measurement directions.",
    )

    compression = VocabularyTerm(
        code="COMPRESSION", label="Compression", description="Compression measurement."
    )

    tension = VocabularyTerm(
        code="TENSION", label="Tension", description="Tension measurement."
    )

    tension_compression = VocabularyTerm(
        code="TENSION_COMPRESSION",
        label="Tension/Compression",
        description="Tension and compression measurement.",
    )


class JointTypes(VocabularyType):
    defs = VocabularyTypeDef(
        code="JOINT_TYPES",
        description="""Types of welding joint arrangements.""",
    )

    butt_joint = VocabularyTerm(
        code="BUTT_JOINT",
        label="Butt joint",
        description="A butt joint.",
    )

    corner_joint = VocabularyTerm(
        code="CORNER_JOINT",
        label="Corner joint",
        description="A corner joint.",
    )

    t_joint = VocabularyTerm(
        code="T_JOINT",
        label="T-joint",
        description="A T-joint.",
    )

    lap_joint = VocabularyTerm(
        code="LAP_JOINT",
        label="Lap joint",
        description="A lap joint.",
    )

    edge_joint = VocabularyTerm(
        code="EDGE_JOINT",
        label="Edge joint",
        description="An edge joint.",
    )


class BackingTypes(VocabularyType):
    defs = VocabularyTypeDef(
        code="BACKING_TYPES",
        description="""Welding support backing types""",
    )

    none = VocabularyTerm(
        code="NONE",
        label="None",
        description="No backing.",
    )

    strip = VocabularyTerm(
        code="STRIP",
        label="Strip",
        description="Strip backing.",
    )

    strap = VocabularyTerm(
        code="STRAP",
        label="Strap",
        description="Strap backing.",
    )

    ring = VocabularyTerm(
        code="RING",
        label="Ring",
        description="Ring backing.",
    )

    split_pipe = VocabularyTerm(
        code="SPLIT_PIPE",
        label="Split pipe",
        description="Split-pipe backing.",
    )


class WeldTypes(VocabularyType):
    defs = VocabularyTypeDef(
        code="WELD_TYPES",
        prev_versions=["WELDING.WELD_TYPE:v0"],
        description="""Types of joining weld.""",
    )

    groove = VocabularyTerm(
        code="GROOVE",
        prev_versions=["WELDING_GROOVE_WELD:v0"],
        label="Groove",
        description="A groove weld.",
    )

    fillet = VocabularyTerm(
        code="FILLET",
        prev_versions=["WELDING_FILLET_WELD:v0"],
        label="Fillet",
        description="A fillet weld.",
    )

    plug = VocabularyTerm(
        code="PLUG",
        prev_versions=["WELDING_PLUG_WELD:v0"],
        label="Plug",
        description="A plug weld.",
    )

    slot = VocabularyTerm(
        code="SLOT",
        label="Slot",
        description="A slot weld.",
    )

    spot = VocabularyTerm(
        code="SPOT",
        prev_versions=["WELDING_SPOT_WELD:v0"],
        label="Spot",
        description="A spot weld.",
    )

    seam = VocabularyTerm(
        code="SEAM",
        label="Seam",
        description="A seam weld.",
    )

    flange = VocabularyTerm(
        code="FLANGE",
        label="Flange",
        description="A flange weld.",
    )

    surfacing = VocabularyTerm(
        code="SURFACING",
        prev_versions=["WELDING_SURFACING_WELD:v0"],
        label="surfacing weld",
        description="""A weld applied to a surface, as opposed to making a joint, to obtain desired properties or dimensions.//Auftragsschweißung zur Strukturbildung oder Beschichtung""",
    )

    tack = VocabularyTerm(
        code="TACK",
        prev_versions=["WELDING_TACK_WELD:v0"],
        label="tack weld",
        description="""Used to hold the parts of a weldment in proper alignment are placed in grooves or fillet locations and are small enough to be consumed by the production weld.//Heftnaht zur Positionierung von Bauteilen""",
    )


class WeldingJointStates(VocabularyType):
    defs = VocabularyTypeDef(
        code="WELDING_JOINT_STATES",
        description="""State of a welding joint.""",
    )

    prepared = VocabularyTerm(
        code="PREPARED",
        label="Prepared",
        description="The joint is prepared for welding.",
    )

    partially_welded = VocabularyTerm(
        code="PARTIALLY_WELDED",
        label="Partially welded",
        description="The joint is partially welded.",
    )

    completed = VocabularyTerm(
        code="COMPLETED",
        label="Completed",
        description="The joint is fully welded.",
    )

    other = VocabularyTerm(
        code="OTHER",
        label="Other",
        description="Another joint state.",
    )


class GrooveTypes(VocabularyType):
    defs = VocabularyTypeDef(
        code="GROOVE_TYPES",
        description="Welding groove preparations identified by code number and type according to DIN EN ISO 9692-1.",
    )

    groove_1_2_1 = VocabularyTerm(
        code="1.2.1",
        label="1.2.1 (I-Groove)",
        description="I-Groove with code number 1.2.1.",
    )

    groove_1_2_2 = VocabularyTerm(
        code="1.2.2",
        label="1.2.2 (I-Groove)",
        description="I-Groove with code number 1.2.2.",
    )

    groove_2_1 = VocabularyTerm(
        code="2.1",
        label="2.1 (I-Groove)",
        description="I-Groove with code number 2.1.",
    )

    groove_1_3 = VocabularyTerm(
        code="1.3",
        label="1.3 (V-Groove)",
        description="V-Groove with code number 1.3.",
    )

    groove_1_5 = VocabularyTerm(
        code="1.5",
        label="1.5 (V-Groove)",
        description="V-Groove with code number 1.5.",
    )

    groove_1_6 = VocabularyTerm(
        code="1.6",
        label="1.6 (UV-Groove)",
        description="UV-Groove with code number 1.6.",
    )

    groove_1_7 = VocabularyTerm(
        code="1.7",
        label="1.7 (VV-Groove)",
        description="VV-Groove with code number 1.7.",
    )

    groove_1_8 = VocabularyTerm(
        code="1.8",
        label="1.8 (U-Groove)",
        description="U-Groove with code number 1.8.",
    )

    groove_1_9_1 = VocabularyTerm(
        code="1.9.1",
        label="1.9.1 (HV-Groove)",
        description="HV-Groove with code number 1.9.1.",
    )

    groove_1_9_2 = VocabularyTerm(
        code="1.9.2",
        label="1.9.2 (HV-Groove)",
        description="HV-Groove with code number 1.9.2.",
    )

    groove_2_8 = VocabularyTerm(
        code="2.8",
        label="2.8 (HV-Groove)",
        description="HV-Groove with code number 2.8.",
    )

    groove_1_11 = VocabularyTerm(
        code="1.11",
        label="1.11 (HU-Groove)",
        description="HU-Groove with code number 1.11.",
    )

    groove_2_10 = VocabularyTerm(
        code="2.10",
        label="2.10 (HU-Groove)",
        description="HU-Groove with code number 2.10.",
    )

    groove_2_4 = VocabularyTerm(
        code="2.4",
        label="2.4 (DV-Groove)",
        description="DV-Groove with code number 2.4.",
    )

    groove_2_5_1 = VocabularyTerm(
        code="2.5.1",
        label="2.5.1 (DV-Groove)",
        description="DV-Groove with code number 2.5.1.",
    )

    groove_2_5_2 = VocabularyTerm(
        code="2.5.2",
        label="2.5.2 (DV-Groove)",
        description="DV-Groove with code number 2.5.2.",
    )

    groove_2_7 = VocabularyTerm(
        code="2.7",
        label="2.7 (DU-Groove)",
        description="DU-Groove with code number 2.7.",
    )

    groove_2_9_1 = VocabularyTerm(
        code="2.9.1",
        label="2.9.1 (DHV-Groove)",
        description="DHV-Groove with code number 2.9.1.",
    )

    groove_2_9_2 = VocabularyTerm(
        code="2.9.2",
        label="2.9.2 (DHV-Groove)",
        description="DHV-Groove with code number 2.9.2.",
    )

    groove_2_11 = VocabularyTerm(
        code="2.11",
        label="2.11 (DHU-Groove)",
        description="DHU-Groove with code number 2.11.",
    )

    groove_1_12 = VocabularyTerm(
        code="1.12",
        label="1.12 (Frontal-Face-Groove)",
        description="Frontal-Face-Groove with code number 1.12.",
    )

    groove_1_13 = VocabularyTerm(
        code="1.13",
        label="1.13 (Frontal-Face-Groove)",
        description="Frontal-Face-Groove with code number 1.13.",
    )

    groove_2_12 = VocabularyTerm(
        code="2.12",
        label="2.12 (Frontal-Face-Groove)",
        description="Frontal-Face-Groove with code number 2.12.",
    )

    groove_3_1_1 = VocabularyTerm(
        code="3.1.1",
        label="3.1.1 (Frontal-Face-Groove)",
        description="Frontal-Face-Groove with code number 3.1.1.",
    )

    groove_3_1_2 = VocabularyTerm(
        code="3.1.2",
        label="3.1.2 (Frontal-Face-Groove)",
        description="Frontal-Face-Groove with code number 3.1.2.",
    )

    groove_3_1_3 = VocabularyTerm(
        code="3.1.3",
        label="3.1.3 (Frontal-Face-Groove)",
        description="Frontal-Face-Groove with code number 3.1.3.",
    )

    groove_4_1_1 = VocabularyTerm(
        code="4.1.1",
        label="4.1.1 (Frontal-Face-Groove)",
        description="Frontal-Face-Groove with code number 4.1.1.",
    )

    groove_4_1_2 = VocabularyTerm(
        code="4.1.2",
        label="4.1.2 (Frontal-Face-Groove)",
        description="Frontal-Face-Groove with code number 4.1.2.",
    )

    groove_4_1_3 = VocabularyTerm(
        code="4.1.3",
        label="4.1.3 (Frontal-Face-Groove)",
        description="Frontal-Face-Groove with code number 4.1.3.",
    )


class LaserGainMedium(VocabularyType):
    defs = VocabularyTypeDef(
        code="LASER_GAIN_MEDIUM",
        description="""Material in which optical gain is produced//Material, in dem die optische Verstärkung stattfindet""",
    )

    nd_yag = VocabularyTerm(
        code="ND_YAG",
        label="Nd:YAG",
        description="""Neodymium-doped yttrium aluminum garnet//Neodym-dotierter Yttrium-Aluminium-Granat""",
    )

    yb_yag = VocabularyTerm(
        code="YB_YAG",
        label="Yb:YAG",
        description="""Ytterbium-doped yttrium aluminum garnet//Ytterbium-dotierter Yttrium-Aluminium-Granat""",
    )

    yb_doped_silica = VocabularyTerm(
        code="YB_DOPED_SILICA",
        label="Ytterbium-doped silica",
        description="""Silica glass doped with ytterbium//Ytterbium-dotiertes Siliziumdioxidglas""",
    )

    semiconductor = VocabularyTerm(
        code="SEMICONDUCTOR",
        label="Semiconductor",
        description="""Semiconductor material serving as the optical gain medium//Halbleitermaterial als optisches Verstärkungsmedium""",
    )


class RawMatForm(VocabularyType):
    defs = VocabularyTypeDef(
        code="RAW_MAT_FORM",
        prev_versions=["RAW_MAT_FORM:v0"],
        description="""Raw Material Form//Form des Rohmaterials""",
    )

    component = VocabularyTerm(
        code="COMPONENT",
        prev_versions=["COMPONENT:v0"],
        label="Material from component",
        description="""Material from component//Material aus Komponente""",
    )

    flat_bar = VocabularyTerm(
        code="FLAT_BAR",
        prev_versions=["FLAT_BAR:v0"],
        label="Flat bar",
        description="""Flat bar//Flachmaterial""",
    )

    pipe = VocabularyTerm(
        code="PIPE",
        prev_versions=["PIPE:v0"],
        label="Pipe",
        description="""Pipe//Rohr""",
    )

    plate_metal = VocabularyTerm(
        code="PLATE_METAL",
        prev_versions=["PLATE_METAL:v0"],
        label="Plate metal",
        description="""Plate metal//Plattenmaterial""",
    )

    round_bar = VocabularyTerm(
        code="ROUND_BAR",
        prev_versions=["ROUND_BAR:v0"],
        label="Round bar",
        description="""Round bar//Rundmaterial""",
    )

    sheet_metal = VocabularyTerm(
        code="SHEET_METAL",
        prev_versions=["SHEET_METAL:v0"],
        label="Sheet metal",
        description="""Sheet metal//Blech""",
    )


class WorkpieceTreatment(VocabularyType):
    defs = VocabularyTypeDef(
        code="WORKPIECE_TREATMENT",
        prev_versions=["RAW_MAT_TREATMENT_STEEL:v0", "RAW_MAT_TREATMENT_ALU:v0"],
        description="Treatment or temper recorded for an individual workpiece.",
    )

    steel_a = VocabularyTerm(
        code="STEEL_A",
        prev_versions=["A:v0"],
        label="Annealed (+A)",
        description="""Annealed (+A)//Weichgeglüht (+A)""",
    )

    steel_ac = VocabularyTerm(
        code="STEEL_AC",
        prev_versions=["AC:v0"],
        label="Annealed on globular cementite (+AC)",
        description="""Annealed on globular cementite (+AC)//Geglüht zur Erzielung kugeliger Carbide (+AC)""",
    )

    steel_ar = VocabularyTerm(
        code="STEEL_AR",
        prev_versions=["AR:v0"],
        label="As Rolled (+AR)",
        description="""As Rolled (+AR)//Wie gewalzt (+AR)""",
    )

    steel_at = VocabularyTerm(
        code="STEEL_AT",
        prev_versions=["AT:v0"],
        label="Solution Annealed and Quenched (+AT)",
        description="""Solution Annealed and Quenched (+AT)//Lösungsgeglüht und Abgeschreckt (+AT)""",
    )

    steel_bc = VocabularyTerm(
        code="STEEL_BC",
        prev_versions=["BC:v0"],
        label="Thermoformed and Blasted (+BC)",
        description="""Thermoformed and Blasted (+BC)//Warmgeformt und gestrahlt (+BC)""",
    )

    steel_c = VocabularyTerm(
        code="STEEL_C",
        prev_versions=["C:v0"],
        label="Cold Drawn (+C)",
        description="""Cold Drawn (+C)//Kaltgezogen (+C)""",
    )

    steel_fp = VocabularyTerm(
        code="STEEL_FP",
        prev_versions=["FP:v0"],
        label="Annealed on Ferrite-Perlite Microstructure (+FP)",
        description="""Annealed on Ferrite-Perlite Microstructure (+FP)//Behandelt auf Ferrit-Perlit-Gefüge (+FP)""",
    )

    steel_h = VocabularyTerm(
        code="STEEL_H",
        prev_versions=["H:v0"],
        label="Normal Hardenability (+H)",
        description="""Normal Hardenability (+H)//Normale Härtbarkeit (+H)""",
    )

    steel_hh = VocabularyTerm(
        code="STEEL_HH",
        prev_versions=["HH:v0"],
        label="Hardenability restricted to upper scatter band (+HH)",
        description="""Hardenability restricted to upper scatter band (+HH)//Härtbarkeit beschränkt auf oberes Streuband (+HH)""",
    )

    steel_hl = VocabularyTerm(
        code="STEEL_HL",
        prev_versions=["HL:v0"],
        label="Hardenability restricted to lower scatter band (+HL)",
        description="""Hardenability restricted to lower scatter band (+HL)//Härtbarkeit beschränkt auf unteres Streuband (+HL)""",
    )

    steel_m = VocabularyTerm(
        code="STEEL_M",
        prev_versions=["M:v0"],
        label="Thermomechanically Rolled (+M)",
        description="""Thermomechanically Rolled (+M)//Thermomechanisch gewalzt (+M)""",
    )

    steel_n = VocabularyTerm(
        code="STEEL_N",
        prev_versions=["N:v0"],
        label="Normalised or Normalising Rolled (+N)",
        description="""Normalised or Normalising Rolled (+N)//Normalgeglüht oder Normalisierend umgeformt (+N)""",
    )

    steel_nt = VocabularyTerm(
        code="STEEL_NT",
        prev_versions=["NT:v0"],
        label="Normalised and Tempered (+NT)",
        description="""Normalised and Tempered (+NT)//Normalisiert und angelassen (+NT)""",
    )

    steel_qt = VocabularyTerm(
        code="STEEL_QT",
        prev_versions=["QT:v0"],
        label="Quenched and Tempered (+QT)",
        description="""Quenched and Tempered (+QT)//Vergütet (+QT)""",
    )

    steel_sh = VocabularyTerm(
        code="STEEL_SH",
        prev_versions=["SH:v0"],
        label="Peeled (+SH)",
        description="""Peeled (+SH)//Geschält (+SH)""",
    )

    steel_t = VocabularyTerm(
        code="STEEL_T",
        prev_versions=["T:v0"],
        label="Tempered (+T)",
        description="""Tempered (+T)//Angelassen (+T)""",
    )

    aluminium_h14 = VocabularyTerm(
        code="ALUMINIUM_H14",
        prev_versions=["H14:v0"],
        label="H14",
        description="""Work hardenend - 1/2 hard//Kaltverfestigt - 1/2 hart""",
    )

    aluminium_h16 = VocabularyTerm(
        code="ALUMINIUM_H16",
        prev_versions=["H16:v0"],
        label="H16",
        description="""Work hardenend - 3/4 hard//Kaltverfestigt - 3/4 hart""",
    )

    aluminium_h18 = VocabularyTerm(
        code="ALUMINIUM_H18",
        prev_versions=["H18:v0"],
        label="H18",
        description="""Work hardenend - 4/4 hard//Kaltverfestigt - 4/4 hart""",
    )

    aluminium_h19 = VocabularyTerm(
        code="ALUMINIUM_H19",
        prev_versions=["H19:v0"],
        label="H19",
        description="""Work hardenend - extra hard//Kaltverfestigt - extra hart""",
    )

    aluminium_h22 = VocabularyTerm(
        code="ALUMINIUM_H22",
        prev_versions=["H22:v0"],
        label="H22",
        description="""Work hardenend - 1/4 hard//Kaltverfestigt - 1/4 hart""",
    )

    aluminium_h24_h34 = VocabularyTerm(
        code="ALUMINIUM_H24_H34",
        prev_versions=["H24_H34:v0"],
        label="H24_H34",
        description="""Work hardenend - 1/2 hard//Kaltverfestigt - 1/2 hart""",
    )

    aluminium_h26_h36 = VocabularyTerm(
        code="ALUMINIUM_H26_H36",
        prev_versions=["H26_H36:v0"],
        label="H26_H36",
        description="""Work hardenend - 3/4 hard//Kaltverfestigt - 3/4 hart""",
    )

    aluminium_h111 = VocabularyTerm(
        code="ALUMINIUM_H111",
        prev_versions=["H111:v0"],
        label="H111",
        description="""Annealed and slightly strain-hardened (less than H11) during subsequent operations such as stretching or levelling//Geglüht und durch anschließende Arbeitsgänge, z.B. Recken oder Richten, geringfügig kaltverfestigt""",
    )

    aluminium_o = VocabularyTerm(
        code="ALUMINIUM_O",
        prev_versions=["O:v0"],
        label="O",
        description="""Annealed (O)//Geglüht (O)""",
    )

    aluminium_t4 = VocabularyTerm(
        code="ALUMINIUM_T4",
        prev_versions=["T4:v0"],
        label="T4",
        description="""Solution Annealed and Naturally Aged//Lösungsgeglüht und natürlich gealtert""",
    )

    aluminium_t6 = VocabularyTerm(
        code="ALUMINIUM_T6",
        prev_versions=["T6:v0"],
        label="T6",
        description="""Solution Annealed and Artificially Aged//Lösungsgeglüht und künstlich gealtert""",
    )

    aluminium_t73 = VocabularyTerm(
        code="ALUMINIUM_T73",
        prev_versions=["T73:v0"],
        label="T73",
        description="""Solution Annealed and Artificially Overaged to achieve best Resistance to Stress Corrosion//Lösungsgeglüht und künstlich überaltert zum Erreichen einer guten Beständigkeit gegen Spannungsrisskorrosion""",
    )

    aluminium_t76 = VocabularyTerm(
        code="ALUMINIUM_T76",
        prev_versions=["T76:v0"],
        label="T76",
        description="""Solution Annealed and Artificially Overaged to achieve best Resistance to Stress Corrosion//Lösungsgeglüht und künstlich überaltert zum Erreichen einer guten Beständigkeit gegen Schichtkorrosion""",
    )
