from bam_masterdata.datamodel.activities import ExperimentalStep
from bam_masterdata.datamodel.instruments import Instrument
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment


class Ellipsometer(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.ELLIPSOMETER",
        description="""
        Ellipsometer instrument and its available capabilities and operating ranges//Ellipsometer
        und seine verfügbaren Funktionen und Betriebsbereiche
        """,
        generated_code_prefix="INS.ELLIPS",
    )

    ellipsometric_configuration = PropertyTypeAssignment(
        code="ELLIPSOMETRIC_CONFIGURATION",
        data_type="VARCHAR",
        property_label="Available ellipsometric configuration",
        description="""
        Ellipsometric configuration supported by the instrument//Vom Instrument unterstützte
        ellipsometrische Konfiguration
        """,
        mandatory=False,
        section="Ellipsometer Information",
    )

    ellipsometric_arrangement = PropertyTypeAssignment(
        code="ELLIPSOMETRIC_ARRANGEMENT",
        data_type="VARCHAR",
        property_label="Available ellipsometric arrangement",
        description="""
        Ellipsometric arrangement supported by the instrument//Vom Instrument unterstützte ellipsometrische
        Anordnung
        """,
        mandatory=False,
        section="Ellipsometer Information",
    )

    elli_spectral_range_lower = PropertyTypeAssignment(
        code="ELLI_SPECTRAL_RANGE_LOWER",
        data_type="REAL",
        property_label="Lowest supported spectral range value",
        description="""
        Lowest spectral value supported by the instrument//Niedrigster vom Instrument unterstützter Spektralwert
        """,
        mandatory=False,
        section="Ellipsometer Information",
    )

    elli_spectral_range_upper = PropertyTypeAssignment(
        code="ELLI_SPECTRAL_RANGE_UPPER",
        data_type="REAL",
        property_label="Highest supported spectral range value",
        description="""
        Highest spectral value supported by the instrument//Höchster vom Instrument unterstützter Spektralwert
        """,
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
        property_label="Lowest supported angle of incidence (AOI)",
        units="degrees",
        description=(
            "Lowest angle of incidence (AOI) supported by the instrument"
            "//Kleinster vom Instrument unterstützter Einfallswinkel"
        ),
        mandatory=False,
        section="Ellipsometer Information",
    )

    elli_aoi_range_upper = PropertyTypeAssignment(
        code="ELLI_AOI_RANGE_UPPER",
        data_type="REAL",
        property_label="Highest supported angle of incidence (AOI)",
        units="degrees",
        description=(
            "Highest angle of incidence (AOI) supported by the instrument"
            "//Größter vom Instrument unterstützter Einfallswinkel"
        ),
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
        property_label="Available imaging cameras",
        description=(
            "Cameras installed or available on the imaging ellipsometer, "
            "e.g. VIS, NIR, UV"
            "//Am Imaging-Ellipsometer installierte oder verfügbare Kameras, "
            "z.B. VIS, NIR, UV"
        ),
        mandatory=False,
        section="Ellipsometer Information Imaging",
    )

    elli_imaging_camera_x = PropertyTypeAssignment(
        code="ELLI_IMAGING_CAMERA_X",
        data_type="INTEGER",
        property_label="Camera resolution in X direction",
        units="pixels",
        description=(
            "Native or available camera resolution in X direction (e.g., 1024)"
            "//Native oder verfügbare Kameraauflösung in X-Richtung (z. B. 1024)"
        ),
        mandatory=False,
        section="Ellipsometer Information Imaging",
    )

    elli_imaging_camera_y = PropertyTypeAssignment(
        code="ELLI_IMAGING_CAMERA_Y",
        data_type="INTEGER",
        property_label="Camera resolution in Y direction",
        units="pixels",
        description=(
            "Native or available camera resolution in Y direction (e.g., 1024)"
            "//Native oder verfügbare Kameraauflösung in Y-Richtung (z. B. 1024)"
        ),
        mandatory=False,
        section="Ellipsometer Information Imaging",
    )


class Ellipsometry(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.ELLIPSOMETRY",
        description="""
        Ellipsometry experiment including the measurement configuration and settings used
        for this experiment//Ellipsometrie-Experiment einschließlich der für dieses Experiment
        verwendeten Messkonfiguration und Einstellungen
        """,
        generated_code_prefix="EXP.ELLIPS",
    )

    elli_spectral_low = PropertyTypeAssignment(
        code="ELLI_SPECTRAL_LOW",
        data_type="REAL",
        property_label="Lowest spectral value used",
        description=(
            "Lowest spectral value used for this measurement"
            "//Niedrigster für diese Messung verwendeter Spektralwert"
        ),
        mandatory=False,
        section="Ellipsometry Details",
    )

    elli_spectral_high = PropertyTypeAssignment(
        code="ELLI_SPECTRAL_HIGH",
        data_type="REAL",
        property_label="Highest spectral value used",
        description=(
            "Highest spectral value used for this measurement"
            "//Höchster für diese Messung verwendeter Spektralwert"
        ),
        mandatory=False,
        section="Ellipsometry Details",
    )

    elli_spectral_range_units = PropertyTypeAssignment(
        code="ELLI_SPECTRAL_RANGE_UNITS",
        data_type="VARCHAR",
        property_label="Spectral range units",
        description="""Spectral range units (eV, nm, cm-1, meV...)//Spektralbereich Einheiten (eV, nm, cm-1, meV...)""",
        mandatory=False,
        section="Ellipsometry Details",
    )

    elli_n_spectral_points = PropertyTypeAssignment(
        code="ELLI_N_SPECTRAL_POINTS",
        data_type="INTEGER",
        property_label="Number of spectral points",
        description="""Number of spectral points//Anzahl der Spektralpunkte""",
        mandatory=False,
        section="Ellipsometry Details",
    )

    elli_quantity_type = PropertyTypeAssignment(
        code="ELLI_QUANTITY_TYPE",
        data_type="VARCHAR",
        property_label="Ellipsometric quantity type",
        description=(
            "Ellipsometric quantity or representation used for this measurement, "
            "e.g. MM, PD, Sx, NCS"
            "//Für diese Messung verwendete ellipsometrische Größe oder Darstellung, "
            "z.B. MM, PD, Sx, NCS"
        ),
        mandatory=False,
        section="Ellipsometry Details",
    )

    elli_aoi_low = PropertyTypeAssignment(
        code="ELLI_AOI_LOW",
        data_type="REAL",
        property_label="Lowest angle of incidence used",
        description=(
            "Lowest angle of incidence used for this measurement"
            "//Kleinster für diese Messung verwendeter Einfallswinkel"
        ),
        mandatory=False,
        section="Ellipsometry Details",
    )

    elli_aoi_high = PropertyTypeAssignment(
        code="ELLI_AOI_HIGH",
        data_type="REAL",
        property_label="Highest angle of incidence used",
        description=(
            "Highest angle of incidence used for this measurement"
            "//Größter für diese Messung verwendeter Einfallswinkel"
        ),
        mandatory=False,
        section="Ellipsometry Details",
    )

    elli_n_aoi = PropertyTypeAssignment(
        code="ELLI_N_AOI",
        data_type="INTEGER",
        property_label="Number of angles of incidence (AOI)",
        description="""Number of AOI, e.g. 3//Anzahl AOI, z.B. 3""",
        mandatory=False,
        section="Ellipsometry Details",
    )

    elli_focusing = PropertyTypeAssignment(
        code="ELLI_FOCUSING",
        data_type="BOOLEAN",
        property_label="Were focusing optics used?",
        description=(
            "Whether focusing optics were used for this measurement"
            "//Ob bei dieser Messung Fokussierungsoptiken verwendet wurden"
        ),
        mandatory=False,
        section="Ellipsometry Details",
    )

    elli_accessory = PropertyTypeAssignment(
        code="ELLI_ACCESSORY",
        data_type="MULTILINE_VARCHAR",
        property_label="Accessories used",
        description=(
            "Accessories used for this measurement, e.g. liquid cell, EC cell"
            "//Bei dieser Messung verwendetes Zubehör, z.B. Flüssigkeitszelle, "
            "elektrochemische Zelle"
        ),
        mandatory=False,
        section="Ellipsometry Details",
    )


class EllipsometryInSitu(Ellipsometry):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.ELLIPSOMETRY.ELLIPSOMETRY_IN_SITU",
        description=(
            "In situ or time-resolved ellipsometry experiment"
            "//In-situ- oder zeitaufgelöstes Ellipsometrie-Experiment"
        ),
        generated_code_prefix="EXP.ELLIPS.INSITU",
    )

    elli_in_situ_description = PropertyTypeAssignment(
        code="ELLI_INSITU_DESCR",
        data_type="MULTILINE_VARCHAR",
        property_label="In situ experiment description",
        description=(
            "Description of the in situ experiment, e.g. gas adsorption, electrochemistry, or porosimetry"
            "//Beschreibung des in situ Experiments, z.B. Gasadsorption, Elektrochemie oder Porosimetrie"
        ),
        mandatory=False,
        section="Ellipsometry In Situ Details",
    )

    elli_in_situ_duration = PropertyTypeAssignment(
        code="ELLI_INSITU_TIME",
        data_type="REAL",
        property_label="In situ experiment duration",
        units="s",
        description=(
            "Total duration of the in situ ellipsometry experiment"
            "//Gesamtdauer des In-situ-Ellipsometrie-Experiments"
        ),
        mandatory=False,
        section="Ellipsometry In Situ Details",
    )

    elli_in_situ_n_measurements = PropertyTypeAssignment(
        code="ELLI_INSITU_N_MEAS",
        data_type="INTEGER",
        property_label="Number of measurements",
        description=(
            "Number of individual measurements or time slices during the temperature-controlled or in situ experiment"
            "//Anzahl der Einzelmessungen oder Zeitschritte während des temperaturgeregelten oder in situ Experiments"
        ),
        mandatory=False,
        section="Ellipsometry In Situ Details",
    )


class EllipsometryInSituTemperature(EllipsometryInSitu):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.ELLIPSOMETRY.ELLIPSOMETRY_IN_SITU.ELLIPSOMETRY_IN_SITU_TEMPERATURE",
        description=(
            "Temperature-controlled in situ ellipsometry experiment"
            "//Temperaturgeregeltes In-situ-Ellipsometrie-Experiment"
        ),
        generated_code_prefix="EXP.ELLIPS.INSITU.T",
    )

    elli_temp_heating = PropertyTypeAssignment(
        code="ELLI_TEMP_HEATING",
        data_type="BOOLEAN",
        property_label="Was heating used?",
        description=(
            "Whether heating was used during the experiment"
            "//Ob während des Experiments geheizt wurde"
        ),
        mandatory=True,
        section="Ellipsometry Temperature Details",
    )

    elli_temp_cooling = PropertyTypeAssignment(
        code="ELLI_TEMP_COOLING",
        data_type="BOOLEAN",
        property_label="Was LN2 cooling used?",
        description=(
            "Whether LN2 cooling was used during the experiment"
            "//Ob während des Experiments eine LN2-Kühlung verwendet wurde"
        ),
        mandatory=True,
        section="Ellipsometry Temperature Details",
    )

    elli_temp_variable = PropertyTypeAssignment(
        code="ELLI_TEMP_VARIABLE",
        data_type="BOOLEAN",
        property_label="Was the temperature varied?",
        description=(
            "Whether the temperature varied during the measurement"
            "//Ob die Temperatur während der Messung variiert wurde"
        ),
        mandatory=True,
        section="Ellipsometry Temperature Details",
    )

    elli_temp_constant = PropertyTypeAssignment(
        code="ELLI_TEMP_T_CONST",
        data_type="REAL",
        property_label="Constant temperature",
        units="K",
        description=(
            "Temperature setpoint used for an isothermal measurement or time-series"
            "//Temperatur-Sollwert für eine isotherme Messung oder Zeitreihe"
        ),
        mandatory=False,
        section="Ellipsometry Temperature Details",
    )

    elli_temp_control_low = PropertyTypeAssignment(
        code="ELLI_TEMP_CONTROL_T_LOW",
        data_type="REAL",
        property_label="Minimum temperature",
        units="K",
        description=(
            "Minimum temperature of a variable-temperature experiment"
            "//Minimale Temperatur eines Experiments mit variabler Temperatur"
        ),
        mandatory=False,
        section="Ellipsometry Temperature Details",
    )

    elli_temp_control_high = PropertyTypeAssignment(
        code="ELLI_TEMP_CONTROL_T_HIGH",
        data_type="REAL",
        property_label="Maximum temperature",
        units="K",
        description=(
            "Maximum temperature of a variable-temperature experiment"
            "//Maximale Temperatur eines Experiments mit variabler Temperatur"
        ),
        mandatory=False,
        section="Ellipsometry Temperature Details",
    )

    elli_temp_heating_rate = PropertyTypeAssignment(
        code="ELLI_TEMP_CONTROL_R_HEAT",
        data_type="REAL",
        property_label="Maximum heating rate",
        units="K/min",
        description=(
            "Maximum heating rate used in the temperature program. "
            "The program may contain multiple ramps with different heating rates."
            "//Maximale im Temperaturprogramm verwendete Heizrate. "
            "Das Programm kann mehrere Rampen mit unterschiedlichen Heizraten enthalten."
        ),
        mandatory=False,
        section="Ellipsometry Temperature Details",
    )

    elli_temp_cooling_rate = PropertyTypeAssignment(
        code="ELLI_TEMP_CONTROL_R_COOL",
        data_type="REAL",
        property_label="Maximum cooling rate",
        units="K/min",
        description=(
            "Maximum cooling rate used in the temperature program. "
            "The program may contain multiple ramps with different cooling rates."
            "//Maximale im Temperaturprogramm verwendete Abkühlrate. "
            "Das Programm kann mehrere Rampen mit unterschiedlichen Abkühlraten enthalten."
        ),
        mandatory=False,
        section="Ellipsometry Temperature Details",
    )


class EllipsometryMapping(Ellipsometry):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.ELLIPSOMETRY_MAPPING",
        description="""Ellipsometry mapping//Ellipsometrisches Mapping""",
        generated_code_prefix="EXP.ELLIPS.MAP",
    )

    elli_mapping_n_points = PropertyTypeAssignment(
        code="ELLI_MAPPING_N_PTS",
        data_type="INTEGER",
        property_label="Number of mapping points",
        description=(
            "Number of measurement points in the mapping"
            "//Anzahl der Messpunkte im Mapping"
        ),
        mandatory=False,
        section="Ellipsometry Mapping Details",
    )

    elli_mapping_size = PropertyTypeAssignment(
        code="ELLI_MAPPING_SIZE",
        data_type="VARCHAR",
        property_label="Mapped area size",
        description=(
            "Size of the mapped area as x x y dimensions or diameter, including units"
            "//Größe des gemappten Bereichs als x x y Abmessungen oder Durchmesser, "
            "einschließlich Einheit"
        ),
        mandatory=False,
        section="Ellipsometry Mapping Details",
    )


class EllipsometryImaging(Ellipsometry):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.ELLIPSOMETRY_IMAGING",
        description="""Imaging ellipsometry//Bildgebende Ellipsometrie""",
        generated_code_prefix="EXP.ELLIPS.IMG",
    )

    elli_img_dataset_type = PropertyTypeAssignment(
        code="ELLI_IMG_DATASET_TYPE",
        data_type="VARCHAR",
        property_label="Imaging dataset type",
        description=(
            "Description of the imaging measurement strategy or resulting dataset, "
            "e.g. ROI spectra, pixel shot, ellipsometric map"
            "//Beschreibung der bildgebenden Messstrategie oder des resultierenden Datensatzes, "
            "z. B. ROI-Spektren, Pixel-Aufnahme, ellipsometrische Karte"
        ),
        mandatory=True,
        section="Imaging Ellipsometry Details",
    )

    elli_img_n_pixels_x = PropertyTypeAssignment(
        code="ELLI_IMG_N_PIXELS_X",
        data_type="INTEGER",
        property_label="Acquired image size in X direction",
        units="pixels",
        description=(
            "Number of pixels in X direction of the image acquired in this experiment"
            "//Anzahl der Pixel in X-Richtung des in diesem Experiment aufgenommenen Bildes"
        ),
        mandatory=False,
        section="Imaging Ellipsometry Details",
    )

    elli_img_n_pixels_y = PropertyTypeAssignment(
        code="ELLI_IMG_N_PIXELS_Y",
        data_type="INTEGER",
        property_label="Acquired image size in Y direction",
        units="pixels",
        description=(
            "Number of pixels in Y direction of the image acquired in this experiment"
            "//Anzahl der Pixel in Y-Richtung des in diesem Experiment aufgenommenen Bildes"
        ),
        mandatory=False,
        section="Imaging Ellipsometry Details",
    )

    elli_img_lens_used = PropertyTypeAssignment(
        code="ELLI_IMG_LENS_USED",
        data_type="VARCHAR",
        property_label="Lens used",
        description=(
            "Lens used during the imaging ellipsometry experiment, e.g. Nikon 10x"
            "//Bei der bildgebenden Ellipsometrie verwendetes Objektiv, z.B. Nikon 10x"
        ),
        mandatory=True,
        section="Imaging Ellipsometry Details",
    )

    elli_img_camera_used = PropertyTypeAssignment(
        code="ELLI_IMG_CAMERA_USED",
        data_type="VARCHAR",
        property_label="Camera used",
        description=(
            "Camera used for this imaging ellipsometry experiment, "
            "e.g. VIS, NIR, UV"
            "//Für dieses Imaging-Ellipsometrie-Experiment verwendete Kamera, "
            "z.B. VIS, NIR, UV"
        ),
        mandatory=False,
        section="Imaging Ellipsometry Details",
    )

    elli_img_n_rois = PropertyTypeAssignment(
        code="ELLI_IMG_N_ROIS",
        data_type="INTEGER",
        property_label="Number of ROIs",
        description=(
            "Number of regions of interest (ROIs)"
            "//Anzahl der Regions of Interest (ROIs)"
        ),
        mandatory=False,
        section="Imaging Ellipsometry Details",
    )

    elli_img_focus_scanning = PropertyTypeAssignment(
        code="ELLI_IMG_FOCUSSCANNING",
        data_type="BOOLEAN",
        property_label="Was focus scanning used?",
        description=(
            "Whether focus scanning was used during the measurement"
            "//Ob Fokus-Scanning während der Messung verwendet wurde"
        ),
        mandatory=True,
        section="Imaging Ellipsometry Details",
    )

    elli_img_multi_measurement = PropertyTypeAssignment(
        code="ELLI_IMG_MULTI",
        data_type="BOOLEAN",
        property_label="Were multiple measurements or image stitching used?",
        description=(
            "Whether multiple measurement fields or image stitching were used"
            "//Ob mehrere Messfelder oder Image-Stitching verwendet wurden"
        ),
        mandatory=False,
        section="Imaging Ellipsometry Details",
    )

    elli_img_n_images = PropertyTypeAssignment(
        code="ELLI_IMG_MULTI_N_IMAGES",
        data_type="INTEGER",
        property_label="Number of images",
        description=(
            "Number of images used for multiple measurements or stitching"
            "//Anzahl der Bilder für Mehrfachmessungen oder Stitching"
        ),
        mandatory=False,
        section="Imaging Ellipsometry Details",
    )

    elli_img_data_optimisation = PropertyTypeAssignment(
        code="ELLI_IMG_DATA_OPTIMISATION",
        data_type="MULTILINE_VARCHAR",
        property_label="Data optimisation",
        description=(
            "Data preprocessing or optimisation applied, e.g. cropping or image alignment"
            "//Angewandte Datenvorverarbeitung oder -optimierung, z.B. Zuschneiden "
            "oder Bildausrichtung"
        ),
        mandatory=False,
        section="Imaging Ellipsometry Details",
    )
