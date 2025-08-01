"""
This module contains the maps for the metadata entities from their labels in this package to the
ones in openBIS when using PyBIS.
Last update: 2025-04-01
"""

COLLECTION_TYPE_MAP = {
    "code": "code",
    "description": "description",
    "validation_script": "validationPlugin",
}

DATASET_TYPE_MAP = {
    "code": "code",
    "description": "description",
    "validation_script": "validationPlugin",
    "main_dataset_pattern": "mainDataSetPattern",
    "main_dataset_path": "mainDataSetPath",
}

OBJECT_TYPE_MAP = {
    "code": "code",
    "description": "description",
    "validation_script": "validationPlugin",
    "generated_code_prefix": "generatedCodePrefix",
    "auto_generate_codes": "autoGeneratedCodes",
}

VOCABULARY_TYPE_MAP = {
    "code": "code",
    "description": "description",
    "url_template": "",
}
