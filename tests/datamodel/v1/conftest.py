import importlib
import inspect
import pkgutil

import pytest

from bam_masterdata.checker.schema_validator import get_object_types
from bam_masterdata.datamodel import v1
from bam_masterdata.metadata.entities import VocabularyType

OBJECT_TYPES = get_object_types("v1")
VOCABULARY_TYPES = sorted(
    {
        cls
        for info in pkgutil.walk_packages(v1.__path__, prefix=f"{v1.__name__}.")
        for module in [importlib.import_module(info.name)]
        for _, cls in inspect.getmembers(module, inspect.isclass)
        if cls.__module__ == module.__name__
        and issubclass(cls, VocabularyType)
        and "defs" in vars(cls)
    },
    key=lambda cls: (cls.__module__, cls.__name__),
)


@pytest.fixture(params=OBJECT_TYPES + VOCABULARY_TYPES, ids=lambda cls: cls.__name__)
def v1_type(request):
    return request.param


@pytest.fixture(params=OBJECT_TYPES, ids=lambda cls: cls.__name__)
def v1_object_type(request):
    return request.param


@pytest.fixture(params=VOCABULARY_TYPES, ids=lambda cls: cls.__name__)
def v1_vocabulary_type(request):
    return request.param


@pytest.fixture
def v1_reference_codes():
    return (
        {cls.defs.code for cls in OBJECT_TYPES},
        {cls.defs.code for cls in VOCABULARY_TYPES},
    )
