from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.entities import ObjectType

# Hierarchy of datamodel/v1:

#   Root
#   ├── Activity
#   │   ├── Experiment   (see `activities.py`)
#   │   └── Computation  (see `activities.py`)
#   └── Entity
#       ├── Context         (see `entities.py`)
#       ├──  Location       (see `entities.py`)
#       └── Material Entity (see `entities.py`)


class Root(ObjectType):
    defs = ObjectTypeDef(
        code="ROOT",
        description="Root of the masterdata hierarchy",
        description_de="Wurzel der Masterdaten-Hierarchie",
        generated_code_prefix="ROOT",
        prev_versions=["ENTRY:v0"],
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="Name",
        description_de="Namen",
        mandatory=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="Detailed description of the entry",
        description_de="Ausführliche Beschreibung des Eintrags",
        mandatory=False,
        section="General Information",
    )

    external_identifiers = PropertyTypeAssignment(
        code="EXTERNAL_IDENTIFIERS",
        data_type="VARCHAR",
        property_label="External identifiers",
        description="Identifiers of the entry in external systems",
        description_de="Kennungen des Eintrags in externen Systemen",
        mandatory=False,
        section="General Information",
        multivalued=True,
    )

    hash = PropertyTypeAssignment(
        code="HASH",
        data_type="VARCHAR",
        property_label="Hash",
        description="Hash value associated with the entry",
        description_de="Dem Eintrag zugeordneter Hashwert",
        mandatory=False,
        section="General Information",
    )

    external_references = PropertyTypeAssignment(
        code="EXTERNAL_REFERENCES",
        data_type="MULTILINE_VARCHAR",
        property_label="External references",
        description="References to external resources",
        description_de="Verweise auf externe Ressourcen",
        mandatory=False,
        section="General Information",
        multivalued=True,
    )

    ontology_iri = PropertyTypeAssignment(
        code="ONTOLOGY_IRI",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="ONTOLOGY_IRI",
        property_label="Ontology IRI",
        description="IRI of the ontology concept associated with the entry",
        description_de="IRI des dem Eintrag zugeordneten Ontologiekonzepts",
        mandatory=False,
        section="General Information",
    )

    prev_permid = PropertyTypeAssignment(
        code="PREV_PERMID",
        data_type="VARCHAR",
        property_label="Previous permID",
        description="Previous permanent identifier of the entry",
        description_de="Vorherige permanente Kennung des Eintrags",
        mandatory=False,
        section="General Information",
    )


class Activity(Root):
    defs = ObjectTypeDef(
        code="ACTIVITY",
        description="Activity",
        description_de="Activität",
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
        description="Start date",
        description_de="Startdatum",
        mandatory=False,
        section="General Information",
    )
    end_date = PropertyTypeAssignment(
        code="END_DATE",
        data_type="TIMESTAMP",
        property_label="End date",
        description="End date",
        description_de="Enddatum",
        mandatory=False,
        section="General Information",
    )
    activity_status = PropertyTypeAssignment(
        code="ACTIVITY_STATUS",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="ACTIVITY_STATUS",
        property_label="Activity Status",
        description="Activity Status",
        description_de="Aktivitätsstatus",
        mandatory=False,
        section="Activity Details",
    )
    operators = PropertyTypeAssignment(
        code="OPERATORS",
        data_type="OBJECT",
        object_code="PERSON",
        property_label="Operators",
        description="Persons performing the activity",
        description_de="Personen die Aktivität durchführen",
        mandatory=False,
        section="Activity Details",
    )

    objective = PropertyTypeAssignment(
        code="OBJECTIVE",
        data_type="MULTILINE_VARCHAR",
        property_label="Objective",
        description="Objective of the activity",
        description_de="Ziel der Aktivität",
        mandatory=False,
        section="Activity Details",
    )
    activity_sheet = PropertyTypeAssignment(
        code="ACTIVITY_SHEET",
        data_type="XML",
        property_label="Activity sheet",
        description="Activity sheet (spreadsheet)",
        description_de="Aktivitätsblatt (Tabelle)",
        mandatory=False,
        section="Activity Details",
    )

    inputs = PropertyTypeAssignment(
        code="INPUTS",
        data_type="OBJECT",
        property_label="Inputs",
        object_code="ENTITY",
        description="Entities used by the activity",
        description_de="Von der Aktivität verwendete Entitäten",
        mandatory=False,
        section="Inputs and Outputs",
    )

    outputs = PropertyTypeAssignment(
        code="OUTPUTS",
        data_type="OBJECT",
        object_code="ENTITY",
        property_label="Outputs",
        description="Entities generated by the activity",
        description_de="Von der Aktivität erzeugte Entitäten",
        mandatory=False,
        section="Inputs and Outputs",
    )


class Entity(Root):
    defs = ObjectTypeDef(
        code="ENTITY",
        description="A physical, digital, conceptual, or other kind of thing with some "
        "fixed aspects; entities may be tangible or intangible",
        description_de="Ein physisches, digitales, konzeptionelles oder anderes Ding mit "
        "bestimmten festen Aspekten; Entitäten können materiell oder immateriell sein",
        generated_code_prefix="ENT",
        iri=[
            "http://purl.obolibrary.org/obo/BFO_0000002",
            "http://www.w3.org/ns/prov#Entity",
        ],
    )
