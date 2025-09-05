# How-To: Creating a new Parser for bam-masterdata

### Goal:

By the end of this guide, you will be able to implement your own parser that integrates seamlessly with **bam-masterdata**.
A parser is responsible for reading raw files (e.g., CSV, Excel, JSON, XML) and transforming them into the masterdata format defined in **bam-masterdata**.
This allows you to bring custom or third-party data sources into the existing masterdata workflows without manual conversion.

### Requirements

To follow this guide, you will need:

- **Python ≥ 3.10** installed
- Access to the **bam-masterdata** repository or package
- Basic Python knowledge (functions, classes, error handling)
- A working development environment (e.g., VS Code, PyCharm, or terminal + editor)
- Installed dependencies via:
```bash
  pip install .
```
- (Optional) knowledge using `pytest` to validate your parser implementation


## 1. Getting the Structure

1. Go to [masterdata-parser-example](https://github.com/BAMresearch/masterdata-parser-example) and either **fork** (if you want to keep your own version on GitHub) or simply **clone** the repository to your local machine.
   *(Tip: Use the README of that repo, Step 1, as a guide if you’re unsure.)*

2. Create a new folder where you want your parser project to live.
   *(Example: `mkdir ~/projects/my-parser`)*

3. Inside that folder, clone your forked or the original repository:
```sh
   git clone [your repository link]
```

4. After cloning, you should see a folder structure like this:

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

---

### Setting up a Virtual Environment

It is recommended to create a virtual environment named `.venv` (already included in `.gitignore`) to manage dependencies.

`cd [your repo name]`

* **Using venv:**

```sh
python -m venv .venv
source .venv/bin/activate  # on Linux/macOS
.\.venv\Scripts\activate  # on Windows
```

* **Using conda:**

```sh
conda create --prefix .venv python=3.10
conda activate .venv
```

5. Verify that everything is set up correctly by running inside the repo:

```sh
pip install -e .
pytest
```

You should see all tests passing before you start customizing.

## 2. Choosing a Name

Since everything in the template project is named `masterdata_parser_example`, you will need to replace that with your own parser name.
This ensures that your parser has a unique and consistent package name.

---

### Steps

1. **In the cloned project folder**

   Locate and open the pyproject.toml

2. **Update the `pyproject.toml`**

   * Search for all occurrences of `masterdata_parser_example`.
   * Replace them with your chosen name, preferably in the format:

     ```
     [yourparsername_parser]
     ```
   * As of *05.09*, there are **5 occurrences** in total.
   * ⚠️ **Important**: 2 of them are concatenated with `_entry_point`.
     Keep the `_entry_point` part, e.g.:

     ```
     [yourparsername_parser]_entry_point
     ```

3. **Rename the source folder**
   In the structure below:

   ```sh
   [your repo name]
   ├── src
   │   └── masterdata_parser_example
   ```

   Rename `masterdata_parser_example` to [yourparsername_parser], for example:

   ```sh
   [your repo name]
   ├── src
   │   └── yourparsername_parser
   ```

   ✅ Use **lowercase** names with underscores if needed (e.g., `csv_parser`, `supplierdata_parser`).

4. **Update the `__init__.py`**
   Inside your renamed folder, open `__init__.py` and replace:

   ```python
   masterdata_parser_example_entry_point
   ```

   with:

   ```python
   [yourparsername_parser]_entry_point
   ```


5. **Update the `conftest.py`**
   Find the conftest file in the test folder
   ```sh
   [your repo name]
   ├── tests
   │   └── conftest.py
   ```
   And change the folder name in the import to:
     ```python
     from [yourparsername_parser].parser import MasterdataParserExample
     ```
---

### Tips

* Stick to Python package naming conventions:

  * lowercase only
  * use `_` instead of `-`
  * avoid spaces or special characters

* After renaming, run the following to check everything still works:

  ```sh
  pip install -e .
  pytest
  ```

  All tests should still pass — if not, double-check for missed occurrences of `masterdata_parser_example`.


## 3. Creating the Parser Class

This section will guide you through creating your own parser class for your specific data type.

---

### Steps

1. **Open the `parser.py` file** under:

   ```sh
   [your repo name]
   └── src
       └── '[yourparsername]'
           └── parser.py
   ```

2. **Modify imports**

   * Ignore `from bam_masterdata.parsing import AbstractParser` if not needed for your setup.
   * Change the object type import to the one relevant for your parser. For example:

     ```python
     from bam_masterdata.datamodel.object_types import Sem
     ```

   **Note:** Available data types can be found [here](https://github.com/BAMresearch/bam-masterdata/blob/main/bam_masterdata/datamodel/object_types.py)

3. **Define the parser class**

   * The class should inherit from `AbstractParser` and implement the `parse` method:

     ```python
     class [ParserClassName](AbstractParser):
         def parse(self, files, collection, logger):
             ...  # parse data from file
             ...  # create object type instances
             ...  # add object type instances to collection
	     ...  # log successful parsing in the logger
     ```

4. **Working with Object Types**

   * Create instances of the object type you imported. For example:

     ```python
     Sem(name="SemExampleName", ...)
     ```
   * The accepted values for each object type are listed in [bam-masterdata](https://github.com/BAMresearch/bam-masterdata/blob/main/bam_masterdata/datamodel/object_types.py)

5. **Add objects to the collection**

   * Use the `collection.add()` method to register each object instance, e.g.:

     ```python
     collection.add(Sem("$name"="SemExampleName", ...))
     ```

---

### Tips

* Keep your parser class focused on a single file type or data source for clarity.
* Use the logger to provide useful messages during parsing:

  ```python
  logger.info("Parsing file XYZ")
  ```
* Test your parser incrementally by adding one object at a time to the collection and verifying results.

## 4. Updating the entry\_points

This section explains how to register your parser so that it can be discovered and used by bam-masterdata.

---

### Steps

1. **Open `__init__.py`** in:

   ```sh
   [your repo name]
   └── src
       └── '[yourparsername]'
            └── __init__.py
   ```

2. **Update the parser import**

   * Change the import line from:

     ```python
     from .parser import MasterdataParserExample
     ```

     to:

     ```python
     from .parser import [ParserClassName]
     ```

3. **Update the entry\_points dictionary**

   * Update the dictionary values to reflect your parser:

     ```python
     entry_points = {
         "name": "[YourParserName]",
         "description": "[Your parser's description]",
         "parser_class": [ParserClassName]
     }
     ```
   * `"name"` → the display name of your parser
   * `"description"` → a short description of what your parser does
   * `"parser_class"` → the class you just implemented in `parser.py`

4. **Update the tests folder**

   * In the `conftest.py` change the example class in the import and in the parser() function to your [ParserClassName]
   * In the `test_parser.py` change the


---

### Tips

* Keep the description concise but informative.
* Ensure the parser class name matches exactly with the class in `parser.py` to avoid import errors.
* After updating, run `pip install -e .` and any relevant tests to confirm the parser is correctly registered.



---

## Final Steps

You now have all the core components of your custom parser in place:

- Project structure set up
- Package renamed to your parser name
- Parser class created
- Entry points updated

### What’s left?

1. **Update `pyproject.toml`**
   - Make sure the package name, version, and entry points match your parser.
   - Adjust dependencies if your parser requires additional libraries (e.g., `pandas`).

2. **Update the `README.md`**
   - Replace the template content with a description of your parser.
   - Document how to install it and how to run it.
   - Optionally, add usage examples for clarity.

---

✅ At this point, your parser should be ready to test and integrate into the bam-masterdata workflow.

