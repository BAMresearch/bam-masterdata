# How-to: Create new parsers

This guide explains how to create a custom parser that reads raw files (CSV, Excel, JSON, XML, etc) and transforms them into the `bam-masterdata` format. By following these steps, your parser can be integrated into the Data Store workflow and used in the [Parser app](parser_app.md).
This allows you to bring custom or third-party data sources into the existing masterdata workflows without manual conversion.

!!! note "Prerequisites"
    - **Python ≥ 3.10** installed
    - Knowledge of the **bam-masterdata** schema definitions in [`bam_masterdata/datamodel/`](https://github.com/BAMresearch/bam-masterdata/tree/main/bam_masterdata/datamodel). Learn more in [Work with Object Types](use_object_types.md).

---


## Use the GitHub parser example
1. Go to [masterdata-parser-example](https://github.com/BAMresearch/masterdata-parser-example).
2. Either **fork** it (keep your own version) or **use it as a template** to start a new repository.
3. Clone your fork/template locally:
    ```sh
    git clone [your repository link]
    ```
4. Verify the folder structure includes `src/`, `tests/`, `pyproject.toml`, and `README.md`:
    ```sh
    [your repo name]
    ├── LICENSE
    ├── pyproject.toml
    ├── README.md
    ├── src
    │   └── masterdata_parser_example
    │       ├── __init__.py
    │       ├── parser.py
    │       └── _version.py
    └── tests
        ├── __init__.py
        ├── conftest.py
        └── test_parser.py
    ```

    * `src/` → contains the parser package code
    * `tests/` → contains test files to check your parser works correctly
    * `pyproject.toml` → defines dependencies and project configuration
    * `README.md` → instructions and documentation


??? tip "Forking or using the template"
    You can read more details in the GitHub docs on [forking a repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) and on [creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).

    Either way, you should end up with your own repository in which you can work on the definition and logic behind the parser.

## Set up a Virtual Environment

It is recommended to create a virtual environment named `.venv` (already included in `.gitignore`) to manage dependencies. In the terminal, do:
```sh
cd [your repo name]
```

You have two options to create a virtual environment:

1. Using venv
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # on Linux/macOS
    .\.venv\Scripts\activate  # on Windows
    ```
2. Using conda
    ```sh
    conda create --prefix .venv python=3.10
    conda activate .venv
    ```

Verify that everything is set up correctly by running inside the repo:

```sh
pip install --upgrade pip
pip install -e .
pytest tests
```

You should see all tests passing before you start customizing.

??? tip "Faster pip installation"
    We recommend installing `uv` before installing the package by doing:
    ```sh
    pip install --upgrade pip
    pip install uv
    uv pip install -e .
    ```


## Modify the project structure and files

Since everything in the template project is named `masterdata_parser_example` and derivates, you will need to replace that with your own parser name.
This ensures that your parser has a unique and consistent package name.

For the purpose of this guide, we will rename everything using a ficticious code name _SupercodeX_.

??? tip "Python naming conventions"
    - **Packages / modules:** lowercase, underscores allowed (e.g., `my_parser`)
    - **Classes:** CapWords / PascalCase (e.g., `MyParser`)
    - **Variables / functions:** lowercase with underscores (e.g., `file_name`, `parse_file`)

    See the official Python style guide: [PEP 8 – Naming Conventions](https://peps.python.org/pep-0008/#naming-conventions)

### Rename project folder and parser class

1. Modify the `src` package name from `masterdata_parser_example` to your package name (e.g., `supercode_x`). This will affect on how your users install the package later on by doing `pip install` (e.g., `pip install supercode_x`).
2. Update in the `pyproject.toml` all occurrences of `masterdata_parser_example` to the new package name (e.g., `supercode_x`).
3. Update the `[project]` section in `pyproject.toml` with your specific information.
4. Go to `src/supercode_x/parser.py` and change the class name from `MasterdataParserExample` to your case (`SupercodeXParser`).
5. Update importing this class in `src/supercode_x/__init__.py` and `tests/conftest.py`.
6. Update the entry point dictionary in `src/supercode_x/__init__.py`.
7. Verify that the project is still working by running `pytest tests`. If everything is good, the testing should pass.

### Rename entry point

1. Go to `src/supercode_x/__init__.py`.
2. Modify `masterdata_parser_example_entry_point` for your new entry point variable name (e.g., `supercode_x_entry_point`).
3. Update in the `pyproject.toml` all occurrences of `masterdata_parser_example_entry_point` to the new entry point name  (e.g., `supercode_x_entry_point`).


## Add parser logic

Open the `src/.../parser.py` file. After renaming your parser class to `SupercodeXParser`, you should have:
```python
from bam_masterdata.datamodel.object_types import ExperimentalStep
from bam_masterdata.parsing import AbstractParser


class SupercodeXParser(AbstractParser):
    def parse(self, files, collection, logger):
        synthesis = ExperimentalStep(name="Synthesis")
        synthesis_id = collection.add(synthesis)
        measurement = ExperimentalStep(name="Measurement")
        measurement_id = collection.add(measurement)
        _ = collection.add_relationship(synthesis_id, measurement_id)
        logger.info(
            "Parsing finished: Added examples synthesis and measurement experimental steps."
        )
```

Writing a parser logic is composed of a series of steps:
1. The object type classes imported from `bam_masterdata` (in the example above, `ExperimentalStep`).
2. Open the `files` with Python and read metainformation from them.
3. Instantiate object types and add the metainformation to the corresponding fields.
4. Add those object types and their relationships to `collection`.

Optionally, you can add log messages (`info`, `warning`, `error`, or `critical`) to debug the logic of your parser.


### Example

As an example, imagine we are expecting to pass a `super.json` file to our `SupercodeXParser` to read certain metadata. The file contents are:
```json
{
    "program_name": "SupercodeX",
    "program_version": "1.1.0",
}
```

We recommend moving files in which you are testing the parser to a `tests/data/` folder.


#### Step 1: Import necessary classes

At the top of `parser.py`, ensure you import:
```python
# Step 1: import necessary classes
import json
from bam_masterdata.datamodel.object_types import SoftwareCode
from bam_masterdata.parsing import AbstractParser
```

#### Step 2: Modify the parse() method

1. Iterate over the `files` argument.
2. Open each file and read the JSON content.
3. Optionally, log progress using `logger.info()`.

```python
# Step 1: import necessary classes
import json
from bam_masterdata.datamodel.object_types import SoftwareCode
from bam_masterdata.parsing import AbstractParser


class SupercodeXParser(AbstractParser):
    def parse(self, files, collection, logger):
        for file_path in files:
            # Step 2: read files metainformation
            logger.info(f"Parsing file: {file_path}")
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
```


#### Step 3: Instantiate objects and add metadata

1. Instantiate `SoftwareCode` objects and fill in the fields with the JSON data.
2. Optionally, log progress using `logger.info()`.

```python
# Step 1: import necessary classes
import json
from bam_masterdata.datamodel.object_types import SoftwareCode
from bam_masterdata.parsing import AbstractParser


class SupercodeXParser(AbstractParser):
    def parse(self, files, collection, logger):
        for file_path in files:
            # Step 2: read files metainformation
            logger.info(f"Parsing file: {file_path}")
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Step 3: Instantiate and populate classes metadata
            software = SoftwareCode(
                name=data.get("program_name"),
                version=data.get("program_version")
            )
```

#### Step 4: Add objects and relationships to the collection

1. Add the object to the collection using `collection.add(object)`.
2. You can also add relationships between objects using `collection.relationships(parent_id, child_id)`.

```python
# Step 1: import necessary classes
import json
from bam_masterdata.datamodel.object_types import SoftwareCode
from bam_masterdata.parsing import AbstractParser


class SupercodeXParser(AbstractParser):
    def parse(self, files, collection, logger):
        for file_path in files:
            # Step 2: read files metainformation
            logger.info(f"Parsing file: {file_path}")
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Step 3: Instantiate and populate classes metadata
            software = SoftwareCode(
                name=data.get("program_name"),
                version=data.get("program_version")
            )

            # Step 4: Add to collection
            software_id = collection.add(software)
            logger.info(f"Added SoftwareCode with ID {software_id}")
```


### Tips

* Use the logger to provide useful messages during parsing, but bear in mind this can clutter the app if you plan to parse hundreds or more files.
  ```python
  logger.info("Parsing file XYZ")
  ```
* Test your parser incrementally by adding one object at a time to the collection and verifying results. You can test this by modifying the `tests/test_parser.py` testing file.


## Final steps

You now have all the core components of your custom parser in place:

- Project structure set up.
- Package renamed to your parser name.
- Parser class created and logic accepting the metainformation of the specific files.
- Entry points updated.

### What’s left?

1. **Update `pyproject.toml`**
    - Make sure the package name, version, and entry points match your parser.
    - Adjust dependencies if your parser requires additional libraries (e.g., `pandas`).
2. **Update the `README.md`**
    - Replace the `README.md` content with a description of your parser.
    - Document how to install it and how to run it.
3. **Create a new release in GitHub**
    - Go to your repository on GitHub.
    - Click on the **Releases** tab (or navigate to `https://github.com/[your-username]/[your-repo]/releases`).
    - Click **Create a new release**.
    - Choose a tag version (e.g., `v1.0.0`) and add a release title.
    - Optionally, add release notes describing changes or new features.
    - Click **Publish release** to make it available.


## Updating the Parser

Once your parser is implemented and tested, future updates are usually minimal and follow a clear process.

1. **Modify only `parser.py`**
    - All changes should be contained within your parser class and helper functions.
    - Avoid renaming packages or changing the project structure unless absolutely necessary.

2. **Notify the Admin for a new release**
    - After updates, inform the administrator or the person responsible for releases.
    - Provide details of the changes and any new dependencies.
