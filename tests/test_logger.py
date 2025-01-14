from typing import Callable

import pytest

from bam_masterdata.logger import logger


@pytest.mark.parametrize(
    "log_level, message, level",
    [
        (logger.info, "This is a test info message.", "info"),
        (logger.debug, "This is a test debug message.", "debug"),
        (logger.warning, "This is a test warning message.", "warning"),
    ],
)
def test_logger_info_message(
    cleared_log_storage: list, log_level: Callable, message: str, level: str
):
    """Tests if a `level` message is correctly logged into the (cleared) `log_storage`."""
    log_level(message)

    # Check the log storage for the recorded message
    assert len(cleared_log_storage) == 1
    sorted(cleared_log_storage[0].keys()) == [
        "event",
        "func_name",
        "level",
        "lineno",
        "pathname",
        "timestamp",
    ]
    assert cleared_log_storage[0]["event"] == message
    assert cleared_log_storage[0]["func_name"] == "test_logger_info_message"
    assert cleared_log_storage[0]["level"] == level
    assert cleared_log_storage[0]["lineno"] == 20
    assert cleared_log_storage[0]["pathname"].endswith("tests/test_logger.py")
    assert "timestamp" in cleared_log_storage[0]
