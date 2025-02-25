<<<<<<< HEAD
import json
import os

from bam_masterdata.cli.entities_dict import EntitiesDict
from bam_masterdata.logger import logger


class DataModelLoader:
    def __init__(
        self,
        source_dir: str = "bam_masterdata/datamodel",
        export_dir: str = "bam_masterdata/checker/tmp/datamodel",
    ):
        """
        Initialize the DataModelLoader.

        Args:
            source_dir (str): Directory where the Python datamodel files are located.
            export_dir (str): Directory where the final JSON file will be saved.
        """
        self.source_dir = source_dir
        self.export_dir = export_dir
        self.logger = logger
        self.data = self.parse_pydantic_models()
        self._save_json_file()  # Using standard logging
=======
import inspect
import json
import os
from typing import TYPE_CHECKING
>>>>>>> 3e1c0f647499112e50bf6118aad054efc1816c03

if TYPE_CHECKING:
    from structlog._config import BoundLoggerLazyProxy

import click

from bam_masterdata.logger import logger
from bam_masterdata.utils import import_module


class DataModelLoader:
    def __init__(
        self,
        source_paths: list[str],
    ):
        """
<<<<<<< HEAD
        Reads Pydantic classes from the provided source directory, converts them to JSON format,
        and returns a dictionary representation of all entities.

        Returns:
            dict: A dictionary containing JSON data of all Pydantic entities.
        """
        entities_dict = EntitiesDict(python_path=self.source_dir, logger=self.logger)
        return entities_dict.single_json()

    def _save_json_file(self):
        """
        Saves the extracted data to a JSON file in the export directory.
        """
        os.makedirs(self.export_dir, exist_ok=True)  # Ensure export directory exists
        output_file = os.path.join(self.export_dir, "full_datamodel.json")

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2)

        self.logger.info(f"Saved full aggregated JSON to {output_file}")
=======
        Initialize the DataModelLoader.

        Args:
            source_paths (list[str]): List of Python module paths containing the Pydantic models.
        """
        self.source_paths = source_paths
        self.logger = logger
        self.data = self.entities_to_single_dict(self.source_paths)

    @staticmethod
    def entities_to_single_dict(module_paths: list[str]) -> dict[str, dict[str, dict]]:
        """
        Process all entities from multiple Python modules and store them into a single dictionary.

        Args:
            module_paths (list[str]): List of Python module file paths.
            logger (BoundLoggerLazyProxy): The logger to log messages.

        Returns:
            dict: A nested dictionary containing all entities, structured as:
                {
                    "module_name": {
                        "entity_code": {
                            "properties": [...],
                            "defs": {...}
                        }
                    },
                    "property_types": {
                        "property_code": {
                            "code": "...",
                            "description": "...",
                            "id": "...",
                            "property_label": "...",
                            "data_type": "...",
                            "vocabulary_code": "...",
                            "object_code": "...",
                            "metadata": null,
                            "dynamic_script": null
                        }
                    }
                }
        """
        aggregated_data = {}
        property_types = {}

        export_dir = "bam_masterdata/checker/tmp/datamodel"

        for module_path in module_paths:
            # Skip __init__.py file
            if os.path.basename(module_path) == "__init__.py":
                logger.info(f"Skipping {module_path} (init file)")
                continue

            module = import_module(module_path=module_path)
            module_name = os.path.basename(module_path).replace(".py", "")

            # Special case for property_types.py
            if "property_types.py" in module_path:
                for name, obj in inspect.getmembers(module):
                    if name.startswith("_") or name == "PropertyTypeDef":
                        continue
                    try:
                        property_data = obj.model_dump()
                        property_types[property_data["code"]] = property_data
                    except Exception as err:
                        click.echo(
                            f"Failed to process property {name} in {module_path}: {err}"
                        )
                continue  # ✅ Skip normal processing for this module

            # Dictionary to store data from this module
            module_data = {}

            # Process all datamodel classes
            for name, obj in inspect.getmembers(module, inspect.isclass):
                # Ensure the class has `defs` and a callable `model_to_json` method
                if not hasattr(obj, "defs") or not callable(
                    getattr(obj, "model_to_json")
                ):
                    continue
                try:
                    entity_code = (
                        obj.defs.code
                    )  # Get the code from the class definition

                    # Convert JSON string to a dictionary
                    json_data = json.loads(obj().model_to_json(indent=2))

                    module_data[entity_code] = json_data  # Store as dictionary
                except Exception as err:
                    click.echo(
                        f"Failed to process class {name} in {module_path}: {err}"
                    )

            # Add this module's data to the aggregated dictionary
            if module_data:
                aggregated_data[module_name] = module_data

        # ✅ Add property types separately
        if property_types:
            aggregated_data["property_types"] = property_types

        # Save as one big JSON file
        os.makedirs(export_dir, exist_ok=True)  # Ensure the export directory exists
        output_file = os.path.join(export_dir, "full_datamodel.json")

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(aggregated_data, f, indent=2)

        logger.info(f"Saved full aggregated JSON to {output_file}")

        return aggregated_data
>>>>>>> 3e1c0f647499112e50bf6118aad054efc1816c03
