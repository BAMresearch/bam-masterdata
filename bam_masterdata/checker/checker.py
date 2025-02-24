from bam_masterdata.checker.masterdata_validator import MasterDataValidator
from bam_masterdata.checker.source_loader import SourceLoader


class MasterdataChecker:
    def __init__(self, validation_rules_path: str):
        """
        Initialize the comparator with validation rules.
        """
        self.validation_rules = self._load_validation_rules(validation_rules_path)
        self.current_model = None
        self.new_entities = None

    def _load_validation_rules(self, path: str) -> dict:
        """
        Load validation rules from a JSON file.
        """
        pass

    def load_current_model(self, source_path: str):
        """
        Load and transform the current data model (Pydantic classes) into JSON.
        """
        # loader = DataModelLoader(source_path)
        # self.current_model = loader.parse_pydantic_models()

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
