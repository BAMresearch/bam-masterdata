from bam_masterdata.datamodel.v1.base_objects import Entity
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment


class Context(Entity):
    defs = ObjectTypeDef(
        code="ENTITY.CONTEXT",
        description="An (information content) entity representing information that is"
        " about entities or activities and provides descriptive, configurational, or "
        "classificatory context",
        description_de="Eine (Informationsinhalts-)Entität, die Informationen über "
        "Entitäten oder Aktivitäten darstellt und beschreibenden, konfigurativen oder"
        "klassifikatorischen Kontext liefert",
        generated_code_prefix="ENT.CTX",
        ontodefs=[
            "http://purl.obolibrary.org/obo/IAO_0000030",
        ],
    )


class Location(Entity):
    defs = ObjectTypeDef(
        code="ENTITY.LOCATION",
        description="An entity that represents a physical or spatial place where one or more entities or activities are located or occurred",
        description_de="Eine Entität, die einen physischen oder räumlichen Ort darstellt, an dem sich eine oder mehrere Entitäten oder Aktivitäten befinden oder stattgefunden haben",
        generated_code_prefix="ENT.LOC",
        ontodefs=[
            "http://purl.obolibrary.org/obo/BFO_0000029",
        ],
    )

    # NOTE: the Miro board specifies `coordinates (json)`, but openBIS has no JSON data
    # type (see the `DataType` enum). Stored as free text holding a JSON document.
    coordinates = PropertyTypeAssignment(
        code="COORDINATES",
        data_type="MULTILINE_VARCHAR",
        property_label="Coordinates",
        description="Coordinates of the location, as a JSON document",
        description_de="Koordinaten des Ortes, als JSON-Dokument",
        mandatory=False,
        section="Location Details",
    )


class MaterialEntity(Entity):
    defs = ObjectTypeDef(
        code="ENTITY.MATERIAL_ENTITY",
        description="An (independent continuant) entity that has some portion of matter as a proper or improper continuant part, and persists through time while possibly gaining or losing parts",
        description_de="Eine (unabhängig fortdauernde) Entität, die einen Teil der Materie als eigentlichen oder uneigentlichen fortdauernden Bestandteil hat und über die Zeit fortbesteht, während sie möglicherweise Bestandteile gewinnt oder verliert",
        generated_code_prefix="ENT.MAT",
        ontodefs=[
            "http://purl.obolibrary.org/obo/BFO_0000040",
        ],
    )
