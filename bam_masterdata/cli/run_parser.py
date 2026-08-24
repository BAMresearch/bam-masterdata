from collections import Counter

from pybis import Openbis

from bam_masterdata.logger import logger
from bam_masterdata.metadata.entities import (
    CollectionType,
    ObjectType,
    PropertyTypeAssignment,
)
from bam_masterdata.parsing import AbstractParser


class RunParsers:
    def __init__(
        self,
        openbis: Openbis | None = None,
        space_name: str = "",
        project_name: str = "PROJECT",
        collection_name: str = "",
        files_parser: dict[AbstractParser, list[str]] = {},
        logger=logger,
        collection_type: str = "COLLECTION",
        **kwargs,
    ):
        """Class to run parsers and create objects in openBIS.

        Args:
            openbis (Openbis | None, optional): The instance of openBIS. Defaults to None.
            space_name (str): The name of the space in openBIS. Defaults to "".
            project_name (str): The name of the project to create or get. Defaults to "PROJECT".
            collection_name (str, optional): The name of the collection to create or get. Defaults to "".
            files_parser (dict[AbstractParser, list[str]]): A dictionary mapping parsers to lists of file paths. Defaults to {}.
            logger (_type_, optional): The logger instance. Defaults to logger.
            collection_type (str, optional): The type of the collection. Defaults to "COLLECTION".

        Returns:
            _type_: _description_
        """
        if openbis is None:
            logger.error(
                "An instance of Openbis must be provided for the parser to run."
            )
            return None
        # Ensure the space, project, and collection are set
        if not space_name:
            logger.error("The Space name must be specified for the parser to run.")
            return None
        if not project_name:
            logger.error("The Project name must be specified for the parser to run.")
            return None
        # Ensure the files_parser is not empty
        if not files_parser:
            logger.error(
                "No files or parsers to parse. Please provide valid file paths or contact an Admin to add missing parser."
            )
            return None
        # Ensure collection_type is valid
        if collection_type not in ["COLLECTION", "DEFAULT_EXPERIMENT"]:
            logger.error(
                f"Invalid collection_type '{collection_type}'. Must be either 'COLLECTION' or 'DEFAULT_EXPERIMENT'."
            )
            return None

        self.logger = logger
        self.openbis = openbis
        self.collection_name = collection_name
        self.files_parser = files_parser
        self._openbis_init(space_name, project_name, collection_name, collection_type)

    def _openbis_init(self, space_name, project_name, collection_name, collection_type):
        self.space = self._get_space(space_name)
        self.project = self._get_project(project_name)
        self.collection_openbis = self._get_collection(
            collection_name, space_name, project_name, collection_type
        )
        self.collection = CollectionType()

    def _get_space(self, space_name: str):
        """
        Gets the OpenBis space.

        Args:
            space_name (str): The name of the space in openBIS. Defaults to "".

        Returns:
            Space: The retrieved space.
        """
        space = None
        try:
            space = self.openbis.get_space(space_name)
        except Exception:
            pass

        if space is None:
            username = self.openbis.username.upper()
            for openbis_space in self.openbis.get_spaces():
                if openbis_space.code.endswith(username):
                    self.logger.warning(
                        f"No space specified, using default space: {openbis_space.code}"
                    )
                    return space

            self.logger.error(
                "No usable space for the user found. Please specify a valid space."
            )
        return space

    def _get_project(self, project_name: str):
        """
        Gets or creates a project in the specified space.

        Args:
            project_name (str): The name of the project to create or get.

        Returns:
            Project: The created or retrieved project.
        """
        project = None
        # Get project if `project_name` already exists under the space or create a new one if it does not
        try:
            project = self.space.get_project(project_name)
        except Exception:
            pass
        if project is None:
            self.logger.info(
                f"Project {project_name} not found. Creating a new project."
            )
            project = self.space.new_project(
                code=project_name.replace(" ", "_").upper(),
                description=f"New project named {project_name.replace(' ', '_').upper()} created via automated parsing with `bam_masterdata`.",
            )
            project.save()
            return project
        return project

    def _get_collection(
        self,
        collection_name: str,
        space_name: str,
        project_name: str,
        collection_type: str = "COLLECTION",
    ):
        """
        Creates or gets the OpenBis collection or defaults to the project if no collection name is provided.

        Args:
            collection_name (str): The name of the collection to create or get.
            space_name (str): The name of the space in openBIS. Defaults to "".
            project_name (str): The name of the project in openBIS. Defaults to "".
            collection_type (str, optional): The type of the collection. Defaults to "COLLECTION".

        Returns:
            collection/project: The created or retrieved collection or the project.
        """
        # Create a new pybis `COLLECTION` to store the generated objects
        collection = None
        if not self.collection_name:
            self.logger.info(
                "No Collection name specified. Attaching objects directly to Project."
            )
            if self.project is None:
                self.logger.error(
                    "Project not found. Cannot attach objects directly to Project."
                )
                return collection
            collection = self.project
            return collection
        else:
            if self.collection_name.upper() in [
                c.code for c in self.project.get_collections()
            ]:
                collection = self.space.get_collection(
                    f"/{space_name}/{project_name}/{collection_name}".upper()
                )
                return collection
            else:
                self.logger.info("Creating new collection.")
                collection = self.openbis.new_collection(
                    code=collection_name.replace(" ", "_").upper(),
                    type=collection_type,
                    project=self.project,
                )
            collection.save()
            return collection

    def parsing(self):
        """
        Runs the Parser specific parsing function the linked files.

        Returns:
            collection: The collection containing the parsed objects.
        """
        for parser, files in self.files_parser.items():
            parser.parse(files, self.collection, logger=self.logger)

        return self.collection

    def _make_unique_code(self, code: str, seen_codes: Counter) -> str:
        """
        Generate a unique code by appending a duplicate counter if the code has already been seen.

        Args:
            code (str): The original code to make unique.
            seen_codes (Counter): A counter tracking codes and their occurrence counts.

        Returns:
            str: The unique code, either the original code or the code with a duplicate suffix.
        """
        seen_codes[code] += 1

        if seen_codes[code] == 1:
            return code

        return f"{code}__dup{seen_codes[code] - 1}"

    def _get_entity(
        self,
        obj: str | dict,
        object_role: str,
    ):
        """
        Resolve an object reference to an OpenBIS object.

        Args:
            openbis: OpenBIS connection instance.
            openbis_id_map: Mapping from internal IDs to OpenBIS identifiers.
            obj: Either an internal object ID or a dictionary that can be passed directly to `openbis.get_object`.
            object_role: Used for logging (e.g. "parent" or "child").

        Returns:
            OpenBIS object instance.
        """

        if isinstance(obj, dict):
            try:
                return self.openbis.get_object(**obj)
            except Exception as e:
                self.logger.warning(
                    f"Error occurred while fetching {object_role} object: {e}"
                )
                return None

        identifier = self.openbis_id_map[obj]
        return self.openbis.get_object(identifier)

    def _load_object_props(self, object_id, object_instance):
        """
        Load and map object properties, resolving OBJECT type references to openBIS identifiers.

        Args:
            object_id: The internal ID of the object.
            object_instance: The object instance containing properties.
        """
        # Map PropertyTypeAssignment to pybis props dictionary
        obj_props = {}
        for key in object_instance._properties.keys():
            value = getattr(object_instance, key, None)
            if value is None or isinstance(value, PropertyTypeAssignment):
                continue
            # Handle OBJECT data type properties
            property_metadata = object_instance._property_metadata[key]
            if property_metadata.data_type == "OBJECT":
                if isinstance(value, str):
                    # Value is a path string, verify it exists in openBIS
                    try:
                        referenced_object = self.openbis.get_object(value)
                        # Use the identifier from the fetched object
                        obj_props[property_metadata.code.lower()] = (
                            referenced_object.identifier
                        )
                    except Exception as e:
                        logger.error(
                            f"Failed to resolve OBJECT reference '{value}' for property '{key}': {e}"
                        )
                        continue
                elif isinstance(value, ObjectType):
                    # Value is an ObjectType instance, construct the path
                    if not value.code:
                        logger.warning(
                            f"OBJECT reference for property '{key}' has no code, skipping"
                        )
                        continue
                    # Construct the identifier path
                    # Try to find this object in the openbis_id_map first (if it's being created in the same batch)
                    referenced_identifier = None
                    for obj_id, obj_inst in self.collection.attached_objects.items():
                        if obj_inst is value and obj_id in self.openbis_id_map:
                            referenced_identifier = self.openbis_id_map[obj_id]
                            break
                    if not referenced_identifier:
                        # Construct identifier from the object's code
                        # Assume it's in the same space/project as the current object
                        if not self.collection.name:
                            referenced_identifier = (
                                f"/{self.space.code}/{self.project.code}/{value.code}"
                            )
                        else:
                            referenced_identifier = f"/{self.space.code}/{self.project.code}/{self.collection.name}/{value.code}"
                    obj_props[property_metadata.code.lower()] = referenced_identifier
                else:
                    # Unexpected type, skip
                    logger.warning(
                        f"Unexpected type for OBJECT property '{key}': {type(value).__name__}"
                    )
                    continue
            else:
                # Not an OBJECT type, handle normally
                obj_props[property_metadata.code.lower()] = value

        return obj_props

    def _get_relationships(self, parent, child):
        """
        Links object to referenced objects or new ones.

        Args:
            parent (object | dict): Parent object or identifier.
            child (object | dict): Child object or identifier.

        Returns:
            Tuple[Optional[object], Optional[object]]: A tuple containing the parent and child objects, or None for either if not found.
        """
        if (
            not isinstance(parent, dict)
            and not isinstance(child, dict)
            and (parent not in self.openbis_id_map or child not in self.openbis_id_map)
        ):
            self.logger.warning(
                f"Skipping relationship with parent {parent} and child {child} "
                "because one of them is not found attached or in OpenBIS."
            )
            pass
        parent_obj = self._get_entity(
            parent,
            "parent",
        )
        child_obj = self._get_entity(
            child,
            "child",
        )
        # ...
        if parent_obj is None or child_obj is None:
            return None, None
        return parent_obj, child_obj

    def _attach_datasets(self):
        """
        Attaches files to the collection/project in openBIS for each parser and its associated files.
        """
        for files in self.files_parser.values():
            try:
                if not self.collection_name:
                    # ! This won't work on a project -> datasets only attached to collections in pyBIS
                    dataset = self.openbis.new_dataset(
                        type="RAW_DATA",
                        files=files,
                        project=self.project,
                    )
                else:
                    dataset = self.openbis.new_dataset(
                        type="RAW_DATA",
                        files=files,
                        collection=self.collection_openbis,
                    )
                dataset.save()
            except Exception as e:
                logger.warning(f"Error uploading files {files} to openBIS: {e}")
                continue
            logger.info(
                f"Files uploaded to openBIS collection {self.collection_openbis.code}."
            )

    def _save_datasets(self, object_instance, identifier):
        """
        Saves attached dataset to objects.

        Args:
            object_instance: Object from collection
            identifier (str): Identifier of the object in openBIS to which the dataset should be attached.
        """
        try:
            if object_instance.datasets != []:
                attached_datasets = self.openbis.new_dataset(
                    type="RAW_DATA",
                    sample=identifier,
                    files=object_instance.datasets,
                )
                attached_datasets.save()
                logger.info(
                    f"Dataset for files {attached_datasets.files} saved successfully"
                )
        except Exception as e:
            logger.warning(
                f"Error saving dataset for files {attached_datasets.files}: {e}"
            )

    def _identifier(self, object_instance):
        """
        Checks for duplicate local codes and generates a unique identifier for the object in openBIS.

        Args:
            object_instance : The object instance for which to generate an identifier.

        Returns:
            identifier (str): The unique identifier for the object in openBIS, ensuring no duplicates.
        """
        original_code = object_instance.code
        unique_code = self._make_unique_code(original_code, self.code_counter)
        if unique_code != original_code:
            self.logger.warning(
                f"Duplicate local code {original_code} → renamed to {unique_code}"
            )
            object_instance.code = unique_code  # Update the code in the object instance
        identifier = (
            f"/{self.space.code}/{self.project.code}/{unique_code}"
            if not self.collection_name
            else f"/{self.space.code}/{self.project.code}/{self.collection_name}/{unique_code}"
        )
        return identifier

    def run(self):
        """
        1. Uploads each object in the collection
        2. Attaches datasets to the objects if any are attached
        3. Creates relationships between objects in the collection based on the relationships defined in the collection
        """
        self.parsing()
        self.openbis_id_map = {}
        self.code_counter = Counter()
        for object_id, object_instance in self.collection.attached_objects.items():
            obj_props = self._load_object_props(
                object_id,
                object_instance,
            )
            identifier = self._identifier(object_instance)

            # Check if object already exists in openBIS, and if so, notify and get for updating properties
            if not object_instance.code:
                logger.warning(
                    f"Object with code {object_instance.code} has no code, skipping creation in openBIS."
                )
                continue
            else:
                try:
                    object_openbis = self.openbis.get_object(identifier)
                    logger.info(
                        f"Object {identifier} already exists in openBIS, updating properties."
                    )
                    object_openbis.set_props(obj_props)  # update properties
                except Exception:
                    logger.info(
                        f"Creating new Object with code {object_instance.code}."
                    )
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

            # Save datasets for the object if any are attached
            self._save_datasets(object_instance, object_openbis.identifier)

        # Storing files as datasets in openBIS
        self._attach_datasets()

        for parent, child in self.collection.relationships.values():
            # RELATIONSHIPS
            parent_obj, child_obj = self._get_relationships(parent, child)
            child_obj.add_parents(parent_obj)
            child_obj.save()
            self.logger.info(
                f"Prepared relationship: {child_obj.identifier} -> parent {parent_obj.identifier}"
            )


class RunParsersWithTransactions(RunParsers):
    def __init__(
        self,
        openbis: Openbis | None = None,
        space_name: str = "",
        project_name: str = "PROJECT",
        collection_name: str = "",
        files_parser: dict[AbstractParser, list[str]] = {},
        logger=logger,
        collection_type: str = "COLLECTION",
        **kwargs,
    ):
        """
        Same as RunParsers but uses transactions for object and relationship creation in openBIS.
        """
        super().__init__(
            openbis,
            space_name,
            project_name,
            collection_name,
            files_parser,
            logger,
            collection_type,
            **kwargs,
        )
        self.rel_transaction = self.openbis.new_transaction()
        self.obj_transaction = self.openbis.new_transaction()

    def run(self):
        self.parsing()
        self.openbis_id_map = {}
        self.code_counter = Counter()

        for object_id, object_instance in self.collection.attached_objects.items():
            obj_props = self._load_object_props(
                object_id,
                object_instance,
            )

            identifier = self._identifier(object_instance)

            try:
                object_openbis = self.openbis.get_object(identifier)
            except Exception:
                object_openbis = None
            # if object exists branch in updating

            if object_openbis is not None:
                obj = object_openbis
                obj.set_props(obj_props)
                self.obj_transaction.add(obj)
                self.logger.info(f"{identifier} will be UPDATED in transaction")

            else:
                obj = self.openbis.new_object(
                    type=object_instance.defs.code,
                    code=object_instance.code,
                    space=self.space,
                    project=self.project,
                    collection=self.collection_openbis
                    if self.collection_name
                    else None,
                    props=obj_props,
                )
                self.obj_transaction.add(obj)
                self.logger.info(f"{identifier} will be CREATED in transaction")

            self.openbis_id_map[object_id] = identifier

        try:
            self.obj_transaction.commit()
            self.logger.info("Transaction committed successfully")
        except Exception as e:
            self.logger.error(f"Failed to commit object transaction: {e}")
            return None

        # TODO (May 2026) if later transactions support datasets change it to transaction.
        for object_id, object_instance in self.collection.attached_objects.items():
            identifier = self.openbis_id_map[object_id]
            self._save_datasets(object_instance, identifier)

        # ---- DATASETS IN TRANSACTION ----
        self._attach_datasets()

        for parent, child in self.collection.relationships.values():
            # RELATIONSHIPS
            parent_obj, child_obj = self._get_relationships(parent, child)
            child_obj.add_parents(parent_obj)
            self.rel_transaction.add(child_obj)
            self.logger.info(
                f"Prepared relationship: {child_obj.identifier} -> parent {parent_obj.identifier}"
            )
        try:
            self.rel_transaction.commit()
            self.logger.info("Datasets and relationships committed successfully")
        except Exception as e:
            self.logger.error(f"Failed to commit datasets/relationships: {e}")
