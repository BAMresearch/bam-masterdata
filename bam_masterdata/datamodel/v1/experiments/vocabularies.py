from bam_masterdata.metadata.definitions import VocabularyTerm, VocabularyTypeDef
from bam_masterdata.metadata.entities import VocabularyType


class WeldType(VocabularyType):
    defs = VocabularyTypeDef(
        code="WELD_TYPE",
        description="Types of welds",
        prev_versions=["WELDING.WELD_TYPE:v0"],
    )

    welding_fillet_weld = VocabularyTerm(
        code="WELDING_FILLET_WELD",
        label="fillet weld",
        description="A weld of approximately triangular cross section joining two surfaces approximately at right angles to each other in a lap joint, T-joint, or corner joint.",
    )

    welding_groove_weld = VocabularyTerm(
        code="WELDING_GROOVE_WELD",
        label="groove weld",
        description="A weld in a weld groove on a workpiece surface, between workpiece edges, between workpiece surfaces, or between workpiece edges and surfaces.",
    )

    welding_plug_weld = VocabularyTerm(
        code="WELDING_PLUG_WELD",
        label="plug weld",
        description="A weld made in a circular hole in one member of a joint fusing that member to another member. A fillet-welded hole is not to be construed as conforming to this definition.",
    )

    welding_spot_weld = VocabularyTerm(
        code="WELDING_SPOT_WELD",
        label="spot weld",
        description="A  weld made by arc spot or resistance spot welding",
    )

    welding_surfacing_weld = VocabularyTerm(
        code="WELDING_SURFACING_WELD",
        label="surfacing weld",
        description="A weld applied to a surface, as opposed to making a joint, to obtain desired properties or dimensions.",
    )

    welding_tack_weld = VocabularyTerm(
        code="WELDING_TACK_WELD",
        label="tack weld",
        description="Used to hold the parts of a weldment in proper alignment are placed in grooves or fillet locations and are small enough to be consumed by the production weld.",
    )


class MicroscopyFcgCracklengthType(VocabularyType):
    defs = VocabularyTypeDef(
        code="MICROSCOPY_FCG_CRACKLENGTH_TYPE",
        description="Describes which Cracklength has been measured",
        prev_versions=["MICROSCOPY_FCG_CRACKLENGTH_TYPE:v0"],
    )

    beachmark = VocabularyTerm(
        code="BEACHMARK",
        label="Cracklength corresponding with a beachmark",
        description="Cracklength corresponding with a beachmark",
    )

    final = VocabularyTerm(
        code="FINAL",
        label="Final crack length",
        description="Final crack length",
    )

    notch = VocabularyTerm(
        code="NOTCH",
        label="Notch depth",
        description="Notch depth",
    )


class CameraShutterMode(VocabularyType):
    defs = VocabularyTypeDef(
        code="CAMERA_SHUTTER_MODE",
        description="Shutter modes of digital cameras",
        prev_versions=["CAMERA_SHUTTER_MODE:v0"],
    )

    camera_shutter_global = VocabularyTerm(
        code="CAMERA_SHUTTER_GLOBAL",
        label="global shutter",
        description="Global shutter",
    )

    camera_shutter_rolling = VocabularyTerm(
        code="CAMERA_SHUTTER_ROLLING",
        label="rolling shutter",
        description="Rolling shutter",
    )


class ScatteringModelPSDLD(VocabularyType):
    defs = VocabularyTypeDef(
        code="SCATTERING_MODEL_PSD_LD",
        description="Light scattering model for analyzing laser diffraction data",
        prev_versions=["SCATTERING_MODEL_PSD_LD:v0"],
    )

    mie = VocabularyTerm(
        code="MIE",
        label="Mie scattering",
        description="The Mie model describes the scattering and refraction of light by spherical particles whose size is comparable to the wavelength of light. For particles < 50 µm",
    )

    fraunhofer = VocabularyTerm(
        code="FRAUNHOFER",
        label="Fraunhofer diffraction for particles",
        description="In the context of the laser light scattering method for particle size determination, Fraunhofer scattering refers to a simplified mathematical description of light scattering that is used for relatively large particles (significantly larger than the wavelength of light). For particles > 50 µm",
    )


class MsAcquisitionMode(VocabularyType):
    defs = VocabularyTypeDef(
        code="MS_ACQUISITION_MODE",
        description="Acquisition mode",
        prev_versions=["MS_ACQUISITION_MODE:v0"],
    )

    fullscan = VocabularyTerm(
        code="FULL_SCAN",
        label="Full Scan",
        description="Full Scan",
    )

    ida = VocabularyTerm(
        code="IDA",
        label="IDA",
        description="Information dependent acquisition",
    )

    swath = VocabularyTerm(
        code="SWATH",
        label="SWATH",
        description="SWATH",
    )

    mrm = VocabularyTerm(
        code="MRM",
        label="MRM",
        description="Multiple Reaction Monitoring",
    )

    sim = VocabularyTerm(
        code="SIM",
        label="SIM",
        description="Single Ion Monitoring",
    )


class MsIonPolarity(VocabularyType):
    defs = VocabularyTypeDef(
        code="MS_ION_POLARITY",
        description="Ion polarity",
        prev_versions=["MS_ION_POLARITY:v0"],
    )

    positive = VocabularyTerm(
        code="POSITIVE",
        label="Positive",
        description="Positive Ion",
    )

    negative = VocabularyTerm(
        code="NEGATIVE",
        label="Negative",
        description="Negative Ion",
    )

    positive_negative = VocabularyTerm(
        code="POSITIVENEGATIVE",
        label="Positive/Negative",
        description="Positive and Negative Ions",
    )


class FtirAccessories(VocabularyType):
    defs = VocabularyTypeDef(
        code="FTIR_ACCESSORIES",
        description="FTIR-Accessories",
        prev_versions=["FTIR_ACCESSORIES:v0"],
    )

    ftir_accessory_ge_disc = VocabularyTerm(
        code="FTIR_ACCESSORY_GE_DISC",
        label="Germanium Disc (ATR)",
        description="Germanium Disc (ATR)",
    )

    ftir_accessory_golden_gate = VocabularyTerm(
        code="FTIR_ACCESSORY_GOLDEN_GATE",
        label="Golden Gate, Diamond Window (ATR)",
        description="Golden Gate, Diamond Window (ATR)",
    )

    ftir_accessory_none = VocabularyTerm(
        code="FTIR_ACCESSORY_NONE",
        label="None (Transmission)",
        description="None (Transmission)",
    )

    ftir_accessory_other = VocabularyTerm(
        code="FTIR_ACCESSORY_OTHER",
        label="Other Accessory (please specify in comments)",
        description="Other Accessory (please specify in comments)",
    )


class DcpdPotCal(VocabularyType):
    defs = VocabularyTypeDef(
        code="DCPD_POT_CAL",
        description="DCPD Potential Calibration Options",
        prev_versions=["DCPD_POT_CAL:v0"],
    )

    fem_fit = VocabularyTerm(
        code="FEM_FIT",
        label="Finite Element Fit",
        description="Finite Element Fit",
    )

    johnson = VocabularyTerm(
        code="JOHNSON",
        label="Johnson Formula",
        description="Johnson Formula",
    )


class SIMSPrimaryIon(VocabularyType):
    defs = VocabularyTypeDef(
        code="SIMS_PRIMARY_ION",
        description="Type of Primary Ion",
        prev_versions=["SIMS_PRIMARY_ION:v0"],
    )

    Bi1 = VocabularyTerm(
        code="BI1",
        label="Bi+",
        description="Bi+",
    )

    Bi2 = VocabularyTerm(
        code="BI2",
        label="Bi2+",
        description="Bi2+",
    )

    Bi3 = VocabularyTerm(
        code="BI3",
        label="Bi3+",
        description="Bi3+",
    )

    Bi4 = VocabularyTerm(
        code="BI4",
        label="Bi4+",
        description="Bi4+",
    )

    Bi5 = VocabularyTerm(
        code="BI5",
        label="Bi5+",
        description="Bi5+",
    )

    Bi6 = VocabularyTerm(
        code="BI6",
        label="Bi6+",
        description="Bi6+",
    )

    Bi7 = VocabularyTerm(
        code="BI7",
        label="Bi7+",
        description="Bi7+",
    )

    Bi1pp = VocabularyTerm(
        code="BI1PP",
        label="Bi1++",
        description="Bi1++",
    )

    Bi3pp = VocabularyTerm(
        code="BI3PP",
        label="Bi3++",
        description="Bi3++",
    )

    Bi5pp = VocabularyTerm(
        code="BI5PP",
        label="Bi5++",
        description="Bi5++",
    )

    Bi7pp = VocabularyTerm(
        code="BI7PP",
        label="Bi7++",
        description="Bi7++",
    )


class NmrNuclei(VocabularyType):
    defs = VocabularyTypeDef(
        code="NMR_NUCLEI",
        description="NMR Nuclei",
        prev_versions=["NMR_NUCLEI:v0"],
    )

    nmr_nuc_1h = VocabularyTerm(
        code="NMR_NUC_1H",
        label="1H",
        description="1H",
    )

    nmr_nuc_11b = VocabularyTerm(
        code="NMR_NUC_11B",
        label="11B",
        description="11B",
    )

    nmr_nuc_13c = VocabularyTerm(
        code="NMR_NUC_13C",
        label="13C",
        description="13C",
    )

    nmr_nuc_14n = VocabularyTerm(
        code="NMR_NUC_14N",
        label="14N",
        description="14N",
    )

    nmr_nuc_15n = VocabularyTerm(
        code="NMR_NUC_15N",
        label="15N",
        description="15N",
    )

    nmr_nuc_17o = VocabularyTerm(
        code="NMR_NUC_17O",
        label="17O",
        description="17O",
    )

    nmr_nuc_19f = VocabularyTerm(
        code="NMR_NUC_19F",
        label="19F",
        description="19F",
    )

    nmr_nuc_27al = VocabularyTerm(
        code="NMR_NUC_27AL",
        label="27Al",
        description="27Al",
    )

    nmr_nuc_29si = VocabularyTerm(
        code="NMR_NUC_29SI",
        label="29Si",
        description="29Si",
    )

    nmr_nuc_31p = VocabularyTerm(
        code="NMR_NUC_31P",
        label="31P",
        description="31P",
    )

    nmr_nuc_33s = VocabularyTerm(
        code="NMR_NUC_33S",
        label="33S",
        description="33S",
    )

    nmr_nuc_35cl = VocabularyTerm(
        code="NMR_NUC_35CL",
        label="35Cl",
        description="35Cl",
    )

    nmr_nuc_37cl = VocabularyTerm(
        code="NMR_NUC_37CL",
        label="37Cl",
        description="37Cl",
    )

    nmr_nuc_119sn = VocabularyTerm(
        code="NMR_NUC_119SN",
        label="119Sn",
        description="119Sn",
    )

    nmr_nuc_195pt = VocabularyTerm(
        code="NMR_NUC_195PT",
        label="195Pt",
        description="195Pt",
    )

    nmr_nuc_other = VocabularyTerm(
        code="NMR_NUC_OTHER",
        label="Other Nucleus  (please specify in comments)",
        description="Other Nucleus  (please specify in comments)",
    )


class NmrSolvents(VocabularyType):
    defs = VocabularyTypeDef(
        code="NMR_SOLVENTS",
        description="NMR Solvents",
        prev_versions=["NMR_SOLVENTS:v0"],
    )

    nmr_sol_acetone_d6 = VocabularyTerm(
        code="NMR_SOL_ACETONE_D6",
        label="Acetone-d6",
        description="Deuterated Acetone",
    )

    nmr_sol_c6d5cl = VocabularyTerm(
        code="NMR_SOL_C6D5CL",
        label="C6D6Cl",
        description="Deuterated Chlorobenzene",
    )

    nmr_sol_c6d6 = VocabularyTerm(
        code="NMR_SOL_C6D6",
        label="C6D6",
        description="Deuterated Benzene",
    )

    nmr_sol_cd2cl2 = VocabularyTerm(
        code="NMR_SOL_CD2CL2",
        label="CD2Cl2",
        description="Deuterated Dichloromethane",
    )

    nmr_sol_cd3cn = VocabularyTerm(
        code="NMR_SOL_CD3CN",
        label="CD3CN",
        description="Deuterated Acetonitrile",
    )

    nmr_sol_cd3od = VocabularyTerm(
        code="NMR_SOL_CD3OD",
        label="CD3OD",
        description="Deuterated Methanol",
    )

    nmr_sol_cdcl3 = VocabularyTerm(
        code="NMR_SOL_CDCL3",
        label="CDCl3",
        description="Deuterated Chloroform",
    )

    nmr_sol_d2o = VocabularyTerm(
        code="NMR_SOL_D2O",
        label="D2O",
        description="Deuterium Oxide",
    )

    nmr_sol_dmso_d6 = VocabularyTerm(
        code="NMR_SOL_DMSO_D6",
        label="DMSO-d6",
        description="Deuterated Dimethylsulfoxide",
    )

    nmr_sol_other = VocabularyTerm(
        code="NMR_SOL_OTHER",
        label="Other Solvent (please specify in comments)",
        description="Other Solvent (please specify in comments)",
    )

    nmr_sol_tfe_d3 = VocabularyTerm(
        code="NMR_SOL_TFE_D3",
        label="Trifluoroethanol-d3",
        description="Deuterated Trifluoroethanol",
    )

    nmr_sol_thf_d8 = VocabularyTerm(
        code="NMR_SOL_THF-D8",
        label="THF-d8",
        description="Deuterated Tetrahydrofuran",
    )

    nmr_sol_toluene_d8 = VocabularyTerm(
        code="NMR_SOL_TOLUENE_D8",
        label="Toluene-d8",
        description="Deuterated Toluene",
    )


class NmrExperimentTypes(VocabularyType):
    defs = VocabularyTypeDef(
        code="NMR_EXPERIMENT_TYPES",
        description="NMR Experiments",
        prev_versions=["NMR_EXPERIMENT_TYPES:v0"],
    )

    nmr_exp_cosy = VocabularyTerm(
        code="NMR_EXP_COSY",
        label="COSY (2D)",
        description="COSY (2D)",
    )

    nmr_exp_cp_mas = VocabularyTerm(
        code="NMR_EXP_CP_MAS",
        label="CP/MAS (1D, solid state)",
        description="CP/MAS (1D, solid state)",
    )

    nmr_exp_dept = VocabularyTerm(
        code="NMR_EXP_DEPT",
        label="DEPT (1D)",
        description="DEPT (1D)",
    )

    nmr_exp_hmbc = VocabularyTerm(
        code="NMR_EXP_HMBC",
        label="HMBC (2D)",
        description="HMBC (2D)",
    )

    nmr_exp_hmqc = VocabularyTerm(
        code="NMR_EXP_HMQC",
        label="HMQC (2D)",
        description="HMQC (2D)",
    )

    nmr_exp_hsqc = VocabularyTerm(
        code="NMR_EXP_HSQC",
        label="HSQC (2D)",
        description="HSQC (2D)",
    )

    nmr_exp_ir = VocabularyTerm(
        code="NMR_EXP_IR",
        label="Inversion Recovery (T1 Relaxation)",
        description="Inversion Recovery (T1 Relaxation)",
    )

    nmr_exp_noesy = VocabularyTerm(
        code="NMR_EXP_NOESY",
        label="NOESY (2D)",
        description="NOESY (2D)",
    )

    nmr_exp_other = VocabularyTerm(
        code="NMR_EXP_OTHER",
        label="Other Experiment (please specify in comments)",
        description="Other Experiment (please specify in comments)",
    )

    nmr_exp_roesy = VocabularyTerm(
        code="NMR_EXP_ROESY",
        label="ROESY (2D)",
        description="ROESY (2D)",
    )

    nmr_exp_spin_echo = VocabularyTerm(
        code="NMR_EXP_SPIN_ECHO",
        label="Spin Echo (T2 Relaxation)",
        description="Spin Echo (T2 Relaxation)",
    )

    nmr_exp_standard = VocabularyTerm(
        code="NMR_EXP_STANDARD",
        label="Standard (1D)",
        description="Standard (1D)",
    )

    nmr_exp_tocsy = VocabularyTerm(
        code="NMR_EXP_TOCSY",
        label="TOCSY (2D)",
        description="TOCSY (2D)",
    )
