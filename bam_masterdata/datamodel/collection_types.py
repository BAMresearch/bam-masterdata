from bam_masterdata.metadata.definitions import CollectionTypeDef
from bam_masterdata.metadata.entities import CollectionType


class Collection(CollectionType):
    defs = CollectionTypeDef(
        code="COLLECTION",
        description="""""",
    )


class DefaultExperiment(CollectionType):
    defs = CollectionTypeDef(
        code="DEFAULT_EXPERIMENT",
        description="""""",
        validation_script="DEFAULT_EXPERIMENT.date_range_validation",
    )


class MeasurementsCollection(CollectionType):
    defs = CollectionTypeDef(
        code="MEASUREMENTS_COLLECTION",
        description="""Contains individual measurements, common metadata//Enthält individuelle Messungen, gemeinsame Metadaten""",
    )
