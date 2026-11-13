import inspect
from collections import defaultdict

import pytest

from bam_masterdata.datamodel.v1 import activities, base_objects, entities
from bam_masterdata.metadata.definitions import PropertyTypeAssignment
from bam_masterdata.metadata.entities import ObjectType

# openBIS property types are global: every assignment of a code must agree on these fields.
SHARED_FIELDS = (
    "data_type",
    "property_label",
    "description",
    "units",
    "vocabulary_code",
    "object_code",
    "multivalued",
)

# Pre-existing inconsistencies, not part of the computation schema work.
INCONSISTENT_CODES_ALLOWLIST = {
    "RESPONSIBLE_PERSON",  # property_label differs between Activity and PhysicalObject
}

# Pre-existing OBJECT properties that point to a type with subtypes, as (defining class, property code).
OBJECT_TARGET_WITH_SUBTYPES_ALLOWLIST = {
    ("Activity", "INPUT"),
    ("Activity", "OUTPUT"),
    ("Activity", "RESPONSIBLE_PERSON"),
    ("PhysicalObject", "RESPONSIBLE_PERSON"),
}


def _object_type_classes():
    return [
        cls
        for module in (base_objects, entities, activities)
        for _, cls in inspect.getmembers(module, inspect.isclass)
        if issubclass(cls, ObjectType)
        and cls.__module__ == module.__name__
        and "defs" in vars(cls)
    ]


def _assignments():
    """(defining class, assignment) for every property declared directly on a v1 class."""
    return [
        (cls, value)
        for cls in _object_type_classes()
        for value in vars(cls).values()
        if isinstance(value, PropertyTypeAssignment)
    ]


def _assignments_by_code():
    by_code = defaultdict(list)
    for cls, prop in _assignments():
        by_code[prop.code].append((cls, prop))
    return by_code


@pytest.mark.parametrize(
    "code",
    sorted(
        code
        for code, items in _assignments_by_code().items()
        if len(items) > 1 and code not in INCONSISTENT_CODES_ALLOWLIST
    ),
)
def test_shared_property_codes_have_identical_definitions(code):
    items = _assignments_by_code()[code]
    definitions = {
        cls.__name__: {field: getattr(prop, field) for field in SHARED_FIELDS}
        for cls, prop in items
    }
    first = next(iter(definitions.values()))
    assert all(d == first for d in definitions.values()), definitions


def test_object_properties_do_not_target_types_with_subtypes():
    # openBIS restricts an OBJECT property to exactly the type it names, so subtypes cannot be selected.
    codes_with_subtypes = {
        cls.defs.code
        for cls in _object_type_classes()
        if any("defs" in vars(sub) for sub in cls.__subclasses__())
    }
    offending = {
        (cls.__name__, prop.code)
        for cls, prop in _assignments()
        if prop.data_type == "OBJECT" and prop.object_code in codes_with_subtypes
    }
    assert offending <= OBJECT_TARGET_WITH_SUBTYPES_ALLOWLIST, (
        offending - OBJECT_TARGET_WITH_SUBTYPES_ALLOWLIST
    )
