from bam_masterdata.metadata.definitions import VocabularyTerm, VocabularyTypeDef
from bam_masterdata.metadata.entities import VocabularyType


class BuildingMaterialType(VocabularyType):
    defs = VocabularyTypeDef(
        code="BUILDING_MATERIAL_TYPE",
        description="""Building Material Type//Baustofftyp""",
    )

    bituminous = VocabularyTerm(
        code="BITUMINOUS",
        label="Bituminous Material",
        description="""Bituminous Material//Bituminöses Material""",
    )

    mineral = VocabularyTerm(
        code="MINERAL",
        label="Mineral Material",
        description="""Mineral Material//Mineralischer Baustoff""",
    )

    plastic = VocabularyTerm(
        code="PLASTIC",
        label="Plastic Material",
        description="""Plastic Material//Kunststoff""",
    )

    wood = VocabularyTerm(
        code="WOOD",
        label="Wood-based Material",
        description="""Wood-based Material//Holzwerkstoff""",
    )


class BuildingMaterialsTestMachine(VocabularyType):
    defs = VocabularyTypeDef(
        code="BUILDING_MATERIALS_TEST_MACHINE",
        description="""Building Materials Test Machine//Baustoffprüfmaschine""",
    )

    tenmn = VocabularyTerm(
        code="10MN",
        label="10 MN",
        description="""10 MN//10 MN""",
    )

    fivemn = VocabularyTerm(
        code="5MN",
        label="5 MN",
        description="""5 MN//5 MN""",
    )

    onemn = VocabularyTerm(
        code="1MN",
        label="1 MN",
        description="""1 MN//1 MN""",
    )

    seidner = VocabularyTerm(
        code="SEIDNER",
        label="Seidner",
        description="""Seidner//Seidner""",
    )

    toni = VocabularyTerm(
        code="TONI",
        label="Toni",
        description="""Toni//Toni""",
    )
