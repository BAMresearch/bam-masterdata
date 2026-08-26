from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any


class SyncAction(StrEnum):
    """
    Synchronization actions when updating the masterdata model in openBIS from bam-masterdata definitions.

    Allowed terms are:

    - CREATED: something was created new in openBIS
    - MODIFIED: something was modified in openBIS
    - UNCHANGED: compared and found equal
    - REJECTED: source model requested a change that synchronization refuses to apply
    - IGNORED: difference detected but deliberately outside of current synchronization scope
    """

    CREATED = "created"
    MODIFIED = "modified"
    UNCHANGED = "unchanged"
    REJECTED = "rejected"
    IGNORED = "ignored"


class SyncTarget(StrEnum):
    """
    Target entity when an action is synchronizing the masterdata model with openBIS.
    """

    OBJECT_TYPE = "object_type"
    PROPERTY_TYPE = "property_type"
    PROPERTY_ASSIGNMENT = "property_assignment"
    VOCABULARY = "vocabulary"
    VOCABULARY_TERM = "vocabulary_term"


@dataclass(slots=True)
class SyncChange:
    action: SyncAction
    target: SyncTarget
    code: str
    parent_code: str | None = None
    field: str | None = None
    old_value: Any = None
    new_value: Any = None
    message: str | None = None


@dataclass
class SyncResult:
    changes: list[SyncChange] = field(default_factory=list)

    def add(
        self,
        action: SyncAction,
        target: SyncTarget,
        code: str,
        *,
        parent_code: str | None = None,
        field: str | None = None,
        old_value: Any = None,
        new_value: Any = None,
        message: str | None = None,
    ) -> None:
        """Appends changes with the corresponding metadata."""
        self.changes.append(
            SyncChange(
                action=action,
                target=target,
                code=code,
                parent_code=parent_code,
                field=field,
                old_value=old_value,
                new_value=new_value,
                message=message,
            )
        )

    def created(
        self,
        target: SyncTarget,
        code: str,
        *,
        parent_code: str | None = None,
        message: str | None = None,
    ) -> None:
        """Specific add() method for SyncAction.CREATED actions."""
        self.add(
            SyncAction.CREATED,
            target,
            code,
            parent_code=parent_code,
            message=message,
        )

    def modified(
        self,
        target: SyncTarget,
        code: str,
        field: str,
        old_value: Any,
        new_value: Any,
        *,
        parent_code: str | None = None,
        message: str | None = None,
    ) -> None:
        """Specific add() method for SyncAction.MODIFIED actions."""
        self.add(
            SyncAction.MODIFIED,
            target,
            code,
            parent_code=parent_code,
            field=field,
            old_value=old_value,
            new_value=new_value,
            message=message,
        )

    def rejected(
        self,
        target: SyncTarget,
        code: str,
        field: str,
        old_value: Any,
        new_value: Any,
        *,
        parent_code: str | None = None,
        message: str | None = None,
    ) -> None:
        """Specific add() method for SyncAction.REJECTED actions."""
        self.add(
            SyncAction.REJECTED,
            target,
            code,
            parent_code=parent_code,
            field=field,
            old_value=old_value,
            new_value=new_value,
            message=message,
        )

    def log_sync_result(self, logger) -> None:
        """Transforms the changes list into log messages."""

        for change in self.changes:
            target = change.target.value.replace("_", " ")

            if change.action == SyncAction.CREATED:
                logger.info(f"Created {target} '{change.code}'.")

            elif change.action == SyncAction.MODIFIED:
                logger.info(
                    f"Modified {target} '{change.code}': "
                    f"{change.field} changed from {change.old_value!r} "
                    f"to {change.new_value!r}."
                )

            elif change.action == SyncAction.REJECTED:
                logger.error(
                    change.message
                    or (
                        f"Rejected change to {target} '{change.code}': "
                        f"{change.field} from {change.old_value!r} "
                        f"to {change.new_value!r}."
                    )
                )

            elif change.action == SyncAction.IGNORED:
                logger.warning(
                    change.message or f"Ignored change to {target} '{change.code}'."
                )

            elif change.action == SyncAction.UNCHANGED:
                logger.info(change.message or f"Unchanged {target} '{change.code}'.")
