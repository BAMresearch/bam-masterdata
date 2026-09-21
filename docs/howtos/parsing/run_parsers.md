# Run a parser locally with a Jupyter notebook

This how-to explains how to create a local `run.ipynb` notebook for a parser
created according to [Create New Parsers](create_new_parsers.md). The notebook
lets you select input files, connect to an openBIS instance, and start the
parser interactively without having to write a separate command-line script.

The notebook is a runner only: the parser implementation remains in the
parser repository under `src/`, and the parser's tests remain under `tests/`.
This separation makes it possible to test the parser logic locally before
uploading data to openBIS.

## Prerequisites

Before creating the notebook, make sure that:

- the parser repository has the structure described in
  [Create New Parsers](create_new_parsers.md);
- the parser's virtual environment is active;
- the parser package and its dependencies are installed in editable mode:

    ```sh
    pip install -e .
    ```

- the notebook support is installed:

    ```sh
    pip install jupyter ipykernel
    ```

If the parser uses additional libraries, add them to `pyproject.toml` and
install the project again. Do not install them only in the notebook
environment, otherwise another user will not be able to reproduce the run.

## Create the notebook

Create a file named `run.ipynb` in the root of the parser repository. You can
also copy the reference notebook
[`tools/scripts/run.ipynb`](../../../tools/scripts/run.ipynb) from
`bam-masterdata` and replace its example-specific values.

Start Jupyter from the parser repository so that the local `src/` package is
available to the notebook:

```sh
jupyter notebook
```

Select the kernel belonging to the parser's `.venv`. If it is not listed,
register it once:

```sh
python -m ipykernel install --user --name my-parser --display-name "Python (my-parser)"
```

Replace `my-parser` with a meaningful name for the parser.

## Add the notebook cells

The following cells are the minimum required for an openBIS run. Execute them
from top to bottom.

### 1. Import the runner and create a logger

Import the parser class from the package created in `src/`. The import path
must match the package name chosen in `pyproject.toml` and
`src/<package_name>/__init__.py`.

```python
from getpass import getpass

from pybis import Openbis

from bam_masterdata.cli.run_parser import RunParsers
from bam_masterdata.logger import logger
from src.<parser> import <ParserClass>

parser = <ParserClass>()
```

For example, a parser package named `supercode_x` with a class named
`SupercodeXParser` is imported as follows:

```python
from src.supercode_x import SupercodeXParser

parser = SupercodeXParser()
```

If the parser package exports the class from `__init__.py`, importing from the
package itself is also possible:

```python
from supercode_x import SupercodeXParser
```

### 2. Select the files to parse

Use paths relative to the notebook (normally the repository root), or use
absolute paths. Keep test input files in a dedicated directory such as
`tests/data/`, as described in [Create New Parsers](create_new_parsers.md).

```python
FILE_1 = "tests/data/super.json"
# FILE_2 = "tests/data/another-file.json"

files = [FILE_1]
# files = [FILE_1, FILE_2]  # use this for multiple files
```

The parser receives the complete list in `files`. Every file must be supported
by the parser and must exist before starting the run.

### 3. Connect to openBIS

Set the URL of the target openBIS instance and enter the credentials when
prompted. `getpass()` prevents the password from being displayed or stored in
the notebook.

```python
OPENBIS_URL = "https://your-openbis-instance.example"

print(f"Connecting to openBIS instance at {OPENBIS_URL}...")
openbis = Openbis(OPENBIS_URL)

username = input("Username: ")
password = getpass("Password: ")
openbis.login(username, password, save_token=True)
```

Only use `save_token=True` on a trusted local machine. Never write a password
or an access token into a notebook or commit it to the parser repository.

### 4. Define the openBIS destination

Set the names of the space and project. A collection is optional. When
`COLLECTION` is an empty string, the parser stores objects directly under the
project according to the `RunParsers` behavior.

```python
SPACE = "MY_SPACE"
PROJECT = "MY_PROJECT"
COLLECTION = "MY_COLLECTION"  # optional; use "" for no collection
```

The space, project, and collection must be available to the logged-in user.
`RunParsers` resolves them and creates missing destinations where the
configured openBIS permissions allow it.

### 5. Configure and create the parser run

`files_parser` is a dictionary whose keys are parser instances and whose values
are lists of input-file paths. This also allows several parsers to be run in a
single notebook by adding more entries.

```python
files_parser = {
    parser: files,
}

parsing = RunParsers(
    openbis=openbis,
    space_name=SPACE,
    project_name=PROJECT,
    collection_name=COLLECTION,
    files_parser=files_parser,
    logger=logger,
)
```

For multiple parsers, create one instance per parser:

```python
files_parser = {
    SupercodeXParser(): ["tests/data/super.json"],
    # OtherParser(): ["tests/data/other.csv"],
}
```

### 6. Start the run

Run the final cell only after checking the input files and destination
settings. The parser first builds the `bam-masterdata` collection and then
`RunParsers` creates or updates the corresponding openBIS objects, uploads the
input files, and creates relationships.

```python
print("Starting parsing...")
parsing.run()
print("Done")
```

Review the notebook output and the parser log messages for warnings or errors.
For an initial test, use a small number of files and a test project or
collection.

## Test parser logic without openBIS

To verify only the parser logic, do not create an `Openbis` connection and do
not call `RunParsers`. Use a `CollectionType` directly:

```python
from bam_masterdata.logger import logger
from bam_masterdata.metadata.entities import CollectionType

test_collection = CollectionType()
parser.parse(files, test_collection, logger)

print(f"Objects added: {len(test_collection.attached_objects)}")
for object_id, obj in test_collection.attached_objects.items():
    print(f"{object_id}: {obj}")
```

This check is useful for debugging file handling, object creation, and
relationships. It does not authenticate with openBIS, create destinations, or
upload datasets. Keep the automated tests in `tests/` as the authoritative
regression check and run them with:

```sh
pytest tests
```

## Troubleshooting

- **`ModuleNotFoundError` for the parser package:** start Jupyter from the
  parser repository root and select the parser's virtual-environment kernel.
  Confirm that `pip install -e .` was run in that same environment.
- **`FileNotFoundError`:** check the notebook's current working directory and
  use paths relative to it, or provide absolute paths.
- **Authentication or permission errors:** verify `OPENBIS_URL`, the supplied
  credentials, and access to `SPACE`, `PROJECT`, and `COLLECTION`.
- **Unexpected objects or values:** run the parser with `CollectionType` first,
  inspect the resulting objects, and then repeat the openBIS run with a test
  destination.

## Recommended repository layout

Keep the notebook next to the parser project files so that its imports and
relative input paths remain reproducible:

```text
your-parser/
├── pyproject.toml
├── run.ipynb
├── src/
│   └── your_parser/
│       ├── __init__.py
│       └── parser.py
└── tests/
    ├── test_parser.py
    └── data/
        └── input-file.json
```

Do not commit credentials, access tokens, or production-only file paths to
`run.ipynb`. If the notebook contains instance-specific settings, keep a
sanitized template in version control and configure the actual values locally.