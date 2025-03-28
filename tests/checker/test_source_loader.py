from unittest.mock import patch

import pytest

from bam_masterdata.checker.source_loader import SourceLoader
from bam_masterdata.logger import logger


def remove_row_location(data):  # Not present in Python so just one dict is needed
    """
    Recursively removes all 'row_location' fields from a nested dictionary.

    Args:
        data (dict): The original dictionary.

    Returns:
        dict: The dictionary without 'row_location' fields.
    """
    if isinstance(data, dict):
        return {
            k: remove_row_location(v) for k, v in data.items() if k != "row_location"
        }
    elif isinstance(data, list):
        return [remove_row_location(item) for item in data]
    else:
        return data


@pytest.fixture
def expected_transformed_data():
    """Expected JSON structure after transformation."""
    return {
        "collection_types": {
            "COLLECTION": {
                "properties": [
                    {
                        "code": "$NAME",
                        "description": "Name",
                        "iri": None,
                        "id": "Name",
                        "property_label": "Name",
                        "data_type": "VARCHAR",
                        "vocabulary_code": None,
                        "object_code": None,
                        "metadata": None,
                        "dynamic_script": None,
                        "mandatory": False,
                        "show_in_edit_views": False,
                        "section": "General info",
                        "unique": None,
                        "internal_assignment": None,
                    }
                ],
                "defs": {
                    "code": "COLLECTION",
                    "description": "",
                    "iri": None,
                    "id": "Collection",
                    "validation_script": None,
                },
            },
            "DEFAULT_EXPERIMENT": {
                "properties": [
                    {
                        "code": "DEFAULT_EXPERIMENT.EXPERIMENTAL_DESCRIPTION",
                        "description": "Description of the experiment",
                        "iri": None,
                        "id": "DefaultExperimentExperimentalDescription",
                        "property_label": "Description",
                        "data_type": "MULTILINE_VARCHAR",
                        "vocabulary_code": None,
                        "object_code": None,
                        "metadata": None,
                        "dynamic_script": None,
                        "mandatory": False,
                        "show_in_edit_views": False,
                        "section": "Experimental details",
                        "unique": None,
                        "internal_assignment": None,
                    }
                ],
                "defs": {
                    "code": "DEFAULT_EXPERIMENT",
                    "description": "",
                    "iri": None,
                    "id": "DefaultExperiment",
                    "validation_script": "DEFAULT_EXPERIMENT.date_range_validation",
                },
            },
        },
        "dataset_types": {
            "ANALYSIS_NOTEBOOK": {
                "properties": [
                    {
                        "code": "$HISTORY_ID",
                        "description": "History ID",
                        "iri": None,
                        "id": "HistoryId",
                        "property_label": "History ID",
                        "data_type": "VARCHAR",
                        "vocabulary_code": None,
                        "object_code": None,
                        "metadata": None,
                        "dynamic_script": None,
                        "mandatory": False,
                        "show_in_edit_views": False,
                        "section": "",
                        "unique": None,
                        "internal_assignment": None,
                    }
                ],
                "defs": {
                    "code": "ANALYSIS_NOTEBOOK",
                    "description": "",
                    "iri": None,
                    "id": "AnalysisNotebook",
                    "validation_script": None,
                    "main_dataset_pattern": None,
                    "main_dataset_path": None,
                },
            },
            "ANALYZED_DATA": {
                "properties": [
                    {
                        "code": "NOTES",
                        "description": "Notes//Notizen",
                        "iri": None,
                        "id": "Notes",
                        "property_label": "Notes",
                        "data_type": "MULTILINE_VARCHAR",
                        "vocabulary_code": None,
                        "object_code": None,
                        "metadata": None,
                        "dynamic_script": None,
                        "mandatory": False,
                        "show_in_edit_views": False,
                        "section": "Comments",
                        "unique": None,
                        "internal_assignment": None,
                    }
                ],
                "defs": {
                    "code": "ANALYZED_DATA",
                    "description": "",
                    "iri": None,
                    "id": "AnalyzedData",
                    "validation_script": None,
                    "main_dataset_pattern": None,
                    "main_dataset_path": None,
                },
            },
        },
        "object_types": {
            "ACTION": {
                "properties": [
                    {
                        "code": "ACTING_PERSON",
                        "description": "Acting Person//Handelnde Person",
                        "iri": None,
                        "id": "ActingPerson",
                        "property_label": "Acting Person",
                        "data_type": "OBJECT",
                        "vocabulary_code": None,
                        "object_code": None,
                        "metadata": None,
                        "dynamic_script": None,
                        "mandatory": False,
                        "show_in_edit_views": False,
                        "section": "Action Data",
                        "unique": None,
                        "internal_assignment": None,
                    }
                ],
                "defs": {
                    "code": "ACTION",
                    "description": "This Object allows to store information on an action by a user.//Dieses Objekt erlaubt eine Nutzer-Aktion zu beschreiben.",
                    "iri": None,
                    "id": "Action",
                    "validation_script": None,
                    "generated_code_prefix": "ACT",
                    "auto_generated_codes": True,
                },
            }
        },
    }


@pytest.mark.parametrize(
    "source_path, expected_source_type",
    [
        ("tests/data/checker/example_incoming_excel.xlsx", "excel"),
        ("tests/data/checker/example_incoming_python/", "python"),
    ],
)
def test_source_loader_initialization(source_path, expected_source_type):
    """Test if SourceLoader correctly identifies the source type."""
    loader = SourceLoader(source_path, logger=logger)
    assert loader.source_type == expected_source_type


def test_entities_to_json(expected_transformed_data):
    """Test if the transformed JSON from an Excel file matches the expected output."""
    source_loader = SourceLoader("tests/data/checker/example_incoming_excel.xlsx")
    result_dict = source_loader.entities_to_json()

    assert remove_row_location(result_dict) == expected_transformed_data


def test_source_loader_load_excel(expected_transformed_data):
    """Test if the SourceLoader correctly loads an Excel file and returns the expected JSON structure."""
    with patch("bam_masterdata.logger.logger.info") as mock_logger:
        source_loader = SourceLoader("tests/data/checker/example_incoming_excel.xlsx")
        result_dict = source_loader.load()

        assert remove_row_location(result_dict) == expected_transformed_data

        # Extract all logged messages
        log_messages = [call.args[0] for call in mock_logger.call_args_list]

        # Ensure both messages are present
        assert "Source type: excel" in log_messages
        assert "Validation rules successfully loaded." in log_messages


def test_source_loader_load_python(expected_transformed_data):
    """Test if the SourceLoader correctly loads a Python file and returns the expected JSON structure."""
    with patch("bam_masterdata.logger.logger.info") as mock_logger:
        source_loader = SourceLoader("tests/data/checker/example_incoming_python/")
        result_dict = source_loader.load()

        assert remove_row_location(result_dict) == expected_transformed_data
        mock_logger.assert_called_with("Source type: python")


def test_unsupported_source_type():
    """Test if SourceLoader logs a warning for unsupported source types."""
    with patch("bam_masterdata.logger.logger.warning") as mock_logger:
        loader = SourceLoader("tests/data/checker/example_incoming_unsupported.txt")
        assert loader.source_type is None
        mock_logger.assert_called_with(
            "Unsupported source type for path: tests/data/checker/example_incoming_unsupported.txt"
        )


def test_unsupported_source_type_load():
    """Test if the load() function raises NotImplementedError for unsupported types and logs an error."""
    source_loader = SourceLoader("tests/data/checker/example_incoming_unsupported.txt")

    with (
        pytest.raises(NotImplementedError) as exc_info,
        patch("bam_masterdata.logger.logger.info") as mock_logger,
    ):
        source_loader.load()

    assert "Source type None not supported" in str(exc_info.value)
    mock_logger.assert_called_with("Source type: None")
