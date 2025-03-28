import datetime
from typing import Optional

import pytest

from bam_masterdata.metadata.definitions import (
    BaseObjectTypeDef,
    CollectionTypeDef,
    DatasetTypeDef,
    DataType,
    EntityDef,
    ObjectTypeDef,
    PropertyTypeAssignment,
    PropertyTypeDef,
    VocabularyTerm,
    VocabularyTypeDef,
)


class TestDataType:
    @pytest.mark.parametrize(
        "data_type, result",
        [
            (DataType.BOOLEAN, bool),
            (
                DataType.CONTROLLEDVOCABULARY,
                None,
            ),  # Update this once the mapping is implemented
            (DataType.DATE, datetime.date),
            (DataType.HYPERLINK, str),
            (DataType.INTEGER, int),
            (DataType.MULTILINE_VARCHAR, str),
            (DataType.OBJECT, None),  # Update this once the mapping is implemented
            (DataType.REAL, float),
            (
                DataType.TIMESTAMP,
                datetime.datetime,
            ),  # Update this once the mapping is implemented
            (DataType.VARCHAR, str),
            (DataType.XML, None),  # Update this once the mapping is implemented
        ],
    )
    def test_pytype(self, data_type: DataType, result: type):
        """Test the `pytype` property of `DataType`."""
        assert data_type.pytype == result


class TestEntityDef:
    def test_fields(self):
        """Test the existing defined fields of the `EntityDef` class."""
        names = list(EntityDef.model_fields.keys())
        field_types = [val.annotation for val in list(EntityDef.model_fields.values())]
        assert names == ["code", "description", "iri", "id", "row_location"]
        assert field_types == [str, str, Optional[str], Optional[str], Optional[str]]

    @pytest.mark.parametrize(
        "code, description, id, is_valid",
        [
            # `code` in capital and separated by underscores
            ("EXPERIMENTAL_STEP", "Valid description", "ExperimentalStep", True),
            # `code` starting with $ symbol
            ("$NAME", "Valid description", "Name", True),
            # `code` separating inheritance with points
            ("WELDING_EQUIPMENT.INSTRUMENT", "Valid description", "Instrument", True),
            # Invalid `code`
            ("INVALID CODE", "Valid description", None, False),
            # `description` is not a string
            ("EXPERIMENTAL_STEP", 2, None, False),
            # Empty `code`
            ("", "Valid description", "", False),
        ],
    )
    def test_entity_def(self, code: str, description: str, id: str, is_valid: bool):
        """Test creation of `EntityDef` and field validation."""
        if is_valid:
            entity = EntityDef(code=code, description=description)
            assert entity.code == code
            assert entity.description == description
            assert entity.id == id
        else:
            with pytest.raises(ValueError):
                EntityDef(code=code, description=description)

    @pytest.mark.parametrize(
        "code, is_valid",
        [
            # `code` in capital and separated by underscores
            ("EXPERIMENTAL_STEP", True),
            # `code` starting with $ symbol
            ("$NAME", True),
            # `code` separating inheritance with points
            ("WELDING_EQUIPMENT.INSTRUMENT", True),
            # Invalid `code`
            ("INVALID CODE", False),
            # Empty code
            ("", False),
        ],
    )
    def test_validate_code(self, code: str, is_valid: bool):
        """Test the code validator."""
        if is_valid:
            entity = EntityDef(code=code, description="Valid description")
            assert entity.code == code
        else:
            with pytest.raises(ValueError):
                EntityDef(code=code, description="Valid description")

    def test_strip_description(self):
        """Test the `strip_description` method."""
        entity = EntityDef(
            code="EXPERIMENTAL_STEP", description="  Valid description  "
        )
        assert entity.description == "Valid description"


class TestBaseObjectTypeDef:
    def test_fields(self):
        """Test the existing defined fields of the `BaseObjectTypeDef` class."""
        names = list(BaseObjectTypeDef.model_fields.keys())
        field_types = [
            val.annotation for val in list(BaseObjectTypeDef.model_fields.values())
        ]
        assert names == [
            "code",
            "description",
            "iri",
            "id",
            "row_location",
            "validation_script",
        ]
        assert field_types == [
            str,
            str,
            Optional[str],
            Optional[str],
            Optional[str],
            Optional[str],
        ]


class TestCollectionTypeDef:
    def test_fields(self):
        """Test the existing defined fields of the `CollectionTypeDef` class."""
        names = list(CollectionTypeDef.model_fields.keys())
        field_types = [
            val.annotation for val in list(CollectionTypeDef.model_fields.values())
        ]
        assert names == [
            "code",
            "description",
            "iri",
            "id",
            "row_location",
            "validation_script",
        ]
        assert field_types == [
            str,
            str,
            Optional[str],
            Optional[str],
            Optional[str],
            Optional[str],
        ]


class TestDatasetTypeDef:
    def test_fields(self):
        """Test the existing defined fields of the `DatasetTypeDef` class."""
        names = list(DatasetTypeDef.model_fields.keys())
        field_types = [
            val.annotation for val in list(DatasetTypeDef.model_fields.values())
        ]
        assert names == [
            "code",
            "description",
            "iri",
            "id",
            "row_location",
            "validation_script",
            "main_dataset_pattern",
            "main_dataset_path",
        ]
        assert field_types == [
            str,
            str,
            Optional[str],
            Optional[str],
            Optional[str],
            Optional[str],
            Optional[str],
            Optional[str],
        ]


class TestObjectTypeDef:
    def test_fields(self):
        """Test the existing defined fields of the `ObjectTypeDef` class."""
        names = list(ObjectTypeDef.model_fields.keys())
        field_types = [
            val.annotation for val in list(ObjectTypeDef.model_fields.values())
        ]
        assert names == [
            "code",
            "description",
            "iri",
            "id",
            "row_location",
            "validation_script",
            "generated_code_prefix",
            "auto_generated_codes",
        ]
        assert field_types == [
            str,
            str,
            Optional[str],
            Optional[str],
            Optional[str],
            Optional[str],
            Optional[str],
            bool,
        ]

    @pytest.mark.parametrize(
        "code, generated_code_prefix, result",
        [
            # No `generated_code_prefix`
            ("INSTRUMENT", None, "INS"),
            ("INSTRUMENT", "", "INS"),
            # `generated_code_prefix` is already set
            ("INSTRUMENT", "INSTRU", "INSTRU"),
        ],
    )
    def test_model_validator_after_init(
        self, code: str, generated_code_prefix: Optional[str], result: str
    ):
        """Test the after-init model validator for `ObjectTypeDef`."""
        entity = ObjectTypeDef(
            code=code,
            description="Valid description",
            generated_code_prefix=generated_code_prefix,
        )
        assert entity.generated_code_prefix == result


class TestPropertyTypeDef:
    def test_fields(self):
        """Test the existing defined fields of the `PropertyTypeDef` class."""
        names = list(PropertyTypeDef.model_fields.keys())
        field_types = [
            val.annotation for val in list(PropertyTypeDef.model_fields.values())
        ]
        assert names == [
            "code",
            "description",
            "iri",
            "id",
            "row_location",
            "property_label",
            "data_type",
            "vocabulary_code",
            "object_code",
            "metadata",
            "dynamic_script",
        ]
        assert field_types == [
            str,
            str,
            Optional[str],
            Optional[str],
            Optional[str],
            str,
            DataType,
            Optional[str],
            Optional[str],
            Optional[dict],
            Optional[str],
        ]


class TestPropertyTypeAssignment:
    def test_fields(self):
        """Test the existing defined fields of the `PropertyTypeAssignment` class."""
        names = list(PropertyTypeAssignment.model_fields.keys())
        field_types = [
            val.annotation for val in list(PropertyTypeAssignment.model_fields.values())
        ]
        assert names == [
            "code",
            "description",
            "iri",
            "id",
            "row_location",
            "property_label",
            "data_type",
            "vocabulary_code",
            "object_code",
            "metadata",
            "dynamic_script",
            "mandatory",
            "show_in_edit_views",
            "section",
            "unique",
            "internal_assignment",
        ]
        assert field_types == [
            str,
            str,
            Optional[str],
            Optional[str],
            Optional[str],
            str,
            DataType,
            Optional[str],
            Optional[str],
            Optional[dict],
            Optional[str],
            bool,
            bool,
            str,
            Optional[str],
            Optional[str],
        ]


class TestVocabularyTypeDef:
    def test_fields(self):
        """Test the existing defined fields of the `VocabularyTypeDef` class."""
        names = list(VocabularyTypeDef.model_fields.keys())
        field_types = [
            val.annotation for val in list(VocabularyTypeDef.model_fields.values())
        ]
        assert names == [
            "code",
            "description",
            "iri",
            "id",
            "row_location",
            "url_template",
        ]
        assert field_types == [
            str,
            str,
            Optional[str],
            Optional[str],
            Optional[str],
            Optional[str],
        ]


class TestVocabularyTerm:
    def test_fields(self):
        """Test the existing defined fields of the `VocabularyTerm` class."""
        names = list(VocabularyTerm.model_fields.keys())
        field_types = [
            val.annotation for val in list(VocabularyTerm.model_fields.values())
        ]
        assert names == [
            "code",
            "description",
            "iri",
            "id",
            "row_location",
            "url_template",
            "label",
            "official",
        ]
        assert field_types == [
            str,
            str,
            Optional[str],
            Optional[str],
            Optional[str],
            Optional[str],
            str,
            bool,
        ]
