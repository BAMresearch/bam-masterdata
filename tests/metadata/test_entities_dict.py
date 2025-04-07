import json
import os

import pytest

from bam_masterdata.metadata.entities_dict import EntitiesDict


class TestEntitiesDict:
    @pytest.mark.parametrize(
        "module_name, entity_code, attr_names, result_json",
        [
            (
                "collection_types",
                "COLLECTION",
                ["properties", "defs"],
                """{
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
                ["properties", "defs"],
                """{
                    "properties": [
                    {
                        "code": "$NAME",
                        "description": "Name",
                        "iri": null,
                        "id": "Name",
                        "row_location": 4218,
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
                        "row_location": 4228,
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
                        "row_location": 4238,
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
                        "row_location": 4249,
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
                        "row_location": 4259,
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
                        "row_location": 4211,
                        "validation_script": null,
                        "generated_code_prefix": "ACT",
                        "auto_generated_codes": true
                    }
                }""",
            ),
            (
                "vocabulary_types",
                "$STORAGE_FORMAT",
                ["terms", "defs"],
                """{
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
        assert data[entity_code] == json.loads(result_json)

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
