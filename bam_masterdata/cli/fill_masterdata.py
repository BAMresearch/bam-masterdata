import time

import click

from bam_masterdata.openbis import OpenbisEntities
from bam_masterdata.openbis.login import environ


class MasterdataCodeGenerator:
    """
    Class to generate Python code for the masterdata datamodel based on the entities existing in an
    openBIS instance.
    """

    def __init__(self, url: str = environ("OPENBIS_URL")):
        start_time = time.time()
        # * This part takes some time due to the loading of all entities from Openbis
        self.properties = OpenbisEntities(url=url).get_property_dict()
        self.collections = OpenbisEntities(url=url).get_collection_dict()
        self.datasets = OpenbisEntities(url=url).get_dataset_dict()
        self.objects = OpenbisEntities(url=url).get_object_dict()
        self.vocabularies = OpenbisEntities(url=url).get_vocabulary_dict()
        elapsed_time = time.time() - start_time
        click.echo(
            f"Loaded OpenBIS entities in `MasterdataCodeGenerator` initialization {elapsed_time:.2f} seconds\n"
        )

    def _format_class_name(self, code: str) -> str:
        """
        Format the class name based on the `code` of the entity to follow Python snake case conventions.

        Args:
            code (str): The code of the entity.

        Returns:
            str: The formatted class name.
        """
        if "." in code:
            code = code.split(".")[-1]
        return code.title().replace("_", "").replace("$", "")

    def determine_parent_class(
        self, code: str, class_names: dict, default: str, lines: list
    ) -> tuple:
        """
        Determine the parent class information of the entity based on its `code`. It returns
        the `parent_code` and `parent class`, as well as the `class_name` of the entity. The
        class will inherit from `parent_class`.

        If the parent class does not exist, a note is added to the `lines` list for debugging purposes.

        Args:
            code (str): The code of the entity.
            class_names (dict): A dictionary with the class names of the entities.
            default (str): The default parent class if the parent class does not exist.
            lines (list): A list of strings to be printed to the Python module.

        Returns:
            tuple: The parent code, parent class, and class name of the entity.
        """
        parent_code = ""
        if "." in code:
            parent_code = code.rsplit(".", 1)[0]
        parent_class = class_names.get(parent_code, default)

        # Format class name
        class_name = self._format_class_name(code)
        class_names[code] = class_name

        # If the parent class does not exist but the `code` shows some inheritance, we add a note for debugging
        if parent_code and parent_class == default:
            lines.append(
                f"# ! The parent class of {class_name} is not defined (missing {parent_class})"
            )

        return parent_code, parent_class, class_name

    def add_properties(
        self, entities: dict, parent_code: str, data: dict, lines: list
    ) -> None:
        """
        Add the properties of the entity to the `lines` list. The properties are added as
        `PropertyTypeAssignment` objects.

        Args:
            entities (dict): The dictionary of entities (objects, collections, datasets, vocabularies).
            parent_code (code): The code of the parent class.
            data (dict): The data information for the entity as obtained from openBIS.
            lines (list): A list of strings to be printed to the Python module.
        """
        parent_properties = entities.get(parent_code, {}).get("properties", {}).keys()
        for prop_code, prop_data in data.get("properties", {}).items():
            # Skip "UNKNOWN" properties
            if prop_code == "UNKNOWN":
                continue

            # We check if the property is inherited from the parent class
            if prop_code in parent_properties:
                continue

            prop_name = prop_code.lstrip("$").replace(".", "_").lower()
            lines.append(f"    {prop_name} = PropertyTypeAssignment(")
            lines.append(f'        code="{prop_code}",')
            # ! patching dataType=SAMPLE instead of OBJECT
            if prop_data.get("dataType", "") == "SAMPLE":
                prop_data["dataType"] = "OBJECT"
            lines.append(f"        data_type=\"{prop_data.get('dataType', '')}\",")
            property_label = (prop_data.get("label") or "").replace("\n", "\\n")
            lines.append(f'        property_label="{property_label}",')
            description = (
                (prop_data.get("description") or "")
                .replace('"', "`")
                .replace("\n", "\\n")
                .replace("'", "`")
            )
            lines.append(f'        description="""{description}""",')
            lines.append(f"        mandatory={prop_data.get('mandatory', False)},")
            lines.append(
                f"        show_in_edit_views={prop_data.get('show_in_edit_views', False)},"
            )
            section = (
                (prop_data.get("section") or "")
                .replace('"', '\\"')
                .replace("\n", "\\n")
                .replace("'", "\\'")
            )
            lines.append(f'        section="{section}",')
            lines.append("    )")
            lines.append("")

    def generate_property_types(self) -> str:
        """
        Generate Python code for the property types in the Openbis datamodel. The code is generated
        as a string which is then printed out to the specific Python module in `bam_masterdata/datamodel/property_types.py`.

        Returns:
            str: Python code for the property types.
        """
        lines = []

        # Add imports at the top
        lines.append("from bam_masterdata.metadata.definitions import PropertyTypeDef")
        lines.append("")

        # Process each property type
        for code, data in self.properties.items():
            # Skip the "UNKNOWN" object type
            if code == "UNKNOWN":
                continue

            # Format class name
            class_name = self._format_class_name(code)

            # Add class definition
            lines.append(f"{class_name} = PropertyTypeDef(")
            lines.append(f'    code="{code}",')
            description = (
                (data.get("description") or "")
                .replace('"', "`")
                .replace("\n", "\\n")
                .replace("'", "`")
            )
            lines.append(f'    description="""{description}""",')
            # ! patching dataType=SAMPLE instead of OBJECT
            if data.get("dataType", "") == "SAMPLE":
                data["dataType"] = "OBJECT"
            lines.append(f"    data_type=\"{data.get('dataType', '')}\",")
            property_label = (
                (data.get("label") or "").replace('"', '\\"').replace("\n", "\\n")
            )
            lines.append(f'    property_label="{property_label}",')
            lines.append(")")
            lines.append("")

            # Add newline between classes
            lines.append("")

        return "\n".join(lines)

    def generate_collection_types(self) -> str:
        """
        Generate Python code for the collection types in the Openbis datamodel. The code is generated
        as a string which is then printed out to the specific Python module in `bam_masterdata/datamodel/collection_types.py`.

        Returns:
            str: Python code for the collection types.
        """
        lines = []
        class_names: dict = {}

        # Add imports at the top
        lines.append(
            "from bam_masterdata.metadata.definitions import CollectionTypeDef, PropertyTypeAssignment"
        )
        lines.append("from bam_masterdata.metadata.entities import CollectionType")
        lines.append("")
        lines.append("")

        # Process each collection type
        for code, data in self.collections.items():
            # Skip the "UNKNOWN" object type
            if code == "UNKNOWN":
                continue

            # Determine parent class
            parent_code, parent_class, class_name = self.determine_parent_class(
                code=code,
                class_names=class_names,
                default="CollectionType",
                lines=lines,
            )

            # Add class definition
            lines.append(f"class {class_name}({parent_class}):")
            lines.append("    defs = CollectionTypeDef(")
            lines.append(f'        code="{code}",')
            description = (
                (data.get("description") or "")
                .replace('"', "`")
                .replace("\n", "\\n")
                .replace("'", "`")
            )
            lines.append(f'        description="""{description}""",')
            if data.get("validationPlugin") != "":
                lines.append(
                    f"        validation_script=\"{data.get('validationPlugin')}\","
                )
            lines.append("    )")
            lines.append("")

            # Add properties
            self.add_properties(self.collections, parent_code, data, lines)
            # Add newline between classes
            lines.append("")

        return "\n".join(lines)

    def generate_dataset_types(self) -> str:
        """
        Generate Python code for the dataset types in the Openbis datamodel. The code is generated
        as a string which is then printed out to the specific Python module in `bam_masterdata/datamodel/dataset_types.py`.

        Returns:
            str: Python code for the dataset types.
        """
        lines = []
        class_names: dict = {}

        # Add imports at the top
        lines.append(
            "from bam_masterdata.metadata.definitions import DatasetTypeDef, PropertyTypeAssignment"
        )
        lines.append("from bam_masterdata.metadata.entities import DatasetType")
        lines.append("")
        lines.append("")

        # Process each dataset type
        for code, data in self.datasets.items():
            # Skip the "UNKNOWN" object type
            if code == "UNKNOWN":
                continue

            # Determine parent class
            parent_code, parent_class, class_name = self.determine_parent_class(
                code=code, class_names=class_names, default="DatasetType", lines=lines
            )

            # Add class definition
            lines.append(f"class {class_name}({parent_class}):")
            lines.append("    defs = DatasetTypeDef(")
            lines.append(f'        code="{code}",')
            description = (
                (data.get("description") or "")
                .replace('"', "`")
                .replace("\n", "\\n")
                .replace("'", "`")
            )
            lines.append(f'        description="""{description}""",')
            lines.append("    )")
            lines.append("")

            # Add properties
            self.add_properties(self.datasets, parent_code, data, lines)
            # Add newline between classes
            lines.append("")

        return "\n".join(lines)

    def generate_object_types(self) -> str:
        """
        Generate Python code for the object types in the Openbis datamodel. The code is generated
        as a string which is then printed out to the specific Python module in `bam_masterdata/datamodel/object_types.py`.

        Returns:
            str: Python code for the object types.
        """
        lines = []
        class_names: dict = {}

        # Add imports at the top
        lines.append(
            "from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment"
        )
        lines.append("from bam_masterdata.metadata.entities import ObjectType")
        lines.append("")
        lines.append("")

        # Process each object type
        for code, data in self.objects.items():
            # Skip the "UNKNOWN" object type
            if code == "UNKNOWN":
                continue

            # Determine parent class
            parent_code, parent_class, class_name = self.determine_parent_class(
                code=code, class_names=class_names, default="ObjectType", lines=lines
            )

            # Add class definition
            lines.append(f"class {class_name}({parent_class}):")
            lines.append("    defs = ObjectTypeDef(")
            lines.append(f'        code="{code}",')
            description = (
                (data.get("description") or "")
                .replace('"', "`")
                .replace("\n", "\\n")
                .replace("'", "`")
            )
            lines.append(f'        description="""{description}""",')
            lines.append(
                f"        generated_code_prefix=\"{data.get('generatedCodePrefix', '')}\","
            )
            lines.append("    )")
            lines.append("")

            # Add properties
            self.add_properties(self.objects, parent_code, data, lines)
            # Add newline between classes
            lines.append("")

        return "\n".join(lines)

    def generate_vocabulary_types(self) -> str:
        """
        Generate Python code for the vocabulary types in the Openbis datamodel. The code is generated
        as a string which is then printed out to the specific Python module in `bam_masterdata/datamodel/vocabulary_types.py`.

        Returns:
            str: Python code for the vocabulary types.
        """
        lines = []
        class_names: dict = {}

        # Add imports at the top
        lines.append(
            "from bam_masterdata.metadata.definitions import VocabularyTerm, VocabularyTypeDef"
        )
        lines.append("from bam_masterdata.metadata.entities import VocabularyType")
        lines.append("")
        lines.append("")

        # Process each object type
        for code, data in self.vocabularies.items():
            # Skip the "UNKNOWN" object type
            if code == "UNKNOWN":
                continue

            # Determine parent class
            parent_code, parent_class, class_name = self.determine_parent_class(
                code=code,
                class_names=class_names,
                default="VocabularyType",
                lines=lines,
            )

            # Add class definition
            lines.append(f"class {class_name}({parent_class}):")
            lines.append("    defs = VocabularyTypeDef(")
            lines.append(f'        code="{code}",')
            description = (
                (data.get("description") or "")
                .replace('"', "`")
                .replace("\n", "\\n")
                .replace("'", "`")
            )
            lines.append(f'        description="""{description}""",')
            lines.append("    )")
            lines.append("")

            # Add terms
            parent_terms = self.objects.get(parent_code, {}).get("terms", {}).keys()
            for term_code, term_data in data.get("terms", {}).items():
                # Skip "UNKNOWN" properties
                if term_code == "UNKNOWN":
                    continue

                # We check if the term is inherited from the parent class
                if term_code in parent_terms:
                    continue

                term_name = (
                    term_code.lstrip("$").replace(".", "_").replace("-", "_").lower()
                )
                if term_name[0].isdigit():
                    term_name = f"_{term_name}"
                if term_name == "l":
                    term_name = "L"
                if term_name == "O":
                    term_name = "o"
                if term_name == "I":
                    term_name = "i"
                lines.append(f"    {term_name} = VocabularyTerm(")
                lines.append(f'        code="{term_code}",')
                label = (term_data.get("label") or "").replace('"', "")
                lines.append(f'        label="{label}",')
                description = (
                    (term_data.get("description") or "")
                    .replace('"', "`")
                    .replace("\n", "\\n")
                    .replace("'", "`")
                )
                lines.append(f'        description="""{description}""",')
                lines.append("    )")
                lines.append("")

            # Add newline between classes
            lines.append("")

        return "\n".join(lines)
