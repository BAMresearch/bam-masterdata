import json
import re

from bam_masterdata.logger import logger
from bam_masterdata.utils import is_reduced_version


class MasterDataValidator:
    def __init__(self, new_entities: dict, current_model: dict, validation_rules: dict):
        """
        Initialize the validator with new and current entity data.

        Args:
            new_entities (dict): The incoming datamodel.
            current_model (dict): The existing datamodel.
            rules_path (str): Path to the validation rules JSON file.
        """
        self.new_entities = new_entities
        self.current_model = current_model
        self.validation_rules = validation_rules
        self.logger = logger
        self.log_msgs: list = []
        self.validation_results: dict = {}

    def validate(self, mode: str = "all") -> dict:
        """
        Run validations based on mode:
        - "self": Validate current model structure and format.
        - "incoming": Validate new entities structure and format.
        - "validate": Validate both current and incoming models but do not compare.
        - "compare": Validate new entities against the current model.
        - "all": Run both.

         Returns:
            dict: Validation results.
        """
        self.logger.info("Starting validation process...", mode=mode)

        # Reset validation results before running checks
        self.validation_results = {}

        if mode in ["self", "all", "validate"]:
            self.logger.info("Validating current model...")
            self._validate_model(self.current_model)
            self.validation_results["current_model"] = self._extract_log_messages(
                self.current_model
            )

        if mode in ["incoming", "all", "validate"]:
            self.logger.info("Validating new entities...")
            self._validate_model(self.new_entities)
            self.validation_results["incoming_model"] = self._extract_log_messages(
                self.new_entities
            )

        if mode in ["compare", "all"]:
            self.logger.info("Comparing new entities with current model...")
            self._compare_with_current_model(self.current_model, self.new_entities)
            self.validation_results["comparisons"] = self._extract_log_messages(
                self.new_entities
            )

        return self.validation_results

    def _validate_model(self, model: dict) -> dict:
        """
        Validate the given datamodel against the validation rules.

        Args:
            model (dict): The datamodel to validate.
            results (dict): Dictionary storing validation errors and warnings.
        """
        for entity_type, entities in model.items():
            for entity_name, entity_data in entities.items():
                entity_id = entity_data.get("defs", {}).get("code", entity_name)

                # Ensure _log_msgs exists
                if "_log_msgs" not in entity_data:
                    entity_data["_log_msgs"] = []

                logger.info(f"Validating {entity_type} -> {entity_id}")

                # Validate 'defs'
                if "defs" in entity_data:
                    row_location = entity_data["defs"].get("row_location", "Unknown")
                    self._validate_fields(
                        entity_data["defs"],
                        "defs_validation",
                        entity_type,
                        entity_id,
                        row_location,
                        entity_data,
                    )

                # Validate 'properties' (except for vocabulary_types, which uses 'terms')
                if entity_type != "vocabulary_types" and "properties" in entity_data:
                    for prop in entity_data["properties"]:
                        row_location = prop.get("row_location", "Unknown")
                        self._validate_fields(
                            prop,
                            "properties_validation",
                            entity_type,
                            entity_id,
                            row_location,
                            entity_data,
                        )

                # Validate 'terms' (only for vocabulary_types)
                if entity_type == "vocabulary_types" and "terms" in entity_data:
                    for term in entity_data["terms"]:
                        row_location = term.get("row_location", "Unknown")
                        self._validate_fields(
                            term,
                            "terms_validation",
                            entity_type,
                            entity_id,
                            row_location,
                            entity_data,
                        )

        return entity_data

    def _validate_fields(
        self,
        data: dict,
        rule_type: str,
        entity_type: str,
        entity_name: str,
        row_location: str,
        parent_entity: dict,
    ):
        """
        Validate a dictionary of fields against the corresponding validation rules.

        Args:
            data (dict): The fields to validate.
            rule_type (str): The rule section to use ("defs_validation", "properties_validation", or "terms_validation").
            entity_type (str): The entity type being validated.
            entity_name (str): The specific entity name (ID if available).
            row_location (str): The row where the entity is located in the source file.
            parent_entity (dict): The entity dictionary where _log_msgs should be stored.
        """

        # Determine where the issue is occurring (in properties, terms, or main entity fields)
        extra_location = {
            "properties_validation": " in 'properties'.",
            "terms_validation": " in 'terms'.",
        }.get(rule_type, ".")

        for field, value in data.items():
            rule = self.validation_rules.get(rule_type, {}).get(field)

            if not rule:
                continue  # Skip fields with no validation rules

            # Handle empty fields
            if "allow_empty" in rule and (value is None or value == "" or not value):
                continue  # Skip check if empty fields are allowed

            # Validate pattern (regex)
            if "pattern" in rule and value is not None:
                if not re.match(rule["pattern"], str(value)):
                    self._store_log(
                        parent_entity,
                        entity_type,
                        entity_name,
                        field,
                        value,
                        row_location,
                        extra_location,
                        "Invalid format.",
                    )

            # Validate boolean fields
            if "is_bool" in rule and str(value).strip().lower() not in [
                "true",
                "false",
            ]:
                self._store_log(
                    parent_entity,
                    entity_type,
                    entity_name,
                    field,
                    value,
                    row_location,
                    extra_location,
                    "Expected a boolean.",
                )

            # Validate special cases (e.g., extra validation functions)
            if "extra_validation" in rule:
                validation_func = getattr(self, rule["extra_validation"], None)
                if validation_func == "is_reduced_version" and not is_reduced_version(
                    value, entity_name
                ):
                    self._store_log(
                        parent_entity,
                        entity_type,
                        entity_name,
                        field,
                        value,
                        row_location,
                        extra_location,
                        "The generated code should be a part of the code.",
                    )

    def _compare_with_current_model(
        self, current_model: dict, incoming_model: dict
    ) -> dict:
        """
        Compare new entities against the current model using validation rules.
        """
        pass

    def _store_log(
        self,
        entity_ref,
        entity_type,
        entity_name,
        field,
        value,
        row_location,
        extra_location,
        message,
    ):
        """
        Logs an error and stores it inside the parent entity's _log_msgs list.

        Args:
            entity_ref (dict): The entity dictionary where _log_msgs should be stored.
            entity_type (str): The entity type being validated.
            entity_name (str): The specific entity name (ID if available).
            field (str): The field that is being validated.
            value (str): The actual value of the field.
            row_location (str): The row where the issue occurred.
            extra_location (str): Whether the error is in properties, terms, or main fields.
            message (str): The error message to log.
        """
        log_message = (
            f"Invalid '{value}' value found in the '{field}' field at line {row_location} "
            f"in entity '{entity_name}' of '{entity_type}'"
            + (f" {extra_location}" if extra_location else "")
            + f" {message}"
        )

        # Log the message using structlog (for debugging purposes)
        logger.error(log_message)

        # Ensure _log_msgs exists in parent entity (NOT in properties/terms)
        if "_log_msgs" not in entity_ref:
            entity_ref["_log_msgs"] = []

        # Append log message to the parent entity
        entity_ref["_log_msgs"].append(log_message)

        self.log_msgs.append(log_message)

    def _extract_log_messages(self, model: dict) -> dict:
        """
        Extracts and structures the _log_msgs from the validated entities.

        Args:
            model (dict): The validated entity model.

        Returns:
            dict: A dictionary containing only the _log_msgs structured by entity type and entity name.
        """
        simplified_logs: dict = {}

        for entity_type, entities in model.items():
            for entity_name, entity_data in entities.items():
                if "_log_msgs" in entity_data and entity_data["_log_msgs"]:
                    if entity_type not in simplified_logs:
                        simplified_logs[entity_type] = {}
                    simplified_logs[entity_type][entity_name] = {
                        "_log_msgs": entity_data["_log_msgs"]
                    }

        return simplified_logs
