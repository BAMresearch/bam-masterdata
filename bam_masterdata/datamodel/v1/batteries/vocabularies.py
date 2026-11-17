"""Planar geometry terms; electrode roles are relationships, not intrinsic classes."""

from bam_masterdata.metadata.definitions import VocabularyTerm, VocabularyTypeDef
from bam_masterdata.metadata.entities import VocabularyType


class PlanarShape(VocabularyType):
    defs = VocabularyTypeDef(
        code="PLANAR_SHAPE",
        description="Planar shapes supported by the battery archive mapping.",
    )
    circle = VocabularyTerm(
        code="CIRCLE", label="Circle", description="Circular planar geometry."
    )
    rectangle = VocabularyTerm(
        code="RECTANGLE", label="Rectangle", description="Rectangular planar geometry."
    )
