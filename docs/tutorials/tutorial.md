## Installation setup

You can install the package in two methods:

- using `pip` as an additional package to your project,
- as a developer, cloning and installing the repository locally

### Installing with `pip`

We recommend you to create first a virtual environment, either with [`conda`](https://anaconda.org/anaconda/conda) or with [`venv`](https://docs.python.org/3/library/venv.html). Note that `bam-masterdata` can be installed with any Python version between 3.9 and 3.12.

**Conda**

Run:
```bash
conda create --name .venv pip python=3.12
conda activate .venv
```

**Venv**

Run:
```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

After creating and activating your environment, make sure you have `pip` upgraded, and install the package:
```bash
pip install --upgrade pip
pip install bam-masterdata
```

!!! hint Faster installation
    In order to install faster the package, you can use [`uv`](https://docs.astral.sh/uv/) for pip installing Python packages:
    ```bash
    pip install uv
    uv pip install bam-masterdata
    ```

### Development

In order to develop the package, first you have to clone the repository:
```bash
git clone https://git.bam.de/bam-data-store/bam-masterdata.git
cd bam-masterdata
```

Same as before, create a virtual environment (in this example, we use `venv`) and activate it:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Run the following script:

```bash
./scripts/install_python_dependencies.sh
```

??? info "Installation script"
    The script contains a set of steps which ensure to install the package with all optional dependencies. If you prefer to install manually, we recommend you to take a look into the script and install only the desired dependencies.

    Its content is:
    ```sh
    #!/bin/bash

    # Fail immediately if any command exits with a non-zero status
    set -e

    echo "Making sure pip is up to date..."
    pip install --upgrade pip

    echo "Installing uv..."
    pip install uv

    echo "Installing main project dependencies..."
    uv pip install -e '.[dev,docu]'

    echo "All dependencies installed successfully."
    ```
