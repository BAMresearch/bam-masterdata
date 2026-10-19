from bam_masterdata.datamodel.object_types import ExperimentalStep, Instrument
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.entities import ObjectType


# ! The parent class of Welding is not defined (missing ObjectType)
class Welding(ObjectType):
    defs = ObjectTypeDef(
        code="CONSUMABLE.WELDING",
        description="""Generic welding consumable//Generisches Verbrauchsmaterial für Schweißen""",
        generated_code_prefix="CONS.WLD",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        section="General Information",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative Name",
        description="""e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname""",
        mandatory=False,
        section="General Information",
    )

    manufacturer = PropertyTypeAssignment(
        code="MANUFACTURER",
        data_type="VARCHAR",
        property_label="Manufacturer",
        description="""Manufacturer//Hersteller""",
        mandatory=True,
        section="General Information",
    )

    supplier = PropertyTypeAssignment(
        code="SUPPLIER",
        data_type="VARCHAR",
        property_label="Supplier",
        description="""Supplier//Lieferant""",
        mandatory=False,
        section="General Information",
    )

    batch_number = PropertyTypeAssignment(
        code="BATCH_NUMBER",
        data_type="VARCHAR",
        property_label="Batch number",
        description="""Batch number//Chargennummer""",
        mandatory=True,
        section="General Information",
    )

    inventory_no = PropertyTypeAssignment(
        code="INVENTORY_NO",
        data_type="INTEGER",
        property_label="Inventory Number",
        description="""PARFIS inventory number (8-digit)//PARFIS Inventarnummer (8-stellig)""",
        mandatory=False,
        section="BAM Information",
    )

    inventory_no_add = PropertyTypeAssignment(
        code="INVENTORY_NO_ADD",
        data_type="INTEGER",
        property_label="Inventory Number Addition",
        description="""PARFIS inventory number (8-digit)//PARFIS Inventarnummer (8-stellig)""",
        mandatory=False,
        section="BAM Information",
    )

    bam_oe = PropertyTypeAssignment(
        code="BAM_OE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_OE",
        property_label="BAM Organizational Entity",
        description="""BAM Organizational Entity//BAM Organisationseinheit (OE)""",
        mandatory=True,
        section="BAM Information",
    )

    responsible_person = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Responsible person",
        description="""Responsible person//Verantwortliche Person""",
        mandatory=False,
        section="BAM Information",
    )

    co_responsible_person = PropertyTypeAssignment(
        code="CO_RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Co-responsible person",
        description="""Co-responsible person//Weitere verantwortliche Person""",
        mandatory=False,
        section="BAM Information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        section="Additional Information",
    )

    last_systemcheck = PropertyTypeAssignment(
        code="LAST_SYSTEMCHECK",
        data_type="DATE",
        property_label="Last System Check",
        description="""Date of the last system check//Datum des letzten Systemchecks""",
        mandatory=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        section="Comments",
    )


# ------------------------------
# INSTRUMENT
# ------------------------------


class WeldingEquipment(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.WELDING_EQUIPMENT",
        description="""Generic Welding Equipment//Unspezifisches Schweiß-Equipment""",
        generated_code_prefix="INS.WLD_EQP",
    )

    last_systemcheck = PropertyTypeAssignment(
        code="LAST_SYSTEMCHECK",
        data_type="DATE",
        property_label="Last System Check",
        description="""Date of the last system check//Datum des letzten Systemchecks""",
        mandatory=False,
        section="Additional Information",
    )


class GmawTorch(WeldingEquipment):
    defs = ObjectTypeDef(
        code="INSTRUMENT.WELDING_EQUIPMENT.GMAW_TORCH",
        description="""Arc welding torch for gas metal arc welding (GMAW) applications//Schweißbrenner für Metall-Schutzgas-Schweißen (MSG-Schweißen)""",
        generated_code_prefix="INS.WLD_EQP.GMAW_TRCH",
    )

    welding_torch_type = PropertyTypeAssignment(
        code="WELDING.TORCH_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="WELDING.GMAW_TORCH_TYPE",
        property_label="Type",
        description="""type of welding torch//Art des Schweißbrenners""",
        mandatory=True,
        section="General Information",
    )


class GmawWeldingPowerSource(WeldingEquipment):
    defs = ObjectTypeDef(
        code="INSTRUMENT.WELDING_EQUIPMENT.GMAW_WELDING_POWER_SOURCE",
        description="""Power source for gas metal arc welding (GMAW) applications//Stromquelle für Metall-Schutzgas-Schweißen (MSG-Schweißen)""",
        generated_code_prefix="INS.WLD_EQP.GMAW_PWR_SRC",
    )

    welding_arc_current_min = PropertyTypeAssignment(
        code="WELDING.ARC_CURRENT_MIN",
        data_type="REAL",
        property_label="Arc current minimum [A]",
        description="""Minimum arc current//Minimaler Schweißstrom""",
        mandatory=False,
        section="Power Source Information",
    )

    welding_arc_current_max = PropertyTypeAssignment(
        code="WELDING.ARC_CURRENT_MAX",
        data_type="REAL",
        property_label="Arc current maximum [A]",
        description="""Maximum arc current//Maximaler Schweißstrom""",
        mandatory=False,
        section="Power Source Information",
    )

    welding_arc_current_continuous = PropertyTypeAssignment(
        code="WELDING.ARC_CURRENT_CONTINUOUS",
        data_type="REAL",
        property_label="Maximum continuous arc current [A]",
        description="""Maximum continuous arc current at 100% duty cycle//Maximaler Schweißstrom bei 100% Einschaltdauer""",
        mandatory=False,
        section="Power Source Information",
    )

    firmware_version = PropertyTypeAssignment(
        code="FIRMWARE_VERSION",
        data_type="VARCHAR",
        property_label="Current firmware version",
        description="""The currently installed firmware version//Die aktuell installierte Firmware-Version""",
        mandatory=False,
        section="Software Information",
    )


class Positioner(WeldingEquipment):
    defs = ObjectTypeDef(
        code="INSTRUMENT.WELDING_EQUIPMENT.POSITIONER",
        description="""A generic welding table or handling device//Generischer Schweißtisch oder anderer Positionierer zum Schweißen""",
        generated_code_prefix="INS.WLD_EQP.WLD_PSR",
    )

    positioner_type = PropertyTypeAssignment(
        code="POSITIONER_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="POSITIONER_TYPE",
        property_label="Positioner type",
        description="""Positioner type//Art des Positionierers""",
        mandatory=False,
        section="Positioner Information",
    )

    positioner_axis_count = PropertyTypeAssignment(
        code="POSITIONER_AXIS_COUNT",
        data_type="INTEGER",
        property_label="Number of axis",
        description="""The number of controllable axis of the positioner (a value of 0 indicates static positioner)//""",
        mandatory=False,
        section="Positioner Information",
    )

    positioner_payload_max = PropertyTypeAssignment(
        code="POSITIONER_PAYLOAD_MAX",
        data_type="REAL",
        property_label="Maximum payload [kg]",
        description="""The maximum payload to be handled by the positioner//Maximal zulässige Traglast""",
        mandatory=False,
        section="Positioner Information",
    )


class RobotController(WeldingEquipment):
    defs = ObjectTypeDef(
        code="INSTRUMENT.WELDING_EQUIPMENT.ROBOT_CONTROLLER",
        description="""Controller connected to a welding robot//Steuerung für Schweißroboter""",
        generated_code_prefix="INS.WLD_EQP.RBT_CTRL",
    )

    robot_controller_axis_count = PropertyTypeAssignment(
        code="ROBOT_CONTROLLER_AXIS_COUNT",
        data_type="INTEGER",
        property_label="Number of robot axis",
        description="""The number of robot axis the controller can operate//Anzahl der Roboterachsen die von der Steuerung angesteuert werden können""",
        mandatory=True,
        section="Controller Information",
    )

    robot_controller_axis_count_external = PropertyTypeAssignment(
        code="ROBOT_CONTROLLER_AXIS_COUNT_EXTERNAL",
        data_type="INTEGER",
        property_label="Number of external axis",
        description="""The number of external axis the controller can operate//Anzahl der zusätzlichen externen Achsen die von der Steuerung angesteuert werden können""",
        mandatory=True,
        section="Controller Information",
    )

    firmware_version = PropertyTypeAssignment(
        code="FIRMWARE_VERSION",
        data_type="VARCHAR",
        property_label="Current firmware version",
        description="""The currently installed firmware version//Die aktuell installierte Firmware-Version""",
        mandatory=False,
        section="Software Information",
    )


class Robot(WeldingEquipment):
    defs = ObjectTypeDef(
        code="INSTRUMENT.WELDING_EQUIPMENT.ROBOT",
        description="""A generic robot used for welding//Ein generischer Schweißroboter""",
        generated_code_prefix="INS.WLD_EQP.RBT",
    )

    robot_type = PropertyTypeAssignment(
        code="ROBOT_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="ROBOT_TYPE",
        property_label="Type of Robot",
        description="""Type of Robot//Roboterart""",
        mandatory=True,
        section="Robot Information",
    )

    robot_payload_max = PropertyTypeAssignment(
        code="ROBOT_PAYLOAD_MAX",
        data_type="INTEGER",
        property_label="Robot maximum payload [kg]",
        description="""The maximum allowable payload of the robot//Die maximal zulässig Traglast des Roboters""",
        mandatory=False,
        section="Robot Information",
    )

    robot_working_range = PropertyTypeAssignment(
        code="ROBOT_WORKING_RANGE",
        data_type="REAL",
        property_label="Maximum working range [mm]",
        description="""The maximum specified working range of the robot (in mm)//Größe des maximal angegegebenen Arbeitsbereiches (in mm)""",
        mandatory=False,
        section="Robot Information",
    )

    robot_axis_count = PropertyTypeAssignment(
        code="ROBOT_AXIS_COUNT",
        data_type="INTEGER",
        property_label="Number of robot axis",
        description="""The number of a axis on the robot//Anzahl der Roboterachsen""",
        mandatory=False,
        section="Robot Information",
    )


class StationLayout(WeldingEquipment):
    defs = ObjectTypeDef(
        code="INSTRUMENT.WELDING_EQUIPMENT.STATION_LAYOUT",
        description="""Layout and configuration of a welding station""",
        generated_code_prefix="INS.WLD_EQP.ST_LYT",
    )


# ------------------------------
# EXPERIMENTAL_STEP
# ------------------------------


class Weldment(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.WELDMENT",
        description="""An experimental step describing a welding experiment//Ein experimenteller Schritt der einen Schweißvorgang beschreibt""",
        generated_code_prefix="EXP.WLD",
    )

    uuid = PropertyTypeAssignment(
        code="UUID",
        data_type="VARCHAR",
        property_label="UUID",
        description="""A Universally Unique IDentifier (UUID/GUID) according to RFC 4122//Ein Universally Unique IDentifier (UUID/GUID) nach RFC 4122""",
        mandatory=False,
        section="Identifiers",
    )

    weld_joint_number = PropertyTypeAssignment(
        code="WELD_JOINT_NUMBER",
        data_type="INTEGER",
        property_label="Joint Number",
        description="""Consecutive numbering of weld joints of a workpiece or component//Fortlaufende Numerierung von Schweißnähten an Werkstücken und Bauteilen""",
        mandatory=False,
        section="Identifiers",
    )

    weld_layer_number = PropertyTypeAssignment(
        code="WELD_LAYER_NUMBER",
        data_type="INTEGER",
        property_label="Layer Number",
        description="""Consecutive numbering of weld layers for a parent joint//Fortlaufende Numerierung von Schweißlagen der übergeordneten Schweißnaht""",
        mandatory=False,
        section="Identifiers",
    )

    weld_bead_number = PropertyTypeAssignment(
        code="WELD_BEAD_NUMBER",
        data_type="INTEGER",
        property_label="Bead Number",
        description="""Consecutive numbering of weld beads or tracks for a parent layer//Fortlaufende Numerierung von Schweißraupen der übergeordneten Schweißlage""",
        mandatory=False,
        section="Identifiers",
    )

    weld_weldment_number = PropertyTypeAssignment(
        code="WELD_WELDMENT_NUMBER",
        data_type="INTEGER",
        property_label="Weldment Number",
        description="""Consecutive numbering of uninterrupted weldments in a single bead//Fortlaufende Numerierung von ununterbrochenen Schweißungen einer einzelnen Schweißraupe""",
        mandatory=False,
        section="Identifiers",
    )

    experimental_step_weldment_type = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="WELDING.WELD_TYPE",
        property_label="Type of weld",
        description="""Type of weldment made//Art der Schweißverbindung""",
        mandatory=False,
        section="Weldment Information",
    )


class GmawBase(Weldment):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.WELDMENT.GMAW_BASE",
        description="""A simple gas metal arc welding (GMAW) experiment//Ein einfacher MSG-Schweißversuch""",
        generated_code_prefix="EXP.WLD.GMAW_BASE",
    )

    experimental_step_weldment_workpiece_thickness = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.WORKPIECE_THICKNESS",
        data_type="REAL",
        property_label="Thickness of the workpiece [mm]",
        description="""Workpiece thickness//Bauteildicke""",
        mandatory=False,
        section="Workpiece Parameters",
    )

    experimental_step_weldment_groove_preparation = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.GROOVE_PREPARATION",
        data_type="VARCHAR",
        property_label="Groove preparation",
        description="""Groove or Joint preparation description//Beschreibung der Nahtvorbereitung""",
        mandatory=False,
        section="Workpiece Parameters",
    )

    experimental_step_weldment_weld_travel_speed = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.WELD_TRAVEL_SPEED",
        data_type="REAL",
        property_label="Welding travel speed [cm/min]",
        description="""Welding travel speed//Schweißgeschwindigkeit""",
        mandatory=False,
        section="Welding Parameters",
    )

    experimental_step_weldment_shielding_gas_flow = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.SHIELDING_GAS_FLOW",
        data_type="REAL",
        property_label="Shielding gas flowrate [l/min]",
        description="""Shielding gas flowrate//Schutzgasflussgeschwindigkeit""",
        mandatory=False,
        section="Welding Parameters",
    )

    experimental_step_weldment_arc_process = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.ARC_PROCESS",
        data_type="VARCHAR",
        property_label="Arc welding process",
        description="""Name of the selected arc welding process//Name des Lichtbogenschweißprozesses""",
        mandatory=False,
        section="Arc Welding Parameters",
    )

    experimental_step_weldment_arc_voltage = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.ARC_VOLTAGE",
        data_type="REAL",
        property_label="Arc voltage [V]",
        description="""Welding arc voltage//Lichtbogenspannung""",
        mandatory=False,
        section="Arc Welding Parameters",
    )

    experimental_step_weldment_arc_current = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.ARC_CURRENT",
        data_type="REAL",
        property_label="Arc current [A]",
        description="""Welding arc current//Schweißstrom""",
        mandatory=False,
        section="Arc Welding Parameters",
    )

    experimental_step_weldment_wire_stickout_length = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.WIRE_STICKOUT_LENGTH",
        data_type="REAL",
        property_label="Wire stickout [mm]",
        description="""Length of the wire stickout//Stickoutlänge des Schweißdrahtes""",
        mandatory=False,
        section="Arc Welding Parameters",
    )

    experimental_step_weldment_wire_feed_rate = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.WIRE_FEED_RATE",
        data_type="REAL",
        property_label="Wire feed rate [m/min]",
        description="""Welding wire feed rate//Drahtvorschubrate""",
        mandatory=False,
        section="Arc Welding Parameters",
    )


class LaserHybridMagnet(Weldment):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.WELDMENT.LASER_HYBRID_MAGNET",
        description="""A welding experiment using laser-hybrid welding with magnetic support//Ein Laser-Hybrid Schweißversuch mit magnetischer Badstütze""",
        generated_code_prefix="EXP.WLD.LSR_HYB_MGNT",
    )

    experimental_step_weldment_workpiece_thickness = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.WORKPIECE_THICKNESS",
        data_type="REAL",
        property_label="Thickness of the workpiece [mm]",
        description="""Workpiece thickness//Bauteildicke""",
        mandatory=False,
        section="Workpiece Parameters",
    )

    experimental_step_weldment_groove_preparation = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.GROOVE_PREPARATION",
        data_type="VARCHAR",
        property_label="Groove preparation",
        description="""Groove or Joint preparation description//Beschreibung der Nahtvorbereitung""",
        mandatory=False,
        section="Workpiece Parameters",
    )

    experimental_step_weldment_weld_travel_speed = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.WELD_TRAVEL_SPEED",
        data_type="REAL",
        property_label="Welding travel speed [cm/min]",
        description="""Welding travel speed//Schweißgeschwindigkeit""",
        mandatory=False,
        section="Welding Parameters",
    )

    experimental_step_weldment_shielding_gas_flow = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.SHIELDING_GAS_FLOW",
        data_type="REAL",
        property_label="Shielding gas flowrate [l/min]",
        description="""Shielding gas flowrate//Schutzgasflussgeschwindigkeit""",
        mandatory=False,
        section="Welding Parameters",
    )

    experimental_step_weldment_laser_wire_offset = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.LASER_WIRE_OFFSET",
        data_type="REAL",
        property_label="Laser distance to wire [mm]",
        description="""Distance from laser spot to wire feed//Abstand zwischen Laser und Draht""",
        mandatory=False,
        section="Laser Parameters",
    )

    experimental_step_weldment_laser_power = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.LASER_POWER",
        data_type="REAL",
        property_label="Laser power [kW]",
        description="""Laser power//Laserleistung""",
        mandatory=False,
        section="Laser Parameters",
    )

    experimental_step_weldment_laser_focus = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.LASER_FOCUS",
        data_type="REAL",
        property_label="Laser focus [mm]",
        description="""Laser focus position//Laser Fokuslage""",
        mandatory=False,
        section="Laser Parameters",
    )

    experimental_step_weldment_magnet_capacitance = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.MAGNET_CAPACITANCE",
        data_type="REAL",
        property_label="Capacitance C [µF]",
        description="""Capacitance//Kapazität""",
        mandatory=False,
        section="Magnet Parameters",
    )

    experimental_step_weldment_magnet_frequency = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.MAGNET_FREQUENCY",
        data_type="REAL",
        property_label="Frequency F [Hz]",
        description="""Frequency//Frequenz""",
        mandatory=False,
        section="Magnet Parameters",
    )

    experimental_step_weldment_current_transformer = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.CURRENT_TRANSFORMER",
        data_type="REAL",
        property_label="Current transformer HAS 50-S [mV/A]",
        description="""Current transformer HAS 50-S//Stromwandler HAS 50-S""",
        mandatory=False,
        section="Magnet Parameters",
    )

    experimental_step_weldment_magnet_u_1 = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.MAGNET_U_1",
        data_type="REAL",
        property_label="U_1 [mV]",
        description="""Magnet U_1 value//Magnet U_1 Wert""",
        mandatory=False,
        section="Magnet Parameters",
    )

    experimental_step_weldment_magnet_i_1 = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.MAGNET_I_1",
        data_type="REAL",
        property_label="I_1 [A]",
        description="""Magnet I_1 value//Magnet I_1 Wert""",
        mandatory=False,
        section="Magnet Parameters",
    )

    experimental_step_weldment_arc_process = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.ARC_PROCESS",
        data_type="VARCHAR",
        property_label="Arc welding process",
        description="""Name of the selected arc welding process//Name des Lichtbogenschweißprozesses""",
        mandatory=False,
        section="Arc Welding Parameters",
    )

    experimental_step_weldment_arc_voltage = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.ARC_VOLTAGE",
        data_type="REAL",
        property_label="Arc voltage [V]",
        description="""Welding arc voltage//Lichtbogenspannung""",
        mandatory=False,
        section="Arc Welding Parameters",
    )

    experimental_step_weldment_arc_current = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.ARC_CURRENT",
        data_type="REAL",
        property_label="Arc current [A]",
        description="""Welding arc current//Schweißstrom""",
        mandatory=False,
        section="Arc Welding Parameters",
    )

    experimental_step_weldment_wire_stickout_length = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.WIRE_STICKOUT_LENGTH",
        data_type="REAL",
        property_label="Wire stickout [mm]",
        description="""Length of the wire stickout//Stickoutlänge des Schweißdrahtes""",
        mandatory=False,
        section="Arc Welding Parameters",
    )

    experimental_step_weldment_wire_feed_rate = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.WIRE_FEED_RATE",
        data_type="REAL",
        property_label="Wire feed rate [m/min]",
        description="""Welding wire feed rate//Drahtvorschubrate""",
        mandatory=False,
        section="Arc Welding Parameters",
    )


class LaserMagnet(Weldment):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.WELDMENT.LASER_MAGNET",
        description="""A welding experiment using laser beam welding with magnetic support//Ein Laserstrahl Schweißversuch mit magnetischer Badstütze""",
        generated_code_prefix="EXP.WLD.LSR_MGNT",
    )

    workpiece_material = PropertyTypeAssignment(
        code="WORKPIECE_MATERIAL",
        data_type="VARCHAR",
        property_label="Material",
        description="""Material classification of the workpiece base material//Materialgruppe des verwendeten Grundwerkstoffes""",
        mandatory=False,
        section="Workpiece",
    )

    workpiece_material_treatments = PropertyTypeAssignment(
        code="WORKPIECE_MATERIAL_TREATMENTS",
        data_type="VARCHAR",
        property_label="Material Treatments",
        description="""Additional material treatments (heat treatments, rolling etc.)//Zusätzliche Angaben zu Materialbehandlungen (Wärmebehandlungen usw.)""",
        mandatory=False,
        section="Workpiece",
    )

    workpiece_width = PropertyTypeAssignment(
        code="WORKPIECE_WIDTH",
        data_type="REAL",
        property_label="Workpiece Width",
        units="mm",
        description="""Width of workpiece perpendicular to weld seam direction in [mm]//Probenbreite senkrecht zum Schweißnahtverlauf in [mm]""",
        mandatory=False,
        section="Workpiece",
    )

    workpiece_length = PropertyTypeAssignment(
        code="WORKPIECE_LENGTH",
        data_type="REAL",
        property_label="Workpiece Length",
        units="mm",
        description="""Length of Workpiece in weld seam direction in [mm]//Probenlänge in Richtung der Schweißnaht in [mm]""",
        mandatory=False,
        section="Workpiece",
    )

    workpiece_thickness = PropertyTypeAssignment(
        code="WORKPIECE_THICKNESS",
        data_type="REAL",
        property_label="Workpiece Thickness",
        units="mm",
        description="""Workpiece thickness in [mm]//Probendicke in [mm]""",
        mandatory=False,
        section="Workpiece",
    )

    workpiece_surface_preparation = PropertyTypeAssignment(
        code="SURFACE_PREPARATION",
        data_type="VARCHAR",
        property_label="Surface Preparation",
        description="""Surface preparation//Oberflächenbearbeitung""",
        mandatory=False,
        section="Workpiece",
    )

    weldment_grove_preparation = PropertyTypeAssignment(
        code="WELDMENT_GROOVE_PREPARATION",
        data_type="VARCHAR",
        property_label="Groove preparation",
        description="""Groove or Joint preparation description//Beschreibung der Nahtvorbereitung""",
        mandatory=False,
        section="Joint Configuration",
    )

    weldment_full_penetration = PropertyTypeAssignment(
        code="WELDMENT_FULL_PENETRATION",
        data_type="BOOLEAN",
        property_label="Full penetration",
        description="""Full penetration//Durchschweißung""",
        mandatory=False,
        section="Joint Configuration",
    )

    welding_travel_speed = PropertyTypeAssignment(
        code="WELDING_TRAVEL_SPEED",
        data_type="REAL",
        property_label="Welding travel speed",
        units="cm/min",
        description="""Welding travel speed in [cm/min]//Schweißgeschwindigkeit in [cm/min]""",
        mandatory=False,
        section="Welding Parameters",
    )

    weld_seam_length = PropertyTypeAssignment(
        code="WELD_SEAM_LENGTH",
        data_type="REAL",
        property_label="Weld seam length",
        units="mm",
        description="""Weld seam length in [mm]//Länge der Schweißnaht in [mm]""",
        mandatory=False,
        section="Welding Parameters",
    )

    shielding_gas_composition = PropertyTypeAssignment(
        code="SHIELDING_GAS_COMPOSITION",
        data_type="VARCHAR",
        property_label="Shielding gas composition",
        description="""Shielding gas composition listing all components with their volume percentage, e.g., '82% Ar, 18% CO2'//Schutzgaszusammensetzung mit Aufzählung aller Gasanteile in Volumenprozent, z.B. '82% Ar, 18% CO2'""",
        mandatory=False,
        section="Welding Parameters",
    )

    shielding_gas_flowrate = PropertyTypeAssignment(
        code="SHIELDING_GAS_FLOWRATE",
        data_type="REAL",
        property_label="Shielding gas flowrate",
        units="l/minute",
        description="""Shielding gas flowrate in [l/min]//Schutzgasflussrate in [l/min]""",
        mandatory=False,
        section="Welding Parameters",
    )

    shielding_gas_nozzle_distance = PropertyTypeAssignment(
        code="SHIELDING_GAS_NOZZLE_DISTANCE",
        data_type="REAL",
        property_label="Shielding gas nozzle distance",
        units="mm",
        description="""Shielding gas nozzle distance in vertical direction in [mm]//Senkrechter Abstand der Schutzgasdüse zur Probe in [mm]""",
        mandatory=False,
        section="Welding Parameters",
    )

    shielding_gas_nozzle_angle = PropertyTypeAssignment(
        code="SHIELDING_GAS_NOZZLE_ANGLE",
        data_type="REAL",
        property_label="Shielding gas nozzle angle",
        units="deg",
        description="""Shielding gas nozzle angle in [deg]//Anstellwinkel der Schutzgasdüse in [deg]""",
        mandatory=False,
        section="Welding Parameters",
    )

    laser_power = PropertyTypeAssignment(
        code="LASER_POWER",
        data_type="REAL",
        property_label="Laser power",
        units="kW",
        description="""Laser power in [kW]//Laserleistung in [kW]""",
        mandatory=False,
        section="Laser Parameters",
    )

    laser_angle = PropertyTypeAssignment(
        code="LASER_ANGLE",
        data_type="REAL",
        property_label="Laser angle",
        units="deg",
        description="""Laser angle in [deg]//Laserwinkel in [deg]""",
        mandatory=False,
        section="Laser Parameters",
    )

    laser_focal_length = PropertyTypeAssignment(
        code="LASER_FOCAL_LENGTH",
        data_type="REAL",
        property_label="Focal length",
        units="mm",
        description="""Laser focal length in [mm]//Laser Fokuslänge in [mm]""",
        mandatory=False,
        section="Laser Parameters",
    )

    laser_focal_position = PropertyTypeAssignment(
        code="LASER_FOCAL_POSITION",
        data_type="REAL",
        property_label="Focal position",
        units="mm",
        description="""Laser focal position in [mm]//Laser Fokusposition in [mm]""",
        mandatory=False,
        section="Laser Parameters",
    )

    laser_focal_diameter = PropertyTypeAssignment(
        code="LASER_FOCAL_DIAMETER",
        data_type="REAL",
        property_label="Focal diameter",
        units="mm",
        description="""Laser focal diameter in [mm]//Laser Fokusdurchmesser in [mm]""",
        mandatory=False,
        section="Laser Parameters",
    )

    laser_beam_parameter_prod = PropertyTypeAssignment(
        code="LASER_BEAM_PARAMETER_PROD",
        data_type="REAL",
        property_label="Beam parameter product",
        units="mm*mrad",
        description="""Beam parameter product in [mm*mrad]//Strahlparameterprodukt [mm*mrad]""",
        mandatory=False,
        section="Laser Parameters",
    )

    laser_rayleigh_length = PropertyTypeAssignment(
        code="LASER_RAYLEIGH_LENGTH",
        data_type="REAL",
        property_label="Rayleigh length",
        units="mm",
        description="""Rayleigh length in [mm]//Rayleighlänge in [mm]""",
        mandatory=False,
        section="Laser Parameters",
    )

    magnet_max_flux_density = PropertyTypeAssignment(
        code="MAGNET_MAX_FLUX_DENSITY",
        data_type="REAL",
        property_label="Max flux density",
        units="mT",
        description="""Maximum flux density in [mT]//Maximale Flussdichte in [mT]""",
        mandatory=False,
        section="Magnet Parameters",
    )

    magnet_frequency = PropertyTypeAssignment(
        code="MAGNET_FREQUENCY",
        data_type="REAL",
        property_label="Frequency",
        units="Hz",
        description="""Frequency in [Hz]//Frequenz in [Hz]""",
        mandatory=False,
        section="Magnet Parameters",
    )

    magnet_primary_circuit_voltage = PropertyTypeAssignment(
        code="MAGNET_PRIMARY_CIRCUIT_VOLTAGE",
        data_type="REAL",
        property_label="Primary Circuit Voltage",
        units="mV",
        description="""Voltage set in the primary magnet circuit (U_1) in [mV]//Spannung im Primärkreis des Magneten (U_1) in [mV]""",
        mandatory=False,
        section="Magnet Parameters",
    )

    magnet_primary_circuit_current = PropertyTypeAssignment(
        code="MAGNET_PRIMARY_CIRCUIT_CURRENT",
        data_type="REAL",
        property_label="Primary Circuit Current",
        units="A",
        description="""Current measured in the primary magnet circuit (I_1) in [A]//Gemessene Stromstärke im Primärkreis des Magneten (I_1) in [A]""",
        mandatory=False,
        section="Magnet Parameters",
    )

    laser_program_name = PropertyTypeAssignment(
        code="TLC_LASER_PROGRAM_NAME",
        data_type="VARCHAR",
        property_label="Laser Program Name",
        description="""Name of the laser program used for welding//Name des Laserprogramms zum Schweißen""",
        mandatory=False,
        section="TLC 1005",
    )

    robot_program_name = PropertyTypeAssignment(
        code="TLC_ROBOT_PROGRAM_NAME",
        data_type="VARCHAR",
        property_label="Robot Program Name",
        description="""Name of the robot program used for welding//Name des Roboterprogramms zum Schweißen""",
        mandatory=False,
        section="TLC 1005",
    )

    thermocouples_setup = PropertyTypeAssignment(
        code="THERMOCOUPLES_SETUP",
        data_type="XML",
        property_label="Thermocouples setup",
        description="""Structured description of all Thermocouples measurement and positioning along the workpiece//Strukturierte Beschreibung der Thermoelement-Messungen und Positionen auf der Probe""",
        mandatory=False,
        section="Measurements",
    )

    cameras_setup = PropertyTypeAssignment(
        code="CAMERAS_SETUP",
        data_type="XML",
        property_label="Camera setup",
        description="""Structured description of the Camera setup used//Strukturierte Beschreibung der verwendeten Kameras und ihrer Anordnung""",
        mandatory=False,
        section="Measurements",
    )


class WireSolid(Welding):
    defs = ObjectTypeDef(
        code="CONSUMABLE.WELDING.WIRE_SOLID",
        description="""Solid welding wire//Massivdraht (Schweißzusatz)""",
        generated_code_prefix="CONS.WLD.WRE_SLD",
    )

    welding_wire_diameter = PropertyTypeAssignment(
        code="WELDING_WIRE.DIAMETER",
        data_type="REAL",
        property_label="Diameter [mm]",
        description="""Diameter in mm//Durchmesser in mm""",
        mandatory=True,
        section="Wire Information",
    )

    welding_wire_iso_specname = PropertyTypeAssignment(
        code="WELDING_WIRE.ISO_SPECNAME",
        data_type="VARCHAR",
        property_label="ISO specification",
        description="""ISO specification of the wire//ISO Klassifizierung des Zusatzwerkstoffs""",
        mandatory=False,
        section="Wire Information",
    )

    welding_wire_iso_standard = PropertyTypeAssignment(
        code="WELDING_WIRE.ISO_STANDARD",
        data_type="VARCHAR",
        property_label="ISO standard",
        description="""ISO standard providing the specification//ISO Norm o.ä. mit Angabe zur Klassifizierung""",
        mandatory=False,
        section="Wire Information",
    )

    welding_wire_aws_specname = PropertyTypeAssignment(
        code="WELDING_WIRE.AWS_SPECNAME",
        data_type="VARCHAR",
        property_label="AWS specification",
        description="""AWS specification of the wire//AWS Klassifizierung des Zusatzwerkstoffs""",
        mandatory=False,
        section="Wire Information",
    )

    welding_wire_aws_standard = PropertyTypeAssignment(
        code="WELDING_WIRE.AWS_STANDARD",
        data_type="VARCHAR",
        property_label="AWS standard",
        description="""AWS standard providing the specification//AWS Standard mit Angabe zur Klassifizierung""",
        mandatory=False,
        section="Wire Information",
    )

    welding_wire_weight = PropertyTypeAssignment(
        code="WELDING_WIRE.WEIGHT",
        data_type="REAL",
        property_label="Weight [kg]",
        description="""Weight of the wire package as delivered//Gesamtgewicht des Drahtes bei Lieferung""",
        mandatory=False,
        section="Wire Information",
    )
