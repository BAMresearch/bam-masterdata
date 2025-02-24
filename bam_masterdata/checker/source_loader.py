from bam_masterdata.excel.excel_to_entities import MasterdataExcelExtractor
from bam_masterdata.logger import logger
from bam_masterdata.metadata.entities_dict import EntitiesDict


class SourceLoader:
    """
    Load the entities from a source written in different formats (Python classes, Excel, etc.) as defined
    in the `source_path` into a dictionary.
    """

    def __init__(self, source_path: str, **kwargs):
        self.source_path = source_path
        if self.source_path.endswith(".py"):
            self.source_type = "python"
        elif self.source_path.endswith(".xlsx"):
            self.source_type = "excel"
        self.logger = kwargs.get("logger", logger)
        self.row_cell_info = kwargs.get("row_cell_info", True)

    def load(self) -> dict:
        """
        Load entities from the source path into a dictionary.

        Returns:
            dict: A dictionary containing the entities.
        """
        if self.source_type == "python":
            return EntitiesDict(python_path=self.source_path).single_json()
        elif self.source_type == "excel":
            return MasterdataExcelExtractor(
                excel_path=self.source_path, row_cell_info=self.row_cell_info
            ).excel_to_entities()
        else:
            raise NotImplementedError(f"Source type {self.source_type} not supported.")
