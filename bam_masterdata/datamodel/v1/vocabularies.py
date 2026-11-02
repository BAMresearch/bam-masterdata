from bam_masterdata.metadata.definitions import VocabularyTerm, VocabularyTypeDef
from bam_masterdata.metadata.entities import VocabularyType


class ActivityStatus(VocabularyType):
    defs = VocabularyTypeDef(
        code="ACTIVITY_STATUS",
        description="Current stage of an activity in its lifecycle",
    )

    planned = VocabularyTerm(
        code="PLANNED",
        label="Planned",
        description="The activity is defined but has not started yet",
    )

    in_progress = VocabularyTerm(
        code="IN_PROGRESS",
        label="In progress",
        description="The activity is currently being carried out",
    )

    on_hold = VocabularyTerm(
        code="ON_HOLD",
        label="On hold",
        description="The activity has started but is temporarily paused",
    )

    completed = VocabularyTerm(
        code="COMPLETED",
        label="Completed",
        description="The activity finished as intended",
    )

    failed = VocabularyTerm(
        code="FAILED",
        label="Failed",
        description="The activity ended before completion because of an error or problem",
    )

    cancelled = VocabularyTerm(
        code="CANCELLED",
        label="Cancelled",
        description="The activity was deliberately stopped before completion",
    )


class XcFunctional(VocabularyType):
    defs = VocabularyTypeDef(
        code="XC_FUNCTIONAL",
        description="Exchange-correlation functional, given by its common name",
        prev_versions=["ATOM_XC_FUNCTIONAL:v0"],
    )

    lda = VocabularyTerm(
        code="LDA",
        label="LDA",
        description="LibXC components: XC_LDA_X, XC_LDA_C_PW",
        prev_versions=["XC_FUNC_LDA:v0"],
    )

    pbe = VocabularyTerm(
        code="PBE",
        label="PBE",
        description="LibXC components: XC_GGA_X_PBE, XC_GGA_C_PBE",
        prev_versions=["XC_FUNC_PBE:v0"],
    )

    pbesol = VocabularyTerm(
        code="PBESOL",
        label="PBEsol",
        description="LibXC components: XC_GGA_X_PBE_SOL, XC_GGA_C_PBE_SOL",
        prev_versions=["XC_FUNC_PBE_SOL:v0"],
    )

    rpbe = VocabularyTerm(
        code="RPBE",
        label="RPBE",
        description="LibXC components: XC_GGA_X_RPBE, XC_GGA_C_PBE",
    )

    revpbe = VocabularyTerm(
        code="REVPBE",
        label="revPBE",
        description="LibXC components: XC_GGA_X_PBE_R, XC_GGA_C_PBE",
    )

    pw91 = VocabularyTerm(
        code="PW91",
        label="PW91",
        description="LibXC components: XC_GGA_X_PW91, XC_GGA_C_PW91",
    )

    am05 = VocabularyTerm(
        code="AM05",
        label="AM05",
        description="LibXC components: XC_GGA_X_AM05, XC_GGA_C_AM05",
    )

    scan = VocabularyTerm(
        code="SCAN",
        label="SCAN",
        description="LibXC components: XC_MGGA_X_SCAN, XC_MGGA_C_SCAN",
    )

    r2scan = VocabularyTerm(
        code="R2SCAN",
        label="r2SCAN",
        description="LibXC components: XC_MGGA_X_R2SCAN, XC_MGGA_C_R2SCAN",
    )

    mbj = VocabularyTerm(
        code="MBJ",
        label="mBJ",
        description="LibXC components: XC_MGGA_X_TB09",
    )

    pbe0 = VocabularyTerm(
        code="PBE0",
        label="PBE0",
        description="LibXC components: XC_HYB_GGA_XC_PBEH",
    )

    hse03 = VocabularyTerm(
        code="HSE03",
        label="HSE03",
        description="LibXC components: XC_HYB_GGA_XC_HSE03",
        prev_versions=["XC_FUNC_HSE03:v0"],
    )

    hse06 = VocabularyTerm(
        code="HSE06",
        label="HSE06",
        description="LibXC components: XC_HYB_GGA_XC_HSE06",
        prev_versions=["XC_FUNC_HSE06:v0"],
    )

    b3lyp = VocabularyTerm(
        code="B3LYP",
        label="B3LYP",
        description="LibXC components: XC_HYB_GGA_XC_B3LYP",
        prev_versions=["XC_FUNC_B3LYP:v0"],
    )

    scan0 = VocabularyTerm(
        code="SCAN0",
        label="SCAN0",
        description="LibXC components: XC_HYB_MGGA_X_SCAN0, XC_MGGA_C_SCAN",
        prev_versions=["XC_FUNC_SCAN0:v0"],
    )


class JacobsLadder(VocabularyType):
    defs = VocabularyTypeDef(
        code="JACOBS_LADDER",
        description="Rung of Jacob's ladder of an exchange-correlation functional",
        prev_versions=["PSEUDOPOT_FUNCTIONAL:v0"],
    )

    lda = VocabularyTerm(
        code="LDA",
        label="LDA",
        description="Local density approximation",
        prev_versions=["PSEUDOPOT_LDA:v0"],
    )

    gga = VocabularyTerm(
        code="GGA",
        label="GGA",
        description="Generalized gradient approximation",
        prev_versions=["PSEUDOPOT_GGA:v0"],
    )

    meta_gga = VocabularyTerm(
        code="META_GGA",
        label="meta-GGA",
        description="Meta-generalized gradient approximation",
    )

    hybrid_gga = VocabularyTerm(
        code="HYBRID_GGA",
        label="hybrid-GGA",
        description="Generalized gradient approximation mixed with exact exchange",
        prev_versions=["PSEUDOPOT_HYBRID:v0"],
    )

    hybrid_meta_gga = VocabularyTerm(
        code="HYBRID_META_GGA",
        label="hybrid-meta-GGA",
        description="Meta-generalized gradient approximation mixed with exact exchange",
    )


class ReferenceForm(VocabularyType):
    defs = VocabularyTypeDef(
        code="REFERENCE_FORM",
        description="Kohn-Sham reference form of a density functional theory calculation",
    )

    rks = VocabularyTerm(
        code="RKS",
        label="RKS",
        description="Restricted Kohn-Sham reference",
    )

    uks = VocabularyTerm(
        code="UKS",
        label="UKS",
        description="Unrestricted Kohn-Sham reference",
    )

    roks = VocabularyTerm(
        code="ROKS",
        label="ROKS",
        description="Restricted open-shell Kohn-Sham reference",
    )


class RelativityLevel(VocabularyType):
    defs = VocabularyTypeDef(
        code="RELATIVITY_LEVEL",
        description="Level of relativistic treatment of the valence electrons",
    )

    non_relativistic = VocabularyTerm(
        code="NON_RELATIVISTIC",
        label="Non-relativistic",
        description="Schrödinger equation without relativistic corrections",
    )

    scalar = VocabularyTerm(
        code="SCALAR",
        label="Scalar",
        description="Scalar-relativistic treatment, with spin-orbit coupling omitted",
    )

    two_component = VocabularyTerm(
        code="TWO_COMPONENT",
        label="Two-component",
        description="Two-component treatment with spin-orbit coupling included variationally",
    )

    four_component = VocabularyTerm(
        code="FOUR_COMPONENT",
        label="Four-component",
        description="Four-component Dirac treatment",
    )


class RelativityApproximation(VocabularyType):
    defs = VocabularyTypeDef(
        code="RELATIVITY_APPROXIMATION",
        description="Approximation or decoupling scheme of a relativistic treatment",
    )

    dkh = VocabularyTerm(
        code="DKH",
        label="DKH",
        description="Douglas-Kroll-Hess",
    )

    zora = VocabularyTerm(
        code="ZORA",
        label="ZORA",
        description="Zeroth-order regular approximation",
    )

    fora = VocabularyTerm(
        code="FORA",
        label="FORA",
        description="First-order regular approximation",
    )

    iora = VocabularyTerm(
        code="IORA",
        label="IORA",
        description="Improved regular approximation",
    )

    x2c = VocabularyTerm(
        code="X2C",
        label="X2C",
        description="Exact two-component",
    )

    bss = VocabularyTerm(
        code="BSS",
        label="BSS",
        description="Barysz-Sadlej-Snijders",
    )

    nesc = VocabularyTerm(
        code="NESC",
        label="NESC",
        description="Normalized elimination of the small component",
    )

    pauli = VocabularyTerm(
        code="PAULI",
        label="Pauli",
        description="Pauli spin-orbit correction",
    )

    somf = VocabularyTerm(
        code="SOMF",
        label="SOMF",
        description="Spin-orbit mean-field added after the self-consistent field cycle",
    )


class DispersionModel(VocabularyType):
    defs = VocabularyTypeDef(
        code="DISPERSION_MODEL",
        description="Empirical dispersion correction added to an ab initio method",
    )

    d2 = VocabularyTerm(
        code="D2",
        label="D2",
        description="Grimme DFT-D2",
    )

    d3 = VocabularyTerm(
        code="D3",
        label="D3",
        description="Grimme DFT-D3",
    )

    d3bj = VocabularyTerm(
        code="D3BJ",
        label="D3(BJ)",
        description="Grimme DFT-D3 with Becke-Johnson damping",
    )

    d4 = VocabularyTerm(
        code="D4",
        label="D4",
        description="Grimme DFT-D4",
    )

    obs = VocabularyTerm(
        code="OBS",
        label="OBS",
        description="Ortmann-Bechstedt-Schmidt pairwise correction",
    )

    jchs = VocabularyTerm(
        code="JCHS",
        label="JCHS",
        description="Jurečka-Černý-Hobza-Salahub pairwise correction",
    )

    ts = VocabularyTerm(
        code="TS",
        label="TS",
        description="Tkatchenko-Scheffler density-dependent correction",
    )

    ts_scs = VocabularyTerm(
        code="TS_SCS",
        label="TS-SCS",
        description="Tkatchenko-Scheffler with self-consistent screening",
    )

    mbd = VocabularyTerm(
        code="MBD",
        label="MBD",
        description="Many-body dispersion",
    )

    mbd_rsscs = VocabularyTerm(
        code="MBD_RSSCS",
        label="MBD@rsSCS",
        description="Many-body dispersion with range-separated self-consistent screening",
    )

    xdm = VocabularyTerm(
        code="XDM",
        label="XDM",
        description="Exchange-hole dipole moment model",
    )


class DispersionDamping(VocabularyType):
    defs = VocabularyTypeDef(
        code="DISPERSION_DAMPING",
        description="Short-range damping function of an empirical dispersion correction",
    )

    zero = VocabularyTerm(
        code="ZERO",
        label="zero",
        description="Zero damping",
    )

    bj = VocabularyTerm(
        code="BJ",
        label="BJ",
        description="Becke-Johnson damping",
    )

    fermi = VocabularyTerm(
        code="FERMI",
        label="fermi",
        description="Fermi-type damping",
    )

    rational = VocabularyTerm(
        code="RATIONAL",
        label="rational",
        description="Rational damping",
    )


class NonlocalCorrelation(VocabularyType):
    defs = VocabularyTypeDef(
        code="NONLOCAL_CORRELATION",
        description="Kernel-based nonlocal correlation term added to an exchange-correlation functional",
    )

    vv10 = VocabularyTerm(
        code="VV10",
        label="VV10",
        description="Vydrov-Van Voorhis nonlocal correlation",
    )

    rvv10 = VocabularyTerm(
        code="RVV10",
        label="rVV10",
        description="Revised Vydrov-Van Voorhis nonlocal correlation",
    )

    vdw_df = VocabularyTerm(
        code="VDW_DF",
        label="vdW-DF",
        description="van der Waals density functional",
    )

    vdw_df2 = VocabularyTerm(
        code="VDW_DF2",
        label="vdW-DF2",
        description="Second version of the van der Waals density functional",
    )

    vdw_df_cx = VocabularyTerm(
        code="VDW_DF_CX",
        label="vdW-DF-cx",
        description="Consistent-exchange van der Waals density functional",
    )

    optb88_vdw = VocabularyTerm(
        code="OPTB88_VDW",
        label="optB88-vdW",
        description="van der Waals density functional with optB88 exchange",
    )

    optb86b_vdw = VocabularyTerm(
        code="OPTB86B_VDW",
        label="optB86b-vdW",
        description="van der Waals density functional with optB86b exchange",
    )


class PotentialStyle(VocabularyType):
    defs = VocabularyTypeDef(
        code="POTENTIAL_STYLE",
        description="Functional form of an interatomic potential",
        prev_versions=["ATOM_POTENTIAL_STYLE:v0"],
    )

    eam = VocabularyTerm(
        code="EAM",
        label="Embedded atom model",
        description="Embedded atom model potential",
        prev_versions=["POT_STYLE_EAM:v0"],
    )

    meam = VocabularyTerm(
        code="MEAM",
        label="Modified embedded atom model",
        description="Modified embedded atom model potential",
        prev_versions=["POT_STYLE_MEAM:v0"],
    )

    lennard_jones = VocabularyTerm(
        code="LENNARD_JONES",
        label="Lennard-Jones",
        description="Lennard-Jones pair potential",
        prev_versions=["POT_STYLE_LJ:v0"],
    )

    stillinger_weber = VocabularyTerm(
        code="STILLINGER_WEBER",
        label="Stillinger-Weber",
        description="Stillinger-Weber three-body potential",
        prev_versions=["POT_STYLE_SW:v0"],
    )

    force_field = VocabularyTerm(
        code="FORCE_FIELD",
        label="Force field",
        description="Classical molecular force field with bonded and non-bonded terms",
        prev_versions=["POT_STYLE_FF:v0"],
    )

    mlip = VocabularyTerm(
        code="MLIP",
        label="Machine-learned potential",
        description="Machine-learned interatomic potential fitted to a specific system",
        prev_versions=["POT_STYLE_MLIP:v0"],
    )

    universal_mlip = VocabularyTerm(
        code="UNIVERSAL_MLIP",
        label="Universal machine-learned potential",
        description="Machine-learned interatomic potential trained across the periodic table",
        prev_versions=["POT_STYLE_UMLIP:v0"],
    )


class MethodType(VocabularyType):
    defs = VocabularyTypeDef(
        code="METHOD_TYPE",
        description="Kind of computational method",
    )

    dft = VocabularyTerm(
        code="DFT",
        label="DFT",
        description="Density functional theory",
    )

    force_field = VocabularyTerm(
        code="FORCE_FIELD",
        label="Force field",
        description="Classical or machine-learned interatomic potential",
    )
