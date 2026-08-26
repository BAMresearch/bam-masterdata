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

We recommend using `uv` to manage your virtual environment and the dependencies, as well as using
Python 3.14:

```sh
uv venv --python 3.14
```

Activate the environment:

- *Linux/MacOS*

  ```sh
  source .venv/bin/activate
  ```

- *Windows*

  ```sh
  .venv\Scripts\activate
  ```

With the virtual environment activated, make sure to install the optional dependencies:

```sh
uv sync --all-extras
```

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

### Pre-commit hooks (recommended)

We use `pre-commit` to run fast checks automatically on every commit (formatting, linting, secrets scanning, and a repository-specific policy check).

Install once:

```sh
pip install pre-commit
pre-commit install
```

(Optional) Run on the whole repo:

```sh
pre-commit run --all-files
```

**Secrets baseline:** the repository uses `.secrets.baseline`. If you add new secrets intentionally (rare), update the baseline:

```sh
detect-secrets scan > .secrets.baseline
```

### Documentation on Github pages

To view the documentation locally, make sure to have installed the extra packages with the setup commands explained above (especifically, `uv sync --all-extras`). This command installs the `zensical` dependency.

The first time, build the server:

```sh
zensical build
```

Run the documentation server:

```sh
zensical serve
```

The output looks like:

```sh
Serving .../site on http://localhost:8000
Build started
No issues found
```

Simply click on `http://localhost:8000`. The changes in the `md` files of the documentation are immediately reflected when the files are saved (the local web will automatically refresh).
