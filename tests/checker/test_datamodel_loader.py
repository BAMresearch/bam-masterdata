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


@pytest.mark.parametrize(
    "log_message, log_message_level",
    [
        ("Saved", "info"),
    ],
)
def test_entities_to_single_dict(
    cleared_log_storage,
    log_message,
    log_message_level,
):
    """Test that entities are correctly extracted and aggregated into a dictionary using real test files."""

    # Call function
    test_data_dir = os.path.abspath(os.path.join("tests", "checker", "datamodel"))
    result = DataModelLoader(test_data_dir).data

    # Define the path to the expected JSON file
    expected_json_file = os.path.abspath(
        os.path.join(
            "tests", "checker", "data", "expected_output_datamodel_loader.json"
        )
    )

    # Load the expected output dictionary from the JSON file
    with open(expected_json_file) as f:
        expected_output = json.load(f)

    # Assertions
    assert result == expected_output, "Extracted data does not match expected output."

    # Check if the expected log message appears anywhere in logs
    assert any(
        log_message in log["event"] and log["level"] == log_message_level
        for log in cleared_log_storage
    ), (
        f"Expected log containing '{log_message}' with level '{log_message_level}' not found in logs: {cleared_log_storage}"
    )
