import os
from unittest.mock import MagicMock

import pytest
from pydantic import ConfigDict

from bam_masterdata.logger import log_storage
from bam_masterdata.metadata.definitions import (
    ObjectTypeDef,
    PropertyTypeAssignment,
    VocabularyTerm,
    VocabularyTypeDef,
)
from bam_masterdata.metadata.entities import BaseEntity, ObjectType, VocabularyType
from bam_masterdata.parsing import AbstractParser

if os.getenv("_PYTEST_RAISE", "0") != "0":

    @pytest.hookimpl(tryfirst=True)
    def pytest_exception_interact(call):
        raise call.excinfo.value

    @pytest.hookimpl(tryfirst=True)
    def pytest_internalerror(excinfo):
        raise excinfo.value


@pytest.fixture(autouse=True)
def cleared_log_storage():
    """Fixture to clear the log storage before each test."""
    log_storage.clear()
    yield log_storage


class MockedEntity(BaseEntity):
    model_config = ConfigDict(ignored_types=(ObjectTypeDef, PropertyTypeAssignment))
    defs = ObjectTypeDef(
        code="MOCKED_ENTITY",
        description="""
        Mockup for an entity definition//Mockup für eine Entitätsdefinition
        """,
        generated_code_prefix="MOCKENT",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""
        Name
        """,
        mandatory=True,
        show_in_edit_views=True,
        section="General information",
    )


class MockedObjectType(ObjectType):
    defs = ObjectTypeDef(
        code="MOCKED_OBJECT_TYPE",
        description="""
        Mockup for an object type definition
        """,
        generated_code_prefix="MOCKOBJTYPE",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""
        Name
        """,
        mandatory=True,
        show_in_edit_views=True,
        section="General information",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alias",
        description="""
        Alias
        """,
        mandatory=False,
        show_in_edit_views=True,
        section="General information",
    )
    storage_storage_validation_level = PropertyTypeAssignment(
        code="$STORAGE.STORAGE_VALIDATION_LEVEL",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="$STORAGE.STORAGE_VALIDATION_LEVEL",
        property_label="Validation level",
        description="""Validation level""",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )


class MockedObjectTypeLonger(MockedObjectType):
    defs = ObjectTypeDef(
        code="MOCKED_OBJECT_TYPE_LONGER",
        description="""
        Mockup for an object type definition with more property type assignments
        """,
        generated_code_prefix="MOCKOBJTYPELONG",
    )

    settings = PropertyTypeAssignment(
        code="SETTINGS",
        data_type="MULTILINE_VARCHAR",
        property_label="Settings",
        description="""
        Settings
        """,
        mandatory=False,
        show_in_edit_views=True,
        section="General information",
    )


class MockedVocabularyType(VocabularyType):
    defs = VocabularyTypeDef(
        code="MOCKED_VOCABULARY_TYPE",
        description="""
        Mockup for an vocabulary type definition
        """,
    )

    option_a = VocabularyTerm(
        code="OPTION_A",
        label="Option A",
        description="Option A from two possible options in the vocabulary",
    )

    option_b = VocabularyTerm(
        code="OPTION_B",
        label="Option B",
        description="Option B from two possible options in the vocabulary",
    )


def generate_base_entity():
    return MockedEntity()


def generate_object_type_miss_mandatory():
    return MockedObjectType()


def generate_object_type(name: str = "Mandatory name", code: str = ""):
    if code:
        return MockedObjectType(name=name, code=code)
    return MockedObjectType(name=name)


def generate_object_type_longer():
    return MockedObjectTypeLonger()


def generate_vocabulary_type():
    return MockedVocabularyType()


@pytest.fixture
def mock_openbis():
    """Fixture to provide a mock OpenBIS instance for testing.

    This mock includes:
    - Mock users

    Returns:
        Openbis: A mock OpenBIS instance configured for testing
    """
    mock_openbis = MagicMock()
    mock_openbis.username = "testuser"
    mock_openbis.get_spaces.return_value = []

    def new_object(**kwargs):
        obj = MagicMock(**kwargs)
        obj.identifier = f"/fake/{len(mock_openbis._objects) + 1}"
        mock_openbis._objects.append(obj)
        return obj

    # Mock users
    mock_user1 = MagicMock(firstName="John", lastName="Doe", userId="jdoe")
    mock_user2 = MagicMock(firstName="Jane", lastName="Smith", userId="jsmith")
    mock_user3 = MagicMock(firstName="Markus", lastName="Müller", userId="mmueller")
    mock_openbis.get_users.return_value = [mock_user1, mock_user2, mock_user3]

    # Mock object creation with pybis
    mock_openbis._objects = []
    mock_openbis.new_object.side_effect = new_object

    # # Create the mock openbis instance
    # openbis = Openbis(url="https://test.openbis.ch")
    # openbis.username = "testuser"

    # # Create a default user space and add it to the openbis spaces
    # user_space = MockSpace("USER_TESTUSER")
    # openbis._spaces.append(user_space)

    return mock_openbis


class TestParser(AbstractParser):
    """Simple test parser that creates test objects"""

    def parse(self, files, collection, logger):
        test_obj = generate_object_type()
        test_obj_id = collection.add(test_obj)
        logger.info(f"Added test object with ID {test_obj_id}")


class TestParserWithRelationship(AbstractParser):
    """Test parser that creates objects with relationships"""

    def parse(self, files, collection, logger):
        parent = generate_object_type(name="Parent")
        parent_id = collection.add(parent)
        child = generate_object_type(name="Child")
        child_id = collection.add(child)
        collection.add_relationship(parent_id, child_id)
        logger.info(f"Linked child {child_id} to parent {parent_id}")


class TestParserWithExistingCode(AbstractParser):
    """Test parser that references existing objects by code"""

    def parse(self, files, collection, logger):
        """Parse files and create object with existing code"""
        test_obj = generate_object_type(code="EXISTING_OBJ_0001")
        _ = collection.add(test_obj)
        logger.info(f"Added object with existing code: {test_obj.code}")


# Test fixtures for OBJECT data type testing
class PersonObjectType(ObjectType):
    """Mock Person object type for testing OBJECT references."""

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


class InstrumentObjectType(ObjectType):
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


class TestParserWithObjectReference(AbstractParser):
    """Test parser that creates objects with OBJECT property references"""

    def parse(self, files, collection, logger):
        """Parse files and create objects with OBJECT references"""
        # Create a person object first
        person = PersonObjectType(name="John Doe", code="PERSON_001")
        person_id = collection.add(person)
        logger.info(f"Added person object with ID {person_id}")

        # Create an instrument that references the person by object instance
        instrument1 = InstrumentObjectType(name="Instrument 1")
        instrument1.responsible_person = person
        instrument1_id = collection.add(instrument1)
        logger.info(f"Added instrument1 with object reference, ID {instrument1_id}")

        # Create another instrument that references by path string
        instrument2 = InstrumentObjectType(name="Instrument 2")
        instrument2.responsible_person = (
            "/TEST_SPACE/TEST_PROJECT/TEST_COLLECTION/PERSON_001"
        )
        instrument2_id = collection.add(instrument2)
        logger.info(f"Added instrument2 with path reference, ID {instrument2_id}")
