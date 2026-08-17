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
        """
        Initialize the RunParsers class.
        """
        if openbis is None:
            logger.error(
                "An instance of Openbis must be provided for the parser to run."
            )
            raise ValueError(
                "An instance of Openbis must be provided for the parser to run."
            )
        # Ensure the space, project, and collection are set
        if not project_name:
            logger.error("The Project name must be specified for the parser to run.")
            raise ValueError(
                "The Project name must be specified for the parser to run."
            )
        # Ensure the files_parser is not empty
        if not files_parser:
            logger.error(
                "No files or parsers to parse. Please provide valid file paths or contact an Admin to add missing parser."
            )
            raise ValueError(
                "No files or parsers to parse. Please provide valid file paths or contact an Admin to add missing parser."
            )
        # Ensure collection_type is valid
        if collection_type not in ["COLLECTION", "DEFAULT_EXPERIMENT"]:
            logger.error(
                f"Invalid collection_type '{collection_type}'. Must be either 'COLLECTION' or 'DEFAULT_EXPERIMENT'."
            )
            raise ValueError(
                "Invalid collection_type. Must be either 'COLLECTION' or 'DEFAULT_EXPERIMENT'."
            )
        self.space_name = space_name
        self.logger = logger
        self.openbis = openbis
        self.project_name = project_name
        self.collection_name = collection_name
        self.collection_type = collection_type
        self.files_parser = files_parser
        self._openbis_init()
        self.parsing()

    def _openbis_init(self):
        self._openbis_space()
        self._openbis_project()
        self._openbis_collection()
        self._bam_masterdata_collection()

    def _openbis_space(self):
        try:
            self.space = self.openbis.get_space(self.space_name)
        except Exception:
            self.space = None
        # If space is not found, use the user space
        if self.space is None:
            # user name as default space
            for s in self.openbis.get_spaces():
                if s.code.endswith(self.openbis.username.upper()):
                    self.space = s
                    self.logger.warning(
                        f"Space {self.space_name} does not exist in openBIS. "
                        f"Loading space for {self.openbis.username}."
                    )
                    break
            # no space found
            if self.space is None:
                self.logger.error(
                    f"No usable Space for {self.openbis.username} in openBIS. Please create it first or notify an Admin."
                )
                raise ValueError(
                    f"No usable Space for {self.openbis.username} in openBIS. Please create it first or notify an Admin."
                )

    def _openbis_project(self):
        # Get project if `project_name` already exists under the space or create a new one if it does not
        if self.project_name.upper() in [p.code for p in self.space.get_projects()]:
            self.project = self.space.get_project(self.project_name)
        else:
            self.logger.info("Replacing project code with uppercase and underscores.")
            self.project = self.space.new_project(
                code=self.project_name.replace(" ", "_").upper(),
                description="New project created via automated parsing with `bam_masterdata`.",
            )
        self.project.save()

    def _openbis_collection(self):
        # Create a new pybis `COLLECTION` to store the generated objects
        if not self.collection_name:
            self.logger.info(
                "No Collection name specified. Attaching objects directly to Project."
            )
            self.collection_openbis = self.project
        else:
            if self.collection_name.upper() in [
                c.code for c in self.project.get_collections()
            ]:
                self.collection_openbis = self.space.get_collection(
                    f"/{self.space_name}/{self.project_name}/{self.collection_name}".upper()
                )
            else:
                self.logger.info(
                    "Replacing collection code with uppercase and underscores."
                )
                self.collection_openbis = self.openbis.new_collection(
                    code=self.collection_name.replace(" ", "_").upper(),
                    type=self.collection_type,
                    project=self.project,
                )
            self.collection_openbis.save()

    def _bam_masterdata_collection(self):
        # Create a bam_masterdata CollectionType instance for storing parsed results
        self.collection = CollectionType()

    def parsing(self):
        # Iterate over each parser and its associated files and store them in `collection`
        for parser, files in self.files_parser.items():
            parser.parse(files, self.collection, logger=self.logger)

        return self.collection, self.space, self.project, self.collection_openbis

    def _make_unique_code(self, code: str, seen_codes: dict) -> str:
        """
        Generate a unique code by appending a duplicate counter if the code has already been seen.

        Args:
            code (str): The original code to make unique.
            seen_codes (dict): A dictionary tracking codes and their occurrence counts.

        Returns:
            str: The unique code, either the original code or the code with a duplicate suffix.
        """
        if code not in seen_codes:
            seen_codes[code] = 0
            return code

        seen_codes[code] += 1
        return f"{code}__dup{seen_codes[code]}"

    def _get_entity(
        self,
        openbis,
        openbis_id_map: dict[str, str],
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
                return openbis.get_object(**obj)
            except Exception as e:
                self.logger.warning(
                    f"Error occurred while fetching {object_role} object: {e}"
                )
                raise

        identifier = openbis_id_map[obj]
        return openbis.get_object(identifier)

    def _load_object_props(self, object_id, object_instance):
        """
        Load and map object properties, resolving OBJECT type references to openBIS identifiers.

        Args:
            object_id: The local identifier of the object.
            object_instance: The ObjectType instance containing properties to load.
            openbis: An instance of the Openbis class from pyBIS.
            collection: The CollectionType instance managing parsed results.
            openbis_id_map (dict): A mapping from local object IDs to openBIS identifiers.
            collection_name (str): The name of the collection in openBIS.
            space_name (str): The name of the space in openBIS.
            project_name (str): The name of the project in openBIS.

        Returns:
            dict: A dictionary of object properties with resolved references.
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
                                f"/{self.space_name}/{self.project_name}/{value.code}"
                            )
                        else:
                            referenced_identifier = f"/{self.space_name}/{self.project_name}/{self.collection.name}/{value.code}"
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
            self.openbis,
            self.openbis_id_map,
            parent,
            "parent",
        )
        child_obj = self._get_entity(
            self.openbis,
            self.openbis_id_map,
            child,
            "child",
        )
        # ...
        if parent_obj is None or child_obj is None:
            return None, None
        return parent_obj, child_obj

    def _attach_datasets(self):
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
                f"Files uploaded to openBIS collection {self.collection_openbis.name}."
            )

    def _save_datasets(self, object_instance, identifier):
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
        original_code = object_instance.code
        unique_code = self._make_unique_code(original_code, self.code_counter)
        if unique_code != original_code:
            self.logger.warning(
                f"Duplicate local code {original_code} → renamed to {unique_code}"
            )
            object_instance.code = unique_code  # Update the code in the object instance
        identifier = (
            f"/{self.space_name}/{self.project_name}/{unique_code}"
            if not self.collection_name
            else f"/{self.space_name}/{self.project_name}/{self.collection_name}/{unique_code}"
        )
        return identifier

    def run(self):
        self.openbis_id_map = {}
        self.code_counter = {}
        for object_id, object_instance in self.collection.attached_objects.items():
            obj_props = self._load_object_props(
                object_id,
                object_instance,
            )
            identifier = self._identifier(object_instance)

            # Check if object already exists in openBIS, and if so, notify and get for updating properties
            if not object_instance.code:
                if not self.collection.name:
                    object_openbis = self.openbis.new_object(
                        type=object_instance.defs.code,
                        space=self.space,
                        project=self.project,
                        props=obj_props,
                    )
                else:
                    object_openbis = self.openbis.new_object(
                        type=object_instance.defs.code,
                        space=self.space,
                        project=self.project,
                        collection=self.collection_openbis,
                        props=obj_props,
                    )
                object_openbis.save()
            else:
                try:
                    object_openbis = self.openbis.get_object(identifier)
                    object_openbis.set_props(obj_props)  # update properties
                    logger.info(
                        f"Object {identifier} already exists in openBIS, updating properties."
                    )
                except Exception:
                    logger.info(
                        f"Object with code {object_instance.code} does not exist in openBIS, creating new one."
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
        self.openbis_id_map = {}
        self.code_counter = {}

        for object_id, object_instance in self.collection.attached_objects.items():
            obj_props = self._load_object_props(
                object_id,
                object_instance,
            )

            identifier = self._identifier(object_instance)

            try:
                object = self.openbis.get_object(identifier)
            except Exception:
                object = None
            # if object exists branch in updating

            if object:
                obj = object
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
