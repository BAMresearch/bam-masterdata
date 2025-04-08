from pathlib import Path

from bam_masterdata.utils import DATAMODEL_DIR, VALIDATION_RULES_DIR, find_dir


def test_find_dir():
    assert find_dir(possible_locations=[Path.cwd()]) == str(Path.cwd())


def test_default_dirs():
    assert DATAMODEL_DIR == str(Path.cwd() / "bam_masterdata" / "datamodel")
    assert VALIDATION_RULES_DIR == str(
        Path.cwd() / "bam_masterdata" / "checker" / "validation_rules"
    )
