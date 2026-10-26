import pytest

from bam_masterdata.checker.schema_validator import validate_object_type_codes
from bam_masterdata.metadata.definitions import ObjectTypeDef
from bam_masterdata.metadata.entities import ObjectType


class TestObjectTypeCodeValidation:
    class Root(ObjectType):
        defs = ObjectTypeDef(code="ROOT", description="Root")

    class Entity(Root):
        defs = ObjectTypeDef(code="ENTITY", description="Entity")

    class Activity(Root):
        defs = ObjectTypeDef(code="ACTIVITY", description="Activity")

    def test_unique_codes(self):
        validate_object_type_codes([self.Root, self.Entity, self.Activity])

    def test_duplicate_codes(self):
        class DuplicateEntity(self.Root):
            defs = ObjectTypeDef(
                code="ENTITY",
                description="Duplicate entity",
            )

        with pytest.raises(ValueError, match="Duplicate object type code 'ENTITY'"):
            validate_object_type_codes([self.Root, self.Entity, DuplicateEntity])

    def test_inherited_definition(self):
        class Child(self.Entity):
            pass

        validate_object_type_codes([self.Root, self.Entity, Child])

    def test_repeated_class(self):
        validate_object_type_codes([self.Root, self.Entity, self.Entity])

    def test_invalid_class(self):
        with pytest.raises(TypeError, match="not an ObjectType subclass"):
            validate_object_type_codes([str])

    def test_separate_versions(self):
        class V0Person(ObjectType):
            defs = ObjectTypeDef(
                code="PERSON",
                description="v0 Person",
            )

        class V1Person(ObjectType):
            defs = ObjectTypeDef(
                code="PERSON",
                description="v1 Person",
            )

        # Valid when checked independently.
        validate_object_type_codes([V0Person])
        validate_object_type_codes([V1Person])

        # Invalid when checked as one schema.
        with pytest.raises(ValueError, match="Duplicate object type code"):
            validate_object_type_codes([V0Person, V1Person])
