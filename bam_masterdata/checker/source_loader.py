import glob
import os

from bam_masterdata.excel.excel_to_entities import MasterdataExcelExtractor
from bam_masterdata.logger import logger
from bam_masterdata.metadata.entities_dict import EntitiesDict
from bam_masterdata.utils import convert_enums, format_json_id


class SourceLoader:
    """
    Load the entities from a source written in different formats (Python classes, Excel, etc.) as defined
    in the `source_path` into a dictionary.
    """

    def __init__(self, source_path: str, **kwargs):
        self.source_path = source_path
        self.logger = kwargs.get("logger", logger)
        self.row_cell_info = kwargs.get("row_cell_info", True)
        # Check if the path is a single .py file OR a directory containing .py files
        if self.source_path.endswith(".py") or (
            os.path.isdir(self.source_path)
            and any(glob.glob(os.path.join(self.source_path, "*.py")))
        ):
            self.source_type = "python"
        elif self.source_path.endswith(".xlsx"):
            self.source_type = "excel"
        else:
            self.source_type = None
            self.logger.warning(f"Unsupported source type for path: {source_path}")

    def load(self) -> dict:
        """
        Load entities from the source path into a dictionary.

        Returns:
            dict: A dictionary containing the entities.
        """
        self.logger.info(f"Source type: {self.source_type}")
        if self.source_type == "python":
            return convert_enums(
                EntitiesDict(python_path=self.source_path).single_json()
            )
        elif self.source_type == "excel":
            return self.entities_to_json()
        else:
            raise NotImplementedError(f"Source type {self.source_type} not supported.")

    def entities_to_json(self):
        """
        Transforms the dictionary of entities returned by the Excel extractor into a dictionary in JSON format for later check.

        Returns:
            dict: A dictionary containing the transformed entities.
        """

        excel_entities = MasterdataExcelExtractor(
            excel_path=self.source_path, row_cell_info=self.row_cell_info
        ).excel_to_entities()

        transformed_data = {}

        for entity_type, entities in excel_entities.items():
            transformed_data[entity_type] = {}

            for entity_name, entity_data in entities.items():
                transformed_entity = {
                    "properties": [],  # Now placed before "defs"
                    "defs": {  # Metadata moved to the end
                        "code": entity_data.get("code"),
                        "description": entity_data.get("description", ""),
                        "id": format_json_id(entity_name),  # PascalCase for entity ID
                        "row_location": entity_data.get("row_location"),
                        "validation_script": entity_data.get("validationPlugin")
                        or None,  # Convert "" to None
                        "iri": entity_data.get("iri") or None,  # Convert "" to None
                    },
                }

                # Handle additional fields specific to dataset_types
                if entity_type == "dataset_types":
                    transformed_entity["defs"]["main_dataset_pattern"] = (
                        entity_data.get("main_dataset_pattern")
                    )
                    transformed_entity["defs"]["main_dataset_path"] = entity_data.get(
                        "main_dataset_path"
                    )

                # Handle additional fields specific to object_types
                if entity_type == "object_types":
                    transformed_entity["defs"]["generated_code_prefix"] = (
                        entity_data.get("generatedCodePrefix")
                    )
                    transformed_entity["defs"]["auto_generated_codes"] = (
                        entity_data.get("autoGeneratedCode")
                    )

                # Convert properties from dict to list
                if "properties" in entity_data:
                    for prop_name, prop_data in entity_data["properties"].items():
                        transformed_property = {
                            "code": prop_data.get("code"),
                            "description": prop_data.get("description", ""),
                            "id": format_json_id(
                                prop_name
                            ),  # Now correctly formatted to PascalCase
                            "row_location": prop_data.get("row_location"),
                            "iri": prop_data.get("iri") or None,  # Convert "" to None
                            "property_label": prop_data.get("label"),
                            "data_type": prop_data.get("dataType"),
                            "vocabulary_code": prop_data.get("vocabularyCode")
                            or None,  # Convert "" to None
                            "object_code": None,
                            "metadata": None,
                            "dynamic_script": None,
                            "mandatory": prop_data.get("mandatory", False),
                            "show_in_edit_views": prop_data.get(
                                "show_in_edit_views", False
                            ),
                            "section": prop_data.get("section", ""),
                            "unique": None,
                            "internal_assignment": None,
                        }
                        transformed_entity["properties"].append(transformed_property)

                transformed_data[entity_type][entity_name] = transformed_entity

        return transformed_data

        # # Save the transformed JSON
        # with open(output_json_path, "w", encoding="utf-8") as json_file:
        #     json.dump(transformed_data, json_file, indent=2, ensure_ascii=False)

        # print(f"Transformed JSON saved at: {output_json_path}")
