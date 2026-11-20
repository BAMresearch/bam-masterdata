# AUTO-GENERATED CLASS HIERARCHY — DO NOT EDIT
#
# Sample
# ├── BuildingMaterialsSpecimen
# └── ConcreteMixture
#
# END AUTO-GENERATED CLASS HIERARCHY

from bam_masterdata.datamodel.v1.entities import Sample
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment


class BuildingMaterialsSpecimen(Sample):
    defs = ObjectTypeDef(
        code="BUILDING_MATERIALS_SPECIMEN",
        description="	A BuildingMaterialsSpecimen is a sample of building material prepared or "
        "selected for characterization or testing.",
        generated_code_prefix="BUI_MAT_SAM",
        prev_versions=["SAMPLE.BUILDING_MATERIALS_SPECIMEN:v0"],
    )

    psp_number = PropertyTypeAssignment(
        code="PSP_NUMBER",
        data_type="VARCHAR",
        property_label="PSP Number",
        description="Identifier or project-specific PSP number associated with the sample.",
        mandatory=False,
        section="Sample Details",
        prev_versions=["PSP_NUMBER:v0"],
    )

    date_of_production = PropertyTypeAssignment(
        code="DATE_OF_PRODUCTION",
        data_type="DATE",
        property_label="Date of production",
        description="Date on which the sample or the material represented by the sample was produced or "
        "prepared.",
        mandatory=False,
        section="Sample Details",
        prev_versions=["DATE_OF_PRODUCTION:v0"],
    )

    sample_age_days = PropertyTypeAssignment(
        code="SAMPLE_AGE_DAYS",
        data_type="INTEGER",
        property_label="Sample age",
        units="days",
        description="Age of the sample in days at the relevant time of characterization or testing.",
        mandatory=False,
        section="Sample Details",
        prev_versions=["SAMPLE_AGE_IN_DAYS:v0"],
    )

    sample_dimensions_set_points = PropertyTypeAssignment(
        code="SAMPLE_DIMENSIONS_SET_POINTS",
        data_type="VARCHAR",
        property_label="Sample dimensions set points",
        description="Nominal or target dimensions of the sample, including all dimensions required "
        "to describe its geometry, for example '100 mm x 100 mm x 100 mm'.",
        mandatory=False,
        section="Sample Details",
        prev_versions=["SAMPLE_DIMENSIONS_SET_POINTS:v0"],
    )

    density_kgm3 = PropertyTypeAssignment(
        code="DENSITY_KGM3",
        data_type="REAL",
        units="kg/m^3",
        property_label="Density",
        description="Density of the sample.",
        mandatory=False,
        section="Sample Details",
        prev_versions=["DENSITY_KG_PER_CUBIC_METER:v0"],
    )

    building_material_type = PropertyTypeAssignment(
        code="BUILDING_MATERIAL_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BUILDING_MATERIAL_TYPE",
        property_label="Building material type",
        description="General category of building material from which the sample consists, such as mineral, "
        "bituminous, plastic, or wood-based material.",
        mandatory=True,
        section="Building Materials Specimen Details",
        prev_versions=["BUILDING_MATERIAL_TYPE:v0"],
    )

    building_material_details = PropertyTypeAssignment(
        code="BUILDING_MATERIAL_DETAILS",
        data_type="MULTILINE_VARCHAR",
        property_label="Building material details",
        description="Additional information describing the building material that is not captured by the "
        "material type, such as composition, grade, product designation, or other relevant characteristics.",
        mandatory=False,
        section="Building Materials Specimen Details",
        prev_versions=["BUILDING_MATERIAL_DETAILS:v0"],
    )

    building_name = PropertyTypeAssignment(
        code="BUILDING_NAME",
        data_type="MULTILINE_VARCHAR",
        property_label="Building name",
        description="Name or designation of the building or structure from which the sample originates, if applicable.",
        mandatory=False,
        section="Building Materials Specimen Details",
        prev_versions=["BUILDING_NAME:v0"],
    )

    building_material_test_standard = PropertyTypeAssignment(
        code="BUILDING_MATERIAL_TEST_STANDARD",
        data_type="VARCHAR",
        property_label="Building material test standard",
        description="Standard, technical specification, or other normative document according to which the "
        "building-material test is performed.",
        mandatory=False,
        section="Building Materials Specimen Details",
        prev_versions=["BUILDING_MATERIAL_TEST_STANDARD:v0"],
    )

    building_materials_test_machine = PropertyTypeAssignment(
        code="BUILDING_MATERIALS_TEST_MACHINE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BUILDING_MATERIALS_TEST_MACHINE",
        property_label="Test machine",
        description="Machine or testing system used to perform the building-material test.",
        mandatory=False,
        section="Building Materials Specimen Details",
        prev_versions=["BUILDING_MATERIALS_TEST_MACHINE:v0"],
    )

    building_materials_test_id = PropertyTypeAssignment(
        code="BUILDING_MATERIALS_TEST_ID",
        data_type="VARCHAR",
        property_label="Test ID",
        description="Identifier used to uniquely reference the test performed on the sample.",
        mandatory=False,
        section="Building Materials Specimen Details",
        prev_versions=["BUILDING_MATERIALS_TEST_ID:v0"],
    )

    building_materials_test_quantity = PropertyTypeAssignment(
        code="BUILDING_MATERIALS_TEST_QUANTITY",
        data_type="VARCHAR",
        property_label="Measured quantity",
        description="Name and unit of the measured quantity from the building-material test.",
        mandatory=True,
        section="Building Materials Specimen Details",
        prev_versions=["BUILDING_MATERIALS_TEST_QUANTITY:v0"],
    )

    building_materials_test_result = PropertyTypeAssignment(
        code="BUILDING_MATERIALS_TEST_RESULT",
        data_type="REAL",
        property_label="Measured quantity result",
        description="Result obtained from the building-material test.",
        mandatory=True,
        section="Building Materials Specimen Details",
        prev_versions=["BUILDING_MATERIALS_TEST_RESULT:v0"],
    )


class ConcreteMixture(Sample):
    defs = ObjectTypeDef(
        code="CONCRETE_MIXTURE",
        description="	A ConcreteMixture is a sample of concrete in its fresh state, identified as a "
        "discrete batch or portion for preparation, characterization, or testing.",
        generated_code_prefix="CON_MIX",
        prev_versions=["SAMPLE.CONCRETE_MIXTURE:v0"],
    )

    binder = PropertyTypeAssignment(
        code="BINDER",
        data_type="MULTILINE_VARCHAR",
        property_label="Binder",
        description="Description of the binder system used in the concrete mixture, including its "
        "constituent binder materials and relevant specifications where known.",
        mandatory=False,
        section="Concrete Information",
        prev_versions=["BINDER:v0"],
    )

    water_to_cement_ratio = PropertyTypeAssignment(
        code="WATER_TO_CEMENT_RATIO",
        data_type="MULTILINE_VARCHAR",
        property_label="Water-to-cement ratio",
        description="Water-to-cement ratio of the concrete mixture, or a description of how the "
        "ratio was determined when it cannot be represented by a single value.",
        mandatory=False,
        section="Concrete Information",
        prev_versions=["WATER_TO_CEMENT_RATIO:v0"],
    )

    consistency = PropertyTypeAssignment(
        code="CONSISTENCY",
        data_type="MULTILINE_VARCHAR",
        property_label="Consistency",
        description="Consistency of the fresh concrete, including the measured value, consistency class, "
        "test method, or other relevant information where available.",
        mandatory=False,
        section="Concrete Information",
        prev_versions=["CONSISTENCY:v0"],
    )

    fresh_concrete_density = PropertyTypeAssignment(
        code="FRESH_CONCRETE_DENSITY",
        data_type="MULTILINE_VARCHAR",
        property_label="Fresh concrete density",
        description="Density of the concrete mixture in its fresh state, including the value and unit or "
        "other relevant measurement information.",
        mandatory=False,
        section="Concrete Information",
        prev_versions=["FRESH_CONCRETE_DENSITY:v0"],
    )

    air_voids_content = PropertyTypeAssignment(
        code="AIR_VOIDS_CONTENT",
        data_type="MULTILINE_VARCHAR",
        property_label="Air voids content",
        description="Air content or air-void content determined for the fresh concrete, including the value, "
        "unit, and measurement method where available.",
        mandatory=False,
        section="Concrete Information",
        prev_versions=["AIR_VOIDS_CONTENT:v0"],
    )

    fresh_concrete_temperature = PropertyTypeAssignment(
        code="FRESH_CONCRETE_TEMPERATURE",
        data_type="MULTILINE_VARCHAR",
        property_label="Fresh concrete temperature",
        description="Temperature of the fresh concrete at the relevant time of preparation, sampling, or testing, "
        "including the value and unit.",
        mandatory=False,
        section="Concrete Information",
        prev_versions=["FRESH_CONCRETE_TEMPERATURE:v0"],
    )

    aggregate = PropertyTypeAssignment(
        code="AGGREGATE",
        data_type="MULTILINE_VARCHAR",
        property_label="Aggregate",
        description="Description of the aggregate or aggregate mixture used in the concrete, including information "
        "such as aggregate type, source, grading, or particle-size fractions where available.",
        mandatory=False,
        section="Concrete Information",
        prev_versions=["AGGREGATE:v0"],
    )

    admixtures = PropertyTypeAssignment(
        code="ADMIXTURES",
        data_type="MULTILINE_VARCHAR",
        property_label="Admixtures",
        description="Description of concrete admixtures added to modify properties of the fresh or hardened "
        "concrete, including type, product, and dosage where available.",
        mandatory=False,
        section="Concrete Information",
        prev_versions=["ADDMIXTURES:v0"],
    )

    additives = PropertyTypeAssignment(
        code="ADDITIVES",
        data_type="MULTILINE_VARCHAR",
        property_label="Additives",
        description="Description of concrete additions used as constituents of the mixture, including type, "
        "material, and quantity where available.",
        mandatory=False,
        section="Concrete Information",
        prev_versions=["ADDITIVES:v0"],
    )
