from bam_masterdata.datamodel.object_types import Instrument
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment


class ForceTransducer(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.FORCE_TRANSDUCER",
        description="""Force Transducer//Kraftmesseinrichtung""",
        generated_code_prefix="INS.FORCE_TRANSD",
    )

    force_transducer_type = PropertyTypeAssignment(
        code="FORCE_TRANSDUCER_TYPE",
        data_type="VARCHAR",
        property_label="Force Transducer Type",
        description="""Force Transducer Type Code as specified by Manufacturer//Typenbezeichnung des Herstellers für die Kraftmesseinrichtung""",
        mandatory=False,
        section="Technical Details",
    )

    max_static_force = PropertyTypeAssignment(
        code="MAX_STATIC_FORCE",
        data_type="REAL",
        property_label="Maximum Static Force [kN]",
        description="""Maximum Static Force in kN//Maximale statische Kraft [kN]""",
        mandatory=True,
        section="Technical Details",
    )

    max_dynamic_force = PropertyTypeAssignment(
        code="MAX_DYNAMIC_FORCE",
        data_type="REAL",
        property_label="Maximum Dynamic Force [kN]",
        description="""Maximum Dynamic Force in kN//Maximale dynamische Kraft [kN[""",
        mandatory=True,
        section="Technical Details",
    )

    max_excitation_voltage = PropertyTypeAssignment(
        code="MAX_EXCITATION_VOLTAGE",
        data_type="REAL",
        property_label="Maximum Excitation Voltage [V]",
        description="""Maximum Excitation Voltage [V]//Maximale Speisespannung [V]""",
        mandatory=True,
        section="Technical Details",
    )

    calibration_interval = PropertyTypeAssignment(
        code="CALIBRATION_INTERVAL",
        data_type="INTEGER",
        property_label="Calibration Interval [months]",
        description="""Calibration Interval [months]//Kalibrierintervall [Monate]""",
        mandatory=False,
        section="Status",
    )


class HydraulicCylinder(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.HYDRAULIC_CYLINDER",
        description="""Hydraulic Cylinder//Hydraulikzylinder""",
        generated_code_prefix="INS.HYDR_CYL",
    )

    cylinder_type = PropertyTypeAssignment(
        code="CYLINDER_TYPE",
        data_type="VARCHAR",
        property_label="Hydraulic Cylinder Type",
        description="""Hydraulic Cylinder Type Code as specified by Manufacturer//Typenbezeichnung des Herstellers für den Hydraulikzylinder""",
        mandatory=False,
        section="Technical Details",
    )

    max_static_force = PropertyTypeAssignment(
        code="MAX_STATIC_FORCE",
        data_type="REAL",
        property_label="Maximum Static Force [kN]",
        description="""Maximum Static Force in kN//Maximale statische Kraft [kN]""",
        mandatory=True,
        section="Technical Details",
    )

    max_dynamic_force = PropertyTypeAssignment(
        code="MAX_DYNAMIC_FORCE",
        data_type="REAL",
        property_label="Maximum Dynamic Force [kN]",
        description="""Maximum Dynamic Force in kN//Maximale dynamische Kraft [kN[""",
        mandatory=True,
        section="Technical Details",
    )

    max_excitation_voltage = PropertyTypeAssignment(
        code="MAX_EXCITATION_VOLTAGE",
        data_type="REAL",
        property_label="Maximum Excitation Voltage [V]",
        description="""Maximum Excitation Voltage [V]//Maximale Speisespannung [V]""",
        mandatory=True,
        section="Technical Details",
    )

    calibration_interval = PropertyTypeAssignment(
        code="CALIBRATION_INTERVAL",
        data_type="INTEGER",
        property_label="Calibration Interval [months]",
        description="""Calibration Interval [months]//Kalibrierintervall [Monate]""",
        mandatory=False,
        section="Status",
    )


class HydraulicMisc(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.HYDRAULIC_MISC",
        description="""Miscellaneous Hydraulic Component""",
        generated_code_prefix="INS.HYDR_MISC",
    )

    misc_hyd_comp_type = PropertyTypeAssignment(
        code="MISC_HYD_COMP_TYPE",
        data_type="VARCHAR",
        property_label="Type Code as specified by Manufacturer",
        description="""Type Code as specified by Manufacturer//Typenbezeichnung des Herstellers""",
        mandatory=False,
        section="Technical Details",
    )

    calibration_interval = PropertyTypeAssignment(
        code="CALIBRATION_INTERVAL",
        data_type="INTEGER",
        property_label="Calibration Interval [months]",
        description="""Calibration Interval [months]//Kalibrierintervall [Monate]""",
        mandatory=False,
        section="Status",
    )


class Servovalve(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.SERVOVALVE",
        description="""Servovalve for servohydraulic testing machines//Servoventil für servohydraulische Prüfmaschinen""",
        generated_code_prefix="INS.HYDR_SVALV",
    )

    valve_type_id = PropertyTypeAssignment(
        code="VALVE_TYPE_ID",
        data_type="VARCHAR",
        property_label="Type",
        description="""Valve Type Code as specified by Manufacturer//Typenbezeichnung des Herstellers für das Servoventil""",
        mandatory=False,
        section="Technical Details",
    )

    valve_model_id = PropertyTypeAssignment(
        code="VALVE_MODEL_ID",
        data_type="VARCHAR",
        property_label="Model",
        description="""Valve Model Code as specified by Manufacturer//Modellbezeichnung des Herstellers für das Servoventil""",
        mandatory=False,
        section="Technical Details",
    )

    rated_flow = PropertyTypeAssignment(
        code="RATED_FLOW",
        data_type="REAL",
        property_label="Rated Flow [l/min]",
        description="""Rated flow [l/min]//Nenndurchfluss [l/min]""",
        mandatory=True,
        section="Technical Details",
    )

    max_pressure = PropertyTypeAssignment(
        code="MAX_PRESSURE",
        data_type="REAL",
        property_label="Maximum Operating Pressure [bar]",
        description="""Maximum Operating Pressure [bar]//Maximaler Betriebsdruck [bar]""",
        mandatory=True,
        section="Technical Details",
    )

    rated_power = PropertyTypeAssignment(
        code="RATED_POWER",
        data_type="REAL",
        property_label="Rated Power [kW]",
        description="""Rated power [kW]//Nennleistung [kW]""",
        mandatory=True,
        section="Technical Details",
    )

    calibration_interval = PropertyTypeAssignment(
        code="CALIBRATION_INTERVAL",
        data_type="INTEGER",
        property_label="Calibration Interval [months]",
        description="""Calibration Interval [months]//Kalibrierintervall [Monate]""",
        mandatory=False,
        section="Status",
    )


class LoadFrame(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.LOAD_FRAME",
        description="""Load Frame of Testing Machine//Lastrahmen für Prüfmaschinen""",
        generated_code_prefix="INS.LOAD_FRAME",
    )

    load_frame_type = PropertyTypeAssignment(
        code="LOAD_FRAME_TYPE",
        data_type="VARCHAR",
        property_label="Load Frame Type Code as specified by Manufacturer",
        description="""Load Frame Type Code as specified by Manufacturer//Typenbezeichnung des Herstellers für den Lastrahmen""",
        mandatory=False,
        section="Technical Details",
    )

    max_static_force = PropertyTypeAssignment(
        code="MAX_STATIC_FORCE",
        data_type="REAL",
        property_label="Maximum Static Force [kN]",
        description="""Maximum Static Force in kN//Maximale statische Kraft [kN]""",
        mandatory=False,
        section="Technical Details",
    )

    max_dynamic_force = PropertyTypeAssignment(
        code="MAX_DYNAMIC_FORCE",
        data_type="REAL",
        property_label="Maximum Dynamic Force [kN]",
        description="""Maximum Dynamic Force in kN//Maximale dynamische Kraft [kN[""",
        mandatory=False,
        section="Technical Details",
    )

    load_frame_orientation = PropertyTypeAssignment(
        code="LOAD_FRAME_ORIENTATION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="LOAD_FRAME_ORIENTATION",
        property_label="Load Frame Orientation",
        description="""Load Frame Orientation//Orientierung des Lastrahmens""",
        mandatory=False,
        section="Technical Details",
    )

    max_space_vert = PropertyTypeAssignment(
        code="MAX_SPACE_VERT",
        data_type="REAL",
        property_label="Maximum vertical space for Specimens and Grips [mm]",
        description="""Maximum vertical space for Specimens and Grips [mm]//Maximaler vertikaler Bauraum für Proben und Probenhalter [mm]""",
        mandatory=False,
        section="Technical Details",
    )

    max_space_hor = PropertyTypeAssignment(
        code="MAX_SPACE_HOR",
        data_type="REAL",
        property_label="Maximum horizontal space between Columns [mm]",
        description="""Maximum horizontal space between Columns [mm]//Maximaler horizontaler Bauraum zwischen den Säulen [mm]""",
        mandatory=False,
        section="Technical Details",
    )


class AlignmentFixture(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.ALIGNMENT_FIXTURE",
        description="""Alignment Fixture for Testing Machine//Ausrichtvorrichtung für Prüfmaschinen""",
        generated_code_prefix="INS.ALGN_FIX",
    )

    max_static_force = PropertyTypeAssignment(
        code="MAX_STATIC_FORCE",
        data_type="REAL",
        property_label="Maximum Static Force [kN]",
        description="""Maximum Static Force in kN//Maximale statische Kraft [kN]""",
        mandatory=False,
        section="Technical Details",
    )

    max_dynamic_force = PropertyTypeAssignment(
        code="MAX_DYNAMIC_FORCE",
        data_type="REAL",
        property_label="Maximum Dynamic Force [kN]",
        description="""Maximum Dynamic Force in kN//Maximale dynamische Kraft [kN[""",
        mandatory=False,
        section="Technical Details",
    )


class Thermocouple(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.THERMOCOUPLE",
        description="""Thermocouple//Thermoelement""",
        generated_code_prefix="INS.TC",
    )

    tc_type = PropertyTypeAssignment(
        code="TC_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="THERMOCOUPLE_TYPE",
        property_label="Thermocouple Type",
        description="""Thermocouple Type//Thermoelement Typ""",
        mandatory=True,
        section="Technical Details",
    )

    tc_min_temp = PropertyTypeAssignment(
        code="TC_MIN_TEMP",
        data_type="REAL",
        property_label="Minimum Operating Temperature [°C]",
        description="""Minimum Operating Temperature [°C]//Minimale Betriebstemperatur [°C]""",
        mandatory=False,
        section="Technical Details",
    )

    tc_max_temp = PropertyTypeAssignment(
        code="TC_MAX_TEMP",
        data_type="REAL",
        property_label="Maximum Operating Temperature [°C]",
        description="""Maximum Operating Temperature [°C]//Maximale Betriebstemperatur [°C]""",
        mandatory=False,
        section="Technical Details",
    )

    tc_diameter = PropertyTypeAssignment(
        code="TC_DIAMETER",
        data_type="REAL",
        property_label="Diameter [mm]",
        description="""Diameter [mm]//Durchmesser [mm]""",
        mandatory=False,
        section="Technical Details",
    )

    tc_cable_length = PropertyTypeAssignment(
        code="TC_CABLE_LENGTH",
        data_type="REAL",
        property_label="Cable Length [mm]",
        description="""Cable Length [mm]//Kabellänge [mm]""",
        mandatory=False,
        section="Technical Details",
    )

    tc_connector = PropertyTypeAssignment(
        code="TC_CONNECTOR",
        data_type="BOOLEAN",
        property_label="Connector",
        description="""Connector//Stecker""",
        mandatory=False,
        section="Technical Details",
    )


class Rtd(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.RTD",
        description="""Resistance Temperature Detector (RTD)//Widerstandsthermometer""",
        generated_code_prefix="INS.RTD",
    )

    rtd_type = PropertyTypeAssignment(
        code="RTD_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="RTD_TYPE",
        property_label="RTD Type",
        description="""RTD Type//Widerstandsthermometer Typ""",
        mandatory=False,
        section="Technical Details",
    )

    rtd_min_temp = PropertyTypeAssignment(
        code="RTD_MIN_TEMP",
        data_type="REAL",
        property_label="Minimum Operating Temperature [°C]",
        description="""Minimum Operating Temperature [°C]//Minimale Betriebstemperatur [°C]""",
        mandatory=False,
        section="Technical Details",
    )

    rtd_max_temp = PropertyTypeAssignment(
        code="RTD_MAX_TEMP",
        data_type="REAL",
        property_label="Maximum Operating Temperature [°C]",
        description="""Maximum Operating Temperature [°C]//Maximale Betriebstemperatur [°C]""",
        mandatory=False,
        section="Technical Details",
    )

    rtd_accuracy_class = PropertyTypeAssignment(
        code="RTD_ACCURACY_CLASS",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="RTD_ACCURACY_CLASS",
        property_label="RTD Accuracy Class",
        description="""RTD Accuracy Class//Widerstandsthermometer Genauigkeitsklasse""",
        mandatory=False,
        section="Technical Details",
    )

    rtd_insulation_material = PropertyTypeAssignment(
        code="RTD_INSULATION_MATERIAL",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="RTD_INSULATION_MATERIAL",
        property_label="RTD Insulation Material",
        description="""RTD Insulation Material//Widerstandsthermometer Isolationsmaterial""",
        mandatory=False,
        section="Technical Details",
    )

    rtd_cover_tube_diameter = PropertyTypeAssignment(
        code="RTD_COVER_TUBE_DIAMETER",
        data_type="REAL",
        property_label="RTD Cover Tube Diameter [mm]",
        description="""RTD Cover Tube Diameter [mm]//Widerstandsthermometer Schutzhülsendurchmesser [mm]""",
        mandatory=False,
        section="Technical Details",
    )

    rtd_cover_tube_length = PropertyTypeAssignment(
        code="RTD_COVER_TUBE_LENGTH",
        data_type="REAL",
        property_label="RTD Cover Tube Length [mm]",
        description="""RTD Cover Tube Length [mm]//Widerstandsthermometer Schutzhülsenlänge [mm]""",
        mandatory=False,
        section="Technical Details",
    )

    rtd_cable_length = PropertyTypeAssignment(
        code="RTD_CABLE_LENGTH",
        data_type="REAL",
        property_label="RTD Cable Length [mm]",
        description="""RTD Cable Length [mm]//Widerstandsthermometer Kabellänge [mm]""",
        mandatory=False,
        section="Technical Details",
    )

    rtd_connection = PropertyTypeAssignment(
        code="RTD_CONNECTION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="RTD_CONNECTION_TYPE",
        property_label="RTD Connection",
        description="""RTD Connection//Widerstandsthermometer Anschlussart""",
        mandatory=False,
        section="Technical Details",
    )


class Nanovoltmeter(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.NANOVOLTMETER",
        description="""Nanovoltmeter//Nanovoltmeter""",
        generated_code_prefix="INS.NANOVM",
    )

    number_of_channels = PropertyTypeAssignment(
        code="NUMBER_OF_CHANNELS",
        data_type="INTEGER",
        property_label="Number of Channels",
        description="""Number of Channels//Anzahl der Kanäle""",
        mandatory=False,
        section="Inputs",
    )

    minrange = PropertyTypeAssignment(
        code="MINRANGE",
        data_type="REAL",
        property_label="Minimum Range [V]",
        description="""Minimum Range [V]//Kleinster Messbereich [V]""",
        mandatory=False,
        section="Inputs",
    )

    minrange_resolution = PropertyTypeAssignment(
        code="MINRANGE_RESOLUTION",
        data_type="REAL",
        property_label="Resolution at minimum Range [nV]",
        description="""Resolution at minimum Range [nV]//Auflösung im kleinsten Messbereich [nV]""",
        mandatory=False,
        section="Inputs",
    )

    maxrange = PropertyTypeAssignment(
        code="MAXRANGE",
        data_type="REAL",
        property_label="Maximum Range [V]",
        description="""Maximum Range [V]//Größter Messbereich [V]""",
        mandatory=False,
        section="Inputs",
    )

    maxrange_resolution = PropertyTypeAssignment(
        code="MAXRANGE_RESOLUTION",
        data_type="REAL",
        property_label="Resolution at maximum Range [nV]",
        description="""Resolution at maximum Range [nV]//Auflösung im größten Messbereich [nV]""",
        mandatory=False,
        section="Inputs",
    )

    number_of_analog_outputs = PropertyTypeAssignment(
        code="NUMBER_OF_ANALOG_OUTPUTS",
        data_type="INTEGER",
        property_label="Number of Analog Outputs",
        description="""Number of Analog Outputs//Anzahl Analoger Ausgänge""",
        mandatory=False,
        section="Outputs",
    )

    analog_output_voltage_min = PropertyTypeAssignment(
        code="ANALOG_OUTPUT_VOLTAGE_MIN",
        data_type="REAL",
        property_label="Analog Output Minimum Voltage [V]",
        description="""Analog Output Minimum Voltage [V]//Minimale Spannung am Analogen Ausgang [V]""",
        mandatory=False,
        section="Outputs",
    )

    analog_output_voltage_max = PropertyTypeAssignment(
        code="ANALOG_OUTPUT_VOLTAGE_MAX",
        data_type="REAL",
        property_label="Analog Output Maximum Voltage [V]",
        description="""Analog Output Maximum Voltage [V]//Maximale Spannung am Analogen Ausgang [V]""",
        mandatory=False,
        section="Outputs",
    )

    gpib = PropertyTypeAssignment(
        code="GPIB",
        data_type="BOOLEAN",
        property_label="GPIB Interface",
        description="""GPIB Interface//GPIB Schnittstelle""",
        mandatory=False,
        section="Command Interfaces",
    )

    rs232 = PropertyTypeAssignment(
        code="RS232",
        data_type="BOOLEAN",
        property_label="RS232 Interface",
        description="""RS232 Interface//RS232 Schnittstelle""",
        mandatory=False,
        section="Command Interfaces",
    )

    ethernet = PropertyTypeAssignment(
        code="ETHERNET",
        data_type="BOOLEAN",
        property_label="Ethernet Interface",
        description="""Ethernet Interface//Ethernet Schnittstelle""",
        mandatory=False,
        section="Command Interfaces",
    )

    usb = PropertyTypeAssignment(
        code="USB",
        data_type="BOOLEAN",
        property_label="USB Interface",
        description="""USB Interface//USB Schnittstelle""",
        mandatory=False,
        section="Command Interfaces",
    )


class PowerSupply(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.POWER_SUPPLY",
        description="""Power Supply//Labornetzgerät""",
        generated_code_prefix="INS.POWR_SPPLY",
    )

    number_of_outputs = PropertyTypeAssignment(
        code="NUMBER_OF_OUTPUTS",
        data_type="INTEGER",
        property_label="Number of Outputs",
        description="""Number of Outputs//Anzahl der Ausgänge""",
        mandatory=False,
        section="Outputs",
    )

    max_output_voltage = PropertyTypeAssignment(
        code="MAX_OUTPUT_VOLTAGE",
        data_type="REAL",
        property_label="Maximum Output Voltage [V]",
        description="""Maximum Output Voltage [V]//Maximale Ausgangsspannung [V]""",
        mandatory=False,
        section="Outputs",
    )

    max_output_current = PropertyTypeAssignment(
        code="MAX_OUTPUT_CURRENT",
        data_type="REAL",
        property_label="Maximum Output Current [A]",
        description="""Maximum Output Current [A]//Maximaler Ausgangsstrom [A]""",
        mandatory=False,
        section="Outputs",
    )

    gpib = PropertyTypeAssignment(
        code="GPIB",
        data_type="BOOLEAN",
        property_label="GPIB Interface",
        description="""GPIB Interface//GPIB Schnittstelle""",
        mandatory=False,
        section="Command Interfaces",
    )

    rs232 = PropertyTypeAssignment(
        code="RS232",
        data_type="BOOLEAN",
        property_label="RS232 Interface",
        description="""RS232 Interface//RS232 Schnittstelle""",
        mandatory=False,
        section="Command Interfaces",
    )

    ethernet = PropertyTypeAssignment(
        code="ETHERNET",
        data_type="BOOLEAN",
        property_label="Ethernet Interface",
        description="""Ethernet Interface//Ethernet Schnittstelle""",
        mandatory=False,
        section="Command Interfaces",
    )

    usb = PropertyTypeAssignment(
        code="USB",
        data_type="BOOLEAN",
        property_label="USB Interface",
        description="""USB Interface//USB Schnittstelle""",
        mandatory=False,
        section="Command Interfaces",
    )


class MeasuringAmplifier(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.MEASURING_AMPLIFIER",
        description="""Measuring Amplifier//Messverstärker""",
        generated_code_prefix="INS.MEAS_AMP",
    )

    bandwidth = PropertyTypeAssignment(
        code="BANDWIDTH",
        data_type="REAL",
        property_label="Bandwidth [Hz]",
        description="""Bandwidth [Hz]//Bandbreite [Hz]""",
        mandatory=False,
        section="Technical Details",
    )

    accuracy_class_vde0410 = PropertyTypeAssignment(
        code="ACCURACY_CLASS_VDE0410",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="ACCURACY_CLASS_VDE0410",
        property_label="Accuracy Class according to VDE 0410",
        description="""Accuracy Class according to VDE 0410//Genauigkeitsklasse anch VDE 0410""",
        mandatory=False,
        section="Technical Details",
    )

    number_of_inputs = PropertyTypeAssignment(
        code="NUMBER_OF_INPUTS",
        data_type="INTEGER",
        property_label="Number of Inputs",
        description="""Number of Inputs//Anzahl der Eingänge""",
        mandatory=False,
        section="Inputs",
    )

    min_excitation_voltage = PropertyTypeAssignment(
        code="MIN_EXCITATION_VOLTAGE",
        data_type="REAL",
        property_label="Minimum Excitation Voltage [V]",
        description="""Minimum Excitation Voltage [V]//Minimale Speisespannung [V]""",
        mandatory=False,
        section="Inputs",
    )

    max_excitation_voltage = PropertyTypeAssignment(
        code="MAX_EXCITATION_VOLTAGE",
        data_type="REAL",
        property_label="Maximum Excitation Voltage [V]",
        description="""Maximum Excitation Voltage [V]//Maximale Speisespannung [V]""",
        mandatory=False,
        section="Inputs",
    )

    max_common_mode_voltage = PropertyTypeAssignment(
        code="MAX_COMMON_MODE_VOLTAGE",
        data_type="REAL",
        property_label="Maximum Common Mode Voltage [V]",
        description="""Maximum Common Mode Voltage [V]//Maximale Gleichtaktspannung [V]""",
        mandatory=False,
        section="Inputs",
    )

    number_of_analog_outputs = PropertyTypeAssignment(
        code="NUMBER_OF_ANALOG_OUTPUTS",
        data_type="INTEGER",
        property_label="Number of Analog Outputs",
        description="""Number of Analog Outputs//Anzahl Analoger Ausgänge""",
        mandatory=False,
        section="Outputs",
    )

    analog_output_voltage_min = PropertyTypeAssignment(
        code="ANALOG_OUTPUT_VOLTAGE_MIN",
        data_type="REAL",
        property_label="Analog Output Minimum Voltage [V]",
        description="""Analog Output Minimum Voltage [V]//Minimale Spannung am Analogen Ausgang [V]""",
        mandatory=False,
        section="Outputs",
    )

    analog_output_voltage_max = PropertyTypeAssignment(
        code="ANALOG_OUTPUT_VOLTAGE_MAX",
        data_type="REAL",
        property_label="Analog Output Maximum Voltage [V]",
        description="""Analog Output Maximum Voltage [V]//Maximale Spannung am Analogen Ausgang [V]""",
        mandatory=False,
        section="Outputs",
    )

    gpib = PropertyTypeAssignment(
        code="GPIB",
        data_type="BOOLEAN",
        property_label="GPIB Interface",
        description="""GPIB Interface//GPIB Schnittstelle""",
        mandatory=False,
        section="Command Interfaces",
    )

    rs232 = PropertyTypeAssignment(
        code="RS232",
        data_type="BOOLEAN",
        property_label="RS232 Interface",
        description="""RS232 Interface//RS232 Schnittstelle""",
        mandatory=False,
        section="Command Interfaces",
    )

    ethernet = PropertyTypeAssignment(
        code="ETHERNET",
        data_type="BOOLEAN",
        property_label="Ethernet Interface",
        description="""Ethernet Interface//Ethernet Schnittstelle""",
        mandatory=False,
        section="Command Interfaces",
    )

    usb = PropertyTypeAssignment(
        code="USB",
        data_type="BOOLEAN",
        property_label="USB Interface",
        description="""USB Interface//USB Schnittstelle""",
        mandatory=False,
        section="Command Interfaces",
    )

    calibration_interval = PropertyTypeAssignment(
        code="CALIBRATION_INTERVAL",
        data_type="INTEGER",
        property_label="Calibration Interval [months]",
        description="""Calibration Interval [months]//Kalibrierintervall [Monate]""",
        mandatory=False,
        section="Status",
    )


class LaserLineScanner(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.LASER_LINE_SCANNER",
        description="""A laser scanner used to measure 2D profiles along a laser line//Laserlinienscanner""",
        generated_code_prefix="INS.LAS_LINE_SCAN",
    )

    instrument_laser_scanner_z_min = PropertyTypeAssignment(
        code="INSTRUMENT.LASER_SCANNER.Z_MIN",
        data_type="REAL",
        property_label="Minimum z distance [mm]",
        description="""Minimal measuring distance in z-Direction//Minimaler Messabstand in z-Richtung""",
        mandatory=False,
        section="Laser Sensor Information",
    )

    instrument_laser_scanner_z_max = PropertyTypeAssignment(
        code="INSTRUMENT.LASER_SCANNER.Z_MAX",
        data_type="REAL",
        property_label="Maximum z distance [mm]",
        description="""Maximum measuring distance in z-Direction//Maximaler Messabstand in z-Richtung""",
        mandatory=False,
        section="Laser Sensor Information",
    )

    instrument_laser_scanner_x_min = PropertyTypeAssignment(
        code="INSTRUMENT.LASER_SCANNER.X_MIN",
        data_type="REAL",
        property_label="Minimum x measuring range [mm]",
        description="""Minimal measuring distance in z-Direction//Minimaler Messabstand in z-Richtung""",
        mandatory=False,
        section="Laser Sensor Information",
    )

    instrument_laser_scanner_x_max = PropertyTypeAssignment(
        code="INSTRUMENT.LASER_SCANNER.X_MAX",
        data_type="REAL",
        property_label="Maximum x measuring range [mm]",
        description="""Maximum measuring distance in z-Direction//Maximaler Messabstand in z-Richtung""",
        mandatory=False,
        section="Laser Sensor Information",
    )

    instrument_laser_scanner_line_resolution = PropertyTypeAssignment(
        code="INSTRUMENT.LASER_SCANNER.LINE_RESOLUTION",
        data_type="INTEGER",
        property_label="Maximum line resolution [pixel]",
        description="""Maximum resolution per laser line//Maximale Anzahl Messpunkte per Linienmessung""",
        mandatory=False,
        section="Laser Sensor Information",
    )

    laser_wavelength = PropertyTypeAssignment(
        code="LASER_WAVELENGTH",
        data_type="VARCHAR",
        property_label="Laser wavelength [nm]",
        description="""Wavelength of emitted laser light//Wellenlänge des Laserlichts""",
        mandatory=False,
        section="Laser Sensor Information",
    )

    laser_class = PropertyTypeAssignment(
        code="LASER_CLASS",
        data_type="VARCHAR",
        property_label="Laser class",
        description="""Laser class rating according to DIN EN 60825-1//Laserklasse nach DIN EN 60825-1""",
        mandatory=False,
        section="Laser Sensor Information",
    )

    firmware_version = PropertyTypeAssignment(
        code="FIRMWARE_VERSION",
        data_type="VARCHAR",
        property_label="Current firmware version",
        description="""The currently installed firmware version//Die aktuell installierte Firmware-Version""",
        mandatory=False,
        section="Software Information",
    )

    last_systemcheck = PropertyTypeAssignment(
        code="LAST_SYSTEMCHECK",
        data_type="DATE",
        property_label="Last System Check",
        description="""Date of the last system check//Datum des letzten Systemchecks""",
        mandatory=False,
        section="Additional Information",
    )


class Centrifuge(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.CENTRIFUGE",
        description="""Centrifuge//Zentrifuge""",
        generated_code_prefix="INS.CEN",
    )

    centrifuge_maximum_speed_rpm = PropertyTypeAssignment(
        code="CENTRIFUGE.MAXIMUM_SPEED_RPM",
        data_type="INTEGER",
        property_label="Maximum Centrifugation Speed (depending on rotor) [rpm]",
        description="""Maximum Centrifugation Speed (depending on rotor) [rpm]//Maximale Zentrifugationsgeschwindigkeit (rotorabhängig) [rpm]""",
        mandatory=False,
        section="Instrument Specification",
    )

    centrifuge_maximum_speed_rcf = PropertyTypeAssignment(
        code="CENTRIFUGE.MAXIMUM_SPEED_RCF",
        data_type="INTEGER",
        property_label="Maximum Centrifugation Speed (depending on rotor) [rcf]",  # ToDo: not a valid pint unit
        description="""Maximum Centrifugation Speed (depending on rotor) [rcf]//Maximale Zentrifugationsgeschwindigkeit (rotorabhängig) [rcf]""",
        mandatory=False,
        section="Instrument Specification",
    )

    centrifuge_is_temperature_controlled = PropertyTypeAssignment(
        code="CENTRIFUGE.IS_TEMPERATURE_CONTROLLED",
        data_type="BOOLEAN",
        property_label="Temperature can be set",
        description="""Centrifuge Temperature can be set//Zentrifuge ist temperierbar""",
        mandatory=False,
        section="Instrument Specification",
    )

    centrifuge_minimum_temperature = PropertyTypeAssignment(
        code="CENTRIFUGE.MINIMUM_TEMPERATURE",
        data_type="INTEGER",
        property_label="Minimum Temperature [°C]",
        description="""Minimum Centrifuge Temperature [°C]//Minimale Zentrifugen-Temperatur [°C]""",
        mandatory=False,
        section="Instrument Specification",
    )

    centrifuge_maximum_temperature = PropertyTypeAssignment(
        code="CENTRIFUGE.MAXIMUM_TEMPERATURE",
        data_type="INTEGER",
        property_label="Maximum Temperature [°C]",
        description="""Maximum Centrifuge Temperature [°C]//Maximale Zentrifugen-Temperatur [°C]""",
        mandatory=False,
        section="Instrument Specification",
    )

    centrifuge_compatible_rotors = PropertyTypeAssignment(
        code="CENTRIFUGE.COMPATIBLE_ROTORS",
        data_type="VARCHAR",
        property_label="Compatible Rotors",
        description="""Compatible Rotors with this Centrifuge//Kompatible Rotatoren mit dieser Zentrifuge""",
        mandatory=False,
        section="Instrument Specification",
    )

    centrifuge_requires_dguv_checking = PropertyTypeAssignment(
        code="CENTRIFUGE.REQUIRES_DGUV_CHECKING",
        data_type="BOOLEAN",
        property_label="Requires DGUV check",
        description="""Requires checks according to DGUV Paragraph 3 Rule 100-500//Sicherheitstechnische Überprüfung gemäß DGUV Paragraph 3 Regel 100-500 vorgeschrieben""",
        mandatory=False,
        section="Instrument Specification",
    )

    centrifuge_date_last_dguv_checking = PropertyTypeAssignment(
        code="CENTRIFUGE.DATE_LAST_DGUV_CHECKING",
        data_type="DATE",
        property_label="Date of last DGUV check",
        description="""Date of last checks according to DGUV Paragraph 3 Rule 100-500//Datum der letzten sicherheitstechnischen Überprüfung gemäß DGUV Paragraph 3 Regel 100-500""",
        mandatory=False,
        section="Instrument Specification",
    )


class CentrifugeRotor(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.CENTRIFUGE_ROTOR",
        description="""Centrifuge Rotor//Zentrifugenrotor""",
        generated_code_prefix="INS.CEN_ROT",
    )

    centrifuge_rotor_maximum_speed_rpm = PropertyTypeAssignment(
        code="CENTRIFUGE_ROTOR.MAXIMUM_SPEED_RPM",
        data_type="INTEGER",
        property_label="Maximum Speed [rpm]",
        description="""Maximum Rotor Speed [rpm]//Maximale Rotor-Geschwindigkeit [rpm]""",
        mandatory=False,
        section="Rotor Specification",
    )

    centrifuge_rotor_maximum_speed_rcf = PropertyTypeAssignment(
        code="CENTRIFUGE_ROTOR.MAXIMUM_SPEED_RCF",
        data_type="INTEGER",
        property_label="Maximum Speed [rcf]",  # ToDo: not a valid pint unit
        description="""Maximum Rotor Speed [rcf]//Maximale Rotor-Geschwindigkeit [rcf]""",
        mandatory=False,
        section="Rotor Specification",
    )

    centrifuge_rotor_maximum_capacity_vials = PropertyTypeAssignment(
        code="CENTRIFUGE_ROTOR.MAXIMUM_CAPACITY_VIALS",
        data_type="INTEGER",
        property_label="Maximum Capacity (Number of Vials)",
        description="""Maximum Rotor Capacity (number of vials)//Maximale Rotor-Kapazität (Anzahl an Gefäßen)""",
        mandatory=False,
        section="Rotor Specification",
    )

    centrifuge_rotor_maximum_capacity_volume = PropertyTypeAssignment(
        code="CENTRIFUGE_ROTOR.MAXIMUM_CAPACITY_VOLUME",
        data_type="INTEGER",
        property_label="Maximum Capacity (Volume) [mL]",
        description="""Maximum Rotor Capacity (volume) [mL]//Maximale Rotor-Kapazität (Volumen) [mL]""",
        mandatory=False,
        section="Rotor Specification",
    )

    centrifuge_rotor_compatible_vials = PropertyTypeAssignment(
        code="CENTRIFUGE_ROTOR.COMPATIBLE_VIALS",
        data_type="VARCHAR",
        property_label="Compatible vials (possibly with adapters)",
        description="""Compatible vials (possibly with adapters)//Kompatible Gefäße (ggf. mit Adapter)""",
        mandatory=False,
        section="Rotor Specification",
    )


# Freezer is defined several times in the model
class Freezer2(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.FREEZER",
        description="""Cooling Device//Kühlgerät""",
        generated_code_prefix="INS.FRE",
    )

    temp_min_celsius = PropertyTypeAssignment(
        code="TEMP_MIN_CELSIUS",
        data_type="REAL",
        property_label="Temperature Minimum [°C]",
        description="""Minimum Temperature [°C]//Minimaltemperatur [°C]""",
        mandatory=True,
        section="Freezer Details",
    )

    temp_max_celsius = PropertyTypeAssignment(
        code="TEMP_MAX_CELSIUS",
        data_type="REAL",
        property_label="Temperature Maximum [°C]",
        description="""Maximum Temperature [°C]//Maximaltemperatur [°C]""",
        mandatory=True,
        section="Freezer Details",
    )


class Scale(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.SCALE",
        description="""Scale//Waage""",
        generated_code_prefix="INS.SCA",
    )

    weight_min = PropertyTypeAssignment(
        code="WEIGHT_MIN",
        data_type="REAL",
        property_label="Minimum weight",
        description="""Minimum weight (in UNIT_MASS)//Minimales Gewicht (in UNIT_MASS)""",
        mandatory=True,
        section="Technical Details",
    )

    weight_max = PropertyTypeAssignment(
        code="WEIGHT_MAX",
        data_type="REAL",
        property_label="Maximum weight",
        description="""Maximum weight (in UNIT_MASS)//Maximales Gewicht (in UNIT_MASS)""",
        mandatory=True,
        section="Technical Details",
    )

    precision_mass = PropertyTypeAssignment(
        code="PRECISION_MASS",
        data_type="REAL",
        property_label="Measurement precision//Messgenauigkeit",
        description="""Precision of the scale/measurement  (in UNIT_MASS)//Messgenauigkeit Waage/Messung  (in UNIT_MASS)""",
        mandatory=False,
        section="Technical Details",
    )

    unit_mass = PropertyTypeAssignment(
        code="UNIT_MASS",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="UNIT_MASS",
        property_label="Mass unit//Masseeinheit",
        description="""Mass unit//Masseeinheit""",
        mandatory=True,
        section="Technical Details",
    )


class SpectrometerOptical(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.SPECTROMETER_OPTICAL",
        description="""Optical Spectrometer//Optisches Spektrometer""",
        generated_code_prefix="INS.SPEC_OPT",
    )

    detection_range_min_in_nm = PropertyTypeAssignment(
        code="DETECTION_RANGE_MIN_IN_NM",
        data_type="REAL",
        property_label="Detection Range Min [nm]",
        description="""Minimal detectable wavelength [nm]//Minimale detektierbare Wellenlänge [nm]""",
        mandatory=False,
        section="Specifications",
    )

    detection_range_max_in_nm = PropertyTypeAssignment(
        code="DETECTION_RANGE_MAX_IN_NM",
        data_type="REAL",
        property_label="Detection Range Max [nm]",
        description="""Maximal detectable wavelength [nm]//Maximale detektierbare Wellenlänge [nm]""",
        mandatory=False,
        section="Specifications",
    )

    spectrometer_type = PropertyTypeAssignment(
        code="SPECTROMETER_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="OPTICAL_SPECTROMETER_TYPE",
        property_label="Spectrometer Type",
        description="""Type of spectrometer//Spektrometertyp""",
        mandatory=False,
        section="Specifications",
    )


class LaserGeneral(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.LASER_GENERAL",
        description="""Generalized laser entry//Generischer Laser""",
        generated_code_prefix="INS.LAS_GEN",
    )

    laser_pulse_energy_normal_in_mj = PropertyTypeAssignment(
        code="LASER_PULSE_ENERGY_NORMAL_IN_MJ",
        data_type="REAL",
        property_label="Nominal Pulse Energy [mJ]",
        description="""Nominal pulse energy in mJ//Nominale Pulsenergie in mJ""",
        mandatory=False,
        section="Laser Specifications",
    )

    laser_beam_diameter_in_mm = PropertyTypeAssignment(
        code="LASER_BEAM_DIAMETER_IN_MM",
        data_type="REAL",
        property_label="Beam Diameter [mm]",
        description="""Output laser beam diameter in mm//Durchmesser des Ausgangslaserstrahls in mm""",
        mandatory=False,
        section="Laser Specifications",
    )

    laser_wavelength_in_nm = PropertyTypeAssignment(
        code="LASER_WAVELENGTH_IN_NM",
        data_type="XML",
        property_label="Operating Wavelength(s) [nm]",
        description="""List all allowed wavelengths following the XML schema given//Auflistung aller zulässigen Wellenlängen gemäß dem angegebenen XML-Schema""",
        mandatory=False,
        section="Laser Specifications",
    )

    laser_repetition_rate_in_hz = PropertyTypeAssignment(
        code="LASER_REPETITION_RATE_IN_HZ",
        data_type="REAL",
        property_label="Repetition Rate [Hz]",
        description="""Maximum repetition rate (-1 for CW) in Hz//Maximale Wiederholrate (-1 für CW) in Hz""",
        mandatory=False,
        section="Laser Specifications",
    )

    laser_m2 = PropertyTypeAssignment(
        code="LASER_M2",
        data_type="REAL",
        property_label="M²",
        description="""M² (parameter which relates the beam divergence of a laser beam to the minimum focussed spot size that can be achieved)//M² (Beugungsmaßzahl, welche beschreibt, wie gut ein Laserstrahl bei einer gegebenen Divergenz fokussiert werden kann)""",
        mandatory=False,
        section="Laser Specifications",
    )

    laser_type = PropertyTypeAssignment(
        code="LASER_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="LASER_TYPE",
        property_label="Laser Type",
        description="""Type of the laser//Lasertyp""",
        mandatory=False,
        section="Laser Specifications",
    )


class FlashLamp(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.FLASH_LAMP",
        description="""Flash lamp//Blitzlampe""",
        generated_code_prefix="INS.FLA_LAM",
    )

    max_pulse_energy_in_joule = PropertyTypeAssignment(
        code="MAX_PULSE_ENERGY_IN_JOULE",
        data_type="REAL",
        property_label="Maximum pulse energy [J]",
        description="""Maximum pulse energy in J//Maximale Pulsenergie in J""",
        mandatory=True,
        section="Flash Lamp Specifics",
    )

    flash_lamp_shape = PropertyTypeAssignment(
        code="FLASH_LAMP_SHAPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="FLASH_LAMP_SHAPE",
        property_label="Lamp shape",
        description="""Lamp shape//Lampenform""",
        mandatory=True,
        section="Flash Lamp Specifics",
    )


class ObjectiveSpacer(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.OBJECTIVE_SPACER",
        description="""Objective spacer//Abstandsring""",
        generated_code_prefix="INS.OBJ_SPA",
    )

    thickness_in_millimeter = PropertyTypeAssignment(
        code="THICKNESS_IN_MILLIMETER",
        data_type="REAL",
        property_label="Thickness [mm]",
        description="""Thickness of the spacer in mm//Dicke des Abstandsringes in mm""",
        mandatory=True,
        section="Properties",
    )


class LocalWorkstation(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.LOCAL_WORKSTATION",
        description="""BAM local workstation//BAM Arbeitsstation""",
        generated_code_prefix="INS.LOC_WOR",
    )

    operating_system = PropertyTypeAssignment(
        code="OPERATING_SYSTEM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="OPERATING_SYSTEM",
        property_label="Operating System",
        description="""Operating System (OS)//Betriebssystem""",
        mandatory=False,
        section="Technical Information",
    )


class Camera(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.CAMERA",
        description="""A generic camera  device for recording video or photos//Eine generische Kamera für Video- oder Fotoaufnahmen""",
        generated_code_prefix="INS.CAM",
    )

    image_sensor_name = PropertyTypeAssignment(
        code="IMAGE_SENSOR_NAME",
        data_type="VARCHAR",
        property_label="Sensor",
        description="""Name of the image sensor model//Modellbezeichnung des Bildsensors""",
        mandatory=False,
        section="Camera Information",
    )

    image_sensor_size = PropertyTypeAssignment(
        code="IMAGE_SENSOR_SIZE",
        data_type="VARCHAR",
        property_label="Sensor size",
        description="""Size of the image sensor//Größenangabe des Bildsensors""",
        mandatory=False,
        section="Camera Information",
    )

    image_sensor_resolution_horizontal = PropertyTypeAssignment(
        code="IMAGE_SENSOR_RESOLUTION_HORIZONTAL",
        data_type="INTEGER",
        property_label="Horizontal sensor resolution [pixel]",
        description="""Horizontal camera resolution in pixel//Horizontale Auflösung des Sensors""",
        mandatory=True,
        section="Camera Information",
    )

    image_sensor_resolution_vertical = PropertyTypeAssignment(
        code="IMAGE_SENSOR_RESOLUTION_VERTICAL",
        data_type="INTEGER",
        property_label="Vertical camera resolution [pixel]",
        description="""Vertical camera resolution in pixel//Vertikale Sensorauflösung in pixel""",
        mandatory=True,
        section="Camera Information",
    )

    image_sensor_framerate = PropertyTypeAssignment(
        code="IMAGE_SENSOR_FRAMERATE",
        data_type="REAL",
        property_label="Framerate (at max. resolution)",
        description="""Highest framerate at indicated maximum resolution//Höchste erreichbare Bildrate bei voller Auflösung""",
        mandatory=False,
        section="Camera Information",
    )

    lens_mount_type = PropertyTypeAssignment(
        code="LENS_MOUNT_TYPE",
        data_type="VARCHAR",
        property_label="Lens mount",
        description="""The lens mount of a camera or lens//Art des Objektivanschluss""",
        mandatory=False,
        section="Camera Information",
    )

    firmware_version = PropertyTypeAssignment(
        code="FIRMWARE_VERSION",
        data_type="VARCHAR",
        property_label="Current firmware version",
        description="""The currently installed firmware version//Die aktuell installierte Firmware-Version""",
        mandatory=False,
        section="Software Information",
    )

    last_systemcheck = PropertyTypeAssignment(
        code="LAST_SYSTEMCHECK",
        data_type="DATE",
        property_label="Last System Check",
        description="""Date of the last system check//Datum des letzten Systemchecks""",
        mandatory=False,
        section="Additional Information",
    )


class Lens(Camera):
    defs = ObjectTypeDef(
        code="INSTRUMENT.CAMERA.LENS",
        description="""Lens used together with imaging camera//Objektiv für Bildaufnahmen mit einer Kamera""",
        generated_code_prefix="INS.CAM.LENS",
    )

    lens_focallength = PropertyTypeAssignment(
        code="LENS_FOCALLENGTH",
        data_type="REAL",
        property_label="Focal length [mm]",
        description="""Focal length of optical lens [mm]//Brennweite der Kameralinse [mm]""",
        mandatory=True,
        section="Lens Information",
    )

    lens_aperture_max = PropertyTypeAssignment(
        code="LENS_APERTURE_MAX",
        data_type="REAL",
        property_label="Maximum Aperture [f/]",  # ToDo: not a valid pint unit
        description="""Maximum Aperture [f/]//Maximale Blendenöffnung [f/]""",
        mandatory=False,
        section="Lens Information",
    )

    lens_aperture_min = PropertyTypeAssignment(
        code="LENS_APERTURE_MIN",
        data_type="REAL",
        property_label="Minimum Aperture [f/]",  # ToDo: not a valid pint unit
        description="""Minimum Aperture [f/]//Minimale Blendenzahl [f/]""",
        mandatory=False,
        section="Lens Information",
    )

    lens_confocal = PropertyTypeAssignment(
        code="LENS_CONFOCAL",
        data_type="BOOLEAN",
        property_label="Confocal",
        description="""Confocal optics//Konfokale Linse""",
        mandatory=False,
        section="Lens Information",
    )


class Ellipsometer(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.ELLIPSOMETER",
        description="""Ellipsometer//Ellipsometer""",
        generated_code_prefix="INS.ELLIPS",
    )

    ellipsometric_configuration = PropertyTypeAssignment(
        code="ELLIPSOMETRIC_CONFIGURATION",
        data_type="VARCHAR",
        property_label="Ellipsometric Configuration",
        description="""Ellipsometric configuration//Ellipsometrisches Konfigurationsschema""",
        mandatory=False,
        section="Ellipsometer Information",
    )

    ellipsometric_arrangement = PropertyTypeAssignment(
        code="ELLIPSOMETRIC_ARRANGEMENT",
        data_type="VARCHAR",
        property_label="Ellipsometric Arrangement",
        description="""Ellipsometric arrangement//Ellipsometrisches Arrangementschema""",
        mandatory=False,
        section="Ellipsometer Information",
    )

    elli_spectral_range_lower = PropertyTypeAssignment(
        code="ELLI_SPECTRAL_RANGE_LOWER",
        data_type="REAL",
        property_label="Low end of spectral range",
        description="""Low end of spectral range//Spektralbereich kleinste Zahl""",
        mandatory=False,
        section="Ellipsometer Information",
    )

    elli_spectral_range_upper = PropertyTypeAssignment(
        code="ELLI_SPECTRAL_RANGE_UPPER",
        data_type="REAL",
        property_label="High end of spectral range",
        description="""High end of spectral range//Spektralbereich größte Zahl""",
        mandatory=False,
        section="Ellipsometer Information",
    )

    elli_spectral_range_units = PropertyTypeAssignment(
        code="ELLI_SPECTRAL_RANGE_UNITS",
        data_type="VARCHAR",
        property_label="Spectral range units",
        description="""Spectral range units (eV, nm, cm-1, meV...)//Spektralbereich Einheiten (eV, nm, cm-1, meV...)""",
        mandatory=False,
        section="Ellipsometer Information",
    )

    elli_aoi_range_lower = PropertyTypeAssignment(
        code="ELLI_AOI_RANGE_LOWER",
        data_type="REAL",
        property_label="Low end of angle of incidence (AOI) range",
        units="degrees",
        description="""Low end of angle of incidence (AOI) range//AOI Bereich kleinste Zahl""",
        mandatory=False,
        section="Ellipsometer Information",
    )

    elli_aoi_range_upper = PropertyTypeAssignment(
        code="ELLI_AOI_RANGE_UPPER",
        data_type="REAL",
        property_label="High end of angle of incidence (AOI) range",
        units="degrees",
        description="""High end of angle of incidence (AOI) range//AOI Bereich größte Zahl""",
        mandatory=False,
        section="Ellipsometer Information",
    )

    elli_auto_align_option = PropertyTypeAssignment(
        code="ELLI_AUTO_ALIGN_OPTION",
        data_type="BOOLEAN",
        property_label="Is auto alignment option present?",
        description="""Automatic sample align option present?//Automatische Probenpositionierung vorhanden?""",
        mandatory=False,
        section="Ellipsometer Information",
    )

    elli_azimuth_angle_option = PropertyTypeAssignment(
        code="ELLI_AZIMUTH_ANGLE_OPTION",
        data_type="BOOLEAN",
        property_label="Is azimuth angle variable?",
        description="""Azimuth angle variable?//Azimutwinkel variabel?""",
        mandatory=False,
        section="Ellipsometer Information",
    )

    elli_light_sources = PropertyTypeAssignment(
        code="ELLI_LIGHT_SOURCES",
        data_type="VARCHAR",
        property_label="Light sources",
        description="""Light sources//Lichtquellen""",
        mandatory=False,
        section="Ellipsometer Information",
    )

    elli_focusing_option = PropertyTypeAssignment(
        code="ELLI_FOCUSING_OPTION",
        data_type="BOOLEAN",
        property_label="Is focusing option present?",
        description="""Focusing option present?//Fokussierungsoption vorhanden?""",
        mandatory=False,
        section="Ellipsometer Information Accessory",
    )

    elli_temperature_control_option = PropertyTypeAssignment(
        code="ELLI_TEMPERATURE_CONTROL_OPTION",
        data_type="BOOLEAN",
        property_label="Is temperature control option present?",
        description="""Temperature control option present?//Temperaturkontrolloption vorhanden?""",
        mandatory=False,
        section="Ellipsometer Information Accessory",
    )

    elli_liquid_cell_option = PropertyTypeAssignment(
        code="ELLI_LIQUID_CELL_OPTION",
        data_type="BOOLEAN",
        property_label="Is liquid cell option present?",
        description="""Liquid cell option present?//Flüssigkeitszellenoption vorhanden?""",
        mandatory=False,
        section="Ellipsometer Information Accessory",
    )

    elli_other_accessory = PropertyTypeAssignment(
        code="ELLI_OTHER_ACCESSORY",
        data_type="MULTILINE_VARCHAR",
        property_label="List of other accessory devices",
        description="""List of other accessory devices (e.g., gas cell, electrochemistry, adsorption, etc.)//Liste anderer Zubehörgeräte (z. B. Gaskammer, Elektrochemie, Adsorption usw.)""",
        mandatory=False,
        section="Ellipsometer Information Accessory",
    )

    elli_mapping_option = PropertyTypeAssignment(
        code="ELLI_MAPPING_OPTION",
        data_type="BOOLEAN",
        property_label="Is mapping option present?",
        description="""Mapping option present?//Mapping-Option vorhanden?""",
        mandatory=False,
        section="Ellipsometer Information Mapping",
    )

    elli_mapping_range = PropertyTypeAssignment(
        code="ELLI_MAPPING_RANGE",
        data_type="VARCHAR",
        property_label="Mapping range in X x Y format",
        units="cm^2",
        description="""Mapping range (e.g., 20 x 20)//Mapping-Bereich (z. B. 20 x 20)""",
        mandatory=False,
        section="Ellipsometer Information Mapping",
    )

    elli_imaging_option = PropertyTypeAssignment(
        code="ELLI_IMAGING_OPTION",
        data_type="BOOLEAN",
        property_label="Is imaging option present?",
        description="""Imaging option present?//Imaging-Option vorhanden?""",
        mandatory=False,
        section="Ellipsometer Information Imaging",
    )

    elli_imaging_elli_lenses = PropertyTypeAssignment(
        code="ELLI_IMAGING_ELLI_LENSES",
        data_type="MULTILINE_VARCHAR",
        property_label="Imaging ellipsometer list of focusing lenses",
        description="""Imaging ellipsometer lenses (Nikon 2.5x, Nikon 5x, Nikon 10x, Nikon 20x, Nikon 50x, etc.)//Imaging-Ellipsometerlinsen (Nikon 2,5x, Nikon 5x, Nikon 10x, Nikon 20x, Nikon 50x usw.)""",
        mandatory=False,
        section="Ellipsometer Information Imaging",
    )

    elli_imaging_cameras = PropertyTypeAssignment(
        code="ELLI_IMAGING_CAMERAS",
        data_type="MULTILINE_VARCHAR",
        property_label="Imaging ellipsometer list of cameras",
        description="""Imaging ellipsometer cameras (UV, VIS, NIR)//Imaging-Ellipsometerkameras (UV, VIS, NIR)""",
        mandatory=False,
        section="Ellipsometer Information Imaging",
    )

    elli_imaging_camera_x = PropertyTypeAssignment(
        code="ELLI_IMAGING_CAMERA_X",
        data_type="INTEGER",
        property_label="Imaging ellipsometer camera X resolution",
        units="pixels",
        description="""Imaging ellipsometer camera X resolution (e.g., 1024)//Imaging-Ellipsometerkamera X-Auflösung (z. B. 1024)""",
        mandatory=False,
        section="Ellipsometer Information Imaging",
    )

    elli_imaging_camera_y = PropertyTypeAssignment(
        code="ELLI_IMAGING_CAMERA_Y",
        data_type="INTEGER",
        property_label="Imaging ellipsometer camera Y resolution",
        units="pixels",
        description="""Imaging ellipsometer camera Y resolution (e.g., 1024)//Imaging-Ellipsometerkamera Y-Auflösung (z. B. 1024)""",
        mandatory=False,
        section="Ellipsometer Information Imaging",
    )
