import os
import time
from pathlib import Path

import click

from bam_masterdata.cli.fill_masterdata import MasterdataCodeGenerator


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


if __name__ == "__main__":
    cli()
