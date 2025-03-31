import inspect
import os
import re

import click

from bam_masterdata.logger import logger
from bam_masterdata.utils import (
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

        # Read the module source code and store line numbers
        with open(module_path, encoding="utf-8") as f:
            module_source = f.readlines()

        # Detect class definitions (entity types)
        class_locations = {
            match.group(1): i + 1  # Store line number (1-based index)
            for i, line in enumerate(module_source)
            if (match := re.match(r"^\s*class\s+(\w+)\s*\(.*\):", line))
        }

        # Detect property assignments (`PropertyTypeAssignment(...)`) with class context
        property_locations: dict = {}
        current_class = None

        for i, line in enumerate(module_source):
            class_match = re.match(r"^\s*class\s+(\w+)\s*\(.*\):", line)
            if class_match:
                current_class = class_match.group(1)

            prop_match = re.search(r"^\s*(\w+)\s*=\s*PropertyTypeAssignment\(", line)
            if prop_match and current_class:
                property_name = prop_match.group(1)
                if current_class not in property_locations:
                    property_locations[current_class] = {}
                property_locations[current_class][property_name] = i + 1

        # Detect vocabulary terms (`VocabularyTerm(...)`) with class context
        vocabulary_term_locations: dict = {}
        current_vocab_class = None

        for i, line in enumerate(module_source):
            class_match = re.match(r"^\s*class\s+(\w+)\s*\(.*\):", line)
            if class_match:
                current_vocab_class = class_match.group(1)

            term_match = re.search(r"^\s*(\w+)\s*=\s*VocabularyTerm\(", line)
            if term_match and current_vocab_class:
                term_name = term_match.group(1)
                if current_vocab_class not in vocabulary_term_locations:
                    vocabulary_term_locations[current_vocab_class] = {}
                vocabulary_term_locations[current_vocab_class][term_name] = i + 1

        # Process all classes in the module
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if not hasattr(obj, "defs") or not callable(getattr(obj, "model_to_dict")):
                continue
            try:
                obj_data = obj().model_to_dict()
                obj_data["defs"]["row_location"] = class_locations.get(name, None)

                if "properties" in obj_data:
                    # Processing standard properties (PropertyTypeAssignment)
                    for prop in obj_data["properties"]:
                        prop_id = (
                            prop["code"].lower().replace(".", "_").replace("$", "")
                        )
                        matched_key = next(
                            (
                                key
                                for key in property_locations.get(name, {})
                                if key == prop_id
                            ),
                            None,
                        )
                        prop["row_location"] = property_locations.get(name, {}).get(
                            matched_key, None
                        )

                elif "terms" in obj_data:
                    # Processing vocabulary terms (VocabularyTerm)
                    for term in obj_data["terms"]:
                        term_id = term["code"].lower().replace(".", "_")
                        matched_key = next(
                            (
                                key
                                for key in vocabulary_term_locations.get(name, {})
                                if key == term_id
                            ),
                            None,
                        )
                        term["row_location"] = vocabulary_term_locations.get(
                            name, {}
                        ).get(matched_key, None)

                data[obj.defs.code] = obj_data
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
            data = self.to_dict(module_path=module_path)
            # name can be collection_type, object_type, dataset_type, vocabulary_type, or property_type
            name = os.path.basename(module_path).replace(".py", "")
            full_data[name] = data
        return full_data
