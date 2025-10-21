from pybis import Openbis

from bam_masterdata.logger import logger
from bam_masterdata.metadata.entities import (
    CollectionType,
    ObjectType,
    PropertyTypeAssignment,
)
from bam_masterdata.parsing import AbstractParser


def run_parser(
    openbis: Openbis | None = None,
    space_name: str = "",
    project_name: str = "PROJECT",
    collection_name: str = "",
    files_parser: dict[AbstractParser, list[str]] = {},
) -> None:
    """
    Run the parsers on the specified files and collect the results.
    login with save_token=True don't forget!!

    Args:
        openbis (Openbis): An instance of the Openbis class from pyBIS, already logged in.
        space_name (str): The space in openBIS where the entities will be stored.
        project_name (str): The project in openBIS where the entities will be stored.
        collection_name (str): The collection in openBIS where the entities will be stored.
        files_parser (dict): A dictionary where keys are parser instances and values are lists of file paths to be parsed. E.g., {MasterdataParserExample(): ["path/to/file.json", "path/to/another_file.json"]}
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
                type="DEFAULT_EXPERIMENT",
                project=project,
            )
        collection_openbis.save()

    # Create a bam_masterdata CollectionType instance for storing parsed results
    collection = CollectionType()
    # Iterate over each parser and its associated files and store them in `collection`
    for parser, files in files_parser.items():
        parser.parse(files, collection, logger=logger)

    # Map the objects added to CollectionType to objects in openBIS using pyBIS
    openbis_id_map = {}
    for object_id, object_instance in collection.attached_objects.items():
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
            object_openbis = space.get_object(identifier)
            object_openbis.set_props(obj_props)
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
