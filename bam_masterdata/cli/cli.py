import os
import subprocess
import time
from pathlib import Path

import click
from decouple import config as environ
from openpyxl import Workbook

from bam_masterdata.cli.entities_to_excel import entities_to_excel
from bam_masterdata.cli.entities_to_json import entities_to_json
from bam_masterdata.cli.fill_masterdata import MasterdataCodeGenerator
from bam_masterdata.logger import logger
from bam_masterdata.utils import (
    delete_and_create_dir,
    import_module,
    listdir_py_modules,
)

DATAMODEL_DIR = os.path.join(".", "bam_masterdata", "datamodel")


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
def fill_masterdata(url, excel_file):
    start_time = time.time()

    # Define output directory
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
        generator = MasterdataCodeGenerator(path=excel_file)
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
    Default is `./bam_masterdata/datamodel/`.
    """,
)
def export_to_json(force_delete, python_path):
    # Get the directories from the Python modules and the export directory for the static artifacts
    export_dir = os.path.join(".", "artifacts")

    # Delete and create the export directory
    delete_and_create_dir(
        directory_path=export_dir,
        logger=logger,
        force_delete=force_delete,
    )

    # Get the Python modules to process the datamodel
    py_modules = listdir_py_modules(directory_path=python_path, logger=logger)

    # Process each module using the `model_to_json` method of each entity
    for module_path in py_modules:
        entities_to_json(module_path=module_path, export_dir=export_dir, logger=logger)

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
    Default is `./bam_masterdata/datamodel/`.
    """,
)
def export_to_excel(force_delete, python_path):
    # Get the directories from the Python modules and the export directory for the static artifacts
    export_dir = os.path.join(".", "artifacts")

    # Delete and create the export directory
    delete_and_create_dir(
        directory_path=export_dir,
        logger=logger,
        force_delete=force_delete,
    )

    # Get the Python modules to process the datamodel
    py_modules = listdir_py_modules(directory_path=python_path, logger=logger)

    # Load the definitions module classes
    definitions_module = import_module(
        module_path="./bam_masterdata/metadata/definitions.py"
    )

    # Process the modules and save the entities to the openBIS masterdata Excel file
    masterdata_file = os.path.join(".", "artifacts", "masterdata.xlsx")
    wb = Workbook()
    for i, module_path in enumerate(py_modules):
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


if __name__ == "__main__":
    cli()
