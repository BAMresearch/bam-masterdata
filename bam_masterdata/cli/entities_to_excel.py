import inspect
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from openpyxl.worksheet.worksheet import Worksheet

from bam_masterdata.utils import import_module


def entities_to_excel(
    worksheet: "Worksheet",
    module_path: str,
    definitions_module: Any,
) -> None:
    """
    Export entities to the Excel file. The Python modules are imported using the function `import_module`,
    and their contents are inspected (using `inspect`) to find the classes in the datamodel containing
    `defs` and with a `model_to_json` method defined. Each row is then appended to the `worksheet`.

    Args:
        worksheet (Worksheet): The worksheet to append the entities.
        module_path (str): Path to the Python module file.
        definitions_module (Any): The module containing the definitions of the entities. This is used
            to match the header definitions of the entities.
    """
    def_members = inspect.getmembers(definitions_module, inspect.isclass)
    module = import_module(module_path=module_path)

    # Inspect Python modules and their objects and print them to Excel
    for _, obj in inspect.getmembers(module, inspect.isclass):
        # Ensure the class has the `model_to_json` method
        if not hasattr(obj, "defs") or not callable(getattr(obj, "model_to_json")):
            continue

        obj_instance = obj()

        # Entity title
        obj_definitions = obj_instance.defs
        worksheet.append([obj_definitions.excel_name])

        # Entity header definitions and values
        for def_name, def_cls in def_members:
            if def_name == obj_definitions.name:
                break
        # Appending headers and values in worksheet
        excel_headers = []
        header_values = []
        for field, excel_header in obj_definitions.excel_headers_map.items():
            header_values.append(getattr(obj_definitions, field))
            excel_headers.append(excel_header)
        worksheet.append(excel_headers)
        worksheet.append(header_values)

        # Properties assignment for ObjectType, DatasetType, and CollectionType
        if obj_instance.cls_name in ["ObjectType", "DatasetType", "CollectionType"]:
            if not obj_instance.properties:
                continue
            worksheet.append(
                list(obj_instance.properties[0].excel_headers_map.values())
            )
            for prop in obj_instance.properties:
                row = []
                for field in prop.excel_headers_map.keys():
                    if field == "data_type":
                        val = prop.data_type.value
                    else:
                        val = getattr(prop, field)
                    row.append(val)
                worksheet.append(row)
        # Terms assignment for VocabularyType
        elif obj_instance.cls_name == "VocabularyType":
            if not obj_instance.terms:
                continue
            worksheet.append(list(obj_instance.terms[0].excel_headers_map.values()))
            for term in obj_instance.terms:
                worksheet.append(
                    getattr(term, f_set) for f_set in term.excel_headers_map.keys()
                )
        worksheet.append([""])  # empty row after entity definitions
