import inspect
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from structlog._config import BoundLoggerLazyProxy

from bam_masterdata.utils import import_module


def duplicated_property_types(module_path: str, logger: "BoundLoggerLazyProxy") -> dict:
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
