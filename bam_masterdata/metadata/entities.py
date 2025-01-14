import json
from typing import TYPE_CHECKING, Any, Callable, Optional

if TYPE_CHECKING:
    from pybis import Openbis
    from structlog._config import BoundLoggerLazyProxy


from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, model_validator

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


class BaseEntity(BaseModel):
    """
    Base class used to define `ObjectType` and `VocabularyType` classes. It extends the `BaseModel`
    adding new methods that are useful for interfacing with openBIS.
    """

    def to_json(self, indent: Optional[int] = None) -> str:
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

    def to_dict(self) -> dict:
        """
        Returns the model as a dictionary storing the data `defs` and the property or vocabulary term
        assignments.

        Returns:
            dict: The dictionary representation of the model.
        """
        dump_json = self.to_json()
        return json.loads(dump_json)

    @property
    def cls_name(self) -> str:
        """
        Returns the entity name of the class as a string to speed up checks. This is a property
        to be overwritten by each of the abstract entity types.
        """
        return self.__class__.__name__

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

        openbis_entities = getattr(
            OpenbisEntities(url=openbis.url), f"get_{type}_dict"
        )()
        defs = getattr(self, "defs")
        if defs.code in openbis_entities.keys():
            obis_entity = openbis_entities.get(defs.code)
            for key in defs.model_fields.keys():
                obis_attr = type_map.get(key)
                value = obis_entity.get(obis_attr)

                # Skip if the value is empty and the attribute is not set
                if not value and not getattr(defs, key):
                    continue

                # Check if the value has changed
                if value != getattr(defs, key):
                    # `code` are immutable if they exist already in openBIS
                    if key == "code":
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
                        entity = get_type(openbis, defs.code)
                        print(entity)  # TODO delete this and uncomment next line
                        # setattr(entity, obis_attr, getattr(self, key))

            # Need to assign `entity` to check on the `properties` later
            if entity is None:
                entity = get_type(openbis, defs.code)
        else:
            # Adding it to openBIS
            entity = create_type(openbis, defs)
            print(entity)  # TODO delete this and uncomment next line
            # entity.save()

        # Properties/Terms assignment
        properties = getattr(self, "properties", [])
        obis_properties = entity.get_property_assignments()
        obis_properties_codes = [ob_prop.code for ob_prop in obis_properties]
        for prop in properties:
            # If property is not assigned, assign it
            if prop.code not in obis_properties_codes:
                logger.info(f"Adding new property {prop} to {defs.code}.")
                entity.assign_property(
                    prop=prop.code,
                    section=prop.section,
                    mandatory=prop.mandatory,
                    showInEditView=prop.show_in_edit_views,
                )
            # If property is assigned...
            else:
                pass
                # for ob_prop in obis_properties:
                #     ob_prop = ob_prop.get_property_type()
                #     # ? check if we need to test more attributes
                #     if (
                #         prop.code == ob_prop.code
                #         and prop.description == ob_prop.description
                #         and prop.property_label == ob_prop.label
                #         and prop.data_type == ob_prop.dataType
                #     ):
                #         continue
                #     logger.error(
                #         f"The definition of the property {prop} has changed:\n"
                #         f"    - New code: `{prop.code}` | openBIS code: `{ob_prop.code}`"
                #         f"    - New description: `{prop.description}` | openBIS description: `{ob_prop.description}`"
                #         f"    - New label: `{prop.property_label}` | openBIS label: `{ob_prop.label}`"
                #         "Please, update the PropertyType first in openBIS."
                #     )


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

    @property
    def cls_name(self) -> str:
        """
        Returns the entity name of the class as a string.
        """
        return "ObjectType"

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
                autoGeneratedCodes=defs.auto_generated_codes,
            )

        super()._to_openbis(
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

    @property
    def cls_name(self) -> str:
        """
        Returns the entity name of the class as a string.
        """
        return "VocabularyType"


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
