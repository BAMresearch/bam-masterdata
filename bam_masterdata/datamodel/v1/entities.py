from bam_masterdata.datamodel.v1.base_objects import Entity
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment

# Hierarchy of the Entity branch of datamodel/v1:

#   Entity                          (see `base_objects.py`)
#   ├── Context
#   │   ├── Software
#   │   ├── WorkflowDefinition
#   │   ├── Pseudopotential
#   │   ├── SimulatedSystem
#   │   ├── ComputationalMethod
#   │   └── InputSpecification
#   │       ├── ElectronicStructureParameters
#   │       ├── GeometryOptimizationParameters
#   │       ├── MolecularDynamicsParameters
#   │       ├── EquationOfStateFitParameters
#   │       ├── OrbitalProjectionParameters
#   │       ├── ProjectionQualityParameters
#   │       ├── BondingAnalysisParameters
#   │       └── BondingEnvironmentParameters
#   └── MaterialEntity
#       └── HPC


class Context(Entity):
    defs = ObjectTypeDef(
        code="CONTEXT",
        description="A Context is an entity that carries information about other entities or activities, "
        "such as specifications, parameters, or results.",
        generated_code_prefix="CTX",
        iri=["http://purl.obolibrary.org/obo/IAO_0000030"],
    )


class MaterialEntity(Entity):
    defs = ObjectTypeDef(
        code="MATERIAL_ENTITY",
        description="A MaterialEntity is an entity that has some portion of matter as part, such as a "
        "material, a sample, or a device.",
        generated_code_prefix="MAT_ENT",
        iri=["http://purl.obolibrary.org/obo/BFO_0000040"],
    )


class Software(Context):
    defs = ObjectTypeDef(
        code="SOFTWARE",
        description="A Software is a context that specifies a computer program or library, in a given version, which "
        "can be executed to carry out a computation.",
        generated_code_prefix="SW",
        iri=["http://purl.obolibrary.org/obo/IAO_0000010"],
        prev_versions=["SOFTWARE_CODE:v0"],
    )

    version = PropertyTypeAssignment(
        code="VERSION",
        data_type="VARCHAR",
        property_label="Version",
        description="Version identifier of the entity, such as a release number or a date.",
        mandatory=False,
        section="Software Details",
        prev_versions=["VERSION:v0"],
    )

    license = PropertyTypeAssignment(
        code="LICENSE",
        data_type="VARCHAR",
        property_label="License",
        description="License under which the entity is distributed.",
        mandatory=False,
        section="Software Details",
        prev_versions=["LICENSE:v0"],
    )

    link = PropertyTypeAssignment(
        code="LINK",
        data_type="HYPERLINK",
        property_label="Link",
        description="Website or download location of the entity, such as the project page or a repository.",
        mandatory=False,
        section="Software Details",
        prev_versions=["SOURCE_LINK:v0"],
    )

    # Properties from v0 that need to be migrated to v1 (from SOFTWARE_CODE:v0):
    # SOFTWARE_NAME
    # REFERENCE


class WorkflowDefinition(Context):
    defs = ObjectTypeDef(
        code="WORKFLOW_DEFINITION",
        description="A WorkflowDefinition is a context that specifies the steps of a computational "
        "workflow and the order in which they are executed.",
        generated_code_prefix="WF_DEF",
        iri=["https://w3id.org/pmd/co/PMD_0000012"],
        prev_versions=["WORKFLOW_REFERENCE:v0"],
    )

    # Properties from v0 that need to be migrated to v1 (from WORKFLOW_REFERENCE:v0):
    # REFERENCE


class Pseudopotential(Context):
    defs = ObjectTypeDef(
        code="PSEUDOPOTENTIAL",
        description="A Pseudopotential is a context that specifies a pseudopotential or PAW dataset replacing the "
        "core electrons of a chemical species in electronic structure calculations.",
        generated_code_prefix="PSEUDO",
        prev_versions=["PSEUDOPOTENTIAL:v0"],
    )

    version = PropertyTypeAssignment(
        code="VERSION",
        data_type="VARCHAR",
        property_label="Version",
        description="Version identifier of the entity, such as a release number or a date.",
        mandatory=False,
        section="Pseudopotential Details",
        prev_versions=["VERSION:v0"],
    )

    license = PropertyTypeAssignment(
        code="LICENSE",
        data_type="VARCHAR",
        property_label="License",
        description="License under which the entity is distributed.",
        mandatory=False,
        section="Pseudopotential Details",
        prev_versions=["LICENSE:v0"],
    )

    chemical_species = PropertyTypeAssignment(
        code="CHEMICAL_SPECIES",
        data_type="VARCHAR",
        property_label="Chemical species",
        description="Chemical species described by the entity, given as element symbols such as Fe or C.",
        mandatory=False,
        section="Pseudopotential Details",
        multivalued=True,
        prev_versions=["CHEM_SPECIES_ADDRESSED:v0"],
    )

    pseudopotential_type = PropertyTypeAssignment(
        code="PSEUDOPOTENTIAL_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="PSEUDOPOTENTIAL_TYPE",
        property_label="Pseudopotential type",
        description="Formalism of the pseudopotential, such as norm-conserving, ultrasoft, or PAW.",
        mandatory=False,
        section="Pseudopotential Details",
        prev_versions=["PSEUDOPOT_TYPE:v0"],
    )

    xc_functional = PropertyTypeAssignment(
        code="XC_FUNCTIONAL",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="XC_FUNCTIONAL",
        property_label="Exchange-correlation functional",
        description="Exchange-correlation functional, such as PBE or HSE06.",
        mandatory=False,
        section="Pseudopotential Details",
    )

    jacobs_ladder = PropertyTypeAssignment(
        code="JACOBS_LADDER",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="JACOBS_LADDER",
        property_label="Jacob's ladder",
        description="Highest rung of Jacob's ladder among the components of the exchange-correlation functional.",
        mandatory=False,
        section="Pseudopotential Details",
        prev_versions=["PSEUDOPOT_FUNC:v0"],
    )

    n_valence_electrons = PropertyTypeAssignment(
        code="N_VALENCE_ELECTRONS",
        data_type="REAL",
        property_label="Number of valence electrons",
        description="Number of valence electrons treated explicitly by the pseudopotential.",
        mandatory=False,
        section="Pseudopotential Details",
    )

    reference_configuration = PropertyTypeAssignment(
        code="REFERENCE_CONFIGURATION",
        data_type="VARCHAR",
        property_label="Reference configuration",
        description="Electronic configuration used to generate the pseudopotential, such as 3p6 3d7 4s1.",
        mandatory=False,
        section="Pseudopotential Details",
    )

    semicore_states = PropertyTypeAssignment(
        code="SEMICORE_STATES",
        data_type="VARCHAR",
        property_label="Semicore states",
        description="Semicore shells treated as valence states by the pseudopotential, such as 3p.",
        mandatory=False,
        section="Pseudopotential Details",
        prev_versions=["PSEUDOPOT_SEMICORE:v0"],
    )

    is_gw_optimized = PropertyTypeAssignment(
        code="IS_GW_OPTIMIZED",
        data_type="BOOLEAN",
        property_label="GW optimized",
        description="Whether the pseudopotential is optimized for GW and other excited-state calculations.",
        mandatory=False,
        section="Pseudopotential Details",
    )

    recommended_cutoff = PropertyTypeAssignment(
        code="RECOMMENDED_CUTOFF",
        data_type="REAL",
        property_label="Recommended cutoff",
        units="eV",
        description="Plane-wave cutoff energy for the wavefunctions recommended for the pseudopotential.",
        mandatory=False,
        section="Pseudopotential Details",
    )

    pseudization_scheme = PropertyTypeAssignment(
        code="PSEUDIZATION_SCHEME",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="PSEUDIZATION_SCHEME",
        property_label="Pseudization scheme",
        description="Method used to generate the smooth part of the pseudopotential.",
        mandatory=False,
        section="Pseudopotential Details",
    )

    software_compatibility = PropertyTypeAssignment(
        code="SOFTWARE_COMPATIBILITY",
        data_type="VARCHAR",
        property_label="Software compatibility",
        description="Software that can use the entity as input.",
        mandatory=False,
        section="Pseudopotential Details",
        prev_versions=["SW_COMPATIBILITY:v0"],
    )

    # Properties from v0 that need to be migrated to v1 (from PSEUDOPOTENTIAL:v0):
    # REFERENCE


class SimulatedSystem(Context):
    defs = ObjectTypeDef(
        code="SIMULATED_SYSTEM",
        description="A SimulatedSystem is a context that specifies a set of particles, such as atoms, with their "
        "positions, cell, and periodicity, used as input to a computation or produced by one.",
        generated_code_prefix="SIM_SYS",
        prev_versions=[
            "MAT_SIM_STRUCTURE:v0",
            "MAT_SIM_STRUCTURE.CRYSTAL:v0",
            "MAT_SIM_STRUCTURE.AMORPHOUS:v0",
        ],
    )

    system_type = PropertyTypeAssignment(
        code="SYSTEM_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="SYSTEM_TYPE",
        property_label="System type",
        description="Periodicity and dimensionality of the system, such as molecule, surface, or bulk.",
        mandatory=False,
        section="System Details",
    )

    dimensionality = PropertyTypeAssignment(
        code="DIMENSIONALITY",
        data_type="INTEGER",
        property_label="Dimensionality",
        description="Number of dimensions in which the system is extended: 0, 1, 2, or 3.",
        mandatory=False,
        section="System Details",
    )

    structural_order = PropertyTypeAssignment(
        code="STRUCTURAL_ORDER",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="STRUCTURAL_ORDER",
        property_label="Structural order",
        description="Long-range order of the atomic arrangement, as asserted by the author. Not applicable to atoms and molecules.",
        mandatory=False,
        section="System Details",
    )

    n_particles = PropertyTypeAssignment(
        code="N_PARTICLES",
        data_type="INTEGER",
        property_label="Number of particles",
        description="Number of particles, such as atoms, in the system.",
        mandatory=False,
        section="System Details",
        prev_versions=["N_ATOMS_TOTAL:v0"],
    )

    total_charge = PropertyTypeAssignment(
        code="TOTAL_CHARGE",
        data_type="INTEGER",
        property_label="Total charge",
        description="Net charge of the system in units of the elementary charge.",
        mandatory=False,
        section="System Details",
    )

    total_spin_multiplicity = PropertyTypeAssignment(
        code="TOTAL_SPIN_MULTIPLICITY",
        data_type="INTEGER",
        property_label="Total spin multiplicity",
        description="Spin multiplicity 2S+1 of the system, such as 1 for a singlet or 2 for a doublet.",
        mandatory=False,
        section="System Details",
    )

    chemical_formula_descriptive = PropertyTypeAssignment(
        code="CHEMICAL_FORMULA_DESCRIPTIVE",
        data_type="VARCHAR",
        property_label="Descriptive formula",
        description="Chemical formula of the system with non-reduced proportions, such as Fe54C.",
        mandatory=False,
        section="Chemical Formula",
        prev_versions=["CHEM_SPECIES_BY_N_ATOMS:v0"],
    )

    chemical_formula_reduced = PropertyTypeAssignment(
        code="CHEMICAL_FORMULA_REDUCED",
        data_type="VARCHAR",
        property_label="Reduced formula",
        description="Alphabetically sorted chemical formula with reduced integer proportions, such as CFe3.",
        mandatory=False,
        section="Chemical Formula",
    )

    chemical_formula_iupac = PropertyTypeAssignment(
        code="CHEMICAL_FORMULA_IUPAC",
        data_type="VARCHAR",
        property_label="IUPAC formula",
        description="Chemical formula with reduced proportions and the elements ordered by electronegativity following the IUPAC nomenclature.",
        mandatory=False,
        section="Chemical Formula",
    )

    chemical_formula_hill = PropertyTypeAssignment(
        code="CHEMICAL_FORMULA_HILL",
        data_type="VARCHAR",
        property_label="Hill formula",
        description="Chemical formula in Hill notation: carbon first, then hydrogen, then the other elements in alphabetical order.",
        mandatory=False,
        section="Chemical Formula",
    )

    chemical_formula_anonymous = PropertyTypeAssignment(
        code="CHEMICAL_FORMULA_ANONYMOUS",
        data_type="VARCHAR",
        property_label="Anonymous formula",
        description="Reduced formula with the elements ordered by proportion and replaced by letters, such as A2B for H2O.",
        mandatory=False,
        section="Chemical Formula",
    )

    lattice_vectors = PropertyTypeAssignment(
        code="LATTICE_VECTORS",
        data_type="JSON",
        property_label="Lattice vectors",
        description="Lattice vectors of the cell in angstrom, as a 3x3 matrix whose rows are the vectors a, b, and c.",
        mandatory=False,
        section="Cell Details",
        prev_versions=["SIM_CELL_VECTORS:v0"],
    )

    periodic_a = PropertyTypeAssignment(
        code="PERIODIC_A",
        data_type="BOOLEAN",
        property_label="Periodic along a",
        description="Whether periodic boundary conditions apply along the lattice vector a.",
        mandatory=False,
        section="Cell Details",
    )

    periodic_b = PropertyTypeAssignment(
        code="PERIODIC_B",
        data_type="BOOLEAN",
        property_label="Periodic along b",
        description="Whether periodic boundary conditions apply along the lattice vector b.",
        mandatory=False,
        section="Cell Details",
    )

    periodic_c = PropertyTypeAssignment(
        code="PERIODIC_C",
        data_type="BOOLEAN",
        property_label="Periodic along c",
        description="Whether periodic boundary conditions apply along the lattice vector c.",
        mandatory=False,
        section="Cell Details",
    )

    cell_volume = PropertyTypeAssignment(
        code="CELL_VOLUME",
        data_type="REAL",
        property_label="Cell volume",
        units="angstrom**3",
        description="Volume of the cell.",
        mandatory=False,
        section="Cell Details",
        prev_versions=["LATTICE_VOLUME_IN_A3:v0", "SIM_CELL_VOLUME_IN_A3:v0"],
    )

    cell_length_a = PropertyTypeAssignment(
        code="CELL_LENGTH_A",
        data_type="REAL",
        property_label="Cell length a",
        units="angstrom",
        description="Length of the lattice vector a.",
        mandatory=False,
        section="Cell Details",
        prev_versions=["LATTICE_PARAM_A_IN_A:v0"],
    )

    cell_length_b = PropertyTypeAssignment(
        code="CELL_LENGTH_B",
        data_type="REAL",
        property_label="Cell length b",
        units="angstrom",
        description="Length of the lattice vector b.",
        mandatory=False,
        section="Cell Details",
        prev_versions=["LATTICE_PARAM_B_IN_A:v0"],
    )

    cell_length_c = PropertyTypeAssignment(
        code="CELL_LENGTH_C",
        data_type="REAL",
        property_label="Cell length c",
        units="angstrom",
        description="Length of the lattice vector c.",
        mandatory=False,
        section="Cell Details",
        prev_versions=["LATTICE_PARAM_C_IN_A:v0"],
    )

    cell_angle_alpha = PropertyTypeAssignment(
        code="CELL_ANGLE_ALPHA",
        data_type="REAL",
        property_label="Cell angle alpha",
        units="degree",
        description="Angle between the lattice vectors b and c.",
        mandatory=False,
        section="Cell Details",
        prev_versions=["LATTICE_ANGALPHA_IN_DEG:v0"],
    )

    cell_angle_beta = PropertyTypeAssignment(
        code="CELL_ANGLE_BETA",
        data_type="REAL",
        property_label="Cell angle beta",
        units="degree",
        description="Angle between the lattice vectors a and c.",
        mandatory=False,
        section="Cell Details",
        prev_versions=["LATTICE_ANGBETA_IN_DEG:v0"],
    )

    cell_angle_gamma = PropertyTypeAssignment(
        code="CELL_ANGLE_GAMMA",
        data_type="REAL",
        property_label="Cell angle gamma",
        units="degree",
        description="Angle between the lattice vectors a and b.",
        mandatory=False,
        section="Cell Details",
        prev_versions=["LATTICE_ANGGAMMA_IN_DEG:v0"],
    )

    space_group_number = PropertyTypeAssignment(
        code="SPACE_GROUP_NUMBER",
        data_type="INTEGER",
        property_label="Space group number",
        description="International Tables number of the space group of the system, from 1 to 230.",
        mandatory=False,
        section="Symmetry Details",
        prev_versions=["SPACE_GROUP:v0"],
    )

    space_group_symbol = PropertyTypeAssignment(
        code="SPACE_GROUP_SYMBOL",
        data_type="VARCHAR",
        property_label="Space group symbol",
        description="International Tables symbol of the space group of the system, such as Fm-3m.",
        mandatory=False,
        section="Symmetry Details",
    )

    point_group_symbol = PropertyTypeAssignment(
        code="POINT_GROUP_SYMBOL",
        data_type="VARCHAR",
        property_label="Point group symbol",
        description="Hermann-Mauguin symbol of the crystallographic point group, such as m-3m.",
        mandatory=False,
        section="Symmetry Details",
    )

    hall_symbol = PropertyTypeAssignment(
        code="HALL_SYMBOL",
        data_type="VARCHAR",
        property_label="Hall symbol",
        description="Hall symbol of the space group setting, such as -F 4 2 3.",
        mandatory=False,
        section="Symmetry Details",
    )

    hall_number = PropertyTypeAssignment(
        code="HALL_NUMBER",
        data_type="INTEGER",
        property_label="Hall number",
        description="Number from 1 to 530 identifying the Hall symbol of the space group setting.",
        mandatory=False,
        section="Symmetry Details",
    )

    lattice_type = PropertyTypeAssignment(
        code="LATTICE_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="LATTICE_TYPE",
        property_label="Lattice type",
        description="Crystal family of the Bravais lattice.",
        mandatory=False,
        section="Symmetry Details",
    )

    lattice_centering = PropertyTypeAssignment(
        code="LATTICE_CENTERING",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="LATTICE_CENTERING",
        property_label="Lattice centering",
        description="Centering of the Bravais lattice.",
        mandatory=False,
        section="Symmetry Details",
    )

    strukturbericht_designation = PropertyTypeAssignment(
        code="STRUKTURBERICHT_DESIGNATION",
        data_type="VARCHAR",
        property_label="Strukturbericht designation",
        description="Strukturbericht classification of the structure, such as B3 or L10.",
        mandatory=False,
        section="Symmetry Details",
    )

    prototype_formula = PropertyTypeAssignment(
        code="PROTOTYPE_FORMULA",
        data_type="VARCHAR",
        property_label="Prototype formula",
        description="Formula of the prototype structure in the AFLOW encyclopedia of crystallographic prototypes.",
        mandatory=False,
        section="Symmetry Details",
    )

    prototype_aflow_id = PropertyTypeAssignment(
        code="PROTOTYPE_AFLOW_ID",
        data_type="VARCHAR",
        property_label="Prototype AFLOW ID",
        description="Identifier of the prototype structure in the AFLOW encyclopedia of crystallographic prototypes.",
        mandatory=False,
        section="Symmetry Details",
    )

    symmetry_tolerance = PropertyTypeAssignment(
        code="SYMMETRY_TOLERANCE",
        data_type="REAL",
        property_label="Symmetry tolerance",
        units="angstrom",
        description="Distance tolerance used to determine the symmetry.",
        mandatory=False,
        section="Symmetry Details",
    )

    symmetry_tool = PropertyTypeAssignment(
        code="SYMMETRY_TOOL",
        data_type="VARCHAR",
        property_label="Symmetry tool",
        description="Software used to determine the symmetry, such as spglib.",
        mandatory=False,
        section="Symmetry Details",
    )

    # Properties from v0 that need to be migrated to v1 (from MAT_SIM_STRUCTURE:v0 and subtypes):
    # BRAVAIS_LATTICE (split into LATTICE_TYPE and LATTICE_CENTERING)
    # CRYSTAL_ORIENTATION
    # SIM_CELL_LENGTHS_IN_A
    # SIM_CELL_ANGLES_IN_DEG
    # LATTICE_C_OVER_A
    # ATOM_SHORT_RNG_ORD
    # ATOM_SAMPLE_TEMP_IN_K
    # WORKFLOW_MANAGER
    # CONCEPTUAL_DICTIONARY


class ComputationalMethod(Context):
    defs = ObjectTypeDef(
        code="COMPUTATIONAL_METHOD",
        description="A ComputationalMethod is a context that specifies the model solved in a computation, such as "
        "density functional theory or an interatomic potential.",
        generated_code_prefix="COMP_METH",
        iri=["https://w3id.org/pmd/co/PMD_0000931"],
        prev_versions=["INTERATOMIC_POTENTIAL:v0"],
    )

    method_type = PropertyTypeAssignment(
        code="METHOD_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="METHOD_TYPE",
        property_label="Method type",
        description="Kind of computational method, such as density functional theory or a force field.",
        mandatory=False,
        section="Method Details",
    )

    is_spin_polarized = PropertyTypeAssignment(
        code="IS_SPIN_POLARIZED",
        data_type="BOOLEAN",
        property_label="Spin-polarized",
        description="Whether the two spin channels are treated separately.",
        mandatory=False,
        section="DFT Details",
        prev_versions=["ATOM_SPIN_POLARIZED:v0"],
    )

    non_collinear_magnetism = PropertyTypeAssignment(
        code="NON_COLLINEAR_MAGNETISM",
        data_type="BOOLEAN",
        property_label="Non-collinear magnetism",
        description="Whether the magnetic moments are allowed to point in arbitrary directions.",
        mandatory=False,
        section="DFT Details",
        prev_versions=["ATOM_NON_COLL_MAG:v0"],
    )

    reference_form = PropertyTypeAssignment(
        code="REFERENCE_FORM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="REFERENCE_FORM",
        property_label="Reference form",
        description="Kohn-Sham reference form used for the calculation.",
        mandatory=False,
        section="DFT Details",
    )

    xc_functional = PropertyTypeAssignment(
        code="XC_FUNCTIONAL",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="XC_FUNCTIONAL",
        property_label="Exchange-correlation functional",
        description="Exchange-correlation functional, such as PBE or HSE06.",
        mandatory=False,
        section="XC Functional",
        prev_versions=["ATOM_XC_FUNCTIONAL:v0"],
    )

    xc_components = PropertyTypeAssignment(
        code="XC_COMPONENTS",
        data_type="VARCHAR",
        property_label="XC components",
        description="LibXC labels of the components of the exchange-correlation functional, such as XC_GGA_X_PBE.",
        mandatory=False,
        section="XC Functional",
        multivalued=True,
    )

    jacobs_ladder = PropertyTypeAssignment(
        code="JACOBS_LADDER",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="JACOBS_LADDER",
        property_label="Jacob's ladder",
        description="Highest rung of Jacob's ladder among the components of the exchange-correlation functional.",
        mandatory=False,
        section="XC Functional",
    )

    global_exact_exchange = PropertyTypeAssignment(
        code="GLOBAL_EXACT_EXCHANGE",
        data_type="REAL",
        property_label="Global exact exchange",
        description="Global fraction of exact (Hartree-Fock) exchange mixed into the functional.",
        mandatory=False,
        section="XC Functional",
    )

    uses_libxc = PropertyTypeAssignment(
        code="USES_LIBXC",
        data_type="BOOLEAN",
        property_label="Uses LibXC",
        description="Whether the program evaluated the functional with the LibXC library rather than its own implementation.",
        mandatory=False,
        section="XC Functional",
    )

    relativity_level = PropertyTypeAssignment(
        code="RELATIVITY_LEVEL",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="RELATIVITY_LEVEL",
        property_label="Relativity level",
        description="Relativistic treatment of the valence electrons.",
        mandatory=False,
        section="Relativity",
    )

    relativity_approximation = PropertyTypeAssignment(
        code="RELATIVITY_APPROXIMATION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="RELATIVITY_APPROXIMATION",
        property_label="Relativity approximation",
        description="Approximation or decoupling scheme of the relativistic treatment.",
        mandatory=False,
        section="Relativity",
    )

    hubbard_correction = PropertyTypeAssignment(
        code="HUBBARD_CORRECTION",
        data_type="BOOLEAN",
        property_label="Hubbard correction",
        description="Whether a Hubbard (DFT+U) correction is applied.",
        mandatory=False,
        section="Hubbard Interactions",
        prev_versions=["ATOM_XC_U_CORRECTION:v0"],
    )

    hubbard_parameters = PropertyTypeAssignment(
        code="HUBBARD_PARAMETERS",
        data_type="JSON",
        property_label="Hubbard parameters",
        description="Hubbard interactions as a list with one entry per corrected orbital, with the keys orbital, u_effective, u_interaction, and j_hunds_coupling, with energies in eV.",
        mandatory=False,
        section="Hubbard Interactions",
    )

    double_counting_correction = PropertyTypeAssignment(
        code="DOUBLE_COUNTING_CORRECTION",
        data_type="VARCHAR",
        property_label="Double counting correction",
        description="Double counting correction scheme of the Hubbard interactions, such as Dudarev or Liechtenstein.",
        mandatory=False,
        section="Hubbard Interactions",
    )

    dispersion_model = PropertyTypeAssignment(
        code="DISPERSION_MODEL",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DISPERSION_MODEL",
        property_label="Dispersion model",
        description="Empirical dispersion correction added to the functional.",
        mandatory=False,
        section="Dispersion",
    )

    dispersion_damping = PropertyTypeAssignment(
        code="DISPERSION_DAMPING",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DISPERSION_DAMPING",
        property_label="Dispersion damping",
        description="Short-range damping function of the dispersion correction.",
        mandatory=False,
        section="Dispersion",
    )

    nonlocal_correlation = PropertyTypeAssignment(
        code="NONLOCAL_CORRELATION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="NONLOCAL_CORRELATION",
        property_label="Nonlocal correlation",
        description="Kernel-based nonlocal correlation term added to the functional.",
        mandatory=False,
        section="Dispersion",
    )

    potential_style = PropertyTypeAssignment(
        code="POTENTIAL_STYLE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="POTENTIAL_STYLE",
        property_label="Potential style",
        description="Functional form of the interatomic potential.",
        mandatory=False,
        section="Interatomic Potential Details",
        prev_versions=["ATOM_POTENTIAL_STYLE:v0"],
    )

    kim_id = PropertyTypeAssignment(
        code="KIM_ID",
        data_type="VARCHAR",
        property_label="OpenKIM ID",
        description="Identifier of the potential in the OpenKIM repository, such as EAM_Dynamo_Mendelev_2003_Fe__MO_546673549085_000.",
        mandatory=False,
        section="Interatomic Potential Details",
    )

    chemical_species = PropertyTypeAssignment(
        code="CHEMICAL_SPECIES",
        data_type="VARCHAR",
        property_label="Chemical species",
        description="Chemical species described by the entity, given as element symbols such as Fe or C.",
        mandatory=False,
        section="Interatomic Potential Details",
        multivalued=True,
        prev_versions=["CHEM_SPECIES_ADDRESSED:v0"],
    )

    link = PropertyTypeAssignment(
        code="LINK",
        data_type="HYPERLINK",
        property_label="Link",
        description="Website or download location of the entity, such as the project page or a repository.",
        mandatory=False,
        section="Interatomic Potential Details",
        prev_versions=["SOURCE_LINK:v0"],
    )

    software_compatibility = PropertyTypeAssignment(
        code="SOFTWARE_COMPATIBILITY",
        data_type="VARCHAR",
        property_label="Software compatibility",
        description="Software that can use the entity as input.",
        mandatory=False,
        section="Interatomic Potential Details",
        prev_versions=["SFTW_COMPATIBILITY:v0"],
    )

    # Properties from v0 that need to be migrated to v1 (from INTERATOMIC_POTENTIAL:v0):
    # REFERENCE


class HPC(MaterialEntity):
    defs = ObjectTypeDef(
        code="HPC",
        description="An HPC is a material entity consisting of a high-performance computing cluster "
        "used to execute computations.",
        generated_code_prefix="HPC",
        iri=["https://w3id.org/pmd/co/PMD_0000582"],
        prev_versions=["HPC:v0"],
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alias",
        description="Alternative name of the entity, such as an abbreviation or nickname.",
        mandatory=False,
        section="HPC Details",
        prev_versions=["ALIAS:v0"],
    )

    cpu_nodes_config = PropertyTypeAssignment(
        code="CPU_NODES_CONFIG",
        data_type="MULTILINE_VARCHAR",
        property_label="CPU node configuration",
        description="Configuration of the CPU nodes of the cluster, such as processor type, cores and memory per node.",
        mandatory=False,
        section="HPC Details",
        prev_versions=["CPU_NODES_CONFIG:v0"],
    )

    gpu_nodes_config = PropertyTypeAssignment(
        code="GPU_NODES_CONFIG",
        data_type="MULTILINE_VARCHAR",
        property_label="GPU node configuration",
        description="Configuration of the GPU nodes of the cluster, such as GPU type and number of GPUs per node.",
        mandatory=False,
        section="HPC Details",
        prev_versions=["GPU_NODES_CONFIG:v0"],
    )

    file_system_config = PropertyTypeAssignment(
        code="FILE_SYSTEM_CONFIG",
        data_type="MULTILINE_VARCHAR",
        property_label="File system configuration",
        description="Configuration of the file systems available on the cluster.",
        mandatory=False,
        section="HPC Details",
        prev_versions=["FILE_SYSTEM_CONFIG:v0"],
    )

    external_address = PropertyTypeAssignment(
        code="HPC_EXT_PHYS_ADDRESS",
        data_type="VARCHAR",
        property_label="External HPC address",
        description="Physical address of the cluster when it is operated by an external institution.",
        mandatory=False,
        section="HPC Details",
        prev_versions=["HPC_EXT_PHYS_ADDRESS:v0"],
    )

    external_contact = PropertyTypeAssignment(
        code="HPC_EXT_EMAIL_ADDRESS",
        data_type="VARCHAR",
        property_label="External HPC contact",
        description="Email address or point of contact of the cluster when it is operated by an external institution.",
        mandatory=False,
        section="HPC Details",
        prev_versions=["HPC_EXT_EMAIL_ADDRESS:v0"],
    )

    # Properties from v0 that need to be migrated to v1 (from HPC:v0):
    # OPERATING_SYSTEM
    # QUEUING_SYSTEM
    # RESPONSIBLE_PERSON
    # CO_RESPONSIBLE_PERSON
    # REFERENCE


class InputSpecification(Context):
    defs = ObjectTypeDef(
        code="INPUT_SPECIFICATION",
        description="An InputSpecification is a context that bundles the input prescriptions of a computation, "
        "with the concrete parameter values given to it. It is referenced by the computation, so the same "
        "specification can be reused by several computations.",
        generated_code_prefix="IN_SPEC",
        # PMD_0000014 prescribes a single required input data item; this type bundles several such prescriptions
        # with their values. The IRI is a broad association at a coarser granularity, not an identity.
        iri=["https://w3id.org/pmd/co/PMD_0000014"],
    )


# --- Specifications for atomistic simulations ---


class ElectronicStructureParameters(InputSpecification):
    defs = ObjectTypeDef(
        code="ELECTRONIC_STRUCTURE_PARAMETERS",
        description="ElectronicStructureParameters is an input specification with the computational setup used to "
        "solve the electronic structure: the pseudopotential or PAW datasets, the basis-set cutoff, the "
        "Brillouin-zone sampling, the occupations, and the self-consistent field convergence. The datasets also "
        "affect the physical approximation, not only the numerics. The physical model itself (functional, spin "
        "treatment, DFT+U) is a ComputationalMethod.",
        generated_code_prefix="EL_PARAM",
    )

    pseudopotentials = PropertyTypeAssignment(
        code="PSEUDOPOTENTIALS",
        data_type="OBJECT",
        object_code="PSEUDOPOTENTIAL",
        property_label="Pseudopotentials",
        description="Pseudopotentials or PAW datasets used, one per chemical species (VASP: POTCAR).",
        mandatory=False,
        section="Pseudopotentials",
        multivalued=True,
    )

    plane_wave_cutoff = PropertyTypeAssignment(
        code="PLANE_WAVE_CUTOFF",
        data_type="REAL",
        property_label="Plane-wave cutoff",
        units="eV",
        description="Kinetic-energy cutoff of the plane-wave basis set for the wave functions (VASP: ENCUT). "
        "Only for plane-wave codes.",
        mandatory=False,
        section="Basis Set",
        iri=["https://purls.helmholtz-metadaten.de/asmo/EnergyCutoff"],
        prev_versions=["ATOM_E_CUTOFF_IN_EV:v0"],
    )

    kpoint_mesh_type = PropertyTypeAssignment(
        code="KPOINT_MESH_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="KPOINT_MESH_TYPE",
        property_label="K-point mesh type",
        description="How the k-points sampling the Brillouin zone are placed, such as a Gamma-centered or a "
        "Monkhorst-Pack mesh.",
        mandatory=False,
        section="Brillouin Zone Sampling",
        iri=["https://purls.helmholtz-metadaten.de/asmo/KPointMesh"],
        # v0 ATOM_KPOINT_TYPE mixes how the mesh was generated (KPOINTS_KSPACING) with how it is placed. A mesh
        # generated from KSPACING can be Gamma-centered or Monkhorst-Pack (VASP: KGAMMA), so the term must be
        # derived from the v0 type together with ATOM_KPT_GAMMA_CENT or the raw KPOINTS / INCAR. Leave the
        # property unset if the centering cannot be determined.
        prev_versions=["ATOM_KPOINT_TYPE:v0"],
    )

    kpoint_mesh_b1 = PropertyTypeAssignment(
        code="KPOINT_MESH_B1",
        data_type="INTEGER",
        property_label="K-point subdivisions along b1",
        description="Number of subdivisions of the k-point mesh along the first reciprocal lattice vector b1.",
        mandatory=False,
        section="Brillouin Zone Sampling",
        # v0 used x/y/z wording; check that these were the three mesh indices along b1/b2/b3 before migrating.
        prev_versions=["ATOMISTIC_N_KPT_X:v0"],
    )

    kpoint_mesh_b2 = PropertyTypeAssignment(
        code="KPOINT_MESH_B2",
        data_type="INTEGER",
        property_label="K-point subdivisions along b2",
        description="Number of subdivisions of the k-point mesh along the second reciprocal lattice vector b2.",
        mandatory=False,
        section="Brillouin Zone Sampling",
        prev_versions=["ATOMISTIC_N_KPT_Y:v0"],
    )

    kpoint_mesh_b3 = PropertyTypeAssignment(
        code="KPOINT_MESH_B3",
        data_type="INTEGER",
        property_label="K-point subdivisions along b3",
        description="Number of subdivisions of the k-point mesh along the third reciprocal lattice vector b3.",
        mandatory=False,
        section="Brillouin Zone Sampling",
        prev_versions=["ATOMISTIC_N_KPT_Z:v0"],
    )

    kpoint_spacing = PropertyTypeAssignment(
        code="KPOINT_SPACING",
        data_type="REAL",
        property_label="K-point spacing",
        units="1/angstrom",
        description="Requested k-point spacing, if the mesh was generated from a spacing (VASP: KSPACING). With "
        "the VASP convention, the number of subdivisions along each reciprocal lattice vector b_i (b_i . a_j = "
        "delta_ij, without the factor 2 pi) is N_i = max(1, ceil(2 pi |b_i| / KSPACING)), so the realized interval "
        "2 pi |b_i| / N_i is at most this value. Codes that define the spacing without the factor 2 pi (|b_i| / "
        "N_i) give values smaller by 2 pi; convert before comparing across codes. The realized subdivisions are "
        "KPOINT_MESH_B1 to B3.",
        mandatory=False,
        section="Brillouin Zone Sampling",
        prev_versions=["ATOMISTIC_KPT_SPACIN_IN_1_A:v0"],
    )

    symmetry_usage = PropertyTypeAssignment(
        code="SYMMETRY_USAGE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="SYMMETRY_USAGE",
        property_label="Symmetry usage",
        description="Which symmetries are used to reduce the k-point sampling and to symmetrize quantities "
        "(VASP: ISYM).",
        mandatory=False,
        section="Brillouin Zone Sampling",
    )

    occupation_scheme = PropertyTypeAssignment(
        code="OCCUPATION_SCHEME",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="OCCUPATION_SCHEME",
        property_label="Occupation scheme",
        description="Method used to set the (partial) occupations of the Kohn-Sham orbitals, such as Gaussian "
        "smearing or the tetrahedron method (VASP: ISMEAR).",
        mandatory=False,
        section="Occupations",
        prev_versions=["ELECTRONIC_SMEARING:v0"],
    )

    smearing_width = PropertyTypeAssignment(
        code="SMEARING_WIDTH",
        data_type="REAL",
        property_label="Smearing width",
        units="eV",
        description="Width of the smearing function (VASP: SIGMA). For Fermi-Dirac smearing it equals the "
        "electronic temperature times the Boltzmann constant. Not used by the tetrahedron methods without smearing.",
        mandatory=False,
        section="Occupations",
        prev_versions=["ATOM_SIGMA_IN_EV:v0"],
    )

    methfessel_paxton_order = PropertyTypeAssignment(
        code="METHFESSEL_PAXTON_ORDER",
        data_type="INTEGER",
        property_label="Methfessel-Paxton order",
        description="Order of the Methfessel-Paxton expansion, if that occupation scheme is used (VASP: the "
        "positive value of ISMEAR).",
        mandatory=False,
        section="Occupations",
    )

    n_bands = PropertyTypeAssignment(
        code="N_BANDS",
        data_type="INTEGER",
        property_label="Number of bands",
        description="Number of Kohn-Sham orbitals computed at each k-point (VASP: NBANDS). For a later LOBSTER "
        "projection, the atomate2 workflow sets it to the number of local basis functions of the largest basis set "
        "it tests.",
        mandatory=False,
        section="Self-Consistent Field",
    )

    electronic_algorithm = PropertyTypeAssignment(
        code="ELECTRONIC_ALGORITHM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="ELECTRONIC_ALGORITHM",
        property_label="Electronic algorithm",
        description="Algorithm used to optimize the Kohn-Sham orbitals in the self-consistent field cycle "
        "(VASP: ALGO).",
        mandatory=False,
        section="Self-Consistent Field",
        prev_versions=["ATOM_ELEC_MIN_ALGO:v0"],
    )

    scf_energy_convergence = PropertyTypeAssignment(
        code="SCF_ENERGY_CONVERGENCE",
        data_type="REAL",
        property_label="SCF energy convergence threshold",
        units="eV",
        description="The self-consistent field cycle stops when the total energy changes by less than this value "
        "between two iterations (VASP: EDIFF; VASP also requires the change of the band-structure energy to be "
        "below it).",
        mandatory=False,
        section="Self-Consistent Field",
        prev_versions=["ATOM_EL_E_TOL_IN_EV:v0"],
    )

    max_scf_iterations = PropertyTypeAssignment(
        code="MAX_SCF_ITERATIONS",
        data_type="INTEGER",
        property_label="Maximum number of SCF iterations",
        description="Largest number of self-consistent field iterations per ionic step (VASP: NELM).",
        mandatory=False,
        section="Self-Consistent Field",
    )

    initial_wavefunctions_reused = PropertyTypeAssignment(
        code="INITIAL_WAVEFUNCTIONS_REUSED",
        data_type="BOOLEAN",
        property_label="Initial wave functions from a previous run",
        description="Whether the initial wave functions are read from a previous calculation.",
        mandatory=False,
        section="Self-Consistent Field",
        prev_versions=["ATOM_WAVEFUNC_REUSE:v0"],
    )

    initial_density_reused = PropertyTypeAssignment(
        code="INITIAL_DENSITY_REUSED",
        data_type="BOOLEAN",
        property_label="Initial charge density from a previous run",
        description="Whether the initial charge density is read from a previous calculation.",
        mandatory=False,
        section="Self-Consistent Field",
        prev_versions=["ATOM_CHGDENS_REUSE:v0"],
    )

    # Not migrated from v0 PYIRON_JOB.VASP:
    # ATOM_XC_FUNCTIONAL, ATOM_XC_U_CORRECTION, ATOM_SPIN_POLARIZED, ATOM_NON_COLL_MAG (part of the physical model:
    #   ComputationalMethod XC_FUNCTIONAL, HUBBARD_CORRECTION, IS_SPIN_POLARIZED, NON_COLLINEAR_MAGNETISM)
    # ATOM_KPT_GAMMA_CENT (combined with ATOM_KPOINT_TYPE into KPOINT_MESH_TYPE; see there)
    # ATOMISTIC_KPT_FULL (explicit k-point lists should be attached as a file; the migration must actually attach
    #   it, otherwise the list is lost)


class GeometryOptimizationParameters(InputSpecification):
    defs = ObjectTypeDef(
        code="GEOMETRY_OPTIMIZATION_PARAMETERS",
        description="GeometryOptimizationParameters is an input specification that states which degrees of freedom "
        "of a structure may relax, the algorithm that moves them, and when the optimization counts as converged.",
        generated_code_prefix="GEO_OPT_PARAM",
    )

    # v0 had three booleans (ATOM_POS_RELAX, ATOM_CELL_SHP_RELAX, ATOM_CELL_VOL_RELAX). They are one multivalued
    # vocabulary here, following ASMO RelaxationDOF; a v0 value of True maps to the corresponding term.
    relaxation_degrees_of_freedom = PropertyTypeAssignment(
        code="RELAXATION_DEGREES_OF_FREEDOM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="RELAXATION_DEGREE_OF_FREEDOM",
        property_label="Relaxation degrees of freedom",
        description="Degrees of freedom of the structure that may change during the optimization: atomic "
        "positions, cell shape, cell volume.",
        mandatory=False,
        section="Degrees of Freedom",
        multivalued=True,
        iri=["https://purls.helmholtz-metadaten.de/asmo/RelaxationDOF"],
    )

    geometry_optimization_algorithm = PropertyTypeAssignment(
        code="GEOMETRY_OPTIMIZATION_ALGORITHM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="GEOMETRY_OPTIMIZATION_ALGORITHM",
        property_label="Geometry optimization algorithm",
        description="Algorithm used to move the nuclei, and the cell if allowed, towards a local energy minimum.",
        mandatory=False,
        section="Algorithm",
        prev_versions=["ATOM_IONIC_MIN_ALGO:v0"],
    )

    force_convergence = PropertyTypeAssignment(
        code="FORCE_CONVERGENCE",
        data_type="REAL",
        property_label="Force convergence threshold",
        units="eV/angstrom",
        description="The optimization stops when the force reduction given by FORCE_CONVERGENCE_NORM is below this "
        "value (VASP: absolute value of a negative EDIFFG; LAMMPS minimize: ftol). Thresholds for different "
        "reductions are not comparable.",
        mandatory=False,
        section="Convergence",
        # v0 ATOM_F_TOL_IN_EV_A was shared by VASP and LAMMPS jobs without stating the norm. Migrate the value
        # together with FORCE_CONVERGENCE_NORM: MAX_ATOM_NORM for VASP; for LAMMPS take the norm from the job's
        # min_modify settings (default GLOBAL_VECTOR_NORM). Leave the norm unset if the settings are not known.
        prev_versions=["ATOM_F_TOL_IN_EV_A:v0"],
    )

    force_convergence_norm = PropertyTypeAssignment(
        code="FORCE_CONVERGENCE_NORM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="FORCE_CONVERGENCE_NORM",
        property_label="Force convergence norm",
        description="Reduction of the atomic forces compared with the force convergence threshold, such as the "
        "largest per-atom force norm (VASP) or the norm of the 3N-dimensional force vector (LAMMPS default).",
        mandatory=False,
        section="Convergence",
    )

    ionic_energy_convergence = PropertyTypeAssignment(
        code="IONIC_ENERGY_CONVERGENCE",
        data_type="REAL",
        property_label="Ionic energy convergence threshold",
        units="eV",
        description="Absolute criterion: the optimization stops when the total energy changes by less than this "
        "value between two ionic steps (VASP: positive EDIFFG). For a relative criterion use "
        "IONIC_RELATIVE_ENERGY_CONVERGENCE.",
        mandatory=False,
        section="Convergence",
        # v0 ATOM_E_TOL_ION_IN_EV is labelled eV but was also used for LAMMPS, whose etol is relative. Migrate
        # values from VASP jobs here; values from LAMMPS jobs belong to IONIC_RELATIVE_ENERGY_CONVERGENCE after
        # checking what the exporter stored. Do not convert between the two.
        prev_versions=["ATOM_E_TOL_ION_IN_EV:v0"],
    )

    ionic_relative_energy_convergence = PropertyTypeAssignment(
        code="IONIC_RELATIVE_ENERGY_CONVERGENCE",
        data_type="REAL",
        property_label="Ionic relative energy convergence threshold",
        description="Dimensionless relative criterion: the optimization stops when the energy change between two "
        "iterations, divided by the magnitude of the energy, is below this value (LAMMPS minimize: etol).",
        mandatory=False,
        section="Convergence",
    )

    max_ionic_steps = PropertyTypeAssignment(
        code="MAX_IONIC_STEPS",
        data_type="INTEGER",
        property_label="Maximum number of ionic steps",
        description="Largest number of ionic steps the optimization may take (VASP: NSW; LAMMPS minimize: maxiter). "
        "A requested upper bound, distinct from N_IONIC_STEPS, the number actually carried out.",
        mandatory=False,
        section="Convergence",
        # Broad association: ASMO NumberOfIonicSteps is both an input and an output parameter, but its definition
        # describes the iterations performed. ASMO has no exact term for a maximum; the shared IRI with
        # N_IONIC_STEPS does not make the two values interchangeable.
        iri=["https://purls.helmholtz-metadaten.de/asmo/NumberOfIonicSteps"],
        prev_versions=["MAX_ITERS:v0"],
    )


class MolecularDynamicsParameters(InputSpecification):
    defs = ObjectTypeDef(
        code="MOLECULAR_DYNAMICS_PARAMETERS",
        description="MolecularDynamicsParameters is an input specification that states the statistical ensemble to "
        "be sampled, the target conditions, the integration time step and length, and the thermostat and barostat "
        "algorithms used to approach the ensemble.",
        generated_code_prefix="MD_PARAM",
    )

    # The ensemble is what the run is meant to sample; thermostat and barostat are the algorithms used for it.
    # Not every algorithm samples the intended ensemble exactly (see the vocabulary term descriptions).

    thermodynamic_ensemble = PropertyTypeAssignment(
        code="THERMODYNAMIC_ENSEMBLE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="THERMODYNAMIC_ENSEMBLE",
        property_label="Thermodynamic ensemble",
        description="Statistical ensemble the run is meant to sample, such as NVE, NVT, or NPT.",
        mandatory=False,
        section="Statistical Ensemble",
        iri=["https://purls.helmholtz-metadaten.de/asmo/StatisticalEnsemble"],
        prev_versions=["ATOM_MD_ENSEMBLE:v0"],
    )

    # Target conditions of the thermostat and barostat are given as start and end values. A ramp between them is
    # one supported protocol (such as LAMMPS fix nvt/npt Tstart/Tstop, Pstart/Pstop); equal values mean constant
    # conditions. The temperature used to draw the initial velocities is a separate input.

    velocity_initialization_temperature = PropertyTypeAssignment(
        code="VELOCITY_INITIALIZATION_TEMPERATURE",
        data_type="REAL",
        property_label="Velocity initialization temperature",
        units="K",
        description="Temperature of the Maxwell-Boltzmann distribution from which the initial velocities are "
        "drawn (LAMMPS: velocity create). Independent of the thermostat targets; for example, pyiron sets it to "
        "twice the first target temperature if not given. Not the measured instantaneous temperature at the start.",
        mandatory=False,
        section="Statistical Ensemble",
        # pyiron's initial_temperature is this velocity temperature. Check the exporter of each v0 record before
        # migrating.
        prev_versions=["ATOM_MD_INIT_TEMP_IN_K:v0"],
    )

    target_temperature_start = PropertyTypeAssignment(
        code="TARGET_TEMPERATURE_START",
        data_type="REAL",
        property_label="Target temperature at start",
        units="K",
        description="Target temperature of the thermostat at the start of the run (LAMMPS: Tstart).",
        mandatory=False,
        section="Statistical Ensemble",
    )

    target_temperature_end = PropertyTypeAssignment(
        code="TARGET_TEMPERATURE_END",
        data_type="REAL",
        property_label="Target temperature at end",
        units="K",
        description="Target temperature of the thermostat at the end of the run (LAMMPS: Tstop); equal to the start "
        "value for runs at constant temperature.",
        mandatory=False,
        section="Statistical Ensemble",
        # v0 ATOM_MD_TARG_TEMP_IN_K is a generic target, not established as a ramp endpoint. For a constant
        # target set both start and end; if the v0 job used a ramp, take both values from the job input.
        prev_versions=["ATOM_MD_TARG_TEMP_IN_K:v0"],
    )

    target_pressure_start = PropertyTypeAssignment(
        code="TARGET_PRESSURE_START",
        data_type="REAL",
        property_label="Target pressure at start",
        units="GPa",
        description="Hydrostatic target pressure of the barostat at the start of the run (LAMMPS: Pstart). A scalar "
        "describes only hydrostatic or equal-axis targets, not independently controlled stress components.",
        mandatory=False,
        section="Statistical Ensemble",
        # v0 ATOM_MD_INIT_PRESS_IN_GPA may be a barostat start target or a measured initial pressure. Migrate it
        # here only if the exporter shows it was Pstart; keep a measured value separately.
        prev_versions=["ATOM_MD_INIT_PRESS_IN_GPA:v0"],
    )

    target_pressure_end = PropertyTypeAssignment(
        code="TARGET_PRESSURE_END",
        data_type="REAL",
        property_label="Target pressure at end",
        units="GPa",
        description="Hydrostatic target pressure of the barostat at the end of the run (LAMMPS: Pstop); equal to "
        "the start value for runs at constant pressure.",
        mandatory=False,
        section="Statistical Ensemble",
        # As for TARGET_TEMPERATURE_END: a constant v0 target sets both start and end.
        prev_versions=["ATOM_TARG_PRESS_IN_GPA:v0"],
    )

    time_step = PropertyTypeAssignment(
        code="TIME_STEP",
        data_type="REAL",
        property_label="Time step",
        units="ps",
        description="Time step used to integrate the equations of motion of the nuclei (VASP: POTIM, given in fs, "
        "so divide by 1000; LAMMPS metal units: timestep, in ps).",
        mandatory=False,
        section="Integration",
        iri=["https://purls.helmholtz-metadaten.de/asmo/TimeStep"],
        prev_versions=["ATOM_MD_TIME_STP_IN_PS:v0"],
    )

    n_time_steps = PropertyTypeAssignment(
        code="N_TIME_STEPS",
        data_type="INTEGER",
        property_label="Number of time steps",
        description="Number of time steps to integrate (VASP: NSW).",
        mandatory=False,
        section="Integration",
    )

    simulated_time = PropertyTypeAssignment(
        code="SIMULATED_TIME",
        data_type="REAL",
        property_label="Simulated time",
        units="ps",
        description="Requested physical duration of the run, i.e. the requested number of time steps times the time "
        "step, assuming a constant time step. The duration actually reached can be shorter, for example if the run "
        "was interrupted; it follows from N_IONIC_STEPS of the MolecularDynamics.",
        mandatory=False,
        section="Integration",
        iri=["https://purls.helmholtz-metadaten.de/asmo/SimulationTime"],
        prev_versions=["ATOM_SIM_TIME_PS_IN_PS:v0"],
    )

    # v0 ATOM_MD_LANGEVIN (boolean) corresponds to THERMOSTAT = LANGEVIN; the type change prevents a direct link.
    thermostat = PropertyTypeAssignment(
        code="THERMOSTAT",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="THERMOSTAT",
        property_label="Thermostat",
        description="Algorithm used to control the temperature.",
        mandatory=False,
        section="Temperature Control",
        iri=["https://purls.helmholtz-metadaten.de/asmo/Thermostat"],
    )

    thermostat_time_constant = PropertyTypeAssignment(
        code="THERMOSTAT_TIME_CONSTANT",
        data_type="REAL",
        property_label="Thermostat time constant",
        units="ps",
        description="Characteristic relaxation time of the thermostat coupling. For Langevin dynamics, the damping "
        "time tau of the friction force -m v / tau (LAMMPS: damp), i.e. the inverse of a friction rate gamma in "
        "-m gamma v. If the friction is given as a coefficient zeta in -zeta v, the time is m / zeta instead.",
        mandatory=False,
        section="Temperature Control",
    )

    barostat = PropertyTypeAssignment(
        code="BAROSTAT",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAROSTAT",
        property_label="Barostat",
        description="Algorithm used to control the pressure.",
        mandatory=False,
        section="Pressure Control",
        iri=["https://purls.helmholtz-metadaten.de/asmo/Barostat"],
    )

    barostat_time_constant = PropertyTypeAssignment(
        code="BAROSTAT_TIME_CONSTANT",
        data_type="REAL",
        property_label="Barostat time constant",
        units="ps",
        description="Characteristic relaxation time of the barostat coupling.",
        mandatory=False,
        section="Pressure Control",
    )

    pressure_coupling = PropertyTypeAssignment(
        code="PRESSURE_COUPLING",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="PRESSURE_COUPLING",
        property_label="Pressure coupling",
        description="Which cell degrees of freedom the barostat may change.",
        mandatory=False,
        section="Pressure Control",
    )


# --- Specifications for analyses ---


class EquationOfStateFitParameters(InputSpecification):
    defs = ObjectTypeDef(
        code="EQUATION_OF_STATE_FIT_PARAMETERS",
        description="EquationOfStateFitParameters is an input specification that states the equation of state "
        "fitted to energy-volume data, which computed energy is fitted, and how the volumes were sampled.",
        generated_code_prefix="EOS_PARAM",
    )

    equation_of_state = PropertyTypeAssignment(
        code="EQUATION_OF_STATE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="EQUATION_OF_STATE",
        property_label="Equation of state",
        description="Equation-of-state model fitted to the energy-volume data, such as Birch-Murnaghan or Vinet. "
        "It identifies the fitting model or algorithm family, not the fit activity itself.",
        mandatory=False,
        section="Fit",
        # ASMO EquationOfStateFit is a SimulationAlgorithm whose individuals (Murnaghan, BirchMurnaghan, Vinet) are
        # the vocabulary terms; the IRI groups them, it is not an identity with this property.
        iri=["https://purls.helmholtz-metadaten.de/asmo/EquationOfStateFit"],
        prev_versions=["MURN_EQN_OF_STATE:v0"],
    )

    equation_of_state_order = PropertyTypeAssignment(
        code="EQUATION_OF_STATE_ORDER",
        data_type="INTEGER",
        property_label="Fit order",
        description="Order of the fitted polynomial, or order of the finite-strain expansion for Birch-Murnaghan "
        "and Poirier-Tarantola (such as 3 for third order). Its meaning depends on EQUATION_OF_STATE.",
        mandatory=False,
        section="Fit",
        # v0 MURN_FIT_EQN_ORDER is the polynomial degree only (pyiron fit_order), and is set even for analytic
        # fits. Migrate it only for EOS_POLYNOMIAL fits; for analytic forms take the order from the implementation
        # (pymatgen implements fixed third-order Birch-Murnaghan), not from the old input.
        prev_versions=["MURN_FIT_EQN_ORDER:v0"],
    )

    fitted_energy = PropertyTypeAssignment(
        code="FITTED_ENERGY",
        data_type="VARCHAR",
        property_label="Fitted energy",
        description="Which computed energy is fitted, such as the total energy extrapolated to zero smearing or "
        "the potential energy of a force field. Fits to different energies give different results.",
        mandatory=False,
        section="Fit",
    )

    n_volumes = PropertyTypeAssignment(
        code="EOS_N_VOLUMES",
        data_type="INTEGER",
        property_label="Number of volumes",
        description="Number of cell volumes, i.e. energy-volume data points.",
        mandatory=False,
        section="Volume Sampling",
        prev_versions=["MURN_N_DATA_POINTS:v0"],
    )

    relative_volume_range = PropertyTypeAssignment(
        code="EOS_RELATIVE_VOLUME_RANGE",
        data_type="REAL",
        property_label="Relative volume range",
        description="Largest relative change of the volume: the volumes span (1 - r) to (1 + r) times the "
        "reference volume, such as 0.1 for plus or minus 10 percent.",
        mandatory=False,
        section="Volume Sampling",
        iri=["https://purls.helmholtz-metadaten.de/asmo/VolumeRange"],
        prev_versions=["MURN_STRAINVOL_RANGE:v0"],
    )

    strain_axes = PropertyTypeAssignment(
        code="EOS_STRAIN_AXES",
        data_type="VARCHAR",
        property_label="Strain axes",
        description="Axes along which the cell is strained to change its volume, as given to the workflow; "
        "straining along all three axes scales the cell isotropically, which still constrains its shape. Whether "
        "the fitted curvature is the hydrostatic bulk modulus depends on which cell-shape and internal degrees of "
        "freedom were relaxed at fixed volume, as recorded by the relaxation degrees of freedom of the parent "
        "simulations, not on the strain axes alone.",
        mandatory=False,
        section="Volume Sampling",
        prev_versions=["MURN_STRAIN_AXES:v0"],
    )


class OrbitalProjectionParameters(InputSpecification):
    defs = ObjectTypeDef(
        code="ORBITAL_PROJECTION_PARAMETERS",
        description="OrbitalProjectionParameters is an input specification that states the auxiliary local "
        "atomic-orbital basis onto which wave functions are projected.",
        generated_code_prefix="ORB_PROJ_PARAM",
    )

    basis_set = PropertyTypeAssignment(
        code="LOCAL_BASIS_SET",
        data_type="VARCHAR",
        property_label="Local basis set",
        description="Name of the auxiliary local atomic-orbital basis set used for the projection, such as "
        "pbeVaspFit2015 or Bunge.",
        mandatory=False,
        section="Local Basis",
    )

    basis_functions = PropertyTypeAssignment(
        code="LOCAL_BASIS_FUNCTIONS",
        data_type="VARCHAR",
        property_label="Local basis functions",
        description="Atomic orbitals included in the projection for one chemical species, given as the element "
        "symbol followed by the orbitals, such as Ga 3d 4s 4p. One value per chemical species.",
        mandatory=False,
        section="Local Basis",
        multivalued=True,
    )


class ProjectionQualityParameters(InputSpecification):
    defs = ObjectTypeDef(
        code="PROJECTION_QUALITY_PARAMETERS",
        description="ProjectionQualityParameters is an input specification with the thresholds and comparison "
        "settings used to judge an orbital projection.",
        generated_code_prefix="PROJ_QUAL_PARAM",
    )

    band_overlap_deviation_limit = PropertyTypeAssignment(
        code="BAND_OVERLAP_DEVIATION_LIMIT",
        data_type="REAL",
        property_label="Band overlap deviation limit",
        description="Threshold for the maximal deviation of the band overlap matrix from the identity at a single "
        "k-point, such as 0.1.",
        mandatory=False,
        section="Orthonormality Check",
    )

    pdos_comparison_energy_min = PropertyTypeAssignment(
        code="PDOS_COMPARISON_ENERGY_MIN",
        data_type="REAL",
        property_label="PDOS comparison energy minimum",
        units="eV",
        description="Requested lower bound, relative to the Fermi level, of the energy range used for the PDOS "
        "comparison. The implementation may clip it to the available energies.",
        mandatory=False,
        section="PDOS Comparison",
    )

    pdos_comparison_energy_max = PropertyTypeAssignment(
        code="PDOS_COMPARISON_ENERGY_MAX",
        data_type="REAL",
        property_label="PDOS comparison energy maximum",
        units="eV",
        description="Requested upper bound, relative to the Fermi level, of the energy range used for the PDOS "
        "comparison. The implementation may clip it to the available energies.",
        mandatory=False,
        section="PDOS Comparison",
    )

    pdos_comparison_n_bins = PropertyTypeAssignment(
        code="PDOS_COMPARISON_N_BINS",
        data_type="INTEGER",
        property_label="PDOS comparison number of bins",
        description="Requested number of energy bins of the fingerprints used for the PDOS comparison. The "
        "similarity values depend on it. LobsterPy caps the requested value, so the number actually used can "
        "be smaller.",
        mandatory=False,
        section="PDOS Comparison",
    )


class BondingAnalysisParameters(InputSpecification):
    defs = ObjectTypeDef(
        code="BONDING_ANALYSIS_PARAMETERS",
        description="BondingAnalysisParameters is an input specification that states which orbital-pair bonding "
        "indicators and population analyses are computed, for which atom pairs, and on which energy grid.",
        generated_code_prefix="BOND_PARAM",
    )

    bonding_indicators = PropertyTypeAssignment(
        code="BONDING_INDICATORS",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BONDING_INDICATOR",
        property_label="Bonding indicators",
        description="Bonding indicators computed for the selected atom pairs, such as COHP, COOP, or COBI.",
        mandatory=False,
        section="Indicators",
        multivalued=True,
    )

    population_analyses = PropertyTypeAssignment(
        code="POPULATION_ANALYSES",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="POPULATION_ANALYSIS",
        property_label="Population analyses",
        description="Population analyses used to obtain atomic gross populations and charges, such as Mulliken "
        "or Loewdin.",
        mandatory=False,
        section="Indicators",
        multivalued=True,
    )

    pair_distance_min = PropertyTypeAssignment(
        code="BONDING_PAIR_DISTANCE_MIN",
        data_type="REAL",
        property_label="Minimum pair distance",
        units="angstrom",
        description="Shortest interatomic distance for which atom pairs are included "
        "(lower bound of the LOBSTER keyword cohpGenerator).",
        mandatory=False,
        section="Atom Pairs",
    )

    pair_distance_max = PropertyTypeAssignment(
        code="BONDING_PAIR_DISTANCE_MAX",
        data_type="REAL",
        property_label="Maximum pair distance",
        units="angstrom",
        description="Longest interatomic distance for which atom pairs are included "
        "(upper bound of the LOBSTER keyword cohpGenerator).",
        mandatory=False,
        section="Atom Pairs",
    )

    # Relative to the Fermi level as in pymatgen Lobsterin.standard_with_energy_range_from_vasprun, which sets both
    # bounds from complete_dos.energies - complete_dos.efermi. Not yet confirmed against the current LOBSTER manual.
    energy_window_start = PropertyTypeAssignment(
        code="BONDING_ENERGY_WINDOW_START",
        data_type="REAL",
        property_label="Energy window start",
        units="eV",
        description="Lower bound, relative to the Fermi level of the input calculation (zero at the Fermi level), "
        "of the energy range in which the energy-resolved bonding indicators are evaluated (LOBSTER keyword "
        "COHPstartEnergy).",
        mandatory=False,
        section="Energy Grid",
    )

    energy_window_end = PropertyTypeAssignment(
        code="BONDING_ENERGY_WINDOW_END",
        data_type="REAL",
        property_label="Energy window end",
        units="eV",
        description="Upper bound, relative to the Fermi level of the input calculation (zero at the Fermi level), "
        "of the energy range in which the energy-resolved bonding indicators are evaluated (LOBSTER keyword "
        "COHPendEnergy).",
        mandatory=False,
        section="Energy Grid",
    )

    n_energy_points = PropertyTypeAssignment(
        code="BONDING_N_ENERGY_POINTS",
        data_type="INTEGER",
        property_label="Number of energy points",
        description="Number of energy points at which the energy-resolved bonding indicators are evaluated "
        "(LOBSTER keyword COHPSteps).",
        mandatory=False,
        section="Energy Grid",
    )

    gaussian_smearing_width = PropertyTypeAssignment(
        code="GAUSSIAN_SMEARING_WIDTH",
        data_type="REAL",
        property_label="Gaussian smearing width",
        units="eV",
        description="Width of the Gaussian broadening applied to the energy-resolved quantities "
        "(LOBSTER keyword gaussianSmearingWidth).",
        mandatory=False,
        section="Energy Grid",
    )


class BondingEnvironmentParameters(InputSpecification):
    defs = ObjectTypeDef(
        code="BONDING_ENVIRONMENT_PARAMETERS",
        description="BondingEnvironmentParameters is an input specification that states which bonds are considered "
        "and how relevant bonds are selected when coordination environments are derived from integrated bonding "
        "indicators.",
        generated_code_prefix="BOND_ENV_PARAM",
    )

    bond_selection = PropertyTypeAssignment(
        code="BOND_SELECTION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BOND_SELECTION",
        property_label="Bond selection",
        description="Kinds of atom pairs included, such as only cation-anion bonds or all bonds.",
        mandatory=False,
        section="Bond Selection",
    )

    valence_assignment = PropertyTypeAssignment(
        code="VALENCE_ASSIGNMENT_SCHEME",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="VALENCE_ASSIGNMENT_SCHEME",
        property_label="Valence assignment",
        description="Source of the atomic valences used to classify atoms as cations or anions.",
        mandatory=False,
        section="Bond Selection",
    )

    icohp_relative_cutoff = PropertyTypeAssignment(
        code="ICOHP_RELATIVE_CUTOFF",
        data_type="REAL",
        property_label="Relative ICOHP cutoff",
        description="Dimensionless fraction (such as 0.1) applied to bonding magnitudes: a neighbour is not counted "
        "when determining coordination environments if the magnitude |ICOHP| of its bonding interaction is below "
        "this fraction of the largest bonding |ICOHP|. Since bonding ICOHP values are negative, a smaller magnitude "
        "is a less negative value. The reference interaction is taken from the pairs allowed by BOND_SELECTION "
        "(LobsterPy: adapt_extremum_to_add_cond). In LobsterPy both the reference and the compared values are "
        "spin-summed ICOHPs, independent of SPINS_SUMMED.",
        mandatory=False,
        section="Bond Selection",
    )

    bonding_energy_lower_limit = PropertyTypeAssignment(
        code="BONDING_ENERGY_LOWER_LIMIT",
        data_type="REAL",
        property_label="Lower energy limit for bonding fractions",
        units="eV",
        description="Lower energy limit, relative to the Fermi level, for evaluating the bonding and antibonding "
        "fractions of each bond. Not set if all states below the Fermi level are included.",
        mandatory=False,
        section="Evaluation",
    )

    spins_summed = PropertyTypeAssignment(
        code="SPINS_SUMMED",
        data_type="BOOLEAN",
        property_label="Spin channels summed",
        description="Whether the two spin channels are summed in the COHP curves collected for the relevant bonds "
        "(LobsterPy: summed_spins). It does not affect the selection of relevant neighbours, which in LobsterPy "
        "always uses spin-summed ICOHPs.",
        mandatory=False,
        section="Evaluation",
    )

    orbital_resolved = PropertyTypeAssignment(
        code="ORBITAL_RESOLVED",
        data_type="BOOLEAN",
        property_label="Orbital resolved",
        description="Whether the relevant bonds are additionally analysed per orbital pair.",
        mandatory=False,
        section="Evaluation",
    )
