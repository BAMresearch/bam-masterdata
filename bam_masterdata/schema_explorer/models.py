from typing import Literal

from pydantic import BaseModel, Field

from bam_masterdata.metadata.definitions import PropertyTypeAssignment


class SchemaNode(BaseModel):
    """Representation of an object type node in the schema explorer."""

    id: str
    name: str
    description: str
    hierarchy: str

    iri: list[str] = Field(default_factory=list)

    properties: list[PropertyTypeAssignment] = Field(default_factory=list)


class SchemaEdge(BaseModel):
    """Relationship between two object types nodes."""

    source: str
    target: str

    type: Literal["inheritance", "object_reference"]

    property_code: str | None = None
    multivalued: bool = False
    mandatory: bool = False


class SchemaExport(BaseModel):
    """Exported schema for a specific datamodel version."""

    version: Literal["v0", "v1"]

    nodes: list[SchemaNode] = Field(default_factory=list)
    edges: list[SchemaEdge] = Field(default_factory=list)
