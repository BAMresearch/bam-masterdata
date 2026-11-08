from bam_masterdata.datamodel.v1.base_objects import Activity
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment

# IRI convention: object type iri = exact match of the class;
# property iri = class of the quantity the value is an instance of;
# vocabulary term iri = the individual of the vocabulary's class.

# Hierarchy of the Activity branch of datamodel/v1:

#   Activity                        (see `base_objects.py`)
#   ├── Computation
#   │   ├── Analysis
#   │   │   ├── CreepTestDataProcessing
#   │   │   └── SimulationAnalysis
#   │   │       ├── LocalOrbitalBondingAnalysis
#   │   │       ├── ProjectionQualityAssessment
#   │   │       ├── BondingEnvironmentAnalysis
#   │   │       └── EquationOfStateFit
#   │   └── Simulation
#   │       └── AtomisticSimulation
#   │           ├── SinglePointCalculation
#   │           ├── GeometryOptimization
#   │           └── MolecularDynamics
#   └── Experiment
#       ├── Processing
#       ├── Measurement
#       ├── Calibration
#       ├── Synthesis
#       └── Test


class Computation(Activity):
    defs = ObjectTypeDef(
        code="COMPUTATION",
        description="A Computation is an activity that executes computational methods to process information "
        "or perform calculations.",
        generated_code_prefix="COMPUT",
        prev_versions=["COMPUTATIONAL_ANALYSIS:v0"],
        iri=["https://w3id.org/pmd/co/PMD_0000583"],
    )

    software = PropertyTypeAssignment(
        code="SOFTWARE",
        data_type="OBJECT",
        object_code="SOFTWARE",
        property_label="Software",
        description="Software used to perform the computation",
        mandatory=False,
        section="Computation Details",
        prev_versions=["CREEP_TEST_SOFTWARE:v0", "WORKFLOW_MANAGER:v0"],
    )

    computational_method = PropertyTypeAssignment(
        code="COMPUTATIONAL_METHOD",
        data_type="OBJECT",
        object_code="COMPUTATIONAL_METHOD",
        property_label="Computational method",
        description="Computational methods applied during the computation, such as density functional "
        "theory or molecular dynamics.",
        mandatory=False,
        section="Computation Details",
        multivalued=True,
    )

    # Properties from v0 that need to be migrated to v1:
    # SOURCE_CODE_LANGUAGE


class Analysis(Computation):
    defs = ObjectTypeDef(
        code="ANALYSIS",
        description="An Analysis is a computation that examines one or more existing inputs to derive "
        "information, properties, parameters, or other outputs.",
        generated_code_prefix="ANALY",
    )

    primary_data_series = PropertyTypeAssignment(
        code="PRIMARY_DATA_SERIES",
        data_type="MULTILINE_VARCHAR",
        property_label="Primary data series",
        description="Description of the original data series used in the analysis, "
        "including measured quantities and units.",
        mandatory=False,
        section="Analysis Details",
        prev_versions=["CREEP_TEST_PRIMARY_DATA_SERIES:v0"],
    )

    processed_data_series = PropertyTypeAssignment(
        code="PROCESSED_DATA_SERIES",
        data_type="MULTILINE_VARCHAR",
        property_label="Processed data series",
        description="Description of the data series produced by the analysis, "
        "including derived quantities and units.",
        mandatory=False,
        section="Analysis Details",
        prev_versions=["CREEP_TEST_PROCESSED_DATA_SERIES:v0"],
    )

    analysis_procedure = PropertyTypeAssignment(
        code="ANALYSIS_PROCEDURE",
        data_type="MULTILINE_VARCHAR",
        property_label="Analysis procedure",
        description="Description of the methods or operations applied to the input "
        "data to obtain the analysis results.",
        mandatory=False,
        section="Analysis Details",
        prev_versions=["CREEP_TEST_ANALYSIS_PROCEDURE:v0"],
    )

    automated_workflow = PropertyTypeAssignment(
        code="AUTOMATED_WORKFLOW",
        data_type="BOOLEAN",
        property_label="Automated workflow",
        description="Whether the analysis was performed using an automated computational workflow.",
        mandatory=False,
        section="Analysis Details",
        prev_versions=["CREEP_TEST_WORKFLOW_USAGE:v0"],
    )


class CreepTestDataProcessing(Analysis):
    defs = ObjectTypeDef(
        code="CREEP_TEST_DATA_PROCESSING",
        description="A CreepTestDataProcessing is an analysis that transforms or evaluates data acquired "
        "during creep testing to derive material properties or characterize creep behavior.",
        generated_code_prefix="CREEP_DATA_PROC",
        prev_versions=[
            "COMPUTATIONAL_ANALYSIS.CREEP_TEST_DATA_PROCESSING_PROCEDURES:v0"
        ],
    )


class Simulation(Computation):
    defs = ObjectTypeDef(
        code="SIMULATION",
        description="A Simulation is a computation that uses one or more computational models to "
        "reproduce, predict, or explore the behavior of a system under specified conditions.",
        generated_code_prefix="SIMUL",
        iri=[
            "https://purls.helmholtz-metadaten.de/asmo/Simulation",
            "https://w3id.org/pmd/co/PMD_0000933",
        ],
        prev_versions=["PYIRON_JOB:v0"],
    )

    simulated_system = PropertyTypeAssignment(
        code="SIMULATED_SYSTEM",
        data_type="OBJECT",
        object_code="SIMULATED_SYSTEM",
        property_label="Simulated system",
        description="System being simulated, from atomistic to continuum scale",
        mandatory=False,
        section="Simulation Details",
        multivalued=True,
    )

    walltime = PropertyTypeAssignment(
        code="WALLTIME",
        data_type="REAL",
        property_label="Walltime",
        units="h",
        description="Elapsed time between the start and end of simulation execution.",
        mandatory=False,
        section="Execution Details",
        prev_versions=["SIM_WALLTIME_IN_HOURS:v0"],
    )

    core_time = PropertyTypeAssignment(
        code="CORE_TIME",
        data_type="REAL",
        property_label="Core time",
        units="h",
        description="Total CPU time consumed by the simulation, expressed in core-hours.",
        mandatory=False,
        section="Execution Details",
        prev_versions=["SIM_CORETIME_IN_HOURS:v0"],
    )

    n_cores = PropertyTypeAssignment(
        code="N_CORES",
        data_type="INTEGER",
        property_label="Number of cores",
        description="Number of CPU cores allocated to the simulation.",
        mandatory=False,
        section="Execution Details",
        prev_versions=["NCORES:v0"],
    )

    n_gpus = PropertyTypeAssignment(
        code="N_GPUS",
        data_type="INTEGER",
        property_label="Number of GPUs",
        description="Number of GPUs allocated to the simulation.",
        mandatory=False,
        section="Execution Details",
        prev_versions=["NGPUS:v0"],
    )

    n_threads = PropertyTypeAssignment(
        code="N_THREADS",
        data_type="INTEGER",
        property_label="Number of threads",
        description="Number of execution threads configured for the simulation.",
        mandatory=False,
        section="Execution Details",
        prev_versions=["NTHREADS:v0"],
    )

    hpc_job_queue = PropertyTypeAssignment(
        code="HPC_JOB_QUEUE",
        data_type="VARCHAR",
        property_label="HPC job queue",
        description="Name of the HPC scheduler queue or partition used to execute the simulation.",
        mandatory=False,
        section="Execution Details",
        prev_versions=["HPC_JOB_QUEUE:v0"],
    )

    hpc_job_id = PropertyTypeAssignment(
        code="HPC_JOB_ID",
        data_type="VARCHAR",
        property_label="HPC job ID",
        description="Identifier assigned to the simulation by an HPC job scheduler.",
        mandatory=False,
        section="Execution Details",
        prev_versions=["HPC_JOB_ID:v0"],
    )

    # Properties from v0 that need to be migrated to v1 (from PYIRON_JOB:v0):
    # BAM_USERNAME
    # CONCEPTUAL_DICTIONARY


# --- Atomistic simulations ---
# The kind of process is the object type (single point, geometry optimization, molecular dynamics).
# The physical model (DFT, interatomic potential) is the referenced ComputationalMethod (COMPUTATIONAL_METHOD), so ab initio
# MD is a MolecularDynamics with a DFT ComputationalMethod and ElectronicStructureParameters.
# Input parameters are ParameterSet objects referenced by the activity; result values are properties of
# the activity. The initial and final structures are SimulatedSystems referenced by INITIAL_SYSTEM and
# FINAL_SYSTEM. Per-atom quantities (positions,
# velocities, forces; CMSO AtomicPosition, AtomicVelocity, AtomicForce) and trajectories are attached as files.


class AtomisticSimulation(Simulation):
    defs = ObjectTypeDef(
        code="ATOMISTIC_SIMULATION",
        description="An AtomisticSimulation is a simulation in which the atoms of the system and their positions are "
        "represented explicitly, and energies and forces are computed for nuclear configurations.",
        generated_code_prefix="ATOM_SIM",
        # v0 jobs map to the subtype given by their ATOMISTIC_CALC_TYPE: ATOM_CALC_SC -> SinglePointCalculation,
        # ATOM_CALC_STRUC_OPT -> GeometryOptimization, ATOM_CALC_MD -> MolecularDynamics
        # (ATOM_CALC_MC and ATOM_CALC_NEB are not modelled yet).
        prev_versions=["PYIRON_JOB.VASP:v0", "PYIRON_JOB.LAMMPS:v0"],
    )

    initial_system = PropertyTypeAssignment(
        code="INITIAL_SYSTEM",
        data_type="OBJECT",
        object_code="SIMULATED_SYSTEM",
        property_label="Initial system",
        description="Simulated system at the start of the simulation.",
        mandatory=False,
        section="Simulated Systems",
    )

    final_system = PropertyTypeAssignment(
        code="FINAL_SYSTEM",
        data_type="OBJECT",
        object_code="SIMULATED_SYSTEM",
        property_label="Final system",
        description="Simulated system at the end of the simulation, such as the relaxed structure or the last "
        "configuration of a molecular dynamics run.",
        mandatory=False,
        section="Simulated Systems",
    )

    electronic_structure_parameters = PropertyTypeAssignment(
        code="ELECTRONIC_STRUCTURE_PARAMETERS",
        data_type="OBJECT",
        object_code="ELECTRONIC_STRUCTURE_PARAMETERS",
        property_label="Electronic structure parameters",
        description="Numerical parameters used to solve the electronic structure, for electronic-structure methods "
        "such as DFT.",
        mandatory=False,
        section="Input Specification",
    )

    # Results for the final configuration

    max_force_norm = PropertyTypeAssignment(
        code="MAX_FORCE_NORM",
        data_type="REAL",
        property_label="Maximum force norm",
        units="eV/angstrom",
        description="Largest norm of the force on a single atom in the final configuration.",
        mandatory=False,
        section="Results",
    )

    max_force_component = PropertyTypeAssignment(
        code="MAX_FORCE_COMPONENT",
        data_type="REAL",
        property_label="Maximum force component",
        units="eV/angstrom",
        description="Largest absolute Cartesian component of the force on any atom in the final configuration "
        "(LAMMPS: fmax).",
        mandatory=False,
        section="Results",
        prev_versions=["ATOM_FORCE_MAX_IN_EV_A:v0"],
    )

    force_vector_norm = PropertyTypeAssignment(
        code="FORCE_VECTOR_NORM",
        data_type="REAL",
        property_label="Force vector norm",
        units="eV/angstrom",
        description="Euclidean norm of the 3N-dimensional vector of all atomic forces in the final configuration "
        "(LAMMPS: fnorm).",
        mandatory=False,
        section="Results",
        prev_versions=["ATOM_FIN_FNORM_IN_EV_A:v0"],
    )

    # With a tensile-positive stress tensor sigma this is P = -tr(sigma)/3; codes differ in the sign of the stress
    # they print, so the convention of the source must be checked. VASP prints it in the OUTCAR line external
    # pressure, in kbar (1 GPa = 10 kbar).
    final_pressure = PropertyTypeAssignment(
        code="FINAL_PRESSURE",
        data_type="REAL",
        property_label="Final pressure",
        units="GPa",
        description="Hydrostatic pressure of the final configuration, with the convention that positive values mean "
        "the system is compressed and would expand if allowed, and negative values mean it would contract.",
        mandatory=False,
        section="Results",
        iri=["https://purls.helmholtz-metadaten.de/asmo/Pressure"],
        prev_versions=["ATOM_FIN_PRESS_IN_GPA:v0"],
    )

    # For electronic-structure methods use the specific total energies below, which state their treatment of the
    # electronic entropy.
    final_potential_energy = PropertyTypeAssignment(
        code="FINAL_POTENTIAL_ENERGY",
        data_type="REAL",
        property_label="Final potential energy",
        units="eV",
        description="Potential energy of the final nuclear configuration as given by the referenced computational "
        "method, such as the energy of a force field (LAMMPS: pe). For molecular dynamics, the configuration of the "
        "last time step.",
        mandatory=False,
        section="Results",
        iri=["https://purls.helmholtz-metadaten.de/asmo/PotentialEnergy"],
    )

    # Results of electronic-structure methods. The three energies coincide when no smearing is used. In VASP all
    # energies are relative to the isolated atoms in the reference configuration of the PAW datasets, so only
    # differences between calculations with the same datasets are meaningful.

    scf_converged = PropertyTypeAssignment(
        code="SCF_CONVERGED",
        data_type="BOOLEAN",
        property_label="SCF converged",
        description="Whether the self-consistent field cycle of the final configuration reached its convergence "
        "threshold.",
        mandatory=False,
        section="Electronic Structure Results",
    )

    n_irreducible_kpoints = PropertyTypeAssignment(
        code="N_IRREDUCIBLE_KPOINTS",
        data_type="INTEGER",
        property_label="Number of irreducible k-points",
        description="Number of k-points left after the mesh was reduced by the symmetry used in the calculation.",
        mandatory=False,
        section="Electronic Structure Results",
    )

    total_free_energy = PropertyTypeAssignment(
        code="TOTAL_FREE_ENERGY",
        data_type="REAL",
        property_label="Total free energy",
        units="eV",
        description="Total energy of the final configuration including the electronic entropy term -TS of the "
        "smeared occupations (VASP: free energy TOTEN).",
        mandatory=False,
        section="Electronic Structure Results",
    )

    total_energy_without_entropy = PropertyTypeAssignment(
        code="TOTAL_ENERGY_WITHOUT_ENTROPY",
        data_type="REAL",
        property_label="Total energy without entropy",
        units="eV",
        description="Total free energy minus the electronic entropy term -TS (VASP: energy without entropy).",
        mandatory=False,
        section="Electronic Structure Results",
    )

    total_energy_zero_smearing = PropertyTypeAssignment(
        code="TOTAL_ENERGY_ZERO_SMEARING",
        data_type="REAL",
        property_label="Total energy extrapolated to zero smearing",
        units="eV",
        description="Total energy extrapolated to zero smearing width (VASP: energy(sigma->0)).",
        mandatory=False,
        section="Electronic Structure Results",
    )

    fermi_energy = PropertyTypeAssignment(
        code="FERMI_ENERGY",
        data_type="REAL",
        property_label="Fermi energy",
        units="eV",
        description="Fermi energy of the final configuration (VASP: E-fermi). For systems with a band gap, where "
        "in the gap it lies depends on the occupation scheme and code settings.",
        mandatory=False,
        section="Electronic Structure Results",
    )

    # Needs manual mapping from ATOM_FIN_TOTMGMO_IN_MUB:v0: v0 stored VARCHAR and also covered noncollinear jobs
    # (ATOM_NON_COLL_MAG). Migrate only values that parse as a single number from collinear jobs; keep vector or
    # other text values separately.
    total_magnetic_moment = PropertyTypeAssignment(
        code="TOTAL_MAGNETIC_MOMENT",
        data_type="REAL",
        property_label="Total magnetic moment",
        units="bohr_magneton",
        description="Signed total spin magnetic moment of the cell along the spin quantization axis of a collinear "
        "spin-polarized calculation, i.e. the number of spin-up minus spin-down electrons. Not defined for "
        "noncollinear calculations, whose total moment is a vector; its magnitude must not be stored here.",
        mandatory=False,
        section="Electronic Structure Results",
    )

    # Not migrated from v0:
    # ATOM_FIN_TOT_ENG_IN_EV, ATOM_FIN_POT_ENG_IN_EV: shared by the v0 VASP and LAMMPS job types. For LAMMPS the
    #   potential energy is FINAL_POTENTIAL_ENERGY for every calculation type, and the total energy is
    #   FINAL_TOTAL_ENERGY of MolecularDynamics. For VASP it is unclear which VASP energy pyiron stored: pyiron
    #   vasp/base.py (_vasp_generic_energy_free_affected) shows that legacy HDF version 0.1.0 stored inconsistent
    #   generic energies, so check the HDF version and the raw OUTCAR per job before migrating.
    # ATOM_FIN_VOL_IN_A3: CELL_VOLUME of the SimulatedSystem referenced by FINAL_SYSTEM.
    # PERIODIC_BOUNDARY_X/Y/Z: periodicity belongs to the SimulatedSystem (PERIODIC_A/B/C); x/y/z and a/b/c only
    #   coincide for orthogonal cells aligned with the axes.


class SinglePointCalculation(AtomisticSimulation):
    defs = ObjectTypeDef(
        code="SINGLE_POINT_CALCULATION",
        description="A SinglePointCalculation is an atomistic simulation that computes the energy, forces, and other "
        "properties for one fixed nuclear configuration. For electronic-structure methods this usually includes one "
        "self-consistent field solution, but it can also be a non-self-consistent calculation on a fixed density, "
        "such as for a band structure.",
        generated_code_prefix="SINGLE_PT",
    )


class GeometryOptimization(AtomisticSimulation):
    defs = ObjectTypeDef(
        code="GEOMETRY_OPTIMIZATION",
        description="A GeometryOptimization is an atomistic simulation that moves the nuclei, and the cell if "
        "allowed, towards a local minimum of the energy.",
        generated_code_prefix="GEO_OPT",
        iri=["https://w3id.org/pmd/co/PMD_0000956"],
    )

    geometry_optimization_parameters = PropertyTypeAssignment(
        code="GEOMETRY_OPTIMIZATION_PARAMETERS",
        data_type="OBJECT",
        object_code="GEOMETRY_OPTIMIZATION_PARAMETERS",
        property_label="Geometry optimization parameters",
        description="Degrees of freedom, algorithm, and convergence thresholds of the optimization.",
        mandatory=False,
        section="Input Specification",
    )

    n_ionic_steps = PropertyTypeAssignment(
        code="N_IONIC_STEPS",
        data_type="INTEGER",
        property_label="Number of ionic steps",
        description="Number of ionic steps (geometry optimization steps or molecular dynamics time steps) actually "
        "carried out.",
        mandatory=False,
        section="Results",
        iri=["https://purls.helmholtz-metadaten.de/asmo/NumberOfIonicSteps"],
        prev_versions=["ATOMISTIC_IONIC_STEPS:v0", "ATOM_IONIC_STEPS:v0"],
    )

    # Stopping before the maximum number of ionic steps does not by itself mean convergence, since an optimization
    # can also stop for other reasons (see OPTIMIZATION_STOP_REASON).
    geometry_converged = PropertyTypeAssignment(
        code="GEOMETRY_CONVERGED",
        data_type="BOOLEAN",
        property_label="Geometry converged",
        description="Whether the final configuration satisfies the convergence criteria of the optimization, "
        "including when they are met at the last allowed ionic step.",
        mandatory=False,
        section="Results",
    )

    optimization_stop_reason = PropertyTypeAssignment(
        code="OPTIMIZATION_STOP_REASON",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="OPTIMIZATION_STOP_REASON",
        property_label="Stop reason",
        description="Reason why the optimization stopped, as reported by the code. A criterion can be met on the "
        "last allowed step; in that case the code's report decides, and GEOMETRY_CONVERGED is true. Not set if the "
        "code did not report a reason.",
        mandatory=False,
        section="Results",
    )


class MolecularDynamics(AtomisticSimulation):
    defs = ObjectTypeDef(
        code="MOLECULAR_DYNAMICS",
        description="A MolecularDynamics is an atomistic simulation that integrates the classical equations of motion "
        "of the nuclei in time, with forces from the referenced computational method.",
        generated_code_prefix="MD",
        # No IRI: PMDco has ab initio MD (PMD_0000504) and empirical potential MD (PMD_0000631) as separate process
        # classes, both narrower than this type; ASMO MolecularDynamics is a computational method, not a process.
    )

    molecular_dynamics_parameters = PropertyTypeAssignment(
        code="MOLECULAR_DYNAMICS_PARAMETERS",
        data_type="OBJECT",
        object_code="MOLECULAR_DYNAMICS_PARAMETERS",
        property_label="Molecular dynamics parameters",
        description="Ensemble, target conditions, time step, thermostat, and barostat of the run.",
        mandatory=False,
        section="Input Specification",
    )

    n_ionic_steps = PropertyTypeAssignment(
        code="N_IONIC_STEPS",
        data_type="INTEGER",
        property_label="Number of ionic steps",
        description="Number of ionic steps (geometry optimization steps or molecular dynamics time steps) actually "
        "carried out.",
        mandatory=False,
        section="Results",
        iri=["https://purls.helmholtz-metadaten.de/asmo/NumberOfIonicSteps"],
        prev_versions=["ATOMISTIC_IONIC_STEPS:v0", "ATOM_IONIC_STEPS:v0"],
    )

    # Averages are over the time steps of the run, as recorded by v0. Whether an equilibration period was excluded
    # is not recorded; the time series should be attached as a file.

    average_temperature = PropertyTypeAssignment(
        code="AVERAGE_TEMPERATURE",
        data_type="REAL",
        property_label="Average temperature",
        units="K",
        description="Time average of the instantaneous temperature over the time steps of the run.",
        mandatory=False,
        section="Results",
        prev_versions=["ATOM_MD_AVG_TEMP_IN_K:v0"],
    )

    average_pressure = PropertyTypeAssignment(
        code="AVERAGE_PRESSURE",
        data_type="REAL",
        property_label="Average pressure",
        units="GPa",
        description="Time average of the instantaneous pressure over the time steps of the run.",
        mandatory=False,
        section="Results",
        prev_versions=["ATOM_AVG_PRESS_IN_GPA:v0"],
    )

    average_volume = PropertyTypeAssignment(
        code="AVERAGE_VOLUME",
        data_type="REAL",
        property_label="Average volume",
        units="angstrom**3",
        description="Time average of the cell volume over the time steps of the run.",
        mandatory=False,
        section="Results",
        prev_versions=["ATOM_AVG_VOL_IN_A3:v0"],
    )

    average_potential_energy = PropertyTypeAssignment(
        code="AVERAGE_POTENTIAL_ENERGY",
        data_type="REAL",
        property_label="Average potential energy",
        units="eV",
        description="Time average of the potential energy of the nuclear configuration over the time steps of "
        "the run.",
        mandatory=False,
        section="Results",
        prev_versions=["ATOM_AVG_POT_ENG_IN_EV:v0"],
    )

    average_total_energy = PropertyTypeAssignment(
        code="AVERAGE_TOTAL_ENERGY",
        data_type="REAL",
        property_label="Average total energy",
        units="eV",
        description="Time average of potential plus kinetic energy of the nuclei over the time steps of the run.",
        mandatory=False,
        section="Results",
        prev_versions=["ATOM_AVG_TOT_ENG_IN_EV:v0"],
    )

    average_force_vector_norm = PropertyTypeAssignment(
        code="AVERAGE_FORCE_VECTOR_NORM",
        data_type="REAL",
        property_label="Average force vector norm",
        units="eV/angstrom",
        description="Time average of the Euclidean norm of the 3N-dimensional force vector over the time steps of "
        "the run (LAMMPS: fnorm).",
        mandatory=False,
        section="Results",
        prev_versions=["ATOM_AVG_FNORM_IN_EV_A:v0"],
    )

    # FINAL_POTENTIAL_ENERGY is inherited from AtomisticSimulation.

    final_total_energy = PropertyTypeAssignment(
        code="FINAL_TOTAL_ENERGY",
        data_type="REAL",
        property_label="Final total energy",
        units="eV",
        description="Potential plus kinetic energy of the nuclei at the last time step.",
        mandatory=False,
        section="Results",
        iri=["https://purls.helmholtz-metadaten.de/asmo/TotalEnergy"],
    )


# --- Analyses of simulation results ---
# Same pattern as for simulations: parameters are ParameterSet objects referenced by the analysis, result
# values are properties of the analysis. Two links are kept apart:
# - Data dependency: the parents of an analysis (openBIS parent-child) are exactly the computations whose outputs
#   it used, no more and no fewer (PROV: the analysis used their outputs / was informed by them). Parents are used
#   rather than a typed property because an openBIS object property accepts only its exact target type, and the
#   upstream computations are of several types.
# - Subject: ANALYSED_SYSTEM is the one SimulatedSystem that the results of the analysis describe (NOMAD:
#   Outputs.model_system_ref; IAO: is about). It is single-valued so that every result has one system, and it is
#   set directly rather than derived from the parents, whose SIMULATED_SYSTEM is multivalued and has no roles.
# The physical model of the upstream calculation is not copied to the analysis; it is reached through the parents.
#
# Orbital-based bonding analysis of plane-wave DFT results (VASP + LOBSTER + LobsterPy, as in the atomate2
# LobsterTaskDocument). Chain, parent -> child:
#   SinglePointCalculation (static VASP run)
#     -> LocalOrbitalBondingAnalysis    projection + COHP/COOP/COBI + populations (one LOBSTER run)
#       -> ProjectionQualityAssessment  checks of the projection (LobsterPy)
#       -> BondingEnvironmentAnalysis   relevant bonds and coordination environments (LobsterPy)
# Parent links alone do not show which saved projection (LOBSTER saveProjectionToFile / loadProjectionFromFile)
# was reused: attach the run files (lobsterout, lobsterin) and the reused projection file to the activities
# concerned.
# Per-site and per-bond results and energy-resolved curves (COHPCAR, COOPCAR, COBICAR, DOSCAR) are attached as
# files.
# Sources: atomate2 / emmet LobsterTaskDocument and LobsterPy source; Maintz et al., J. Comput. Chem. 37, 1030
# (2016); Sanchez-Portal et al., Solid State Commun. 95, 685 (1995); Ertural et al., RSC Adv. 9, 29821 (2019);
# Naik et al., Sci. Data 10, 610 (2023); LobsterPy quality/analyze.py and pymatgen CompleteDos.get_dos_fp.
# All analyses of one chain have the same ANALYSED_SYSTEM: the system of the static SinglePointCalculation.


class SimulationAnalysis(Analysis):
    defs = ObjectTypeDef(
        code="SIMULATION_ANALYSIS",
        description="A SimulationAnalysis is an analysis that derives information from the results of one or more "
        "simulations, about one simulated system.",
        generated_code_prefix="SIM_ANALY",
    )

    analysed_system = PropertyTypeAssignment(
        code="ANALYSED_SYSTEM",
        data_type="OBJECT",
        object_code="SIMULATED_SYSTEM",
        property_label="Analysed system",
        description="Simulated system whose properties the results of the analysis describe. The computations "
        "whose outputs were used are the parents of the analysis.",
        mandatory=False,
        section="Analysis Details",
    )


class LocalOrbitalBondingAnalysis(SimulationAnalysis):
    defs = ObjectTypeDef(
        code="LOCAL_ORBITAL_BONDING_ANALYSIS",
        description="A LocalOrbitalBondingAnalysis is an analysis that projects the wave functions of a converged "
        "electronic-structure calculation onto a local atomic-orbital basis and derives orbital-pair bonding "
        "indicators and atomic populations from the projected wave functions, in one program run.",
        generated_code_prefix="LOC_ORB_BOND",
    )

    orbital_projection_parameters = PropertyTypeAssignment(
        code="ORBITAL_PROJECTION_PARAMETERS",
        data_type="OBJECT",
        object_code="ORBITAL_PROJECTION_PARAMETERS",
        property_label="Orbital projection parameters",
        description="Local basis used for the projection.",
        mandatory=False,
        section="Input Specification",
    )

    bonding_analysis_parameters = PropertyTypeAssignment(
        code="BONDING_ANALYSIS_PARAMETERS",
        data_type="OBJECT",
        object_code="BONDING_ANALYSIS_PARAMETERS",
        property_label="Bonding analysis parameters",
        description="Indicators, population analyses, atom pairs, and energy grid of the analysis.",
        mandatory=False,
        section="Input Specification",
    )

    # Taking absolute values keeps deficits and excesses from cancelling, so this is not literally the fraction of
    # electrons lost. For spin-polarized calculations, the mean of the two spin channels.
    absolute_charge_spilling = PropertyTypeAssignment(
        code="ABSOLUTE_CHARGE_SPILLING",
        data_type="REAL",
        property_label="Absolute charge spilling",
        units="percent",
        description="Average, over k-points and occupied states, of abs(1 - O_jj), where O = C^dagger S C is the "
        "overlap matrix of the projected states and O_jj the self-overlap (squared norm) of state j, in percent "
        "(Maintz et al. 2016). Lower values mean the local basis reproduces the original wave functions better.",
        mandatory=False,
        section="Results",
    )

    # LOBSTER reports spilling per spin channel (pymatgen Lobsterout stores one value per spin). LobsterPy
    # summarizes them as sum(values) / 2 * 100, which is the mean only if both channels are present; for
    # non-spin-polarized output recompute from lobsterout rather than copying that summary.

    absolute_total_spilling = PropertyTypeAssignment(
        code="ABSOLUTE_TOTAL_SPILLING",
        data_type="REAL",
        property_label="Absolute total spilling",
        units="percent",
        description="Average, over k-points and all bands included in the projection (occupied and unoccupied), "
        "of abs(1 - O_jj), where O_jj is the self-overlap (squared norm) of projected state j, in percent. "
        "For spin-polarized calculations, the mean of the two spin channels.",
        mandatory=False,
        section="Results",
    )


class ProjectionQualityAssessment(SimulationAnalysis):
    defs = ObjectTypeDef(
        code="PROJECTION_QUALITY_ASSESSMENT",
        description="A ProjectionQualityAssessment is an analysis that judges how faithfully an orbital projection "
        "represents the wave functions of its parent calculation, by checking the chosen basis, the orthonormality "
        "of the projected wave functions, the chemical plausibility of the resulting atomic charges, and the "
        "agreement of the projected densities of states with those of the parent calculation.",
        generated_code_prefix="PROJ_QUAL",
    )

    projection_quality_parameters = PropertyTypeAssignment(
        code="PROJECTION_QUALITY_PARAMETERS",
        data_type="OBJECT",
        object_code="PROJECTION_QUALITY_PARAMETERS",
        property_label="Projection quality parameters",
        description="Thresholds and comparison settings of the quality checks.",
        mandatory=False,
        section="Input Specification",
    )

    is_minimal_basis = PropertyTypeAssignment(
        code="IS_MINIMAL_BASIS",
        data_type="BOOLEAN",
        property_label="Minimal basis",
        description="Whether the projection used the smallest set of basis functions available for each chemical "
        "species, given its pseudopotential. If not, comparing with a minimal-basis projection is advisable.",
        mandatory=False,
        section="Basis Check",
    )

    # Original description: Whether LOBSTER reported k-points at which the projected wave functions could not be
    # fully orthonormalized, in which case it writes the file bandOverlaps.lobster.
    has_band_overlap_deviations = PropertyTypeAssignment(
        code="HAS_BAND_OVERLAP_DEVIATIONS",
        data_type="BOOLEAN",
        property_label="Band overlap deviations reported",
        description="Whether k-points were reported at which the projected wave functions could not be fully "
        "orthonormalized (LOBSTER: bandOverlaps.lobster).",
        mandatory=False,
        section="Orthonormality Check",
    )

    # Original description: Largest deviation of the overlap matrix of the projected bands from the identity
    # matrix, over all k-points listed in bandOverlaps.lobster. Not set if no deviations were reported.
    band_overlap_max_deviation = PropertyTypeAssignment(
        code="BAND_OVERLAP_MAX_DEVIATION",
        data_type="REAL",
        property_label="Band overlap maximal deviation",
        description="Largest deviation of the overlap matrix of the projected bands from the identity matrix, over "
        "all k-points with reported deviations (LOBSTER: bandOverlaps.lobster). Not set if no deviations were "
        "reported.",
        mandatory=False,
        section="Orthonormality Check",
    )

    band_overlaps_within_limit = PropertyTypeAssignment(
        code="BAND_OVERLAPS_WITHIN_LIMIT",
        data_type="BOOLEAN",
        property_label="Band overlaps within limit",
        description="Whether the maximal band overlap deviation stays at or below the deviation limit at every "
        "listed k-point.",
        mandatory=False,
        section="Orthonormality Check",
    )

    kpoints_above_deviation_limit = PropertyTypeAssignment(
        code="KPOINTS_ABOVE_DEVIATION_LIMIT",
        data_type="REAL",
        property_label="K-points above deviation limit",
        units="percent",
        description="Share of the k-points of the calculation whose maximal band overlap deviation exceeds the "
        "deviation limit.",
        mandatory=False,
        section="Orthonormality Check",
    )

    # The classification is as in LobsterPy. This is not a three-way sign test: a neutral atom is grouped with the
    # cations.
    mulliken_signs_agree_with_bond_valence = PropertyTypeAssignment(
        code="MULLIKEN_SIGNS_AGREE_WITH_BOND_VALENCE",
        data_type="BOOLEAN",
        property_label="Mulliken charge signs agree with bond valence",
        description="Whether every atom falls in the same class for its Mulliken charge as for the valence "
        "estimated by a bond valence analysis of the crystal structure, where each value is classified as "
        "nonnegative (zero counts with positive) or negative. Not set if the bond valence analysis could not "
        "assign valences.",
        mandatory=False,
        section="Charge Sign Check",
    )

    # The classification is as in LobsterPy. This is not a three-way sign test: a neutral atom is grouped with the
    # cations.
    loewdin_signs_agree_with_bond_valence = PropertyTypeAssignment(
        code="LOEWDIN_SIGNS_AGREE_WITH_BOND_VALENCE",
        data_type="BOOLEAN",
        property_label="Loewdin charge signs agree with bond valence",
        description="Whether every atom falls in the same class for its Loewdin charge as for the valence "
        "estimated by a bond valence analysis of the crystal structure, where each value is classified as "
        "nonnegative (zero counts with positive) or negative. Not set if the bond valence analysis could not "
        "assign valences.",
        mandatory=False,
        section="Charge Sign Check",
    )

    pdos_similarity_s = PropertyTypeAssignment(
        code="PDOS_SIMILARITY_S",
        data_type="REAL",
        property_label="PDOS similarity (s)",
        description="Tanimoto similarity between the normalized fingerprints of the s-orbital projected density of "
        "states from the orbital projection and from the parent calculation. 1 means identical.",
        mandatory=False,
        section="PDOS Comparison",
    )

    # The energy range and number of bins in ProjectionQualityParameters are the requested settings. LobsterPy
    # clips the range to the available DOS energies and caps the number of bins, and returns the values it used;
    # the number of bins used is stored below as PDOS_COMPARISON_EFFECTIVE_N_BINS. Record the LobsterPy version on
    # the Software of the assessment.

    pdos_similarity_p = PropertyTypeAssignment(
        code="PDOS_SIMILARITY_P",
        data_type="REAL",
        property_label="PDOS similarity (p)",
        description="Tanimoto similarity between the normalized fingerprints of the p-orbital projected density of "
        "states from the orbital projection and from the parent calculation. 1 means identical.",
        mandatory=False,
        section="PDOS Comparison",
    )

    pdos_similarity_d = PropertyTypeAssignment(
        code="PDOS_SIMILARITY_D",
        data_type="REAL",
        property_label="PDOS similarity (d)",
        description="Tanimoto similarity between the normalized fingerprints of the d-orbital projected density of "
        "states from the orbital projection and from the parent calculation. 1 means identical.",
        mandatory=False,
        section="PDOS Comparison",
    )

    pdos_similarity_f = PropertyTypeAssignment(
        code="PDOS_SIMILARITY_F",
        data_type="REAL",
        property_label="PDOS similarity (f)",
        description="Tanimoto similarity between the normalized fingerprints of the f-orbital projected density of "
        "states from the orbital projection and from the parent calculation. 1 means identical.",
        mandatory=False,
        section="PDOS Comparison",
    )

    pdos_similarity_summed = PropertyTypeAssignment(
        code="PDOS_SIMILARITY_SUMMED",
        data_type="REAL",
        property_label="PDOS similarity (summed)",
        description="Tanimoto similarity between the normalized fingerprints of the summed projected density of "
        "states from the orbital projection and from the parent calculation. 1 means identical.",
        mandatory=False,
        section="PDOS Comparison",
    )

    pdos_comparison_effective_n_bins = PropertyTypeAssignment(
        code="PDOS_COMPARISON_EFFECTIVE_N_BINS",
        data_type="INTEGER",
        property_label="PDOS comparison number of bins used",
        description="Number of energy bins of the fingerprints actually used for the PDOS comparison, after the "
        "requested number was capped (LobsterPy: n_bins).",
        mandatory=False,
        section="PDOS Comparison",
    )

    quality_summary = PropertyTypeAssignment(
        code="PROJECTION_QUALITY_SUMMARY",
        data_type="MULTILINE_VARCHAR",
        property_label="Quality summary",
        description="Text summary of the results of the quality checks.",
        mandatory=False,
        section="Quality Summary",
    )


class BondingEnvironmentAnalysis(SimulationAnalysis):
    defs = ObjectTypeDef(
        code="BONDING_ENVIRONMENT_ANALYSIS",
        description="A BondingEnvironmentAnalysis is an analysis that selects the relevant bonds of each atom from "
        "integrated bonding indicators, such as ICOHP, and derives coordination environments and bond summaries "
        "from them.",
        generated_code_prefix="BOND_ENV",
    )

    bonding_environment_parameters = PropertyTypeAssignment(
        code="BONDING_ENVIRONMENT_PARAMETERS",
        data_type="OBJECT",
        object_code="BONDING_ENVIRONMENT_PARAMETERS",
        property_label="Bonding environment parameters",
        description="Bond selection and evaluation settings of the analysis.",
        mandatory=False,
        section="Input Specification",
    )

    # The next two are LobsterPy's max_considered_bond_length and number_considered_ions, renamed here because
    # the LobsterPy names do not describe what is counted.
    # The indicator file is such as ICOHPLIST.lobster; weak interactions that are later filtered out can set this
    # value (LobsterPy: max of Icohpcollection._list_length).
    max_input_interaction_distance = PropertyTypeAssignment(
        code="MAX_INPUT_INTERACTION_DISTANCE",
        data_type="REAL",
        property_label="Maximum interaction distance in input",
        units="angstrom",
        description="Longest interatomic distance in the full list of interactions read from the integrated bonding "
        "indicator file, before the relevant bonds are selected. This is not the longest selected bond.",
        mandatory=False,
        section="Results",
    )

    n_analysed_inequivalent_sites = PropertyTypeAssignment(
        code="N_ANALYSED_INEQUIVALENT_SITES",
        data_type="INTEGER",
        property_label="Number of analysed inequivalent sites",
        description="Number of symmetry-inequivalent sites used as analysis centres (LobsterPy: "
        "len(seq_ineq_ions)). With cation-anion bond selection these are the selected cation sites; with all-bond "
        "selection, all inequivalent sites. Not a count of all atoms in the cell, since multiplicities are not "
        "included.",
        mandatory=False,
        section="Results",
    )

    bonding_summary = PropertyTypeAssignment(
        code="BONDING_SUMMARY",
        data_type="MULTILINE_VARCHAR",
        property_label="Bonding summary",
        description="Text summary of the coordination environments and relevant bonds found in the analysis.",
        mandatory=False,
        section="Results",
    )


class EquationOfStateFit(SimulationAnalysis):
    defs = ObjectTypeDef(
        code="EQUATION_OF_STATE_FIT",
        description="An EquationOfStateFit is an analysis that fits an equation of state E(V) to the energies of "
        "one structure computed at several cell volumes, to obtain its equilibrium volume, equilibrium energy, and "
        "bulk modulus.",
        generated_code_prefix="EOS_FIT",
        prev_versions=["PYIRON_JOB.MURNAGHAN:v0"],
    )

    # The simulations at the individual volumes are its parents, one per energy-volume point; the energy-volume
    # data are attached as a file. ANALYSED_SYSTEM is the reference structure whose volume was scaled; the strained
    # structures stay with the parent simulations and have the same composition and number of particles.
    # For energies from static calculations, the results are static-lattice values at zero temperature, without
    # zero-point or thermal vibrations.

    equation_of_state_fit_parameters = PropertyTypeAssignment(
        code="EQUATION_OF_STATE_FIT_PARAMETERS",
        data_type="OBJECT",
        object_code="EQUATION_OF_STATE_FIT_PARAMETERS",
        property_label="Equation of state fit parameters",
        description="Equation of state, fit order, fitted energy, and volume sampling.",
        mandatory=False,
        section="Input Specification",
    )

    equilibrium_volume = PropertyTypeAssignment(
        code="EQUILIBRIUM_VOLUME",
        data_type="REAL",
        property_label="Equilibrium volume",
        units="angstrom**3",
        description="Volume V0 at the minimum of the fitted E(V) curve, for the cell of the ANALYSED_SYSTEM, i.e. for "
        "its number of particles.",
        mandatory=False,
        section="Results",
        prev_versions=["ATOM_EQUIL_VOL_IN_A3:v0"],
    )

    equilibrium_energy = PropertyTypeAssignment(
        code="EQUILIBRIUM_ENERGY",
        data_type="REAL",
        property_label="Equilibrium energy",
        units="eV",
        description="Energy E0 at the minimum of the fitted E(V) curve, for the cell of the ANALYSED_SYSTEM, i.e. for "
        "its number of particles.",
        mandatory=False,
        section="Results",
        prev_versions=["ATOM_EQUIL_TOTENG_IN_EV:v0"],
    )

    # Isotropic straining is not sufficient in general: for an anisotropic crystal equal strains give unequal
    # normal stresses, and the curvature of an isotropically scaled cell can exceed the hydrostatic bulk modulus.
    # For cubic symmetry isotropic scaling keeps the correct cell shape, but internal coordinates must still be
    # relaxed. Otherwise the value is the curvature along the constrained deformation path (see EOS_STRAIN_AXES and
    # the relaxation degrees of freedom of the parent simulations).
    bulk_modulus = PropertyTypeAssignment(
        code="BULK_MODULUS",
        data_type="REAL",
        property_label="Bulk modulus",
        units="GPa",
        description="Bulk modulus B0 = V d2E/dV2 at the equilibrium volume, from the fitted curve. This is the "
        "equilibrium (relaxed-ion) hydrostatic bulk modulus only if, at each fixed volume, the energy was minimized "
        "over the cell shape and the internal coordinates.",
        mandatory=False,
        section="Results",
        iri=["https://purls.helmholtz-metadaten.de/asmo/BulkModulus"],
        prev_versions=["ATOM_EQUIL_K_MOD_IN_GPA:v0"],
    )

    bulk_modulus_pressure_derivative = PropertyTypeAssignment(
        code="BULK_MODULUS_PRESSURE_DERIVATIVE",
        data_type="REAL",
        property_label="Pressure derivative of the bulk modulus",
        description="Dimensionless pressure derivative B0' = dB/dP of the bulk modulus at the equilibrium volume, "
        "from the fitted curve.",
        mandatory=False,
        section="Results",
    )


class Experiment(Activity):
    defs = ObjectTypeDef(
        code="EXPERIMENT",
        description="An Experiment is an activity that applies controlled procedures to investigate, "
        "measure, produce, or modify physical systems.",
        generated_code_prefix="EXPER",
    )

    method_name = PropertyTypeAssignment(
        code="METHOD_NAME",
        data_type="VARCHAR",
        property_label="Method name",
        description="Name of the method or procedure used to perform the experiment, such as X-ray diffraction, "
        "tensile testing, or chemical vapor deposition.",
        mandatory=False,
        section="Experiment Details",
    )

    location = PropertyTypeAssignment(
        code="LOCATION",
        data_type="OBJECT",
        object_code="LOCATION",
        property_label="Location",
        description="Physical location.",
        mandatory=False,
        section="Experiment Details",
    )


class Processing(Experiment):
    defs = ObjectTypeDef(
        code="PROCESSING",
        description="A Processing is an experiment that alters the structure, composition, or form "
        "of a material.",
        generated_code_prefix="PROCESSING",
        iri=["https://w3id.org/pmd/co/PMD_0000833"],
        prev_versions=["SAMPLE_PRETREATMENT:v0"],
    )


class Measurement(Experiment):
    defs = ObjectTypeDef(
        code="MEASUREMENT",
        description="A Measurement is an experiment that determines one or more properties or characteristics "
        "of a system through observation or measurement procedures.",
        generated_code_prefix="MEASUR",
        iri=["http://purl.obolibrary.org/obo/OBI_0000070"],
    )


class Calibration(Experiment):
    defs = ObjectTypeDef(
        code="CALIBRATION",
        description="A Calibration is an experiment that establishes or adjusts the mapping between "
        "measurement outputs and reference standards.",
        generated_code_prefix="CALIB",
        iri=["https://w3id.org/pmd/co/PMD_0001039"],
        prev_versions=["CALIBRATION:v0"],
    )

    calibration_date = PropertyTypeAssignment(
        code="CALIBRATION_DATE",
        data_type="DATE",
        property_label="Calibration date",
        description="Date on which the calibration was performed or formally recorded.",
        mandatory=False,
        section="Calibration Details",
        prev_versions=["CALIBRATION_DATE:v0"],
    )

    calibration_provider = PropertyTypeAssignment(
        code="CALIBRATION_PROVIDER",
        data_type="VARCHAR",
        property_label="Calibration provider",
        description="Organization or service provider responsible for performing the calibration, "
        "such as an internal laboratory or an external calibration service.",
        mandatory=False,
        section="Calibration Details",
        prev_versions=["CALIBRATION_PROVIDER:v0"],
    )

    calibration_certificate_number = PropertyTypeAssignment(
        code="CALIBRATION_CERTIFICATE_NUMBER",
        data_type="VARCHAR",
        property_label="Calibration certificate number",
        description="Unique identifier assigned to the calibration certificate documenting the "
        "calibration results.",
        mandatory=False,
        section="Calibration Details",
        prev_versions=["CALIBRATION_CERTIFICATE_NUMBER:v0"],
    )

    accredited_calibration_lab = PropertyTypeAssignment(
        code="ACCREDITATED_CALIBRATION_LAB",
        data_type="BOOLEAN",
        property_label="Accredited calibration laboratory",
        description="Whether the calibration was performed by an accredited calibration laboratory",
        mandatory=False,
        section="Calibration Details",
        prev_versions=["ACCREDITATED_CALIBRATION_LAB:v0"],
    )

    calibration_lab_accreditation_number = PropertyTypeAssignment(
        code="CALIBRATION_LAB_ACCREDITATION_NUMBER",
        data_type="VARCHAR",
        property_label="Calibration laboratory accreditation number",
        description="Identifier assigned to the calibration laboratory by its accreditation body.",
        mandatory=False,
        section="Calibration Details",
        prev_versions=["CALIBRATION_LAB_ACCREDITATION_NUMBER:v0"],
    )

    # Properties from v0 that need to be migrated to v1 (from CALIBRATION:v0):
    # INSTRUMENT


class Synthesis(Experiment):
    defs = ObjectTypeDef(
        code="SYNTHESIS",
        description="A Synthesis is an experiment that creates or assembles materials through chemical "
        "or physical means.",
        generated_code_prefix="SYNTH",
    )


class Test(Experiment):  # needs clarification # do we need test and measurement
    defs = ObjectTypeDef(
        code="TEST",
        description="A Test is an experiment that evaluates the behavior or performance of a system under "
        "specified conditions.",
        generated_code_prefix="TEST",
    )
