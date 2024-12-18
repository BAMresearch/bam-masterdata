import os
import time
from pathlib import Path

import click
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


@click.group(help="Entry point to run `bam_masterdata` CLI commands.")
def cli():
    pass


@cli.command(
    name="fill_masterdata",
    help="Fill the masterdata from the openBIS instance specified in the `.env` in the bam_masterdata/datamodel/ subfolder.",
)
def fill_masterdata():
    start_time = time.time()

    # ! this takes a lot of time loading all the entities in Openbis
    generator = MasterdataCodeGenerator()

    # Add each module to the `bam_masterdata/datamodel` directory
    output_dir = os.path.join(".", "bam_masterdata", "datamodel")
    for module_name in ["property", "collection", "dataset", "object", "vocabulary"]:
        module_start_time = time.perf_counter()  # more precise time measurement
        output_file = Path(os.path.join(output_dir, f"{module_name}_types.py"))

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

    # ! this could be automated in the CLI
    click.echo(
        "Don't forget to apply ruff at the end after generating the files by doing:\n"
    )
    click.echo("    ruff check .\n")
    click.echo("    ruff format .\n")


@cli.command(
    name="export_to_json",
    help="Export entities to JSON files to the `./artifacts/` folder.",
)
def export_to_json():
    # Get the directories from the Python modules and the export directory for the static artifacts
    datamodel_dir = os.path.join(".", "bam_masterdata", "datamodel")
    export_dir = os.path.join(".", "artifacts")

    # Delete and create the export directory
    delete_and_create_dir(directory_path=export_dir, logger=logger)

    # Get the Python modules to process the datamodel
    py_modules = listdir_py_modules(directory_path=datamodel_dir, logger=logger)

    # Process each module using the `to_json` method of each entity
    for module_path in py_modules:
        entities_to_json(module_path=module_path, export_dir=export_dir, logger=logger)

    click.echo(f"All entity artifacts have been generated and saved to {export_dir}")


@cli.command(
    name="export_to_excel",
    help="Export entities to an Excel file in the path `./artifacts/masterdata.xlsx`.",
)
def export_to_excel():
    # Get the Python modules to process the datamodel
    datamodel_dir = os.path.join(".", "bam_masterdata", "datamodel")
    py_modules = listdir_py_modules(directory_path=datamodel_dir, logger=logger)

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
