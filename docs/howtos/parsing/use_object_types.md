# How-to: Work with Object Types



This guide explains how to create and use object type instances defined in **bam-masterdata**.
Object types represent structured domain concepts (e.g., `ExperimentalStep`, `Sample`, `Sem`) and come with predefined metadata fields.
By the end of this guide, you will know how to:

- Import and instantiate object types
- Assign metadata to their properties
- Work with controlled vocabularies
- Validate objects and save them into collections

!!! note "Prerequisites"
    - **Python ≥ 3.10** installed

---


## Installation & Setup

1. Create a folder and open the terminal. Type:
    ```sh
    cd test_folder/
    ```
2. Create a virtual environment with `venv` or `conda`:
    - `venv`
        ```sh
        python -m venv .venv
        source .venv/bin/activate  # on Linux/macOS
        .\.venv\Scripts\activate  # on Windows
        ```
    - `conda`
        ```sh
        conda create --prefix .venv python=3.10
        conda activate .venv
        ```
3. Install the package:
    ```sh
    pip install --upgrade pip
    pip install bam-masterdata
    ```
4. Create a Python script `test_folder/test.py` and verify that the installation worked:
    ```python
    from bam_masterdata.datamodel.object_types import ExperimentalStep


    print("Import OK")
    ```



## Overview of the Object Types

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
```

You can read more in [Schema Definitions](../../explanations/schema_defs.md) to learn about the definitions of Object Types and how to assign properties.

!!! warning
    Note that the schema definitions is evolving and will likely change in the future from version to version. Thus, parsers need to be adapted and versioned according to `bam-masterdata`.


## Instantiating Object Types

To use an object type, you create an instance of its class. At minimum, you must provide the **mandatory** fields.
Here is a minimal example creating an `ExperimentalStep`:

```python
from bam_masterdata.datamodel.object_types import ExperimentalStep


step = ExperimentalStep(name="Step 1")
print(step) # prints the object type and its assigned properties
```

This will print:
```bash
Step 1:ExperimentalStep(name="Step 1")
```

You can assign values to other properties after instantiation as well:

```python
from bam_masterdata.datamodel.object_types import ExperimentalStep


step = ExperimentalStep(name="Step 1")
print(step) # prints the object type and its assigned properties
step.show_in_project_overview = True
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
| `OBJECT`             | (openBIS object reference) | `myobj.parent = another_object_instance` (depends on schema) |
| `REAL`               | `float`           | `myobj.temperature = 21.7`                             |
| `TIMESTAMP`          | `datetime.datetime` | `myobj.created_at = datetime.datetime.now()`           |
| `VARCHAR`            | `str`             | `myobj.name = "Test sample"`                           |
| `XML`                | `str` (XML string) | `myobj.config = "<root><tag>value</tag></root>"`       |




## Assigning controlled vocabularies

Many object types have fields that only accept certain values (controlled vocabularies). Use the value codes found in [bam_masterdata/datamodel/vocabulary_types.py](https://github.com/BAMresearch/bam-masterdata/blob/main/bam_masterdata/datamodel/vocabulary_types.py) or check the class directly:
```python
from bam_masterdata.datamodel.vocabulary_types import StorageValidationLevel


print([term.code for term in StorageValidationLevel().terms])
# Out: ['BOX', 'BOX_POSITION', 'RACK']
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