import json
from typing import TYPE_CHECKING, Any, Optional, no_type_check

from pydantic import BaseModel, ConfigDict, Field, model_validator
from rdflib import BNode, Literal
from rdflib.namespace import DC, OWL, RDF, RDFS

if TYPE_CHECKING:
    from rdflib import Graph, Namespace

from bam_masterdata.metadata.definitions import (
    CollectionTypeDef,
    DatasetTypeDef,
    ObjectTypeDef,
    PropertyTypeAssignment,
    VocabularyTerm,
    VocabularyTypeDef,
)


class BaseEntity(BaseModel):
    """
    Base class used to define `ObjectType` and `VocabularyType` classes. It extends the `BaseModel`
    adding new methods that are useful for interfacing with openBIS.
    """

    @property
    def cls_name(self) -> str:
        """
        Returns the entity name of the class as a string to speed up checks. This is a property
        to be overwritten by each of the abstract entity types.
        """
        return self.__class__.__name__

    @property
    def _base_attrs(self) -> list:
        """
        List of base properties or terms assigned to an entity type. This are the direct properties or terms
        assigned when defining a new entity type.
        """
        cls_attrs = self.__class__.__dict__
        base_attrs = [
            attr_name
            for attr_name in cls_attrs
            if not (
                attr_name.startswith("_")
                or callable(cls_attrs[attr_name])
                or attr_name
                in ["defs", "model_config", "model_fields", "model_computed_fields"]
            )
        ]
        return [getattr(self, attr_name) for attr_name in base_attrs]

    def model_to_json(self, indent: Optional[int] = None) -> str:
        """
        Returns the model as a string in JSON format storing the data `defs` and the property or
        vocabulary term assignments.

        Args:
            indent (Optional[int], optional): The indent to print in JSON. Defaults to None.

        Returns:
            str: The JSON representation of the model.
        """
        # * `model_dump_json()` from pydantic does not store the `defs` section of each entity.
        data = self.model_dump()

        attr_value = getattr(self, "defs")
        if isinstance(attr_value, BaseModel):
            data["defs"] = attr_value.model_dump()
        else:
            data["defs"] = attr_value

        return json.dumps(data, indent=indent)

    def model_to_dict(self) -> dict:
        """
        Returns the model as a dictionary storing the data `defs` and the property or vocabulary term
        assignments.

        Returns:
            dict: The dictionary representation of the model.
        """
        dump_json = self.model_to_json()
        return json.loads(dump_json)

    # skos:prefLabel used for class names
    # skos:definition used for `description` (en, de)
    # dc:identifier used for `code`  # ! only defined for internal codes with $ symbol
    # parents defined from `code`
    # assigned properties can be Mandatory or Optional, can be PropertyType or ObjectType
    # ? For OBJECT TYPES
    # ? `generated_code_prefix`, `auto_generated_codes`?
    @no_type_check
    def model_to_rdf(self, namespace: "Namespace", graph: "Graph") -> None:
        entity_uri = namespace[self.defs.id]

        # Define the entity as an OWL class inheriting from the specific namespace type
        graph.add((entity_uri, RDF.type, OWL.Thing))
        parent_classes = self.__class__.__bases__
        for parent_class in parent_classes:
            if issubclass(parent_class, BaseEntity) and parent_class != BaseEntity:
                # if parent_class.__name__ in [
                #     "ObjectType",
                #     "CollectionType",
                #     "DatasetType",
                # ]:
                #     # ! add here logic of subClassOf connecting with PROV-O or BFO
                #     # ! maybe via classes instead of ObjectType/CollectionType/DatasetType?
                #     # ! Example:
                #     # !     graph.add((entity_uri, RDFS.subClassOf, "http://www.w3.org/ns/prov#Entity"))
                #     continue
                parent_uri = namespace[parent_class.__name__]
                graph.add((entity_uri, RDFS.subClassOf, parent_uri))

        # Add attributes like id, code, description in English and Deutsch, property_label, data_type
        graph.add((entity_uri, RDFS.label, Literal(self.defs.id, lang="en")))
        graph.add((entity_uri, DC.identifier, Literal(self.defs.code)))
        descriptions = self.defs.description.split("//")
        if len(descriptions) > 1:
            graph.add((entity_uri, RDFS.comment, Literal(descriptions[0], lang="en")))
            graph.add((entity_uri, RDFS.comment, Literal(descriptions[1], lang="de")))
        else:
            graph.add(
                (entity_uri, RDFS.comment, Literal(self.defs.description, lang="en"))
            )
        # Adding properties relationships to the entities
        for assigned_prop in self._base_attrs:
            prop_uri = namespace[assigned_prop.id]
            restriction = BNode()
            graph.add((restriction, RDF.type, OWL.Restriction))
            if assigned_prop.mandatory:
                graph.add(
                    (restriction, OWL.onProperty, namespace["hasMandatoryProperty"])
                )
            else:
                graph.add(
                    (restriction, OWL.onProperty, namespace["hasOptionalProperty"])
                )
            graph.add((restriction, OWL.someValuesFrom, prop_uri))

            # Add the restriction as a subclass of the entity
            graph.add((entity_uri, RDFS.subClassOf, restriction))


class ObjectType(BaseEntity):
    """
    Base class used to define object types. All object types must inherit from this class. The
    object types are defined in the module `bam_masterdata/object_types.py`.

    The `ObjectType` class contains a list of all `properties` defined for a `ObjectType`, for
    internally represent the model in other formats (e.g., JSON or Excel).

    Note this is also used for `CollectionType` and `DatasetType`, as they also contain a list of
    properties.
    """

    model_config = ConfigDict(
        ignored_types=(
            ObjectTypeDef,
            CollectionTypeDef,
            DatasetTypeDef,
            PropertyTypeAssignment,
        )
    )

    properties: list[PropertyTypeAssignment] = Field(
        default=[],
        description="""
        List of properties assigned to an object type. This is useful for internal representation of the model.
        """,
    )

    @property
    def cls_name(self) -> str:
        """
        Returns the entity name of the class as a string.
        """
        return "ObjectType"

    @model_validator(mode="after")
    @classmethod
    def model_validator_after_init(cls, data: Any) -> Any:
        """
        Validate the model after instantiation of the class.

        Args:
            data (Any): The data containing the fields values to validate.

        Returns:
            Any: The data with the validated fields.
        """
        # Add all the properties assigned to the object type to the `properties` list.
        for attr_name in dir(cls):
            attr = getattr(cls, attr_name)
            if isinstance(attr, PropertyTypeAssignment):
                data.properties.append(attr)

        return data


class VocabularyType(BaseEntity):
    """
    Base class used to define vocabulary types. All vocabulary types must inherit from this class. The
    vocabulary types are defined in the module `bam_masterdata/vocabulary_types.py`.

    The `VocabularyType` class contains a list of all `terms` defined for a `VocabularyType`, for
    internally represent the model in other formats (e.g., JSON or Excel).
    """

    model_config = ConfigDict(ignored_types=(VocabularyTypeDef, VocabularyTerm))

    terms: list[VocabularyTerm] = Field(
        default=[],
        description="""
        List of vocabulary terms. This is useful for internal representation of the model.
        """,
    )

    @property
    def cls_name(self) -> str:
        """
        Returns the entity name of the class as a string.
        """
        return "VocabularyType"

    @model_validator(mode="after")
    @classmethod
    def model_validator_after_init(cls, data: Any) -> Any:
        """
        Validate the model after instantiation of the class.

        Args:
            data (Any): The data containing the fields values to validate.

        Returns:
            Any: The data with the validated fields.
        """
        # Add all the vocabulary terms defined in the vocabulary type to the `terms` list.
        for attr_name in dir(cls):
            attr = getattr(cls, attr_name)
            if isinstance(attr, VocabularyTerm):
                data.terms.append(attr)

        return data


class CollectionType(ObjectType):
    @property
    def cls_name(self) -> str:
        """
        Returns the entity name of the class as a string.
        """
        return "CollectionType"


class DatasetType(ObjectType):
    @property
    def cls_name(self) -> str:
        """
        Returns the entity name of the class as a string.
        """
        return "DatasetType"
