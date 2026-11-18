from bam_masterdata.metadata.definitions import VocabularyTerm, VocabularyTypeDef
from bam_masterdata.metadata.entities import VocabularyType


class CreepTestPieceTypeI(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_PIECE_TYPE_I",
        description="""Test Piece Type I (Metadata, Test piece)""",
    )

    miniaturized_specimen = VocabularyTerm(
        code="MINIATURIZED_SPECIMEN",
        label="Miniaturized specimen",
        description="""Miniaturized specimen""",
    )

    specimen_according_to_standard = VocabularyTerm(
        code="SPECIMEN_ACCORDING_TO_STANDARD",
        label="Specimen according to standard",
        description="""Specimen according to standard""",
    )


class CreepTestPieceTypeII(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_PIECE_TYPE_II",
        description="""Test Piece Type II (Metadata, Test piece)""",
    )

    round_cross_section = VocabularyTerm(
        code="ROUND_CROSS_SECTION",
        label="Round cross section",
        description="""Round cross section""",
    )

    rectangular_section = VocabularyTerm(
        code="RECTANGULAR_SECTION",
        label="Rectangular section",
        description="""Rectangular section""",
    )


class CreepTestPieceTypeIII(VocabularyType):
    defs = VocabularyTypeDef(
        code="CREEP_TEST_PIECE_TYPE_III",
        description="""Test Piece Type III (Metadata, Test piece)""",
    )

    smooth_test_piece = VocabularyTerm(
        code="SMOOTH_TEST_PIECE",
        label="Smooth test piece",
        description="""Smooth test piece""",
    )

    notched_test_piece = VocabularyTerm(
        code="NOTCHED_TEST_PIECE",
        label="Notched test piece",
        description="""Notched test piece""",
    )

    combined_test_piece = VocabularyTerm(
        code="COMBINED_TEST_PIECE",
        label="Combined test piece",
        description="""Combined test piece""",
    )

    other_type_specify = VocabularyTerm(
        code="OTHER_TYPE_SPECIFY",
        label="Other type (specify)",
        description="""Other type (specify)""",
    )
