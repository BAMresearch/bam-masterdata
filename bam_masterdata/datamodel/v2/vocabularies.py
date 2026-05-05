from bam_masterdata.metadata.definitions import VocabularyTerm, VocabularyTypeDef
from bam_masterdata.metadata.entities import VocabularyType


class ActivityStatus(VocabularyType):
    defs = VocabularyTypeDef(
        code="ACTIVITY_STATUS",
        description="""Current status of the activity: PLANNED, RUNNING, COMPLETED, CANCELLED.""",
    )

    planned = VocabularyTerm(
        code="PLANNED",
        label="Planned",
        description="""The activity is planned but has not yet started.""",
    )

    running = VocabularyTerm(
        code="RUNNING",
        label="Running",
        description="""The activity is currently running.""",
    )

    completed = VocabularyTerm(
        code="COMPLETED",
        label="Completed",
        description="""The activity has been completed.""",
    )

    cancelled = VocabularyTerm(
        code="CANCELLED",
        label="Cancelled",
        description="""The activity has been cancelled and will not be completed.""",
    )


class DcpdPotDropCalibration(VocabularyType):
    defs = VocabularyTypeDef(
        code="DCPD_POT_DROP_CALIBRATION",
        description="""DCPD Potential Drop Calibration Options""",
    )

    fem_fit = VocabularyTerm(
        code="FEM_FIT",
        label="Finite Element Fit",
        description="""Finite Element Fit//Finite Elemente Anpassung""",
    )

    johnson = VocabularyTerm(
        code="JOHNSON",
        label="Johnson Formula",
        description="""Johnson Formula//Johnson Formel""",
    )


class MicroscopyFractureSurfaceType(VocabularyType):
    defs = VocabularyTypeDef(
        code="MICROSCOPY_FRACTURE_SURFACE_TYPE",
        description="""Describes which Cracklength has been measured""",
    )

    beachmark = VocabularyTerm(
        code="BEACHMARK",
        label="Cracklength corresponding with a beachmark",
        description="""Cracklength corresponding with a beachmark//Mit einer Rastlinie korrespondierende Risslänge""",
    )

    final = VocabularyTerm(
        code="FINAL",
        label="Final crack length",
        description="""Final crack length//Finale Risslänge""",
    )

    notch = VocabularyTerm(
        code="NOTCH",
        label="Notch depth",
        description="""Notch depth//Kerbtiefe""",
    )


class FtirAccessories(VocabularyType):
    defs = VocabularyTypeDef(
        code="FTIR_ACCESSORIES",
        description="""FTIR-Accessories//FTIR Zubehör""",
    )

    ftir_accessory_ge_disc = VocabularyTerm(
        code="FTIR_ACCESSORY_GE_DISC",
        label="Germanium Disc (ATR)",
        description="""Germanium Disc (ATR)//Germanium-Scheibe (ATR)""",
    )

    ftir_accessory_golden_gate = VocabularyTerm(
        code="FTIR_ACCESSORY_GOLDEN_GATE",
        label="Golden Gate, Diamond Window (ATR)",
        description="""Golden Gate, Diamond Window (ATR)//Golden Gate, Diamantfenster (ATR)""",
    )

    ftir_accessory_none = VocabularyTerm(
        code="FTIR_ACCESSORY_NONE",
        label="None (Transmission)",
        description="""None (Transmission)//Keine (Transmission)""",
    )

    ftir_accessory_other = VocabularyTerm(
        code="FTIR_ACCESSORY_OTHER",
        label="Other Accessory (please specify in comments)",
        description="""Other Accessory (please specify in comments)//Anderes Zubehör  (bitte im Kommentarfeld vermerken)""",
    )


class CameraShutterMode(VocabularyType):
    defs = VocabularyTypeDef(
        code="CAMERA_SHUTTER_MODE",
        description="""Shutter modes of digital cameras//Belichtungsmodi digitaler Bildsensoren""",
    )

    shutter_global = VocabularyTerm(
        code="SHUTTER_GLOBAL",
        label="global shutter",
        description="""Global shutter//Global shutter""",
    )

    shutter_rolling = VocabularyTerm(
        code="SHUTTER_ROLLING",
        label="rolling shutter",
        description="""Rolling shutter//Rolling shutter""",
    )


class NmrNuclei(VocabularyType):
    defs = VocabularyTypeDef(
        code="NMR_NUCLEI",
        description="""NMR Nuclei//NMR Kerne""",
    )

    nmr_nuc_1h = VocabularyTerm(
        code="NMR_NUC_1H",
        label="1H",
        description="""1H//1H""",
    )

    nmr_nuc_11b = VocabularyTerm(
        code="NMR_NUC_11B",
        label="11B",
        description="""11B//11B""",
    )

    nmr_nuc_13c = VocabularyTerm(
        code="NMR_NUC_13C",
        label="13C",
        description="""13C//13C""",
    )

    nmr_nuc_14n = VocabularyTerm(
        code="NMR_NUC_14N",
        label="14N",
        description="""14N//14N""",
    )

    nmr_nuc_15n = VocabularyTerm(
        code="NMR_NUC_15N",
        label="15N",
        description="""15N//15N""",
    )

    nmr_nuc_17o = VocabularyTerm(
        code="NMR_NUC_17O",
        label="17O",
        description="""17O//17O""",
    )

    nmr_nuc_19f = VocabularyTerm(
        code="NMR_NUC_19F",
        label="19F",
        description="""19F//19F""",
    )

    nmr_nuc_27al = VocabularyTerm(
        code="NMR_NUC_27AL",
        label="27Al",
        description="""27Al//27Al""",
    )

    nmr_nuc_29si = VocabularyTerm(
        code="NMR_NUC_29SI",
        label="29Si",
        description="""29Si//29Si""",
    )

    nmr_nuc_31p = VocabularyTerm(
        code="NMR_NUC_31P",
        label="31P",
        description="""31P//31P""",
    )

    nmr_nuc_33s = VocabularyTerm(
        code="NMR_NUC_33S",
        label="33S",
        description="""33S//33S""",
    )

    nmr_nuc_35cl = VocabularyTerm(
        code="NMR_NUC_35CL",
        label="35Cl",
        description="""35Cl//35Cl""",
    )

    nmr_nuc_37cl = VocabularyTerm(
        code="NMR_NUC_37CL",
        label="37Cl",
        description="""37Cl//37Cl""",
    )

    nmr_nuc_119sn = VocabularyTerm(
        code="NMR_NUC_119SN",
        label="119Sn",
        description="""119Sn//119Sn""",
    )

    nmr_nuc_195pt = VocabularyTerm(
        code="NMR_NUC_195PT",
        label="195Pt",
        description="""195Pt//195Pt""",
    )

    nmr_nuc_other = VocabularyTerm(
        code="NMR_NUC_OTHER",
        label="Other Nucleus  (please specify in comments)",
        description="""Other Nucleus  (please specify in comments)//Anderer Kern (bitte im Kommentarfeld vermerken)""",
    )


class NmrSolvents(VocabularyType):
    defs = VocabularyTypeDef(
        code="NMR_SOLVENTS",
        description="""NMR Solvents//NMR Lösungsmittel""",
    )

    nmr_sol_acetone_d6 = VocabularyTerm(
        code="NMR_SOL_ACETONE_D6",
        label="Acetone-d6",
        description="""Deuterated Acetone//Deuteriertes Aceton""",
    )

    nmr_sol_c6d5cl = VocabularyTerm(
        code="NMR_SOL_C6D5CL",
        label="C6D6Cl",
        description="""Deuterated Chlorobenzene//Deuteriertes Chlorbenzol""",
    )

    nmr_sol_c6d6 = VocabularyTerm(
        code="NMR_SOL_C6D6",
        label="C6D6",
        description="""Deuterated Benzene//Deuteriertes Benzol""",
    )

    nmr_sol_cd2cl2 = VocabularyTerm(
        code="NMR_SOL_CD2CL2",
        label="CD2Cl2",
        description="""Deuterated Dichloromethane//Deuteriertes Dichlormethan""",
    )

    nmr_sol_cd3cn = VocabularyTerm(
        code="NMR_SOL_CD3CN",
        label="CD3CN",
        description="""Deuterated Acetonitrile//Deuteriertes Acetonitril""",
    )

    nmr_sol_cd3od = VocabularyTerm(
        code="NMR_SOL_CD3OD",
        label="CD3OD",
        description="""Deuterated Methanol//Deuteriertes Methanol""",
    )

    nmr_sol_cdcl3 = VocabularyTerm(
        code="NMR_SOL_CDCL3",
        label="CDCl3",
        description="""Deuterated Chloroform//Deuteriertes Chloroform""",
    )

    nmr_sol_d2o = VocabularyTerm(
        code="NMR_SOL_D2O",
        label="D2O",
        description="""Deuterium Oxide//Deuteriumoxid""",
    )

    nmr_sol_dmso_d6 = VocabularyTerm(
        code="NMR_SOL_DMSO_D6",
        label="DMSO-d6",
        description="""Deuterated Dimethylsulfoxide//Deuteriertes Dimethylsulfoxid""",
    )

    nmr_sol_other = VocabularyTerm(
        code="NMR_SOL_OTHER",
        label="Other Solvent (please specify in comments)",
        description="""Other Solvent (please specify in comments)//Anderes Lösungsmittel (bitte im Kommentarfeld vermerken)""",
    )

    nmr_sol_tfe_d3 = VocabularyTerm(
        code="NMR_SOL_TFE_D3",
        label="Trifluoroethanol-d3",
        description="""Deuterated Trifluoroethanol//Deuteriertes Trifluorethanol""",
    )

    nmr_sol_thf_d8 = VocabularyTerm(
        code="NMR_SOL_THF-D8",
        label="THF-d8",
        description="""Deuterated Tetrahydrofuran//Deuteriertes Tetrahydrofuran""",
    )

    nmr_sol_toluene_d8 = VocabularyTerm(
        code="NMR_SOL_TOLUENE_D8",
        label="Toluene-d8",
        description="""Deuterated Toluene//Deuteriertes Toluol""",
    )


class NmrExperimentTypes(VocabularyType):
    defs = VocabularyTypeDef(
        code="NMR_EXPERIMENT_TYPES",
        description="""NMR Experiments//NMR Experimente""",
    )

    nmr_exp_cosy = VocabularyTerm(
        code="NMR_EXP_COSY",
        label="COSY (2D)",
        description="""COSY (2D)//COSY (2D)""",
    )

    nmr_exp_cp_mas = VocabularyTerm(
        code="NMR_EXP_CP_MAS",
        label="CP/MAS (1D, solid state)",
        description="""CP/MAS (1D, solid state)//CP/MAS (1D, solid state)""",
    )

    nmr_exp_dept = VocabularyTerm(
        code="NMR_EXP_DEPT",
        label="DEPT (1D)",
        description="""DEPT (1D)//DEPT (1D)""",
    )

    nmr_exp_hmbc = VocabularyTerm(
        code="NMR_EXP_HMBC",
        label="HMBC (2D)",
        description="""HMBC (2D)//HMBC (2D)""",
    )

    nmr_exp_hmqc = VocabularyTerm(
        code="NMR_EXP_HMQC",
        label="HMQC (2D)",
        description="""HMQC (2D)//HMQC (2D)""",
    )

    nmr_exp_hsqc = VocabularyTerm(
        code="NMR_EXP_HSQC",
        label="HSQC (2D)",
        description="""HSQC (2D)//HSQC (2D)""",
    )

    nmr_exp_ir = VocabularyTerm(
        code="NMR_EXP_IR",
        label="Inversion Recovery (T1 Relaxation)",
        description="""Inversion Recovery (T1 Relaxation)//Inversion Recovery (T1 Relaxation)""",
    )

    nmr_exp_noesy = VocabularyTerm(
        code="NMR_EXP_NOESY",
        label="NOESY (2D)",
        description="""NOESY (2D)//NOESY (2D)""",
    )

    nmr_exp_other = VocabularyTerm(
        code="NMR_EXP_OTHER",
        label="Other Experiment (please specify in comments)",
        description="""Other Experiment (please specify in comments)//Anderes Experiment (bitte im Kommentarfeld vermerken)""",
    )

    nmr_exp_roesy = VocabularyTerm(
        code="NMR_EXP_ROESY",
        label="ROESY (2D)",
        description="""ROESY (2D)//ROESY (2D)""",
    )

    nmr_exp_spin_echo = VocabularyTerm(
        code="NMR_EXP_SPIN_ECHO",
        label="Spin Echo (T2 Relaxation)",
        description="""Spin Echo (T2 Relaxation)//Spin Echo (T2 Relaxation)""",
    )

    nmr_exp_standard = VocabularyTerm(
        code="NMR_EXP_STANDARD",
        label="Standard (1D)",
        description="""Standard (1D)//Standard (1D)""",
    )

    nmr_exp_tocsy = VocabularyTerm(
        code="NMR_EXP_TOCSY",
        label="TOCSY (2D)",
        description="""TOCSY (2D)//TOCSY (2D)""",
    )


class ScatteringModelPSDLD(VocabularyType):
    defs = VocabularyTypeDef(
        code="SCATTERING_MODEL_PSD_LD",
        description="""Light scattering model for analyzing laser diffraction data""",
    )

    mie = VocabularyTerm(
        code="MIE",
        label="Mie scattering",
        description="""The Mie model describes the scattering and refraction of light by spherical particles whose size is comparable to the wavelength of light. For particles < 50 µm // Das Mie-Modell beschreibt die Streuung und Brechung von Licht an kugelförmigen Partikeln, deren Größe vergleichbar mit der Wellenlänge des Lichts ist. Für Partikelgrößen kleiner als 50 µm""",
    )

    fraunhofer = VocabularyTerm(
        code="FRAUNHOFER",
        label="Fraunhofer diffraction for particles",
        description="""In the context of the laser light scattering method for particle size determination, Fraunhofer scattering refers to a simplified mathematical description of light scattering that is used for relatively large particles (significantly larger than the wavelength of light). For particles > 50 µm // Im Kontext des Laserstreulichtverfahrens zur Partikelgrößenbestimmung bezieht sich die Fraunhofer-Brechung auf eine vereinfachte mathematische Beschreibung der Lichtstreuung, die für relativ große Partikel (deutlich größer als die Lichtwellenlänge) verwendet wird. Für Partikelgrößen größer als 50 µm""",
    )


class WeldType(VocabularyType):
    defs = VocabularyTypeDef(
        code="WELD_TYPE",
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
