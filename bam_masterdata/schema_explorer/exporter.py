from pathlib import Path

from bam_masterdata.checker.schema_validator import get_object_types
from bam_masterdata.metadata.definitions import (
    ObjectTypeDef,
    PropertyTypeAssignment,
)
from bam_masterdata.metadata.entities import ObjectType
from bam_masterdata.schema_explorer.models import (
    SchemaEdge,
    SchemaExport,
    SchemaNode,
)


def export_schema(version: str) -> SchemaExport:
    """
    Export object type definitions and relationships for a datamodel version.

    Args:
        version (str): The version of the datamodel/vX folder to export.

    Returns:
        (SchemaExport): The exported schema.
    """

    object_types = get_object_types(version)
    known_codes = {cls.defs.code for cls in object_types}

    nodes = []
    edges = []

    for cls in object_types:
        # Reuse existing serialization.
        instance = cls()
        definition = instance.model_to_dict()

        # Extract which class the property originates from (inherited or defined)
        property_origins = {}
        for base in cls.__mro__:
            if base is ObjectType:
                break

            for value in base.__dict__.values():
                if isinstance(value, PropertyTypeAssignment):
                    property_origins.setdefault(value.code, base.defs.code)

        node = SchemaNode(
            id=cls.defs.code,
            name=cls.__name__,
            description=cls.defs.description,
            iri=cls.defs.iri or [],
            properties=definition["properties"],
            property_origins=property_origins,
        )
        nodes.append(node)

        # Inheritance relationship.
        for parent in cls.__mro__[1:]:
            if parent is ObjectType:
                break

            parent_defs = parent.__dict__.get("defs")

            if isinstance(parent_defs, ObjectTypeDef):
                if parent_defs.code in known_codes:
                    edges.append(
                        SchemaEdge(
                            source=parent_defs.code,
                            target=cls.defs.code,
                            type="inheritance",
                        )
                    )
                break

        # OBJECT reference relationships.
        for prop in node.properties:
            if prop.data_type.value != "OBJECT":
                continue

            if prop.object_code in (None, "(ALL)"):
                continue

            edges.append(
                SchemaEdge(
                    source=cls.defs.code,
                    target=prop.object_code,
                    type="object_reference",
                    property_code=prop.code,
                    multivalued=prop.multivalued,
                    mandatory=prop.mandatory,
                )
            )

    return SchemaExport(
        version=version,
        nodes=sorted(nodes, key=lambda node: node.id),
        edges=sorted(
            edges,
            key=lambda edge: (
                edge.source,
                edge.target,
                edge.type,
                edge.property_code or "",
            ),
        ),
    )


def write_schema(version: str, output: str | Path) -> None:
    """Export the selected datamodel to a JSON file."""

    schema = export_schema(version)

    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)

    output.write_text(
        schema.model_dump_json(indent=2) + "\n",
        encoding="utf-8",
    )
