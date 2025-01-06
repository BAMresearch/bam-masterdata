import os
from pathlib import Path

from get_entities import (
    get_collection_dict,
    get_dataset_dict,
    get_object_dict,
    get_property_dict,
    get_vocabulary_dict,
)

object_types_dict = get_object_dict()
collection_types_dict = get_collection_dict()
dataset_types_dict = get_dataset_dict()
property_types_dict = get_property_dict()
vocabulary_types_dict = get_vocabulary_dict()

# Generate the object_types Python file content
def generate_object_types_code(object_types_dict):
    lines = []
    class_names = {}

    def format_class_name(code):
        return code.split(".")[-1].title().replace("_", "")

    # Add imports at the top
    lines.append("from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment")
    lines.append("from bam_masterdata.metadata.entities import ObjectType")
    lines.append("")
    lines.append("")

    # Process each object type
    for code, data in object_types_dict.items():
        # Skip the "UNKNOWN" object type
        if code == "UNKNOWN":
            continue
        
        # Determine parent class
        if "." in code:
            parent_code = code.rsplit(".", 1)[0]
            parent_class = class_names.get(parent_code, "ObjectType")
        else:
            parent_class = "ObjectType"

        # Format class name
        class_name = format_class_name(code)
        class_names[code] = class_name

        # Add class definition
        lines.append(f"class {class_name}({parent_class}):")
        lines.append("    defs = ObjectTypeDef(")
        lines.append(f"        code='{code}',")
        description = (data.get('description') or '').replace('"', '\\"').replace("\n", "\\n")
        lines.append(f"        description=\"{description}\",")
        lines.append(f"        generated_code_prefix='{data.get('generatedCodePrefix', '')}',")
        lines.append("    )")
        lines.append("")

        # Add properties
        for prop_code, prop_data in data.get("properties", {}).items():
            # Skip "UNKNOWN" properties
            if prop_code == "UNKNOWN":
                continue
            
            prop_name = prop_code.lstrip("$").replace(".", "_").lower()
            lines.append(f"    {prop_name} = PropertyTypeAssignment(")
            lines.append(f"        code='{prop_code}',")
            lines.append(f"        data_type='{prop_data.get('dataType', '')}',")
            property_label = (prop_data.get('label') or '').replace('"', '\\"').replace("\n", "\\n")
            lines.append(f"        property_label=\"{property_label}\",")
            description = (prop_data.get('description') or '').replace('"', '\\"').replace("\n", "\\n")
            lines.append(f"        description=\"{description}\",")
            lines.append(f"        mandatory={prop_data.get('mandatory', False)},")
            lines.append(f"        show_in_edit_views={prop_data.get('show_in_edit_views', False)},")
            section = (prop_data.get('section') or '').replace('"', '\\"').replace("\n", "\\n")
            lines.append(f"        section=\"{section}\",")
            lines.append("    )")
            lines.append("")

        # Add newline between classes
        lines.append("")

    return "\n".join(lines)


# Generate the collection_types Python file content
def generate_collection_types_code(collection_types_dict):
    lines = []

    def format_class_name(code):
        return code.title().replace("_", "")

    # Add imports at the top
    lines.append("from bam_masterdata.metadata.definitions import CollectionTypeDef")
    lines.append("from bam_masterdata.metadata.entities import CollectionType")
    lines.append("")
    lines.append("")

    # Process each collection type
    for code, data in collection_types_dict.items():
        # Skip the "UNKNOWN" object type
        if code == "UNKNOWN":
            continue
        
        class_name = format_class_name(code)

        # Add class definition
        lines.append(f"class {class_name}(CollectionType):")
        lines.append("    defs = CollectionTypeDef(")
        lines.append(f"        code='{code}',")
        description = (data.get('description') or '').replace('"', '\\"').replace("\n", "\\n")
        lines.append(f"        description=\"{description}\",")
        if data.get('validationPlugin') != '':
            lines.append(f"        validation_script='{data.get('validationPlugin')}',")
        lines.append("    )")
        lines.append("")

        # Add newline between classes
        lines.append("")

    return "\n".join(lines)

# Generate the property_types Python file content
def generate_property_types_code(property_types_dict):
    lines = []
    class_names = {}

    def format_class_name(code):
        return code.split(".")[-1].title().replace("_", "").replace("$", "")

    # Add imports at the top
    lines.append("from bam_masterdata.metadata.definitions import PropertyTypeDef")
    lines.append("")

    # Process each property type
    for code, data in property_types_dict.items():
        # Skip the "UNKNOWN" object type
        if code == "UNKNOWN":
            continue

        # Format class name
        class_name = format_class_name(code)
        class_names[code] = class_name

        # Add class definition
        lines.append(f"{class_name} = PropertyTypeDef(")
        lines.append(f"    code='{code}',")
        description = (data.get('description') or '').replace('"', '\\"').replace("\n", "\\n")
        lines.append(f"    description=\"{description}\",")
        lines.append(f"    data_type='{data.get('dataType', '')}',")
        property_label = (data.get('label') or '').replace('"', '\\"').replace("\n", "\\n")
        lines.append(f"    property_label=\"{property_label}\",")
        lines.append(")")
        lines.append("")

        # Add newline between classes
        lines.append("")

    return "\n".join(lines)

# Generate the dataset_types Python file content
def generate_dataset_types_code(dataset_types_dict):
    lines = []

    def format_class_name(code):
        return code.title().replace("_", "")

    # Add imports at the top
    lines.append("from pydantic import BaseModel")
    lines.append("")
    lines.append("from bam_masterdata.metadata.definitions import DatasetTypeDef")
    lines.append("")
    lines.append("")

    # Process each dataset type
    for code, data in dataset_types_dict.items():
        # Skip the "UNKNOWN" object type
        if code == "UNKNOWN":
            continue
        
        class_name = format_class_name(code)

        # Add class definition
        lines.append(f"class {class_name}(BaseModel):")
        lines.append("    defs = DatasetTypeDef(")
        lines.append(f"        code='{code}',")
        description = (data.get('description') or '').replace('"', '\\"').replace("\n", "\\n")
        lines.append(f"        description=\"{description}\",")
        lines.append("    )")
        lines.append("")

        # Add newline between classes
        lines.append("")

    return "\n".join(lines)

# Generate the object_types Python file content
def generate_vocabulary_types_code(vocabularies_dict):
    lines = []
    class_names = {}

    def format_class_name(code):
        return code.split(".")[-1].title().replace("_", "").replace("$", "")

    # Add imports at the top
    lines.append("from bam_masterdata.metadata.definitions import VocabularyTerm, VocabularyTypeDef")
    lines.append("from bam_masterdata.metadata.entities import VocabularyType")
    lines.append("")
    lines.append("")

    # Process each object type
    for code, data in vocabularies_dict.items():
        # Skip the "UNKNOWN" object type
        if code == "UNKNOWN":
            continue
        
        # Determine parent class
        if "." in code:
            parent_code = code.rsplit(".", 1)[0]
            parent_class = class_names.get(parent_code, "VocabularyType")
        else:
            parent_class = "VocabularyType"

        # Format class name
        class_name = format_class_name(code)
        class_names[code] = class_name

        # Add class definition
        lines.append(f"class {class_name}({parent_class}):") 
        lines.append("    defs = VocabularyTypeDef(")
        lines.append(f"        code='{code}',")
        description = (data.get('description') or '').replace('"', '\\"').replace("\n", "\\n")
        lines.append(f"        description=\"{description}\",")
        lines.append("    )")
        lines.append("")

        # Add terms
        for term_code, term_data in data.get("terms", {}).items():
            # Skip "UNKNOWN" properties
            if term_code == "UNKNOWN":
                continue
            
            term_name = term_code.lstrip("$").replace(".", "_").replace("-", "_").lower()
            if term_name[0].isdigit():
                term_name = f"_{term_name}"
            if term_name == 'l':
                term_name = "L"
            if term_name == 'O':
                term_name = "o"
            if term_name == 'I':
                term_name = "i"
            lines.append(f"    {term_name} = VocabularyTerm(")
            lines.append(f"        code='{term_code}',")
            lines.append(f"        label='{term_data.get('label', '')}',")
            lines.append(f"        description='{term_data.get('description', '')}',")
            lines.append("    )")
            lines.append("")

        # Add newline between classes
        lines.append("")

    return "\n".join(lines)

output_dir = os.path.join('.', 'bam_masterdata', 'datamodel')
for module_name in ['object', 'collection', 'dataset', 'property', 'vocabulary']:
    output_file = Path(os.path.join(output_dir, f'{module_name}_types.py'))
    # here all the logic calling for each specific function
    function_name = f'generate_{module_name}_types_code'
    if function_name in globals():
         entity_dict = globals()[f'{module_name}_types_dict']
         code = globals()[function_name](entity_dict)
         output_file.write_text(code, encoding='utf-8')
         print(f"Generated {module_name} types in:")
         print(output_file)

# # Set output files
# output_dir = Path(__file__).resolve().parent.parent / "bam_masterdata" / "datamodel"
# output_file_obj = output_dir / "object_types.py"
# output_file_coll = output_dir / "collection_types.py"
# output_file_dataset = output_dir / "dataset_types.py"
# output_file_property = output_dir / "property_types.py"
# output_file_vocab = output_dir / "vocabulary_types.py"

# # Generate the object_types code
# object_types_code = generate_object_types_code(object_types_dict)

# # Write to file
# output_file_obj.write_text(object_types_code)

# print("Generated object_types.py in:")
# print(output_file_obj)

# # Generate the collection_types code
# collection_types_code = generate_collection_types_code(collection_types_dict)

# output_file_coll.write_text(collection_types_code)

# print("Generated collection_types.py:")
# print(output_file_coll)

# # Generate the dataset_types code
# dataset_types_code = generate_dataset_types_code(dataset_types_dict)

# output_file_dataset.write_text(dataset_types_code)

# print("Generated dataset_types.py:")
# print(output_file_dataset)

# # Generate the property_types code
# property_types_code = generate_property_types_code(property_types_dict)

# output_file_property.write_text(property_types_code)

# print("Generated property_types.py:")
# print(output_file_property)

# # Generate the vocabularies code
# vocabularies_code = generate_vocabularies_code(vocabularies_dict)

# output_file_vocab.write_text(vocabularies_code, encoding='utf-8')

# print("Generated vocabulary_types.py:")
# print(output_file_vocab)



