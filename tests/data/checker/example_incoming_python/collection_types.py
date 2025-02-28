from bam_masterdata.metadata.definitions import (
    CollectionTypeDef,
    PropertyTypeAssignment,
)
from bam_masterdata.metadata.entities import CollectionType


class Collection(CollectionType):
    defs = CollectionTypeDef(
        code="COLLECTION",
        description="""""",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )


class DefaultExperiment(CollectionType):
    defs = CollectionTypeDef(
        code="DEFAULT_EXPERIMENT",
        description="""""",
        validation_script="DEFAULT_EXPERIMENT.date_range_validation",
    )

    default_experiment_experimental_description = PropertyTypeAssignment(
        code="DEFAULT_EXPERIMENT.EXPERIMENTAL_DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Description of the experiment""",
        mandatory=False,
        show_in_edit_views=False,
        section="Experimental details",
    )
