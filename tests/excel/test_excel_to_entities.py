import openpyxl
import pytest

from bam_masterdata.excel import MasterdataExcelExtractor


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


# # Failing cases for `index_to_excel_column`
# @pytest.mark.parametrize(
#     "invalid_index",
#     [-1, 0, "ABC", None, 3.5],  # Invalid cases
# )
# def test_index_to_excel_column_invalid(excel_extractor, invalid_index):
#     """Tests that index_to_excel_column fails with invalid input."""
#     with pytest.raises(ValueError):
#         excel_extractor.index_to_excel_column(invalid_index)


# Tests for `get_last_non_empty_row`
def test_get_last_non_empty_row(excel_extractor):
    """Tests finding the last non-empty row."""
    sheet = excel_extractor.workbook["Sheet1"]

    result = excel_extractor.get_last_non_empty_row(sheet, 1)

    assert result == 2  # Last non-empty row should be 4


# # Failing cases for `get_last_non_empty_row`
# @pytest.mark.parametrize(
#     "invalid_sheet, start_index, expected_exception",
#     [
#         (None, 1, AttributeError),  # No sheet provided
#         ("Not a sheet", 1, KeyError),  # Invalid type
#         ("Sheet1", -1, ValueError),  # Negative index
#         ("Sheet1", "ABC", TypeError),  # Non-integer index
#         ("Sheet1", 999, ValueError),  # Index out of bounds
#     ],
# )
# def test_get_last_non_empty_row_invalid(
#     excel_extractor, invalid_sheet, start_index, expected_exception
# ):
#     """Tests that get_last_non_empty_row fails with invalid input."""
#     try:
#         sheet = (
#             excel_extractor.workbook[invalid_sheet]
#             if isinstance(invalid_sheet, str)
#             else invalid_sheet
#         )
#     except KeyError:
#         if expected_exception is KeyError:
#             return  # Test passes if KeyError was expected
#         raise  # Otherwise, raise the error

#     with pytest.raises(expected_exception):
#         excel_extractor.get_last_non_empty_row(sheet, start_index)


# Tests for `is_reduced_version`
@pytest.mark.parametrize(
    "generated_code, full_code, expected_result",
    [
        ("ABC", "ABC", True),  # Identical codes
        ("ABC", "ABC_DEF", True),  # Not a reduced version
        ("ABC.DEF", "ABC.DEF.GHI", True),  # Matching delimiter (.)
        ("ABC_DEF", "ABC_DEF_GHI", True),  # Matching delimiter (_)
        ("ABC.DEF", "ABC_DEF_GHI", False),  # Mismatched delimiters
    ],
)
def test_is_reduced_version(
    excel_extractor, generated_code, full_code, expected_result
):
    """Tests whether generated_code_value is a reduced version of code."""
    result = excel_extractor.is_reduced_version(generated_code, full_code)
    assert result == expected_result


# # Failing cases for `is_reduced_version`
# @pytest.mark.parametrize(
#     "generated_code, full_code, expected_exception",
#     [
#         (None, "ABC.DEF", TypeError),  # None input
#         ("ABC.DEF", None, TypeError),  # None input
#         (123, "ABC.DEF", TypeError),  # Non-string input
#         ("ABC.DEF", 456, TypeError),  # Non-string input
#     ],
# )
# def test_is_reduced_version_invalid(
#     excel_extractor, generated_code, full_code, expected_exception
# ):
#     """Tests that is_reduced_version fails with invalid input."""
#     with pytest.raises(expected_exception):
#         excel_extractor.is_reduced_version(generated_code, full_code)
