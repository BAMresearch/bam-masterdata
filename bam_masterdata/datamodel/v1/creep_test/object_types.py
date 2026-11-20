# AUTO-GENERATED CLASS HIERARCHY — DO NOT EDIT
#
# Sample
# └── CreepTestPiece
#
# END AUTO-GENERATED CLASS HIERARCHY

from bam_masterdata.datamodel.v1.entities import Sample
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment


class CreepTestPiece(Sample):
    defs = ObjectTypeDef(
        code="CREEP_TEST_PIECE",
        description="	A CreepTestPiece is a sample prepared or selected for testing its time-dependent "
        "deformation under sustained loading.",
        generated_code_prefix="CREEP_TEST_PIE",
        prev_versions=["SAMPLE.CREEP_TEST_TEST_PIECE:v0"],
    )

    workshop_order_id = PropertyTypeAssignment(
        code="WORKSHOP_ORDER_ID",
        data_type="VARCHAR",
        property_label="Workshop order ID",
        description="""Workshop/Order identifier""",
        mandatory=False,
        section="Test piece",
        prev_versions=["WORKSHOP_ORDER_ID:v0"],
    )

    creep_test_piece_history = PropertyTypeAssignment(
        code="CREEP_TEST_PIECE_HISTORY",
        data_type="VARCHAR",
        property_label="Test piece history",
        description="Test piece history - Link to file, preferably with machine-readable (meta)data. "
        "The file(s) can include, e.g., data or documentation from previous experiments.",
        mandatory=False,
        section="Test piece",
        prev_versions=["CREEP_TEST_TEST_PIECE_HISTORY:v0"],
    )

    creep_test_piece_type_i = PropertyTypeAssignment(
        code="CREEP_TEST_PIECE_TYPE_I",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_PIECE_TYPE_I",
        property_label="Test piece type I",
        description="""Test piece type I""",
        mandatory=True,
        section="Test piece",
        prev_versions=["CREEP_TEST_TEST_PIECE_TYPE_I:v0"],
    )

    creep_test_piece_type_ii = PropertyTypeAssignment(
        code="CREEP_TEST_PIECE_TYPE_II",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_PIECE_TYPE_II",
        property_label="Test piece type II",
        description="""Test piece type II""",
        mandatory=True,
        section="Test piece",
        prev_versions=["CREEP_TEST_TEST_PIECE_TYPE_II:v0"],
    )

    creep_test_piece_type_iii = PropertyTypeAssignment(
        code="CREEP_TEST_PIECE_TYPE_III",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CREEP_TEST_PIECE_TYPE_III",
        property_label="Test piece type III",
        description="""Test piece type III""",
        mandatory=True,
        section="Test piece",
        prev_versions=["CREEP_TEST_TEST_PIECE_TYPE_III:v0"],
    )

    creep_test_piece_technical_drawing = PropertyTypeAssignment(
        code="CREEP_TEST_PIECE_TECHNICAL_DRAWING",
        data_type="MULTILINE_VARCHAR",
        property_label="Test piece technical drawing",
        description="Test piece technical drawing - Link to file, preferably with machine-readable (meta)data.",
        mandatory=True,
        section="Test piece",
        prev_versions=["CREEP_TEST_TEST_PIECE_TECHNICAL_DRAWING:v0"],
    )

    creep_test_piece_origin_and_orientation = PropertyTypeAssignment(
        code="CREEP_TEST_PIECE_ORIGIN_AND_ORIENTATION",
        data_type="MULTILINE_VARCHAR",
        property_label="Test piece origin and orientation",
        description="Test piece origin and orientation - Describe the exact location / positioning of the "
        "test piece within the as-tested material. E.g.: Do rolling direction and the longitudinal axis coincide?. "
        "Is the test piece located on top or bottom. Do coordinate systems of as-tested material and test piece coincide?. "
        "Add a link to a file, e.g., a technical drawing showing this, preferably with machine-readable (meta)data.",
        mandatory=True,
        section="Test piece",
        prev_versions=["CREEP_TEST_TEST_PIECE_ORIGIN_AND_ORIENTATION:v0"],
    )

    creep_test_piece_orientation_in_test_machine = PropertyTypeAssignment(
        code="CREEP_TEST_PIECE_ORIENTATION_IN_TEST_MACHINE",
        data_type="MULTILINE_VARCHAR",
        property_label="Test piece orientation in test machine",
        description="Test piece orientation in test machine - Describe the exact orientation of the test piece "
        "within the test machine. E.g., is the longitudinal axis of the test piece exactly parallel to the "
        "loading axis of the test machine?. Add a link to a file providing evidence, preferably with machine-readable "
        "(meta)data. This can be, e.g., a technical drawing. // Orientierung des Probekörpers in der Prüfmaschine - "
        "Describe the exact orientation of the test piece within the test machine. E.g., is the longitudinal axis of "
        "the test piece exactly parallel to the loading axis of the test machine?. Add a link to a file providing "
        "evidence, preferably with machine-readable (meta)data. This can be, e.g., a technical drawing.",
        mandatory=True,
        section="Test piece",
        prev_versions=["CREEP_TEST_TEST_PIECE_ORIENTATION_IN_TEST_MACHINE:v0"],
    )

    additional_information = PropertyTypeAssignment(
        code="ADDITIONAL_INFORMATION",
        data_type="MULTILINE_VARCHAR",
        property_label="Additional information test piece",
        description="Additional information test piece - Add the information or a link to file, preferably "
        "with machine-readable (meta)data, e.g., Roughness.",
        mandatory=False,
        section="Test piece",
        prev_versions=["CREEP_TEST_ADDITIONAL_INFORMATION_TEST_PIECE:v0"],
    )

    # CREEP_TEST_TEST_PIECE_ID:v0 maps to SAMPLE_ID
