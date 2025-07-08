from abc import ABC, abstractmethod

from bam_masterdata.metadata.entities import CollectionType


class AbstractParser(ABC):
    """
    Example Abstract base class for parsers.
    Each parser should implement the `parse` method.
    """

    @abstractmethod
    def parse(self, files: list[str], collection: CollectionType):
        """
        Parse the given files and store the results in the specified collection.
        Args:
            files (list): List of file paths to be parsed.
            collection (str): The collection in openBIS where the entities will be stored.
        """
        pass
