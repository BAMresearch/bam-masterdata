import inspect
import json
import logging
import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from structlog._config import BoundLoggerLazyProxy

import click

from bam_masterdata.cli.entities_to_json import entities_to_json
from bam_masterdata.utils import delete_and_create_dir, import_module


class DataModelLoader:
    def __init__(
        self,
        source_paths: list[str],
        export_dir: str = "bam_masterdata/checker/tmp/datamodel",
    ):
        """
        Initialize the DataModelLoader.

        Args:
            source_paths (list[str]): List of Python module paths containing the Pydantic models.
            export_dir (str): Directory where the JSON files will be saved.
        """
        self.source_paths = source_paths
        self.export_dir = export_dir
        self.logger = logging.getLogger(__name__)  # Using standard logging

    @staticmethod
    def entities_to_single_json(
        module_path: str, export_dir: str, logger: "BoundLoggerLazyProxy"
    ) -> None:
        """
        Export all entities from a single Python module into ONE JSON file,
        grouping all the entities under their corresponding category (defs.code).

        Args:
            module_path (str): Path to the Python module file.
            export_dir (str): Path to the directory where the JSON file will be saved.
            logger (BoundLoggerLazyProxy): The logger to log messages.
        """
        module = import_module(module_path=module_path)
        module_name = os.path.basename(module_path).replace(".py", "")

        # Ensure export directory exists
        os.makedirs(export_dir, exist_ok=True)

        # Dictionary to hold all class data in the module, grouped by defs.code
        module_data = {}

        # Process all datamodel classes
        for name, obj in inspect.getmembers(module, inspect.isclass):
            # Ensure the class has `defs` and a callable `model_to_json` method
            if not hasattr(obj, "defs") or not callable(getattr(obj, "model_to_json")):
                continue
            try:
                entity_code = obj.defs.code  # Get the code from the class definition

                # Convert JSON string to a dictionary
                json_data = json.loads(obj().model_to_json(indent=2))

                module_data[entity_code] = json_data  # Store as dictionary
            except Exception as err:
                click.echo(f"Failed to process class {name} in {module_path}: {err}")

        # Write everything to a single JSON file
        output_file = os.path.join(export_dir, f"{module_name}.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(module_data, f, indent=2)

        click.echo(f"Saved grouped JSON for {module_name} to {output_file}")

    def parse_pydantic_models(self) -> dict:
        """
        Reads Pydantic classes from the provided source paths, converts them to JSON format,
        saves them, and returns a dictionary representation of all entities.

        Returns:
            dict: A dictionary containing JSON data of all Pydantic entities.
        """
        # Ensure the export directory exists
        os.makedirs(self.export_dir, exist_ok=True)

        # Process each module and convert entities to JSON
        for path in self.source_paths:
            self.entities_to_single_json(
                module_path=path, export_dir=self.export_dir, logger=self.logger
            )

        # Collect JSON files into a dictionary
        data_model_json = self._load_json_files()

        return data_model_json

    def _load_json_files(self) -> dict:
        """
        Reads all JSON files from the export directory and loads them into a dictionary.

        Returns:
            dict: A dictionary where keys are entity names, and values are the JSON data.
        """
        data_model_json = {}

        for root, _, files in os.walk(self.export_dir):
            for file in files:
                if file.endswith(".json"):
                    file_path = os.path.join(root, file)
                    with open(file_path, encoding="utf-8") as f:
                        try:
                            data_model_json[file] = json.load(f)
                        except json.JSONDecodeError as err:
                            self.logger.error(f"Error loading {file}: {err}")

        return data_model_json
