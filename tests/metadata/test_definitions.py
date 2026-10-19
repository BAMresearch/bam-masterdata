import datetime

import pytest
from pydantic import ValidationError

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


@pytest.mark.parametrize(
    "model, expected_fields",
    [
        (
            EntityDef,
            {
                "code": str,
                "description": str,
                "prev_versions": list[str] | None,
                "iri": list[str] | None,
                "id": str | None,
                "row_location": str | None,
            },
        ),
        (
            BaseObjectTypeDef,
            {
                "validation_script": str | None,
            },
        ),
        (
            DatasetTypeDef,
            {
                "main_dataset_pattern": str | None,
                "main_dataset_path": str | None,
            },
        ),
        (
            ObjectTypeDef,
            {
                "generated_code_prefix": str | None,
                "auto_generate_codes": bool,
            },
        ),
        (
            PropertyTypeDef,
            {
                "property_label": str,
                "units": str | None,
                "data_type": DataType,
                "vocabulary_code": str | None,
                "object_code": str | None,
                "metadata": dict | None,
                "dynamic_script": str | None,
                "ordinal": int | None,
            },
        ),
        (
            PropertyTypeAssignment,
            {
                "mandatory": bool,
                "show_in_edit_views": bool,
                "section": str,
                "unique": str | None,
                "internal_assignment": str | None,
            },
        ),
        (
            VocabularyTypeDef,
            {
                "url_template": str | None,
            },
        ),
        (
            VocabularyTerm,
            {
                "label": str,
                "official": bool,
            },
        ),
    ],
)
def test_definition_fields(model, expected_fields):
    for name, expected_type in expected_fields.items():
        assert name in model.model_fields
        assert model.model_fields[name].annotation == expected_type


class TestEntityDef:
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

    @pytest.mark.parametrize(
        "entity, expected_name",
        [
            (
                CollectionTypeDef(code="COLLECTION", description="Collection"),
                "EXPERIMENT_TYPE",
            ),
            (DatasetTypeDef(code="RAW_DATA", description="Raw data"), "DATASET_TYPE"),
            (ObjectTypeDef(code="INSTRUMENT", description="Instrument"), "SAMPLE_TYPE"),
            (
                VocabularyTypeDef(code="DOCUMENT_TYPE", description="Document type"),
                "VOCABULARY_TYPE",
            ),
            (
                PropertyTypeDef(
                    code="PROPERTY_CODE",
                    description="Property",
                    property_label="Property",
                    data_type=DataType.VARCHAR,
                ),
                None,
            ),
        ],
    )
    def test_excel_name(self, entity, expected_name):
        assert entity.excel_name == expected_name

    def test_excel_headers_map_excludes_internal_fields(self):
        entity = ObjectTypeDef(
            code="INSTRUMENT",
            description="Instrument",
            validation_script="validate.instrument",
        )
        assert entity.excel_headers_map == {
            "code": "Code",
            "description": "Description",
            "validation_script": "Validation script",
            "generated_code_prefix": "Generated code prefix",
            "auto_generate_codes": "Auto generate codes",
        }


class TestObjectTypeDef:
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
        self, code: str, generated_code_prefix: str | None, result: str
    ):
        """Test the after-init model validator for `ObjectTypeDef`."""
        entity = ObjectTypeDef(
            code=code,
            description="Valid description",
            generated_code_prefix=generated_code_prefix,
        )
        assert entity.generated_code_prefix == result


class TestPropertyTypeDef:
    def test_units_append_to_label(self):
        prop = PropertyTypeDef(
            code="LENGTH",
            description="Length of the sample",
            property_label="Length",
            data_type=DataType.REAL,
            units="meter",
        )
        assert prop.property_label == "Length in [meter]"

    def test_units_skip_when_label_already_has_units(self):
        prop = PropertyTypeDef(
            code="LENGTH",
            description="Length of the sample",
            property_label="Length in [m]",
            data_type=DataType.REAL,
            units="meter",
        )
        assert prop.property_label == "Length in [m]"

    def test_units_invalid(self):
        with pytest.raises(ValueError):
            PropertyTypeDef(
                code="LENGTH",
                description="Length of the sample",
                property_label="Length",
                data_type=DataType.REAL,
                units="not_a_real_unit",
            )

    def test_units_invalid_label_format(self):
        with pytest.raises(ValueError):
            PropertyTypeDef(
                code="LENGTH",
                description="Length of the sample",
                property_label="Length [m]",
                data_type=DataType.REAL,
                units="meter",
            )

    def test_model_id_uses_property_conversion(self):
        prop = PropertyTypeDef(
            code="$STORAGE.STORAGE_VALIDATION_LEVEL",
            description="Validation level",
            property_label="Validation level",
            data_type=DataType.VARCHAR,
        )
        assert prop.id == "StorageStorageValidationLevel"


class TestPreviousVersions:
    """Tests for EntityDef.prev_versions validation."""

    @pytest.mark.parametrize(
        "prev_versions",
        [
            None,
            ["EXPERIMENTAL_STEP:v0"],
            ["EXPERIMENT:v1"],
            ["EXPERIMENTAL_STEP:v0", "EXPERIMENT:v1"],
            ["INSTRUMENT.DEVICE:v0"],
            ["TEMPERATURE_1:v2"],
            ["EXPERIMENT:v12"],
            ["$NAME:v0"],
        ],
    )
    def test_valid_prev_versions(self, prev_versions):
        entity = EntityDef(
            code="TEST_ENTITY",
            description="Test entity",
            prev_versions=prev_versions,
        )

        assert entity.prev_versions == prev_versions

    @pytest.mark.parametrize(
        "prev_versions",
        [
            [],
            [""],
            ["EXPERIMENT"],
            ["EXPERIMENT:0"],
            ["EXPERIMENT:v"],
            ["EXPERIMENT:vX"],
            ["EXPERIMENT:v1.0"],
            ["EXPERIMENT:v-1"],
            ["EXPERIMENT:v0:extra"],
            ["EXPERIMENT:v0 "],
            [" EXPERIMENT:v0"],
            ["EXPERIMENT:v0", "INVALID"],
            ["EXPERIMENT:v0", "EXPERIMENT:v0"],
            ["MATERIAL-ENTITY:v0"],
        ],
    )
    def test_invalid_prev_versions(self, prev_versions):
        with pytest.raises(ValidationError):
            EntityDef(
                code="TEST_ENTITY",
                description="Test entity",
                prev_versions=prev_versions,
            )

    def test_prev_versions_default_none(self):
        entity = EntityDef(
            code="TEST_ENTITY",
            description="Test entity",
        )

        assert entity.prev_versions is None

    def test_prev_versions_preserves_order(self):
        versions = [
            "EXPERIMENTAL_STEP:v0",
            "EXPERIMENT:v1",
            "EXPERIMENT:v2",
        ]

        entity = EntityDef(
            code="TEST_ENTITY",
            description="Test entity",
            prev_versions=versions,
        )

        assert entity.prev_versions == versions

    def test_prev_versions_serialization(self):
        versions = [
            "EXPERIMENTAL_STEP:v0",
            "EXPERIMENT:v1",
        ]

        entity = EntityDef(
            code="TEST_ENTITY",
            description="Test entity",
            prev_versions=versions,
        )

        serialized = entity.model_dump()

        assert serialized["prev_versions"] == versions


class TestIRI:
    """Tests for EntityDef.iri validation."""

    @pytest.mark.parametrize(
        "iri",
        [
            None,
            ["BFO_0000001"],
            ["CHEBI_15377"],
            ["ENVO_00002006"],
            ["https://w3id.org/pmd/co/PMD_0000001"],
            ["http://purl.obolibrary.org/obo/BFO_0000001"],
            ["https://example.org/ontology#Instrument"],
            ["https://example.org/ontology/Instrument"],
            [
                "BFO_0000001",
                "CHEBI_15377",
            ],
            [
                "https://w3id.org/pmd/co/PMD_0000001",
                "BFO_0000001",
            ],
        ],
    )
    def test_valid_iri(self, iri):
        entity = EntityDef(
            code="TEST_ENTITY",
            description="Test entity",
            iri=iri,
        )

        assert entity.iri == iri

    @pytest.mark.parametrize(
        "iri",
        [
            [],
            [""],
            [" "],
            ["not an IRI"],
            ["BFO_ABC"],
            ["BFO_"],
            ["BFO_123 456"],
            ["ftp://example.org/ontology"],
            ["http://"],
            ["https://"],
            ["https://example.org/ontology with spaces"],
            ["BFO_0000001", "BFO_0000001"],
            [
                "https://example.org/Instrument",
                "https://example.org/Instrument",
            ],
        ],
    )
    def test_invalid_iri(self, iri):
        with pytest.raises(ValidationError):
            EntityDef(
                code="TEST_ENTITY",
                description="Test entity",
                iri=iri,
            )

    def test_iri_rejects_single_string(self):
        with pytest.raises(ValidationError):
            EntityDef(
                code="TEST_ENTITY",
                description="Test entity",
                iri="BFO_0000001",
            )

    def test_iri_default_none(self):
        entity = EntityDef(
            code="TEST_ENTITY",
            description="Test entity",
        )

        assert entity.iri is None

    def test_iri_preserves_order(self):
        references = [
            "BFO_0000001",
            "CHEBI_15377",
            "https://w3id.org/pmd/co/PMD_0000001",
        ]

        entity = EntityDef(
            code="TEST_ENTITY",
            description="Test entity",
            iri=references,
        )

        assert entity.iri == references

    def test_iri_serialization(self):
        references = [
            "BFO_0000001",
            "https://w3id.org/pmd/co/PMD_0000001",
        ]

        entity = EntityDef(
            code="TEST_ENTITY",
            description="Test entity",
            iri=references,
        )

        serialized = entity.model_dump()

        assert serialized["iri"] == references
