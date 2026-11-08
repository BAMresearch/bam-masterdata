# AUTO-GENERATED CLASS HIERARCHY — DO NOT EDIT
#
# Computation
# ├── Analysis
# │   └── CreepTestDataProcessing
# └── Simulation
# 
# Experiment
# ├── Processing
# ├── Measurement
# ├── Calibration
# ├── Synthesis
# └── Test
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
        iri=["https://w3id.org/pmd/co/PMD_0025012"],
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
