import re

import openpyxl
import pytest

from bam_masterdata.excel import MasterdataExcelExtractor
from bam_masterdata.logger import logger
from bam_masterdata.metadata.definitions import DataType


@pytest.fixture
def excel_extractor(tmp_path):
    """Fixture to create an instance of MasterdataExcelExtractor with a dummy Excel file."""
    # Create a dummy Excel file in the temporary test directory
    dummy_excel = tmp_path / "test.xlsx"
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    # Add some dummy data
    ws.append(["Header1", "Header2", "Header3"])
    ws.append(["Data1", "Data2", "Data3"])
    ws.append(["", "", ""])  # Empty row
    ws.append(["Last", "Row", "Data"])

    wb.save(dummy_excel)

    # Create an instance with the dummy file
    return MasterdataExcelExtractor(excel_path=str(dummy_excel))


# Tests for `index_to_excel_column`
@pytest.mark.parametrize(
    "index, expected_column",
    [
        (1, "A"),
        (2, "B"),
        (26, "Z"),
        (27, "AA"),
        (28, "AB"),
        (52, "AZ"),
        (53, "BA"),
        (702, "ZZ"),
        (703, "AAA"),
        (704, "AAB"),
        (1378, "AZZ"),
        (1379, "BAA"),
        (18278, "ZZZ"),
        (18279, "AAAA"),
        (18280, "AAAB"),
    ],
)
def test_index_to_excel_column(excel_extractor, index, expected_column):
    """Tests the index_to_excel_column method."""
    result = excel_extractor.index_to_excel_column(index)
    assert result == expected_column


# Failing cases for `index_to_excel_column`
@pytest.mark.parametrize(
    "invalid_index",
    [-1, 0],  # Invalid cases
)
def test_index_to_excel_column_invalid(excel_extractor, invalid_index):
    """Tests that index_to_excel_column fails with invalid input."""
    with pytest.raises(ValueError):
        excel_extractor.index_to_excel_column(invalid_index)


# Tests for `get_last_non_empty_row`
def test_get_last_non_empty_row(excel_extractor):
    """Tests finding the last non-empty row."""
    sheet = excel_extractor.workbook["Sheet1"]

    result = excel_extractor.get_last_non_empty_row(sheet, 1)

    assert result == 2  # Last non-empty row should be 4


# Failing cases for `get_last_non_empty_row`
@pytest.mark.parametrize(
    "invalid_sheet, start_index, expected_exception",
    [
        (None, 1, AttributeError),  # No sheet provided
        ("Sheet1", -1, ValueError),  # Negative index
        ("Sheet1", 999, ValueError),  # Index out of bounds
    ],
)
def test_get_last_non_empty_row_invalid(
    excel_extractor, invalid_sheet, start_index, expected_exception
):
    """Tests that get_last_non_empty_row fails with invalid input."""
    try:
        sheet = (
            excel_extractor.workbook[invalid_sheet]
            if isinstance(invalid_sheet, str)
            else invalid_sheet
        )
    except KeyError:
        if expected_exception is KeyError:
            return  # Test passes if KeyError was expected
        raise  # Otherwise, raise the error

    with pytest.raises(expected_exception):
        excel_extractor.get_last_non_empty_row(sheet, start_index)


# Tests for `is_reduced_version`
@pytest.mark.parametrize(
    "generated_code, full_code, expected_result",
    [
        ("ABC", "ABC", True),  # Identical codes
        ("ABC", "ABC_DEF", True),  # Not a reduced version
        ("ABC.DEF", "ABC.DEF.GHI", True),  # Matching delimiter (.)
        ("ABC_DEF", "ABC_DEF_GHI", True),  # Matching delimiter (_)
        ("ABC.DEF", "ABC_DEF_GHI", False),  # Mismatched delimiters
        ("", "AAA", False),  # Not a reduced version, but function returns True
        ("INS_ANS", "INSTRUMENT", False),  # Contains INS, but no reduced version
        ("ABC.DEF", "ABC_DEF", False),  # Error: the symbol is not the same
        ("ABC_DEF", "ABC.DEF.GHI", False),  # Matching delimiter (_)
        ("ABC.DEF.GHI", "ABC.DEF", False),  # Longer than original code
    ],
)
def test_is_reduced_version(
    excel_extractor, generated_code, full_code, expected_result
):
    """Tests whether generated_code_value is a reduced version of code."""
    result = excel_extractor.is_reduced_version(generated_code, full_code)
    assert result == expected_result


@pytest.mark.parametrize(
    "value, expected_result, log_message, log_message_level",
    [
        ("true", True, None, None),
        ("false", False, None, None),
        (True, True, None, None),
        (False, False, None, None),
        ("TrUe", True, None, None),
        ("FaLsE", False, None, None),
        ("", False, None, None),
        (None, False, None, None),
        (
            "yes",
            False,
            "Invalid boolean term value found in the Boolean Term column at position A1 in Sheet1. Accepted values: TRUE or FALSE.",
            "error",
        ),
        (
            "123",
            False,
            "Invalid boolean term value found in the Boolean Term column at position A1 in Sheet1. Accepted values: TRUE or FALSE.",
            "error",
        ),
    ],
)
def test_str_to_bool(
    cleared_log_storage,
    excel_extractor,
    value,
    expected_result,
    log_message,
    log_message_level,
):
    """Tests conversion of string values to boolean with `str_to_bool`."""
    result = excel_extractor.str_to_bool(value, "Boolean Term", "A1", "Sheet1")
    assert result == expected_result

    if log_message:
        # Check if the expected error message appears in logs
        assert any(
            log["event"] == log_message and log["level"] == log_message_level
            for log in cleared_log_storage
        )
    else:
        # Ensure no error messages are logged
        assert not any(log["level"] == "error" for log in cleared_log_storage)


@pytest.mark.parametrize(
    "value, term, coordinate, sheet_title, is_description, is_code, is_data, is_url, expected_result, log_message, log_message_level",
    [
        # Valid cases (No errors should be logged)
        (
            "Valid Code",
            "Code",
            "A1",
            "Sheet1",
            False,
            False,
            False,
            False,
            "Valid Code",
            None,
            None,
        ),
        (
            "Valid Description // Gültige Beschreibung",
            "Description",
            "A1",
            "Sheet1",
            True,
            False,
            False,
            False,
            "Valid Description // Gültige Beschreibung",
            None,
            None,
        ),
        (
            "VALID_CODE",
            "Code",
            "B2",
            "Sheet2",
            False,
            True,
            False,
            False,
            "VALID_CODE",
            None,
            None,
        ),
        (
            "INTEGER",
            "Data Type",
            "C3",
            "Sheet3",
            False,
            False,
            True,
            False,
            "INTEGER",
            None,
            None,
        ),
        (
            "https://valid-url.com",
            "URL",
            "D4",
            "Sheet4",
            False,
            False,
            False,
            True,
            "https://valid-url.com",
            None,
            None,
        ),
        # Invalid cases (Errors should be logged)
        (
            "Missing Separator",
            "Description",
            "A5",
            "Sheet5",
            True,
            False,
            False,
            False,
            "Missing Separator",
            "Invalid description value found in the Description column at position A5 in Sheet5. "
            "Description should follow the schema: English Description + '//' + German Description. ",
            "error",
        ),
        (
            "Invalid Code!",
            "Code",
            "B6",
            "Sheet6",
            False,
            True,
            False,
            False,
            "Invalid Code!",
            "Invalid code value found in the Code column at position B6 in Sheet6.",
            "error",
        ),
        (
            "unknown_data_type",
            "Data Type",
            "C7",
            "Sheet7",
            False,
            False,
            True,
            False,
            "UNKNOWN_DATA_TYPE",
            f"Invalid data type value found in the Data Type column at position C7 in Sheet7. "
            f"The Data Type should be one of the following: {list(dt.value for dt in DataType)}",
            "error",
        ),
        (
            "invalid-url",
            "URL",
            "D8",
            "Sheet8",
            False,
            False,
            False,
            True,
            "invalid-url",
            "Invalid url value found in the URL column at position D8 in Sheet8.",
            "error",
        ),
    ],
)
def test_get_and_check_property(
    cleared_log_storage,
    excel_extractor,
    value,
    term,
    coordinate,
    sheet_title,
    is_description,
    is_code,
    is_data,
    is_url,
    expected_result,
    log_message,
    log_message_level,
):
    """Tests property validation and formatting with `get_and_check_property`."""
    result = excel_extractor.get_and_check_property(
        value, term, coordinate, sheet_title, is_description, is_code, is_data, is_url
    )
    assert result == expected_result

    if log_message:
        # Normalize log message formatting to avoid strict mismatches
        def normalize_log_message(msg):
            return re.sub(r"\s+", " ", msg.replace(". ", ".")).strip()

        cleaned_logs = [
            normalize_log_message(log["event"]) for log in cleared_log_storage
        ]
        expected_cleaned_message = normalize_log_message(log_message)

        # Print debug information for failed tests
        print("\n--- DEBUG LOG CHECK ---")
        print(f"Expected Log Message:\n{expected_cleaned_message}")
        print("\nCaptured Log Messages:")
        for log in cleaned_logs:
            print(f"- {log}")

        # Print raw cleared_log_storage to check log structure
        print("\n--- RAW LOG STORAGE ---")
        for log in cleared_log_storage:
            print(log)

        # Generalized check (avoids strict spacing mismatches)
        assert any(expected_cleaned_message in log for log in cleaned_logs)
    else:
        # Ensure no error messages are logged
        assert not any(log["level"] == "error" for log in cleared_log_storage)
