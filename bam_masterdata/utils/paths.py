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


DIRECTORIES = {
    "datamodel": [
        # Case: Running from a project with `datamodel/`
        Path.cwd() / "datamodel",
        # Case: Running inside bam-masterdata
        Path.cwd() / "bam_masterdata" / "datamodel",
        # Case: Running inside installed package
        Path(__file__).parent.parent / "datamodel",
    ],
    "validation_rules_checker": [
        Path.cwd() / "bam_masterdata" / "checker" / "validation_rules",
        Path(__file__).parent.parent / "checker" / "validation_rules",
    ],
}


DATAMODEL_DIR = find_dir(possible_locations=DIRECTORIES["datamodel"])
VALIDATION_RULES_DIR = find_dir(
    possible_locations=DIRECTORIES["validation_rules_checker"]
)
