from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.entities import ObjectType

# Hierarchy of datamodel/v1:

#   Root
#   ├── Activity
#   │   ├── Experiment   (see `activities.py`)
#   │   └── Computation  (see `activities.py`)
#   └── Entity
#       ├── Context         (see `entities.py`)
#       ├── Location        (see `entities.py`)
#       └── Material Entity (see `entities.py`)


class Root(ObjectType):
    defs = ObjectTypeDef(
        code="ROOT",
        description="A Root is an entity that encompasses all material entities, information entities, "
        "and activities, serving as the common superclass for all object types in the schema.",
        generated_code_prefix="ROOT",
        prev_versions=["ENTRY:v0"],
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="Human-readable name identifying the object.",
        mandatory=True,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="Text describing the object and its relevant characteristics.",
        mandatory=False,
        section="General Information",
    )

    external_identifiers = PropertyTypeAssignment(
        code="EXTERNAL_IDENTIFIER",
        data_type="VARCHAR",
        property_label="External identifiers",
        description="Identifiers assigned to the object by external systems, such as a DOI or database accession number.",
        mandatory=False,
        section="General Information",
        multivalued=True,
    )

    hash = PropertyTypeAssignment(
        code="HASH",
        data_type="VARCHAR",
        property_label="Hash",
        description="Cryptographic hash used to identify or verify the content associated with the object.",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    external_references = PropertyTypeAssignment(
        code="EXTERNAL_REFERENCE",
        data_type="MULTILINE_VARCHAR",
        property_label="External references",
        description="References to external resources related to the object, such as publications or documentation.",
        mandatory=False,
        section="General Information",
        multivalued=True,
    )

    ontology_iri = PropertyTypeAssignment(
        code="ONTOLOGY_IRI",
        data_type="VARCHAR",
        property_label="Ontology IRI",
        description="IRI of an ontology concept used to describe or classify the object.",
        mandatory=False,
        section="General Information",
    )

    prev_permid = PropertyTypeAssignment(
        code="PREV_PERMID",
        data_type="VARCHAR",
        property_label="Previous permID",
        description="Permanent identifier of the corresponding object in a previous openBIS system.",
        mandatory=False,
        section="General Information",
    )


class Activity(Root):
    defs = ObjectTypeDef(
        code="ACTIVITY",
        description="An Activity is an entity that represents a process or action occurring over a period of time, "
        "involving one or more entities and resulting in one or more outcomes.",
        generated_code_prefix="ACT",
        prev_versions=["EXPERIMENTAL_STEP:v0"],
        iri=[
            "http://purl.obolibrary.org/obo/BFO_0000015",
            "http://www.w3.org/ns/prov#Activity",
        ],
    )

    start_date = PropertyTypeAssignment(
        code="START_DATE",
        data_type="TIMESTAMP",
        property_label="Start date",
        description="Date and time when the activity started.",
        mandatory=False,
        section="Activity Details",
    )

    end_date = PropertyTypeAssignment(
        code="END_DATE",
        data_type="TIMESTAMP",
        property_label="End date",
        description="Date and time when the activity ended.",
        mandatory=False,
        section="Activity Details",
    )

    activity_status = PropertyTypeAssignment(
        code="ACTIVITY_STATUS",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="ACTIVITY_STATUS",
        property_label="Activity Status",
        description="Current lifecycle status of the activity, such as planned, in progress, or completed.",
        mandatory=False,
        section="Activity Details",
    )

    responsible_persons = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSONS",
        data_type="OBJECT",
        object_code="PERSON",
        property_label="Responsible Persons",
        description="Persons responsible for performing or executing the activity.",
        mandatory=False,
        section="Activity Details",
        multivalued=True,
    )

    objective = PropertyTypeAssignment(
        code="OBJECTIVE",
        data_type="MULTILINE_VARCHAR",
        property_label="Objective",
        description="Intended goal or purpose of the activity.",
        mandatory=False,
        section="Activity Details",
    )

    activity_sheet = PropertyTypeAssignment(
        code="ACTIVITY_SHEET",
        data_type="XML",
        property_label="Activity sheet",
        description="Structured spreadsheet used to record information about the activity.",
        mandatory=False,
        section="Activity Details",
    )

    inputs = PropertyTypeAssignment(
        code="INPUT",
        data_type="OBJECT",
        object_code="ENTITY",
        property_label="Inputs",
        description="Entities used or consumed by the activity, such as samples, materials, or instruments.",
        mandatory=False,
        section="Inputs and Outputs",
        multivalued=True,
    )

    outputs = PropertyTypeAssignment(
        code="OUTPUT",
        data_type="OBJECT",
        object_code="ENTITY",
        property_label="Outputs",
        description="Entities generated or modified by the activity, such as processed samples or simulation results.",
        mandatory=False,
        section="Inputs and Outputs",
        multivalued=True,
    )


class Entity(Root):
    defs = ObjectTypeDef(
        code="ENTITY",
        description="An Entity is a physical, digital, conceptual, or other kind of thing with some "
        "fixed aspects; entities may be tangible or intangible.",
        generated_code_prefix="ENT",
        iri=[
            "http://purl.obolibrary.org/obo/BFO_0000002",
            "http://www.w3.org/ns/prov#Entity",
        ],
    )
