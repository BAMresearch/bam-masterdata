import json
import os
import textwrap
from enum import Enum

import pytest

from bam_masterdata.metadata.entities_dict import EntitiesDict


def normalize_data(data):
    if isinstance(data, Enum):
        return data.value
    if isinstance(data, dict):
        cleaned = {}
        for k, v in data.items():
            if k == "units" and v is None:
                continue
            cleaned[k] = normalize_data(v)
        return cleaned
    if isinstance(data, list):
        return [normalize_data(item) for item in data]
    return data


class TestEntitiesDict:
    @pytest.mark.parametrize(
        "module_name, entity_code, attr_names, result_json",
        [
            (
                "collection_types",
                "COLLECTION",
                ["properties", "defs", "code"],
                """{
                    "code": null,
                    "properties": [
                        {
                        "code": "$NAME",
                        "description": "Name",
                        "iri": null,
                        "id": "Name",
                        "row_location": 14,
                        "property_label": "Name",
                        "data_type": "VARCHAR",
                        "vocabulary_code": null,
                        "object_code": null,
                        "metadata": null,
                        "dynamic_script": null,
                        "mandatory": false,
                        "show_in_edit_views": false,
                        "section": "General info",
                        "unique": null,
                        "internal_assignment": null
                        },
                        {
                        "code": "$DEFAULT_OBJECT_TYPE",
                        "description": "Enter the code of the object type for which the collection is used",
                        "iri": null,
                        "id": "DefaultObjectType",
                        "row_location": 24,
                        "property_label": "Default object type",
                        "data_type": "VARCHAR",
                        "vocabulary_code": null,
                        "object_code": null,
                        "metadata": null,
                        "dynamic_script": null,
                        "mandatory": false,
                        "show_in_edit_views": false,
                        "section": "General info",
                        "unique": null,
                        "internal_assignment": null
                        },
                        {
                        "code": "$DEFAULT_COLLECTION_VIEW",
                        "description": "Default view for experiments of the type collection",
                        "iri": null,
                        "id": "DefaultCollectionView",
                        "row_location": 34,
                        "property_label": "Default collection view",
                        "data_type": "CONTROLLEDVOCABULARY",
                        "vocabulary_code": "$DEFAULT_COLLECTION_VIEWS",
                        "object_code": null,
                        "metadata": null,
                        "dynamic_script": null,
                        "mandatory": false,
                        "show_in_edit_views": false,
                        "section": "General info",
                        "unique": null,
                        "internal_assignment": null
                        }
                    ],
                    "defs": {
                        "code": "COLLECTION",
                        "description": "",
                        "iri": null,
                        "id": "Collection",
                        "row_location": 8,
                        "validation_script": null
                    }
                }""",
            ),
            # ('dataset_types', False),  # ! this module does not have classes yet
            (
                "object_types",
                "ACTION",
                ["properties", "defs", "code"],
                """{
                    "code": null,
                    "properties": [
                    {
                        "code": "$NAME",
                        "description": "Name",
                        "iri": null,
                        "id": "Name",
                        "row_location": 4228,
                        "property_label": "Name",
                        "data_type": "VARCHAR",
                        "vocabulary_code": null,
                        "object_code": null,
                        "metadata": null,
                        "dynamic_script": null,
                        "mandatory": false,
                        "show_in_edit_views": false,
                        "section": "Device ID",
                        "unique": null,
                        "internal_assignment": null
                        },
                        {
                        "code": "ACTION_DATE",
                        "description": "Action Date//Datum der Handlung",
                        "iri": null,
                        "id": "ActionDate",
                        "row_location": 4238,
                        "property_label": "Monitoring Date",
                        "data_type": "DATE",
                        "vocabulary_code": null,
                        "object_code": null,
                        "metadata": null,
                        "dynamic_script": null,
                        "mandatory": false,
                        "show_in_edit_views": false,
                        "section": "Action Data",
                        "unique": null,
                        "internal_assignment": null
                        },
                        {
                        "code": "ACTING_PERSON",
                        "description": "Acting Person//Handelnde Person",
                        "iri": null,
                        "id": "ActingPerson",
                        "row_location": 4248,
                        "property_label": "Acting Person",
                        "data_type": "OBJECT",
                        "vocabulary_code": null,
                        "object_code": "PERSON.BAM",
                        "metadata": null,
                        "dynamic_script": null,
                        "mandatory": false,
                        "show_in_edit_views": false,
                        "section": "Action Data",
                        "unique": null,
                        "internal_assignment": null
                        },
                        {
                        "code": "$XMLCOMMENTS",
                        "description": "Comments log",
                        "iri": null,
                        "id": "Xmlcomments",
                        "row_location": 4259,
                        "property_label": "Comments",
                        "data_type": "XML",
                        "vocabulary_code": null,
                        "object_code": null,
                        "metadata": null,
                        "dynamic_script": null,
                        "mandatory": false,
                        "show_in_edit_views": false,
                        "section": "Additional Information",
                        "unique": null,
                        "internal_assignment": null
                        },
                        {
                        "code": "$ANNOTATIONS_STATE",
                        "description": "Annotations State",
                        "iri": null,
                        "id": "AnnotationsState",
                        "row_location": 4269,
                        "property_label": "Annotations State",
                        "data_type": "XML",
                        "vocabulary_code": null,
                        "object_code": null,
                        "metadata": null,
                        "dynamic_script": null,
                        "mandatory": false,
                        "show_in_edit_views": false,
                        "section": "",
                        "unique": null,
                        "internal_assignment": null
                        }
                    ],
                    "defs": {
                        "code": "ACTION",
                        "description": "This Object allows to store information on an action by a user.//Dieses Objekt erlaubt eine Nutzer-Aktion zu beschreiben.",
                        "iri": null,
                        "id": "Action",
                        "row_location": 4221,
                        "validation_script": null,
                        "generated_code_prefix": "ACT",
                        "auto_generate_codes": true
                    }
                }""",
            ),
            (
                "vocabulary_types",
                "$STORAGE_FORMAT",
                ["terms", "defs", "code"],
                """{
                    "code": null,
                    "terms": [
                        {
                        "code": "BDS_DIRECTORY",
                        "description": "",
                        "iri": null,
                        "id": "BdsDirectory",
                        "row_location": 30,
                        "url_template": null,
                        "label": "",
                        "official": true
                        },
                        {
                        "code": "PROPRIETARY",
                        "description": "",
                        "iri": null,
                        "id": "Proprietary",
                        "row_location": 36,
                        "url_template": null,
                        "label": "",
                        "official": true
                        }
                    ],
                    "defs": {
                        "code": "$STORAGE_FORMAT",
                        "description": "The on-disk storage format of a data set",
                        "iri": null,
                        "id": "StorageFormat",
                        "row_location": 24,
                        "url_template": null
                    }
                }""",
            ),
        ],
    )
    def test_to_dict(
        self,
        module_name: str,
        entity_code: str,
        attr_names: list[str],
        result_json: str,
    ):
        """Test the `to_dict` function."""
        module_path = os.path.join("./bam_masterdata/datamodel", f"{module_name}.py")

        data = EntitiesDict().to_dict(module_path=module_path)

        assert entity_code in data
        for attr in attr_names:
            assert attr in data[entity_code]
        assert normalize_data(data[entity_code]) == normalize_data(
            json.loads(result_json)
        )

    def test_single_json(self):
        """Test the `single_json` function."""
        data = EntitiesDict(python_path="./bam_masterdata/datamodel").single_json()
        assert len(data) == 4
        assert list(data.keys()) == [
            "collection_types",
            "dataset_types",
            "object_types",
            "vocabulary_types",
        ]

    def test_to_dict_extracts_row_locations_from_temp_module(self, tmp_path):
        module_path = tmp_path / "temp_metadata.py"
        module_path.write_text(
            textwrap.dedent(
                """
                from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment, VocabularyTerm, VocabularyTypeDef
                from bam_masterdata.metadata.entities import ObjectType, VocabularyType


                class TempObject(ObjectType):
                    defs = ObjectTypeDef(code="TEMP_OBJECT", description="Temporary object", generated_code_prefix="TMP")

                    sample_name = PropertyTypeAssignment(
                        code="$SAMPLE.NAME",
                        data_type="VARCHAR",
                        property_label="Sample name",
                        description="Name",
                        mandatory=True,
                        show_in_edit_views=True,
                        section="General",
                    )

                    review_status = PropertyTypeAssignment(
                        code="REVIEW_STATUS",
                        data_type="VARCHAR",
                        property_label="Review status",
                        description="Status",
                        mandatory=False,
                        show_in_edit_views=True,
                        section="General",
                    )


                class TempVocabulary(VocabularyType):
                    defs = VocabularyTypeDef(code="TEMP_VOCAB", description="Temporary vocabulary")

                    option_a = VocabularyTerm(
                        code="OPTION_A",
                        label="Option A",
                        description="Option A",
                    )
                """
            ),
            encoding="utf-8",
        )

        data = EntitiesDict().to_dict(module_path=str(module_path))

        temp_object = data["TEMP_OBJECT"]
        assert temp_object["defs"]["row_location"] == 6
        assert temp_object["properties"][0]["row_location"] == 9
        assert temp_object["properties"][1]["row_location"] == 19

        temp_vocab = data["TEMP_VOCAB"]
        assert temp_vocab["defs"]["row_location"] == 30
        assert temp_vocab["terms"][0]["row_location"] == 33

    def test_to_dict_logs_and_skips_broken_classes(self, tmp_path, capsys):
        module_path = tmp_path / "broken_metadata.py"
        module_path.write_text(
            textwrap.dedent(
                """
                from bam_masterdata.metadata.definitions import ObjectTypeDef


                class BrokenEntity:
                    defs = ObjectTypeDef(code="BROKEN_ENTITY", description="Broken entity", generated_code_prefix="BRK")

                    def model_to_dict(self):
                        raise RuntimeError("broken on purpose")
                """
            ),
            encoding="utf-8",
        )

        data = EntitiesDict().to_dict(module_path=str(module_path))

        captured = capsys.readouterr()
        assert data == {}
        assert "Failed to process class BrokenEntity" in captured.out
        assert "broken on purpose" in captured.out

    def test_single_json_uses_module_names_as_keys(self, monkeypatch):
        module_paths = ["/tmp/beta.py", "/tmp/alpha.py"]

        monkeypatch.setattr(
            "bam_masterdata.metadata.entities_dict.listdir_py_modules",
            lambda directory_path, logger: module_paths,
        )
        monkeypatch.setattr(
            EntitiesDict,
            "to_dict",
            lambda self, module_path: {"module_path": module_path},
        )

        data = EntitiesDict(python_path="/tmp/example").single_json()

        assert data == {
            "beta": {"module_path": "/tmp/beta.py"},
            "alpha": {"module_path": "/tmp/alpha.py"},
        }
