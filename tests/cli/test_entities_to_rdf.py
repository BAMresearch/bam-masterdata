import os

from rdflib import Graph, Literal
from rdflib.namespace import DC, OWL, RDF, RDFS

from bam_masterdata.cli.entities_to_rdf import BAM, entities_to_rdf, rdf_graph_init
from bam_masterdata.logger import logger


def test_rdf_init():
    """
    Test the `rdf_graph_init` function.
    """
    graph = Graph()
    rdf_graph_init(graph)

    # Test how many nodes initialize in the graph
    assert len(graph) == 30

    # Check if base namespaces are bound correctly.
    expected_namespaces = {"dc", "owl", "rdf", "rdfs", "bam", "prov"}
    bound_namespaces = {prefix for prefix, _ in graph.namespaces()}
    expected_namespaces.issubset(bound_namespaces)

    # Ensure standard annotation properties exist with correct types.
    annotation_props = [RDFS.label, RDFS.comment, DC.identifier]
    for prop in annotation_props:
        assert (prop, RDF.type, OWL.AnnotationProperty) in graph

    # Verify bam:dataType and bam:propertyLabel exist with labels and comments.
    custom_props = {
        BAM["dataType"]: "Represents the data type of a property",
        BAM["propertyLabel"]: "A UI-specific annotation used in openBIS",
    }
    for prop, comment_start in custom_props.items():
        assert (prop, RDF.type, OWL.AnnotationProperty) in graph
        assert (
            prop,
            RDFS.label,
            Literal(f"bam:{prop.split('/')[-1]}", lang="en"),
        ) in graph
        assert any(
            o.startswith(comment_start)
            for _, _, o in graph.triples((prop, RDFS.comment, None))
        )

    # Check that BAM object properties exist and have correct characteristics.
    bam_props = {
        BAM["hasMandatoryProperty"]: "The property must be mandatorily filled",
        BAM["hasOptionalProperty"]: "The property is optionally filled",
        BAM["referenceTo"]: "The property is referencing an object",
    }
    for prop, comment_start in bam_props.items():
        assert (prop, RDF.type, OWL.ObjectProperty) in graph
        assert any(
            o.startswith(comment_start)
            for _, _, o in graph.triples((prop, RDFS.comment, None))
        )

    # Ensure PropertyType and related objects exist with labels and comments.
    prop_type_uri = BAM["PropertyType"]
    assert (prop_type_uri, RDF.type, OWL.Thing) in graph
    assert (prop_type_uri, RDFS.label, Literal("PropertyType", lang="en")) in graph
    assert any(
        o.startswith("A conceptual placeholder used to define")
        for _, _, o in graph.triples((prop_type_uri, RDFS.comment, None))
    )


def test_entities_to_rdf():
    module_name = "object_types"  # ! only one module for testing
    module_path = os.path.join("./bam_masterdata/datamodel", f"{module_name}.py")

    graph = Graph()
    rdf_graph_init(graph)
    entities_to_rdf(graph=graph, module_path=module_path, logger=logger)

    # Testing
    # ! this number is subject to change as the datamodel evolves
    assert len(graph) == 11910

    # Check Instrument entity
    instrument_uri = BAM["Instrument"]
    assert (instrument_uri, RDF.type, OWL.Thing) in graph
    assert (instrument_uri, RDFS.label, Literal("Instrument", lang="en")) in graph
    assert (
        instrument_uri,
        RDFS.comment,
        Literal("Measuring Instrument", lang="en"),
    ) in graph
    assert (
        instrument_uri,
        RDFS.comment,
        Literal("Messgerät", lang="de"),
    ) in graph

    # Check Camera entity (subclass of Instrument)
    camera_uri = BAM["Camera"]
    assert (camera_uri, RDF.type, OWL.Thing) in graph
    assert (camera_uri, RDFS.subClassOf, instrument_uri) in graph
    assert (camera_uri, RDFS.label, Literal("Camera", lang="en")) in graph
    assert (
        camera_uri,
        RDFS.comment,
        Literal("A generic camera  device for recording video or photos", lang="en"),
    ) in graph
    assert (
        camera_uri,
        RDFS.comment,
        Literal("Eine generische Kamera für Video- oder Fotoaufnahmen", lang="de"),
    ) in graph
