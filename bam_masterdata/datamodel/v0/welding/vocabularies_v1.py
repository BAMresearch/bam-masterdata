"""Welding vocabularies migrated from v1 to the v0 datamodel."""

from bam_masterdata.metadata.definitions import VocabularyTerm, VocabularyTypeDef
from bam_masterdata.metadata.entities import VocabularyType


class WeldingWireTypes(VocabularyType):
    defs = VocabularyTypeDef(
        code="WELDING.WIRE_TYPES",
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
        code="WELDING.POSITIONS",
        description="Positions in which welding is performed.",
    )

    pa = VocabularyTerm(
        code="PA",
        label="PA",
        description="Flat position.",
    )

    pb = VocabularyTerm(
        code="PB",
        label="PB",
        description="Horizontal-vertical position.",
    )

    pc = VocabularyTerm(
        code="PC",
        label="PC",
        description="Horizontal position.",
    )

    pd = VocabularyTerm(
        code="PD",
        label="PD",
        description="Horizontal-overhead position.",
    )

    pe = VocabularyTerm(
        code="PE",
        label="PE",
        description="Overhead position.",
    )

    pf = VocabularyTerm(
        code="PF",
        label="PF",
        description="Vertical position, welding upwards.",
    )

    pg = VocabularyTerm(
        code="PG",
        label="PG",
        description="Vertical position, welding downwards.",
    )

    ph = VocabularyTerm(
        code="PH",
        label="PH",
        description="Pipe position, welding upwards.",
    )

    pj = VocabularyTerm(
        code="PJ",
        label="PJ",
        description="Pipe position, welding downwards.",
    )

    pk = VocabularyTerm(
        code="PK",
        label="PK",
        description="Pipe position for orbital welding.",
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
        code="WELDING.FIBER_CONNECTOR_TYPES",
        description="Types of laser fiber connectors.",
    )

    llk_d = VocabularyTerm(
        code="LLK_D",
        label="LLK-D",
        description="Trumpf LLK-D connector.",
    )

    llk_x = VocabularyTerm(
        code="LLK_X",
        label="LLK-X",
        description="Trumpf LLK-X connector.",
    )

    qbh = VocabularyTerm(
        code="QBH",
        label="QBH",
        description="QBH connector.",
    )

    sma = VocabularyTerm(
        code="SMA",
        label="SMA",
        description="SMA connector.",
    )


class FiberTypes(VocabularyType):
    defs = VocabularyTypeDef(
        code="WELDING.FIBER_TYPES",
        description="Types of laser fibers.",
    )

    single_core = VocabularyTerm(
        code="SINGLE_CORE",
        label="Single-core",
        description="Single-core fiber.",
    )

    brightlineweld = VocabularyTerm(
        code="BRIGHTLINEWELD",
        label="BrightLineWeld",
        description="BrightLineWeld fiber.",
    )

    structured = VocabularyTerm(
        code="STRUCTURED",
        label="Structured",
        description="Structured fiber.",
    )


class SensorPrinciples(VocabularyType):
    defs = VocabularyTypeDef(
        code="WELDING.SENSOR_PRINCIPLES",
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
        code="WELDING.FORCE_DIRECTIONS",
        description="Permissible force measurement directions.",
    )

    compression = VocabularyTerm(
        code="COMPRESSION",
        label="Compression",
        description="Compression measurement.",
    )

    tension = VocabularyTerm(
        code="TENSION",
        label="Tension",
        description="Tension measurement.",
    )

    tension_compression = VocabularyTerm(
        code="TENSION_COMPRESSION",
        label="Tension/Compression",
        description="Tension and compression measurement.",
    )


class JointTypes(VocabularyType):
    defs = VocabularyTypeDef(
        code="WELDING.JOINT_TYPES",
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
        code="WELDING.BACKING_TYPES",
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


class WeldingJointStates(VocabularyType):
    defs = VocabularyTypeDef(
        code="WELDING.JOINT_STATES",
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
        code="WELDING.GROOVE_TYPES",
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
