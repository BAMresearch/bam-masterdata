from bam_masterdata.datamodel.v1.base_objects import Entity
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment

# Hierarchy of the Entity branch of datamodel/v1:

#   Entity                          (see `base_objects.py`)
#   ├── Context
#   │   ├── Software
#   │   ├── WorkflowDefinition
#   │   ├── Pseudopotential
#   │   ├── SimulatedSystem
#   │   └── ComputationalMethod
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
