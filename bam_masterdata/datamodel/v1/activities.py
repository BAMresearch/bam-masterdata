from bam_masterdata.datamodel.v1.base_objects import Activity
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment


class Experiment(Activity):
    defs = ObjectTypeDef(
        code="ACTIVITY.EXPERIMENT",
        description="An activity that acquires and records observations, measurements, or results for scientific analysis",
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


class Computation(Activity):
    defs = ObjectTypeDef(
        code="ACTIVITY.COMPUTATION",
        description="An activity that performs computational operations using a computing environment to produce one or more outputs",
        description_de="Eine Aktivität, die rechnerische Operationen in einer Rechenumgebung durchführt, um eine oder mehrere Ausgaben zu erzeugen",
        generated_code_prefix="ACT.COMP",
        prev_version=["COMPUTATIONAL_ANALYSIS"],
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
        metadata={"multivalued": True},
    )
