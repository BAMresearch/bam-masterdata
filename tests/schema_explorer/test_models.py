import json

import pytest
from pydantic import ValidationError

from bam_masterdata.metadata.definitions import PropertyTypeAssignment
from bam_masterdata.schema_explorer.models import (
    SchemaEdge,
    SchemaExport,
    SchemaNode,
)


def test_schema_node():
    node = SchemaNode(
        id="ACTIVITY",
        name="Activity",
        description="An activity.",
        hierarchy="ROOT.ACTIVITY",
    )

    assert node.id == "ACTIVITY"
    assert node.hierarchy == "ROOT.ACTIVITY"
    assert node.properties == []
    assert node.iri == []


def test_schema_node_with_properties():
    prop = PropertyTypeAssignment(
        code="START_DATE",
        data_type="TIMESTAMP",
        property_label="Start date",
        description="Start of the activity.",
        mandatory=False,
        section="Activity Details",
    )

    node = SchemaNode(
        id="ACTIVITY",
        name="Activity",
        description="An activity.",
        hierarchy="ROOT.ACTIVITY",
        properties=[prop],
    )

    assert len(node.properties) == 1
    assert node.properties[0].code == "START_DATE"


@pytest.mark.parametrize("version", ["v0", "v1"])
def test_schema_export_versions(version):
    schema = SchemaExport(version=version)

    assert schema.version == version


def test_invalid_schema_version():
    with pytest.raises(ValidationError):
        SchemaExport(version="v999")


def test_schema_edges():
    inheritance = SchemaEdge(
        source="ROOT",
        target="ACTIVITY",
        type="inheritance",
    )

    reference = SchemaEdge(
        source="ACTIVITY",
        target="PERSON",
        type="object_reference",
        property_code="RESPONSIBLE_PERSONS",
    )

    assert inheritance.type == "inheritance"
    assert reference.property_code == "RESPONSIBLE_PERSONS"


def test_invalid_edge_type():
    with pytest.raises(ValidationError):
        SchemaEdge(
            source="ROOT",
            target="ACTIVITY",
            type="unknown",
        )


def test_schema_json_serialization():
    schema = SchemaExport(
        version="v1",
        nodes=[
            SchemaNode(
                id="ROOT",
                name="Root",
                description="Root object type.",
                hierarchy="ROOT",
            ),
        ],
    )

    data = json.loads(schema.model_dump_json())

    assert data["version"] == "v1"
    assert data["nodes"][0]["id"] == "ROOT"
    assert data["edges"] == []


def test_multivalued_reference_edge():
    edge = SchemaEdge(
        source="ACTIVITY",
        target="PERSON",
        type="object_reference",
        property_code="RESPONSIBLE_PERSONS",
        multivalued=True,
    )

    assert edge.multivalued is True
    assert edge.model_dump()["multivalued"] is True


def test_mandatory_reference_edge():
    edge = SchemaEdge(
        source="ACTIVITY",
        target="PERSON",
        type="object_reference",
        property_code="RESPONSIBLE_PERSONS",
        mandatory=True,
    )

    assert edge.mandatory is True
    assert edge.model_dump()["mandatory"] is True
