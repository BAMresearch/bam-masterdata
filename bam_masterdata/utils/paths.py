from pathlib import Path


def find_dir(possible_locations: list[Path]) -> str:
    """
    Search for a valid directory in a list of possible locations.

    Args:
        possible_locations (list[Path]): A list of possible locations to search for a directory.

    Raises:
        FileNotFoundError: If no valid directory is found.

    Returns:
        str: The path of the valid directory.
    """
    for path in possible_locations:
        if path.exists():
            return str(path.resolve())

    raise FileNotFoundError("Could not find a valid directory.")


DIRECTORIES_V0 = {
    "datamodel": [
        # Case: Running from a project with `datamodel/`
        Path.cwd() / "datamodel" / "v0",
        # Case: Running inside bam-masterdata
        Path.cwd() / "bam_masterdata" / "datamodel" / "v0",
        # Case: Running inside installed package
        Path(__file__).parent.parent / "datamodel" / "v0",
    ],
    "validation_rules_checker": [
        Path.cwd() / "bam_masterdata" / "checker" / "validation_rules",
        Path(__file__).parent.parent / "checker" / "validation_rules",
    ],
}


DATAMODEL_DIR = find_dir(possible_locations=DIRECTORIES_V0["datamodel"])
VALIDATION_RULES_DIR = find_dir(
    possible_locations=DIRECTORIES_V0["validation_rules_checker"]
)
