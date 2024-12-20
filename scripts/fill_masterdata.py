from pathlib import Path

from fill_obj_types import get_obj_dict

object_types_dict = get_obj_dict()

# Generate the Python file content
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

# Generate the code
object_types_code = generate_object_types_code(object_types_dict)

# Write to file
output_dir = Path(__file__).resolve().parent.parent / "bam_masterdata" / "datamodel"
output_file = output_dir / "object_types.py"
output_file.write_text(object_types_code)

print("Generated object_types.py:")
print(object_types_code)
