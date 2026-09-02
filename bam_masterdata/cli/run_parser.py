import hashlib
from typing import TYPE_CHECKING

from bam_masterdata.logger import logger
from bam_masterdata.metadata.entities import (
    CollectionType,
    ObjectType,
    PropertyTypeAssignment,
)
from bam_masterdata.parsing import AbstractParser

if TYPE_CHECKING:
    from pybis import Openbis
    from pybis.experiment import Experiment
    from pybis.project import Project
    from pybis.sample import Sample
    from pybis.space import Space
    from structlog._config import BoundLoggerLazyProxy


class RunParsers:
    """
    Run configured parsers and persist the resulting data model to openBIS.

    The class parses input files into an internal collection of objects and relationships, creates
    or updates the corresponding objects in openBIS, attaches datasets, and creates parent-child
    relationships between objects.

    Objects can be stored directly under a project or inside a collection, depending on the
    configured `collection_name`.
    """

    def __init__(
        self,
        openbis: "Openbis" | None = None,
        space_name: str = "",
        project_name: str = "PROJECT",
        collection_name: str = "",
        files_parser: dict[AbstractParser, list[str]] | None = None,
        logger: "BoundLoggerLazyProxy" = logger,
        collection_type: str = "COLLECTION",
    ):
        # Initial checks
        if openbis is None:
            raise ValueError("An openBIS instance must be provided.")
        if not project_name:
            raise ValueError("The project_name must be specified.")

        # Ensure the files_parser is not empty
        if not files_parser:
            raise ValueError(
                "At least one valid parser with its associated files must be provided."
            )

        # Ensure collection_type is valid
        if collection_type not in {"COLLECTION", "DEFAULT_EXPERIMENT"}:
            raise ValueError(
                f"Invalid collection_type '{collection_type}'. "
                "Must be either 'COLLECTION' or 'DEFAULT_EXPERIMENT'."
            )

        self.logger = logger
        self.openbis = openbis
        self.collection_name = collection_name
        self.files_parser = files_parser
        # initializing space/project/collection from openBIS
        self._openbis_init(
            space_name=space_name,
            project_name=project_name,
            collection_name=collection_name,
            collection_type=collection_type,
        )

    def _openbis_init(
        self,
        space_name: str,
        project_name: str,
        collection_name: str,
        collection_type: str = "COLLECTION",
    ):
        """
        Initializes the Space, Project, and (optionally) Experiment objects from openBIS based
        on the input names and collection type. It also creates an instance of `CollectionType`.

        Args:
            space_name (str): The name of the space in openBIS.
            project_name (str): The name of the project to create or get.
            collection_name (str): The name of the collection to create or get.
            collection_type (str): The type of the collection. Defaults to "COLLECTION".
        """
        self.space = self._get_space(space_name)
        self.project = self._get_project(project_name)
        self.collection_openbis = self._get_collection(collection_name, collection_type)
        self.collection = CollectionType()

    def _get_space(self, space_name: str = "") -> "Space" | None:
        """
        Gets the OpenBis space from the specified `space_name`. If no space name is provided, it attempts to find a default space for the username.

        Args:
            space_name (str): The name of the space in openBIS. Defaults to "".

        Returns:
            (Space | None): The retrieved space.
        """
        try:
            return self.openbis.get_space(space_name)
        except Exception:
            username = self.openbis.username.upper()

            for openbis_space in self.openbis.get_spaces():
                if openbis_space.code.endswith(username):
                    self.logger.warning(
                        f"Space '{space_name}' not found. Using default space: {openbis_space.code}"
                    )
                    return openbis_space

        raise ValueError(
            "No space found for the specified name or default username. Please provide a valid space name."
        )

    def _get_project(self, project_name: str) -> "Project" | None:
        """
        Gets project if `project_name` exists in the space in openBIS. Otherwise, creates a new project with the specified name.

        Args:
            project_name (str): The name of the project to create or get.

        Returns:
            (Project | None): The created or retrieved project.
        """
        try:
            return self.space.get_project(project_name)
        except Exception:
            self.logger.info(
                f"Project '{project_name}' not found in the space '{self.space.code}' in openBIS. Creating a new project."
            )
            project_name = project_name.replace(" ", "_").upper()
            project = self.space.new_project(
                code=project_name,
                description=f"New project named {project_name} created via automated parsing with `bam_masterdata`.",
            )
            project.save()
            return project

    def _get_collection(
        self,
        collection_name: str,
        collection_type: str = "COLLECTION",
    ) -> "Experiment" | "Project" | None:
        """
        Gets or creates an openBIS collection. If no collection name is provided, objects are
        attached directly to the project.

        Args:
            collection_name (str): The name of the collection to create or retrieve.
            collection_type (str): openBIS collection type. Defaults to "COLLECTION".

        Returns:
            (Experiment | Project | None): The created or retrieved collection, or the project if no `collection_name` is provided.
        """
        if not collection_name:
            self.logger.info(
                "No collection name specified. Attaching objects directly to the project."
            )
            return self.project

        collection_code = collection_name.replace(" ", "_").upper()

        existing_collections = {c.code: c for c in self.project.get_collections()}

        if collection_code in existing_collections:
            self.logger.info(
                f"Collection '{collection_code}' already exists. Using the existing collection."
            )
            return existing_collections[collection_code]

        self.logger.info(
            f"Collection '{collection_code}' not found. Creating a new collection of type '{collection_type}'."
        )
        collection = self.openbis.new_collection(
            code=collection_code,
            type=collection_type,
            project=self.project,
        )
        collection.save()
        return collection

    def parsing(self) -> None:
        """
        Runs the parser specific class for each of the files specified in `self.files_parser` and adds them to the collection.
        """
        for parser, files in self.files_parser.items():
            parser.parse(files, self.collection, logger=self.logger)

    def _content_hash(self, object_instance: ObjectType, length: int = 16) -> str:
        """
        Generates a hash of the content of the given object instance. This is used to create a unique
        identifier for objects that do not have a specified `code`.

        Args:
            object_instance (ObjectType): The object instance for which to generate a content hash.
            length (int, optional): The length of the hash to generate. Defaults to 16.

        Returns:
            str: The generated content hash.
        """
        serialized_payload = object_instance.to_json()
        return hashlib.sha256(serialized_payload.encode("utf-8")).hexdigest()[:length]

    def _identifier_from_code(self, code: str) -> str:
        """
        Generates an identifier for the given code in openBIS.

        Args:
            code (str): The code for which to generate an identifier.

        Returns:
            str: The generated identifier.
        """
        if not self.collection_name:
            return f"/{self.space.code}/{self.project.code}/{code}"
        return f"/{self.space.code}/{self.project.code}/{self.collection_openbis.code}/{code}"

    def _identifier(self, object_instance: ObjectType) -> str | None:
        """
        Generates a unique identifier for the given object instance in openBIS. If the object has a specified `code`,
        it uses that code. If not, it generates a code by combining the `generated_code_prefix` and a hash of the object's content.

        Args:
            object_instance (ObjectType): The object instance for which to generate an identifier.

        Returns:
            identifier (str | None): The unique identifier for the object in openBIS, ensuring no duplicates.
        """
        code = object_instance.code

        if not code:
            self.logger.info(
                "Object has no specified `code`. Generating one from "
                "`generated_code_prefix` and the hashed content."
            )
            prefix = object_instance.defs.generated_code_prefix
            hash_suffix = self._content_hash(object_instance)
            code = f"{prefix}_{hash_suffix}"
            object_instance.code = code  # Update the code in the object instance

        return self._identifier_from_code(code)

    def _resolve_object_reference(
        self, property_name: str, value: str | ObjectType
    ) -> str | None:
        """
        Resolves an OBJECT type property reference to an openBIS identifier.

        Args:
            property_name (str): The name of the property being resolved.
            value (str | ObjectType): The value of the property, which can be a string path or an ObjectType instance.

        Returns:
            str | None: The resolved openBIS identifier, or None if it cannot be resolved.
        """
        # If `value` is a string, verify this exists in openBIS and return the identifier of the object
        if isinstance(value, str):
            try:
                referenced_object = self.openbis.get_object(value)
                return referenced_object.identifier
            except Exception as exc:
                self.logger.error(
                    f"Failed to resolve OBJECT reference '{value}' "
                    f"for property '{property_name}': {exc}"
                )
                return None

        # If `value` is an ObjectType instance, we need to construct the identifier path
        if isinstance(value, ObjectType):
            if not value.code:
                self.logger.warning(
                    f"OBJECT reference for property '{property_name}' "
                    "has no code, skipping."
                )
                return None

            # Try to find this object in `self.openbis_id_map` first (if it's being created in the same batch)
            referenced_identifier = None
            for obj_id, obj_inst in self.collection.attached_objects.items():
                if obj_inst is value and obj_id in self.openbis_id_map:
                    referenced_identifier = self.openbis_id_map[obj_id]
                    break

            # If not, construct identifier from the object's code
            # Assume it's in the same space/project as the current object
            if not referenced_identifier:
                referenced_identifier = self._identifier_from_code(value.code)

            return referenced_identifier

        self.logger.warning(
            f"Unexpected type for OBJECT property '{property_name}': "
            f"{type(value).__name__}"
        )
        return None

    def _load_openbis_props(self, object_instance: ObjectType) -> dict:
        """
        Loads the properties of an object instance into a dictionary suitable for openBIS, where the keys are the
        property codes and the values are the corresponding property values. It also resolves OBJECT type properties to their openBIS identifiers.

        Args:
            object_instance (ObjectType): The object instance containing properties.

        Returns:
            dict: A dictionary of property codes and their corresponding values, ready for openBIS.
        """
        obj_props = {}

        for key, property_metadata in object_instance._property_metadata.items():
            value = getattr(object_instance, key, None)
            if isinstance(value, PropertyTypeAssignment):
                continue

            prop_name = property_metadata.code.lower()

            # For the special case of OBJECT type properties, we need to resolve the reference to an openBIS identifier.
            if property_metadata.data_type == "OBJECT":
                value = self._resolve_object_reference(key, value)
                if value is None:
                    self.logger.warning(
                        f"Skipping OBJECT property '{key}' for object '{object_instance.code}' because it could not be resolved."
                    )
                    continue

            obj_props[prop_name] = value
        return obj_props

    def _save_datasets(self, object_instance: ObjectType, identifier: str) -> None:
        """
        Saves attached datasets in the object instance to the object specified in the `identifier`.

        Args:
            object_instance (ObjectType): The object instance containing datasets to be saved.
            identifier (str): Identifier of the object in openBIS to which the dataset should be attached.
        """
        if len(object_instance.datasets) == 0:
            self.logger.info(
                f"No datasets attached to object '{object_instance.code}' with identifier '{identifier}'."
            )
            return None

        try:
            attached_datasets = self.openbis.new_dataset(
                type="RAW_DATA",
                sample=identifier,
                files=object_instance.datasets,
            )
            attached_datasets.save()
            self.logger.info(
                f"Dataset for files {attached_datasets.files} saved successfully"
            )
        except Exception as e:
            self.logger.warning(
                f"Error saving dataset for files {attached_datasets.files}: {e}"
            )

    def _attach_datasets(self) -> None:
        """
        Attaches files to the collection/project in openBIS for each parser and its associated files.
        """
        for files in self.files_parser.values():
            try:
                if not self.collection_name:
                    # ! This won't work on a project -> datasets only attached to collections in pyBIS
                    self.logger.error(
                        "Cannot attach datasets directly to a project. If you want to store them during this process, specify a collection name."
                    )
                    continue
                else:
                    dataset = self.openbis.new_dataset(
                        type="RAW_DATA",
                        files=files,
                        collection=self.collection_openbis,
                    )
                dataset.save()
            except Exception as e:
                self.logger.warning(f"Error uploading files {files} to openBIS: {e}")
                continue
            self.logger.info(
                f"Files uploaded to openBIS collection {self.collection_openbis.code}."
            )

    def _get_openbis_obj(
        self,
        obj: str | dict,
        object_role: str,
    ) -> "Sample" | None:
        """
        Gets the openBIS object based on the provided identifier or dictionary. If the object is not found, it logs a warning.

        Args:
            obj: Either a bam-masterdata object ID or a dictionary that can be used to resolve the object using pyBIS.
            object_role: Used for logging (e.g. "parent" or "child").

        Returns:
            (Sample | None): The openBIS object if found, otherwise None.
        """
        # If `obj` is a dictionary, try to extract the identifier from it.
        if isinstance(obj, dict):
            identifier = next(
                (
                    value
                    for key, value in obj.items()
                    if key in {"permId", "code", "identifier"}
                ),
                None,
            )

            if identifier is None:
                self.logger.warning(
                    f"No valid identifier found for {object_role} object: {obj}"
                )
                return None
        # If it's a string, look it up in the `openbis_id_map`.
        else:
            identifier = self.openbis_id_map.get(obj)
            if identifier is None:
                self.logger.warning(
                    f"No openBIS identifier found for {object_role} object '{obj}'."
                )
                return None

        # Try to get identifier from an object existing in openBIS
        try:
            return self.openbis.get_object(identifier)
        except Exception as exc:
            self.logger.warning(
                f"Failed to fetch {object_role} object '{identifier}': {exc}"
            )
            return None

    def _load_relationship_objs(
        self, parent: str | dict, child: str | dict
    ) -> tuple["Sample" | None, "Sample" | None]:
        """
        Loads the parent and child objects for a relationship based on the provided identifiers or dictionaries.
        If either object is not found, it logs a warning.

        Args:
            parent (str | dict): The parent object, which can be a bam-masterdata object ID or a dictionary that can be used to resolve the object using pyBIS.
            child (str | dict): The child object, which can be a bam-masterdata object ID or a dictionary that can be used to resolve the object using pyBIS.

        Returns:
            (tuple[Sample | None, Sample | None]): A tuple containing the parent and child openBIS objects. If either object is not found, it will be (None, None).
        """
        parent_obj = self._get_openbis_obj(parent, "parent")
        child_obj = self._get_openbis_obj(child, "child")

        if parent_obj is None or child_obj is None:
            return None, None
        return parent_obj, child_obj

    def run(self) -> None:
        """
        Runs the complete parsing and openBIS import workflow.

        Parses all configured files into the internal collection, creates or updates the corresponding
        objects in openBIS, stores their local-to-openBIS identifier mapping, attaches object-level
        and collection-level datasets, and finally creates the parent-child relationships defined
        during parsing.

        Existing openBIS objects are updated rather than recreated when their identifier already exists.
        """

        # Runs the parser specific class for each of the files specified in `self.files_parser` and adds them to the `self.collection`.
        self.parsing()

        # Storing objects in openBIS and creating a mapping of local IDs to openBIS identifiers for later use in relationships.
        self.openbis_id_map = {}
        for object_id, object_instance in self.collection.attached_objects.items():
            identifier = self._identifier(object_instance)
            obj_props = self._load_openbis_props(object_instance)

            try:
                object_openbis = self.openbis.get_object(identifier)
                self.logger.info(
                    f"Object '{identifier}' already exists in openBIS, updating properties."
                )
                object_openbis.set_props(obj_props)  # update properties
            except Exception:
                self.logger.info(f"Creating new object '{object_instance.code}'.")
                if not self.collection_name:
                    object_openbis = self.openbis.new_object(
                        type=object_instance.defs.code,
                        code=object_instance.code,
                        space=self.space,
                        project=self.project,
                        props=obj_props,
                    )
                else:
                    object_openbis = self.openbis.new_object(
                        type=object_instance.defs.code,
                        code=object_instance.code,
                        space=self.space,
                        project=self.project,
                        collection=self.collection_openbis,
                        props=obj_props,
                    )
            object_openbis.save()

            # save local and openbis IDs to map parent-child relationships
            self.openbis_id_map[object_id] = object_openbis.identifier

            # Save datasets for the object if any are attached from parsing
            self._save_datasets(object_instance, object_openbis.identifier)

        # Storing files as datasets in openBIS
        self._attach_datasets()

        # Creating relationships between objects in the collection based on the relationships defined in the collection.
        for parent, child in self.collection.relationships.values():
            parent_obj, child_obj = self._load_relationship_objs(parent, child)
            if parent_obj is None or child_obj is None:
                self.logger.warning(
                    f"Skipping relationship with parent {parent} and child {child} "
                    "because one of them is not found attached or in OpenBIS."
                )
                continue
            child_obj.add_parents(parent_obj)
            child_obj.save()
            self.logger.info(
                f"Prepared relationship: {child_obj.identifier} -> parent {parent_obj.identifier}"
            )


class RunParsersWithTransactions(RunParsers):
    """
    Run parsers and persist objects and relationships to openBIS using transactions.

    Object creation and updates are committed in one transaction. Relationships are committed in a separate
    transaction after object creation has completed.

    Dataset uploads are currently performed outside transactions.
    """

    def __init__(
        self,
        openbis: "Openbis" | None = None,
        space_name: str = "",
        project_name: str = "PROJECT",
        collection_name: str = "",
        files_parser: dict[AbstractParser, list[str]] | None = None,
        logger: "BoundLoggerLazyProxy" = logger,
        collection_type: str = "COLLECTION",
    ):
        super().__init__(
            openbis=openbis,
            space_name=space_name,
            project_name=project_name,
            collection_name=collection_name,
            files_parser=files_parser,
            logger=logger,
            collection_type=collection_type,
        )
        self.rel_transaction = self.openbis.new_transaction()
        self.obj_transaction = self.openbis.new_transaction()

    def run(self) -> None:
        """
        Runs the parsing and transactional openBIS import workflow.

        Parses the configured files, creates or updates all generated objects in a single transaction,
        uploads attached datasets, and finally commits parent-child relationships in a separate transaction.

        Dataset uploads are currently performed outside transactions.
        """

        self.parsing()
        self.openbis_id_map = {}

        # Create or update objects in openBIS within a single transaction
        obj_transaction = self.openbis.new_transaction()
        for object_id, object_instance in self.collection.attached_objects.items():
            identifier = self._identifier(object_instance)
            obj_props = self._load_openbis_props(object_instance)

            try:
                object_openbis = self.openbis.get_object(identifier)
            except Exception:
                object_openbis = None

            if object_openbis is not None:
                object_openbis.set_props(obj_props)
                obj_transaction.add(object_openbis)

                self.logger.info(
                    f"Object '{identifier}' will be updated in transaction."
                )
            else:
                object_openbis = self.openbis.new_object(
                    type=object_instance.defs.code,
                    code=object_instance.code,
                    space=self.space,
                    project=self.project,
                    collection=(
                        self.collection_openbis if self.collection_name else None
                    ),
                    props=obj_props,
                )

                obj_transaction.add(object_openbis)

                self.logger.info(
                    f"Object '{identifier}' will be created in transaction."
                )

            self.openbis_id_map[object_id] = identifier

        try:
            obj_transaction.commit()
        except Exception as exc:
            self.logger.error(f"Failed to commit object transaction: {exc}")
            return None

        self.logger.info("Object transaction committed successfully.")

        # ! Dataset transactions are not currently supported.
        # TODO (May 2026) if later transactions support datasets change it to transaction.
        for object_id, object_instance in self.collection.attached_objects.items():
            identifier = self.openbis_id_map[object_id]
            self._save_datasets(object_instance, identifier)

        self._attach_datasets()

        # Creating relationships in a separate transaction after objects have been created or updated
        rel_transaction = self.openbis.new_transaction()
        for parent, child in self.collection.relationships.values():
            parent_obj, child_obj = self._load_relationship_objs(parent, child)

            if parent_obj is None or child_obj is None:
                self.logger.warning(
                    f"Skipping relationship with parent {parent} and child {child} "
                    "because one of the objects could not be resolved."
                )
                continue

            child_obj.add_parents(parent_obj)
            rel_transaction.add(child_obj)

            self.logger.info(
                f"Prepared relationship: {child_obj.identifier} -> parent {parent_obj.identifier}"
            )
        try:
            rel_transaction.commit()
        except Exception as exc:
            self.logger.error(f"Failed to commit relationship transaction: {exc}")
            return None

        self.logger.info("Relationship transaction committed successfully.")
