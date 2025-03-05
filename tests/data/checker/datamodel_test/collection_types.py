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

    default_collection_view = PropertyTypeAssignment(
        code="$DEFAULT_COLLECTION_VIEW",
        data_type="CONTROLLEDVOCABULARY",
        property_label="Default collection view",
        description="""Default view for experiments of the type collection""",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
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

    default_experiment_experimental_results = PropertyTypeAssignment(
        code="DEFAULT_EXPERIMENT.EXPERIMENTAL_RESULTS",
        data_type="MULTILINE_VARCHAR",
        property_label="Results",
        description="""Summary of  experimental results""",
        mandatory=False,
        show_in_edit_views=False,
        section="Experimental details",
    )

    default_experiment_grant = PropertyTypeAssignment(
        code="DEFAULT_EXPERIMENT.GRANT",
        data_type="VARCHAR",
        property_label="Grant",
        description="""Grant""",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
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

    end_date = PropertyTypeAssignment(
        code="END_DATE",
        data_type="TIMESTAMP",
        property_label="End date",
        description="""End date//Enddatum""",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    finished_flag = PropertyTypeAssignment(
        code="FINISHED_FLAG",
        data_type="BOOLEAN",
        property_label="Experiment completed",
        description="""Marks the experiment as finished//Markiert das Experiment als abgeschlossen""",
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

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes//Notizen""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )

    publication = PropertyTypeAssignment(
        code="PUBLICATION",
        data_type="MULTILINE_VARCHAR",
        property_label="Publication",
        description="""Own publication where this entity is referenced//Eigene Publikation, in dem dieses Experiment beschrieben wird""",
        mandatory=False,
        show_in_edit_views=False,
        section="References",
    )

    reference = PropertyTypeAssignment(
        code="REFERENCE",
        data_type="MULTILINE_VARCHAR",
        property_label="References",
        description="""Useful refences//Nützliche Referenzen""",
        mandatory=False,
        show_in_edit_views=False,
        section="References",
    )

    show_in_project_overview = PropertyTypeAssignment(
        code="$SHOW_IN_PROJECT_OVERVIEW",
        data_type="BOOLEAN",
        property_label="Show in project overview",
        description="""Show in project overview page""",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    start_date = PropertyTypeAssignment(
        code="START_DATE",
        data_type="TIMESTAMP",
        property_label="Start date",
        description="""Start date//Startdatum""",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )
