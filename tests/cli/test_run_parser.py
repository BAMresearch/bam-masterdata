from bam_masterdata.cli.run_parser import run_parser
from bam_masterdata.logger import log_storage
from tests.conftest import (
    TestParser,
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
        "instance of Openbis must be provided" in log["event"] for log in log_storage
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
    )

    # Check that objects were created in openbis
    assert len(mock_openbis._objects) == 1

    # Check logs for success messages
    # logs = log_storage  # log_storage is already a list
    assert any("Added test object" in log["event"] for log in cleared_log_storage)


# TODO add other tests for the different situations in `run_parser()` and parsers from `conftest.py`
