import inspect
import json
import os
import shutil
from pathlib import Path

import pytest

from bam_masterdata.logger import logger
from bam_masterdata.utils import (
    code_to_class_name,
    delete_and_create_dir,
    duplicated_property_types,
    import_module,
    is_reduced_version,
    listdir_py_modules,
    load_validation_rules,
)


@pytest.mark.parametrize(
    "directory_path, force_delete, dir_exists",
    [
        # `directory_path` is empty
        ("", True, False),
        # `directory_path` exists but `force_delete` is False
        ("tests/data/tmp/", False, True),
        # `directory_path` does not exist and it is created
        ("tests/data/tmp/", True, True),
    ],
)
def test_delete_and_create_dir(
    cleared_log_storage: list, directory_path: str, force_delete: bool, dir_exists: bool
):
    """Tests the `delete_and_delete_dir` function."""
    delete_and_create_dir(
        directory_path=directory_path,
        logger=logger,
        force_delete=force_delete,
    )
    assert dir_exists == os.path.exists(directory_path)
    if not force_delete:
        assert cleared_log_storage[0]["level"] == "info"
        assert (
            cleared_log_storage[0]["event"]
            == f"Skipping the deletion of the directory at {directory_path}."
        )
    if dir_exists:
        shutil.rmtree(directory_path)  # ! careful with this line
    else:
        assert len(cleared_log_storage) == 1
        assert cleared_log_storage[0]["level"] == "warning"
        assert "directory_path" in cleared_log_storage[0]["event"]


@pytest.mark.parametrize(
    "directory_path, listdir, log_message, log_message_level",
    [
        # `directory_path` is empty
        (
            "",
            [],
            "The `directory_path` is empty. Please, provide a proper input to the function.",
            "warning",
        ),
        # No Python files found in the directory
        (
            "./tests/data/empty",
            [],
            "No Python files found in the directory.",
            "info",
        ),
        # Python files found in the directory
        (
            "./tests/utils",
            [
                "./tests/utils/test_paths.py",
                "./tests/utils/test_utils.py",
            ],
            None,
            None,
        ),
    ],
)
def test_listdir_py_modules(
    cleared_log_storage: list,
    directory_path: str,
    listdir: list[str],
    log_message: str,
    log_message_level: str,
):
    """Tests the `listdir_py_modules` function."""
    result = listdir_py_modules(directory_path=directory_path, logger=logger)
    if not listdir:
        assert cleared_log_storage[0]["event"] == log_message
        assert cleared_log_storage[0]["level"] == log_message_level
    # when testing locally and with Github actions the order of the files is different --> `result` is sorted, so we also sort `listdir`
    # Normalize paths to avoid Windows/Linux differences
    result_normalized = [str(Path(p).resolve()) for p in result]
    expected_normalized = [str(Path(p).resolve()) for p in sorted(listdir)]

    assert result_normalized == expected_normalized


@pytest.mark.skip(
    reason="Very annoying to test this function, as any module we can use to be tested will change a lot in the future."
)
def test_import_module():
    """Tests the `import_module` function."""
    # testing only the possitive results
    module = import_module("./bam_data_store/utils/utils.py")
    assert [f[0] for f in inspect.getmembers(module, inspect.ismodule)] == [
        "glob",
        "importlib",
        "os",
        "shutil",
        "sys",
    ]
    assert [f[0] for f in inspect.getmembers(module, inspect.isclass)] == []
    assert [f[0] for f in inspect.getmembers(module, inspect.isfunction)] == [
        "delete_and_create_dir",
        "import_module",
        "listdir_py_modules",
    ]


@pytest.mark.parametrize(
    "code, entity_type, result",
    [
        # No code
        (None, "object", ""),
        ("", "object", ""),
        # for entities which are objects
        # normal code
        ("NORMAL", "object", "Normal"),
        # code starting with '$'
        ("$NATIVE", "object", "Native"),
        # code separated by underscores
        ("SEPARATED_BY_UNDERSCORES", "object", "SeparatedByUnderscores"),
        # code starting with '$' and separated by underscores
        ("$NATIVE_SEPARATED_BY_UNDERSCORES", "object", "NativeSeparatedByUnderscores"),
        # code with a dot for inheritance
        ("POINT.INHERITANCE", "object", "Inheritance"),
        # code starting with '$' and with a dot for inheritance
        ("$POINT.INHERITANCE", "object", "Inheritance"),
        # code starting with '$' and with a dot for inheritance and separated by underscores
        ("$POINT.INHERITANCE_SEPARATED", "object", "InheritanceSeparated"),
        # for entities which are properties
        # normal code
        ("NORMAL", "property", "Normal"),
        # code starting with '$'
        ("$NATIVE", "property", "Native"),
        # code separated by underscores
        ("SEPARATED_BY_UNDERSCORES", "property", "SeparatedByUnderscores"),
        # code starting with '$' and separated by underscores
        (
            "$NATIVE_SEPARATED_BY_UNDERSCORES",
            "property",
            "NativeSeparatedByUnderscores",
        ),
        # code with a dot for inheritance
        ("POINT.INHERITANCE", "property", "PointInheritance"),
        # code starting with '$' and with a dot for inheritance
        ("$POINT.INHERITANCE", "property", "PointInheritance"),
        # code starting with '$' and with a dot for inheritance and separated by underscores
        ("$POINT.INHERITANCE_SEPARATED", "property", "PointInheritanceSeparated"),
    ],
)
def test_code_to_class_name(code: str, entity_type: str, result: str):
    assert code_to_class_name(code, logger, entity_type) == result


@pytest.mark.parametrize(
    "file_path, file_content, expected_output, expected_log, expected_exception",
    [
        # Valid JSON file with real validation rules
        (
            "tests/data/valid_rules.json",
            json.dumps(
                VALID_RULES := {
                    "SAMPLE_TYPE": {
                        "Code": {"key": "code", "pattern": "^\\$?[A-Za-z0-9_.]+$"},
                        "Description": {
                            "key": "description",
                            "pattern": ".*",
                            "is_description": True,
                        },
                        "Validation script": {
                            "key": "validationPlugin",
                            "pattern": "^[A-Za-z0-9_]+\\.py$",
                            "allow_empty": True,
                        },
                    },
                    "OBJECT_TYPE": {
                        "Code": {"key": "code", "pattern": "^\\$?[A-Za-z0-9_.]+$"},
                        "Description": {
                            "key": "description",
                            "pattern": ".*",
                            "is_description": True,
                        },
                    },
                }
            ),  # JSON content as a string
            VALID_RULES,  # Expected output as a dictionary
            "Validation rules successfully loaded.",
            None,  # No exception
        ),
        # File path is None (should fallback to default path)
        (
            None,
            json.dumps(
                PROPERTY_RULES := {
                    "PROPERTY_TYPE": {
                        "Code": {"key": "code", "pattern": "^\\$?[A-Za-z0-9_.]+$"},
                        "Property label": {"key": "label", "pattern": ".*"},
                        "Data type": {
                            "key": "dataType",
                            "pattern": None,
                            "is_data": True,
                        },
                    }
                }
            ),
            PROPERTY_RULES,
            "Validation rules successfully loaded.",
            None,
        ),
        # File does not exist
        (
            "tests/data/missing.json",
            None,  # File does not exist
            None,
            "Validation rules file not found: tests/data/missing.json",
            FileNotFoundError,
        ),
        # Invalid JSON format (truncated JSON)
        (
            "tests/data/invalid.json",
            '{"SAMPLE_TYPE": {"Code": {"key": "code", "pattern": "^\\$?[A-Za-z0-9_.]+$"}',  # Incomplete JSON
            None,
            "Error parsing validation rules JSON:",
            ValueError,
        ),
        # File contains unexpected structure (empty dictionary)
        (
            "tests/data/empty.json",
            "{}",
            {},
            "Validation rules successfully loaded.",
            None,
        ),
    ],
)
def test_load_validation_rules(
    tmp_path,
    cleared_log_storage,
    file_path,
    file_content,
    expected_output,
    expected_log,
    expected_exception,
):
    """Tests the `load_validation_rules` function with realistic validation rules."""

    # If the file_content is provided, create a temporary JSON file
    if file_content:
        test_file = tmp_path / "test_rules.json"
        test_file.write_text(file_content, encoding="utf-8")
        file_path = str(test_file)

    # Run the function and check results
    if expected_exception:
        with pytest.raises(expected_exception):
            load_validation_rules(logger, file_path)
        assert expected_log in cleared_log_storage[0]["event"]
    else:
        result = load_validation_rules(logger, file_path)
        assert result == expected_output
        assert cleared_log_storage[-1]["event"] == expected_log
        assert cleared_log_storage[-1]["level"] == "info"


@pytest.mark.parametrize(
    "path, result",
    [
        # PropA appears twice
        ("tests/data/utils/example_prop_types_1.py", {"PropA": [3, 18]}),
        # None duplicated
        ("tests/data/utils/example_prop_types_2.py", {}),
    ],
)
def test_duplicated_property_types(cleared_log_storage: list, path: str, result: dict):
    assert result == duplicated_property_types(path, logger)
    if result:
        assert cleared_log_storage[0]["level"] == "critical"
        assert "Found 1 duplicated property types" in cleared_log_storage[0]["event"]


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
def test_is_reduced_version(generated_code, full_code, expected_result):
    """Tests whether generated_code_value is a reduced version of code."""
    result = is_reduced_version(generated_code, full_code)
    assert result == expected_result
