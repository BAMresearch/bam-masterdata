import json

import pytest

from bam_masterdata.datamodel.v1.vocabularies import (
    ActivityStatus,
    DispersionDamping,
    DispersionModel,
    JacobsLadder,
    MethodType,
    NonlocalCorrelation,
    PotentialStyle,
    PseudizationScheme,
    PseudopotentialType,
    ReferenceForm,
    RelativityApproximation,
    RelativityLevel,
    XcFunctional,
)
from bam_masterdata.metadata.definitions import VocabularyTypeDef
from bam_masterdata.metadata.entities import VocabularyType

VOCABULARY_CLASSES = [
    ActivityStatus,
    XcFunctional,
    JacobsLadder,
    ReferenceForm,
    RelativityLevel,
    RelativityApproximation,
    DispersionModel,
    DispersionDamping,
    NonlocalCorrelation,
    PotentialStyle,
    MethodType,
    PseudopotentialType,
    PseudizationScheme,
]


@pytest.mark.parametrize("cls", VOCABULARY_CLASSES, ids=lambda cls: cls.__name__)
def test_vocabulary_types_can_be_instantiated_and_exported(cls):
    vocab = cls()
    assert isinstance(vocab, VocabularyType)
    assert isinstance(cls.defs, VocabularyTypeDef)
    assert cls.defs.description.strip()
    assert vocab.terms

    exported = vocab.model_to_dict()
    assert exported["defs"]["code"] == cls.defs.code
    assert json.loads(vocab.model_to_json()) == exported


@pytest.mark.parametrize("cls", VOCABULARY_CLASSES, ids=lambda cls: cls.__name__)
def test_vocabulary_term_codes_are_unique(cls):
    codes = [term.code for term in cls().terms]
    assert len(codes) == len(set(codes))
