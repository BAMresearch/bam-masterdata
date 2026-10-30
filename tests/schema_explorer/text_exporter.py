import json

import pytest

from bam_masterdata.schema_explorer.exporter import (
    export_schema,
    write_schema,
)
from bam_masterdata.schema_explorer.models import SchemaExport


@pytest.mark.parametrize("version", ["v0", "v1"])
def test_export_schema(version):
    schema = export_schema(version)

    assert isinstance(schema, SchemaExport)
    assert schema.version == version
    assert schema.nodes

    node_ids = [node.id for node in schema.nodes]

    assert len(node_ids) == len(set(node_ids))

    for node in schema.nodes:
        assert node.id
        assert node.name
        assert node.hierarchy
        assert node.hierarchy.split(".")[-1] or node.id


@pytest.mark.parametrize("version", ["v0", "v1"])
def test_inheritance_edges(version):
    schema = export_schema(version)

    node_ids = {node.id for node in schema.nodes}

    for edge in schema.edges:
        if edge.type != "inheritance":
            continue

        assert edge.source in node_ids
        assert edge.target in node_ids
        assert edge.source != edge.target


def test_v1_activity_hierarchy():
    schema = export_schema("v1")

    nodes = {node.id: node for node in schema.nodes}

    assert "ROOT" in nodes
    assert "ACTIVITY" in nodes

    assert nodes["Activity".upper()].hierarchy == "ROOT.ACTIVITY"

    assert any(
        edge.source == "ROOT"
        and edge.target == "ACTIVITY"
        and edge.type == "inheritance"
        for edge in schema.edges
    )


def test_v1_object_references():
    schema = export_schema("v1")

    assert any(
        edge.source == "ACTIVITY"
        and edge.target == "PERSON"
        and edge.type == "object_reference"
        and edge.property_code == "RESPONSIBLE_PERSONS"
        for edge in schema.edges
    )


@pytest.mark.parametrize("version", ["v0", "v1"])
def test_export_deterministic(version):
    first = export_schema(version)
    second = export_schema(version)

    assert first.model_dump() == second.model_dump()


@pytest.mark.parametrize("version", ["v0", "v1"])
def test_write_schema(version, tmp_path):
    output = tmp_path / f"schema-{version}.json"

    write_schema(version, output)

    assert output.exists()

    data = json.loads(output.read_text(encoding="utf-8"))

    assert data["version"] == version
    assert data["nodes"]
    assert "edges" in data


def test_v1_multivalued_object_reference():
    schema = export_schema("v1")

    edges = [
        edge
        for edge in schema.edges
        if edge.source == "ACTIVITY"
        and edge.target == "PERSON"
        and edge.property_code == "RESPONSIBLE_PERSONS"
    ]

    assert len(edges) == 1
    assert edges[0].multivalued is True
