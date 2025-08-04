from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from bam_masterdata.metadata.entities import CollectionType

if TYPE_CHECKING:
    from structlog._config import BoundLoggerLazyProxy


class AbstractParser(ABC):
    """
    Example Abstract base class for parsers. Each parser should inherit from this class and implement
    the `parse()` method to populate `collection`.
    """

    @abstractmethod
    def parse(
        self,
        files: list[str],
        collection: CollectionType,
        logger: "BoundLoggerLazyProxy",
    ) -> None:
        """
        Parse the input `files` and populate the provided `collection` with object types, their metadata,
        and their relationships.

        Args:
            files (list[str]): List of file paths to be parsed.
            collection (CollectionType): Collection to be populated with parsed data.
            logger (BoundLoggerLazyProxy): Logger for logging messages during parsing.
        """
        pass
