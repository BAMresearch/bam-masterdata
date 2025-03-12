import os

from bam_masterdata.checker.masterdata_validator import MasterDataValidator
from bam_masterdata.checker.source_loader import SourceLoader
from bam_masterdata.logger import logger
from bam_masterdata.metadata.entities_dict import EntitiesDict
from bam_masterdata.utils import load_validation_rules


class MasterdataChecker:
    def __init__(
        self,
        validation_rules_path: str = "bam_masterdata/checker/validation_rules",
        datamodel_dir: str = "bam_masterdata/datamodel",
    ):
        """
        Initialize the comparator with validation rules and set the datamodel directory.

        Args:
            validation_rules_path (str): Path to the validation rules JSON file.
            datamodel_dir (str, optional): Directory where the Python datamodel files are located.
                                           Defaults to "bam_masterdata/datamodel".
        """
        self.validation_rules_path = (
            validation_rules_path  # Store the base directory path
        )
        self.datamodel_dir = (
            datamodel_dir  # Allows overriding the default datamodel directory
        )
        self.current_model: dict = None
        self.new_entities: dict = None
        self.logger = logger
        self.validation_rules: dict = {}  # Initialize empty validation rules

    def _load_validation_rules(self, mode: str) -> dict:
        """
        Load validation rules dynamically based on the validation mode using utils.load_validation_rules.

        Args:
            mode (str): The validation mode ("self", "incoming", "validate", "compare", "all").

        Returns:
            dict: The validation rules loaded from the corresponding JSON file.
        """
        rule_file_map = {
            "self": "validation_rules.json",
            "incoming": "validation_rules.json",
            "validate": "validation_rules.json",
            "compare": "compare_validation_rules.json",
            "all": "all_validation_rules.json",
        }

        rule_file = rule_file_map.get(mode)
        if not rule_file:
            raise ValueError(f"No rule file found for mode: {mode}")

        rule_path = os.path.join(self.validation_rules_path, rule_file)

        return load_validation_rules(
            self.logger, rule_path
        )  # Use the existing function

    def load_current_model(self):
        """
        Load and transform the current data model (Pydantic classes) into JSON.

        Uses the default datamodel directory unless overridden.
        """
        self.logger.info(f"Loading current data model from: {self.datamodel_dir}")
        entities_dict = EntitiesDict(python_path=self.datamodel_dir, logger=self.logger)
        self.current_model = entities_dict.single_json()

    def load_new_entities(self, source: str):
        """
        Load new entities from various sources (Python classes, Excel, etc.).
        """
        self.logger.info(f"Loading new entities from: {source}")
        loader = SourceLoader(source)
        self.new_entities = loader.load()

    def validate(self, mode: str = "all") -> dict:
        """
        Run validations.

        Modes:
        - "self" -> Validate only the current data model.
        - "incoming" -> Validate only the new entity structure.
        - "validate" -> Validate both the current model and new entities.
        - "compare" -> Compare new entities against the current model.
        - "all" -> Run both validation types.

        Before running, ensure that required models are loaded based on the mode.

        Returns:
            dict: Validation results.
        """
        # Validate mode selection
        valid_modes = {"self", "incoming", "validate", "compare", "all"}
        if mode not in valid_modes:
            raise ValueError(f"Invalid mode: {mode}. Choose from {valid_modes}.")

        # Load required models based on the selected mode
        if (
            mode in {"self", "validate", "compare", "all"}
            and self.current_model is None
        ):
            self.logger.info("Current model is missing. Loading now...")
            self.load_current_model()

        if (
            mode in {"incoming", "validate", "compare", "all"}
            and self.new_entities is None
        ):
            raise ValueError(
                "New entities must be loaded before validation in 'incoming', 'validate', 'compare', or 'all' modes."
            )

        # Load the appropriate validation rules based on the mode
        self.validation_rules = self._load_validation_rules(mode)

        validator = MasterDataValidator(
            self.new_entities, self.current_model, self.validation_rules
        )
        return validator.validate(mode)
