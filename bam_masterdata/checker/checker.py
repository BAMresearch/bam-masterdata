import os

from bam_masterdata.checker.datamodel_loader import DataModelLoader
from bam_masterdata.checker.masterdata_validator import MasterDataValidator
from bam_masterdata.checker.source_loader import SourceLoader
from bam_masterdata.logger import logger


class MasterdataChecker:
    def __init__(
        self,
        validation_rules_path: str,
        datamodel_dir: str = "bam_masterdata/datamodel",
    ):
        """
        Initialize the comparator with validation rules and set the datamodel directory.

        Args:
            validation_rules_path (str): Path to the validation rules JSON file.
            datamodel_dir (str, optional): Directory where the Python datamodel files are located.
                                           Defaults to "bam_masterdata/datamodel".
        """
        self.validation_rules = self._load_validation_rules(validation_rules_path)
        self.datamodel_dir = (
            datamodel_dir  # Allows overriding the default datamodel directory
        )
        self.current_model = None
        self.new_entities = None
        self.logger = logger

    def _load_validation_rules(self, path: str) -> dict:
        """
        Load validation rules from a JSON file.
        """
        pass

    def load_current_model(self):
        """
        Load and transform the current data model (Pydantic classes) into JSON.

        Uses the default datamodel directory unless overridden.
        """
        export_dir = "bam_masterdata/checker/tmp/datamodel"
        os.makedirs(export_dir, exist_ok=True)  # Ensure export directory exists

        # List all Python files in the datamodel directory (same as CLI behavior)
        source_files = [
            os.path.join(self.datamodel_dir, f)
            for f in os.listdir(self.datamodel_dir)
            if f.endswith(".py")
        ]

        # Ensure we found Python files
        if not source_files:
            raise FileNotFoundError(f"No Python files found in {self.datamodel_dir}")

        # Now call DataModelLoader with the list of files
        self.current_model = DataModelLoader(source_files).data

    def load_new_entities(self, source: str, source_type: str):
        """
        Load new entities from various sources (Python classes, Excel, etc.).
        """
        # loader = SourceLoader(source, source_type)
        # self.new_entities = loader.load()

    def validate(self, mode: str = "all") -> dict:
        """
        Run validations. Mode can be:
        - "self" -> Validate only the new entity structure.
        - "compare" -> Validate new entities against current model.
        - "all" -> Run both validation types.
        """
        validator = MasterDataValidator(
            self.new_entities, self.current_model, self.validation_rules
        )
        return validator.validate(mode)
