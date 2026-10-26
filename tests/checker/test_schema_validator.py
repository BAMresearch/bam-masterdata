import pytest

from bam_masterdata.checker.schema_validator import (
    validate_object_references,
    validate_object_type_codes,
)
from bam_masterdata.metadata.definitions import (
    ObjectTypeDef,
    PropertyTypeAssignment,
)
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


class TestObjectReferenceValidation:
    class Root(ObjectType):
        defs = ObjectTypeDef(
            code="ROOT",
            description="Root",
        )

    class Person(Root):
        defs = ObjectTypeDef(
            code="PERSON",
            description="Person",
        )

    class Activity(Root):
        defs = ObjectTypeDef(
            code="ACTIVITY",
            description="Activity",
        )

        operator = PropertyTypeAssignment(
            code="OPERATOR",
            data_type="OBJECT",
            object_code="PERSON",
            property_label="Operator",
            description="Person performing the activity",
            mandatory=False,
            section="General Information",
        )

    def test_valid_reference(self):
        validate_object_references(
            [
                self.Root,
                self.Person,
                self.Activity,
            ]
        )

    def test_unknown_reference(self):
        class InvalidActivity(self.Root):
            defs = ObjectTypeDef(
                code="INVALID_ACTIVITY",
                description="Invalid activity",
            )

            operator = PropertyTypeAssignment(
                code="OPERATOR",
                data_type="OBJECT",
                object_code="UNKNOWN",
                property_label="Operator",
                description="Unknown operator",
                mandatory=False,
                section="General Information",
            )

        with pytest.raises(
            ValueError,
            match="Unknown object_code 'UNKNOWN'",
        ):
            validate_object_references(
                [
                    self.Root,
                    self.Person,
                    InvalidActivity,
                ]
            )

    @pytest.mark.parametrize("object_code", [None, "(ALL)"])
    def test_unrestricted_reference(self, object_code):
        class ActivityWithUnrestrictedReference(self.Root):
            defs = ObjectTypeDef(
                code="UNRESTRICTED_ACTIVITY",
                description="Activity with unrestricted reference",
            )

            inputs = PropertyTypeAssignment(
                code="INPUTS",
                data_type="OBJECT",
                object_code=object_code,
                property_label="Inputs",
                description="Input entities",
                mandatory=False,
                section="General Information",
            )

        validate_object_references(
            [
                self.Root,
                ActivityWithUnrestrictedReference,
            ]
        )

    def test_reference_to_parent_type(self):
        class ActivityWithParentReference(self.Root):
            defs = ObjectTypeDef(
                code="PARENT_REFERENCE_ACTIVITY",
                description="Activity referencing Root",
            )

            inputs = PropertyTypeAssignment(
                code="INPUTS",
                data_type="OBJECT",
                object_code="ROOT",
                property_label="Inputs",
                description="Input entities",
                mandatory=False,
                section="General Information",
            )

        validate_object_references(
            [
                self.Root,
                ActivityWithParentReference,
            ]
        )

    def test_inherited_reference(self):
        class SpecializedActivity(self.Activity):
            defs = ObjectTypeDef(
                code="SPECIALIZED_ACTIVITY",
                description="Specialized activity",
            )

        with pytest.raises(
            ValueError,
            match="Unknown object_code 'PERSON'",
        ):
            validate_object_references(
                [
                    self.Root,
                    SpecializedActivity,
                ]
            )

    def test_overridden_reference(self):
        class SpecializedActivity(self.Activity):
            defs = ObjectTypeDef(
                code="SPECIALIZED_ACTIVITY",
                description="Specialized activity",
            )

            operator = PropertyTypeAssignment(
                code="OPERATOR",
                data_type="OBJECT",
                object_code="ROOT",
                property_label="Operator",
                description="Overridden operator",
                mandatory=False,
                section="General Information",
            )

        validate_object_references(
            [
                self.Root,
                SpecializedActivity,
            ]
        )

    def test_separate_versions(self):
        class V0Person(ObjectType):
            defs = ObjectTypeDef(
                code="PERSON",
                description="Person in v0",
            )

        class V1Activity(ObjectType):
            defs = ObjectTypeDef(
                code="ACTIVITY_V1",
                description="Activity in v1",
            )

            operator = PropertyTypeAssignment(
                code="OPERATOR",
                data_type="OBJECT",
                object_code="PERSON",
                property_label="Operator",
                description="Operator",
                mandatory=False,
                section="General Information",
            )

        # A reference must not resolve against another schema version.
        with pytest.raises(
            ValueError,
            match="Unknown object_code 'PERSON'",
        ):
            validate_object_references([V1Activity])

        # This passes only because both classes were explicitly supplied.
        # Callers are responsible for keeping schema versions separate.
        validate_object_references([V0Person, V1Activity])
