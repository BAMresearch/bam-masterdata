import os
import time
from pathlib import Path

from bam_masterdata.openbis import OpenbisEntities


class MasterdataCodeGenerator:
    """
    Class to generate Python code for the masterdata datamodel based on the entities existing in an
    openBIS instance.
    """

    def __init__(self):
        start_time = time.time()
        # * This part takes some time due to the loading of all entities from Openbis
        self.objects = OpenbisEntities().get_object_dict()
        self.collections = OpenbisEntities().get_collection_dict()
        self.datasets = OpenbisEntities().get_dataset_dict()
        self.properties = OpenbisEntities().get_property_dict()
        self.vocabularies = OpenbisEntities().get_vocabulary_dict()
        elapsed_time = time.time() - start_time
        print(
            f"Loaded OpenBIS entities in `MasterdataCodeGenerator` initialization {elapsed_time:.2f} seconds\n"
        )

    def _format_class_name(self, code: str) -> str:
        if "." in code:
            code = code.split(".")[-1]
        return code.title().replace("_", "").replace("$", "")

    def determine_parent_class(
        self, code: str, class_names: dict, default: str, lines: list
    ) -> tuple:
        # Determine parent class
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

    def generate_object_types(self) -> str:
        """
        Generate Python code for the object types in the Openbis datamodel. The code is generated
        as a string which is then printed out to the specific Python module in `bam_masterdata/datamodel/object_types.py`.

        Returns:
            str: Python code for the object types.
        """
        lines = []
        class_names = {}

        def format_class_name(code):
            return code.split(".")[-1].title().replace("_", "")

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
            parent_properties = (
                self.objects.get(parent_code, {}).get("properties", {}).keys()
            )
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

        # Add imports at the top
        lines.append(
            "from bam_masterdata.metadata.definitions import CollectionTypeDef"
        )
        lines.append("from bam_masterdata.metadata.entities import CollectionType")
        lines.append("")
        lines.append("")

        # Process each collection type
        for code, data in self.collections.items():
            # Skip the "UNKNOWN" object type
            if code == "UNKNOWN":
                continue

            class_name = self._format_class_name(code)

            # Add class definition
            lines.append(f"class {class_name}(CollectionType):")
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

            # Add newline between classes
            lines.append("")

        return "\n".join(lines)

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

    def generate_dataset_types(self) -> str:
        """
        Generate Python code for the dataset types in the Openbis datamodel. The code is generated
        as a string which is then printed out to the specific Python module in `bam_masterdata/datamodel/dataset_types.py`.

        Returns:
            str: Python code for the dataset types.
        """
        lines = []
        class_names = {}

        # Add imports at the top
        lines.append("from bam_masterdata.metadata.definitions import DataSetTypeDef")
        lines.append("from bam_masterdata.metadata.entities import DatasetType")
        lines.append("")
        lines.append("")

        # Process each dataset type
        for code, data in self.datasets.items():
            # Skip the "UNKNOWN" object type
            if code == "UNKNOWN":
                continue

            # Determine parent class
            _, parent_class, class_name = self.determine_parent_class(
                code=code, class_names=class_names, default="DatasetType", lines=lines
            )

            # Add class definition
            lines.append(f"class {class_name}({parent_class}):")
            lines.append("    defs = DataSetTypeDef(")
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
        class_names = {}

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
                lines.append(
                    f"        label=\"{(term_data.get('label') or '').replace('\"', '')}\","
                )
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


if __name__ == "__main__":
    start_time = time.time()

    # ! this takes a lot of time loading all the entities in Openbis
    generator = MasterdataCodeGenerator()

    # Add each module to the `bam_masterdata/datamodel` directory
    output_dir = os.path.join(".", "bam_masterdata", "datamodel")
    for module_name in ["object", "collection", "dataset", "property", "vocabulary"]:
        module_start_time = time.perf_counter()  # more precise time measurement
        output_file = Path(os.path.join(output_dir, f"{module_name}_types.py"))

        # Get the method from `MasterdataCodeGenerator`
        code = getattr(generator, f"generate_{module_name}_types")()
        code = code.rstrip("\n") + "\n"
        output_file.write_text(code, encoding="utf-8")
        module_elapsed_time = time.perf_counter() - module_start_time
        print(
            f"Generated {module_name} types in {module_elapsed_time:.2f} seconds in {output_file}\n"
        )

    elapsed_time = time.time() - start_time
    print(f"Generated all types in {elapsed_time:.2f} seconds")
