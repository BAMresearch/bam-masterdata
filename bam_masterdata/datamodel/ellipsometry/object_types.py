from bam_masterdata.datamodel.activities import ExperimentalStep
from bam_masterdata.datamodel.instruments import Instrument
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment


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


class Ellipsometry(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.ELLIPSOMETRY",
        description="""Ellipsometry//Ellipsometrie""",
        generated_code_prefix="EXP.ELLIPS",
    )

    elli_spectral_low = PropertyTypeAssignment(
        code="ELLI_SPECTRAL_LOW",
        data_type="INTEGER",
        property_label="Spectral range low",
        units="...",
        description="""Spectral range low end//Spektralbereich Anfang""",
        mandatory=False,
        section="Ellipsometry Details",
    )

    elli_spectral_high = PropertyTypeAssignment(
        code="ELLI_SPECTRAL_HIGH",
        data_type="INTEGER",
        property_label="Spectral range high",
        units="...",
        description="""Spectral range high end//Spektralbereich Ende""",
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
        property_label="Ellipsometric Quantity type",
        description="""Ellipsometric quantity type//Typ der ellipsometrischen Parameter (MM, PD, Sx, NCS,…)""",
        mandatory=False,
        section="Ellipsometry Details",
    )

    elli_aoi_low = PropertyTypeAssignment(
        code="ELLI_AOI_LOW",
        data_type="INTEGER",
        property_label="Lowest Angle of Incidence (deg)",
        description="""Lowest Angle of Incidence (deg)//Kleinster AOI z.B. 55°""",
        mandatory=False,
        section="Ellipsometry Details",
    )

    elli_aoi_high = PropertyTypeAssignment(
        code="ELLI_AOI_HIGH",
        data_type="INTEGER",
        property_label="Highest Angle of Incidence (deg)",
        description="""Highest Angle of Incidence (deg)//Höchster AOI z.B. 75°""",
        mandatory=False,
        section="Ellipsometry Details",
    )

    elli_n_aoi = PropertyTypeAssignment(
        code="ELLI_N_AOI",
        data_type="INTEGER",
        property_label="Number of Angles of Incidence",
        description="""Number of AOI, e.g. 3//Anzahl AOI, z.B. 3""",
        mandatory=False,
        section="Ellipsometry Details",
    )

    elli_focusing = PropertyTypeAssignment(
        code="ELLI_FOCUSING",
        data_type="BOOLEAN",
        property_label="Focusing optics used?",
        description="""Measurement done with focussing optics?""",
        mandatory=False,
        section="Ellipsometry Details",
    )

    elli_accessory = PropertyTypeAssignment(
        code="ELLI_ACCESSORY",
        data_type="MULTILINE_VARCHAR",
        property_label="Accessory used",
        description="""Other accessory used (e.g. liquid cell, EC cell)""",
        mandatory=False,
        section="Ellipsometry Details",
    )


class EllipsometryTemperature(Ellipsometry):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.ELLIPSOMETRY_TEMP",
        description=(
            "Ellipsometry with temperature control or other in situ experiment"
            "//Ellipsometrie mit Temperaturregelung oder sonstigem in situ Experiment"
        ),
        generated_code_prefix="EXP.ELLIPS.T",
    )

    elli_temp_heating = PropertyTypeAssignment(
        code="ELLI_TEMP_HEATING",
        data_type="BOOLEAN",
        property_label="Heating used",
        description=(
            "Heating used during the experiment//Heizung während der Messung verwendet"
        ),
        mandatory=True,
        section="Ellipsometry Temperature Details",
    )

    elli_temp_cooling = PropertyTypeAssignment(
        code="ELLI_TEMP_COOLING",
        data_type="BOOLEAN",
        property_label="LN2 cooling used",
        description=(
            "LN2 cooling used during the experiment"
            "//LN2-Kühlung während der Messung verwendet"
        ),
        mandatory=True,
        section="Ellipsometry Temperature Details",
    )

    elli_temp_variable = PropertyTypeAssignment(
        code="ELLI_TEMP_VARIABLE",
        data_type="BOOLEAN",
        property_label="Variable temperature",
        description=(
            "Temperature varies during the measurement"
            "//Temperatur variiert während der Messung"
        ),
        mandatory=True,
        section="Ellipsometry Temperature Details",
    )

    elli_temp_constant = PropertyTypeAssignment(
        code="ELLI_TEMP_T_CONST",
        data_type="FLOAT",
        property_label="Constant temperature",
        units="K",
        description=(
            "Temperature during the measurement when kept constant"
            "//Temperatur während der Messung, falls konstant"
        ),
        mandatory=False,
        section="Ellipsometry Temperature Details",
    )

    elli_temp_control_low = PropertyTypeAssignment(
        code="ELLI_TEMP_CONTROL_T_LOW",
        data_type="FLOAT",
        property_label="Lowest controlled temperature",
        units="K",
        description=(
            "Lowest temperature reached during temperature control"
            "//Niedrigste Temperatur während der Temperaturregelung"
        ),
        mandatory=False,
        section="Ellipsometry Temperature Details",
    )

    elli_temp_control_high = PropertyTypeAssignment(
        code="ELLI_TEMP_CONTROL_T_HIGH",
        data_type="FLOAT",
        property_label="Highest controlled temperature",
        units="K",
        description=(
            "Highest temperature reached during temperature control"
            "//Höchste Temperatur während der Temperaturregelung"
        ),
        mandatory=False,
        section="Ellipsometry Temperature Details",
    )

    elli_temp_heating_rate = PropertyTypeAssignment(
        code="ELLI_TEMP_CONTROL_R_HEAT",
        data_type="FLOAT",
        property_label="Maximum heating rate",
        units="K/min",
        description=("Maximum heating ramp rate//Maximale Heizrate"),
        mandatory=False,
        section="Ellipsometry Temperature Details",
    )

    elli_temp_cooling_rate = PropertyTypeAssignment(
        code="ELLI_TEMP_CONTROL_R_COOL",
        data_type="FLOAT",
        property_label="Maximum cooling rate",
        units="K/min",
        description=("Maximum cooling ramp rate//Maximale Abkühlrate"),
        mandatory=False,
        section="Ellipsometry Temperature Details",
    )

    elli_temp_in_situ = PropertyTypeAssignment(
        code="ELLI_TEMP_INSITU",
        data_type="BOOLEAN",
        property_label="Other in situ experiment",
        description=(
            "Whether an in situ experiment other than temperature control was performed"
            "//Ob ein anderes in situ Experiment als Temperaturregelung durchgeführt wurde"
        ),
        mandatory=True,
        section="Ellipsometry Temperature Details",
    )

    elli_temp_in_situ_description = PropertyTypeAssignment(
        code="ELLI_TEMP_INSITU_DESCR",
        data_type="MULTILINE_VARCHAR",
        property_label="In situ experiment description",
        description=(
            "Description of the in situ experiment, e.g. gas adsorption, "
            "electrochemistry, or porosimetry"
            "//Beschreibung des in situ Experiments, z.B. Gasadsorption, "
            "Elektrochemie oder Porosimetrie"
        ),
        mandatory=False,
        section="Ellipsometry Temperature Details",
    )

    elli_temp_in_situ_duration = PropertyTypeAssignment(
        code="ELLI_TEMP_INSITU_TIME",
        data_type="FLOAT",
        property_label="Experiment duration",
        units="s",
        description=(
            "Total duration of the temperature-controlled or in situ experiment"
            "//Gesamtdauer des temperaturgeregelten oder in situ Experiments"
        ),
        mandatory=False,
        section="Ellipsometry Temperature Details",
    )

    elli_temp_in_situ_n_measurements = PropertyTypeAssignment(
        code="ELLI_TEMP_INSITU_N_MEAS",
        data_type="INTEGER",
        property_label="Number of measurements",
        description=(
            "Number of individual measurements or time slices during the "
            "temperature-controlled or in situ experiment"
            "//Anzahl der Einzelmessungen oder Zeitschritte während des "
            "temperaturgeregelten oder in situ Experiments"
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

    elli_mapping = PropertyTypeAssignment(
        code="ELLI_MAPPING",
        data_type="BOOLEAN",
        property_label="Mapping performed",
        description=(
            "Whether an ellipsometric mapping was performed"
            "//Ob ein ellipsometrisches Mapping durchgeführt wurde"
        ),
        mandatory=False,
        section="Ellipsometry Mapping Details",
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
            "Size of the mapped area as x × y dimensions or diameter, including units"
            "//Größe des gemappten Bereichs als x × y Abmessungen oder Durchmesser, "
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
        property_label="Dataset type",
        description=(
            "Type of imaging ellipsometry dataset, e.g. ROI spectra, "
            "pixel shot, or ellipsometric map"
            "//Typ des bildgebenden Ellipsometrie-Datensatzes, z.B. ROI-Spektren, "
            "Pixelshot oder ellipsometrisches Mapping"
        ),
        mandatory=True,
        section="Imaging Ellipsometry Details",
    )

    elli_img_n_pixels_x = PropertyTypeAssignment(
        code="ELLI_IMG_N_PIXELS_X",
        data_type="INTEGER",
        property_label="Number of pixels in x direction",
        description=(
            "Number of image pixels in x direction//Anzahl der Bildpixel in x-Richtung"
        ),
        mandatory=False,
        section="Imaging Ellipsometry Details",
    )

    elli_img_n_pixels_y = PropertyTypeAssignment(
        code="ELLI_IMG_N_PIXELS_Y",
        data_type="INTEGER",
        property_label="Number of pixels in y direction",
        description=(
            "Number of image pixels in y direction//Anzahl der Bildpixel in y-Richtung"
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
        property_label="Focus scanning used",
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
        property_label="Multiple measurements or stitching used",
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
