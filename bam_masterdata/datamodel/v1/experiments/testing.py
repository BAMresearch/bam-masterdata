# AUTO-GENERATED CLASS HIERARCHY — DO NOT EDIT
#
# Test*
# ├── FCGTest
# └── MechanicalTest
#     └── IndentationTest
#         └── NanoIndentationTest
#
# END AUTO-GENERATED CLASS HIERARCHY


from bam_masterdata.datamodel.v1.activities import Test
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment


class FCGTest(Test):
    defs = ObjectTypeDef(
        code="FCG_TEST",
        description="An FCGTest is a test that determines the fatigue crack growth "
        "(FCG) behaviour of a specimen under cyclic loading.",
        generated_code_prefix="FCG_TEST",
        prev_versions=["EXPERIMENTAL_STEP.FCG_TEST:v0"],
    )

    fcg_nominal_r = PropertyTypeAssignment(
        code="FCG_NOMINAL_R",
        data_type="REAL",
        property_label="Test Nominal R-Ratio",
        description="Test Nominal R-Ratio",
        mandatory=True,
        section="Experimental Details FCG",
        prev_versions=["FCG_NOMINAL_R:v0"],
    )

    fcg_thrshld = PropertyTypeAssignment(
        code="FCG_THRSHLD",
        data_type="BOOLEAN",
        property_label="Threshold Determination",
        description="Threshold Stress Intensity Factor Range Determination",
        mandatory=False,
        section="Experimental Details FCG",
        prev_versions=["FCG_THRSHLD:v0"],
    )

    fcg_paris = PropertyTypeAssignment(
        code="FCG_PARIS",
        data_type="BOOLEAN",
        property_label="PARIS Parameters Determination",
        description="PARIS Regime Parameters Determination",
        mandatory=False,
        section="Experimental Details FCG",
        prev_versions=["FCG_PARIS:v0"],
    )

    fcg_cyclic_r = PropertyTypeAssignment(
        code="FCG_CYCLIC_R",
        data_type="BOOLEAN",
        property_label="Cyclic R-Curve",
        description="Cyclic R-Curve Determination",
        mandatory=False,
        section="Experimental Details FCG",
        prev_versions=["FCG_CYCLIC_R:v0"],
    )

    fcg_result_thrshld = PropertyTypeAssignment(
        code="FCG_RESULT_THRSHLD",
        data_type="REAL",
        property_label="Threshold Stress intensity Factor Range",
        description="Threshold Stress Intensity Factor Range",
        mandatory=False,
        section="Experimental Results",
        prev_versions=["FCG_RESULT_THRSHLD:v0"],
    )

    fcg_result_paris_c = PropertyTypeAssignment(
        code="FCG_RESULT_PARIS_C",
        data_type="REAL",
        property_label="PARIS Parameter C",
        description="PARIS Parameter C",
        mandatory=False,
        section="Experimental Results",
        prev_versions=["FCG_RESULT_PARIS_C:v0"],
    )

    fcg_result_paris_m = PropertyTypeAssignment(
        code="FCG_RESULT_PARIS_M",
        data_type="REAL",
        property_label="PARIS Parameter m",
        description="PARIS Parameter m",
        mandatory=False,
        section="Experimental Results",
        prev_versions=["FCG_RESULT_PARIS_M:v0"],
    )

    fcg_result_cyclicr_a = PropertyTypeAssignment(
        code="FCG_RESULT_CYCLICR_A",
        data_type="REAL",
        property_label="Cyclic R-Curve Parameter A",
        description="Cyclic R-Curve Parameter A",
        mandatory=False,
        section="Experimental Results",
        prev_versions=["FCG_RESULT_CYCLICR_A:v0"],
    )

    fcg_result_cyclicr_b = PropertyTypeAssignment(
        code="FCG_RESULT_CYCLICR_B",
        data_type="REAL",
        property_label="Cyclic R-Curve Parameter b",
        description="Cyclic R-Curve Parameter b",
        mandatory=False,
        section="Experimental Results",
        prev_versions=["FCG_RESULT_CYCLICR_B:v0"],
    )


class MechanicalTest(Test):
    defs = ObjectTypeDef(
        code="MECHANICAL_TEST",
        description="A MechanicalTest is a test that determines the response of a "
        "material to applied mechanical loads.",
        generated_code_prefix="MECH_TEST",
        prev_versions=["EXPERIMENTAL_STEP.MECHANICAL_TEST:v0"],
    )


class IndentationTest(MechanicalTest):
    defs = ObjectTypeDef(
        code="INDENTATION_TEST",
        description="An IndentationTest is a mechanical test that determines hardness "
        "or elastic properties by pressing an indenter into the surface of "
        "a material.",
        generated_code_prefix="INDENT_TEST",
    )


class NanoIndentationTest(IndentationTest):
    defs = ObjectTypeDef(
        code="NANOINDENTATION_TEST",
        description="A NanoIndentationTest is an indentation test with loads and "
        "penetration depths small enough to probe material properties at "
        "the nanometre scale.",
        generated_code_prefix="NANOINDENT_TEST",
    )
