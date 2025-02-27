import json
import os

from bam_masterdata.checker.source_loader import SourceLoader

print(f"Current working directory: {os.getcwd()}")

# Path to the Excel file
excel_path = os.path.abspath("tests/data/checker/masterdata_example.xlsx")

# Path to save the JSON output
output_excel_path = "tests/data/checker/masterdata_excel_output.json"

# Ensure the directory exists
os.makedirs(os.path.dirname(output_excel_path), exist_ok=True)

# Initialize SourceLoader
source_loader_excel = SourceLoader(excel_path)

# Run the load function
result_dict_excel = source_loader_excel.load()

# Save the result as a JSON file
with open(output_excel_path, "w", encoding="utf-8") as excel_file:
    json.dump(result_dict_excel, excel_file, indent=2, ensure_ascii=False)

print(f"Excel JSON file saved at: {output_excel_path}")

# Path to the Python files
python_path = os.path.abspath("tests/data/datamodel_test/")

# Path to save the JSON output
output_python_path = "tests/data/checker/masterdata_python_output.json"

# Initialize SourceLoader
source_loader_python = SourceLoader(python_path)

# Run the load function
result_dict_python = source_loader_python.load()

# Save the result as a JSON file
with open(output_python_path, "w", encoding="utf-8") as python_file:
    json.dump(result_dict_python, python_file, indent=2, ensure_ascii=False)

print(f"Python JSON file saved at: {output_python_path}")
