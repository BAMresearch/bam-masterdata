"""Regression tests for existing v0 object type definitions."""

import pytest
from pydantic import ValidationError

from bam_masterdata.datamodel.v0.activities import Dcpd
from bam_masterdata.datamodel.v0.object_types import (
    ExperimentalStep,
    Instrument,
    TestObject,
    TestObjectBAM,
)
from bam_masterdata.datamodel.v0.welding.object_types import Welding
from bam_masterdata.metadata.definitions import ObjectTypeDef


@pytest.mark.parametrize(
    "object_type, expected_code, expected_prefix",
    [
        (ExperimentalStep, "EXPERIMENTAL_STEP", "EXP"),
        (Dcpd, "EXPERIMENTAL_STEP.DCPD", "EXP.DCPD"),
        (Instrument, "INSTRUMENT", "INS"),
        (Welding, "CONSUMABLE.WELDING", "CONS.WLD"),
        (TestObject, "TEST_OBJECT", "TEST_OBJ"),
        (TestObjectBAM, "TEST_OBJECT_BAM", "TESTO.BAM"),
    ],
)
def test_v0_codes_and_prefixes_unchanged(object_type, expected_code, expected_prefix):
    """Existing v0 identifiers and prefixes must remain unchanged."""
    assert object_type.defs.code == expected_code
    assert object_type.defs.generated_code_prefix == expected_prefix


def test_v0_dotted_code_remains_valid():
    definition = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.DCPD",
        description="DCPD",
    )

    assert definition.code == "EXPERIMENTAL_STEP.DCPD"
    assert definition.generated_code_prefix == "EXP"


def test_v0_code_remains_mandatory():
    with pytest.raises(ValidationError):
        ObjectTypeDef(description="Missing code")


def test_v0_inherited_properties_unchanged():
    """Child types must continue to inherit their parent's properties."""
    parent = ExperimentalStep()
    child = Dcpd()

    parent_codes = {prop.code for prop in parent.properties}
    child_codes = {prop.code for prop in child.properties}

    assert parent_codes
    assert parent_codes.issubset(child_codes)


def test_v0_hierarchy_does_not_modify_codes():
    """Hierarchy introspection must not change existing definitions."""
    original_code = Dcpd.defs.code
    original_prefix = Dcpd.defs.generated_code_prefix

    assert Dcpd.get_hierarchy() == [
        "EXPERIMENTAL_STEP",
        "EXPERIMENTAL_STEP.DCPD",
    ]

    assert Dcpd.is_subtype_of(ExperimentalStep)

    assert Dcpd.defs.code == original_code
    assert Dcpd.defs.generated_code_prefix == original_prefix
