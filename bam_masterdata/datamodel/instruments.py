from bam_masterdata.datamodel.object_types import Instrument
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
        data_type="INTEGER",
        property_label="Low end of spectral range",
        description="""Low end of spectral range//Spektralbereich kleinste Zahl""",
        mandatory=False,
        section="Ellipsometer Information",
    )

    elli_spectral_range_upper = PropertyTypeAssignment(
        code="ELLI_SPECTRAL_RANGE_UPPER",
        data_type="INTEGER",
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
        data_type="INTEGER",
        property_label="Low end of angle of incidence (AOI) range",
        units="degrees",
        description="""Low end of angle of incidence (AOI) range//AOI Bereich kleinste Zahl""",
        mandatory=False,
        section="Ellipsometer Information",
    )

    elli_aoi_range_upper = PropertyTypeAssignment(
        code="ELLI_AOI_RANGE_UPPER",
        data_type="INTEGER",
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
