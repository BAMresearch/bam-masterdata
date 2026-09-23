import pytest
from pydantic import ValidationError

from bam_masterdata.metadata import Destination


class TestDestination:
    def test_empty_destination(self):
        destination = Destination()

        assert destination.space is None
        assert destination.project is None
        assert destination.collection is None

    def test_project_destination(self):
        destination = Destination(
            project="PROJECT_A",
        )

        assert destination.space is None
        assert destination.project == "PROJECT_A"
        assert destination.collection is None

    def test_project_and_collection_destination(self):
        destination = Destination(
            project="PROJECT_A",
            collection="COLLECTION_A",
        )

        assert destination.space is None
        assert destination.project == "PROJECT_A"
        assert destination.collection == "COLLECTION_A"

    def test_space_project_and_collection_destination(self):
        destination = Destination(
            space="SPACE_A",
            project="PROJECT_A",
            collection="COLLECTION_A",
        )

        assert destination.space == "SPACE_A"
        assert destination.project == "PROJECT_A"
        assert destination.collection == "COLLECTION_A"

    def test_collection_requires_project(self):
        with pytest.raises(
            ValidationError,
            match="`project` must be specified when `collection` is specified.",
        ):
            Destination(
                collection="COLLECTION_A",
            )
