import io

import h5py
import pytest

from bam_masterdata.metadata.definitions import PropertyTypeAssignment
from tests.conftest import (
    generate_base_entity,
    generate_object_type,
    generate_object_type_longer,
    generate_vocabulary_type,
)


class TestBaseEntity:
    def test_setattr(self):
        """Test the method `__setattr__` from the class `BaseEntity`."""
        entity = generate_base_entity()
        assert "name" in entity._property_metadata
        assert isinstance(entity._property_metadata["name"], PropertyTypeAssignment)
        assert isinstance(entity.name, PropertyTypeAssignment)

        # Valid type (VARCHAR is str in Python)
        entity.name = "Test"
        assert entity.name == "Test" and isinstance(entity.name, str)

        # Invalid types
        with pytest.raises(
            TypeError, match="Invalid type for 'name': Expected str, got int"
        ):
            entity.name = 42
        with pytest.raises(
            TypeError, match="Invalid type for 'name': Expected str, got bool"
        ):
            entity.name = True

    def test_repr(self):
        """Test the method `__repr__` from the class `BaseEntity`."""
        entity = generate_base_entity()
        assert repr(entity) == "MockedEntity()"
        entity.name = "Test"
        assert repr(entity) == "MockedEntity(name='Test')"

    def test_to_json(self):
        """Test the method `to_json` from the class `BaseEntity`."""
        entity = generate_base_entity()
        entity.name = "Test"
        data = entity.to_json()
        assert data == '{"name": "Test"}'

    def test_to_dict(self):
        """Test the method `to_dict` from the class `BaseEntity`."""
        entity = generate_base_entity()
        entity.name = "Test"
        data = entity.to_dict()
        assert data == {"name": "Test"}

    def test_to_hdf5(self):
        """Test the method `to_hdf5` from the class `BaseEntity`."""
        entity = generate_base_entity()
        entity.name = "Test"
        # mocking the HDF5 file
        with h5py.File(io.BytesIO(), "w") as hdf_file:
            entity.to_hdf5(hdf_file=hdf_file)
            data = hdf_file
            assert isinstance(data, h5py.File)
            assert isinstance(data["MockedEntity"], h5py.Group)
            assert data["MockedEntity"]["name"][()] == b"Test"
            assert data["MockedEntity"]["name"][()].decode() == "Test"

    def test_model_to_json(self):
        """Test the method `model_to_json` from the class `BaseEntity`."""
        entity = generate_base_entity()
        assert (
            entity.model_to_json()
            == '{"defs": {"code": "MOCKED_ENTITY", "description": "Mockup for an entity definition//Mockup f\\u00fcr eine Entit\\u00e4tsdefinition", "iri": null, "id": "MockedEntity", "row_location": null, "validation_script": null, "generated_code_prefix": "MOCKENT", "auto_generated_codes": true}}'
        )

    def test_model_to_dict(self):
        """Test the method `model_to_dict` from the class `BaseEntity`."""
        entity = generate_base_entity()
        assert entity.model_to_dict() == {
            "defs": {
                "code": "MOCKED_ENTITY",
                "description": "Mockup for an entity definition//Mockup für eine Entitätsdefinition",
                "iri": None,
                "id": "MockedEntity",
                "row_location": None,
                "validation_script": None,
                "generated_code_prefix": "MOCKENT",
                "auto_generated_codes": True,
            }
        }


class TestObjectType:
    def test_model_validator_after_init(self):
        """Test the method `model_validator_after_init` from the class `ObjectType`."""
        # 2 properties in this `ObjectType`
        print(
            f"MockedObjectType properties: {[prop.code for prop in generate_object_type().properties]}"
        )
        print(
            f"MockedObjectTypeLonger properties: {[prop.code for prop in generate_object_type_longer().properties]}"
        )
        object_type = generate_object_type()
        assert len(object_type.properties) == 2
        prop_names = [prop.code for prop in object_type.properties]
        assert prop_names == ["$NAME", "ALIAS"]

        # 3 properties in this `ObjectType`
        object_type = generate_object_type_longer()
        assert len(object_type.properties) == 3
        prop_names = [prop.code for prop in object_type.properties]
        assert prop_names == ["SETTINGS", "$NAME", "ALIAS"]


class TestVocabularyType:
    def test_model_validator_after_init(self):
        """Test the method `model_validator_after_init` from the class `VocabularyType`."""
        vocabulary_type = generate_vocabulary_type()
        assert len(vocabulary_type.terms) == 2
        term_names = [term.code for term in vocabulary_type.terms]
        assert term_names == ["OPTION_A", "OPTION_B"]
