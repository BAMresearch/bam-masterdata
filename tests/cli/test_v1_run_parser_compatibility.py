from unittest.mock import MagicMock

import pytest

from bam_masterdata.cli.run_parser import (
    RunParsers,
    RunParsersWithTransactions,
)
from bam_masterdata.metadata.definitions import (
    ObjectTypeDef,
    PropertyTypeAssignment,
)
from bam_masterdata.metadata.entities import ObjectType
from bam_masterdata.parsing import AbstractParser


class Root(ObjectType):
    defs = ObjectTypeDef(
        code="ROOT",
        description="Root",
    )


class Person(Root):
    defs = ObjectTypeDef(
        code="PERSON",
        description="Person",
        generated_code_prefix="PER",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="Name",
        mandatory=True,
        section="General",
    )


class Instrument(Root):
    defs = ObjectTypeDef(
        code="INSTRUMENT",
        description="Instrument",
        generated_code_prefix="INS",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="Name",
        mandatory=True,
        section="General",
    )

    responsible_person = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON",
        property_label="Responsible person",
        description="Person responsible for the instrument",
        mandatory=False,
        section="General",
    )


class V1Parser(AbstractParser):
    def parse(self, files, collection, logger):
        person = Person(
            name="John Doe",
            code="PERSON_001",
        )

        instrument = Instrument(
            name="Instrument 1",
            code="INSTRUMENT_001",
        )

        instrument.responsible_person = person

        collection.add(person)
        collection.add(instrument)


@pytest.fixture
def openbis_mock():
    openbis = MagicMock()

    space = MagicMock()
    space.code = "TEST_SPACE"

    project = MagicMock()
    project.code = "TEST_PROJECT"

    collection = MagicMock()
    collection.code = "TEST_COLLECTION"

    openbis.get_space.return_value = space
    space.get_project.return_value = project
    project.get_collections.return_value = [collection]

    # Simulate objects not yet existing on the server.
    openbis.get_object.side_effect = ValueError("Object not found")

    def new_object(**kwargs):
        obj = MagicMock()
        obj.identifier = f"/TEST_SPACE/TEST_PROJECT/TEST_COLLECTION/{kwargs['code']}"
        return obj

    openbis.new_object.side_effect = new_object

    return openbis


@pytest.mark.parametrize(
    "runner_class",
    [RunParsers, RunParsersWithTransactions],
)
def test_v1_hierarchy_parsing_and_object_references(
    openbis_mock,
    runner_class,
):
    assert Person.get_hierarchy() == ["ROOT", "PERSON"]
    assert Instrument.get_hierarchy() == ["ROOT", "INSTRUMENT"]

    runner = runner_class(
        openbis=openbis_mock,
        space_name="TEST_SPACE",
        project_name="TEST_PROJECT",
        collection_name="TEST_COLLECTION",
        files_parser={V1Parser(): ["dummy.txt"]},
    )

    runner.run()

    calls = [call.kwargs for call in openbis_mock.new_object.call_args_list]

    assert len(calls) == 2

    person_call = next(call for call in calls if call["type"] == "PERSON")

    instrument_call = next(call for call in calls if call["type"] == "INSTRUMENT")

    assert person_call["code"] == "PERSON_001"
    assert instrument_call["code"] == "INSTRUMENT_001"

    assert instrument_call["props"]["responsible_person"] == (
        "/TEST_SPACE/TEST_PROJECT/TEST_COLLECTION/PERSON_001"
    )

    assert len(runner.openbis_id_map) == 2


def test_object_reference_uses_default_destination_when_not_in_batch(
    openbis_mock,
):
    runner = RunParsers(
        openbis=openbis_mock,
        space_name="TEST_SPACE",
        project_name="TEST_PROJECT",
        collection_name="TEST_COLLECTION",
        files_parser={V1Parser(): ["dummy.txt"]},
    )

    # This object is not registered in the parsing batch.
    person = Person(
        name="External Person",
        code="PERSON_EXTERNAL",
    )

    runner.openbis_id_map = {}

    identifier = runner._resolve_object_reference(
        property_name="responsible_person",
        value=person,
    )

    assert identifier == ("/TEST_SPACE/TEST_PROJECT/TEST_COLLECTION/PERSON_EXTERNAL")
