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
        code="ACTIVITY.COMPUTATION",
        description="An activity that performs computational operations using a computing environment to produce one or more outputs",
        description_de="Eine Aktivität, die rechnerische Operationen in einer Rechenumgebung durchführt, um eine oder mehrere Ausgaben zu erzeugen",
        generated_code_prefix="ACT.COMP",
        prev_versions=["COMPUTATIONAL_ANALYSIS:v0"],
        iri=[
            # Not sure how to define here
        ],
    )

    software = PropertyTypeAssignment(
        code="SOFTWARE",
        data_type="OBJECT",
        object_code="SOFTWARE",
        property_label="Software",
        description="Software used to perform the computation",
        description_de="Software, die zur Durchführung der Berechnung verwendet wird",
        mandatory=False,
        section="Computation Details",
    )

    computational_method = PropertyTypeAssignment(
        code="COMPUTATIONAL_METHOD",
        data_type="OBJECT",
        object_code="COMPUTATIONAL_METHOD",
        property_label="Computational method",
        description="Computational methods, algorithms, and settings used during the computation, e.g. DFT Single Point or Geometry Optimization",
        description_de="Berechnungsmethoden, Algorithmen und Einstellungen, die während der Berechnung verwendet werden, z. B. DFT Single Point oder Geometrieoptimierung",
        mandatory=False,
        section="Computation Details",
        multivalued=True,
    )


class Analysis(Computation):
    # Defines no new properties; serves as a common parent for domain-specific analyses.
    defs = ObjectTypeDef(
        code="ACTIVITY.COMPUTATION.ANALYSIS",
        description="A computation that examines one or more existing inputs to derive information, properties, parameters, or other outputs",
        description_de="Eine Berechnung, die eine oder mehrere vorhandene Eingaben untersucht, um Informationen, Eigenschaften, Parameter oder andere Ausgaben abzuleiten",
        generated_code_prefix="ACT.COMP.ANA",
    )


class CreepTestDataProcessing(Analysis):
    defs = ObjectTypeDef(
        code="ACTIVITY.COMPUTATION.ANALYSIS.CREEP_TEST_DATA_PROCESSING",
        description="Data processing procedures applied to the data of a creep test",
        description_de="Datenverarbeitungsverfahren, die auf die Daten eines Zeitstandversuchs angewendet werden",
        generated_code_prefix="ACT.COMP.ANA.CREEP",  # needs info on this definition style
        prev_versions=[
            "COMPUTATIONAL_ANALYSIS.CREEP_TEST_DATA_PROCESSING_PROCEDURES:v0"
        ],
    )

    creep_test_primary_data_series = PropertyTypeAssignment(
        code="CREEP_TEST_PRIMARY_DATA_SERIES",
        data_type="VARCHAR",
        property_label="Primary data series",
        description="Primary data is data that is directly acquired by sensors or measuring instruments during or after a test. List the measured quantities and their corresponding units.",
        description_de="Primärdaten sind Daten, die während oder nach einer Prüfung direkt von Sensoren oder Messgeräten erfasst werden. Die gemessenen Größen und die zugehörigen Einheiten auflisten.",
        mandatory=False,
        section="Data Processing Procedures",
    )

    creep_test_processed_data_series = PropertyTypeAssignment(
        code="CREEP_TEST_PROCESSED_DATA_SERIES",
        data_type="VARCHAR",
        property_label="Processed data series",
        description="Processed data is obtained by applying procedures (equations, algorithms, methods, unit conversions, averaging, smoothing) to primary data. Describe the transformed quantities, their units, and the applied procedures.",
        description_de="Verarbeitete Daten entstehen durch Verfahren (Gleichungen, Algorithmen, Methoden, Einheitenumrechnungen, Mittelung, Glättung), die Primärdaten transformieren. Die transformierten Größen, deren Einheiten sowie die angewandten Verfahren beschreiben.",
        mandatory=False,
        section="Data Processing Procedures",
    )

    creep_test_procedures = PropertyTypeAssignment(
        code="CREEP_TEST_PROCEDURE",
        data_type="VARCHAR",
        property_label="Test analysis procedures",
        description="Description of the data processing and analysis procedures used to obtain specific test results, e.g. percentage elastic extension",
        description_de="Beschreibung der Datenverarbeitungs- und Analyseverfahren zur Ermittlung spezifischer Prüfergebnisse, z. B. prozentuale elastische Dehnung",
        mandatory=False,
        section="Data Processing Procedures",
    )

    automated_workflow_usage = PropertyTypeAssignment(
        code="CREEP_TEST_WORKFLOW_USAGE",  # needs checking for actual wording
        data_type="BOOLEAN",
        property_label="Automated workflow usage",
        description="Whether automated (user-independent) analysis workflows were used",
        description_de="Ob automatisierte (benutzerunabhängige) Analyse-Workflows verwendet wurden",
        mandatory=False,
        section="Data Processing Procedures",
    )


class Simulation(Computation):
    defs = ObjectTypeDef(
        code="ACTIVITY.COMPUTATION.SIMULATION",
        description="A computation that uses one or more computational models to reproduce, predict, or explore the behavior of a system under specified conditions",
        description_de="Eine Berechnung, die ein oder mehrere Rechenmodelle verwendet, um das Verhalten eines Systems unter festgelegten Bedingungen nachzubilden, vorherzusagen oder zu untersuchen",
        generated_code_prefix="ACT.COMP.SIM",
        iri=[
            "https://ocdo.github.io/asmo/#Simulation",
            "pmd:simulation process",  # needs suggestion
        ],
    )

    simulated_system = PropertyTypeAssignment(
        code="SIMULATED_SYSTEM",
        data_type="OBJECT",
        object_code="ENTITY",  # need info
        property_label="Simulated system",
        description="System being simulated, from atomistic to continuum scale",
        description_de="Simuliertes System, von atomistischer bis zur Kontinuumsskala",
        mandatory=False,
        section="Simulation Details",
        multivalued=True,
    )


class PyironJob(Simulation):
    defs = ObjectTypeDef(
        code="ACTIVITY.COMPUTATION.SIMULATION.PYIRON_JOB",
        description="A simulation run as a job managed by the pyiron workflow framework",
        description_de="Eine Simulation, die als Job im pyiron-Workflow-Framework ausgeführt wird",
        generated_code_prefix="ACT.COMP.SIM.PYI",
        prev_versions=["PYIRON_JOB:v0"],
    )

    simulation_walltime = PropertyTypeAssignment(
        code="SIM_WALLTIME_IN_HOUR",
        data_type="REAL",  # needs more info.
        property_label="Simulation walltime",
        units="h",
        description="Total run time (walltime) of the job",
        description_de="Gesamtlaufzeit (Walltime) des Jobs",
        mandatory=False,
        section="Job Details",
    )

    simulation_core_time = PropertyTypeAssignment(
        code="SIM_CORETIME_IN_HOUR",
        data_type="REAL",
        property_label="Simulation core time",
        units="h",
        description="Total core time used by the job",
        description_de="Vom Job insgesamt verbrauchte Kernzeit",
        mandatory=False,
        section="Job Details",
    )

    n_cores = PropertyTypeAssignment(
        code="NCORE",
        data_type="INTEGER",
        property_label="Number of cores",
        description="Number of cores used by the job",
        description_de="Anzahl der vom Job verwendeten Kerne",
        mandatory=False,
        section="Job Details",
    )

    n_gpus = PropertyTypeAssignment(
        code="NGPU",
        data_type="INTEGER",
        property_label="Number of GPUs",
        description="Number of GPUs used by the job",
        description_de="Anzahl der vom Job verwendeten GPUs",
        mandatory=False,
        section="Job Details",
    )

    n_threads = PropertyTypeAssignment(
        code="NTHREAD",
        data_type="INTEGER",
        property_label="Number of threads",
        description="Number of threads used by the job",
        description_de="Anzahl der vom Job verwendeten Threads",
        mandatory=False,
        section="Job Details",
    )

    hpc_job_id = PropertyTypeAssignment(
        code="HPC_JOB_ID",
        data_type="VARCHAR",
        property_label="HPC job ID",
        description="Job ID in the HPC queue",
        description_de="Job-ID in der HPC-Warteschlange",
        mandatory=False,
        section="Job Details",
    )


# Experiment branch


class Experiment(Activity):
    defs = ObjectTypeDef(
        code="ACTIVITY.EXPERIMENT",
        description="An Experiment is an activity that acquires and records observations, measurements, or results for scientific analysis ",
        description_de="Eine Aktivität, die Beobachtungen, Messungen oder Ergebnisse für die wissenschaftliche Analyse erfasst und aufzeichnet",
        generated_code_prefix="ACT.EXP",
    )

    method_name = PropertyTypeAssignment(
        code="METHOD_NAME",
        data_type="VARCHAR",
        property_label="Method name",
        description="Name of the experimental method",
        description_de="Name der experimentellen Methode",
        mandatory=False,
        section="Experiment Details",
    )

    location = PropertyTypeAssignment(
        code="LOCATION",
        data_type="OBJECT",
        object_code="ENTITY.LOCATION",
        property_label="Location",
        description="Location where the experiment takes place",
        description_de="Ort, an dem das Experiment stattfindet",
        mandatory=False,
        section="Experiment Details",
    )


class Processing(Experiment):
    defs = ObjectTypeDef(
        code="ACTIVITY.EXPERIMENT.PROCESSING",
        description="An experiment that alters the structure, composition, or form of a material",
        description_de="Ein Experiment, das die Struktur, Zusammensetzung oder Form eines Materials verändert",
        generated_code_prefix="ACT.EXP.PROC",
        prev_versions=["SAMPLE_PRETREATMENT:v0"],
    )


class Measurement(Experiment):
    defs = ObjectTypeDef(
        code="ACTIVITY.EXPERIMENT.MEASUREMENT",
        description="An experiment that uses an experimental device to produce quantitative or qualitative data about the properties of a material",
        description_de="Ein Experiment, das mit einem experimentellen Gerät quantitative oder qualitative Daten über die Eigenschaften eines Materials erzeugt",
        generated_code_prefix="ACT.EXP.MEAS",
        iri=["http://purl.obolibrary.org/obo/OBI_0000070"],
    )


class Calibration(Experiment):
    defs = ObjectTypeDef(
        code="ACTIVITY.EXPERIMENT.CALIBRATION",
        description="A Calibration is an experiment that establishes or adjusts the mapping between measurement outputs and reference standards.",
        description_de="Ein Experiment, das die Beziehung zwischen den Ausgaben eines Messgeräts und Referenzwerten ermittelt oder anpasst",
        generated_code_prefix="ACT.EXP.CAL",
        prev_versions=["CALIBRATION:v0"],
    )

    calibration_date = PropertyTypeAssignment(
        code="CALIBRATION_DATE",
        data_type="TIMESTAMP",
        property_label="Calibration date",
        description="Date of calibration",
        description_de="Datum der Kalibrierung",
        mandatory=False,
        section="Calibration Details",
    )

    calibration_provider = PropertyTypeAssignment(
        code="CALIBRATION_PROVIDER",
        data_type="VARCHAR",
        property_label="Calibration provider",
        description="Organization or service that performed the calibration",
        description_de="Organisation oder Dienstleister, der die Kalibrierung durchgeführt hat",
        mandatory=False,
        section="Calibration Details",
    )

    calibration_certificate_number = PropertyTypeAssignment(
        code="CALIBRATION_CERTIFICATE_NUMBER",
        data_type="VARCHAR",
        property_label="Calibration certificate number",
        description="Number of the calibration certificate",
        description_de="Nummer des Kalibrierscheins",
        mandatory=False,
        section="Calibration Details",
    )

    accredited_calibration_lab = PropertyTypeAssignment(
        code="ACCREDITATED_CALIBRATION_LAB",
        data_type="BOOLEAN",
        property_label="Accredited calibration laboratory",
        description="Whether the calibration was performed by an accredited calibration laboratory",
        description_de="Ob die Kalibrierung von einem akkreditierten Kalibrierlabor durchgeführt wurde",
        mandatory=False,
        section="Calibration Details",
    )

    calibration_lab_accreditation_number = PropertyTypeAssignment(
        code="CALIBRATION_LAB_ACCREDITATION_NUMBER",
        data_type="VARCHAR",
        property_label="Calibration laboratory accreditation number",
        description="Accreditation number of the calibration laboratory",
        description_de="Akkreditierungszeichen des Kalibrierlabors",
        mandatory=False,
        section="Calibration Details",
    )


class Synthesis(Experiment):
    defs = ObjectTypeDef(
        code="ACTIVITY.EXPERIMENT.SYNTHESIS",
        description="An experiment that creates or assembles materials through chemical or physical means",
        description_de="Ein Experiment, das Materialien auf chemischem oder physikalischem Weg herstellt oder zusammensetzt",
        generated_code_prefix="ACT.EXP.SYN",
    )


class Test(Experiment):  # needs clarification # do we need test and measurement
    defs = ObjectTypeDef(
        code="ACTIVITY.EXPERIMENT.TEST",
        description="An experiment that subjects materials to specific conditions to evaluate their performance, reliability, or compliance with standards",
        description_de="Ein Experiment, das Materialien bestimmten Bedingungen aussetzt, um ihre Leistung, Zuverlässigkeit oder Konformität mit Normen zu bewerten",
        generated_code_prefix="ACT.EXP.TEST",
    )
