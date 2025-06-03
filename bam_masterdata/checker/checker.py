from bam_masterdata.checker.masterdata_validator import MasterdataValidator
from bam_masterdata.checker.source_loader import SourceLoader
from bam_masterdata.logger import logger
from bam_masterdata.metadata.entities_dict import EntitiesDict
from bam_masterdata.utils import load_validation_rules


class MasterdataChecker:
    VALID_MODES = {"self", "incoming", "validate", "compare", "all", "individual"}

    def __init__(self):
        """
        Initialize the comparator with validation rules and set the datamodel directory.
        """
        self.current_model: dict = None
        self.new_entities: dict = None
        self.logger = logger
        self.validation_rules: dict = {}

    def load_current_model(self, datamodel_dir: str = "./bam_masterdata/datamodel/"):
        """
        Load and transform the current data model (Pydantic classes) into JSON.

        Uses the default datamodel directory unless overridden.
        """
        self.logger.info(f"Loading current data model from: {datamodel_dir}")
        entities_dict = EntitiesDict(python_path=datamodel_dir, logger=self.logger)
        self.current_model = entities_dict.single_json()

    def load_new_entities(self, source: str):
        """
        Load new entities from various sources (Python classes, Excel, etc.).
        """
        self.logger.info(f"Loading new entities from: {source}")
        loader = SourceLoader(source)
        self.new_entities = loader.load()

    def check(self, mode: str = "all") -> dict:
        """
        Run validations.

        Modes:
        - "self" -> Validate only the current data model.
        - "incoming" -> Validate only the new entity structure.
        - "validate" -> Validate both the current model and new entities.
        - "compare" -> Compare new entities against the current model.
        - "all" -> Run both validation types.
        - "individual" -> Run individual repositories validations.

        Before running, ensure that required models are loaded based on the mode.

        Returns:
            dict: Validation results.
        """
        # Validate mode selection
        if mode not in self.VALID_MODES:
            raise ValueError(f"Invalid mode: {mode}. Choose from {self.VALID_MODES}.")

        # Load required models based on the selected mode
        if (
            mode in ["self", "validate", "compare", "all", "individual"]
            and self.current_model is None
        ):
            self.logger.info("Current model is missing. Loading it from local files.")
            self.load_current_model()

        if (
            mode in ["incoming", "validate", "compare", "all", "individual"]
            and self.new_entities is None
        ):
            raise ValueError(
                "New entities must be loaded before validation in 'incoming', 'validate', 'individual', 'compare', or 'all' modes."
            )

        # Load the validation rules
        if (
            mode in ["self", "incoming", "validate", "all", "individual"]
            and self.validation_rules == {}
        ):
            self.validation_rules = load_validation_rules(self.logger)

        validator = MasterdataValidator(
            self.new_entities, self.current_model, self.validation_rules
        )
        return validator.validate(mode)


def no_validation_errors(validation_results: dict) -> bool:
    """
    Check if there are no validation errors in the results.

    Args:
        validation_results (dict): The dictionary containing the specific validation results.

    Returns:
        bool: True if there are no validation errors, False otherwise.
    """

    if not isinstance(validation_results, dict):
        return False
    return all(no_validation_errors(v) for v in validation_results.values())
