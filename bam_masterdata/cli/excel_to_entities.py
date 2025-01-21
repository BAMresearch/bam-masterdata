import re
from typing import TYPE_CHECKING, Any

# import logger
import openpyxl

# logger = logger()


def index_to_excel_column(index):
    column = ""
    while index > 0:
        index, remainder = divmod(index - 1, 26)
        column = chr(65 + remainder) + column
    return column


def get_last_non_empty_row(sheet, start_index):
    """
    Finds the last non-empty row before encountering a completely empty row.

    Args:
        sheet: The worksheet object.
        start_index: The row number to start checking from (1-based index).

    Returns:
        The row number of the last non-empty row before an empty row is encountered,
        or None if no non-empty rows are found starting from the given index.
    """
    last_non_empty_row = None

    for row in range(start_index, sheet.max_row + 1):
        # Check if the entire row is empty
        if all(sheet.cell(row=row, column=col).value in (None, '') for col in range(1, sheet.max_column + 1)):
            return last_non_empty_row  # Return the last non-empty row before the current empty row
        
        last_non_empty_row = row  # Update the last non-empty row

    return last_non_empty_row  # If no empty row is encountered, return the last non-empty row


def properties_to_dict(sheet, start_index_row, last_non_empty_row):
    property_dict = {}
    expected_terms = [
        "Code",
        "Description",
        "Mandatory",
        "Show in edit views",
        "Section",
        "Property label",
        "Data type",
        "Vocabulary code",
    ]

    header_index = start_index_row + 3
    row_headers = [cell.value for cell in sheet[header_index]]

    #print("Header index:", header_index, "//Header:", row_headers)
    #code_index = row_headers.index("Code") + 1
    (
        codes,
        descriptions,
        mandatories,
        shows,
        sections,
        labels,
        data_types,
        vocabulary_codes,
    ) = [], [], [], [], [], [], [], []

    for term in expected_terms:
        if term not in row_headers:
            if term in ("Mandatory", "Show in edit views", "Section"):
                print(f"Warning: '{term}' not found in the properties headers.")
            else:
                print(f"Error: '{term}' not found in the properties headers.")
        else:
            # Find the index of the term in the row
            term_index = row_headers.index(term) + 1
            term_letter = index_to_excel_column(term_index)
            # print(term_index)

            # Check the column below "Code"
            if term == "Code":
                for cell in sheet[term_letter][header_index:last_non_empty_row]:
                    if cell.value is not None:
                        codes.append(cell.value)
                    else:
                        codes.append(None)
                invalid_codes = [
                    i + 5
                    for i, cell in enumerate(codes)
                    if not re.match(r"^\$?[A-Z0-9_.]+$", str(cell))
                ]
                if invalid_codes:
                    # Append an error indicating the positions (row numbers) with invalid values for the current term
                    print(
                        f"Error: Invalid code found in the '{term}' column at row(s): {', '.join(map(str, invalid_codes))}"
                    )

            # Check the cell below "Description"
            elif term == "Description":
                for cell in sheet[term_letter][header_index:last_non_empty_row]:
                    if cell.value is not None:
                        descriptions.append(cell.value)
                    else:
                        descriptions.append("")
                invalid_descriptions = [
                    i + 5
                    for i, cell in enumerate(descriptions)
                    if not re.match(r".*//.*", str(cell))
                ]
                if invalid_descriptions:
                    print(
                        f"Error: Invalid value(s) found in the '{term}' column at row(s): {', '.join(map(str, invalid_descriptions))}. Description should follow the schema: English Description + '//' + German Description."
                    )

            # Check the cell below "Mandatory"
            elif term == "Mandatory":
                for cell in sheet[term_letter][header_index:last_non_empty_row]:
                    if cell.value is not None:
                        mandatories.append(str(cell.value).upper())
                    else:
                        mandatories.append(False)
                invalid_mandatory = [
                    i + 5
                    for i, cell in enumerate(mandatories)
                    if cell not in ["TRUE", "FALSE"]
                ]
                if invalid_mandatory:
                    print(
                        f"Error: Invalid value found in the '{term}' column at row(s): {', '.join(map(str, invalid_mandatory))}. Accepted values: TRUE, FALSE"
                    )

            # Check the cell below "Show in edit views"
            elif term == "Show in edit views":
                for cell in sheet[term_letter][header_index:last_non_empty_row]:
                    if cell.value is not None:
                        shows.append(str(cell.value).upper())
                    else:
                        shows.append(False)
                invalid_show = [
                    i + 5
                    for i, cell in enumerate(shows)
                    if cell not in ["TRUE", "FALSE"]
                ]
                if invalid_show:
                    print(
                        f"Error: Invalid value found in the '{term}' column at row(s): {', '.join(map(str, invalid_show))}. Accepted values: TRUE, FALSE"
                    )

            # Check the cell below "Section"
            elif term == "Section":
                for cell in sheet[term_letter][header_index:last_non_empty_row]:
                    if cell.value is not None:
                        sections.append(cell.value)
                    else:
                        sections.append("")
                invalid_section = [
                    i + 5
                    for i, cell in enumerate(sections)
                    if not re.match(r".*", str(cell))
                ]
                if invalid_section:
                    print(
                        f"Error: Invalid value found in the '{term}' column at row(s): {', '.join(map(str, invalid_section))}. Specify the section as text format"
                    )

            # Check the cell below "Property label"
            elif term == "Property label":
                for cell in sheet[term_letter][header_index:last_non_empty_row]:
                    if cell.value is not None:
                        labels.append(cell.value)
                    else:
                        labels.append("")
                invalid_label = [
                    i + 5
                    for i, cell in enumerate(labels)
                    if not re.match(r".*", str(cell))
                ]
                if invalid_label:
                    print(
                        f"Error: Invalid value found in the '{term}' column at row(s): {', '.join(map(str, invalid_label))}. Specify the property label as text format"
                    )

            # Check the cell below "Data type"
            elif term == "Data type":
                for cell in sheet[term_letter][header_index:last_non_empty_row]:
                    if cell.value is not None:
                        data_types.append(str(cell.value).upper())
                    else:
                        data_types.append("")
                invalid_type = [
                    i + 5
                    for i, cell in enumerate(data_types)
                    if cell
                    not in [
                        "INTEGER",
                        "REAL",
                        "VARCHAR",
                        "MULTILINE_VARCHAR",
                        "HYPERLINK",
                        "BOOLEAN",
                        "CONTROLLEDVOCABULARY",
                        "XML",
                        "TIMESTAMP",
                        "DATE",
                        "SAMPLE",
                    ]
                ]
                if invalid_type:
                    print(
                        f"Error: Invalid value found in the '{term}' column at row(s): {', '.join(map(str, invalid_type))}. Accepted types: INTEGER, REAL, VARCHAR, MULTILINE_VARCHAR, HYPERLINK, BOOLEAN, CONTROLLEDVOCABULARY, XML, TIMESTAMP, DATE, SAMPLE"
                    )

            # Check the column below "Vocabulary code"
            elif term == "Vocabulary code":
                for cell in sheet[term_letter][header_index:last_non_empty_row]:
                    if cell.value is not None:
                        vocabulary_codes.append(str(cell.value).upper())
                    else:
                        vocabulary_codes.append("")
                invalid_vocab = [
                    i + 5
                    for i, cell in enumerate(vocabulary_codes)
                    if cell and not re.match(r"^\$?[A-Z0-9_.]+$", str(cell))
                ]
                if invalid_vocab:
                    # Append an error indicating the positions (row numbers) with invalid values for the current term
                    print(
                        f"Error: Invalid vocabulary code found in the '{term}' column at row(s): {', '.join(map(str, invalid_vocab))}"
                    )

    for i in range(0, len(codes)):
        property_dict[codes[i]] = {
            "permId": codes[i],
            "code": codes[i],
            "section": sections[i],
            "mandatory": mandatories[i],
            "show_in_edit_views": shows[i],
            "label": labels[i],
            "dataType": data_types[i],
            "vocabularyCode": vocabulary_codes[i],
        }

    return property_dict, last_non_empty_row


def block_to_entity_dict(sheet, start_index_row, last_non_empty_row, complete_dict):
    attributes_dict = {}

    entity_type_position = f"A{start_index_row}"
    entity_type = sheet[entity_type_position].value

    entity_types = [
        "OBJECT_TYPE",
        "SAMPLE_TYPE",
        "EXPERIMENT_TYPE",
        "DATASET_TYPE",
        "PROPERTY_TYPE",
        "VOCABULARY_TYPE",
    ]

    header_terms = [cell.value for cell in sheet[start_index_row+1]]

    if entity_type not in entity_types:
        print(
            "The entity type (cell A1) should be one of the following: SAMPLE_TYPE/OBJECT_TYPE, EXPERIMENT_TYPE/COLLECTION_TYPE, DATASET_TYPE, PROPERTY_TYPE, VOCABULARY_TYPE"
        )
        # return "\n".join(errors)
    else:
        if entity_type == "SAMPLE_TYPE" or entity_type == "OBJECT_TYPE":
            expected_terms = [
                "Code",
                "Description",
                "Validation script",
                "Generated code prefix",
                "Auto generate codes",
            ]
            
            code_value = ""
            for term in expected_terms:
                if term not in header_terms:
                    # logger.error(f"Error: '{term}' not found in the entity headers.")
                    print(f"Error: '{term}' not found in the entity headers.")
                else:
                    # Find the index of the term in the second row
                    term_index = header_terms.index(term)

                    # Check the cell below "Code"
                    if term == "Code":
                        code_value = sheet.cell(row=start_index_row + 2, column=term_index + 1).value
                        attributes_dict["permId"] = code_value
                        attributes_dict["code"] = code_value
                        # if cell_below_code.value != code:
                        # logger.error("Error: The code should be the same one indicated in the file name")

                    # Check the cell below "Description"
                    elif term == "Description":
                        description_value = sheet.cell(
                            row=start_index_row + 2, column=term_index + 1
                        ).value
                        attributes_dict["description"] = description_value
                        # description_pattern = re.compile(r".*//.*")
                        # if not description_pattern.match(cell_below_description.value):
                        # logger.error("Error: Description should follow the schema: English Description + '//' + German Description.")

                    # Check the cell below "Generated code prefix"
                    elif term == "Generated code prefix":
                        generated_code_value = sheet.cell(
                            row=start_index_row + 2, column=term_index + 1
                        ).value
                        attributes_dict["generatedCodePrefix"] = generated_code_value
                        # if cell_below_generated_code.value not in code:
                        # logger.error("Error: The value of 'Generated code prefix' should be a part of the 'Code'.")

                    # Check the cell below "Validation script"
                    elif term == "Validation script":
                        validation_value = sheet.cell(
                            row=start_index_row + 2, column=term_index + 1
                        ).value
                        attributes_dict["validationPlugin"] = validation_value
                        # validation_pattern = re.compile(r"^[A-Za-z0-9_]+\.py$")
                        # if cell_below_validation.value and not validation_pattern.match(cell_below_validation.value):
                        # logger.error("Error: Validation script should follow the schema: Words and/or numbers separated by '_' and ending in '.py'")

                    # Check the cell below "Auto generate codes"
                    elif term == "Auto generate codes":
                        auto_generate_value = sheet.cell(
                            row=start_index_row + 2, column=term_index + 1
                        ).value
                        attributes_dict["autoGeneratedCode"] = auto_generate_value
                        # if cell_below_auto_generate.value not in ["TRUE", "FALSE"]:
                        # logger.error("Error: Value below 'Auto generate codes' should be 'TRUE' or 'FALSE'.")

            attributes_dict["properties"] = properties_to_dict(sheet, start_index_row, last_non_empty_row)[0]

            complete_dict[code_value] = attributes_dict

            return complete_dict

        elif entity_type == "EXPERIMENT_TYPE" or entity_type == "DATASET_TYPE":
            expected_terms = ["Code", "Description", "Validation script"]
            for term in expected_terms:
                if term not in header_terms:
                    print(f"Error: '{term}' not found in the second row.")
                else:
                    # Find the index of the term in the second row
                    term_index = header_terms.index(term)

                    # Check the cell below "Code"
                    if term == "Code":
                        code_value = sheet.cell(row=start_index_row + 2, column=term_index + 1).value
                        attributes_dict["permId"] = code_value
                        attributes_dict["code"] = code_value
                        # if cell_below_code.value != code:
                        # logger.error("Error: The code should be the same one indicated in the file name")

                    # Check the cell below "Description"
                    elif term == "Description":
                        description_value = sheet.cell(
                            row=start_index_row + 2, column=term_index + 1
                        ).value
                        attributes_dict["description"] = description_value
                        # description_pattern = re.compile(r".*//.*")
                        # if not description_pattern.match(cell_below_description.value):
                        # logger.error("Error: Description should follow the schema: English Description + '//' + German Description.")

                    # Check the cell below "Validation script"
                    elif term == "Validation script":
                        validation_value = sheet.cell(
                            row=start_index_row + 2, column=term_index + 1
                        ).value
                        attributes_dict["validationPlugin"] = validation_value
                        # validation_pattern = re.compile(r"^[A-Za-z0-9_]+\.py$")
                        # if cell_below_validation.value and not validation_pattern.match(cell_below_validation.value):
                        # logger.error("Error: Validation script should follow the schema: Words and/or numbers separated by '_' and ending in '.py'")

            attributes_dict["properties"] = properties_to_dict(sheet, start_index_row, last_non_empty_row)[0]

            complete_dict[code_value] = attributes_dict

            return complete_dict

        elif entity_type == "VOCABULARY_TYPE":
            expected_terms = ["Code", "Description"]
            for term in expected_terms:
                if term not in header_terms:
                    print(f"Error: '{term}' not found in the second row.")
                else:
                    # Find the index of the term in the second row
                    term_index = header_terms.index(term)

                    # Check the cell below "Code"
                    if term == "Code":
                        code_value = sheet.cell(row=start_index_row + 2, column=term_index + 1).value
                        attributes_dict["permId"] = code_value
                        attributes_dict["code"] = code_value
                        # if cell_below_code.value != code:
                        # logger.error("Error: The code should be the same one indicated in the file name")

                    # Check the cell below "Description"
                    elif term == "Description":
                        description_value = sheet.cell(
                            row=start_index_row + 2, column=term_index + 1
                        ).value
                        attributes_dict["description"] = description_value
                        # description_pattern = re.compile(r".*//.*")
                        # if not description_pattern.match(cell_below_description.value):
                        # logger.error("Error: Description should follow the schema: English Description + '//' + German Description.")

            #TBD: vocabulary_terms as properties
            #attributes_dict["terms"] = properties_to_dict(sheet, False)

            complete_dict[code_value] = attributes_dict

            return complete_dict

def excel_to_entities(excel_path, output_directory="./artifacts/tmp/"):
    complete_dict = {}

    workbook = openpyxl.load_workbook(excel_path)

    sheet = workbook.active
    tab_name = sheet.title

    start_row = 1
    while start_row <= sheet.max_row:
        # Find the last non-empty row of the current block
        last_non_empty_row = get_last_non_empty_row(sheet, start_row)

        # Check if we've reached the end of the sheet or found two consecutive empty rows
        if last_non_empty_row is None:
            print(f"End of the current sheet {tab_name} reached. Switching to next sheet...")
            break

        # Process the block (from start_row to last_non_empty_row)
        complete_dict = block_to_entity_dict(sheet, start_row, last_non_empty_row, complete_dict)

        # Add your block processing logic here
        #for row in range(start_row, last_non_empty_row + 1):
        #    # Example: Print the row content
        #    row_values = [sheet.cell(row=row, column=col).value for col in range(1, sheet.max_column + 1)]
        #    print(row_values)

        # Update start_row to the row after the empty row
        start_row = last_non_empty_row + 1
        while start_row <= sheet.max_row and all(
            sheet.cell(row=start_row, column=col).value in (None, '') for col in range(1, sheet.max_column + 1)
        ):
            start_row += 1

        # Check if there are two consecutive empty rows
        if start_row > sheet.max_row or all(
            sheet.cell(row=start_row, column=col).value in (None, '') for col in range(1, sheet.max_column + 1)
        ):
            print("End of the current sheet reached. Switching to next sheet...")
            break
    
    print(complete_dict)

excel_to_entities(
    r"C:\Users\cmadaria\Documents\Projects\BAMresearch\bam-masterdata\artifacts\masterdata.xlsx"
)
