from pybis import Openbis

from bam_masterdata.logger import logger
from bam_masterdata.metadata.entities import (
    CollectionType,
    ObjectType,
    PropertyTypeAssignment,
)
from bam_masterdata.parsing import AbstractParser


def _parser_init(
    openbis: Openbis | None = None,
    space_name: str = "",
    project_name: str = "PROJECT",
    collection_name: str = "",
    files_parser: dict[AbstractParser, list[str]] = {},
    collection_type: str = "COLLECTION",
) -> tuple[CollectionType, any, any, any] | None:
    """
    Initialize the parser by setting up spaces, projects, and collections in openBIS.

    Args:
        openbis (Openbis | None): An instance of the Openbis class from pyBIS, already logged in.
        space_name (str): The space in openBIS where the entities will be stored.
        project_name (str): The project in openBIS where the entities will be stored.
        collection_name (str): The collection in openBIS where the entities will be stored.
        files_parser (dict[AbstractParser, list[str]]): A dictionary mapping parser instances to lists of file paths.
        collection_type (str): The type of collection to create. Options are "COLLECTION" or "DEFAULT_EXPERIMENT".

    Returns:
        tuple: A tuple containing (collection, space, project, collection_openbis) if successful, None otherwise.
    """
    # Ensure openbis is provided
    if openbis is None:
        logger.error("An instance of Openbis must be provided for the parser to run.")
        return
    # Ensure the space, project, and collection are set
    if not project_name:
        logger.error("The Project name must be specified for the parser to run.")
        return
    # Ensure the files_parser is not empty
    if not files_parser:
        logger.error(
            "No files or parsers to parse. Please provide valid file paths or contact an Admin to add missing parser."
        )
        return
    # Ensure collection_type is valid
    if collection_type not in ["COLLECTION", "DEFAULT_EXPERIMENT"]:
        logger.error(
            f"Invalid collection_type '{collection_type}'. Must be either 'COLLECTION' or 'DEFAULT_EXPERIMENT'."
        )
        return

    # Specify the space
    try:
        space = openbis.get_space(space_name)
    except Exception:
        space = None
    # If space is not found, use the user space
    if space is None:
        # user name as default space
        for s in openbis.get_spaces():
            if s.code.endswith(openbis.username.upper()):
                space = s
                logger.warning(
                    f"Space {space_name} does not exist in openBIS. "
                    f"Loading space for {openbis.username}."
                )
                break
        # no space found
        if space is None:
            logger.error(
                f"No usable Space for {openbis.username} in openBIS. Please create it first or notify an Admin."
            )
            return

    # Get project if `project_name` already exists under the space or create a new one if it does not
    if project_name.upper() in [p.code for p in space.get_projects()]:
        project = space.get_project(project_name)
    else:
        logger.info("Replacing project code with uppercase and underscores.")
        project = space.new_project(
            code=project_name.replace(" ", "_").upper(),
            description="New project created via automated parsing with `bam_masterdata`.",
        )
    project.save()

    # Create a new pybis `COLLECTION` to store the generated objects
    if not collection_name:
        logger.info(
            "No Collection name specified. Attaching objects directly to Project."
        )
        collection_openbis = project
    else:
        if collection_name.upper() in [c.code for c in project.get_collections()]:
            collection_openbis = space.get_collection(
                f"/{space_name}/{project_name}/{collection_name}".upper()
            )
        else:
            logger.info("Replacing collection code with uppercase and underscores.")
            collection_openbis = openbis.new_collection(
                code=collection_name.replace(" ", "_").upper(),
                type=collection_type,
                project=project,
            )
        collection_openbis.save()

    # Create a bam_masterdata CollectionType instance for storing parsed results
    collection = CollectionType()
    # Iterate over each parser and its associated files and store them in `collection`
    for parser, files in files_parser.items():
        parser.parse(files, collection, logger=logger)

    return collection, space, project, collection_openbis


def _load_object_props(
    object_id: any,
    object_instance: ObjectType,
    openbis: Openbis,
    collection: CollectionType,
    openbis_id_map: dict,
    collection_name: str,
    space_name: str,
    project_name: str,
) -> dict:
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
                    referenced_object = openbis.get_object(value)
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
                for obj_id, obj_inst in collection.attached_objects.items():
                    if obj_inst is value and obj_id in openbis_id_map:
                        referenced_identifier = openbis_id_map[obj_id]
                        break
                if not referenced_identifier:
                    # Construct identifier from the object's code
                    # Assume it's in the same space/project as the current object
                    if not collection_name:
                        referenced_identifier = (
                            f"/{space_name}/{project_name}/{value.code}"
                        )
                    else:
                        referenced_identifier = f"/{space_name}/{project_name}/{collection_name}/{value.code}"
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


def make_unique_code(code: str, seen_codes: dict) -> str:
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


def run_parser(
    openbis: Openbis | None = None,
    space_name: str = "",
    project_name: str = "PROJECT",
    collection_name: str = "",
    files_parser: dict[AbstractParser, list[str]] = {},
    collection_type: str = "COLLECTION",
) -> None:
    """
    Run the parsers on the specified files and save objects immediately without using transactions.

    This function parses files and creates/updates objects in openBIS individually, saving each object
    immediately after creation. This approach is simpler to debug but less efficient than transactions.
    After all objects are created, parent-child relationships are established.

    Unlike run_parser_with_transactions(), this functions main difference is that it saves
    each object to openBIS immediately after creation, so objects-uploads are not
    dependent on others being successfully created.


    Args:
        openbis (Openbis): An instance of the Openbis class from pyBIS, already logged in.
        space_name (str): The space in openBIS where the entities will be stored.
        project_name (str): The project in openBIS where the entities will be stored.
        collection_name (str): The collection in openBIS where the entities will be stored.
        files_parser (dict): A dictionary where keys are parser instances and values are lists of file paths to be parsed. E.g., {MasterdataParserExample(): ["path/to/file.json", "path/to/another_file.json"]}
        collection_type (str): The type of collection to create in openBIS. Options are "COLLECTION" or "DEFAULT_EXPERIMENT". Defaults to "COLLECTION".
    """
    collection, space, project, collection_openbis = _parser_init(
        openbis=openbis,
        space_name=space_name,
        collection_name=collection_name,
        project_name=project_name,
        files_parser=files_parser,
        collection_type=collection_type,
    )

    # Map the objects added to CollectionType to objects in openBIS using pyBIS
    openbis_id_map = {}
    for object_id, object_instance in collection.attached_objects.items():
        obj_props = _load_object_props(
            object_id,
            object_instance,
            openbis,
            collection,
            openbis_id_map,
            collection_name,
            space_name,
            project_name,
        )

        # Check if object already exists in openBIS, and if so, notify and get for updating properties
        if not object_instance.code:
            if not collection_name:
                object_openbis = openbis.new_object(
                    type=object_instance.defs.code,
                    space=space,
                    project=project,
                    props=obj_props,
                )
            else:
                object_openbis = openbis.new_object(
                    type=object_instance.defs.code,
                    space=space,
                    project=project,
                    collection=collection_openbis,
                    props=obj_props,
                )
            object_openbis.save()
        else:
            identifier = (
                f"/{space_name}/{project_name}/{object_instance.code}"
                if not collection_name
                else f"/{space_name}/{project_name}/{collection_name}/{object_instance.code}"
            )
            try:
                object_openbis = space.get_object(identifier)
                object_openbis.set_props(obj_props)  # update properties
            except Exception:
                logger.info(
                    f"Object with code {object_instance.code} does not exist in openBIS, creating new one."
                )
                if not collection_name:
                    object_openbis = openbis.new_object(
                        type=object_instance.defs.code,
                        code=object_instance.code,
                        space=space,
                        project=project,
                        props=obj_props,
                    )
                else:
                    object_openbis = openbis.new_object(
                        type=object_instance.defs.code,
                        code=object_instance.code,
                        space=space,
                        project=project,
                        collection=collection_openbis,
                        props=obj_props,
                    )
            object_openbis.save()
            logger.info(
                f"Object {identifier} already exists in openBIS, updating properties."
            )

        # save local and openbis IDs to map parent-child relationships
        openbis_id_map[object_id] = object_openbis.identifier

    # Storing files as datasets in openBIS
    for files in files_parser.values():
        try:
            if not collection_name:
                # ! This won't work on a project -> datasets only attached to collections in pyBIS
                dataset = openbis.new_dataset(
                    type="RAW_DATA",
                    files=files,
                    project=project,
                )
            else:
                dataset = openbis.new_dataset(
                    type="RAW_DATA",
                    files=files,
                    collection=collection_openbis,
                )
            dataset.save()
        except Exception as e:
            logger.warning(f"Error uploading files {files} to openBIS: {e}")
            continue
        logger.info(f"Files uploaded to openBIS collection {collection_name}.")

    # Map parent-child relationships
    for parent_id, child_id in collection.relationships.values():
        if parent_id in openbis_id_map and child_id in openbis_id_map:
            parent_openbis_id = openbis_id_map[parent_id]
            child_openbis_id = openbis_id_map[child_id]

            child_openbis = openbis.get_object(child_openbis_id)
            child_openbis.add_parents(parent_openbis_id)
            child_openbis.save()

            logger.info(
                f"Linked child {child_openbis_id} to parent {parent_openbis_id} in collection {collection_name}."
            )


def run_parser_with_transactions(
    openbis: Openbis | None = None,
    space_name: str = "",
    project_name: str = "PROJECT",
    collection_name: str = "",
    files_parser: dict[AbstractParser, list[str]] = {},
    collection_type: str = "COLLECTION",
) -> None:
    """
    Run the parsers on the specified files and save objects using openBIS transactions.

    This function parses files and creates/updates objects in openBIS using transactions for atomicity.
    Operations are batched and committed together, ensuring consistency. If any operation fails,
    all changes within that transaction are rolled back.

    Args:
        openbis (Openbis): An instance of the Openbis class from pyBIS, already logged in.
        space_name (str): The space in openBIS where the entities will be stored.
        project_name (str): The project in openBIS where the entities will be stored.
        collection_name (str): The collection in openBIS where the entities will be stored.
        files_parser (dict): A dictionary where keys are parser instances and values are lists of file paths to be parsed. E.g., {MasterdataParserExample(): ["path/to/file.json", "path/to/another_file.json"]}
        collection_type (str): The type of collection to create in openBIS. Options are "COLLECTION" or "DEFAULT_EXPERIMENT". Defaults to "COLLECTION".
    """
    collection, space, project, collection_openbis = _parser_init(
        openbis=openbis,
        space_name=space_name,
        collection_name=collection_name,
        project_name=project_name,
        files_parser=files_parser,
        collection_type=collection_type,
    )

    obj_transaction = openbis.new_transaction()

    openbis_id_map = {}
    code_counter = {}

    for object_id, object_instance in collection.attached_objects.items():
        obj_props = _load_object_props(
            object_id,
            object_instance,
            openbis,
            collection,
            openbis_id_map,
            collection_name,
            space_name,
            project_name,
        )

        original_code = object_instance.code
        unique_code = make_unique_code(original_code, code_counter)

        if unique_code != original_code:
            logger.warning(
                f"Duplicate local code {original_code} → renamed to {unique_code}"
            )

        identifier = (
            f"/{space_name}/{project_name}/{unique_code}"
            if not collection_name
            else f"/{space_name}/{project_name}/{collection_name}/{unique_code}"
        )

        try:
            object = openbis.get_object(identifier)
        except Exception:
            object = None
        # if object exists branch in updating

        if object:
            obj = object
            obj.set_props(obj_props)
            obj_transaction.add(obj)
            logger.info(f"{identifier} will be UPDATED in transaction")

        else:
            obj = openbis.new_object(
                type=object_instance.defs.code,
                code=unique_code,
                space=space,
                project=project,
                collection=collection_openbis if collection_name else None,
                props=obj_props,
            )
            obj_transaction.add(obj)
            logger.info(f"{identifier} will be CREATED in transaction")

        openbis_id_map[object_id] = identifier

    try:
        obj_transaction.commit()
        logger.info("Transaction committed successfully")
    except Exception as e:
        logger.error(f"Failed to commit object transaction: {e}")
        return None

    rel_transaction = openbis.new_transaction()

    # ---- DATASETS IN TRANSACTION ----
    for files in files_parser.values():
        try:
            if collection_name:
                dataset = openbis.new_dataset(
                    type="RAW_DATA",
                    files=files,
                    collection=collection_openbis,
                )
            else:
                dataset = openbis.new_dataset(
                    type="RAW_DATA",
                    files=files,
                    project=project,
                )

            rel_transaction.add(dataset)
            logger.info(f"Dataset for files {files} added to transaction")

        except Exception as e:
            logger.warning(f"Error preparing dataset {files}: {e}")

    # ---- RELATIONSHIPS IN TRANSACTION ----
    for parent_id, child_id in collection.relationships.values():
        if parent_id not in openbis_id_map or child_id not in openbis_id_map:
            continue

        parent_identifier = openbis_id_map[parent_id]
        child_identifier = openbis_id_map[child_id]

        parent_identifier
        child_identifier
        parent = openbis.get_object(parent_identifier)
        child = openbis.get_object(child_identifier)

        child.add_parents(parent)
        rel_transaction.add(child)

        logger.info(
            f"Prepared relationship: {child_identifier} -> parent {parent_identifier}"
        )

    try:
        rel_transaction.commit()
        logger.info("Datasets and relationships committed successfully")
    except Exception as e:
        logger.error(f"Failed to commit datasets/relationships: {e}")
