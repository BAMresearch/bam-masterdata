import inspect
import os
import shutil

import pytest

from bam_masterdata.logger import logger
from bam_masterdata.utils import (
    code_to_class_name,
    delete_and_create_dir,
    import_module,
    listdir_py_modules,
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
        ("./tests/data", [], "No Python files found in the directory.", "info"),
        # Python files found in the directory
        (
            "./tests/utils",
            [
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
    assert result == sorted(listdir)


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
    assert code_to_class_name(code, entity_type) == result
