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

    def parse_pydantic_models(self) -> dict:
        """
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
