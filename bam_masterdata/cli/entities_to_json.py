import inspect
import json

import click

from bam_masterdata.utils import import_module


def entities_to_json(module_path: str) -> dict:
    """
    Export entities to JSON files. The Python modules are imported using the function `import_module`,
    and their contents are inspected (using `inspect`) to find the classes in the datamodel containing
    `defs` and with a `model_to_json` method defined.

    Args:
        module_path (str): Path to the Python module file.
        export_dir (str): Path to the directory where the JSON files will be saved.
        logger (BoundLoggerLazyProxy): The logger to log messages.
    """
    module = import_module(module_path=module_path)

    # initializing the dictionary with keys as the `code` of the entity and values the json dumped data
    json_data: dict = {}

    # Special case of `PropertyTypeDef` in `property_types.py`
    if "property_types.py" in module_path:
        for name, obj in inspect.getmembers(module):
            if name.startswith("_") or name == "PropertyTypeDef":
                continue
            try:
                # json_data[obj.code] = json.dumps(obj.model_dump(), indent=2)
                json_data[obj.code] = obj.model_dump()
            except Exception as err:
                click.echo(f"Failed to process class {name} in {module_path}: {err}")
        return json_data

    # All other datamodel modules
    for name, obj in inspect.getmembers(module, inspect.isclass):
        # Ensure the class has the `model_to_json` method
        if not hasattr(obj, "defs") or not callable(getattr(obj, "model_to_json")):
            continue

        try:
            # Instantiate the class and call the method
            json_data[obj.defs.code] = obj().model_to_dict()
        except Exception as err:
            click.echo(f"Failed to process class {name} in {module_path}: {err}")

    return json_data
