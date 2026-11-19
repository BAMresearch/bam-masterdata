import textwrap
from enum import Enum

import pytest

from bam_masterdata.checker.schema_validator import get_object_types
from bam_masterdata.metadata.entities_dict import EntitiesDict
from bam_masterdata.utils import DATAMODEL_DIR


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
    def test_single_json(self):
        """Test the `single_json` function."""
        data = EntitiesDict(python_path="./bam_masterdata/datamodel/v0").single_json()
        assert {
            "collection_types",
            "dataset_types",
            "object_types",
            "vocabulary_types",
            "activities",
        } <= data.keys()

        assert "ACTION" in data["object_types"]

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
        assert temp_object["defs"]["code"] == "TEMP_OBJECT"
        assert temp_object["defs"]["row_location"] == 6
        assert temp_object["properties"][0]["row_location"] == 9
        assert temp_object["properties"][1]["row_location"] == 19

        temp_vocab = data["TEMP_VOCAB"]
        assert temp_vocab["defs"]["code"] == "TEMP_VOCAB"
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

    def test_single_json_merges_modules_with_same_name(self, monkeypatch):
        module_data = {
            "/tmp/domain_a/object_types.py": {
                "OBJECT_A": {"defs": {"code": "OBJECT_A"}},
            },
            "/tmp/domain_b/object_types.py": {
                "OBJECT_B": {"defs": {"code": "OBJECT_B"}},
            },
        }

        monkeypatch.setattr(
            "bam_masterdata.metadata.entities_dict.listdir_py_modules",
            lambda directory_path, logger: list(module_data),
        )
        monkeypatch.setattr(
            EntitiesDict,
            "to_dict",
            lambda self, module_path: module_data[module_path],
        )

        data = EntitiesDict(python_path="/tmp").single_json()

        assert set(data["object_types"]) == {"OBJECT_A", "OBJECT_B"}

    def test_single_json_rejects_duplicate_codes(self, monkeypatch):
        module_data = {
            "/tmp/domain_a/object_types.py": {
                "OBJECT_A": {"defs": {"code": "OBJECT_A"}},
            },
            "/tmp/domain_b/object_types.py": {
                "OBJECT_A": {"defs": {"code": "OBJECT_A"}},
            },
        }

        monkeypatch.setattr(
            "bam_masterdata.metadata.entities_dict.listdir_py_modules",
            lambda directory_path, logger: list(module_data),
        )
        monkeypatch.setattr(
            EntitiesDict,
            "to_dict",
            lambda self, module_path: module_data[module_path],
        )

        with pytest.raises(ValueError, match="Duplicate entity codes"):
            EntitiesDict(python_path="/tmp").single_json()

    def test_single_json_preserves_all_v0_object_types(self):
        expected = {cls.defs.code for cls in get_object_types("v0")}

        data = EntitiesDict(python_path=DATAMODEL_DIR).single_json()

        exported = {
            code
            for entities in data.values()
            for code, entity in entities.items()
            if "generated_code_prefix" in entity["defs"]
        }

        assert expected <= exported
