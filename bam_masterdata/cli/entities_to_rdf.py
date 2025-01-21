import inspect
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from rdflib import Graph
    from structlog._config import BoundLoggerLazyProxy

import click
from rdflib import Literal, Namespace
from rdflib.namespace import DC, OWL, RDF, RDFS, SKOS

from bam_masterdata.utils import import_module

BAM = Namespace("http://bam.de/masterdata/")


def rdf_graph_init(g: "Graph") -> None:
    # Adding base namespaces
    g.bind("dc", DC)
    g.bind("owl", OWL)
    g.bind("rdf", RDF)
    g.bind("rdfs", RDFS)
    g.bind("skos", SKOS)
    g.bind("bam", BAM)

    # Adding annotation properties from base namespaces
    annotation_props = [
        DC.identifier,
        DC.type,
        SKOS.altLabel,
        SKOS.definition,
        SKOS.prefLabel,
    ]
    for prop in annotation_props:
        g.add((prop, RDF.type, OWL.AnnotationProperty))

    # Internal BAM properties
    # ? `section`, `ordinal`, `show_in_edit_views`?
    bam_props_uri = {
        BAM["hasMandatoryProperty"]: [
            (RDF.type, OWL.ObjectProperty),
            (RDFS.subPropertyOf, OWL.topObjectProperty),
            (RDFS.domain, OWL.Thing),
            (SKOS.prefLabel, Literal("hasMandatoryProperty", lang="en")),
        ],
        BAM["hasOptionalProperty"]: [
            (RDF.type, OWL.ObjectProperty),
            (RDFS.subPropertyOf, OWL.topObjectProperty),
            (RDFS.domain, OWL.Thing),
            (SKOS.prefLabel, Literal("hasOptionalProperty", lang="en")),
        ],
    }
    for prop_uri, obj_properties in bam_props_uri.items():
        for prop in obj_properties:
            g.add((prop_uri, prop[0], prop[1]))

    # Adding base entity types objects
    for entity in ["PropertyType", "ObjectType", "CollectionType", "DatasetType"]:
        entity_uri = BAM[entity]
        g.add((entity_uri, RDF.type, OWL.Class))
        g.add((entity_uri, SKOS.prefLabel, Literal(entity, lang="en")))

    return g


def entities_to_rdf(
    graph: "Graph", module_path: str, logger: "BoundLoggerLazyProxy"
) -> None:
    rdf_graph_init(graph)

    module = import_module(module_path=module_path)

    # Special case of `PropertyTypeDef` in `property_types.py`
    # PROPERTY TYPES
    # skos:prefLabel used for class names
    # skos:definition used for `description` (en, de)
    # skos:altLabel used for `property_label`
    # dc:identifier used for `code`  # ! only defined for internal codes with $ symbol
    # dc:type used for `data_type`
    if "property_types.py" in module_path:
        for name, obj in inspect.getmembers(module):
            if name.startswith("_") or name == "PropertyTypeDef":
                continue
            prop_uri = BAM[obj.id]

            # Define the property as an OWL class inheriting from PropertyType
            graph.add((prop_uri, RDF.type, OWL.Class))
            graph.add((prop_uri, RDFS.subClassOf, BAM.PropertyType))

            # Add attributes like id, code, description in English and Deutsch, property_label, data_type
            graph.add((prop_uri, SKOS.prefLabel, Literal(obj.id, lang="en")))
            graph.add((prop_uri, DC.identifier, Literal(obj.code)))
            descriptions = obj.description.split("//")
            if len(descriptions) > 1:
                graph.add(
                    (prop_uri, SKOS.definition, Literal(descriptions[0], lang="en"))
                )
                graph.add(
                    (prop_uri, SKOS.definition, Literal(descriptions[1], lang="de"))
                )
            else:
                graph.add(
                    (prop_uri, SKOS.definition, Literal(obj.description, lang="en"))
                )
            graph.add((prop_uri, SKOS.altLabel, Literal(obj.property_label, lang="en")))
            graph.add((prop_uri, DC.type, Literal(obj.data_type.value)))
        return None

    # All other datamodel modules
    # OBJECT/DATASET/COLLECTION TYPES
    # skos:prefLabel used for class names
    # skos:definition used for `description` (en, de)
    # dc:identifier used for `code`  # ! only defined for internal codes with $ symbol
    # parents defined from `code`
    # assigned properties can be Mandatory or Optional, can be PropertyType or ObjectType
    # ? For OBJECT TYPES
    # ? `generated_code_prefix`, `auto_generated_codes`?
    for name, obj in inspect.getmembers(module, inspect.isclass):
        # Ensure the class has the `to_json` method
        if not hasattr(obj, "defs") or not callable(getattr(obj, "to_rdf")):
            continue
        try:
            # Instantiate the class and call the method
            entity = obj()
            entity.to_rdf(namespace=BAM, graph=graph)
        except Exception as err:
            click.echo(f"Failed to process class {name} in {module_path}: {err}")
