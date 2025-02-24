import inspect
import os

import click

from bam_masterdata.logger import logger
from bam_masterdata.utils import (
    duplicated_property_types,
    import_module,
    listdir_py_modules,
)


class EntitiesDict:
    """
    Class to convert the entities in the datamodel defined in Python to a dictionary. The entities are read from the Python
    files defined in `python_path`.
    """

    def __init__(self, python_path: str = "", **kwargs):
        self.python_path = python_path
        self.logger = kwargs.get("logger", logger)
        self.data: dict = {}

    def to_dict(self, module_path: str) -> dict:
        """
        Returns a dictionary containing entities read from the `module_path` Python file. The Python modules
        are imported using the function `import_module` and their contents are inspected (using `inspect`) to
        find the classes in the datamodel containing `defs` and with a `model_to_dict` method defined.

        Args:
            module_path (str): Path to the Python module file.

        Returns:
            dict: A dictionary containing the entities in the datamodel defined in one Python module file.
        """
        module = import_module(module_path=module_path)

        # initializing the dictionary with keys as the `code` of the entity and values the json dumped data
        data: dict = {}

        # Special case of `PropertyTypeDef` in `property_types.py`
        if "property_types.py" in module_path:
            for name, obj in inspect.getmembers(module):
                if name.startswith("_") or name == "PropertyTypeDef":
                    continue
                try:
                    data[obj.code] = obj.model_dump()
                except Exception as err:
                    click.echo(
                        f"Failed to process class {name} in {module_path}: {err}"
                    )
            return data

        # All other datamodel modules
        for name, obj in inspect.getmembers(module, inspect.isclass):
            # Ensure the class has the `model_to_json` method
            if not hasattr(obj, "defs") or not callable(getattr(obj, "model_to_dict")):
                continue

            try:
                # Instantiate the class and call the method
                data[obj.defs.code] = obj().model_to_dict()
            except Exception as err:
                click.echo(f"Failed to process class {name} in {module_path}: {err}")

        return data

    def single_json(self) -> dict:
        """
        Returns a single dictionary containing all the entities in the datamodel defined in the Python files
        in `python_path`. The format of this dictionary is:
            {
                "collection_type": {
                    "COLLECTION": {
                        "defs": {
                            "code": "COLLECTION",
                            "description": "",
                            ...
                        },
                        "properties": [
                            {
                                "code": "$DEFAULT_COLLECTION_VIEW",
                                "description": "Default view for experiments of the type collection",
                                ...
                            },
                            {...},
                            ...
                        ]
                    }
                },
                "object_type": {...},
                ...
            }

        Returns:
            dict: A dictionary containing all the entities in the datamodel.
        """
        # Get the Python modules to process the datamodel
        py_modules = listdir_py_modules(
            directory_path=self.python_path, logger=self.logger
        )

        # Process each module using the `model_to_dict` method of each entity and store them in a single dictionary
        full_data: dict = {}
        for module_path in py_modules:
            if module_path.endswith("property_types.py"):
                if duplicated_property_types(
                    module_path=module_path, logger=self.logger
                ):
                    click.echo(
                        "Please fix the duplicated property types before exporting to JSON."
                    )
                    return {}

            data = self.to_dict(module_path=module_path)
            # name can be collection_type, object_type, dataset_type, vocabulary_type, or property_type
            name = os.path.basename(module_path).replace(".py", "")
            full_data[name] = data
        return full_data
