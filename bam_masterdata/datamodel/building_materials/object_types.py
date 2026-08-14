from bam_masterdata.datamodel.object_types import Sample
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.entities import ObjectType


class BuildingMaterialsSpecimen(Sample):
    defs = ObjectTypeDef(
        code="SAMPLE.BUILDING_MATERIALS_SPECIMENT",
        description="""A generic specimen used for building material tests, such as compressive strength tests.//Ein Standardprüfkörper, der für Baustoffprüfungen, wie beispielsweise Druckfestigkeitsprüfungen, verwendet wird.""",
        generated_code_prefix="SAM.BMS",
    )

    psp_number = PropertyTypeAssignment(
        code="PSP_NUMBER",
        data_type="VARCHAR",
        property_label="PSP Number",
        description="""PSP number//PSP-Nummer""",
        mandatory=False,
        section="Specimen Information",
    )

    building_material_group = (
        PropertyTypeAssignment(  # why not building_material_type??
            code="BUILDING_MATERIAL_GROUP",
            data_type="CONTROLLEDVOCABULARY",
            vocabulary_code="BUILDING_MATERIAL_TYPE",
            property_label="Building material group",
            description="""Building material group//Baustoffmaterialgruppe""",
            mandatory=True,
            section="Specimen Information",
        )
    )

    building_material_details = PropertyTypeAssignment(
        code="BUILDING_MATERIAL_DETAILS",
        data_type="MULTILINE_VARCHAR",
        property_label="Building material details",
        description="""Building material details//Baustoffmaterialdetails""",
        mandatory=False,
        section="Specimen Information",
    )

    date_of_production = PropertyTypeAssignment(
        code="DATE_OF_PRODUCTION",
        data_type="DATE",
        property_label="Date of production",
        description="""Date of production//Herstellungsdatum""",
        mandatory=False,
        section="Specimen Information",
    )

    specimen_age_in_days = PropertyTypeAssignment(
        code="SPECIMEN_AGE_IN_DAYS",
        data_type="INTEGER",
        property_label="Specimen age",
        units="days",
        description="""Specimen age in [days]//Alter des Prüfkörpers in [Tagen]""",
        mandatory=False,
        section="Specimen Information",
    )

    specimen_dimensions_set_points = PropertyTypeAssignment(  # what's this??
        code="SPECIMEN_DIMENSIONS_SET_POINTS",
        data_type="VARCHAR",
        property_label="Specimen dimensions set points",
        description="""Specimen dimensions (set points)//Prüfkörpermaße (Sollwerte)""",
        mandatory=False,
        section="Specimen Information",
    )

    # There are one already defined: DENSITY_GRAM_PER_CUBIC_CM
    # units of this??
    density = PropertyTypeAssignment(
        code="DENSITY",
        data_type="VARCHAR",  # float??
        property_label="Density",
        description="""Density//Rohdichte""",
        mandatory=False,
        section="Specimen Information",
    )

    geometry = PropertyTypeAssignment(  # name it specimen_geometry instead of geometry??
        code="GEOMETRY",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="SPECIMEN_GEOMETRY",
        property_label="Geometry",
        description="""Specimen geometry//Prüfkörpergeometrie""",  # better description??
        mandatory=False,
        section="Specimen Information",
    )

    origin = PropertyTypeAssignment(  # call it specimen_origin instead of origin??
        code="ORIGIN",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="SPECIMEN_ORIGIN",  # not defined!!
        property_label="Origin",
        description="""Specimen origin//Prüfkörperherkunft""",  # better description??
        mandatory=False,
        section="Specimen Information",
    )

    building_name = PropertyTypeAssignment(
        code="BUILDING_NAME",
        data_type="MULTILINE_VARCHAR",  # mmm what's this?
        property_label="Building name",
        description="""Building name//Bauwerksname""",
        mandatory=False,
        section="Specimen Information",
    )

    building_material_test_standard = PropertyTypeAssignment(
        code="BUILDING_MATERIAL_TEST_STANDARD",
        data_type="VARCHAR",  # no CONTROLLEDVOCABULARY for this??
        property_label="Building material test standard",
        description="""Building material test standard//Baustoff-Prüfnorm""",  # better description??
        mandatory=False,
        section="Specimen Information",
    )

    test_machine = PropertyTypeAssignment(  # call it BUILDING_MATERIALS_TEST_MACHINE?
        code="TEST_MACHINE",  # too generic, it should be BUILDING_MATERIALS_TEST_MACHINE
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BUILDING_MATERIALS_TEST_MACHINE",
        property_label="Test machine",
        description="""Test Machine//Prüfmaschine""",  # better description??
        mandatory=False,
        section="Specimen Information",
    )

    test_id = PropertyTypeAssignment(
        code="TEST_ID",
        data_type="VARCHAR",
        property_label="Test ID",
        description="""Test ID//Prüfkennung""",
        mandatory=False,
        section="Specimen Information",
    )

    test_result = PropertyTypeAssignment(
        code="TEST_RESULT",
        data_type="MULTILINE_VARCHAR",
        property_label="Test result",
        description="""Test Result//Prüfergebnis""",
        mandatory=True,
        section="Specimen Information",
    )


class ConcreteMixture(Sample):
    defs = ObjectTypeDef(
        code="SAMPLE.CONCRETE_MIXTURE",
        description="""Concrete mixture used for building material tests, such as compressive strength tests.//Betonmischung für Baustoffprüfungen, wie beispielsweise Druckfestigkeitsprüfungen.""",
        generated_code_prefix="SAM.CON_MIX",
    )

    # all of these are MULTILINE_VARCHAR, wtf?

    binder = PropertyTypeAssignment(
        code="BINDER",
        data_type="MULTILINE_VARCHAR",
        property_label="Binder",
        description="""Binder//Bindemittel""",
        mandatory=False,
        section="Concrete Information",
    )

    # units?
    water_to_cement_ratio = PropertyTypeAssignment(
        code="WATER_TO_CEMENT_RATIO",
        data_type="MULTILINE_VARCHAR",
        property_label="Water-to-cement ratio",
        description="""Water-to-cement ratio//Wasser-Zement-Verhältnis""",
        mandatory=False,
        section="Concrete Information",
    )

    consistency = PropertyTypeAssignment(
        code="CONSISTENCY",
        data_type="MULTILINE_VARCHAR",
        property_label="Consistency",
        description="""Consistency//Konsistenz""",
        mandatory=False,
        section="Concrete Information",
    )

    # units?
    fresh_concrete_density = PropertyTypeAssignment(
        code="FRESH_CONCRETE_DENSITY",
        data_type="MULTILINE_VARCHAR",
        property_label="Fresh concrete density",
        description="""Fresh concrete density//Frischer Betondichte""",
        mandatory=False,
        section="Concrete Information",
    )

    air_voids_content = PropertyTypeAssignment(
        code="AIR_VOIDS_CONTENT",
        data_type="MULTILINE_VARCHAR",
        property_label="Air voids content",
        description="""Air voids content//Lufthohlräume""",
        mandatory=False,
        section="Concrete Information",
    )

    # units?
    fresh_concrete_temperature = PropertyTypeAssignment(
        code="FRESH_CONCRETE_TEMPERATURE",
        data_type="MULTILINE_VARCHAR",
        property_label="Fresh concrete temperature",
        description="""Fresh concrete temperature//Frischer Betontemperatur""",
        mandatory=False,
        section="Concrete Information",
    )

    aggregate = PropertyTypeAssignment(
        code="AGGREGATE",
        data_type="MULTILINE_VARCHAR",
        property_label="Aggregate",
        description="""Aggregate//Aggregat""",
        mandatory=False,
        section="Concrete Information",
    )

    admixtures = PropertyTypeAssignment(
        code="ADDMIXTURES",
        data_type="MULTILINE_VARCHAR",
        property_label="Admixtures",
        description="""Admixtures//Zusatzstoffe""",
        mandatory=False,
        section="Concrete Information",
    )

    additives = PropertyTypeAssignment(
        code="ADDITIVES",
        data_type="MULTILINE_VARCHAR",
        property_label="Additives",
        description="""Additives//Zusatzstoffe""",
        mandatory=False,
        section="Concrete Information",
    )
