from bam_masterdata.metadata.definitions import CollectionTypeDef
from bam_masterdata.metadata.entities import CollectionType


class Collection(CollectionType):
    defs = CollectionTypeDef(
        code='COLLECTION',
        description='',
    )


class DefaultExperiment(CollectionType):
    defs = CollectionTypeDef(
        code='DEFAULT_EXPERIMENT',
        description='',
        validation_script='DEFAULT_EXPERIMENT.date_range_validation',
    )


class DropboxCollection(CollectionType):
    defs = CollectionTypeDef(
        code='DROPBOX_COLLECTION',
        description='Test collection type to test collection properties in dropboxsystem',
    )
