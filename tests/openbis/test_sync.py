from unittest.mock import MagicMock

from bam_masterdata.openbis.sync import (
    SyncAction,
    SyncChange,
    SyncResult,
    SyncTarget,
)


def test_sync_change():
    change = SyncChange(
        action=SyncAction.MODIFIED,
        target=SyncTarget.PROPERTY_TYPE,
        code="TEST",
        field="description",
        old_value="old",
        new_value="new",
    )

    assert change.action == SyncAction.MODIFIED
    assert change.target == SyncTarget.PROPERTY_TYPE
    assert change.code == "TEST"
    assert change.field == "description"
    assert change.old_value == "old"
    assert change.new_value == "new"


def test_sync_result_add():
    result = SyncResult()

    result.add(
        action=SyncAction.IGNORED,
        target=SyncTarget.PROPERTY_ASSIGNMENT,
        code="TEST",
        parent_code="OBJECT",
        message="Ignored.",
    )

    assert len(result.changes) == 1

    change = result.changes[0]
    assert change.action == SyncAction.IGNORED
    assert change.target == SyncTarget.PROPERTY_ASSIGNMENT
    assert change.code == "TEST"
    assert change.parent_code == "OBJECT"
    assert change.message == "Ignored."


def test_sync_result_created():
    result = SyncResult()

    result.created(
        target=SyncTarget.OBJECT_TYPE,
        code="TEST",
    )

    assert result.changes == [
        SyncChange(
            action=SyncAction.CREATED,
            target=SyncTarget.OBJECT_TYPE,
            code="TEST",
        )
    ]


def test_sync_result_modified():
    result = SyncResult()

    result.modified(
        target=SyncTarget.PROPERTY_TYPE,
        code="TEST",
        field="label",
        old_value="Old",
        new_value="New",
    )

    change = result.changes[0]

    assert change.action == SyncAction.MODIFIED
    assert change.field == "label"
    assert change.old_value == "Old"
    assert change.new_value == "New"


def test_sync_result_rejected():
    result = SyncResult()

    result.rejected(
        target=SyncTarget.PROPERTY_TYPE,
        code="TEST",
        field="data_type",
        old_value="VARCHAR",
        new_value="INTEGER",
    )

    change = result.changes[0]

    assert change.action == SyncAction.REJECTED
    assert change.field == "data_type"


def test_log_created():
    result = SyncResult()
    result.created(
        target=SyncTarget.OBJECT_TYPE,
        code="TEST",
    )

    logger = MagicMock()

    result.log_sync_result(logger)

    logger.info.assert_called_once_with("Created object type 'TEST'.")


def test_log_modified():
    result = SyncResult()
    result.modified(
        target=SyncTarget.PROPERTY_TYPE,
        code="TEST",
        field="label",
        old_value="Old",
        new_value="New",
    )

    logger = MagicMock()

    result.log_sync_result(logger)

    logger.info.assert_called_once_with(
        "Modified property type 'TEST': label changed from 'Old' to 'New'."
    )


def test_log_rejected():
    result = SyncResult()
    result.rejected(
        target=SyncTarget.PROPERTY_TYPE,
        code="TEST",
        field="data_type",
        old_value="VARCHAR",
        new_value="INTEGER",
    )

    logger = MagicMock()

    result.log_sync_result(logger)

    logger.error.assert_called_once_with(
        "Rejected change to property type 'TEST': "
        "data_type from 'VARCHAR' to 'INTEGER'."
    )


def test_log_ignored_with_message():
    result = SyncResult()
    result.add(
        action=SyncAction.IGNORED,
        target=SyncTarget.PROPERTY_ASSIGNMENT,
        code="TEST",
        message="Not supported yet.",
    )

    logger = MagicMock()

    result.log_sync_result(logger)

    logger.warning.assert_called_once_with("Not supported yet.")


def test_log_unchanged():
    result = SyncResult()
    result.add(
        action=SyncAction.UNCHANGED,
        target=SyncTarget.PROPERTY_TYPE,
        code="TEST",
    )

    logger = MagicMock()

    result.log_sync_result(logger)

    logger.info.assert_called_once_with("Unchanged property type 'TEST'.")
