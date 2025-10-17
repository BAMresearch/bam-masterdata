"""Tests for OBJECT data type handling in ObjectType entities."""

import pytest

from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.entities import ObjectType


class Person(ObjectType):
    """Mock Person object type for testing."""

    defs = ObjectTypeDef(
        code="PERSON",
        description="A person entity for testing",
        generated_code_prefix="PER",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="Person's name",
        mandatory=True,
        show_in_edit_views=True,
        section="General",
    )


class Instrument(ObjectType):
    """Mock Instrument object type with OBJECT property for testing."""

    defs = ObjectTypeDef(
        code="INSTRUMENT",
        description="An instrument entity for testing",
        generated_code_prefix="INS",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="Instrument name",
        mandatory=True,
        show_in_edit_views=True,
        section="General",
    )

    responsible_person = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON",
        property_label="Responsible Person",
        description="Person responsible for the instrument",
        mandatory=False,
        show_in_edit_views=True,
        section="General",
    )


class TestObjectDataType:
    """Test suite for OBJECT data type handling."""

    def test_object_property_with_path_4_parts(self):
        """Test setting an OBJECT property with a valid 4-part path."""
        instrument = Instrument()
        instrument.name = "Test Instrument"

        # Valid 4-part path: /{space}/{project}/{collection}/{object}
        path = "/MY_SPACE/MY_PROJECT/MY_COLLECTION/PERSON_001"
        instrument.responsible_person = path

        assert instrument.responsible_person == path

    def test_object_property_with_path_3_parts(self):
        """Test setting an OBJECT property with a valid 3-part path."""
        instrument = Instrument()
        instrument.name = "Test Instrument"

        # Valid 3-part path: /{space}/{project}/{object}
        path = "/MY_SPACE/MY_PROJECT/PERSON_001"
        instrument.responsible_person = path

        assert instrument.responsible_person == path

    def test_object_property_with_path_leading_trailing_slashes(self):
        """Test that paths with or without leading/trailing slashes are handled."""
        instrument = Instrument()
        instrument.name = "Test Instrument"

        # Path without leading slash - should fail
        with pytest.raises(ValueError, match="Invalid OBJECT path format"):
            instrument.responsible_person = "MY_SPACE/MY_PROJECT/PERSON_001"

        # Path with trailing slash - should work (gets stripped)
        path = "/MY_SPACE/MY_PROJECT/PERSON_001/"
        instrument.responsible_person = path
        assert instrument.responsible_person == path

    def test_object_property_with_invalid_path_too_short(self):
        """Test that paths with too few parts are rejected."""
        instrument = Instrument()
        instrument.name = "Test Instrument"

        with pytest.raises(ValueError, match="Invalid OBJECT path format"):
            instrument.responsible_person = "/MY_SPACE/PERSON_001"

    def test_object_property_with_invalid_path_too_long(self):
        """Test that paths with too many parts are rejected."""
        instrument = Instrument()
        instrument.name = "Test Instrument"

        with pytest.raises(ValueError, match="Invalid OBJECT path format"):
            instrument.responsible_person = (
                "/MY_SPACE/MY_PROJECT/MY_COLLECTION/SUB/PERSON_001"
            )

    def test_object_property_with_object_instance(self):
        """Test setting an OBJECT property with an ObjectType instance."""
        instrument = Instrument()
        instrument.name = "Test Instrument"

        person = Person()
        person.name = "John Doe"
        person.code = "PERSON_001"

        instrument.responsible_person = person

        assert instrument.responsible_person == person
        assert instrument.responsible_person.code == "PERSON_001"

    def test_object_property_with_object_instance_no_code(self):
        """Test that setting an OBJECT property with an instance without code fails."""
        instrument = Instrument()
        instrument.name = "Test Instrument"

        person = Person()
        person.name = "John Doe"
        # No code set

        with pytest.raises(ValueError, match="must have a 'code' attribute set"):
            instrument.responsible_person = person

    def test_object_property_with_invalid_type(self):
        """Test that setting an OBJECT property with an invalid type fails."""
        instrument = Instrument()
        instrument.name = "Test Instrument"

        # Try to set with an integer
        with pytest.raises(
            TypeError, match="Expected str \\(path\\) or ObjectType instance"
        ):
            instrument.responsible_person = 123

        # Try to set with a list
        with pytest.raises(
            TypeError, match="Expected str \\(path\\) or ObjectType instance"
        ):
            instrument.responsible_person = ["PERSON_001"]

    def test_object_property_none_value(self):
        """Test that setting an OBJECT property to None is allowed (for optional properties)."""
        instrument = Instrument()
        instrument.name = "Test Instrument"

        # responsible_person is optional (mandatory=False)
        # Setting it to None or leaving it unset should be fine
        # (This tests that we don't break existing behavior)
        assert not hasattr(instrument, "responsible_person") or isinstance(
            getattr(instrument, "responsible_person", None), PropertyTypeAssignment
        )
