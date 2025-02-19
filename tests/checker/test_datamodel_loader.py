import json
import logging
import os
from unittest.mock import MagicMock

import pytest

from bam_masterdata.checker.datamodel_loader import DataModelLoader
from bam_masterdata.logger import logger


@pytest.fixture
def mock_logger():
    """Fixture to create a mock logger."""
    return MagicMock(spec=logging.Logger)


@pytest.fixture
def sample_module_paths():
    """Fixture providing the actual test module paths."""
    test_data_dir = os.path.abspath(os.path.join("tests", "checker", "datamodel"))

    return [
        os.path.join(test_data_dir, "collection_types.py"),
        os.path.join(test_data_dir, "object_types.py"),
        os.path.join(test_data_dir, "__init__.py"),  # Should be skipped
    ]


@pytest.mark.parametrize(
    "log_message, log_message_level",
    [
        ("__init__.py", "info"),
        ("Saved", "info"),
    ],
)
def test_entities_to_single_dict(
    cleared_log_storage,
    mock_logger,
    sample_module_paths,
    log_message,
    log_message_level,
):
    """Test that entities are correctly extracted and aggregated into a dictionary using real test files."""

    # Call function
    result = DataModelLoader.entities_to_single_dict(sample_module_paths)

    # Expected output dictionary
    expected_output = {
        "collection_types": {
            "COLLECTION": {
                "properties": [
                    {
                        "code": "$DEFAULT_OBJECT_TYPE",
                        "description": "Enter the code of the object type for which the collection is used",
                        "id": "DefaultObjectType",
                        "property_label": "Default object type",
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
                    },
                    {
                        "code": "$NAME",
                        "description": "Name",
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
                    },
                ],
                "defs": {
                    "code": "COLLECTION",
                    "description": "",
                    "id": "Collection",
                    "validation_script": None,
                },
            },
            "DEFAULT_EXPERIMENT": {
                "properties": [
                    {
                        "code": "DEFAULT_EXPERIMENT.EXPERIMENTAL_DESCRIPTION",
                        "description": "Description of the experiment",
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
                    },
                    {
                        "code": "DEFAULT_EXPERIMENT.EXPERIMENTAL_GOALS",
                        "description": "Goals of the experiment",
                        "id": "DefaultExperimentExperimentalGoals",
                        "property_label": "Goals",
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
                    },
                ],
                "defs": {
                    "code": "DEFAULT_EXPERIMENT",
                    "description": "",
                    "id": "DefaultExperiment",
                    "validation_script": "DEFAULT_EXPERIMENT.date_range_validation",
                },
            },
        },
        "object_types": {
            "ACTION": {
                "properties": [
                    {
                        "code": "$NAME",
                        "description": "Name",
                        "id": "Name",
                        "property_label": "Name",
                        "data_type": "MULTILINE_VARCHAR",
                        "vocabulary_code": None,
                        "object_code": None,
                        "metadata": None,
                        "dynamic_script": None,
                        "mandatory": False,
                        "show_in_edit_views": False,
                        "section": "Device ID",
                        "unique": None,
                        "internal_assignment": None,
                    },
                    {
                        "code": "$XMLCOMMENTS",
                        "description": "Comments log",
                        "id": "Xmlcomments",
                        "property_label": "Comments",
                        "data_type": "HYPERLINK",
                        "vocabulary_code": None,
                        "object_code": None,
                        "metadata": None,
                        "dynamic_script": None,
                        "mandatory": False,
                        "show_in_edit_views": False,
                        "section": "Additional Information",
                        "unique": None,
                        "internal_assignment": None,
                    },
                ],
                "defs": {
                    "code": "ACTION",
                    "description": "This Object allows to store information on an action by a user.//Dieses Objekt erlaubt eine Nutzer-Aktion zu beschreiben.",
                    "id": "Action",
                    "validation_script": None,
                    "generated_code_prefix": "ACT",
                    "auto_generated_codes": True,
                },
            },
            "AUXILIARY_MATERIAL": {
                "properties": [
                    {
                        "code": "ALIAS",
                        "description": "e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname",
                        "id": "Alias",
                        "property_label": "Alternative Name",
                        "data_type": "INTEGER",
                        "vocabulary_code": None,
                        "object_code": None,
                        "metadata": None,
                        "dynamic_script": None,
                        "mandatory": False,
                        "show_in_edit_views": False,
                        "section": "General Information",
                        "unique": None,
                        "internal_assignment": None,
                    },
                    {
                        "code": "$ANNOTATIONS_STATE",
                        "description": "Annotations State",
                        "id": "AnnotationsState",
                        "property_label": "Annotations State",
                        "data_type": "REAL",
                        "vocabulary_code": None,
                        "object_code": None,
                        "metadata": None,
                        "dynamic_script": None,
                        "mandatory": False,
                        "show_in_edit_views": False,
                        "section": "Comments",
                        "unique": None,
                        "internal_assignment": None,
                    },
                ],
                "defs": {
                    "code": "AUXILIARY_MATERIAL",
                    "description": "Auxiliary Material//Hilfsstoff",
                    "id": "AuxiliaryMaterial",
                    "validation_script": None,
                    "generated_code_prefix": "AUX_MAT",
                    "auto_generated_codes": True,
                },
            },
        },
    }

    # Assertions
    assert result == expected_output, "Extracted data does not match expected output."

    # Check if the expected log message appears anywhere in logs
    assert any(
        log_message in log["event"] and log["level"] == log_message_level
        for log in cleared_log_storage
    ), (
        f"Expected log containing '{log_message}' with level '{log_message_level}' not found in logs: {cleared_log_storage}"
    )
