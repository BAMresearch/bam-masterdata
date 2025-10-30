from unittest.mock import MagicMock

from bam_masterdata.cli.run_parser import run_parser
from bam_masterdata.logger import log_storage
from tests.conftest import (
    TestParser,
    TestParserWithObjectReference,
    # TestParserWithExistingCode,
    # TestParserWithRelationship,
)


def test_run_parser_missing_openbis(cleared_log_storage):
    """Test that `run_parser` returns early if openbis is None"""
    run_parser(
        openbis=None,
        space_name="TEST_SPACE",
        project_name="TEST_PROJECT",
        collection_name="TEST_COLLECTION",
        files_parser={},
    )
    assert any(
        "instance of Openbis must be provided" in log["event"]
        for log in cleared_log_storage
    )


def test_run_parser_missing_project_name(cleared_log_storage, mock_openbis):
    """Test that `run_parser` returns early if project_name is empty"""
    run_parser(
        openbis=mock_openbis,
        space_name="TEST_SPACE",
        project_name="",
        collection_name="TEST_COLLECTION",
        files_parser={},
    )
    assert any(
        "Project name must be specified" in log["event"] for log in cleared_log_storage
    )


def test_run_parser_empty_files_parser(cleared_log_storage, mock_openbis):
    """Test that run_parser returns early if files_parser is empty"""
    log_storage.clear()

    run_parser(
        openbis=mock_openbis,
        space_name="TEST_SPACE",
        project_name="TEST_PROJECT",
        collection_name="TEST_COLLECTION",
        files_parser={},  # Empty files_parser
    )

    # Check that an error was logged
    assert any(
        "No files or parsers to parse" in log["event"] for log in cleared_log_storage
    )


def test_run_parser_with_test_parser(cleared_log_storage, mock_openbis):
    """Test run_parser with `TestParser`."""
    file = "./tests/data/cli/test_parser.txt"
    files_parser = {TestParser(): [file]}
    run_parser(
        openbis=mock_openbis,
        space_name="USERNAME_SPACE",
        project_name="TEST_PROJECT",
        collection_name="TEST_COLLECTION",
        files_parser=files_parser,
        collection_type="COLLECTION",
    )

    # Check that objects were created in openbis
    assert len(mock_openbis._objects) == 1

    # Check logs for success messages
    # logs = log_storage  # log_storage is already a list
    assert any("Added test object" in log["event"] for log in cleared_log_storage)


def test_run_parser_with_object_reference(cleared_log_storage, mock_openbis):
    """Test run_parser with OBJECT property references."""

    # Mock the get_object method to return a mock object for path references
    def get_object_mock(path):
        # Validate that the path follows OpenBIS identifier format
        if not path.startswith("/"):
            raise ValueError(f"Invalid path format: must start with '/', got '{path}'")
        parts = path.strip("/").split("/")
        if len(parts) not in [3, 4]:
            raise ValueError(
                f"Invalid path format: must have 3 or 4 parts, got {len(parts)}"
            )

        mock_obj = MagicMock()
        mock_obj.identifier = path
        return mock_obj

    mock_openbis.get_object = get_object_mock

    file = "./tests/data/cli/test_parser.txt"
    files_parser = {TestParserWithObjectReference(): [file]}
    run_parser(
        openbis=mock_openbis,
        space_name="TEST_SPACE",
        project_name="TEST_PROJECT",
        collection_name="TEST_COLLECTION",
        files_parser=files_parser,
        collection_type="COLLECTION",
    )

    # Only 2 instruments are created (the person is referenced but not persisted)
    assert len(mock_openbis._objects) == 2

    # Check logs for success messages
    assert any("Added person object" in log["event"] for log in cleared_log_storage)
    assert any(
        "Added instrument1 with object reference" in log["event"]
        for log in cleared_log_storage
    )
    assert any(
        "Added instrument2 with path reference" in log["event"]
        for log in cleared_log_storage
    )


def test_run_parser_with_default_experiment_type(cleared_log_storage, mock_openbis):
    """Test run_parser with DEFAULT_EXPERIMENT collection type."""
    file = "./tests/data/cli/test_parser.txt"
    files_parser = {TestParser(): [file]}
    run_parser(
        openbis=mock_openbis,
        space_name="USERNAME_SPACE",
        project_name="TEST_PROJECT",
        collection_name="TEST_COLLECTION",
        files_parser=files_parser,
        collection_type="DEFAULT_EXPERIMENT",
    )

    # Check that objects were created in openbis
    assert len(mock_openbis._objects) == 1

    # Check logs for success messages
    assert any("Added test object" in log["event"] for log in cleared_log_storage)


def test_run_parser_defaults_to_collection_type(cleared_log_storage, mock_openbis):
    """Test that run_parser defaults to COLLECTION type when not specified."""
    file = "./tests/data/cli/test_parser.txt"
    files_parser = {TestParser(): [file]}
    # Call without specifying collection_type - should default to "COLLECTION"
    run_parser(
        openbis=mock_openbis,
        space_name="USERNAME_SPACE",
        project_name="TEST_PROJECT",
        collection_name="TEST_COLLECTION",
        files_parser=files_parser,
    )

    # Check that objects were created in openbis
    assert len(mock_openbis._objects) == 1

    # Check logs for success messages
    assert any("Added test object" in log["event"] for log in cleared_log_storage)


# TODO add other tests for the different situations in `run_parser()` and parsers from `conftest.py`
