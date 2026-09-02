import hashlib
from pathlib import Path
from unittest.mock import MagicMock

import pytest

from bam_masterdata.cli.run_parser import RunParsers, RunParsersWithTransactions
from tests.conftest import (
    InstrumentObjectType,
    PersonObjectType,
    TestParser,
    TestParserWithExistingCode,
    TestParserWithObjectReference,
    TestParserWithRelationship,
    generate_object_type,
)

TEST_FILE = Path("./tests/data/cli/test_parser.txt")


def make_runner(
    openbis_runner_mock,
    *,
    parser=None,
    collection_name: str = "TEST_COLLECTION",
    collection_type: str = "COLLECTION",
    cls=RunParsers,
):
    parser = parser or TestParser()
    return cls(
        openbis=openbis_runner_mock,
        space_name="TEST_SPACE",
        project_name="TEST_PROJECT",
        collection_name=collection_name,
        files_parser={parser: [str(TEST_FILE)]},
        collection_type=collection_type,
    )


# -----------------------------------------------------------------------------
# Initialization and openBIS hierarchy
# -----------------------------------------------------------------------------


def test_init_requires_openbis():
    with pytest.raises(ValueError, match="openBIS instance"):
        RunParsers(
            openbis=None,
            files_parser={TestParser(): [str(TEST_FILE)]},
        )


def test_init_requires_project_name(openbis_runner_mock):
    with pytest.raises(ValueError, match="project_name"):
        RunParsers(
            openbis=openbis_runner_mock,
            project_name="",
            files_parser={TestParser(): [str(TEST_FILE)]},
        )


@pytest.mark.parametrize("files_parser", [None, {}])
def test_init_requires_files_parser(openbis_runner_mock, files_parser):
    with pytest.raises(ValueError, match="At least one valid parser"):
        RunParsers(
            openbis=openbis_runner_mock,
            files_parser=files_parser,
        )


def test_init_rejects_invalid_collection_type(openbis_runner_mock):
    with pytest.raises(ValueError, match="Invalid collection_type"):
        RunParsers(
            openbis=openbis_runner_mock,
            files_parser={TestParser(): [str(TEST_FILE)]},
            collection_type="INVALID",
        )


def test_get_space_returns_requested_space(openbis_runner_mock):
    runner = make_runner(openbis_runner_mock)

    assert runner.space is openbis_runner_mock._space
    openbis_runner_mock.get_space.assert_called_with("TEST_SPACE")


def test_get_space_falls_back_to_user_space(openbis_runner_mock):
    fallback = MagicMock()
    fallback.code = "USER_TESTUSER"
    openbis_runner_mock.get_space.side_effect = RuntimeError("not found")
    openbis_runner_mock.get_spaces.return_value = [fallback]

    runner = RunParsers(
        openbis=openbis_runner_mock,
        space_name="MISSING",
        project_name="TEST_PROJECT",
        collection_name="",
        files_parser={TestParser(): [str(TEST_FILE)]},
    )

    assert runner.space is fallback


def test_get_space_raises_when_no_requested_or_fallback_space(openbis_runner_mock):
    openbis_runner_mock.get_space.side_effect = RuntimeError("not found")
    openbis_runner_mock.get_spaces.return_value = []

    with pytest.raises(ValueError, match="No space found"):
        RunParsers(
            openbis=openbis_runner_mock,
            space_name="MISSING",
            project_name="TEST_PROJECT",
            files_parser={TestParser(): [str(TEST_FILE)]},
        )


def test_get_project_creates_missing_project(openbis_runner_mock):
    space = openbis_runner_mock._space
    space.get_project.side_effect = RuntimeError("not found")

    created_project = MagicMock()
    created_project.code = "MY_PROJECT"
    created_project.get_collections.return_value = []
    space.new_project.return_value = created_project

    runner = RunParsers(
        openbis=openbis_runner_mock,
        space_name="TEST_SPACE",
        project_name="My Project",
        collection_name="",
        files_parser={TestParser(): [str(TEST_FILE)]},
    )

    assert runner.project is created_project
    space.new_project.assert_called_once()
    kwargs = space.new_project.call_args.kwargs
    assert kwargs["code"] == "MY_PROJECT"
    created_project.save.assert_called_once()


def test_no_collection_uses_project(openbis_runner_mock):
    runner = make_runner(openbis_runner_mock, collection_name="")

    assert runner.collection_openbis is runner.project
    openbis_runner_mock.new_collection.assert_not_called()


def test_existing_collection_is_reused(openbis_runner_mock):
    existing = MagicMock()
    existing.code = "TEST_COLLECTION"
    openbis_runner_mock._project.get_collections.return_value = [existing]

    runner = make_runner(openbis_runner_mock)

    assert runner.collection_openbis is existing
    openbis_runner_mock.new_collection.assert_not_called()


def test_missing_collection_is_created_with_normalized_code(openbis_runner_mock):
    runner = RunParsers(
        openbis=openbis_runner_mock,
        space_name="TEST_SPACE",
        project_name="TEST_PROJECT",
        collection_name="My Collection",
        files_parser={TestParser(): [str(TEST_FILE)]},
        collection_type="DEFAULT_EXPERIMENT",
    )

    assert runner.collection_openbis is openbis_runner_mock._collection
    openbis_runner_mock.new_collection.assert_called_once_with(
        code="MY_COLLECTION",
        type="DEFAULT_EXPERIMENT",
        project=openbis_runner_mock._project,
    )
    openbis_runner_mock._collection.save.assert_called_once()


# -----------------------------------------------------------------------------
# Parsing, hashing and identifiers
# -----------------------------------------------------------------------------


def test_parsing_delegates_files_collection_and_logger(openbis_runner_mock):
    parser = MagicMock()
    runner = make_runner(openbis_runner_mock, parser=parser)

    runner.parsing()

    parser.parse.assert_called_once_with(
        [str(TEST_FILE)],
        runner.collection,
        logger=runner.logger,
    )


def test_content_hash_is_deterministic_and_respects_length(openbis_runner_mock):
    runner = make_runner(openbis_runner_mock)
    obj = generate_object_type(name="Same content")

    expected = hashlib.sha256(obj.to_json().encode("utf-8")).hexdigest()[:12]

    assert runner._content_hash(obj, length=12) == expected
    assert runner._content_hash(obj, length=12) == runner._content_hash(obj, length=12)


def test_identifier_uses_explicit_code(openbis_runner_mock):
    runner = make_runner(openbis_runner_mock)
    obj = generate_object_type(code="EXPLICIT_CODE")

    assert (
        runner._identifier(obj)
        == "/TEST_SPACE/TEST_PROJECT/TEST_COLLECTION/EXPLICIT_CODE"
    )
    assert obj.code == "EXPLICIT_CODE"


def test_identifier_generates_code_from_prefix_and_content_hash(openbis_runner_mock):
    runner = make_runner(openbis_runner_mock)
    obj = generate_object_type(name="Generated")
    expected_hash = runner._content_hash(obj)

    identifier = runner._identifier(obj)

    assert obj.code == f"MOCKOBJTYPE_{expected_hash}"
    assert identifier == (
        f"/TEST_SPACE/TEST_PROJECT/TEST_COLLECTION/MOCKOBJTYPE_{expected_hash}"
    )


def test_generated_identifier_is_deterministic_for_same_content(openbis_runner_mock):
    runner = make_runner(openbis_runner_mock)
    first = generate_object_type(name="Same")
    second = generate_object_type(name="Same")

    assert runner._identifier(first) == runner._identifier(second)


def test_identifier_without_collection_uses_project_path(openbis_runner_mock):
    runner = make_runner(openbis_runner_mock, collection_name="")
    obj = generate_object_type(code="OBJ_1")

    assert runner._identifier(obj) == "/TEST_SPACE/TEST_PROJECT/OBJ_1"


# -----------------------------------------------------------------------------
# OBJECT property resolution and property mapping
# -----------------------------------------------------------------------------


def test_resolve_object_reference_from_existing_path(openbis_runner_mock):
    runner = make_runner(openbis_runner_mock)
    identifier = "/TEST_SPACE/TEST_PROJECT/TEST_COLLECTION/PERSON_001"
    referenced = MagicMock()
    referenced.identifier = identifier
    openbis_runner_mock._registry[identifier] = referenced

    assert (
        runner._resolve_object_reference("responsible_person", identifier) == identifier
    )


def test_resolve_object_reference_returns_none_for_missing_path(openbis_runner_mock):
    runner = make_runner(openbis_runner_mock)

    assert (
        runner._resolve_object_reference(
            "responsible_person",
            "/TEST_SPACE/TEST_PROJECT/TEST_COLLECTION/MISSING",
        )
        is None
    )


def test_resolve_object_reference_prefers_batch_identifier_map(openbis_runner_mock):
    runner = make_runner(openbis_runner_mock)
    person = PersonObjectType(name="John", code="PERSON_001")
    local_id = runner.collection.add(person)
    runner.openbis_id_map = {local_id: "/CUSTOM/IDENTIFIER/PERSON_001"}

    assert (
        runner._resolve_object_reference("responsible_person", person)
        == "/CUSTOM/IDENTIFIER/PERSON_001"
    )


def test_resolve_object_reference_constructs_identifier_when_not_mapped(
    openbis_runner_mock,
):
    runner = make_runner(openbis_runner_mock)
    runner.openbis_id_map = {}
    person = PersonObjectType(name="John", code="PERSON_001")

    assert runner._resolve_object_reference("responsible_person", person) == (
        "/TEST_SPACE/TEST_PROJECT/TEST_COLLECTION/PERSON_001"
    )


def test_resolve_object_reference_without_code_returns_none(openbis_runner_mock):
    runner = make_runner(openbis_runner_mock)
    runner.openbis_id_map = {}
    person = PersonObjectType(name="John")

    assert runner._resolve_object_reference("responsible_person", person) is None


def test_load_openbis_props_maps_property_codes_to_lowercase(openbis_runner_mock):
    runner = make_runner(openbis_runner_mock)
    obj = generate_object_type(name="Sample", code="OBJ_1")
    obj.alias = "alias"

    props = runner._load_openbis_props(obj)

    assert props["$name"] == "Sample"
    assert props["alias"] == "alias"


def test_load_openbis_props_resolves_object_property(openbis_runner_mock):
    runner = make_runner(openbis_runner_mock)
    runner.openbis_id_map = {}
    person = PersonObjectType(name="John", code="PERSON_001")
    instrument = InstrumentObjectType(name="Instrument", code="INS_001")
    instrument.responsible_person = person

    props = runner._load_openbis_props(instrument)

    assert props["responsible_person"] == (
        "/TEST_SPACE/TEST_PROJECT/TEST_COLLECTION/PERSON_001"
    )


def test_load_openbis_props_skips_unresolved_object_property(openbis_runner_mock):
    runner = make_runner(openbis_runner_mock)
    runner.openbis_id_map = {}
    person = PersonObjectType(name="John")
    instrument = InstrumentObjectType(name="Instrument", code="INS_001")
    instrument.responsible_person = person

    props = runner._load_openbis_props(instrument)

    assert "responsible_person" not in props


# -----------------------------------------------------------------------------
# Datasets
# -----------------------------------------------------------------------------


def test_save_datasets_does_nothing_when_object_has_no_datasets(openbis_runner_mock):
    runner = make_runner(openbis_runner_mock)
    obj = generate_object_type(code="OBJ_1")

    runner._save_datasets(obj, "/TEST_SPACE/TEST_PROJECT/TEST_COLLECTION/OBJ_1")

    openbis_runner_mock.new_dataset.assert_not_called()


def test_save_datasets_attaches_files_to_object(openbis_runner_mock):
    runner = make_runner(openbis_runner_mock)
    obj = generate_object_type(code="OBJ_1")
    obj.datasets.extend(["a.dat", "b.dat"])
    identifier = "/TEST_SPACE/TEST_PROJECT/TEST_COLLECTION/OBJ_1"

    runner._save_datasets(obj, identifier)

    openbis_runner_mock.new_dataset.assert_called_once_with(
        type="RAW_DATA",
        sample=identifier,
        files=["a.dat", "b.dat"],
    )
    openbis_runner_mock._datasets[-1].save.assert_called_once()


def test_attach_datasets_attaches_parser_files_to_collection(openbis_runner_mock):
    runner = make_runner(openbis_runner_mock)

    runner._attach_datasets()

    openbis_runner_mock.new_dataset.assert_called_once_with(
        type="RAW_DATA",
        files=[str(TEST_FILE)],
        collection=runner.collection_openbis,
    )
    openbis_runner_mock._datasets[-1].save.assert_called_once()


def test_attach_datasets_skips_when_objects_are_directly_under_project(
    openbis_runner_mock,
):
    runner = make_runner(openbis_runner_mock, collection_name="")

    runner._attach_datasets()

    openbis_runner_mock.new_dataset.assert_not_called()


# -----------------------------------------------------------------------------
# Relationship resolution
# -----------------------------------------------------------------------------


def test_get_openbis_obj_resolves_local_object_id(openbis_runner_mock):
    runner = make_runner(openbis_runner_mock)
    object_id = "LOCAL_ID"
    identifier = "/TEST_SPACE/TEST_PROJECT/TEST_COLLECTION/OBJ_1"
    obj = MagicMock()
    obj.identifier = identifier
    runner.openbis_id_map = {object_id: identifier}
    openbis_runner_mock._registry[identifier] = obj

    assert runner._get_openbis_obj(object_id, "parent") is obj


def test_get_openbis_obj_resolves_dictionary_identifier(openbis_runner_mock):
    runner = make_runner(openbis_runner_mock)
    identifier = "/TEST_SPACE/TEST_PROJECT/TEST_COLLECTION/OBJ_1"
    obj = MagicMock()
    obj.identifier = identifier
    openbis_runner_mock._registry[identifier] = obj

    assert runner._get_openbis_obj({"identifier": identifier}, "parent") is obj


@pytest.mark.parametrize("key", ["identifier", "code", "permId"])
def test_get_openbis_obj_accepts_supported_dictionary_keys(openbis_runner_mock, key):
    runner = make_runner(openbis_runner_mock)
    identifier = "VALUE"
    obj = MagicMock()
    openbis_runner_mock._registry[identifier] = obj

    assert runner._get_openbis_obj({key: identifier}, "parent") is obj


def test_get_openbis_obj_returns_none_for_unknown_local_id(openbis_runner_mock):
    runner = make_runner(openbis_runner_mock)
    runner.openbis_id_map = {}

    assert runner._get_openbis_obj("UNKNOWN", "parent") is None


def test_get_openbis_obj_returns_none_for_invalid_dictionary(openbis_runner_mock):
    runner = make_runner(openbis_runner_mock)

    assert runner._get_openbis_obj({"name": "not an identifier"}, "parent") is None


def test_load_relationship_objs_returns_both_objects(openbis_runner_mock):
    runner = make_runner(openbis_runner_mock)
    parent = MagicMock()
    child = MagicMock()
    parent.identifier = "/PARENT"
    child.identifier = "/CHILD"
    runner.openbis_id_map = {"p": "/PARENT", "c": "/CHILD"}
    openbis_runner_mock._registry.update({"/PARENT": parent, "/CHILD": child})

    assert runner._load_relationship_objs("p", "c") == (parent, child)


def test_load_relationship_objs_returns_none_pair_if_one_is_missing(
    openbis_runner_mock,
):
    runner = make_runner(openbis_runner_mock)
    parent = MagicMock()
    runner.openbis_id_map = {"p": "/PARENT"}
    openbis_runner_mock._registry["/PARENT"] = parent

    assert runner._load_relationship_objs("p", "missing") == (None, None)


# -----------------------------------------------------------------------------
# RunParsers workflow
# -----------------------------------------------------------------------------


def test_run_creates_new_object_and_populates_identifier_map(openbis_runner_mock):
    runner = make_runner(openbis_runner_mock, parser=TestParserWithExistingCode())

    runner.run()

    identifier = "/TEST_SPACE/TEST_PROJECT/TEST_COLLECTION/EXISTING_OBJ_0001"
    assert identifier in openbis_runner_mock._registry
    assert identifier in runner.openbis_id_map.values()
    openbis_runner_mock.new_object.assert_called_once()


def test_run_updates_existing_object_instead_of_creating(openbis_runner_mock):
    runner = make_runner(openbis_runner_mock, parser=TestParserWithExistingCode())
    identifier = "/TEST_SPACE/TEST_PROJECT/TEST_COLLECTION/EXISTING_OBJ_0001"
    existing = MagicMock()
    existing.identifier = identifier
    openbis_runner_mock._registry[identifier] = existing

    runner.run()

    existing.set_props.assert_called_once()
    existing.save.assert_called_once()
    openbis_runner_mock.new_object.assert_not_called()


def test_run_without_collection_creates_object_under_project(openbis_runner_mock):
    runner = make_runner(
        openbis_runner_mock,
        parser=TestParserWithExistingCode(),
        collection_name="",
    )

    runner.run()

    kwargs = openbis_runner_mock.new_object.call_args.kwargs
    assert "collection" not in kwargs
    assert kwargs["space"] is runner.space
    assert kwargs["project"] is runner.project


def test_run_creates_parent_child_relationship(openbis_runner_mock):
    runner = make_runner(openbis_runner_mock, parser=TestParserWithRelationship())

    runner.run()

    assert len(runner.openbis_id_map) == 2
    parent_id, child_id = list(runner.openbis_id_map.values())
    parent = openbis_runner_mock._registry[parent_id]
    child = openbis_runner_mock._registry[child_id]
    child.add_parents.assert_called_once_with(parent)
    # New objects are saved once during creation and child is saved again after linking.
    assert child.save.call_count == 2


def test_run_resolves_object_instance_and_path_references(openbis_runner_mock):
    runner = make_runner(openbis_runner_mock, parser=TestParserWithObjectReference())

    runner.run()

    assert len(runner.openbis_id_map) == 3
    calls = openbis_runner_mock.new_object.call_args_list
    instrument_calls = [
        call.kwargs for call in calls if call.kwargs["type"] == "INSTRUMENT"
    ]
    assert len(instrument_calls) == 2
    assert all("responsible_person" in call["props"] for call in instrument_calls)


# -----------------------------------------------------------------------------
# RunParsersWithTransactions workflow
# -----------------------------------------------------------------------------


def test_transactional_run_uses_one_object_and_one_relationship_transaction(
    openbis_runner_mock,
):
    runner = make_runner(
        openbis_runner_mock,
        parser=TestParserWithRelationship(),
        cls=RunParsersWithTransactions,
    )

    runner.run()

    assert openbis_runner_mock.new_transaction.call_count == 2
    object_transaction, relationship_transaction = openbis_runner_mock._transactions
    object_transaction.commit.assert_called_once()
    relationship_transaction.commit.assert_called_once()
    assert len(object_transaction.objects) == 2
    assert len(relationship_transaction.objects) == 1


def test_transactional_run_creates_new_object_in_object_transaction(
    openbis_runner_mock,
):
    runner = make_runner(
        openbis_runner_mock,
        parser=TestParserWithExistingCode(),
        cls=RunParsersWithTransactions,
    )

    runner.run()

    object_transaction = openbis_runner_mock._transactions[0]
    assert len(object_transaction.objects) == 1
    identifier = "/TEST_SPACE/TEST_PROJECT/TEST_COLLECTION/EXISTING_OBJ_0001"
    assert identifier in runner.openbis_id_map.values()
    assert identifier in openbis_runner_mock._registry


def test_transactional_run_updates_existing_object(openbis_runner_mock):
    runner = make_runner(
        openbis_runner_mock,
        parser=TestParserWithExistingCode(),
        cls=RunParsersWithTransactions,
    )
    identifier = "/TEST_SPACE/TEST_PROJECT/TEST_COLLECTION/EXISTING_OBJ_0001"
    existing = MagicMock()
    existing.identifier = identifier
    openbis_runner_mock._registry[identifier] = existing

    runner.run()

    existing.set_props.assert_called_once()
    openbis_runner_mock.new_object.assert_not_called()
    assert openbis_runner_mock._transactions[0].objects == [existing]


def test_transactional_run_stops_if_object_transaction_fails(openbis_runner_mock):
    runner = make_runner(
        openbis_runner_mock,
        parser=TestParserWithExistingCode(),
        cls=RunParsersWithTransactions,
    )

    # Transaction is created lazily by run().
    failing_transaction = MagicMock()
    failing_transaction.objects = []
    failing_transaction.add.side_effect = failing_transaction.objects.append
    failing_transaction.commit.side_effect = RuntimeError("commit failed")
    openbis_runner_mock.new_transaction.side_effect = [failing_transaction]

    runner.run()

    failing_transaction.commit.assert_called_once()
    openbis_runner_mock.new_dataset.assert_not_called()


def test_transactional_run_skips_unresolvable_relationship(openbis_runner_mock):
    runner = make_runner(
        openbis_runner_mock,
        parser=TestParserWithRelationship(),
        cls=RunParsersWithTransactions,
    )

    # Resolve object lookups during relationship phase as missing after object commit.
    original_get_object = openbis_runner_mock.get_object.side_effect
    call_count = {"value": 0}

    def get_object_with_missing_relationship(identifier):
        call_count["value"] += 1
        # First two lookups are object existence checks; relationship lookups come later.
        if call_count["value"] > 2:
            raise KeyError(identifier)
        return original_get_object(identifier)

    openbis_runner_mock.get_object.side_effect = get_object_with_missing_relationship

    runner.run()

    relationship_transaction = openbis_runner_mock._transactions[1]
    assert relationship_transaction.objects == []
    relationship_transaction.commit.assert_called_once()


def test_transactional_run_handles_relationship_commit_failure(openbis_runner_mock):
    runner = make_runner(
        openbis_runner_mock,
        parser=TestParserWithRelationship(),
        cls=RunParsersWithTransactions,
    )

    object_transaction = MagicMock()
    object_transaction.objects = []
    object_transaction.add.side_effect = object_transaction.objects.append

    def commit_objects():
        for obj in object_transaction.objects:
            openbis_runner_mock._registry[obj.identifier] = obj

    object_transaction.commit.side_effect = commit_objects

    relationship_transaction = MagicMock()
    relationship_transaction.objects = []
    relationship_transaction.add.side_effect = relationship_transaction.objects.append
    relationship_transaction.commit.side_effect = RuntimeError("relationship failed")

    openbis_runner_mock.new_transaction.side_effect = [
        object_transaction,
        relationship_transaction,
    ]

    runner.run()

    object_transaction.commit.assert_called_once()
    relationship_transaction.commit.assert_called_once()


@pytest.mark.parametrize("runner_cls", [RunParsers, RunParsersWithTransactions])
def test_both_runners_support_default_experiment_collection_type(
    openbis_runner_mock,
    runner_cls,
):
    runner = make_runner(
        openbis_runner_mock,
        collection_type="DEFAULT_EXPERIMENT",
        cls=runner_cls,
    )

    assert runner.collection_openbis is openbis_runner_mock._collection
    assert (
        openbis_runner_mock.new_collection.call_args.kwargs["type"]
        == "DEFAULT_EXPERIMENT"
    )
