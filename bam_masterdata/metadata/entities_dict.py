import inspect
import os
import re

import click

from bam_masterdata.logger import logger
from bam_masterdata.utils import (
    import_module,
    listdir_py_modules,
)

CLASS_DEFINITION_PATTERN = re.compile(r"^\s*class\s+(\w+)\s*\(.*\):")


class EntitiesDict:
    """
    Class to convert the entities in the datamodel defined in Python to a dictionary. The entities are read from the Python
    files defined in `python_path`.
    """

    def __init__(self, python_path: str = "", **kwargs):
        self.python_path = python_path
        self.logger = kwargs.get("logger", logger)
        self.data: dict = {}

    @staticmethod
    def _read_module_source(module_path: str) -> list[str]:
        with open(module_path, encoding="utf-8") as module_file:
            return module_file.readlines()

    @staticmethod
    def _collect_class_locations(module_source: list[str]) -> dict[str, int]:
        return {
            match.group(1): line_number
            for line_number, line in enumerate(module_source, start=1)
            if (match := CLASS_DEFINITION_PATTERN.match(line))
        }

    @staticmethod
    def _collect_member_locations(
        module_source: list[str], constructor_name: str
    ) -> dict[str, dict[str, int]]:
        member_pattern = re.compile(rf"^\s*(\w+)\s*=\s*{re.escape(constructor_name)}\(")
        member_locations: dict[str, dict[str, int]] = {}
        current_class = None

        for line_number, line in enumerate(module_source, start=1):
            class_match = CLASS_DEFINITION_PATTERN.match(line)
            if class_match:
                current_class = class_match.group(1)
                continue

            member_match = member_pattern.search(line)
            if member_match and current_class:
                member_name = member_match.group(1)
                member_locations.setdefault(current_class, {})[member_name] = (
                    line_number
                )

        return member_locations

    @staticmethod
    def _code_to_attribute_name(code: str, *, strip_dollar: bool = False) -> str:
        normalized_code = code.lower().replace(".", "_")
        if strip_dollar:
            normalized_code = normalized_code.replace("$", "")
        return normalized_code

    @classmethod
    def _assign_row_locations(
        cls,
        entity_name: str,
        items: list[dict],
        member_locations: dict[str, dict[str, int]],
        *,
        strip_dollar: bool = False,
    ) -> None:
        entity_locations = member_locations.get(entity_name, {})
        for item in items:
            attr_name = cls._code_to_attribute_name(
                item["code"], strip_dollar=strip_dollar
            )
            item["row_location"] = entity_locations.get(attr_name)

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
        module_source = self._read_module_source(module_path)
        class_locations = self._collect_class_locations(module_source)
        property_locations = self._collect_member_locations(
            module_source, "PropertyTypeAssignment"
        )
        vocabulary_term_locations = self._collect_member_locations(
            module_source, "VocabularyTerm"
        )

        # Process all classes in the module
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if not hasattr(obj, "defs") or not callable(getattr(obj, "model_to_dict")):
                continue
            try:
                obj_data = obj().model_to_dict()
                obj_data["defs"]["row_location"] = class_locations.get(name, None)

                if "properties" in obj_data:
                    self._assign_row_locations(
                        name,
                        obj_data["properties"],
                        property_locations,
                        strip_dollar=True,
                    )

                elif "terms" in obj_data:
                    self._assign_row_locations(
                        name, obj_data["terms"], vocabulary_term_locations
                    )

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
