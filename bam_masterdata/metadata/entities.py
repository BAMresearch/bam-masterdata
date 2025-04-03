import json
from typing import TYPE_CHECKING, Any, Callable, Optional, no_type_check

import h5py
from pydantic import BaseModel, ConfigDict, Field, model_validator
from rdflib import BNode, Literal
from rdflib.namespace import DC, OWL, RDF, RDFS

if TYPE_CHECKING:
    from pybis import Openbis
    from rdflib import Graph, Namespace, URIRef
    from structlog._config import BoundLoggerLazyProxy

from datetime import datetime

from bam_masterdata.metadata._maps import (
    COLLECTION_TYPE_MAP,
    DATASET_TYPE_MAP,
    OBJECT_TYPE_MAP,
    VOCABULARY_TYPE_MAP,
)
from bam_masterdata.metadata.definitions import (
    CollectionTypeDef,
    DatasetTypeDef,
    ObjectTypeDef,
    PropertyTypeAssignment,
    VocabularyTerm,
    VocabularyTypeDef,
)
from bam_masterdata.openbis import OpenbisEntities
from bam_masterdata.utils import code_to_class_name


class BaseEntity(BaseModel):
    """
    Base class used to define `ObjectType` and `VocabularyType` classes. It extends the `BaseModel`
    adding new methods that are useful for interfacing with openBIS.
    """

    def __init__(self, **kwargs):
        super().__init__()

        # We store the `_property_metadata` during instantiation of the class
        self._property_metadata = self.get_property_metadata()

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __setattr__(self, key, value):
        if key == "_property_metadata":
            super().__setattr__(key, value)
            return

        if key in self._property_metadata:
            # TODO add CONTROLLEDVOCABULARY and OBJECT cases
            expected_type = self._property_metadata[key].data_type.pytype
            if expected_type and not isinstance(value, expected_type):
                raise TypeError(
                    f"Invalid type for '{key}': Expected {expected_type.__name__}, got {type(value).__name__}"
                )

        # TODO add check if someone tries to set up a definition instead of an assigned property

        object.__setattr__(self, key, value)

    def __repr__(self):
        # Filter for attributes that are `PropertyTypeAssignment` and set to a finite value
        fields = []
        for key, metadata in self._property_metadata.items():
            if isinstance(metadata, PropertyTypeAssignment):
                value = getattr(self, key, None)
                # Only include set attributes
                if value is not None and not isinstance(value, PropertyTypeAssignment):
                    fields.append(f"{key}={repr(value)}")

        # Format the output
        class_name = self.__class__.__name__
        return f"{class_name}({', '.join(fields)})"

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

    def _to_openbis(
        self,
        logger: "BoundLoggerLazyProxy",
        openbis: "Openbis",
        type: str,
        type_map: dict,
        get_type: Callable[..., Any],
        create_type: Callable[..., Any],
    ) -> None:
        """
        Add the entity type (object, collection, dataset, or vocabulary) to openBIS if it does not
        exist. If it exists, it checks if the values have changed and logs criticals if `code` has
        been modified while only warnings for the other attributes.
        This function is used in `ObjectType`, `CollectionType`, `DatasetType`, and `VocabularyType` classes.
        Each of these classes' method `to_openbis()` calls their internal functions (they must be explictly
        defined in those classes) `get_type` and `create_type` using PyBIS utilities.
        Args:
            logger (BoundLoggerLazyProxy): The logger to log messages.
            openbis (Openbis): The openBIS instance.
            type (str): The type of entity to add to openBIS.
            type_map (dict): The mapping of the attributes between the model and openBIS. Defined in `bam_masterdata/metadata/_maps.py`.
            get_type (Callable[..., Any]): The function to get the entity type from openBIS using PyBIS.
            create_type (Callable[..., Any]): The function to create the entity type in openBIS using PyBIS.
        """
        # Initialize entity to None
        entity = None
        new_entity = True

        openbis_entities = getattr(
            OpenbisEntities(url=openbis.url), f"get_{type}_dict"
        )()
        defs = getattr(self, "defs")
        print(f"This is defs {defs}")
        # Entity_type already exists in openBIS
        if defs.code in openbis_entities.keys():  # addlog with creation indication
            logger.info(f"Updating existing entity in openBIS:{defs.code}")
            # entity = get_type(openbis, defs.code)
            obis_entity = openbis_entities.get(defs.code)
            # print("This is 'entity'", entity, "\n", "This is obis", obis_entity)
            new_entity = False
            for key in defs.model_fields.keys():
                obis_attr = type_map.get(key)
                value = obis_entity.get(obis_attr)

                # Skip if the value is empty and the attribute is not set
                if not value and not getattr(defs, key):
                    continue

                # Check if the value has changed
                if value != getattr(defs, key):
                    # `code` are immutable if they exist already in openBIS
                    if key == "code" or key == "id":
                        logger.critical(
                            f"`code` cannot be changed once it is set (old {value}, new {getattr(defs, key)}). "
                            "You need to define a new property."
                        )
                        return None
                    # Otherwise, the attribute can be changed
                    else:
                        logger.warning(
                            f"{defs.code} has changed the value for `{key}` from ``{value}`` to ``{getattr(defs, key)}``, <<{datetime.now()}>>\n"
                            "We will update its value in openBIS."
                        )
                        setattr(entity, obis_attr, getattr(self, key))
                        entity.save()

            # Need to assign `entity` to check on the `properties` later
            if entity is None:
                entity = get_type(openbis, defs.code)
                new_entity = False
        else:
            new_entity = True
            # Adding it to openBIS
            entity = create_type(openbis, defs)
            entity.save()

        # Properties/Terms assignment
        properties = getattr(self, "properties", [])
        [print(prop.code) for prop in properties]
        obis_properties = entity.get_property_assignments() if not new_entity else []
        if obis_properties:
            obis_properties_codes = [ob_prop.code for ob_prop in obis_properties]
        else:
            obis_properties_codes = []
        for prop in properties:
            print(prop.code, prop.description)
            # If property is not assigned, assign it
            if prop.code not in obis_properties_codes:
                logger.info(f"Adding new property {prop.code} to {defs.code}.")
                try:
                    openbis.get_property_type(prop.code)
                except ValueError:
                    logger.info(
                        f"Property {prop.code} does not exist in openBIS. Creating it..."
                    )
                    if prop.data_type == "CONTROLLEDVOCABULARY":
                        try:
                            # Check if the vocabulary exists in OpenBIS
                            openbis.get_vocabulary(prop.vocabulary_code)
                            vocabulary_exists = (
                                True  # Set a flag if no exception is raised
                            )
                        except ValueError:
                            logger.error(
                                f"Vocabulary {prop.vocabulary_code} does not exist in openBIS. Define it first."
                            )
                            vocabulary_exists = (
                                False  # Set the flag to False if an exception is raised
                            )
                            entity.delete(
                                "Error"
                            )  # Delete the entity if the vocabulary does not exist
                            break

                        # Only add the vocabulary property if the vocabulary exists
                        if vocabulary_exists:
                            new_prop = openbis.new_property_type(
                                code=prop.code,
                                label=prop.property_label,
                                description=prop.description,
                                dataType=prop.data_type,
                                vocabulary=prop.vocabulary_code,  # Add the vocabulary only if it exists
                            )
                            new_prop.save()
                        else:
                            continue

                    else:
                        if prop.data_type == "OBJECT" or prop.data_type == "SAMPLE":
                            prop.data_type = "SAMPLE"
                        # For other data types, create the property without the vocabulary
                        new_prop = openbis.new_property_type(
                            code=prop.code,
                            label=prop.property_label,
                            description=prop.description,
                            dataType=prop.data_type,
                        )
                        new_prop.save()

                entity.assign_property(
                    prop=prop.code,
                    section=prop.section,
                    mandatory=prop.mandatory,
                    showInEditView=prop.show_in_edit_views,
                )
            # If property is assigned...
            else:
                continue  # These checks will be already performed using the checker

    def _to_openbis2(
        self,
        logger: "BoundLoggerLazyProxy",
        openbis: "Openbis",
        type: str,
        type_map: dict,
        get_type: Callable[..., Any],
        create_type: Callable[..., Any],
    ) -> None:
        """
        Simplified function to add or update the entity type in openBIS.
        """
        # Get all existing entities from openBIS
        openbis_entities = getattr(
            OpenbisEntities(url=openbis.url), f"get_{type}_dict"
        )()
        defs = getattr(self, "defs")

        # Check if the entity already exists
        if defs.code in openbis_entities:
            logger.info(f"Entity '{defs.code}' already exists in openBIS.")
            # Retrieve the existing entity
            entity = get_type(openbis, defs.code)
            # entity = openbis_entities[defs.code]

            # Get properties from self and openBIS
            self_properties = getattr(self, "properties", [])
            obis_properties = entity.get_property_assignments()
            obis_property_codes = [prop.code for prop in obis_properties]

            # Check for properties in self that are not in openBIS
            new_properties_added = False
            for prop in self_properties:
                if prop.code not in obis_property_codes:
                    logger.info(
                        f"Adding new property '{prop.code}' to entity '{defs.code}'."
                    )
                    # Handle special case for OBJECT or SAMPLE data types
                    if prop.data_type == "OBJECT" or prop.data_type == "SAMPLE":
                        prop.data_type = "SAMPLE"

                    # Assign the property to the entity
                    entity.assign_property(
                        prop=prop.code,
                        section=prop.section,
                        mandatory=prop.mandatory,
                        showInEditView=prop.show_in_edit_views,
                    )

            if not new_properties_added:
                logger.info(f"No new properties added to entity '{defs.code}'.")

            # Save the entity after adding new properties
            entity.save()
            return entity

        # If the entity is new, create it
        logger.info(f"Creating new entity '{defs.code}' in openBIS.")
        entity = create_type(openbis, defs)
        entity.save()

        # Assign properties to the new entity
        properties = getattr(self, "properties", [])
        for prop in properties:
            logger.info(f"Adding new property {prop.code} to {defs.code}.")
            # Handle special case for OBJECT or SAMPLE data types
            if prop.data_type == "OBJECT" or prop.data_type == "SAMPLE":
                prop.data_type = "SAMPLE"

            # Assign the property to the entity
            entity.assign_property(
                prop=prop.code,
                section=prop.section,
                mandatory=prop.mandatory,
                showInEditView=prop.show_in_edit_views,
            )

        # Save the entity after assigning properties
        entity.save()
        return entity

    def get_property_metadata(self) -> dict:
        """
        Dictionary containing the metadata of the properties assigned to the entity type.

        Returns:
            dict: A dictionary containing the keys of the `PropertyTypeAssignment` attribute names and the
            values of the definitions of `PropertyTypeAssignment`. Example:
            {
                "name": PropertyTypeAssignment(
                    code="$NAME",
                    data_type=VARCHAR,
                    mandatory=True,
                    property_label="Name"
                ),
                "age": PropertyTypeAssignment(
                    code="AGE",
                    data_type=INTEGER,
                    mandatory=False,
                    property_label="Age"
                ),
            }
        """
        cls_attrs = self.__class__.__dict__

        # Store property metadata at class level
        prop_meta_dict: dict = {}
        for attr_name, attr_value in cls_attrs.items():
            if isinstance(attr_value, PropertyTypeAssignment):
                prop_meta_dict[attr_name] = attr_value
        return prop_meta_dict

    def to_json(self, indent: Optional[int] = None) -> str:
        """
        Returns the entity as a string in JSON format storing the value of the properties
        assigned to the entity.

        Args:
            indent (Optional[int], optional): The indent to print in JSON. Defaults to None.

        Returns:
            str: The JSON representation of the entity.
        """
        data: dict = {}
        for key in self._property_metadata.keys():
            try:
                data[key] = getattr(self, key)
            except AttributeError:
                continue
        return json.dumps(data, indent=indent)

    def to_dict(self) -> dict:
        """
        Returns the entity as a dictionary storing the value of the properties assigned to the entity.

        Returns:
            dict: The dictionary representation of the entity.
        """
        dump_json = self.to_json()
        return json.loads(dump_json)

    def to_hdf5(self, hdf_file: h5py.File, group_name: str = "") -> h5py.File:
        """
        Serialize the entity to a HDF5 file under the group specified in the input.

        Args:
            hdf_file (h5py.File): The HDF5 file to store the entity.
            group_name (str, optional): The group name to serialize the data.
        """
        if not group_name:
            group_name = self.cls_name
        group = hdf_file.create_group(group_name)

        for key in self._property_metadata.keys():
            try:
                value = getattr(self, key)
                if not value:
                    continue
                if isinstance(value, (str, int, float, bool, list, tuple)):
                    group.create_dataset(key, data=value)
                else:
                    raise TypeError(
                        f"Unsupported type {type(value)} for key {key} for HDF5 serialization."
                    )
            except AttributeError:
                continue

    def model_to_dict(self) -> dict:
        """
        Returns the model as a dictionary storing the data `defs` and the property or vocabulary term
        assignments.

        Returns:
            dict: The dictionary representation of the model.
        """
        data = self.model_dump()

        attr_value = getattr(self, "defs")
        if isinstance(attr_value, BaseModel):
            data["defs"] = attr_value.model_dump()
        else:
            data["defs"] = attr_value
        return data

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
        data = self.model_to_dict()
        return json.dumps(data, indent=indent)

    def _add_properties_rdf(
        self,
        namespace: "Namespace",
        graph: "Graph",
        prop: "PropertyTypeAssignment",
        logger: "BoundLoggerLazyProxy",
    ) -> "URIRef":
        """
        Add the properties assigned to the entity to the RDF graph extracting the information from
        OpenBIS for the `object_code` or `vocabulary_code`.

        Args:
            namespace (Namespace): The namespace to use for the RDF graph.
            graph (Graph): The RDF graph to which the properties are added.
            prop (PropertyTypeAssignment): The property assigned to the entity.
            logger (BoundLoggerLazyProxy): The logger to log messages.

        Returns:
            URIRef: The URI reference of the property added to the RDF graph.
        """
        prop_uri = namespace[prop.id]

        # Define the property as an OWL class inheriting from PropertyType
        graph.add((prop_uri, RDF.type, OWL.Thing))
        graph.add((prop_uri, RDFS.subClassOf, namespace.PropertyType))

        # Add attributes like id, code, description in English and Deutsch, property_label, data_type
        graph.add((prop_uri, RDFS.label, Literal(prop.id, lang="en")))
        graph.add((prop_uri, DC.identifier, Literal(prop.code)))
        descriptions = prop.description.split("//")
        if len(descriptions) > 1:
            graph.add((prop_uri, RDFS.comment, Literal(descriptions[0], lang="en")))
            graph.add((prop_uri, RDFS.comment, Literal(descriptions[1], lang="de")))
        else:
            graph.add((prop_uri, RDFS.comment, Literal(prop.description, lang="en")))
        graph.add(
            (prop_uri, namespace.propertyLabel, Literal(prop.property_label, lang="en"))
        )
        graph.add((prop_uri, namespace.dataType, Literal(prop.data_type.value)))
        if prop.data_type.value == "OBJECT":
            # entity_ref_uri = BAM[code_to_class_name(obj.object_code)]
            # graph.add((prop_uri, BAM.referenceTo, entity_ref_uri))
            object_code = code_to_class_name(prop.object_code, logger)
            if not object_code:
                logger.error(
                    f"Failed to identify the `object_code` for the property {prop.id}"
                )
                return prop_uri
            entity_ref_uri = namespace[object_code]

            # Create a restriction with referenceTo
            restriction = BNode()
            graph.add((restriction, RDF.type, OWL.Restriction))
            graph.add((restriction, OWL.onProperty, namespace["referenceTo"]))
            graph.add((restriction, OWL.someValuesFrom, entity_ref_uri))

            # Add the restriction as a subclass of the property
            graph.add((prop_uri, RDFS.subClassOf, restriction))
        return prop_uri

    # skos:prefLabel used for class names
    # skos:definition used for `description` (en, de)
    # dc:identifier used for `code`  # ! only defined for internal codes with $ symbol
    # parents defined from `code`
    # assigned properties can be Mandatory or Optional, can be PropertyType or ObjectType
    # ? For OBJECT TYPES
    # ? `generated_code_prefix`, `auto_generated_codes`?
    @no_type_check
    def model_to_rdf(
        self, namespace: "Namespace", graph: "Graph", logger: "BoundLoggerLazyProxy"
    ) -> None:
        """
        Convert the entity to RDF triples and add them to the graph. The function uses the
        `_add_properties_rdf` method to convert the properties assigned to the entity to RDF triples.

        Args:
            namespace (Namespace): The namespace to use for the RDF graph.
            graph (Graph): The RDF graph to which the entity is added.
            logger (BoundLoggerLazyProxy): The logger to log messages.
        """
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
            prop_uri = self._add_properties_rdf(namespace, graph, assigned_prop, logger)
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
        for attr_name in cls.__dict__.keys():
            attr = getattr(cls, attr_name)
            if isinstance(attr, PropertyTypeAssignment):
                data.properties.append(attr)

        return data

    def to_openbis(
        self,
        logger: "BoundLoggerLazyProxy",
        openbis: "Openbis",
        type: str = "object",
        type_map: dict = OBJECT_TYPE_MAP,
    ) -> None:
        def get_type(openbis: "Openbis", code: str):
            return openbis.get_object_type(code)

        def create_type(openbis: "Openbis", defs: ObjectTypeDef):
            return openbis.new_object_type(
                code=defs.code,
                description=defs.description,
                validationPlugin=defs.validation_script,
                generatedCodePrefix=defs.generated_code_prefix,
                autoGeneratedCode=defs.auto_generated_codes,
            )

        super()._to_openbis2(
            logger=logger,
            openbis=openbis,
            type=type,
            type_map=type_map,
            get_type=get_type,
            create_type=create_type,
        )


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
        for attr_name in cls.__dict__.keys():
            attr = getattr(cls, attr_name)
            if isinstance(attr, VocabularyTerm):
                data.terms.append(attr)

        return data

    def to_openbis(
        self,
        logger: "BoundLoggerLazyProxy",
        openbis: "Openbis",
        type: str = "vocabulary",
        type_map: dict = VOCABULARY_TYPE_MAP,
    ) -> None:
        def get_type(openbis: "Openbis", code: str):
            return openbis.get_vocabulary_type(code)

        def create_type(openbis: "Openbis", defs: VocabularyTypeDef):
            return openbis.new_vocabulary_type(
                code=defs.code, description=defs.description
            )

        super()._to_openbis(
            logger=logger,
            openbis=openbis,
            type=type,
            type_map=type_map,
            get_type=get_type,
            create_type=create_type,
        )


class CollectionType(ObjectType):
    @property
    def cls_name(self) -> str:
        """
        Returns the entity name of the class as a string.
        """
        return "CollectionType"

    def to_openbis(
        self,
        logger: "BoundLoggerLazyProxy",
        openbis: "Openbis",
        type: str = "collection",
        type_map: dict = COLLECTION_TYPE_MAP,
    ) -> None:
        def get_type(openbis: "Openbis", code: str):
            return openbis.get_collection_type(code)

        def create_type(openbis: "Openbis", defs: CollectionTypeDef):
            return openbis.new_collection_type(
                code=defs.code,
                description=defs.description,
                validationPlugin=defs.validation_script,
            )

        super()._to_openbis(
            logger=logger,
            openbis=openbis,
            type=type,
            type_map=type_map,
            get_type=get_type,
            create_type=create_type,
        )


class DatasetType(ObjectType):
    @property
    def cls_name(self) -> str:
        """
        Returns the entity name of the class as a string.
        """
        return "DatasetType"

    def to_openbis(
        self,
        logger: "BoundLoggerLazyProxy",
        openbis: "Openbis",
        type: str = "dataset",
        type_map: dict = DATASET_TYPE_MAP,
    ) -> None:
        def get_type(openbis: "Openbis", code: str):
            return openbis.get_dataset_type(code)

        def create_type(openbis: "Openbis", defs: DatasetTypeDef):
            return openbis.new_dataset_type(
                code=defs.code,
                description=defs.description,
                validationPlugin=defs.validation_script,
                mainDatasetPattern=defs.main_dataset_pattern,
                mainDatasetPath=defs.main_dataset_path,
            )

        super()._to_openbis(
            logger=logger,
            openbis=openbis,
            type=type,
            type_map=type_map,
            get_type=get_type,
            create_type=create_type,
        )
