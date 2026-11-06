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


class PseudopotentialType(VocabularyType):
    defs = VocabularyTypeDef(
        code="PSEUDOPOTENTIAL_TYPE",
        description="Formalism of a pseudopotential",
        prev_versions=["PSEUDOPOT_TYPE:v0"],
    )

    nc = VocabularyTerm(
        code="NC",
        label="NC",
        description="Norm-conserving pseudopotential",
        prev_versions=["PSEUDOPOT_NC:v0"],
    )

    us = VocabularyTerm(
        code="US",
        label="US",
        description="Ultrasoft pseudopotential in the Vanderbilt formalism",
        prev_versions=["PSEUDOPOT_ULTRASOFT:v0"],
    )

    paw = VocabularyTerm(
        code="PAW",
        label="PAW",
        description="Projector augmented wave dataset",
        prev_versions=["PSEUDOPOT_PAW:v0"],
    )

    nc_paw = VocabularyTerm(
        code="NC_PAW",
        label="NC-PAW",
        description="Projector augmented wave dataset with norm-conserving partial waves",
    )

    nc_paw_gw = VocabularyTerm(
        code="NC_PAW_GW",
        label="NC-PAW-GW",
        description="Norm-conserving projector augmented wave dataset optimized for GW and BSE calculations",
    )


class PseudizationScheme(VocabularyType):
    defs = VocabularyTypeDef(
        code="PSEUDIZATION_SCHEME",
        description="Method used to generate the smooth part of a pseudopotential",
    )

    troullier_martins = VocabularyTerm(
        code="TROULLIER_MARTINS",
        label="Troullier-Martins",
        description="Troullier-Martins scheme with continuous derivatives",
    )

    polynomial = VocabularyTerm(
        code="POLYNOMIAL",
        label="Polynomial",
        description="Polynomial matching at the core radius",
    )

    bessel = VocabularyTerm(
        code="BESSEL",
        label="Bessel",
        description="Construction based on Bessel functions",
    )

    extra_soft = VocabularyTerm(
        code="EXTRA_SOFT",
        label="Extra-Soft",
        description="Scheme optimized for low cutoff energies",
    )


class SystemType(VocabularyType):
    defs = VocabularyTypeDef(
        code="SYSTEM_TYPE",
        description="Periodicity and dimensionality of a simulated system",
    )

    atom = VocabularyTerm(
        code="ATOM",
        label="Atom",
        description="Single isolated atom",
    )

    molecule = VocabularyTerm(
        code="MOLECULE",
        label="Molecule",
        description="Isolated molecule without periodic boundary conditions",
    )

    cluster = VocabularyTerm(
        code="CLUSTER",
        label="Cluster",
        description="Isolated group of atoms without periodic boundary conditions",
    )

    one_dimensional = VocabularyTerm(
        code="ONE_DIMENSIONAL",
        label="1D",
        description="System periodic in one direction, such as a nanowire or a polymer chain",
    )

    surface = VocabularyTerm(
        code="SURFACE",
        label="Surface",
        description="Slab periodic in two directions with a finite thickness in the third",
    )

    two_dimensional = VocabularyTerm(
        code="TWO_DIMENSIONAL",
        label="2D",
        description="Atomically thin layer periodic in two directions, such as graphene",
    )

    bulk = VocabularyTerm(
        code="BULK",
        label="Bulk",
        description="System periodic in all three directions",
    )


class StructuralOrder(VocabularyType):
    defs = VocabularyTypeDef(
        code="STRUCTURAL_ORDER",
        description="Long-range order of the atomic arrangement of a simulated system, as asserted "
        "by its author",
    )

    crystalline = VocabularyTerm(
        code="CRYSTALLINE",
        label="Crystalline",
        description="Atomic arrangement with long-range periodic order",
    )

    amorphous = VocabularyTerm(
        code="AMORPHOUS",
        label="Amorphous",
        description="Atomic arrangement without long-range order",
    )


class LatticeType(VocabularyType):
    defs = VocabularyTypeDef(
        code="LATTICE_TYPE",
        description="Crystal family of a Bravais lattice, given by the first letter of the Pearson symbol",
    )

    triclinic = VocabularyTerm(
        code="TRICLINIC",
        label="a - triclinic",
        description="Triclinic 3D lattice",
    )

    monoclinic = VocabularyTerm(
        code="MONOCLINIC",
        label="m - monoclinic",
        description="Monoclinic 3D lattice",
    )

    orthorhombic = VocabularyTerm(
        code="ORTHORHOMBIC",
        label="o - orthorhombic",
        description="Orthorhombic 3D lattice",
    )

    tetragonal = VocabularyTerm(
        code="TETRAGONAL",
        label="t - tetragonal",
        description="Tetragonal 3D lattice",
    )

    trigonal = VocabularyTerm(
        code="TRIGONAL",
        label="r - trigonal",
        description="Trigonal 3D lattice",
    )

    hexagonal = VocabularyTerm(
        code="HEXAGONAL",
        label="h - hexagonal",
        description="Hexagonal 3D lattice",
    )

    cubic = VocabularyTerm(
        code="CUBIC",
        label="c - cubic",
        description="Cubic 3D lattice",
    )

    oblique = VocabularyTerm(
        code="OBLIQUE",
        label="mp - oblique",
        description="Oblique 2D lattice",
    )

    rectangular = VocabularyTerm(
        code="RECTANGULAR",
        label="op - rectangular",
        description="Rectangular 2D lattice",
    )

    centered_rectangular = VocabularyTerm(
        code="CENTERED_RECTANGULAR",
        label="oc - centered rectangular",
        description="Centered rectangular 2D lattice",
    )

    square = VocabularyTerm(
        code="SQUARE",
        label="tp - square",
        description="Square 2D lattice",
    )

    hexagonal_2d = VocabularyTerm(
        code="HEXAGONAL_2D",
        label="hp - hexagonal 2D",
        description="Hexagonal 2D lattice",
    )

    linear = VocabularyTerm(
        code="LINEAR",
        label="ap - linear",
        description="Linear 1D lattice",
    )


class LatticeCentering(VocabularyType):
    defs = VocabularyTypeDef(
        code="LATTICE_CENTERING",
        description="Centering of a Bravais lattice, given by the second letter of the Pearson symbol",
    )

    primitive = VocabularyTerm(
        code="PRIMITIVE",
        label="P - primitive",
        description="Lattice points only at the cell corners",
    )

    rhombohedral = VocabularyTerm(
        code="RHOMBOHEDRAL",
        label="R - rhombohedral",
        description="Rhombohedral centering of the hexagonal setting",
    )

    side_centered = VocabularyTerm(
        code="SIDE_CENTERED",
        label="S - face centered",
        description="One pair of opposite faces centered",
    )

    body_centered = VocabularyTerm(
        code="BODY_CENTERED",
        label="I - body centered",
        description="Additional lattice point at the cell center",
    )

    face_centered = VocabularyTerm(
        code="FACE_CENTERED",
        label="F - all faces centered",
        description="All faces centered",
    )

    centered_2d = VocabularyTerm(
        code="CENTERED_2D",
        label="c - centered 2D",
        description="Centered 2D lattice",
    )

    primitive_2d = VocabularyTerm(
        code="PRIMITIVE_2D",
        label="p - primitive 2D/1D",
        description="Primitive 2D or 1D lattice",
    )


# Draft vocabularies for atomistic simulations, analyses of their results, and LOBSTER bonding analysis.
# IRIs point to ASMO terms where the meaning matches.
class RelaxationDegreeOfFreedom(VocabularyType):
    defs = VocabularyTypeDef(
        code="RELAXATION_DEGREE_OF_FREEDOM",
        description="Degree of freedom of a structure that may change during a geometry optimization",
        iri=["https://purls.helmholtz-metadaten.de/asmo/RelaxationDOF"],
    )

    atomic_positions = VocabularyTerm(
        code="ATOMIC_POSITIONS",
        label="Atomic positions",
        description="The positions of the atoms may change (v0: ATOM_POS_RELAX)",
        iri=["https://purls.helmholtz-metadaten.de/asmo/AtomicPositionRelaxation"],
    )

    cell_shape = VocabularyTerm(
        code="CELL_SHAPE",
        label="Cell shape",
        description="The shape of the cell may change (v0: ATOM_CELL_SHP_RELAX)",
        iri=["https://purls.helmholtz-metadaten.de/asmo/CellShapeRelaxation"],
    )

    cell_volume = VocabularyTerm(
        code="CELL_VOLUME",
        label="Cell volume",
        description="The volume of the cell may change (v0: ATOM_CELL_VOL_RELAX)",
        iri=["https://purls.helmholtz-metadaten.de/asmo/CellVolumeRelaxation"],
    )


class GeometryOptimizationAlgorithm(VocabularyType):
    defs = VocabularyTypeDef(
        code="GEOMETRY_OPTIMIZATION_ALGORITHM",
        description="Algorithm used to move the nuclei, and the cell if allowed, towards a local energy minimum",
        prev_versions=["MINIMIZATION_ALGO:v0"],
    )

    conjugate_gradient = VocabularyTerm(
        code="CONJUGATE_GRADIENT",
        label="Conjugate gradient",
        description="Each search direction is conjugate to the previous ones, with a line minimization along it "
        "(VASP: IBRION = 2)",
        prev_versions=["MIN_ALGO_CG:v0"],
    )

    quasi_newton_rmm_diis = VocabularyTerm(
        code="QUASI_NEWTON_RMM_DIIS",
        label="Quasi-Newton (RMM-DIIS)",
        description="Quasi-Newton (variable metric) method that builds an approximate inverse Hessian from the "
        "history of previous steps (VASP: IBRION = 1)",
    )

    damped_molecular_dynamics = VocabularyTerm(
        code="DAMPED_MOLECULAR_DYNAMICS",
        label="Damped molecular dynamics",
        description="Molecular dynamics with a friction term on the velocities, so the system comes to rest in a "
        "minimum (VASP: IBRION = 3)",
        prev_versions=["MIN_ALGO_DAMPED_MD:v0"],
    )

    steepest_descent = VocabularyTerm(
        code="STEEPEST_DESCENT",
        label="Steepest descent",
        description="Steps along the direction of the forces",
        prev_versions=["MIN_ALGO_STEEP_DESC:v0"],
    )

    lbfgs = VocabularyTerm(
        code="LBFGS",
        label="Limited-memory BFGS",
        description="Limited-memory Broyden-Fletcher-Goldfarb-Shanno quasi-Newton method",
        prev_versions=["MIN_ALGO_LBFGS:v0"],
    )

    fire = VocabularyTerm(
        code="FIRE",
        label="FIRE",
        description="Fast inertial relaxation engine",
        prev_versions=["MIN_ALGO_FIRE:v0"],
    )

    quickmin = VocabularyTerm(
        code="QUICKMIN",
        label="Quickmin",
        description="Damped molecular dynamics according to Sheppard et al., J. Chem. Phys. 128, 134106 (2008)",
        prev_versions=["MIN_ALGO_QUICKMIN:v0"],
    )

    hessian_free_truncated_newton = VocabularyTerm(
        code="HESSIAN_FREE_TRUNCATED_NEWTON",
        label="Hessian-free truncated Newton",
        description="Hessian-free truncated Newton algorithm",
        prev_versions=["MIN_ALGO_HFTN:v0"],
    )


class ForceConvergenceNorm(VocabularyType):
    defs = VocabularyTypeDef(
        code="FORCE_CONVERGENCE_NORM",
        description="Reduction of the atomic forces that is compared with the force convergence threshold of a "
        "geometry optimization. The criteria are not interchangeable and a threshold cannot be converted between them",
    )

    max_atom_norm = VocabularyTerm(
        code="MAX_ATOM_NORM",
        label="Maximum per-atom force norm",
        description="Largest Euclidean norm of the force on a single atom (VASP: negative EDIFFG; LAMMPS: min_modify "
        "norm max)",
    )

    max_component = VocabularyTerm(
        code="MAX_COMPONENT",
        label="Maximum force component",
        description="Largest absolute Cartesian component of the force on any atom (LAMMPS: min_modify norm inf)",
    )

    global_vector_norm = VocabularyTerm(
        code="GLOBAL_VECTOR_NORM",
        label="Global force vector norm",
        description="Euclidean norm of the 3N-dimensional vector of all atomic forces; grows with the number of "
        "atoms (LAMMPS: min_modify norm two, the default)",
    )


class OptimizationStopReason(VocabularyType):
    defs = VocabularyTypeDef(
        code="OPTIMIZATION_STOP_REASON",
        description="Reason why a geometry optimization stopped, as reported by the code",
    )

    energy_criterion_met = VocabularyTerm(
        code="ENERGY_CRITERION_MET",
        label="Energy criterion met",
        description="The energy convergence criterion was satisfied (VASP: positive EDIFFG reached; LAMMPS: stopping "
        "criterion energy tolerance)",
    )

    force_criterion_met = VocabularyTerm(
        code="FORCE_CRITERION_MET",
        label="Force criterion met",
        description="The force convergence criterion was satisfied (VASP: negative EDIFFG reached; LAMMPS: stopping "
        "criterion force tolerance)",
    )

    max_steps_reached = VocabularyTerm(
        code="MAX_STEPS_REACHED",
        label="Maximum number of steps reached",
        description="The maximum number of ionic steps or iterations was reached without the convergence criteria "
        "being satisfied (VASP: NSW reached; LAMMPS: max iterations)",
    )

    max_force_evaluations_reached = VocabularyTerm(
        code="MAX_FORCE_EVALUATIONS_REACHED",
        label="Maximum number of force evaluations reached",
        description="The maximum number of energy and force evaluations was reached (LAMMPS: max force evaluations)",
    )

    line_search_failed = VocabularyTerm(
        code="LINE_SEARCH_FAILED",
        label="Line search failed",
        description="The minimizer could not make further progress, such as a line search step length of zero or a "
        "trust region that became too small (LAMMPS: linesearch alpha is zero, trust region too small)",
    )

    time_limit_reached = VocabularyTerm(
        code="TIME_LIMIT_REACHED",
        label="Time limit reached",
        description="The run stopped at a wall-time limit set in the code or by the job scheduler",
    )

    aborted = VocabularyTerm(
        code="ABORTED",
        label="Aborted",
        description="The run stopped because of an error or was terminated externally",
    )


class ElectronicAlgorithm(VocabularyType):
    defs = VocabularyTypeDef(
        code="ELECTRONIC_ALGORITHM",
        description="Algorithm used to optimize the Kohn-Sham orbitals in the self-consistent field cycle",
        prev_versions=["MINIMIZATION_ALGO:v0"],
    )

    blocked_davidson = VocabularyTerm(
        code="BLOCKED_DAVIDSON",
        label="Blocked Davidson",
        description="Blocked Davidson iterative diagonalization (VASP: ALGO = Normal)",
        prev_versions=["MIN_ALGO_BLOCK_DVD:v0"],
    )

    rmm_diis = VocabularyTerm(
        code="RMM_DIIS",
        label="RMM-DIIS",
        description="Residual minimization method with direct inversion in the iterative subspace "
        "(VASP: ALGO = VeryFast)",
        prev_versions=["MIN_ALGO_RMM_DIIS:v0"],
    )

    blocked_davidson_then_rmm_diis = VocabularyTerm(
        code="BLOCKED_DAVIDSON_THEN_RMM_DIIS",
        label="Blocked Davidson, then RMM-DIIS",
        description="Blocked Davidson in the initial phase, then RMM-DIIS (VASP: ALGO = Fast)",
        prev_versions=["MIN_ALGO_VAPS_FAST:v0"],
    )

    all_band_conjugate_gradient = VocabularyTerm(
        code="ALL_BAND_CONJUGATE_GRADIENT",
        label="All-band conjugate gradient",
        description="Direct minimization updating all orbitals simultaneously with a preconditioned conjugate "
        "gradient (VASP: ALGO = All)",
        prev_versions=["MIN_ALGO_PREC_CG:v0"],
    )

    exact_diagonalization = VocabularyTerm(
        code="EXACT_DIAGONALIZATION",
        label="Exact diagonalization",
        description="Exact diagonalization of the Hamiltonian (VASP: ALGO = Exact)",
        prev_versions=["MIN_ALGO_EXCT_DIAG:v0"],
    )


class KpointMeshType(VocabularyType):
    defs = VocabularyTypeDef(
        code="KPOINT_MESH_TYPE",
        iri=["https://purls.helmholtz-metadaten.de/asmo/KPointMesh"],
        description="How the k-points sampling the Brillouin zone are placed",
        prev_versions=["ATOM_KPOINT_TYPE:v0"],
    )

    gamma_centered = VocabularyTerm(
        code="GAMMA_CENTERED",
        iri=["https://purls.helmholtz-metadaten.de/asmo/GammaCenteredKPointMesh"],
        label="Gamma-centered mesh",
        description="Regular mesh that always contains the Gamma point. Recommended for the tetrahedron methods",
    )

    monkhorst_pack = VocabularyTerm(
        code="MONKHORST_PACK",
        iri=["https://purls.helmholtz-metadaten.de/asmo/MonkhorstPackKPointMesh"],
        label="Monkhorst-Pack mesh",
        description="Regular mesh of Monkhorst and Pack, Phys. Rev. B 13, 5188 (1976); it contains the Gamma point "
        "only for odd numbers of subdivisions",
        prev_versions=["KPOINTS_MP:v0"],
    )

    explicit_list = VocabularyTerm(
        code="EXPLICIT_LIST",
        iri=["https://purls.helmholtz-metadaten.de/asmo/ExplicitKPointMesh"],
        label="Explicit list",
        description="K-points and weights given one by one",
        prev_versions=["KPOINTS_MANUAL:v0"],
    )


class SymmetryUsage(VocabularyType):
    defs = VocabularyTypeDef(
        code="SYMMETRY_USAGE",
        description="Which symmetries an electronic-structure calculation uses to reduce the k-point sampling",
    )

    crystal_symmetry = VocabularyTerm(
        code="CRYSTAL_SYMMETRY",
        label="Crystal symmetry",
        description="The symmetry of the structure (and of the initial magnetic moments) is used (VASP: ISYM = 1, "
        "2, or 3)",
    )

    time_reversal_only = VocabularyTerm(
        code="TIME_REVERSAL_ONLY",
        label="Time reversal only",
        description="No crystal symmetry is used, but the wave function at -k is taken as the complex conjugate of "
        "the one at k (VASP: ISYM = 0)",
    )

    none = VocabularyTerm(
        code="NONE",
        label="None",
        description="No symmetry is used, not even time reversal (VASP: ISYM = -1)",
    )


class OccupationScheme(VocabularyType):
    defs = VocabularyTypeDef(
        code="OCCUPATION_SCHEME",
        description="Method used to set the (partial) occupations of the Kohn-Sham orbitals",
        prev_versions=["ELECTRONIC_SMEARING:v0"],
    )

    gaussian = VocabularyTerm(
        code="GAUSSIAN",
        label="Gaussian smearing",
        description="Occupations from a Gaussian-broadened step function (VASP: ISMEAR = 0)",
        prev_versions=["ELEC_SMEAR_GAUSS:v0"],
    )

    fermi_dirac = VocabularyTerm(
        code="FERMI_DIRAC",
        label="Fermi-Dirac smearing",
        description="Occupations from the Fermi-Dirac distribution; the smearing width is an electronic "
        "temperature (VASP: ISMEAR = -1)",
        prev_versions=["ELEC_SMEAR_FERMI:v0"],
    )

    methfessel_paxton = VocabularyTerm(
        code="METHFESSEL_PAXTON",
        label="Methfessel-Paxton smearing",
        description="Higher-order approximation of the step function by Methfessel and Paxton; occupations can be "
        "negative or larger than one, so it is not suited for insulators (VASP: ISMEAR > 0, the value is the order)",
        prev_versions=["ELEC_SMEAR_MP:v0"],
    )

    tetrahedron = VocabularyTerm(
        code="TETRAHEDRON",
        label="Tetrahedron method",
        description="Linear tetrahedron method without smearing (VASP: ISMEAR = -4)",
        prev_versions=["ELEC_SMEAR_TET:v0"],
    )

    tetrahedron_bloechl = VocabularyTerm(
        code="TETRAHEDRON_BLOECHL",
        label="Tetrahedron method with Bloechl corrections",
        description="Tetrahedron method with Bloechl corrections without smearing (VASP: ISMEAR = -5)",
        prev_versions=["ELEC_SMEAR_TET_BL:v0"],
    )

    fixed = VocabularyTerm(
        code="FIXED",
        label="Fixed occupations",
        description="Occupations given by the user or read from a file and kept fixed (VASP: ISMEAR = -2)",
        prev_versions=["ELEC_SMEAR_FILE:v0"],
    )


class ThermodynamicEnsemble(VocabularyType):
    defs = VocabularyTypeDef(
        code="THERMODYNAMIC_ENSEMBLE",
        iri=["https://purls.helmholtz-metadaten.de/asmo/StatisticalEnsemble"],
        description="Statistical ensemble a simulation is meant to sample, named by the quantities held fixed",
        prev_versions=["THERMODYN_ENSEMBLE:v0"],
    )

    nve = VocabularyTerm(
        code="NVE",
        iri=["https://purls.helmholtz-metadaten.de/asmo/MicrocanonicalEnsemble"],
        label="NVE (microcanonical)",
        description="Fixed number of particles, volume, and energy",
        prev_versions=["TD_ENSEMBLE_NVE:v0"],
    )

    nvt = VocabularyTerm(
        code="NVT",
        iri=["https://purls.helmholtz-metadaten.de/asmo/CanonicalEnsemble"],
        label="NVT (canonical)",
        description="Fixed number of particles, volume, and temperature",
        prev_versions=["TD_ENSEMBLE_ATOM_ENS.NVT:v0"],
    )

    npt = VocabularyTerm(
        code="NPT",
        iri=["https://purls.helmholtz-metadaten.de/asmo/IsothermalIsobaricEnsemble"],
        label="NPT (isothermal-isobaric)",
        description="Fixed number of particles, pressure, and temperature",
        prev_versions=["TD_ENSEMBLE_NPT:v0"],
    )

    nph = VocabularyTerm(
        code="NPH",
        iri=["https://purls.helmholtz-metadaten.de/asmo/IsoenthalpicIsobaricEnsemble"],
        label="NPH (isoenthalpic-isobaric)",
        description="Fixed number of particles, pressure, and enthalpy",
        prev_versions=["TD_ENSEMBLE_NPH:v0"],
    )

    grand_canonical = VocabularyTerm(
        code="GRAND_CANONICAL",
        iri=["https://purls.helmholtz-metadaten.de/asmo/GrandCanonicalEnsemble"],
        label="Grand canonical (muVT)",
        description="Fixed chemical potentials, volume, and temperature; the number of particles varies",
        prev_versions=["TD_ENSEMBLE_GC:v0"],
    )

    semi_grand_canonical = VocabularyTerm(
        code="SEMI_GRAND_CANONICAL",
        label="Semi-grand canonical",
        description="Fixed total number of particles, temperature, and differences of the chemical potentials; "
        "the composition varies. Exists at fixed volume or at fixed pressure, depending on the molecular dynamics "
        "ensemble combined with the identity changes (such as LAMMPS fix atom/swap with NVT or NPT)",
        prev_versions=["TD_ENSEMBLE_SGC:v0"],
    )


class Thermostat(VocabularyType):
    defs = VocabularyTypeDef(
        code="THERMOSTAT",
        iri=["https://purls.helmholtz-metadaten.de/asmo/Thermostat"],
        description="Algorithm used to control the temperature in molecular dynamics",
    )

    nose_hoover = VocabularyTerm(
        code="NOSE_HOOVER",
        iri=["https://purls.helmholtz-metadaten.de/asmo/NoseHoover"],
        label="Nose-Hoover",
        description="Deterministic extended-system thermostat (Nose 1984, Hoover 1985); samples the canonical "
        "ensemble if the dynamics is ergodic, which can fail for small or stiff systems",
    )

    nose_hoover_chain = VocabularyTerm(
        code="NOSE_HOOVER_CHAIN",
        label="Nose-Hoover chain",
        description="Nose-Hoover thermostat coupled to a chain of further thermostats, intended to improve "
        "ergodic sampling of the canonical ensemble; this is not guaranteed for every system "
        "(Martyna, Klein, Tuckerman 1992)",
    )

    langevin = VocabularyTerm(
        code="LANGEVIN",
        iri=["https://purls.helmholtz-metadaten.de/asmo/Langevin"],
        label="Langevin",
        description="Stochastic dynamics with a friction force and a random force; samples the canonical ensemble",
    )

    andersen = VocabularyTerm(
        code="ANDERSEN",
        iri=["https://purls.helmholtz-metadaten.de/asmo/AndersenThermostat"],
        label="Andersen",
        description="Velocities of randomly chosen particles are redrawn from the Maxwell-Boltzmann distribution "
        "(Andersen 1980); samples the canonical ensemble but disturbs the dynamics",
    )

    stochastic_velocity_rescaling = VocabularyTerm(
        code="STOCHASTIC_VELOCITY_RESCALING",
        iri=["https://purls.helmholtz-metadaten.de/asmo/BussiDonadioParrinello"],
        label="Stochastic velocity rescaling",
        description="Velocities are rescaled by a random factor chosen so that the canonical ensemble is sampled "
        "(Bussi, Donadio, Parrinello 2007)",
    )

    berendsen = VocabularyTerm(
        code="BERENDSEN",
        iri=["https://purls.helmholtz-metadaten.de/asmo/BerendsenThermostat"],
        label="Berendsen",
        description="Weak coupling to a heat bath: the temperature relaxes exponentially to the target with a "
        "time constant (Berendsen et al. 1984); does not sample the canonical ensemble",
    )

    velocity_rescaling = VocabularyTerm(
        code="VELOCITY_RESCALING",
        iri=["https://purls.helmholtz-metadaten.de/asmo/VelocityRescaling"],
        label="Velocity rescaling",
        description="Velocities are rescaled to give exactly the target temperature; does not sample the "
        "canonical ensemble",
    )


class Barostat(VocabularyType):
    defs = VocabularyTypeDef(
        code="BAROSTAT",
        iri=["https://purls.helmholtz-metadaten.de/asmo/Barostat"],
        description="Algorithm used to control the pressure in molecular dynamics",
    )

    andersen = VocabularyTerm(
        code="ANDERSEN",
        iri=["https://purls.helmholtz-metadaten.de/asmo/AndersenBarostat"],
        label="Andersen",
        description="Extended system with the volume as dynamical variable; isotropic volume changes only "
        "(Andersen 1980)",
    )

    parrinello_rahman = VocabularyTerm(
        code="PARRINELLO_RAHMAN",
        iri=["https://purls.helmholtz-metadaten.de/asmo/ParrinelloRahman"],
        label="Parrinello-Rahman",
        description="Extended system with the cell vectors as dynamical variables, so the cell shape can change "
        "(Parrinello, Rahman 1980, 1981)",
    )

    martyna_tobias_klein = VocabularyTerm(
        code="MARTYNA_TOBIAS_KLEIN",
        label="Martyna-Tobias-Klein",
        description="Extended-system equations of motion that generate the isothermal-isobaric ensemble, for "
        "isotropic or fully flexible cells (Martyna, Tobias, Klein 1994)",
    )

    berendsen = VocabularyTerm(
        code="BERENDSEN",
        iri=["https://purls.helmholtz-metadaten.de/asmo/BerendsenBarostat"],
        label="Berendsen",
        description="Weak coupling to a pressure bath: the cell is scaled so the pressure relaxes to the target "
        "with a time constant (Berendsen et al. 1984); does not sample the isothermal-isobaric ensemble",
    )


class PressureCoupling(VocabularyType):
    defs = VocabularyTypeDef(
        code="PRESSURE_COUPLING",
        description="Which cell degrees of freedom a barostat may change",
    )

    isotropic = VocabularyTerm(
        code="ISOTROPIC",
        label="Isotropic",
        description="The cell is scaled uniformly; its shape is kept",
    )

    anisotropic = VocabularyTerm(
        code="ANISOTROPIC",
        label="Anisotropic",
        description="The cell lengths change independently; the cell angles are kept",
    )

    fully_flexible = VocabularyTerm(
        code="FULLY_FLEXIBLE",
        label="Fully flexible",
        description="All six degrees of freedom of the cell, lengths and angles, may change",
    )


class EquationOfState(VocabularyType):
    defs = VocabularyTypeDef(
        code="EQUATION_OF_STATE",
        iri=["https://purls.helmholtz-metadaten.de/asmo/EquationOfStateFit"],
        description="Functional form of an equation of state fitted to energy-volume data",
        prev_versions=["MURN_EQN_OF_STATE:v0"],
    )

    murnaghan = VocabularyTerm(
        code="MURNAGHAN",
        iri=["https://purls.helmholtz-metadaten.de/asmo/Murnaghan"],
        label="Murnaghan",
        description="Assumes a bulk modulus that varies linearly with pressure (Murnaghan 1944)",
        prev_versions=["EOS_MURNAGHAN:v0"],
    )

    birch_murnaghan = VocabularyTerm(
        code="BIRCH_MURNAGHAN",
        iri=["https://purls.helmholtz-metadaten.de/asmo/BirchMurnaghan"],
        label="Birch-Murnaghan",
        description="Expansion of the energy in the Eulerian finite strain (Birch 1947); the order is given "
        "separately",
        prev_versions=["EOS_BIRCH_MURNAGHAN:v0"],
    )

    vinet = VocabularyTerm(
        code="VINET",
        iri=["https://purls.helmholtz-metadaten.de/asmo/Vinet"],
        label="Vinet",
        description="Universal equation of state derived from a scaled binding-energy curve (Vinet et al. 1987)",
        prev_versions=["EOS_VINET:v0"],
    )

    poirier_tarantola = VocabularyTerm(
        code="POIRIER_TARANTOLA",
        label="Poirier-Tarantola",
        description="Expansion in the logarithmic (Hencky, natural) strain (Poirier, Tarantola 1998); the order "
        "is given separately",
    )

    polynomial = VocabularyTerm(
        code="POLYNOMIAL",
        label="Polynomial",
        description="Polynomial in the volume; the order is given separately",
        prev_versions=["EOS_POLYNOMIAL:v0"],
    )


class BondingIndicator(VocabularyType):
    defs = VocabularyTypeDef(
        code="BONDING_INDICATOR",
        description="Energy-resolved, orbital-pair indicator of chemical bonding between two atoms in a solid",
    )

    cohp = VocabularyTerm(
        code="COHP",
        label="COHP",
        description="Crystal orbital Hamilton population: partitions the band-structure energy into orbital-pair "
        "contributions, weighted by the Hamiltonian matrix element. Negative values indicate bonding and positive "
        "values antibonding interactions. Its energy integral up to the Fermi level (ICOHP) is an indicator of bond "
        "strength, not a bond dissociation energy. Dronskowski and Bloechl, J. Phys. Chem. 97, 8617 (1993)",
    )

    coop = VocabularyTerm(
        code="COOP",
        label="COOP",
        description="Crystal orbital overlap population: density of states weighted by the overlap population of an "
        "orbital pair. Positive values indicate bonding and negative values antibonding interactions. "
        "Hughbanks and Hoffmann, J. Am. Chem. Soc. 105, 3528 (1983)",
    )

    cobi = VocabularyTerm(
        code="COBI",
        label="COBI",
        description="Two-center crystal orbital bond index: energy-resolved, weighted by the density matrix "
        "element; generalizes the Wiberg-Mayer bond index to solids. Positive values indicate bonding. Its energy "
        "integral up to the Fermi level (ICOBI) is a covalent bond-order index, not an integer Lewis bond order. "
        "Multicenter COBI, whose sign interpretation differs, is not covered by this term. Mueller et al., "
        "J. Phys. Chem. C (2021), doi:10.1021/acs.jpcc.1c00718",
    )


class PopulationAnalysis(VocabularyType):
    defs = VocabularyTypeDef(
        code="POPULATION_ANALYSIS",
        description="Scheme used to partition the electrons of a system among its atoms, from which atomic gross "
        "populations and charges are obtained",
    )

    mulliken = VocabularyTerm(
        code="MULLIKEN",
        label="Mulliken",
        description="Mulliken population analysis, which splits overlap populations equally between the two atoms",
    )

    loewdin = VocabularyTerm(
        code="LOEWDIN",
        label="Loewdin",
        description="Loewdin population analysis, carried out in the symmetrically orthonormalized local basis",
    )


class ValenceAssignmentScheme(VocabularyType):
    defs = VocabularyTypeDef(
        code="VALENCE_ASSIGNMENT_SCHEME",
        description="Source of the atomic valences used to classify atoms as cations or anions in an automated "
        "bonding analysis",
    )

    mulliken_charges = VocabularyTerm(
        code="MULLIKEN_CHARGES",
        label="Mulliken charges",
        description="Signs of the Mulliken charges from the population analysis",
    )

    loewdin_charges = VocabularyTerm(
        code="LOEWDIN_CHARGES",
        label="Loewdin charges",
        description="Signs of the Loewdin charges from the population analysis",
    )

    bond_valence = VocabularyTerm(
        code="BOND_VALENCE",
        label="Bond valence",
        description="Valences estimated from the crystal structure by a bond valence analysis, without using the "
        "wave function",
    )


class BondSelection(VocabularyType):
    defs = VocabularyTypeDef(
        code="BOND_SELECTION",
        description="Kinds of atom pairs included in an automated bonding analysis",
    )

    cation_anion = VocabularyTerm(
        code="CATION_ANION",
        label="Cation-anion",
        description="Only bonds between atoms classified as cations and atoms classified as anions",
    )

    all_bonds = VocabularyTerm(
        code="ALL",
        label="All",
        description="All atom pairs, including cation-cation and anion-anion interactions",
    )
