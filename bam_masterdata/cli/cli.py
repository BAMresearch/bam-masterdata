import json
import os
import subprocess
import time
from pathlib import Path

import click
from decouple import config as environ
from openpyxl import Workbook
from rdflib import Graph

from bam_masterdata.cli.entities_dict import EntitiesDict
from bam_masterdata.cli.entities_to_excel import entities_to_excel
from bam_masterdata.cli.entities_to_rdf import entities_to_rdf
from bam_masterdata.cli.fill_masterdata import MasterdataCodeGenerator
from bam_masterdata.logger import logger
from bam_masterdata.utils import (
    delete_and_create_dir,
    duplicated_property_types,
    import_module,
    listdir_py_modules,
)


def find_datamodel_dir():
    """Search for 'datamodel/' in possible locations and return its absolute path."""
    possible_locations = [
        # Case: Running from a project with `datamodel/`
        Path.cwd() / "datamodel",
        # Case: Running inside bam-masterdata
        Path.cwd() / "bam_masterdata" / "datamodel",
        # Case: Running inside installed package
        Path(__file__).parent / "datamodel",
    ]

    for path in possible_locations:
        if path.exists():
            return str(path.resolve())

    raise FileNotFoundError("Could not find a valid 'datamodel/' directory.")


DATAMODEL_DIR = find_datamodel_dir()


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
    for module_name in ["property", "collection", "dataset", "object", "vocabulary"]:
        module_start_time = time.perf_counter()  # more precise time measurement
        output_file = Path(os.path.join(output_directory, f"{module_name}_types.py"))

        # Get the method from `MasterdataCodeGenerator`
        code = getattr(generator, f"generate_{module_name}_types")()
        code = code.rstrip("\n") + "\n"
        output_file.write_text(code, encoding="utf-8")
        module_elapsed_time = time.perf_counter() - module_start_time
        click.echo(
            f"Generated {module_name} types in {module_elapsed_time:.2f} seconds in {output_file}\n"
        )

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
        if module_path.endswith("property_types.py"):
            if duplicated_property_types(module_path=module_path, logger=logger):
                click.echo(
                    "Please fix the duplicated property types before exporting to RDF/XML."
                )
                return
        entities_to_rdf(graph=graph, module_path=module_path, logger=logger)

    # Saving RDF/XML to file
    rdf_output = graph.serialize(format="pretty-xml")
    masterdata_file = os.path.join(export_dir, "masterdata.owl")
    with open(masterdata_file, "w", encoding="utf-8") as f:
        f.write(rdf_output)

    click.echo(
        f"All masterdata has been generated in RDF/XML format and saved to {masterdata_file}"
    )


@cli.command(
    name="checker",
    help="Checks the files specified in the tag `--from` with respect to the ones specified in `--to`.",
)
@click.option(
    "--from",
    "from_path",  # alias
    type=click.Path(exists=True, dir_okay=True),
    default="./artifacts/masterdata.xlsx",
    help="""
    The path to the directory containing the Python modules or the individual masterdata Excel file to be checked.
    """,
)
@click.option(
    "--to",
    "to_path",  # alias
    type=click.Path(exists=True, dir_okay=True),
    default=DATAMODEL_DIR,
    help="""
    The path to the directory containing the Python modules the the path defined in `from` will be checked with respect to.
    """,
)
def checker(from_path, to_path):
    print(f"From: {from_path}, To: {to_path}")


if __name__ == "__main__":
    cli()
