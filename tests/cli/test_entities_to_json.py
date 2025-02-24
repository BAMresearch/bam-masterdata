import json
import os
import shutil

import pytest

from bam_masterdata.cli.entities_to_json import entities_to_json
from bam_masterdata.logger import logger


@pytest.mark.parametrize(
    "module_name, entity_code, attr_names",
    [
        ("collection_types", "COLLECTION", ["properties", "defs"]),
        # ('dataset_types', False),  # ! this module does not have classes yet
        ("object_types", "ACTION", ["properties", "defs"]),
        (
            "property_types",
            "$NAME",
            ["code", "description", "property_label", "data_type"],
        ),
        ("vocabulary_types", "$STORAGE_FORMAT", ["terms", "defs"]),
    ],
)
def test_entities_to_json(module_name: str, entity_code: str, attr_names: list[str]):
    """Test the `entities_to_json` function."""
    module_path = os.path.join("./bam_masterdata/datamodel", f"{module_name}.py")

    json_data = entities_to_json(module_path=module_path)
    assert entity_code in json_data
    for attr in attr_names:
        assert attr in json_data[entity_code]
