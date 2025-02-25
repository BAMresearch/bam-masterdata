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
<<<<<<< HEAD
        self.logger.info(f"Loading current data model from: {self.datamodel_dir}")
        self.current_model = DataModelLoader(self.datamodel_dir).data
=======
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
>>>>>>> 3e1c0f647499112e50bf6118aad054efc1816c03

    def load_new_entities(self, source: str, source_type: str):
        """
        Load new entities from various sources (Python classes, Excel, etc.).
        """
        self.logger.info(f"Loading new entities from: {source} (Type: {source_type})")
        loader = SourceLoader(source, source_type)
        self.new_entities = loader.load()

    def validate(self, mode: str = "all") -> dict:
        """
        Run validations.

        Modes:
        - "self" -> Validate only the current data model.
        - "incoming" -> Validate only the new entity structure.
        - "compare" -> Validate new entities against the current model.
        - "all" -> Run both validation types.

        Before running, ensure that required models are loaded based on the mode.

        Returns:
            dict: Validation results.
        """
        # Validate mode selection
        valid_modes = {"self", "incoming", "compare", "all"}
        if mode not in valid_modes:
            raise ValueError(f"Invalid mode: {mode}. Choose from {valid_modes}.")

        # Load required models based on the selected mode
        if mode in {"self", "compare", "all"} and self.current_model is None:
            self.logger.info("Current model is missing. Loading now...")
            self.load_current_model()

        if mode in {"incoming", "compare", "all"} and self.new_entities is None:
            raise ValueError(
                "New entities must be loaded before validation in 'incoming', 'compare', or 'all' modes."
            )

        validator = MasterDataValidator(
            self.new_entities, self.current_model, self.validation_rules
        )
        return validator.validate(mode)
