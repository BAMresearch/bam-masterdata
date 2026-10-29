from bam_masterdata.datamodel.v1.base_objects import Activity
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment

# Hierarchy of the Activity branch of datamodel/v1:

#   Activity                        (see `base_objects.py`)
#   ├── Computation
#   │   ├── Analysis
#   │   │   └── CreepTestDataProcessing
#   │   └── Simulation
#   │       └── PyironJob
#   └── Experiment
#       ├── Processing
#       ├── Measurement
#       ├── Calibration
#       ├── Synthesis
#       └── Test


# Computation branch


class Computation(Activity):
    defs = ObjectTypeDef(
        code="COMPUTATION",
        description="An activity that performs computational operations using a computing environment to produce one or more outputs",
        generated_code_prefix="COMPUTATION",
        prev_versions=["COMPUTATIONAL_ANALYSIS:v0"],
    )

    software = PropertyTypeAssignment(
        code="SOFTWARE",
        data_type="OBJECT",
        object_code="SOFTWARE",
        property_label="Software",
        description="Software used to perform the computation",
        mandatory=False,
        section="Computation Details",
    )

    computational_method = PropertyTypeAssignment(
        code="COMPUTATIONAL_METHOD",
        data_type="OBJECT",
        object_code="COMPUTATIONAL_METHOD",
        property_label="Computational method",
        description="Computational methods, algorithms, and settings used during the computation, e.g. DFT Single Point or Geometry Optimization",
        mandatory=False,
        section="Computation Details",
        multivalued=True,
    )


class Analysis(Computation):
    # Defines no new properties; serves as a common parent for domain-specific analyses.
    defs = ObjectTypeDef(
        code="ANALYSIS",
        description="A computation that examines one or more existing inputs to derive information, properties, parameters, or other outputs",
        generated_code_prefix="ANALYSIS",
    )


class CreepTestDataProcessing(Analysis):
    defs = ObjectTypeDef(
        code="CREEP_TEST_DATA_PROCESSING",
        description="Data processing procedures applied to the data of a creep test",
        generated_code_prefix="CREEP_DATA_PROCESSING",
        prev_versions=[
            "COMPUTATIONAL_ANALYSIS.CREEP_TEST_DATA_PROCESSING_PROCEDURES:v0"
        ],
    )

    creep_test_primary_data_series = PropertyTypeAssignment(
        code="CREEP_TEST_PRIMARY_DATA_SERIES",
        data_type="VARCHAR",
        property_label="Primary data series",
        description="Primary data is data that is directly acquired by sensors or measuring instruments during or after a test. List the measured quantities and their corresponding units.",
        mandatory=False,
        section="Data Processing Procedures",
    )

    creep_test_processed_data_series = PropertyTypeAssignment(
        code="CREEP_TEST_PROCESSED_DATA_SERIES",
        data_type="VARCHAR",
        property_label="Processed data series",
        description="Processed data is obtained by applying procedures (equations, algorithms, methods, unit conversions, averaging, smoothing) to primary data. Describe the transformed quantities, their units, and the applied procedures.",
        mandatory=False,
        section="Data Processing Procedures",
    )

    creep_test_procedures = PropertyTypeAssignment(
        code="CREEP_TEST_PROCEDURE",
        data_type="VARCHAR",
        property_label="Test analysis procedures",
        description="Description of the data processing and analysis procedures used to obtain specific test results, e.g. percentage elastic extension",
        mandatory=False,
        section="Data Processing Procedures",
    )

    automated_workflow_usage = PropertyTypeAssignment(
        code="CREEP_TEST_WORKFLOW_USAGE",  # needs checking for actual wording
        data_type="BOOLEAN",
        property_label="Automated workflow usage",
        description="Whether automated (user-independent) analysis workflows were used",
        mandatory=False,
        section="Data Processing Procedures",
    )


class Simulation(Computation):
    defs = ObjectTypeDef(
        code="SIMULATION",
        description="A computation that uses one or more computational models to reproduce, predict, or explore the behavior of a system under specified conditions",
        generated_code_prefix="SIMULATION",
        iri=["https://ocdo.github.io/asmo/#Simulation"],
    )

    simulated_system = PropertyTypeAssignment(
        code="SIMULATED_SYSTEM",
        data_type="OBJECT",
        object_code="ENTITY",  # need info
        property_label="Simulated system",
        description="System being simulated, from atomistic to continuum scale",
        mandatory=False,
        section="Simulation Details",
        multivalued=True,
    )


class PyironJob(Simulation):
    defs = ObjectTypeDef(
        code="PYIRON_JOB",
        description="A simulation run as a job managed by the pyiron workflow framework",
        generated_code_prefix="PYIRON_JOB",
        prev_versions=["PYIRON_JOB:v0"],
    )

    simulation_walltime = PropertyTypeAssignment(
        code="SIM_WALLTIME_IN_HOUR",
        data_type="REAL",  # needs more info.
        property_label="Simulation walltime",
        units="h",
        description="Total run time (walltime) of the job",
        mandatory=False,
        section="Job Details",
    )

    simulation_core_time = PropertyTypeAssignment(
        code="SIM_CORETIME_IN_HOUR",
        data_type="REAL",
        property_label="Simulation core time",
        units="h",
        description="Total core time used by the job",
        mandatory=False,
        section="Job Details",
    )

    n_cores = PropertyTypeAssignment(
        code="NCORE",
        data_type="INTEGER",
        property_label="Number of cores",
        description="Number of cores used by the job",
        mandatory=False,
        section="Job Details",
    )

    n_gpus = PropertyTypeAssignment(
        code="NGPU",
        data_type="INTEGER",
        property_label="Number of GPUs",
        description="Number of GPUs used by the job",
        mandatory=False,
        section="Job Details",
    )

    n_threads = PropertyTypeAssignment(
        code="NTHREAD",
        data_type="INTEGER",
        property_label="Number of threads",
        description="Number of threads used by the job",
        mandatory=False,
        section="Job Details",
    )

    hpc_job_id = PropertyTypeAssignment(
        code="HPC_JOB_ID",
        data_type="VARCHAR",
        property_label="HPC job ID",
        description="Job ID in the HPC queue",
        mandatory=False,
        section="Job Details",
    )


# Experiment branch


class Experiment(Activity):
    defs = ObjectTypeDef(
        code="EXPERIMENT",
        description="An Experiment is an activity that acquires and records observations, measurements, or results for scientific analysis",
        generated_code_prefix="EXPERIMENT",
    )

    method_name = PropertyTypeAssignment(
        code="METHOD_NAME",
        data_type="VARCHAR",
        property_label="Method name",
        description="Name of the experimental method",
        mandatory=False,
        section="Experiment Details",
    )

    location = PropertyTypeAssignment(
        code="LOCATION",
        data_type="OBJECT",
        object_code="LOCATION",
        property_label="Location",
        description="Location where the experiment takes place",
        mandatory=False,
        section="Experiment Details",
    )


class Processing(Experiment):
    defs = ObjectTypeDef(
        code="PROCESSING",
        description="An experiment that alters the structure, composition, or form of a material",
        generated_code_prefix="PROCESSING",
        prev_versions=["SAMPLE_PRETREATMENT:v0"],
    )


class Measurement(Experiment):
    defs = ObjectTypeDef(
        code="MEASUREMENT",
        description="An experiment that uses an experimental device to produce quantitative or qualitative data about the properties of a material",
        generated_code_prefix="MEASUREMENT",
        iri=["http://purl.obolibrary.org/obo/OBI_0000070"],
    )


class Calibration(Experiment):
    defs = ObjectTypeDef(
        code="CALIBRATION",
        description="A Calibration is an experiment that establishes or adjusts the mapping between measurement outputs and reference standards.",
        generated_code_prefix="CALIBRATION",
        prev_versions=["CALIBRATION:v0"],
    )

    calibration_date = PropertyTypeAssignment(
        code="CALIBRATION_DATE",
        data_type="TIMESTAMP",
        property_label="Calibration date",
        description="Date of calibration",
        mandatory=False,
        section="Calibration Details",
    )

    calibration_provider = PropertyTypeAssignment(
        code="CALIBRATION_PROVIDER",
        data_type="VARCHAR",
        property_label="Calibration provider",
        description="Organization or service that performed the calibration",
        mandatory=False,
        section="Calibration Details",
    )

    calibration_certificate_number = PropertyTypeAssignment(
        code="CALIBRATION_CERTIFICATE_NUMBER",
        data_type="VARCHAR",
        property_label="Calibration certificate number",
        description="Number of the calibration certificate",
        mandatory=False,
        section="Calibration Details",
    )

    accredited_calibration_lab = PropertyTypeAssignment(
        code="ACCREDITATED_CALIBRATION_LAB",
        data_type="BOOLEAN",
        property_label="Accredited calibration laboratory",
        description="Whether the calibration was performed by an accredited calibration laboratory",
        mandatory=False,
        section="Calibration Details",
    )

    calibration_lab_accreditation_number = PropertyTypeAssignment(
        code="CALIBRATION_LAB_ACCREDITATION_NUMBER",
        data_type="VARCHAR",
        property_label="Calibration laboratory accreditation number",
        description="Accreditation number of the calibration laboratory",
        mandatory=False,
        section="Calibration Details",
    )


class Synthesis(Experiment):
    defs = ObjectTypeDef(
        code="SYNTHESIS",
        description="An experiment that creates or assembles materials through chemical or physical means",
        generated_code_prefix="SYNTHESIS",
    )


class Test(Experiment):  # needs clarification # do we need test and measurement
    defs = ObjectTypeDef(
        code="TEST",
        description="An experiment that subjects materials to specific conditions to evaluate their performance, reliability, or compliance with standards",
        generated_code_prefix="TEST",
    )
