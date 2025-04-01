import inspect
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from rdflib import Graph
    from structlog._config import BoundLoggerLazyProxy

import click
from rdflib import Literal, Namespace
from rdflib.namespace import DC, OWL, RDF, RDFS

from bam_masterdata.utils import import_module

BAM = Namespace("https://bamresearch.github.io/bam-masterdata/#")
PROV = Namespace("http://www.w3.org/ns/prov#")


def rdf_graph_init(g: "Graph") -> None:
    """
    Initialize the RDF graph with base namespaces, annotation properties, and internal BAM properties. This
    function also creates placeholders for PropertyType and other entity types. The graph is to be printed out
    in RDF/XML format in the `entities_to_rdf` function.

    Args:
        g (Graph): The RDF graph to be initialized.
    """
    # Adding base namespaces
    g.bind("dc", DC)
    g.bind("owl", OWL)
    g.bind("rdf", RDF)
    g.bind("rdfs", RDFS)
    g.bind("bam", BAM)
    g.bind("prov", PROV)

    # Adding annotation properties from base namespaces
    annotation_props = [
        RDFS.label,
        RDFS.comment,
        DC.identifier,
    ]
    for prop in annotation_props:
        g.add((prop, RDF.type, OWL.AnnotationProperty))

    # Custom annotation properties from openBIS: `dataType`, `propertyLabel
    custom_annotation_props = {
        BAM[
            "dataType"
        ]: """Represents the data type of a property as defined in the openBIS platform.
        This annotation is used to ensure alignment with the native data types in openBIS,
        facilitating seamless integration and data exchange.

        The allowed values for this annotation correspond directly to the openBIS type system,
        including BOOLEAN, CONTROLLEDVOCABULARY, DATE, HYPERLINK, INTEGER, MULTILINE_VARCHAR, OBJECT,
        REAL, TIMESTAMP, VARCHAR, and XML.

        While `bam:dataType` is primarily intended for internal usage with openBIS, mappings to
        standard vocabularies such as `xsd` (e.g., `xsd:boolean`, `xsd:string`) are possible to use and documented to
        enhance external interoperability. The full mapping is:
        - BOOLEAN: xsd:boolean
        - CONTROLLEDVOCABULARY: xsd:string
        - DATE: xsd:date
        - HYPERLINK: xsd:anyURI
        - INTEGER: xsd:integer
        - MULTILINE_VARCHAR: xsd:string
        - OBJECT: bam:ObjectType
        - REAL: xsd:decimal
        - TIMESTAMP: xsd:dateTime
        - VARCHAR: xsd:string
        - XML: xsd:string""",
        BAM[
            "propertyLabel"
        ]: """A UI-specific annotation used in openBIS to provide an alternative label for a property
        displayed in the frontend. Not intended for semantic reasoning or interoperability beyond openBIS.""",
    }
    for custom_prop, custom_prop_def in custom_annotation_props.items():
        g.add((custom_prop, RDF.type, OWL.AnnotationProperty))
        g.add(
            (
                custom_prop,
                RDFS.label,
                Literal(f"bam:{custom_prop.split('/')[-1]}", lang="en"),
            )
        )
        g.add((custom_prop, RDFS.comment, Literal(custom_prop_def, lang="en")))

    # Internal BAM properties
    # ? `section`, `ordinal`, `show_in_edit_views`?
    bam_props_uri = {
        BAM["hasMandatoryProperty"]: [
            (RDF.type, OWL.ObjectProperty),
            # (RDFS.domain, OWL.Class),
            (RDFS.range, BAM.PropertyType),
            (RDFS.label, Literal("hasMandatoryProperty", lang="en")),
            (
                RDFS.comment,
                Literal(
                    "The property must be mandatorily filled when creating the object in openBIS.",
                    lang="en",
                ),
            ),
        ],
        BAM["hasOptionalProperty"]: [
            (RDF.type, OWL.ObjectProperty),
            # (RDFS.domain, OWL.Class),
            (RDFS.range, BAM.PropertyType),
            (RDFS.label, Literal("hasOptionalProperty", lang="en")),
            (
                RDFS.comment,
                Literal(
                    "The property is optionally filled when creating the object in openBIS.",
                    lang="en",
                ),
            ),
        ],
        BAM["referenceTo"]: [
            (RDF.type, OWL.ObjectProperty),
            (RDFS.domain, BAM.PropertyType),  # Restricting domain to PropertyType
            # (RDFS.range, OWL.Class),  # Explicitly setting range to ObjectType
            (RDFS.label, Literal("referenceTo", lang="en")),
            (
                RDFS.comment,
                Literal(
                    "The property is referencing an object existing in openBIS.",
                    lang="en",
                ),
            ),
        ],
    }
    for prop_uri, obj_properties in bam_props_uri.items():
        for prop in obj_properties:  # type: ignore
            g.add((prop_uri, prop[0], prop[1]))  # type: ignore

    # Adding base PropertyType and other objects as placeholders
    # ! add only PropertyType
    prop_type_description = """A conceptual placeholder used to define and organize properties as first-class entities.
        PropertyType is used to place properties and define their metadata, separating properties from the
        entities they describe.

        In integration scenarios:
        - PropertyType can align with `BFO:Quality` for inherent attributes.
        - PropertyType can represent `BFO:Role` if properties serve functional purposes.
        - PropertyType can be treated as a `prov:Entity` when properties participate in provenance relationships."""
    for entity in ["PropertyType", "ObjectType", "CollectionType", "DatasetType"]:
        entity_uri = BAM[entity]
        g.add((entity_uri, RDF.type, OWL.Thing))
        g.add((entity_uri, RDFS.label, Literal(entity, lang="en")))
        if entity == "PropertyType":
            g.add((entity_uri, RDFS.comment, Literal(prop_type_description, lang="en")))


def entities_to_rdf(
    graph: "Graph", module_path: str, logger: "BoundLoggerLazyProxy"
) -> None:
    """
    Convert the entities defined in the specified module to RDF triples and add them to the graph. The function
    uses the `model_to_rdf` method defined in each class to convert the class attributes to RDF triples. The
    function also adds the PropertyType and other entity types as placeholders in the graph.

    Args:
        graph (Graph): The RDF graph to which the entities are added.
        module_path (str): The path to the module containing the entities to be converted.
        logger (BoundLoggerLazyProxy): The logger to log messages.
    """
    rdf_graph_init(graph)

    module = import_module(module_path=module_path)

    # All datamodel modules
    # OBJECT/DATASET/COLLECTION TYPES
    # skos:prefLabel used for class names
    # skos:definition used for `description` (en, de)
    # dc:identifier used for `code`  # ! only defined for internal codes with $ symbol
    # parents defined from `code`
    # assigned properties can be Mandatory or Optional, can be PropertyType or ObjectType
    # ? For OBJECT TYPES
    # ? `generated_code_prefix`, `auto_generated_codes`?
    for name, obj in inspect.getmembers(module, inspect.isclass):
        # Ensure the class has the `model_to_rdf` method
        if not hasattr(obj, "defs") or not callable(getattr(obj, "model_to_rdf")):
            continue
        try:
            # Instantiate the class and call the method
            entity = obj()
            entity.model_to_rdf(namespace=BAM, graph=graph, logger=logger)
        except Exception as err:
            click.echo(f"Failed to process class {name} in {module_path}: {err}")
