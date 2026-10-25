from bam_masterdata.metadata.definitions import VocabularyTerm, VocabularyTypeDef
from bam_masterdata.metadata.entities import VocabularyType


# ! The parent class of GmawTorchType is not defined (missing VocabularyType)
class GmawTorchType(VocabularyType):
    defs = VocabularyTypeDef(
        code="WELDING.GMAW_TORCH_TYPE",
        description="""General types of GMAW torches//Arten von MSG-Schweißbrennern""",
    )

    welding_gmaw_torch_type_ngw_rot = VocabularyTerm(
        code="WELDING_GMAW_TORCH_TYPE_NGW_ROT",
        label="narrow gap torch (rotating arc)",
        description="""A generic dual wire tandem torch//generischer Zweidraht-/Tandem-MSG-Brenner""",
    )

    welding_gmaw_torch_type_ngw_swing = VocabularyTerm(
        code="WELDING_GMAW_TORCH_TYPE_NGW_SWING",
        label="narrow gap torch (swing arc)",
        description="""A generic dual wire tandem torch//generischer Zweidraht-/Tandem-MSG-Brenner""",
    )

    welding_gmaw_torch_type_single = VocabularyTerm(
        code="WELDING_GMAW_TORCH_TYPE_SINGLE",
        label="single wire torch",
        description="""Generic GMAW torch with a single wire//generischer Eindraht MSG-Brenner""",
    )

    welding_gmaw_torch_type_tandem = VocabularyTerm(
        code="WELDING_GMAW_TORCH_TYPE_TANDEM",
        label="tandem torch",
        description="""A generic dual wire tandem torch//generischer Zweidraht-/Tandem-MSG-Brenner""",
    )


# ! The parent class of WeldType is not defined (missing VocabularyType)
class WeldType(VocabularyType):
    defs = VocabularyTypeDef(
        code="WELDING.WELD_TYPE",
        description="""Types of welds//Arten von Schweißverbindungen""",
    )

    welding_fillet_weld = VocabularyTerm(
        code="WELDING_FILLET_WELD",
        label="fillet weld",
        description="""A weld of approximately triangular cross section joining two surfaces approximately at right angles to each other in a lap joint, T-joint, or corner joint.//Kehlnahtschweißung mit näherungsweise dreieckiger Schweißnahtgeometrie.""",
    )

    welding_groove_weld = VocabularyTerm(
        code="WELDING_GROOVE_WELD",
        label="groove weld",
        description="""A weld in a weld groove on a workpiece surface, between workpiece edges, between workpiece surfaces, or between workpiece edges and surfaces.//Fugennahtschweißung auf oder zwischen Werkstückoberflächen, -ecken""",
    )

    welding_plug_weld = VocabularyTerm(
        code="WELDING_PLUG_WELD",
        label="plug weld",
        description="""A weld made in a circular hole in one member of a joint fusing that member to another member. A fillet-welded hole is not to be construed as conforming to this definition.//Lochschweißung zur Verbindung paralleler oder überlappender Werkstücke""",
    )

    welding_spot_weld = VocabularyTerm(
        code="WELDING_SPOT_WELD",
        label="spot weld",
        description="""A  weld made by arc spot or resistance spot welding//durch Punktschweißen hergestellte Verbindung""",
    )

    welding_surfacing_weld = VocabularyTerm(
        code="WELDING_SURFACING_WELD",
        label="surfacing weld",
        description="""A weld applied to a surface, as opposed to making a joint, to obtain desired properties or dimensions.//Auftragsschweißung zur Strukturbildung oder Beschichtung""",
    )

    welding_tack_weld = VocabularyTerm(
        code="WELDING_TACK_WELD",
        label="tack weld",
        description="""Used to hold the parts of a weldment in proper alignment are placed in grooves or fillet locations and are small enough to be consumed by the production weld.//Heftnaht zur Positionierung von Bauteilen""",
    )
