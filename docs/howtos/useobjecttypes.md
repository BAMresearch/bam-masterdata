## How To: Creating instances of object types and populating them with metadata

### Goal

By the end of this guide, you will know how to create and work with instances of object types defined in **bam-masterdata**.
You will learn how to:

* Import and use the available object types
* Populate them with metadata by assigning values to their properties
* Understand how these objects fit into the masterdata workflow (e.g., later being collected, stored, and queried)

Object types in **bam-masterdata** represent structured domain concepts (e.g., `Sem`, `ExperimentalStep`, `Sample`).
Each type comes with a set of predefined fields that describe metadata consistently across datasets.

---

### Requirements

To follow this guide, you will need:

* **Python ≥ 3.10** installed
* Access to the **bam-masterdata** repository or package
* Basic Python knowledge (functions, classes, error handling)
* A working development environment (e.g., VS Code, PyCharm, or terminal + editor)
* (Optional) A virtual environment (`.venv` or conda environment) to keep dependencies isolated

---

## 1. Installation & Setup

Install the package from PyPI:

```bash
pip install bam-masterdata
```

Or, if you are working from a local clone of the repository:

```bash
# from the repository root
pip install -e .
```

Import and quick smoke test:

```python
from bam_masterdata.datamodel.object_types import ExperimentalStep
# replace ExperimentalStep with your object type(s)

print("Import OK")
```

---
## 2. Overview of Object Types

All accessible object types are defined as Python classes in
`bam_masterdata.datamodel.object_types`.
Each object type has a set of attributes (metadata fields), some of which are required.

---

### Examples of Object Types

| Object Type       | Key Attributes (examples)           | Required Fields                    |
|-------------------|-------------------------------------|------------------------------------|
| `ExperimentalStep`| `name`,  `start_date`               |                                    |
| `Sem`             | `name`, `sem_instrument`            |                                    |
| `Storage`         | `name`, `storage_box_num`           | `storage_storage_validation_level` |

---

### Where to Find All Object Types
The full list of available object types and their attributes can be found in:
[bam_masterdata/datamodel/object_types.py](https://github.com/BAMresearch/bam-masterdata/blob/main/bam_masterdata/datamodel/object_types.py)

---

> 💡 **Tip:** Keep a small table like the one above in your own docs for quick reference to the object types and their required attributes.


## 3. Creating Instances

To use an object type, you create an instance of its class. At minimum, you must provide the required fields.
Here is a minimal example creating an `ExperimentalStep`:

```python
from bam_masterdata.datamodel.object_types import ExperimentalStep

step = ExperimentalStep(name="Step 1")
print(step) # prints propertie fields
```

---

### Explanation

* `ExperimentalStep` is imported from the `object_types` module.
* An instance is created by calling the class with its attributes (here: `name`).
* Optional attributes (such as `start_date`, etc.) can be added when needed.

---

### Example with more metadata

```python
from bam_masterdata.datamodel.object_types import ExperimentalStep

step = ExperimentalStep(
    name="Sample Preparation",
    start_date="2025 09 09",
)

print(step)
```

This creates a fully populated object that can later be added to a collection or used in workflows.


## 4. Assigning Metadata

Object types come with predefined attributes (metadata fields).
You can assign values to the object types directly or by using `setattr`.
To explore which attributes are available for a given type, check its `_property_metadata`.

### Listing available attributes

```python
from bam_masterdata.datamodel.object_types import ExperimentalStep

step = ExperimentalStep()
print(list(step._property_metadata.keys()))
# Example output:
# ['name', 'show_in_project_overview', 'finished_flag', 'start_date', ...]
```

### Setting values

```python
setattr(step, "name", "My Experimental Step")  # using setattr
print(step.name)  # -> My Experimental Step

# Or assign directly
step.finished_flag = True
```

### Working with dates and structured values

Dates should be provided in ISO 8601 format.
For example, to set today's date:

```python
from datetime import date

step.start_date = date.today().isoformat()
```

### Working with controlled vocabularies

Many object types have fields that only accept certain values (controlled vocabularies). Use the value codes found in [bam_masterdata/datamodel/vocabulary_types.py](https://github.com/BAMresearch/bam-masterdata/blob/main/bam_masterdata/datamodel/vocabulary_types.py) or check the class directly:
```python
from bam_masterdata.datamodel.vocabulary_types import StorageValidationLevel

print([term.code for term in StorageValidationLevel().terms])
# Out: ['BOX', 'BOX_POSITION', 'RACK']
```

```python
store = Storage()
store.storage_storage_validation_level = "BOX"  # CONTROLLEDVOCABULARY

print(store.storage_storage_validation_level)
```

### Checking mandatory fields

Some object types have required attributes that must be set to avoid validation errors.
You can inspect which fields are mandatory as follows:

```python
from bam_masterdata.datamodel.object_types import Storage

test_type = Storage()
mandatory = [key for key, value in test_type._property_metadata.items() if value.mandatory]
print(mandatory)
# Example output: ['storage_storage_validation_level']
```

---


## 5. Validation & Error Handling

It is important to validate object integrity before saving or exporting any object type instances.
There are two main types of validation:

### 1. Check valid attributes

```python
from bam_masterdata.datamodel.object_types import ExperimentalStep
from datetime import date

validate = ExperimentalStep()
try:
    setattr(validate, "start-date", date.today().isoformat())
except Exception as e:
    print(f"Validation error: {e}")
# Example output:
# Validation error: "Key 'start-date' not found in ..."
```

### 2. Check valid values

```python
validate = ExperimentalStep()
try:
    setattr(validate, "start_date", 2000)
except Exception as e:
    print(f"Validation error: {e}")
# Example output:
# Validation error: Invalid type for 'start_date': Expected datetime or ISO format string, got int
```

---

> 💡 **Tip:** Validate early and often to catch errors before they propagate.

## 6. Automation of Object Creation
To automate the process of creatin an Object use self defined python functions e.g.:
```python
def metadata_to_instance(metadata: dict, instance: object):
    """sets metadata in the object class

    Args:
        metadata (dict): Metadata of Object
        instance (object): Object-Class-Instance

    Returns:
        Object-Instance
    """
    props = metadata_to_masterdata(metadata, instance) # validate values and keys
    for k, v in props.items():
        setattr(instance, k, v) # set keys
    return instance


def metadata_to_masterdata(metadata: dict, object_instance: object):
    """checks if avaliable metadata is in Object-Attributes

    Args:
        metadata (dict): Metadata of Object
        object_instance (object): Object-Class-Instance

    Returns:
         List with verified Object-Attributes
    """
    avaliable_values = object_instance._property_metadata # call valid keys
    data = metadata
    object_prop_list = {
        prop_name: data_value
        for prop_name, prop_obj in avaliable_values.items()
        if (data_value := data.get(prop_name)) is not None
    } # validate data
    return object_prop_list
```
Then only use a dict and function call to create your objects
```python
metadata = {
    "name": "My Experimental Step",
    "start_date": "2023-10-10",
}

instance = metadata_to_instance(metadata, ExperimentalStep())
```

## 7. Saving your Objects in a collection
Most usecases end with saving their objects in a colletion for further use.
This can be done with:
```python
from bam_masterdata.metadata.entities import CollectionType

collection = CollectionType()
objectid1 = collection.add(instance1)
objectid2 = collection.add(instance2)
print(collection.attached_objects) #see attached objects

# Establish a parent-child relationship
collection.add_relationship(objectid1, objectid2)
# objectid1 is the parent of objectid2

```