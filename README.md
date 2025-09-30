<h1 align="center">
  <picture>
    <source srcset="https://github.com/BAMresearch/bam-masterdata/raw/main/docs/assets/bammasterdata_blue_transparent_text.png">
    <img src="https://github.com/BAMresearch/bam-masterdata/raw/main/docs/assets/bammasterdata_blue_transparent_text.png"
         alt="BAM Masterdata"
         style="width: 25rem">
  </picture>
</h1>


<h4 align="center">

[![CI Status](https://github.com/BAMresearch/bam-masterdata/actions/workflows/actions.yml/badge.svg)](https://github.com/BAMresearch/bam-masterdata/actions/workflows/actions.yml/badge.svg)
[![Coverage](https://coveralls.io/repos/github/BAMresearch/bam-masterdata/badge.svg?branch=main)](https://coveralls.io/repos/github/BAMresearch/bam-masterdata/badge.svg?branch=main)
[![PyPI versions](https://img.shields.io/pypi/v/bam-masterdata)](https://img.shields.io/pypi/v/bam-masterdata)
[![Python supported versions](https://img.shields.io/pypi/pyversions/bam-masterdata)](https://img.shields.io/pypi/pyversions/bam-masterdata)

</h4>

The BAM Masterdata repository contains the masterdata schemas defined at BAM and provides utility functions for working with them.

If you want to install it, do:
```sh
pip install bam-masterdata
```

## Development

If you want to develop locally this package, clone the project and enter in the workspace folder:

```sh
git clone https://github.com/BAMresearch/bam-masterdata.git
cd bam-masterdata
```

Create a virtual environment (you can use Python>3.9) in your workspace:

```sh
python3 -m venv .venv
source .venv/bin/activate
```

Run the following script depending on your OS:
- *Linux/MacOS*:
  ```sh
  ./scripts/install_python_dependencies.sh
  ```
- *Windows*:
  ```sh
  scripts/install_python_dependencies.bat
  ```

**Note**: This script installs the required dependencies for development, testing, and documentation, using `uv` and `pip`.

### Run the tests

You can locally run the tests by doing:

```sh
python -m pytest -sv tests
```

where the `-s` and `-v` options toggle the output verbosity.

You can also generate a local coverage report:

```sh
python -m pytest --cov=src tests
```

### Run auto-formatting and linting

We use [Ruff](https://docs.astral.sh/ruff/) for formatting and linting the code following the rules specified in the `pyproject.toml`. You can run locally:

```sh
ruff check .
```

This will produce an output with the specific issues found. In order to auto-fix them, run:

```sh
ruff format .
```

If some issues are not possible to fix automatically, you will need to visit the file and fix them by hand.


### Documentation on Github pages

To view the documentation locally, make sure to have installed the extra packages (this is part of the `scripts/install_python_dependencies.*`, so if you ran this script before, you don't need to do it again now):

```sh
uv pip install -e '[docu]'
```

**Note**: This command installs `mkdocs`, `mkdocs-material`, and other documentation-related dependencies.

The first time, build the server:

```sh
mkdocs build
```

Run the documentation server:

```sh
mkdocs serve
```

The output looks like:

```sh
INFO    -  Building documentation...
INFO    -  Cleaning site directory
INFO    -  [14:07:47] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO    -  [14:07:47] Serving on http://127.0.0.1:8000/
```

Simply click on `http://127.0.0.1:8000/`. The changes in the `md` files of the documentation are immediately reflected when the files are saved (the local web will automatically refresh).

## Main contributors

The main code developers are:

| Name                | E-mail                                                       |
| ------------------- | ------------------------------------------------------------ |
| Carlos Madariaga    | [carlos.madariaga@bam.de](mailto:carlos.madariaga@bam.de)       |
| Lucas Zimmermann    | [lucas.zimmermann@bam.de](mailto:lucas.zimmermann@bam.de)       |
| Dr. Jose M. Pizarro | [jose.pizarro-blanco@bam.de](mailto:jose.pizarro-blanco@bam.de) |
