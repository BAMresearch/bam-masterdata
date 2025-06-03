import glob
import inspect
import json
import os
import shutil
import time
from pathlib import Path

import click
from decouple import config as environ
from openpyxl import Workbook
from rdflib import Graph

from bam_masterdata.checker import MasterdataChecker
from bam_masterdata.cli.entities_to_excel import entities_to_excel
from bam_masterdata.cli.entities_to_rdf import entities_to_rdf
from bam_masterdata.cli.fill_masterdata import MasterdataCodeGenerator
from bam_masterdata.logger import logger
from bam_masterdata.metadata.entities_dict import EntitiesDict
from bam_masterdata.openbis.login import ologin
from bam_masterdata.utils import (
    DATAMODEL_DIR,
    delete_and_create_dir,
    duplicated_property_types,
    import_module,
    listdir_py_modules,
)


@click.group(help="Entry point to run `bam_masterdata` CLI commands.")
def cli():
    pass


@cli.command(
    name="fill_masterdata",
    help="Fill the masterdata from the openBIS instance and stores it in the bam_masterdata/datamodel/ modules.",
)
@click.option(
    "--url",
    type=str,
    required=False,
    help="""
    (Optional) The URL of the openBIS instance from which to extract the data model. If not defined,
    it is using the value of the `OPENBIS_URL` environment variable.
    """,
)
@click.option(
    "--excel-file",
    type=click.Path(exists=True, dir_okay=False),
    required=False,
    help="""
    (Optional) The path to the Masterdata Excel file.
    """,
)
@click.option(
    "--export-dir",
    type=str,
    required=False,
    help="The directory where the Masterdata will be exported to.",
)
@click.option(
    "--row-cell-info",
    type=bool,
    required=False,
    default=False,
    help="""
    (Optional) If when exporting the masterdata from the Excel file, the information of which row in the Excel
    each field is defined should be stored (useful for the `checker` CLI).
    """,
)
def fill_masterdata(url, excel_file, export_dir, row_cell_info):
    start_time = time.time()

    # Define output directory
    if export_dir is not None:
        output_directory = export_dir
    else:
        output_directory = (
            os.path.join(DATAMODEL_DIR, "tmp") if excel_file else DATAMODEL_DIR
        )

    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Check for mutual exclusivity
    if excel_file and url:
        raise click.UsageError(
            "You cannot specify both --url and --excel-file. Please choose one."
        )

    # ! this takes a lot of time loading all the entities in Openbis
    # Use the URL if provided, otherwise fall back to defaults
    if excel_file:
        click.echo(f"Using the Masterdata Excel file path: {excel_file}\n")
        if row_cell_info:
            click.echo("Cell information will be stored in the Python fields.")
        generator = MasterdataCodeGenerator(
            path=excel_file, row_cell_info=row_cell_info
        )
    else:
        if not url:
            url = environ("OPENBIS_URL")
        click.echo(f"Using the openBIS instance: {url}\n")
        generator = MasterdataCodeGenerator(url=url)

    # Add each module to the `bam_masterdata/datamodel` directory
    # for module_name in ["property", "collection", "dataset", "object", "vocabulary"]:
    for module_name in ["collection", "dataset", "object", "vocabulary"]:
        module_start_time = time.perf_counter()  # more precise time measurement
        output_file = Path(os.path.join(output_directory, f"{module_name}_types.py"))

        # Get the method from `MasterdataCodeGenerator`
        code = getattr(generator, f"generate_{module_name}_types")().rstrip()

        if code != "":
            output_file.write_text(code + "\n", encoding="utf-8")
            module_elapsed_time = time.perf_counter() - module_start_time
            click.echo(
                f"Generated {module_name} types in {module_elapsed_time:.2f} seconds in {output_file}\n"
            )
        else:
            click.echo(f"Skipping {module_name}_types.py (empty entity data)")

    elapsed_time = time.time() - start_time
    click.echo(f"Generated all types in {elapsed_time:.2f} seconds\n\n")

    # ! for some reason this ruff is not working; apply after using the CLI
    # try:
    #     # Run ruff check
    #     click.echo("Running `ruff check .`...")
    #     subprocess.run(["ruff", "check", "."], check=True)

    #     # Run ruff format
    #     click.echo("Running `ruff format .`...")
    #     subprocess.run(["ruff", "format", "."], check=True)
    # except subprocess.CalledProcessError as e:
    #     click.echo(f"Error during ruff execution: {e}", err=True)
    # else:
    #     click.echo("Ruff checks and formatting completed successfully!")


@cli.command(
    name="export_to_json",
    help="Export entities to JSON files to the `./artifacts/` folder.",
)
@click.option(
    "--force-delete",
    type=bool,
    required=False,
    default=False,
    help="""
    (Optional) If set to `True`, it will delete the current `./artifacts/` folder and create a new one. Default is `False`.
    """,
)
@click.option(
    "--python-path",
    type=str,
    required=False,
    default=DATAMODEL_DIR,
    help="""
    (Optional) The path to the individual Python module or the directory containing the Python modules to process the datamodel.
    Default is the `/datamodel/` directory.
    """,
)
@click.option(
    "--export-dir",
    type=str,
    required=False,
    default="./artifacts",
    help="The directory where the JSON files will be exported. Default is `./artifacts`.",
)
@click.option(
    "--single-json",
    type=bool,
    default=False,
    help="Whether the export to JSON is done to a single JSON file. Default is False.",
)
def export_to_json(force_delete, python_path, export_dir, single_json):
    # Delete and create the export directory
    if force_delete:
        click.confirm(
            f"Are you sure you want to delete the directory {export_dir}?",
            abort=True,
        )
    delete_and_create_dir(
        directory_path=export_dir,
        logger=logger,
        force_delete=force_delete,
    )

    # Instantiating the class to get the entities in a dictionary from Python
    entities_dict = EntitiesDict(python_path=python_path, logger=logger)

    full_data = entities_dict.single_json()
    if single_json:
        output_file = os.path.join(export_dir, "masterdata.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(full_data, f, indent=2)
    else:
        for entity_type, entity_data in full_data.items():
            # export to specific subfolders for each type of entity (each module)
            module_export_dir = os.path.join(export_dir, os.path.basename(entity_type))
            delete_and_create_dir(directory_path=module_export_dir, logger=logger)
            for name, data in entity_data.items():
                output_file = os.path.join(module_export_dir, f"{name}.json")
                with open(output_file, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2)
                    click.echo(f"Exported {name} to {output_file}")

    click.echo(f"All entity artifacts have been generated and saved to {export_dir}")


@cli.command(
    name="export_to_excel",
    help="Export entities to an Excel file in the path `./artifacts/masterdata.xlsx`.",
)
@click.option(
    "--force-delete",
    type=bool,
    required=False,
    default=False,
    help="""
    (Optional) If set to `True`, it will delete the current `./artifacts/` folder and create a new one. Default is `False`.
    """,
)
@click.option(
    "--python-path",
    type=str,
    required=False,
    default=DATAMODEL_DIR,
    help="""
    (Optional) The path to the individual Python module or the directory containing the Python modules to process the datamodel.
    Default is the `/datamodel/` directory.
    """,
)
@click.option(
    "--export-dir",
    type=str,
    required=False,
    default="./artifacts",
    help="The directory where the Excel file will be exported. Default is `./artifacts`.",
)
def export_to_excel(force_delete, python_path, export_dir):
    # Delete and create the export directory
    if force_delete:
        click.confirm(
            f"Are you sure you want to delete the directory {export_dir}?",
            abort=True,
        )
    delete_and_create_dir(
        directory_path=export_dir,
        logger=logger,
        force_delete=force_delete,
    )

    # Get the Python modules to process the datamodel
    py_modules = listdir_py_modules(directory_path=python_path, logger=logger)

    # Load the definitions module classes
    definitions_path = Path(__file__).parent / ".." / "metadata" / "definitions.py"
    definitions_module = import_module(module_path=str(definitions_path.resolve()))

    # Process the modules and save the entities to the openBIS masterdata Excel file
    masterdata_file = os.path.join(export_dir, "masterdata.xlsx")
    wb = Workbook()
    for i, module_path in enumerate(py_modules):
        if module_path.endswith("property_types.py"):
            if duplicated_property_types(module_path=module_path, logger=logger):
                click.echo(
                    "Please fix the duplicated property types before exporting to Excel."
                )
                return
        if i == 0:
            ws = wb.active
        else:
            ws = wb.create_sheet()
        ws.title = (
            os.path.basename(module_path)
            .capitalize()
            .replace(".py", "")
            .replace("_", " ")
        )
        entities_to_excel(
            worksheet=ws,
            module_path=module_path,
            definitions_module=definitions_module,
        )
    wb.save(masterdata_file)

    click.echo(f"All masterdata have been generated and saved to {masterdata_file}")


@cli.command(
    name="export_to_rdf",
    help="Export entities to a RDF/XML file in the path `./artifacts/bam_masterdata.owl`.",
)
@click.option(
    "--force-delete",
    type=bool,
    required=False,
    default=False,
    help="""
    (Optional) If set to `True`, it will delete the current `./artifacts/` folder and create a new one. Default is `False`.
    """,
)
@click.option(
    "--python-path",
    type=str,
    required=False,
    default=DATAMODEL_DIR,
    help="""
    (Optional) The path to the individual Python module or the directory containing the Python modules to process the datamodel.
    Default is `./bam_masterdata/datamodel/`.
    """,
)
@click.option(
    "--export-dir",
    type=str,
    required=False,
    default="./artifacts",
    help="The directory where the RDF/XML file will be exported. Default is `./artifacts`.",
)
def export_to_rdf(force_delete, python_path, export_dir):
    # Delete and create the export directory
    if force_delete:
        click.confirm(
            f"Are you sure you want to delete the directory {export_dir}?",
            abort=True,
        )
    delete_and_create_dir(
        directory_path=export_dir,
        logger=logger,
        force_delete=force_delete,
    )

    # Get the Python modules to process the datamodel
    py_modules = listdir_py_modules(directory_path=python_path, logger=logger)
    # ! Remove the module containing 'vocabulary_types.py'
    py_modules = [
        module for module in py_modules if "vocabulary_types.py" not in module
    ]

    # Process each module using the `model_to_rdf` method of each entity
    graph = Graph()
    for module_path in py_modules:
        entities_to_rdf(graph=graph, module_path=module_path, logger=logger)

    # Saving RDF/XML to file
    rdf_output = graph.serialize(format="pretty-xml")
    masterdata_file = os.path.join(export_dir, "masterdata.owl")
    with open(masterdata_file, "w", encoding="utf-8") as f:
        f.write(rdf_output)

    click.echo(
        f"All masterdata has been generated in RDF/XML format and saved to {masterdata_file}"
    )


def run_checker(file_path: str, mode: str = "all", datamodel_path: str = DATAMODEL_DIR):
    """

    Run the masterdata checker on the specified file path and mode.

    Args:
        file_path (str): The path to the file or directory containing Python modules or the Excel file to be checked.
        mode (str, optional): The mode for the checker. Defaults to "all". Options are:
            "self" -> Validate only the current data model.
            "incoming" -> Validate only the new entity structure.
            "validate" -> Validate both the current model and new entities.
            "compare" -> Compare new entities against the current model.
            "all" -> Run all validations and comparison. (Default).
            "individual" -> Run individual repositories validations.
        datamodel_path (str, optional): Path to the directory containing the Python modules defining the datamodel. Defaults to DATAMODEL_DIR.
    """
    # Instantiate the checker class and run validation
    checker = MasterdataChecker()

    # Load current model from datamodel path
    checker.load_current_model(datamodel_dir=datamodel_path)

    # Load new entities from the specified file path (could be a Python file, directory, or Excel)
    checker.load_new_entities(source=file_path)

    # Run the checker in the specified mode
    validation_results = checker.check(mode=mode)

    # Check if there are problems with the current model
    if mode in ["self", "all", "validate"] and validation_results.get(
        "current_model", {}
    ):
        for entity, errors in validation_results.get("current_model", {}).items():
            if errors:
                click.echo(
                    f"There are problems in the current model for entity {entity} that need to be solved"
                )

    # Check if there are problems with the incoming model
    if mode in ["incoming", "all", "validate"] and validation_results.get(
        "incoming_model", {}
    ):
        for entity, errors in validation_results.get("incoming_model", {}).items():
            if errors:
                click.echo(
                    f"There are problems in the incoming model in {file_path} for entity {entity} that need to be solved"
                )

    # Check if there are comparison problems
    if mode in ["compare", "all"] and validation_results.get("comparisons", {}):
        for entity, errors in validation_results.get("comparisons", {}).items():
            if errors:
                click.echo(
                    f"There are problems when checking the incoming model in {file_path} against the current model {datamodel_path} for entity {entity} that need to be solved"
                )

    # Check if there are individual repository problems
    if (
        mode in ["individual"]
        and validation_results.get("incoming_model", {})
        and validation_results.get("comparisons", {})
    ):
        for entity, errors in validation_results.get("individual", {}).items():
            if errors:
                click.echo(
                    f"There are problems in the individual repositories when validating them for entity {entity} that need to be solved"
                )
        for entity, errors in validation_results.get("comparisons", {}).items():
            if errors:
                click.echo(
                    f"There are problems in the individual repositories when comparing them with respect to bam-masterdata for entity {entity} that need to be solved"
                )


@cli.command(
    name="checker",
    help="Checks the files specified in the tag `--file-path` with respect to the ones specified in `--datamodel-path`.",
)
@click.option(
    "--file-path",
    "file_path",  # alias
    type=click.Path(exists=True),
    required=True,
    help="""The path to the file or directory containing Python modules or the Excel file to be checked.""",
)
@click.option(
    "--mode",
    "mode",  # alias
    type=click.Choice(
        ["self", "incoming", "validate", "compare", "all", "individual"],
        case_sensitive=False,
    ),
    default="all",
    help="""Specify the mode for the checker. Options are:
    "self" -> Validate only the current data model.
    "incoming" -> Validate only the new entity structure.
    "validate" -> Validate both the current model and new entities.
    "compare" -> Compare new entities against the current model.
    "all" -> Run all validations and comparison. (Default).
    "individual" -> Run individual repositories validations.""",
)
@click.option(
    "--datamodel-path",
    "datamodel_path",  # alias
    type=click.Path(exists=True, dir_okay=True),
    default=DATAMODEL_DIR,
    help="""Path to the directory containing the Python modules defining the datamodel (defaults to './bam_masterdata/datamodel/').""",
)
def checker(file_path, mode, datamodel_path):
    run_checker(file_path=file_path, mode=mode, datamodel_path=datamodel_path)


@cli.command(
    name="push_to_openbis",
    help="Uploads to openBIS the entities contained in the file specified in the tag `--file-path` after passing correctly all the checks from the `checker`.",
)
@click.option(
    "--file-path",
    "file_path",  # alias
    type=click.Path(exists=True),
    required=True,
    help="""The path to the file or directory containing Python modules or the Excel file to be checked.""",
)
@click.option(
    "--datamodel-path",
    "datamodel_path",  # alias
    type=click.Path(exists=True, dir_okay=True),
    default=DATAMODEL_DIR,
    help="""Path to the directory containing the Python modules defining the datamodel (defaults to './bam_masterdata/datamodel/').""",
)
def push_to_openbis(file_path, datamodel_path):
    # Check if the path is a single .py file OR a directory containing .py files
    if file_path.endswith(".py") or (
        os.path.isdir(file_path) and any(glob.glob(os.path.join(file_path, "*.py")))
    ):
        source_type = "python"
    elif file_path.endswith(".xlsx"):
        source_type = "excel"
    else:
        source_type = None
        logger.warning(f"Unsupported source type for path: {file_path}")

    # Handle source_type
    if source_type == "python":
        # Copy all .py files to the tmp directory
        if os.path.isdir(file_path):
            tmp_dir = file_path
        else:
            tmp_dir = os.path.dirname(file_path)
        logger.info(f"Copied Python files to {tmp_dir}")

    elif source_type == "excel":
        tmp_dir = "./bam_masterdata/tmp"
        os.makedirs(tmp_dir, exist_ok=True)

        generator = MasterdataCodeGenerator(path=file_path, row_cell_info=True)

        for module_name in ["collection", "dataset", "object", "vocabulary"]:
            output_file = Path(os.path.join(tmp_dir, f"{module_name}_types.py"))

            # Get the method from `MasterdataCodeGenerator`
            code = getattr(generator, f"generate_{module_name}_types")().rstrip()

            if code != "":
                output_file.write_text(code + "\n", encoding="utf-8")
                click.echo(f"Generated {module_name} types in {output_file}\n")
            else:
                click.echo(f"Skipping {module_name}_types.py (empty entity data)")
        logger.info(f"Processed Excel file and exported to {tmp_dir}")

    # Instantiate the checker class and run validation
    checker = MasterdataChecker()

    # Load current model from datamodel path
    checker.load_current_model(datamodel_dir=datamodel_path)

    # Load new entities from the specified file path (could be a Python file, directory, or Excel)
    checker.load_new_entities(source=file_path)

    # Run the checker in the specified mode
    validation_results = checker.check(mode="individual")

    if not validation_results.get("incoming_model"):
        logger.info("No problems found in the new entities definition.")

    # If there are no problems, push to openBIS
    if all(
        isinstance(value, dict) and all(not sub_value for sub_value in value.values())
        for value in validation_results.values()
    ):
        click.echo("No problems found in the datamodel and incoming model.")
        # Push to openBIS

        url = environ("OPENBIS_URL")
        openbis = ologin(url=url)
        click.echo(f"Using the openBIS instance: {url}\n")

        # Push each entity type
        for module_path in listdir_py_modules(tmp_dir):
            module = import_module(module_path=module_path)
            for _, obj in inspect.getmembers(module, inspect.isclass):
                if hasattr(obj, "defs") and callable(getattr(obj, "to_openbis")):
                    obj_instance = obj()
                    obj_instance.to_openbis(openbis=openbis, logger=logger)

    else:
        logger.error(
            f"The checking of the new entities definition located in {file_path} did not pass. Please, check your entity definitions."
        )
        click.echo(
            f"There are problems in the incoming model located in {file_path} that need to be solved"
        )
        return

    if source_type == "excel":
        # Clean up the tmp directory
        shutil.rmtree(tmp_dir)
        click.echo(f"Temporary files in {tmp_dir} have been deleted.")

    logger.info(
        f"Push to openBIS of the new entities located in {file_path} completed."
    )


if __name__ == "__main__":
    cli()
