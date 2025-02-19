import inspect
import json
import logging
import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from structlog._config import BoundLoggerLazyProxy

import click

from bam_masterdata.utils import import_module


class DataModelLoader:
    def __init__(
        self,
        source_paths: list[str],
    ):
        """
        Initialize the DataModelLoader.

        Args:
            source_paths (list[str]): List of Python module paths containing the Pydantic models.
        """
        self.source_paths = source_paths
        self.logger = logging.getLogger(__name__)  # Using standard logging

    @staticmethod
    def entities_to_single_dict(
        module_paths: list[str], logger: "BoundLoggerLazyProxy"
    ) -> dict[str, dict[str, dict]]:
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
                    }
                }
        """
        aggregated_data = {}

        export_dir = "bam_masterdata/checker/tmp/datamodel"

        for module_path in module_paths:
            # Skip __init__.py file
            if os.path.basename(module_path) == "__init__.py":
                logger.info(f"Skipping {module_path} (init file)")
                continue

            module = import_module(module_path=module_path)
            module_name = os.path.basename(module_path).replace(".py", "")

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

        # Save as one big JSON file
        os.makedirs(export_dir, exist_ok=True)  # Ensure the export directory exists
        output_file = os.path.join(export_dir, "full_datamodel.json")

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(aggregated_data, f, indent=2)

        logger.info(f"Saved full aggregated JSON to {output_file}")

        return aggregated_data

    def parse_pydantic_models(self) -> dict:
        """
        Reads Pydantic classes from the provided source paths, converts them to JSON format,
        and aggregates them into a single dictionary.

        Returns:
            dict: A nested dictionary containing all Pydantic entities.
        """
        return self.entities_to_single_dict(self.source_paths, self.logger)

    def _load_json_files(self) -> dict:
        """
        Reads the full_datamodel.json file from the export directory and loads it into a dictionary.

        Returns:
            dict: A dictionary containing all the aggregated data.
        """
        data_model_json = {}
        json_file_path = os.path.join(self.export_dir, "full_datamodel.json")

        if not os.path.exists(json_file_path):
            self.logger.error(
                f"Error: {json_file_path} not found. Run the extraction process first."
            )
            return (
                data_model_json  # Return an empty dictionary if the file doesn't exist
            )

        try:
            with open(json_file_path, encoding="utf-8") as f:
                data_model_json = json.load(f)
        except json.JSONDecodeError as err:
            self.logger.error(f"Error loading JSON from {json_file_path}: {err}")

        return data_model_json
