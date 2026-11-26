import json

from bam_masterdata.metadata.entities import ObjectType

# OBJECT properties approved to have no target type (object_code=None).
UNRESTRICTED_OBJECT_PROPERTIES = {
    "REPRESENTED_MATERIAL",  # MATERIAL and SAMPLE have subtypes
}


def test_types_can_be_instantiated_and_exported(v1_type):
    obj = v1_type()
    exported = obj.model_to_dict()
    assert exported["defs"]["code"] == v1_type.defs.code
    assert json.loads(obj.model_to_json()) == exported
    if isinstance(obj, ObjectType):
        codes = [prop.code for prop in obj.properties]
        assert len(codes) == len(set(codes))
        assert {prop["code"] for prop in exported["properties"]} == set(codes)


def test_vocabulary_and_object_references_resolve(v1_object_type, v1_reference_codes):
    object_codes, vocabulary_codes = v1_reference_codes
    for prop in v1_object_type().properties:
        if prop.data_type == "CONTROLLEDVOCABULARY":
            assert prop.vocabulary_code in vocabulary_codes, prop.code
        if prop.data_type == "OBJECT":
            if prop.object_code is None:
                # Unrestricted references need approval (AGENTS.md); list them here.
                assert prop.code in UNRESTRICTED_OBJECT_PROPERTIES, prop.code
            else:
                assert prop.object_code in object_codes, prop.code
