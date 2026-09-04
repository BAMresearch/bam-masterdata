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

    concrete = VocabularyTerm(
        code="CONCRETE",
        label="Concrete Material",
        description="""Concrete Material//Beton""",
    )

    clay = VocabularyTerm(
        code="CLAY",
        label="Clay Material",
        description="""Clay Material//Lehmbaustoff""",
    )

    natural_stone = VocabularyTerm(
        code="NATURAL_STONE",
        label="Natural Stone Material",
        description="""Natural Stone Material//Naturstein""",
    )

    other = VocabularyTerm(
        code="OTHER",
        label="Other Material Types",
        description="""Other Material Types//Anderer Materialtyp""",
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
