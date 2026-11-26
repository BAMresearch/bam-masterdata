# AUTO-GENERATED CLASS HIERARCHY — DO NOT EDIT
#
# Activity*
# ├── Computation
# │   ├── Analysis
# │   │   ├── CreepTestDataProcessing
# │   │   └── SimulationAnalysis
# │   │       └── EquationOfStateFit
# │   └── Simulation
# │       ├── SinglePointCalculation
# │       ├── GeometryOptimization
# │       ├── MolecularDynamics
# │       ├── MonteCarloSimulation
# │       └── NudgedElasticBand
# └── Experiment
#     ├── Processing
#     ├── Measurement
#     ├── Calibration
#     ├── Synthesis
#     └── Test
#
# END AUTO-GENERATED CLASS HIERARCHY

from bam_masterdata.datamodel.v1.base_objects import Activity
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment


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
        "theory or an interatomic potential.",
        mandatory=False,
        section="Computation Details",
        multivalued=True,
    )

    executed_on = PropertyTypeAssignment(
        code="EXECUTED_ON",
        data_type="OBJECT",
        object_code="HPC",
        property_label="Executed on",
        description="Computing cluster on which the computation was run.",
        mandatory=False,
        section="Execution Details",
        iri=["http://purl.obolibrary.org/obo/RO_0000057"],
    )

    walltime_h = PropertyTypeAssignment(
        code="WALLTIME_H",
        data_type="REAL",
        property_label="Walltime",
        units="h",
        description="Elapsed time between the start and the end of this computation.",
        mandatory=False,
        section="Execution Details",
        prev_versions=["SIM_WALLTIME_IN_HOURS:v0"],
    )

    core_time_h = PropertyTypeAssignment(
        code="CORE_TIME_H",
        data_type="REAL",
        property_label="Core time",
        units="h",
        description="Total CPU time consumed by this computation, expressed in core-hours.",
        mandatory=False,
        section="Execution Details",
        prev_versions=["SIM_CORETIME_IN_HOURS:v0"],
    )

    n_cores = PropertyTypeAssignment(
        code="N_CORES",
        data_type="INTEGER",
        property_label="Number of cores",
        description="Number of CPU cores allocated to this computation.",
        mandatory=False,
        section="Execution Details",
        prev_versions=["NCORES:v0"],
    )

    n_gpus = PropertyTypeAssignment(
        code="N_GPUS",
        data_type="INTEGER",
        property_label="Number of GPUs",
        description="Number of GPUs allocated to this computation.",
        mandatory=False,
        section="Execution Details",
        prev_versions=["NGPUS:v0"],
    )

    n_threads = PropertyTypeAssignment(
        code="N_THREADS",
        data_type="INTEGER",
        property_label="Number of threads",
        description="Number of execution threads configured for this computation.",
        mandatory=False,
        section="Execution Details",
        prev_versions=["NTHREADS:v0"],
    )

    hpc_job_queue = PropertyTypeAssignment(
        code="HPC_JOB_QUEUE",
        data_type="VARCHAR",
        property_label="HPC job queue",
        description="Queue or partition of the cluster in which this computation was run.",
        mandatory=False,
        section="Execution Details",
        prev_versions=["HPC_JOB_QUEUE:v0"],
    )

    hpc_job_id = PropertyTypeAssignment(
        code="HPC_JOB_ID",
        data_type="VARCHAR",
        property_label="HPC job ID",
        description="Identifier that the job scheduler of the cluster assigned to this computation.",
        mandatory=False,
        section="Execution Details",
        prev_versions=["HPC_JOB_ID:v0"],
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


# How computations are linked: see docs/explanations/computation_schema.md.


class Simulation(Computation):
    defs = ObjectTypeDef(
        code="SIMULATION",
        description="A Simulation is a computation that uses one or more computational models to "
        "reproduce, predict, or explore the behavior of a system under specified conditions.",
        generated_code_prefix="SIMUL",
        iri=["https://w3id.org/pmd/co/PMD_0000933"],
        prev_versions=["PYIRON_JOB:v0"],
    )

    simulated_system = PropertyTypeAssignment(
        code="SIMULATED_SYSTEM",
        data_type="OBJECT",
        object_code="SIMULATED_SYSTEM",
        property_label="Simulated system",
        description="All systems involved in the simulation, with INITIAL_SYSTEM and FINAL_SYSTEM "
        "identifying which of them is the start and the end.",
        mandatory=False,
        section="Simulation Details",
        multivalued=True,
    )

    # Properties from v0 that need to be migrated to v1 (from PYIRON_JOB:v0):
    # BAM_USERNAME
    # CONCEPTUAL_DICTIONARY


INITIAL_SYSTEM = PropertyTypeAssignment(
    code="INITIAL_SYSTEM",
    data_type="OBJECT",
    object_code="SIMULATED_SYSTEM",
    property_label="Initial system",
    description="Simulated system at the start of the simulation.",
    mandatory=False,
    section="Simulated Systems",
    iri=["http://purl.obolibrary.org/obo/OBI_0000293"],
)

FINAL_SYSTEM = PropertyTypeAssignment(
    code="FINAL_SYSTEM",
    data_type="OBJECT",
    object_code="SIMULATED_SYSTEM",
    property_label="Final system",
    description="Simulated system at the end of the simulation, such as the relaxed structure or the last "
    "configuration of a molecular dynamics run.",
    mandatory=False,
    section="Simulated Systems",
    iri=["http://purl.obolibrary.org/obo/OBI_0000299"],
)

ELECTRONIC_STRUCTURE_PARAMETERS = PropertyTypeAssignment(
    code="ELECTRONIC_STRUCTURE_PARAMETERS",
    data_type="OBJECT",
    object_code="ELECTRONIC_STRUCTURE_PARAMETERS",
    property_label="Electronic structure parameters",
    description="Numerical parameters used to solve the electronic structure, for electronic-structure methods "
    "such as DFT.",
    mandatory=False,
    section="Input Specification",
)


class _SimulationInputs:  # no defs: not an openBIS type
    initial_system = INITIAL_SYSTEM
    electronic_structure_parameters = ELECTRONIC_STRUCTURE_PARAMETERS


class _SimulationInputsAndOutputs(_SimulationInputs):  # no defs: not an openBIS type
    final_system = FINAL_SYSTEM


class SinglePointCalculation(_SimulationInputs, Simulation):
    defs = ObjectTypeDef(
        code="SINGLE_POINT_CALCULATION",
        description="A SinglePointCalculation is a simulation that computes the energy and other properties of one "
        "fixed configuration of a system.",
        generated_code_prefix="SINGLE_PT",
        prev_versions=["PYIRON_JOB.VASP:v0", "PYIRON_JOB.LAMMPS:v0"],
    )

    single_point_results = PropertyTypeAssignment(
        code="SINGLE_POINT_RESULTS",
        data_type="OBJECT",
        object_code="SINGLE_POINT_RESULTS",
        property_label="Results",
        description="Results of this computation.",
        mandatory=False,
        section="Results",
        iri=["http://purl.obolibrary.org/obo/OBI_0000299"],
    )


class GeometryOptimization(_SimulationInputsAndOutputs, Simulation):
    defs = ObjectTypeDef(
        code="GEOMETRY_OPTIMIZATION",
        description="A GeometryOptimization is a simulation that changes the structure of a system, and its cell if "
        "allowed, towards a local minimum of its energy.",
        generated_code_prefix="GEO_OPT",
        prev_versions=["PYIRON_JOB.VASP:v0", "PYIRON_JOB.LAMMPS:v0"],
        # No IRI: PMD_0000956 (structural optimization simulation) is about the most stable structure,
        # not a local minimum.
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

    geometry_optimization_results = PropertyTypeAssignment(
        code="GEOMETRY_OPTIMIZATION_RESULTS",
        data_type="OBJECT",
        object_code="GEOMETRY_OPTIMIZATION_RESULTS",
        property_label="Results",
        description="Results of this computation.",
        mandatory=False,
        section="Results",
        iri=["http://purl.obolibrary.org/obo/OBI_0000299"],
    )


class MolecularDynamics(_SimulationInputsAndOutputs, Simulation):
    defs = ObjectTypeDef(
        code="MOLECULAR_DYNAMICS",
        description="A MolecularDynamics is a simulation that integrates the equations of motion of the particles "
        "of a system over time, with forces from the referenced computational method.",
        generated_code_prefix="MD",
        prev_versions=["PYIRON_JOB.VASP:v0", "PYIRON_JOB.LAMMPS:v0"],
        # No IRI: PMDco has ab initio MD (PMD_0000504) and empirical potential MD (PMD_0000631) as separate
        # classes, both narrower than this type.
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

    molecular_dynamics_results = PropertyTypeAssignment(
        code="MOLECULAR_DYNAMICS_RESULTS",
        data_type="OBJECT",
        object_code="MOLECULAR_DYNAMICS_RESULTS",
        property_label="Results",
        description="Results of this computation.",
        mandatory=False,
        section="Results",
        iri=["http://purl.obolibrary.org/obo/OBI_0000299"],
    )


class MonteCarloSimulation(_SimulationInputsAndOutputs, Simulation):
    defs = ObjectTypeDef(
        code="MONTE_CARLO_SIMULATION",
        description="A MonteCarloSimulation is a simulation that samples configurations of a system by random "
        "sampling.",
        generated_code_prefix="MC",
        prev_versions=["PYIRON_JOB.VASP:v0", "PYIRON_JOB.LAMMPS:v0"],
    )


class NudgedElasticBand(Simulation):
    defs = ObjectTypeDef(
        code="NUDGED_ELASTIC_BAND",
        description="A NudgedElasticBand is a simulation that finds a minimum energy path between two given "
        "configurations of a system, represented by a chain of intermediate configurations. The end "
        "configurations and the intermediate configurations are listed in SIMULATED_SYSTEM.",
        generated_code_prefix="NEB",
        prev_versions=["PYIRON_JOB.VASP:v0", "PYIRON_JOB.LAMMPS:v0"],
    )

    electronic_structure_parameters = ELECTRONIC_STRUCTURE_PARAMETERS


class SimulationAnalysis(Analysis):
    defs = ObjectTypeDef(
        code="SIMULATION_ANALYSIS",
        description="A SimulationAnalysis is an analysis that derives information from the results of one or more "
        "simulations.",
        generated_code_prefix="SIM_ANALY",
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

    equation_of_state_fit_parameters = PropertyTypeAssignment(
        code="EQUATION_OF_STATE_FIT_PARAMETERS",
        data_type="OBJECT",
        object_code="EQUATION_OF_STATE_FIT_PARAMETERS",
        property_label="Equation of state fit parameters",
        description="Equation of state, fit order, fitted energy, and volume sampling.",
        mandatory=False,
        section="Input Specification",
    )

    equation_of_state_fit_results = PropertyTypeAssignment(
        code="EQUATION_OF_STATE_FIT_RESULTS",
        data_type="OBJECT",
        object_code="EQUATION_OF_STATE_FIT_RESULTS",
        property_label="Results",
        description="Results of this computation.",
        mandatory=False,
        section="Results",
        iri=["http://purl.obolibrary.org/obo/OBI_0000299"],
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
