# AUTO-GENERATED CLASS HIERARCHY — DO NOT EDIT
#
# Sample*
# ├── BuildingMaterialsSpecimen
# └── ConcreteMixture
#
# END AUTO-GENERATED CLASS HIERARCHY

from bam_masterdata.datamodel.v1.entities import Sample
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment


class BuildingMaterialsSample(Sample):
    defs = ObjectTypeDef(
        code="BUILDING_MATERIALS_SAMPLE",
        description="A BuildingMaterialsSample is a sample of building material prepared or "
        "selected for characterization or testing.",
        generated_code_prefix="BUILD_MAT_SAM",
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

    # ! note that SAMPLE_DIMENSIONS_SET_POINTS (defined as '100 mm x 100 mm x 100 mm') is the same as TEST_OBJ_LENGTH x TEST_OBJ_WIDTH TEST_OBJ_HEIGHT
    sample_length_mm = PropertyTypeAssignment(
        code="SAMPLE_LENGTH_MM",
        data_type="REAL",
        property_label="Sample length",
        units="mm",
        description="Length of the sample.",
        mandatory=False,
        section="Dimensions",
        prev_versions=["SAMPLE_DIMENSIONS_SET_POINTS:v0"],
    )

    sample_width_mm = PropertyTypeAssignment(
        code="SAMPLE_WIDTH_MM",
        data_type="REAL",
        property_label="Sample width",
        units="mm",
        description="Width of the sample.",
        mandatory=False,
        section="Dimensions",
        prev_versions=["SAMPLE_DIMENSIONS_SET_POINTS:v0"],
    )

    sample_height_mm = PropertyTypeAssignment(
        code="SAMPLE_HEIGHT_MM",
        data_type="REAL",
        property_label="Sample height",
        units="mm",
        description="Height of the sample.",
        mandatory=False,
        section="Dimensions",
        prev_versions=["SAMPLE_DIMENSIONS_SET_POINTS:v0"],
    )

    sample_density_kgm3 = PropertyTypeAssignment(
        code="SAMPLE_DENSITY_KGM3",
        data_type="REAL",
        property_label="Sample density",
        units="kg/m^3",
        description="Density of the sample.",
        mandatory=False,
        section="Dimensions",
        prev_versions=["DENSITY_KG_PER_CUBIC_METER:v0"],
    )

    sample_weight_kg = PropertyTypeAssignment(
        code="SAMPLE_WEIGHT_KG",
        data_type="REAL",
        property_label="Sample weight",
        units="kg",
        description="Weight of the sample.",
        mandatory=False,
        section="Dimensions",
    )

    building_material_type = PropertyTypeAssignment(
        code="BUILDING_MATERIAL_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BUILDING_MATERIAL_TYPE",
        property_label="Building material type",
        description="General category of building material from which the sample consists, such as mineral, "
        "bituminous, plastic, or wood-based material.",
        mandatory=True,
        section="Building Materials Sample Details",
        prev_versions=["BUILDING_MATERIAL_TYPE:v0"],
    )

    building_material_test_standard = PropertyTypeAssignment(
        code="BUILDING_MATERIAL_TEST_STANDARD",
        data_type="VARCHAR",
        property_label="Building material test standard",
        description="Standard, technical specification, or other normative document according to which the "
        "building-material test is performed.",
        mandatory=False,
        section="Building Materials Sample Details",
        prev_versions=["BUILDING_MATERIAL_TEST_STANDARD:v0"],
    )

    building_materials_test_machine = PropertyTypeAssignment(
        code="BUILDING_MATERIALS_TEST_MACHINE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BUILDING_MATERIALS_TEST_MACHINE",
        property_label="Test machine",
        description="Machine or testing system used to perform the building-material test.",
        mandatory=False,
        section="Building Materials Sample Details",
        prev_versions=["BUILDING_MATERIALS_TEST_MACHINE:v0"],
    )

    building_materials_test_id = PropertyTypeAssignment(
        code="BUILDING_MATERIALS_TEST_ID",
        data_type="VARCHAR",
        property_label="Test ID",
        description="Identifier used to uniquely reference the test performed on the sample.",
        mandatory=False,
        section="Building Materials Sample Details",
        prev_versions=["BUILDING_MATERIALS_TEST_ID:v0"],
    )

    building_materials_test_quantity = PropertyTypeAssignment(
        code="BUILDING_MATERIALS_TEST_QUANTITY",
        data_type="VARCHAR",
        property_label="Measured quantity",
        description="Name and unit of the measured quantity from the building-material test.",
        mandatory=False,
        section="Building Materials Sample Details",
        prev_versions=["BUILDING_MATERIALS_TEST_QUANTITY:v0"],
    )

    building_materials_test_result = PropertyTypeAssignment(
        code="BUILDING_MATERIALS_TEST_RESULT",
        data_type="REAL",
        property_label="Measured quantity result",
        description="Result obtained from the building-material test.",
        mandatory=False,
        section="Building Materials Sample Details",
        prev_versions=["BUILDING_MATERIALS_TEST_RESULT:v0"],
    )

    # Properties from v0 not mapped in v1 (from BUILDING_MATERIALS_SPECIMEN:v0)
    # BUILDING_NAME --> $NAME
    # BUILDING_MATERIAL_DETAILS --> DESCRIPTION


class BuildingSample(Sample):
    defs = ObjectTypeDef(
        code="BUILDING_SAMPLE",
        description="A BuildingSample is a building materials sample that ....",
        generated_code_prefix="BUILD_SAM",
        prev_versions=["TEST_OBJECT:v0", "TEST_OBJECT_EXTERNAL:v0"],
    )

    sample_length_mm = PropertyTypeAssignment(
        code="SAMPLE_LENGTH_MM",
        data_type="REAL",
        property_label="Sample length",
        units="mm",
        description="Length of the sample.",
        mandatory=False,
        section="Dimensions",
        prev_versions=["TEST_OBJ_LENGTH:v0"],
    )

    sample_width_mm = PropertyTypeAssignment(
        code="SAMPLE_WIDTH_MM",
        data_type="REAL",
        property_label="Sample width",
        units="mm",
        description="Width of the sample.",
        mandatory=False,
        section="Dimensions",
        prev_versions=["TEST_OBJ_WIDTH:v0"],
    )

    sample_height_mm = PropertyTypeAssignment(
        code="SAMPLE_HEIGHT_MM",
        data_type="REAL",
        property_label="Sample height",
        units="mm",
        description="Height of the sample.",
        mandatory=False,
        section="Dimensions",
        prev_versions=["TEST_OBJ_HEIGHT:v0"],
    )

    sample_density_kgm3 = PropertyTypeAssignment(
        code="SAMPLE_DENSITY_KGM3",
        data_type="REAL",
        property_label="Sample density",
        units="kg/m^3",
        description="Density of the sample.",
        mandatory=False,
        section="Dimensions",
    )

    sample_weight_kg = PropertyTypeAssignment(
        code="SAMPLE_WEIGHT_KG",
        data_type="REAL",
        property_label="Sample weight",
        units="kg",
        description="Weight of the sample.",
        mandatory=False,
        section="Dimensions",
        prev_versions=["TEST_OBJ_EXT_WEIGHT:v0"],
    )

    building_material_type = PropertyTypeAssignment(
        code="BUILDING_MATERIAL_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BUILDING_MATERIAL_TYPE",
        property_label="Building material type",
        description="General category of building material from which the sample consists, such as mineral, "
        "bituminous, plastic, or wood-based material.",
        mandatory=True,
        section="Building Sample Details",
        prev_versions=["TEST_OBJ_MATERIAL:v0"],
    )

    building_year = PropertyTypeAssignment(
        code="BUILDING_YEAR",
        data_type="INTEGER",
        property_label="Building tear",
        description="Year of construction",
        mandatory=False,
        section="Building Sample Details",
        prev_versions=["BUILDING_YEAR:v0"],
    )

    building_number = PropertyTypeAssignment(
        code="BUILDING_NUMBER",
        data_type="VARCHAR",
        property_label="Building number",
        description="Building or structure identifier",
        mandatory=False,
        section="Building Sample Details",
        prev_versions=["BUILDING_NUMBER:v0"],
    )

    location = PropertyTypeAssignment(
        code="LOCATION",
        data_type="OBJECT",
        object_code="LOCATION",
        property_label="Location",
        description="Physical location.",
        mandatory=False,
        section="Building Sample Details",
        prev_versions=["LOCATION:v0", "GIS_COORDINATES:v0"],
    )

    # Properties from v0 not migrated to v1 (from TEST_OBJECT:v0)
    # BAM_OE
    # BAM_ROOM
    # BAM_FLOOR
    # BAM_HOUSE
    # BAM_LOCATION
    # BAM_LOCATION_COMPLETE


class BuildingSampleBAM(BuildingSample):
    defs = ObjectTypeDef(
        code="BUILDING_SAMPLE_BAM",
        description="A BuildingSampleBAM is a building sample that ....",
        generated_code_prefix="BUILD_SAM_BAM",
        prev_versions=["TEST_OBJECT_BAM:v0"],
    )

    old_db_name = PropertyTypeAssignment(
        code="OLD_DB_NAME",
        data_type="VARCHAR",
        property_label="Old database name",
        description="Name in the previous database",
        mandatory=False,
        section="Building Sample Details",
        prev_versions=["OLD_DB_NAME:v0"],
    )

    project_name = PropertyTypeAssignment(
        code="PROJECT_NAME",
        data_type="VARCHAR",
        property_label="Originating project name",
        description="Name of the originating research project",
        mandatory=True,
        section="Building Sample Details",
        prev_versions=["PROJECT_NAME:v0"],
    )

    parfis_project_no = PropertyTypeAssignment(
        code="PARFIS_PROJECT_NO",
        data_type="VARCHAR",
        property_label="PARFIS project number",
        description="PARFIS project number: `VhXXXX`",
        mandatory=False,
        section="Building Sample Details",
        prev_versions=["PROJECT_NAME:v0"],
    )

    funding_grant_no = PropertyTypeAssignment(
        code="FUNDING_GRANT_NO",
        data_type="VARCHAR",
        property_label="Grant number",
        description="Grant number",
        mandatory=False,
        section="Building Sample Details",
        prev_versions=["FUNDING_GRANT_NO:v0"],
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
