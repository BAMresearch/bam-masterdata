import glob
import importlib.util
import inspect
import json
import os
import re
import shutil
from itertools import chain
from typing import TYPE_CHECKING, Any, Optional

from bam_masterdata.logger import logger

if TYPE_CHECKING:
    from structlog._config import BoundLoggerLazyProxy


def delete_and_create_dir(
    directory_path: str,
    logger: "BoundLoggerLazyProxy" = logger,
    force_delete: bool = False,
) -> None:
    """
    Deletes the directory at `directory_path` and creates a new one in the same path.

    Args:
        directory_path (str): The directory path to delete and create the folder.
        logger (BoundLoggerLazyProxy): The logger to log messages. Default is `logger`.
        force_delete (bool): If True, the directory will be forcibly deleted if it exists.
    """
    if not directory_path:
        logger.warning(
            "The `directory_path` is empty. Please, provide a proper input to the function."
        )
        return None

    if not force_delete:
        logger.info(f"Skipping the deletion of the directory at {directory_path}.")
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        return None

    if os.path.exists(directory_path):
        try:
            shutil.rmtree(directory_path)  # ! careful with this line
        except PermissionError:
            logger.error(
                f"Permission denied to delete the directory at {directory_path}."
            )
            return None
    os.makedirs(directory_path)


def listdir_py_modules(
    directory_path: str, logger: "BoundLoggerLazyProxy" = logger
) -> list[str]:
    """
    Recursively goes through the `directory_path` and returns a list of all .py files that do not start with '_'. If
    `directory_path` is a single Python module file, it will return a list with that file.

    Args:
        directory_path (str): The directory path to search through.
        logger (BoundLoggerLazyProxy): The logger to log messages. Default is `logger`.

    Returns:
        list[str]: A list of all .py files that do not start with '_'
    """
    if not directory_path:
        logger.warning(
            "The `directory_path` is empty. Please, provide a proper input to the function."
        )
        return []

    # In case of a individual Python module file
    if directory_path.endswith(".py"):
        return [directory_path]
    # Use glob to find all .py files recursively in a directory containing all modules
    else:
        files = glob.glob(os.path.join(directory_path, "**", "*.py"), recursive=True)
    if not files:
        logger.info("No Python files found in the directory.")
        return []

    # Filter out files that start with '_'
    # ! sorted in order to avoid using with OS sorting differently
    return sorted(
        [
            f
            for f in files
            if not os.path.basename(f).startswith("_") and "tmp" not in f.split(os.sep)
        ]
    )


def import_module(module_path: str) -> Any:
    """
    Dynamically imports a module from the given file path.

    Args:
        module_path (str): Path to the Python module file.

    Returns:
        module: Imported module object.
    """
    module_name = os.path.splitext(os.path.basename(module_path))[0]
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def code_to_class_name(
    code: Optional[str],
    logger: "BoundLoggerLazyProxy" = logger,
    entity_type: str = "object",
) -> str:
    """
    Converts an openBIS `code` to a class name by capitalizing each word and removing special characters. In
    the special case the entity is a property type, it retains the full name separated by points instead of
    only keeping the last name (e.g., "TEM.INSTRUMENT" -> "TemInstrument" instead of "Instrument").

    Args:
        code (str): The openBIS code to convert to a class name.
        logger (BoundLoggerLazyProxy): The logger to log messages. Default is `logger`.
        entity_type (str): The type of entity to convert. Default is "object".
    Returns:
        str: The class name derived from the openBIS code.
    """
    if not code:
        logger.error(
            "The `code` is empty. Please, provide a proper input to the function."
        )
        return ""

    if entity_type == "property":
        code_names = chain.from_iterable(
            [c.split("_") for c in code.lstrip("$").split(".")]
        )
        return "".join(c.capitalize() for c in code_names)
    return "".join(c.capitalize() for c in code.lstrip("$").rsplit(".")[-1].split("_"))


def load_validation_rules(
    logger: "BoundLoggerLazyProxy",
    file_path: str = "./bam_masterdata/validation_rules/excel_validation_rules.json",
):
    if not os.path.exists(file_path):
        logger.error(f"Validation rules file not found: {file_path}")
        raise FileNotFoundError(f"Validation rules file not found: {file_path}")

    try:
        with open(file_path, encoding="utf-8") as file:
            validation_rules = json.load(file)

        logger.info("Validation rules successfully loaded.")

        return validation_rules

    except json.JSONDecodeError as e:
        logger.error(f"Error parsing validation rules JSON: {e}")
        raise ValueError(f"Error parsing validation rules JSON: {e}")


from pathlib import Path


def duplicated_property_types(module_path: str, logger: "BoundLoggerLazyProxy") -> dict:
    """
    Find the duplicated property types in a module specified by `module_path` and returns a dictionary
    containing the duplicated property types class names as keys and the lines where they matched as values.

    Args:
        module_path (str): The path to the module containing the property types.
        logger (BoundLoggerLazyProxy): The logger to log messages.

    Returns:
        dict: A dictionary containing the duplicated property types class names as keys and the
        lines where they matched as values.
    """
    duplicated_props: dict = {}
    module = import_module(module_path=module_path)
    source_code = inspect.getsource(module)
    for name, _ in inspect.getmembers(module):
        if name.startswith("_") or name == "PropertyTypeDef":
            continue

        pattern = rf"^\s*{name} *= *PropertyTypeDef"

        # Find all matching line numbers
        matches = [
            i + 1  # Convert to 1-based index
            for i, line in enumerate(source_code.splitlines())
            if re.match(pattern, line)
        ]
        if len(matches) > 1:
            duplicated_props[name] = matches
    if duplicated_props:
        logger.critical(
            f"Found {len(duplicated_props)} duplicated property types. These are stored in a dictionary "
            f"where the keys are the names of the variables in property_types.py and the values are the lines in the module: {duplicated_props}"
        )
    return duplicated_props
