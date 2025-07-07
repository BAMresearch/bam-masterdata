from abc import ABC, abstractmethod


class AbstractParser(ABC):
    """
    Example Abstract base class for parsers.
    Each parser should implement the `parse` method.
    Will be in the parsing.py file. 
    """
    @abstractmethod
    def parse(self, files: list[str], collection: str):
        """
        Parse the given files and store the results in the specified collection.
        Args:
            files (list): List of file paths to be parsed.
            collection (str): The collection in openBIS where the entities will be stored.
        """
        pass