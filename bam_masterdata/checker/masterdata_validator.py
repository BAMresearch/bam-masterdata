import re

from bam_masterdata.logger import logger
from bam_masterdata.metadata.definitions import DataType
from bam_masterdata.utils import is_reduced_version, store_log_message


class MasterdataValidator:
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
        - "individual": Validate new entities and compare them with the current model.

         Returns:
            dict: Validation results.
        """
        self.logger.debug("Starting validation process...", mode=mode)

        # Reset validation results before running checks
        self.validation_results = {
            "current_model": {},
            "incoming_model": {},
            "comparisons": {},
        }

        if mode in ["self", "all", "validate"]:
            self.logger.debug("Validating current model...")
            self._validate_model(self.current_model)
            self._extract_log_messages(
                self.current_model, self.validation_results["current_model"]
            )

        if mode in ["incoming", "all", "validate"]:
            self.logger.debug("Validating new entities...")
            self._validate_model(self.new_entities)
            self._extract_log_messages(
                self.new_entities, self.validation_results["incoming_model"]
            )

        if mode in ["compare", "all"]:
            self.logger.debug("Comparing new entities with current model...")
            self._compare_with_current_model(mode=mode)
            self._extract_log_messages(
                self.new_entities, self.validation_results["comparisons"]
            )

        if mode == "individual":
            self.logger.debug(
                "Validating new entities and comparing them with current model..."
            )
            self.validation_results = {
                "incoming_model": {},
                "comparisons": {},
            }
            self._validate_model(self.new_entities)
            self._extract_log_messages(
                self.new_entities, self.validation_results["incoming_model"]
            )
            self._compare_with_current_model(mode="individual")
            self._extract_log_messages(
                self.new_entities, self.validation_results["comparisons"]
            )

        return self.validation_results

    def _validate_model(self, model: dict) -> dict:
        """
        Validate the given datamodel against the validation rules.

        Args:
            model (dict): The datamodel to validate.

        Returns:
            dict: A dictionary containing ...
        """
        for entity_type, entities in model.items():
            for entity_name, entity_data in entities.items():
                entity_id = entity_data.get("defs", {}).get("code", entity_name)

                # Ensure _log_msgs exists
                if "_log_msgs" not in entity_data:
                    entity_data["_log_msgs"] = []

                if model == self.new_entities:
                    self.logger.info(f"Validating {entity_type} -> {entity_id}")

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
                    # Collect ordered sections for each entity
                    entity_sections = []

                    for prop in entity_data["properties"]:
                        row_location = prop.get("row_location", "Unknown")

                        # Collect section names in order
                        section = prop.get("section", "").strip()
                        if section:  # Avoid empty sections
                            entity_sections.append(
                                {
                                    "code": prop["code"],
                                    "section": section,
                                    "row_location": row_location,
                                }
                            )

                        # Check for deprecated `$ANNOTATIONS_STATE`
                        if (
                            prop["code"] == "$ANNOTATIONS_STATE"
                            and model == self.new_entities
                        ):
                            log_message = (
                                f"Property $ANNOTATIONS_STATE is deprecated from openBIS 20.10.7.3. "
                                f"Assigned to entity '{entity_id}' at row {row_location}."
                            )
                            store_log_message(
                                logger, entity_data, log_message, level="warning"
                            )

                        self._validate_fields(
                            prop,
                            "properties_validation",
                            entity_type,
                            entity_id,
                            row_location,
                            entity_data,
                        )

                # TODO: revise if these checks about ordering of sections are truly necessary
                # Check if "Additional Information" is followed only by "Additional Information" or "Comments"
                for i in range(len(entity_sections) - 1):
                    current_section = entity_sections[i]["section"]
                    next_section = entity_sections[i + 1]["section"]
                    row_location = entity_sections[i + 1]["row_location"]

                    if (
                        current_section == "Additional Information"
                        and next_section not in {"Additional Information", "Comments"}
                    ):
                        log_message = (
                            f"Invalid section order: 'Additional Information' at row {entity_sections[i]['row_location']} "
                            f"must be followed by 'Comments', but found '{next_section}' at row {row_location}."
                        )
                        store_log_message(
                            logger, entity_data, log_message, level="error"
                        )

                # Check if required properties exist in specific sections
                required_properties = {
                    "Additional Information": "NOTES",
                    "Comments": "COMMENTS",
                }

                # Track found properties
                found_properties = {section: False for section in required_properties}

                for entry in entity_sections:
                    section = entry["section"]
                    property_code = entry["code"]
                    row_location = entry["row_location"]

                    if (
                        section in required_properties
                        and property_code == required_properties[section]
                    ):
                        found_properties[section] = True

                # Log errors for missing required properties
                for section, prop in required_properties.items():
                    if (
                        any(entry["section"] == section for entry in entity_sections)
                        and not found_properties[section]
                    ):
                        log_message = f"Missing required property '{prop}' in section '{section}'."
                        store_log_message(
                            logger, entity_data, log_message, level="error"
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
            "properties_validation": "in 'properties'.",
            "terms_validation": "in 'terms'.",
        }.get(rule_type, ".")

        for field, value in data.items():
            rule = self.validation_rules.get(rule_type, {}).get(field)

            extra_location_str = f" {extra_location} " if extra_location else " "

            log_message = (
                f"Invalid '{value}' value found in the '{field}' field at line {row_location} "
                f"in entity '{entity_name}' of '{entity_type}'{extra_location_str}"
            )

            if not rule:
                continue  # Skip fields with no validation rules

            # Handle empty fields
            if "allow_empty" in rule and (value is None or value == "" or not value):
                continue  # Skip check if empty fields are allowed

            # Validate pattern (regex)
            if "pattern" in rule and value is not None:
                if not re.match(rule["pattern"], str(value)):
                    log_message = f"{log_message}Invalid format."
                    level = "error"
                    if "is_description" in rule:
                        log_message = f"{log_message} Description should follow the schema: English Description + '//' + German Description. "
                        level = "warning"
                    if "is_section" in rule:
                        log_message = f"{log_message} First letter of every word starts with capitalized lettter."
                        level = "warning"
                    store_log_message(logger, parent_entity, log_message, level=level)

            # Validate boolean fields
            if "is_bool" in rule and str(value).strip().lower() not in [
                "true",
                "false",
            ]:
                store_log_message(
                    logger,
                    parent_entity,
                    f"{log_message}Expected a boolean.",
                    level="error",
                )

            # Validate data types
            if "is_data" in rule and str(value) not in [dt.value for dt in DataType]:
                store_log_message(
                    logger,
                    parent_entity,
                    f"{log_message}The Data Type should be one of the following: {[dt.value for dt in DataType]}",
                    level="error",
                )

            # Validate special cases (e.g., extra validation functions)
            if "extra_validation" in rule:
                validation_func = getattr(self, rule["extra_validation"], None)
                if validation_func == "is_reduced_version" and not is_reduced_version(
                    value, entity_name
                ):
                    store_log_message(
                        logger,
                        parent_entity,
                        f"{log_message}The generated code should be a part of the code.",
                        level="warning",
                    )

    def _compare_with_current_model(self, mode) -> dict:
        """
        Compare new entities against the current model using validation rules.
        """
        self.logger.debug("Starting comparison with the current model...")

        new_entity = False

        all_props = self.extract_property_codes(self.current_model)

        for entity_type, incoming_entities in self.new_entities.items():
            if entity_type not in self.current_model:
                continue  # Skip if entity type does not exist in the current model

            current_entities = self.current_model[entity_type]

            for entity_code, incoming_entity in incoming_entities.items():
                incoming_row_location = "Unknown"
                current_entity = current_entities.get(entity_code)

                # Ensure _log_msgs exists
                if "_log_msgs" not in incoming_entity:
                    incoming_entity["_log_msgs"] = []

                if current_entity:
                    if mode == "individual":
                        log_message = f"The entity {entity_code} already exists in `bam-masterdata`. Please, check your classes. "
                        store_log_message(
                            logger, incoming_entity, log_message, level="critical"
                        )
                    # Compare general attributes for all entities
                    for key, new_value in incoming_entity.get("defs", {}).items():
                        incoming_row_location = incoming_entity.get("defs", {}).get(
                            "row_location", "Unknown"
                        )
                        old_value = current_entity.get("defs", {}).get(key)
                        if (
                            (key != "code" and key != "row_location")
                            and old_value is not None
                            and new_value != old_value
                        ):
                            log_message = (
                                f"Entity type {entity_code} has changed its attribute {key} "
                                f"from '{old_value}' to '{new_value}' at row {incoming_row_location}."
                            )
                            store_log_message(
                                logger, incoming_entity, log_message, level="warning"
                            )

                    # Special case for `property_types`
                    if entity_type == "property_types":
                        incoming_row_location = incoming_entity.get(
                            "row_location", "Unknown"
                        )
                        new_data_type = incoming_entity.get("data_type")
                        old_data_type = current_entity.get("data_type")

                        if (
                            new_data_type
                            and old_data_type
                            and new_data_type != old_data_type
                        ):
                            log_message = (
                                f"Property type {entity_code} has changed its `data_type` value from {old_data_type} to {new_data_type} at row {incoming_row_location}. "
                                "This will cause that data using the Property with inconsistent versions of data type will probably break openBIS. "
                                "You need to define a new property with the new data type or revise your data model."
                            )
                            store_log_message(
                                logger, incoming_entity, log_message, level="critical"
                            )

                        if (
                            new_data_type == "CONTROLLEDVOCABULARY"
                            and incoming_entity.get("vocabulary_code")
                            != current_entity.get("vocabulary_code")
                        ):
                            old_vocabulary = current_entity.get("vocabulary_code")
                            new_vocabulary = incoming_entity.get("vocabulary_code")
                            log_message = (
                                f"Property type {entity_code} using controlled vocabulary has changed its `vocabulary_code` value from {old_vocabulary} to {new_vocabulary}, "
                                f"at row {incoming_row_location} which means that data using a type that is not compatible with the new type will probably break openBIS. "
                                "You need to define a new property with the new data type or revise your data model."
                            )
                            store_log_message(
                                logger, incoming_entity, log_message, level="critical"
                            )

                else:
                    new_entity = True

                # Compare assigned properties or terms
                if "properties" in incoming_entity:
                    self._compare_assigned_properties(
                        entity_code,
                        incoming_entity,
                        current_entity,
                        entity_type,
                        new_entity,
                        incoming_row_location,
                        all_props,
                    )
                elif "terms" in incoming_entity:
                    self._compare_assigned_properties(
                        entity_code,
                        incoming_entity,
                        current_entity,
                        entity_type,
                        new_entity,
                        incoming_row_location,
                        all_props,
                        is_terms=True,
                    )

        if not self.validation_results.get("comparisons"):
            logger.info(
                "No critical conflicts found between new entities compared to the current model."
            )

        return self.validation_results

    def _compare_assigned_properties(
        self,
        entity_code,
        incoming_entity,
        current_entity,
        entity_type,
        new_entity,
        incoming_row_location,
        all_props,
        is_terms=False,
    ):
        """
        Compares assigned properties (for ObjectType, CollectionType, etc.) or terms (for VocabularyType).
        """
        incoming_props = {
            prop["code"]: prop
            for prop in incoming_entity.get(
                "properties" if not is_terms else "terms", []
            )
        }

        incoming_prop_codes = set(incoming_props.keys())

        if not new_entity:
            current_props = {
                prop["code"]: prop
                for prop in current_entity.get(
                    "properties" if not is_terms else "terms", []
                )
            }

            # Check for non-existing assigned properties
            current_prop_codes = set(current_props.keys())

            for prop_code in incoming_prop_codes:
                if prop_code not in all_props and is_terms is False:
                    log_message = (
                        f"The assigned property {prop_code} to the entity {entity_code} at row {incoming_props[prop_code].get('row_location')} does not exist in openBIS. "
                        "Please, define it in your PropertyType section."
                    )
                    store_log_message(
                        logger, incoming_entity, log_message, level="error"
                    )

            # Check for existing changes in assigned properties
            missing_properties = incoming_prop_codes - current_prop_codes
            deleted_properties = current_prop_codes - incoming_prop_codes

            if missing_properties or deleted_properties:
                log_message = f"The assigned properties to {entity_code} at row {incoming_row_location} have changed:"
                store_log_message(logger, incoming_entity, log_message, level="warning")

            # Check for missing properties
            for missing in missing_properties:
                log_message = f"{missing} has been added as a new property at row {incoming_props[missing].get('row_location')}."
                store_log_message(logger, incoming_entity, log_message, level="info")

            # Check for deleted properties
            for deleted in deleted_properties:
                log_message = f"{deleted} has been deleted."
                store_log_message(logger, incoming_entity, log_message, level="warning")

            # Check for property modifications
            common_props = incoming_prop_codes & current_prop_codes
            for prop_code in common_props:
                new_prop = incoming_props[prop_code]
                old_prop = current_props[prop_code]

                for key, new_value in new_prop.items():
                    old_value = old_prop.get(key)
                    if (
                        (key != "code" and key != "row_location")
                        and old_value is not None
                        and new_value != old_value
                    ):
                        log_message = (
                            f"Assigned property {prop_code} to entity type {entity_code} has changed its attribute {key} "
                            f"from '{old_value}' to '{new_value}' at row {incoming_props[prop_code].get('row_location')}."
                        )
                        store_log_message(
                            logger, incoming_entity, log_message, level="warning"
                        )

        # Check if assigned properties match another entity's properties
        for other_entity_code, other_entity in self.current_model.get(
            entity_type, {}
        ).items():
            if other_entity_code != entity_code:
                other_entity_properties = (
                    other_entity.get("properties", [])
                    if not is_terms
                    else other_entity.get("terms", [])
                )
                other_entity_props = {prop["code"] for prop in other_entity_properties}

                if (incoming_prop_codes == other_entity_props) and incoming_prop_codes:
                    log_message = (
                        "Entity will not be imported in openBIS. "
                        f"The entity {entity_code} at row {incoming_entity['defs'].get('row_location')} has the same properties defined as {other_entity_code}. "
                        "Maybe they are representing the same entity?"
                    )
                    store_log_message(
                        logger, incoming_entity, log_message, level="warning"
                    )

    def _extract_log_messages(self, model: dict, target_dict: dict) -> None:
        """
        Extracts and appends _log_msgs from the validated entities into an existing dictionary.

        Args:
            model (dict): The validated entity model.
            target_dict (dict): The dictionary where logs should be appended.
        """
        for entity_type, entities in model.items():
            if entity_type not in target_dict:
                target_dict[entity_type] = {}

            for entity_name, entity_data in entities.items():
                if "_log_msgs" in entity_data and entity_data["_log_msgs"]:
                    if entity_name not in target_dict[entity_type]:
                        target_dict[entity_type][entity_name] = {"_log_msgs": []}

                    # Append new messages to the existing ones
                    target_dict[entity_type][entity_name]["_log_msgs"].extend(
                        entity_data["_log_msgs"]
                    )

    def extract_property_codes(self, data):
        codes = set()

        # Check if the data contains 'properties' and extract 'code'
        if isinstance(data, dict):
            for key, value in data.items():
                # If the key is 'properties', collect all the 'code' values
                if key == "properties" and isinstance(value, list):
                    for property_item in value:
                        if "code" in property_item:
                            codes.add(property_item["code"])
                # Recursively check for more nested structures
                elif isinstance(value, (dict, list)):
                    codes.update(self.extract_property_codes(value))

        elif isinstance(data, list):
            for item in data:
                codes.update(self.extract_property_codes(item))

        return codes
