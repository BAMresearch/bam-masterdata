import glob
import importlib.util
import os
import shutil
from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from structlog._config import BoundLoggerLazyProxy


def delete_and_create_dir(
    directory_path: Optional[str], logger: 'BoundLoggerLazyProxy'
) -> None:
    """
    Deletes the directory at `directory_path` and creates a new one in the same path.

    Args:
        directory_path (Optional[str]): The directory path to delete and create the folder.
        logger (BoundLoggerLazyProxy): The logger to log messages.
    """
    if not directory_path:
        logger.warning(
            'The `directory_path` is empty. Please, provide a proper input to the function.'
        )
        return None

    if os.path.exists(directory_path):
        shutil.rmtree(directory_path)
    os.makedirs(directory_path)


def listdir_py_modules(
    directory_path: Optional[str], logger: 'BoundLoggerLazyProxy'
) -> list[str]:
    """
    Recursively goes through the `directory_path` and returns a list of all .py files that do not start with '_'.

    Args:
        directory_path (Optional[str]): The directory path to search through.
        logger (BoundLoggerLazyProxy): The logger to log messages.

    Returns:
        list[str]: A list of all .py files that do not start with '_'
    """
    if not directory_path:
        logger.warning(
            'The `directory_path` is empty. Please, provide a proper input to the function.'
        )
        return []

    # Use glob to find all .py files recursively
    files = glob.glob(os.path.join(directory_path, '**', '*.py'), recursive=True)
    if not files:
        logger.info('No Python files found in the directory.')
        return []

    # Filter out files that start with '_'
    return [f for f in files if not os.path.basename(f).startswith('_')]


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
