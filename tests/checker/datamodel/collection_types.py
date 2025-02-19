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

    default_object_type = PropertyTypeAssignment(
        code="$DEFAULT_OBJECT_TYPE",
        data_type="VARCHAR",
        property_label="Default object type",
        description="""Enter the code of the object type for which the collection is used""",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
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

    default_experiment_experimental_goals = PropertyTypeAssignment(
        code="DEFAULT_EXPERIMENT.EXPERIMENTAL_GOALS",
        data_type="MULTILINE_VARCHAR",
        property_label="Goals",
        description="""Goals of the experiment""",
        mandatory=False,
        show_in_edit_views=False,
        section="Experimental details",
    )
