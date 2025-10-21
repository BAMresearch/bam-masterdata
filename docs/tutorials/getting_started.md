# Getting Started with `bam-masterdata`

This tutorial will guide you through your first interaction with the `bam-masterdata` package, helping you understand its core concepts and basic functionality.

## What is `bam-masterdata`?

The `bam-masterdata` is a Python package designed to help administrators and users to manage the [Masterdata](../references/glossary.md#masterdata)/schema definitions. It provides with a set of Python classes and utilities for working with different types of entities in the openBIS Research Data Management (RDM) system. It also contains the Masterdata definitions used at the Bundesanstalt für Materialforschung und -prüfung (BAM) in the context of Materials Science and Engineering research.

*[Image placeholder: Architecture overview diagram showing the relationship between BAM Masterdata, openBIS, and the BAM Data Store. The diagram should illustrate data flow and the role of masterdata schemas in the system.]*

The `bam-masterdata` provides you with tools to:

- Export the Masterdata from your openBIS instance.
- Update the Masterdata in your openBIS instance.
- Export/Import from different formats: Excel, Python, RDF/XML, JSON.
- Check consistency of the Masterdata with respect to a ground truth.
- Automatically parse metainformation in your openBIS instance.

!!! note "Prerequisites"
    - Basic Python and openBIS knowledge.
    - A system with Python 3.10 or higher.
    - Knowledge of virtual environments, CLI usage, IDEs such as VSCode, and GitHub.

!!! warning
    Note all steps in this documentation are done in Ubuntu 22.04. All the commands in the terminal need to be modified if you work from Windows.

## Installation and Setup


### Create an empty test directory

We will test the basic functionalities of `bam-masterdata` in an empty directory. Open your terminal and type:
```bash
mkdir test_bm
cd test_bm/
```

### Create a Virtual Environment

We strongly recommend using a virtual environment to avoid conflicts with other packages.

**Using venv:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Using conda:**
```bash
conda create --name .venv python=3.10  # or any version 3.10 <= python <= 3.12
conda activate .venv
```

### Install the Package

`bam-masterdata` is part of the PyPI registry and can be installed via pip:
```bash
pip install --upgrade pip
pip install bam-masterdata
```

!!! tip "Faster Installation"
    For faster installation, you can use [`uv`](https://docs.astral.sh/uv/):
    ```bash
    pip install uv
    uv pip install bam-masterdata
    ```

### Verify Installation

You can verify that the installation was successful. Open a Python script and write:
```python
from importlib.metadata import version


print(f"BAM Masterdata version: {version("bam_masterdata")}")
```

And running in your terminal:
```bash
python <path-to-Python-script>
```

This should return the version of the installed package.

## Your First `bam-masterdata` Experience

### Understanding Entity Types

The BAM Masterdata system organizes information into different entity types:

- **Object Types**: Physical or conceptual objects (samples, instruments, people)
- **Collection Types**: Groups of related objects
- **Dataset Types**: Data files and their metadata
- **Vocabulary Types**: Controlled vocabularies for standardized values

*[Image placeholder: Entity relationship diagram showing the four main entity types and their relationships. Should include sample instances of each type.]*

??? info "Deprecating Collection Types and Dataset Types"
    As of September 2025, the development of new Collection and Dataset types is stalled. We will use the abstract concepts only, i.e., a Collection Type is a class used to add objects to it and their relationships, and a Dataset Type is a class to attach raw data files to it.

### Overview of the Object Types

The central ingredients for defining data models associated with a research activity are the Object Types. These are classes inheriting from an abstract class called `ObjectType` and with two types of attributes:

- `defs`: The definitions of the Object Type. These attributes do not change when filling with data the object.
- `properties`: The list of properties assigned to an object. These attributes are filled when assigning data to the object.

All accessible object types are defined as Python classes in [`bam_masterdata/datamodel/object_types.py`](https://github.com/BAMresearch/bam-masterdata/tree/main/bam_masterdata/datamodel/object_types.py).
Each object type has a set of assigned properties (metadata fields), some of which are **mandatory** and some are **optional**. For example:
```python
class Chemical(ObjectType):
    defs = ObjectTypeDef(
        code="CHEMICAL",
        description="""Chemical Substance//Chemische Substanz""",
        generated_code_prefix="CHEM",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative Name",
        description="""e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    # ... more PropertyTypeAssignment
```

You can read more in [Schema Definitions](../explanations/schema_defs.md) to learn about the definitions of Object Types and how to assign properties.


### Creating Your First Entity

Let's create/instantiate a simple experimental step object:

```python
from bam_masterdata.datamodel.object_types import ExperimentalStep


# Create a new experimental step instance
step = ExperimentalStep(
    name="SEM measurement",
    finished_flag=True,
)
print(step) # prints the object type and its assigned properties
```

This will print:
```bash
SEM measurement:ExperimentalStep(name="SEM measurement", finished_flag=True)
```

You can assign values to other properties after instantiation as well:

```python
step.show_in_project_overview = True
print(step)
```
This will print:
```bash
SEM measurement:ExperimentalStep(name="SEM measurement", show_in_project_overview=True, finished_flag=True)
```

If the type of the property does not match the expected type, an error will be shown. For example, `ExperimentalStep.show_in_project_overview` is a boolean, hence:
```python
step.show_in_project_overview = 2
```
will return:
```bash
TypeError: Invalid type for 'show_in_project_overview': Expected bool, got int
```

## Available properties for an Object Type

To explore which attributes are available for a given type, check its `_property_metadata`.

```python
from bam_masterdata.datamodel.object_types import ExperimentalStep

step = ExperimentalStep()
print(list(step._property_metadata.keys()))
```
will return:
```bash
['name', 'show_in_project_overview', 'finished_flag', 'start_date', ...]
```

If you want a detailed list of the `PropertyTypeAssignment` assigned to an Object Type, you can print `properties` instead.

## Data types

The data types for each assigned property are defined according to openBIS. These have their direct counterpart in Python types. The following table shows the equivalency of each type:

| DataType             | Python type        | Example assignment                                     |
|----------------------|-------------------|--------------------------------------------------------|
| `BOOLEAN`            | `bool`            | `myobj.flag = True`                                    |
| `CONTROLLEDVOCABULARY` | `str` (enum term code) | `myobj.status = "ACTIVE"` (must match allowed vocabulary term) |
| `DATE`               | `datetime.date`   | `myobj.start_date = datetime.date(2025, 9, 29)`        |
| `HYPERLINK`          | `str`             | `myobj.url = "https://example.com"`                    |
| `INTEGER`            | `int`             | `myobj.count = 42`                                     |
| `MULTILINE_VARCHAR`  | `str`             | `myobj.notes = "Line 1\nLine 2\nLine 3"`               |
| `OBJECT`             | `ObjectType` or `str` (path) | `myobj.parent = person_obj` or `myobj.parent = "/SPACE/PROJECT/PERSON_001"` |
| `REAL`               | `float`           | `myobj.temperature = 21.7`                             |
| `TIMESTAMP`          | `datetime.datetime` | `myobj.created_at = datetime.datetime.now()`           |
| `VARCHAR`            | `str`             | `myobj.name = "Test sample"`                           |
| `XML`                | `str` (XML string) | `myobj.config = "<root><tag>value</tag></root>"`       |


## Working with controlled vocabularies

Many object types have fields that only accept certain values (controlled vocabularies). Use the value codes found in [bam_masterdata/datamodel/vocabulary_types.py](https://github.com/BAMresearch/bam-masterdata/blob/main/bam_masterdata/datamodel/vocabulary_types.py) or check the class directly:
```python
from bam_masterdata.datamodel.vocabulary_types import StorageValidationLevel


print([term.code for term in StorageValidationLevel().terms])
```
will return:
```bash
['BOX', 'BOX_POSITION', 'RACK']
```

Thus we can assign only:
```python
from bam_masterdata.datamodel.object_types import Storage


store = Storage()
store.storage_storage_validation_level = "BOX"  # CONTROLLEDVOCABULARY
```

!!! tip
    When assigning values to properties assigned to Object Types, we recommend carefully [handling potential errors](https://blog.miguelgrinberg.com/post/the-ultimate-guide-to-error-handling-in-python).
    This will allow your scripts to work without interruption and with a total control of conflictive lines.


## Working with object references

Some object types have properties that reference other objects in openBIS (when data type is `OBJECT`). For example, an `Instrument` might have a `responsible_person` property that references a `Person` object.

There are two ways to assign object references:

### 1. Using an Object Instance

If you're creating objects in the same batch, you can directly reference the object instance.

```python
from bam_masterdata.datamodel.object_types import Instrument

# Create a person object
person = Person(name="Dr. Jane Smith")
person.code = "PERSON_001"  # Must have a code to be used as reference

# Create an instrument and reference the person
instrument = Instrument(name="Microscope A")
instrument.responsible_person = person  # Direct object reference
```

!!! warning "Object must have a code"
    When using object instances as references, they must have a `code` attribute set. Otherwise, a `ValueError` will be raised.

### 2. Using a Path String

If the object already exists in openBIS, you can reference it using its identifier path:

```python
# Reference an existing object using its path
instrument = Instrument(name="Microscope B")

# Path format: /{space}/{project}/{collection}/{object}
instrument.responsible_person = "/LAB_SPACE/PEOPLE_LIST_PROJECT/STAFF_COLLECTION/PERSON_001"

# Or without collection: /{space}/{project}/{object}
instrument.responsible_person = "/LAB_SPACE/PEOPLE_LIST_PROJECT/PERSON_001"
```

!!! note "Path format validation"
    The path must:

    - Start with a forward slash `/`
    - Have either 3 parts (space/project/object) or 4 parts (space/project/collection/object)
    - Match an existing object identifier in openBIS

### When to use each approach

- **Use object instances** when creating multiple related objects in the same parsing operation. This option is the alternative to defining parent-child relationships if in an Object Type definition you have assigned a property of a certain data type OBJECT.
- **Use path strings** when referencing existing objects in openBIS that were created separately.

Example combining both approaches:

```python
from bam_masterdata.metadata.entities import CollectionType

collection = CollectionType()

# Create and add a person
person = Person(name="Dr. Smith")
person.code = "PERSON_001"
person_id = collection.add(person)

# Create instrument referencing the new person (by instance)
instrument1 = Instrument(name="Instrument 1")
instrument1.responsible_person = person
collection.add(instrument1)

# Create another instrument referencing an existing person in openBIS (by path)
instrument2 = Instrument(name="Instrument 2")
instrument2.responsible_person = "/MY_SPACE/MY_PROJECT/EXISTING_PERSON_002"
collection.add(instrument2)
```


## Saving your Object Types instances in a collection

Most usecases end with saving the Object Types and their field values in a colletion for further use.
This can be done by adding those Object Types in a `CollectionType` like:
```python
from bam_masterdata.metadata.entities import CollectionType
from bam_masterdata.datamodel.object_types import ExperimentalStep


step_1 = ExperimentalStep(name="Step 1")

collection = CollectionType()
step_1_id = collection.add(step_1)
print(collection)
```

This will return the `CollectionType` with the attached objects:
```bash
CollectionType(attached_objects={'EXP8f78245b': ExperimentalStep(name='Step 1')}, relationships={})
```

You can also add relationships between objects by using their ids when attached to the `CollectionType`:
```python
from bam_masterdata.metadata.entities import CollectionType
from bam_masterdata.datamodel.object_types import ExperimentalStep


step_1 = ExperimentalStep(name="Step 1")
step_2 = ExperimentalStep(name="Step 2")

collection = CollectionType()
step_1_id = collection.add(step_1)
step_2_id = collection.add(step_2)
_ = collection.add_relationship(parent_id=step_1_id, child_id=step_2_id)
print(collection)
```
will return:
```bash
CollectionType(attached_objects={'EXP3e6f674e': ExperimentalStep(name='Step 1'), 'EXP87b64b62': ExperimentalStep(name='Step 2')}, relationships={'EXP3e6f674e>>EXP87b64b62': ('EXP3e6f674e', 'EXP87b64b62')})
```

## Converting Object Types

The package supports various export formats for working with Object Types. These divide in two main purposes:

- Exporting the schema definitions: this is done using the methods `model_to_<format>()`.
- Exporting the data model: this is done using the methods `to_<format()>`.

For example:
```python
# Convert data model to dictionary
step_dict = step.to_dict()
# Convert schema to dictionary
step_schema_dict = step.model_to_dict()
print(step_dict)  # print: {'name': 'SEM measurement', 'finished_flag': True}
print(step_schema_dict)  # print: {'properties': [{...}, {...}, {...}, {...}, {...}, {...}, {...}, {...}, {...}, {...}, {...}, {...}, {...}, {...}], 'defs': {'code': 'EXPERIMENTAL_STEP', 'description': 'Experimental Step (generic)//Experimenteller Schritt (allgemein)', 'iri': None, 'id': 'ExperimentalStep', 'row_location': None, 'validation_script': None, 'generated_code_prefix': 'EXP', 'auto_generate_codes': True}}

# Convert to JSON
step_json = step.to_json()
step_schema_json = step.model_to_json()
```

The possible export formats can be found in the [API Reference](../references/api.md) documentation page.


## Working with real raw data

In order to work with raw data, you will need to create a script (also called _parser_) to read the i/o files metainformation, and map such information to the corresponding Object Types classes and properties. You can find more information in [How-to: Create new parsers](../howtos/parsing/create_new_parsers.md)


## Using the Command Line Interface

The package provides a CLI for common operations:

```bash
# Export current masterdata to Excel
bam_masterdata export_to_excel --export-dir=example_export_excel

# Fill masterdata from OpenBIS
bam_masterdata fill_masterdata
```

A comprehensive explanation of all options can be found in the terminal when adding the `--help` flag at the end of the command. For example:
```bash
bam_masterdata export_to_json --help
```
will produce:
```sh
Usage: bam_masterdata export_to_json [OPTIONS]

  Export entities to JSON files to the `./artifacts/` folder.

Options:
  --force-delete BOOLEAN  (Optional) If set to `True`, it will delete the
                          current `./artifacts/` folder and create a new one.
                          Default is `False`.
  --python-path TEXT      (Optional) The path to the individual Python module
                          or the directory containing the Python modules to
                          process the datamodel. Default is the `/datamodel/`
                          directory.
  --export-dir TEXT       The directory where the JSON files will be exported.
                          Default is `./artifacts`.
  --single-json BOOLEAN   Whether the export to JSON is done to a single JSON
                          file. Default is False.
  --help                  Show this message and exit.
```

## Next Steps

Now that you've completed this tutorial, you can:

1. **Explore the How-to Guides**: Learn specific tasks and workflows when using `bam-masterdata`.
2. **Read the Explanations**: Understand the concepts behind the system.
3. **Browse the API Reference**: Dive deep into specific classes and methods.


## Development Setup

If you want to contribute or modify the package:

```bash
git clone https://github.com/BAMresearch/bam-masterdata.git
cd bam-masterdata
python3 -m venv .venv
source .venv/bin/activate
./scripts/install_python_dependencies.sh
```

Read the `README.md` for more details.
