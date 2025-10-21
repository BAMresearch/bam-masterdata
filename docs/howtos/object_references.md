# How-to: Work with Object References

This how-to guide shows you how to work with properties whose data type is OBJECT in order to reference other objects in openBIS.

## What are object references?

Some object types have properties with `data_type="OBJECT"` that create references to other objects. For example:

- An `Instrument` might have a `responsible_person` property that references a `Person` object
- A `Calibration` might have an `instrument` property that references an `Instrument` object
- A `Sample` might have a `parent_sample` property that references another `Sample` object

These are properties defined to reference other existing objects in openBIS. Their purpose is to link between objects, similar to what a parent-child relationship do. However, these links have a semantic meaning, while parent-child relationships are only connecting inputs with outputs.

??? note "Semantic meaning of object referencing"
    The semantic meaning of object referencing is given by the name of the property (e.g., a person responsible for operating an instrument). Nevertheless, openBIS will soon allow for adding more metainformation to these properties to create a more complete description of objects and their relationships.

## Option 1: Reference by Object Instance

When creating multiple related objects in the same operation, you can reference them directly:

```python
from bam_masterdata.datamodel.object_types import Person, Instrument
from bam_masterdata.metadata.entities import CollectionType

# Create a collection
collection = CollectionType()

# Create a person
person = Person(name="Dr. Jane Smith")
person.code = "PERSON_001"  # ⚠️ Must set a code!
person_id = collection.add(person)

# Create an instrument and reference the person
instrument = Instrument(name="High-Resolution Microscope")
instrument.responsible_person = person  # Direct reference
instrument_id = collection.add(instrument)
```

!!! warning "Object must have a code"
    When referencing an object instance, it **must** have a `code` attribute set. If not, you'll get a `ValueError`:

    ```
    ValueError: Object instance for 'responsible_person' must have a 'code' attribute set
    ```

## Option 2: Reference by Path String

If the object already exists in openBIS, you can reference it using its identifier path:

```python
from bam_masterdata.datamodel.object_types import Instrument

# Create an instrument
instrument = Instrument(name="Spectrometer X500")

# Reference an existing person using the path format
# Format: /{space}/{project}/{collection}/{object}
instrument.responsible_person = "/LAB_SPACE/INSTRUMENTS/STAFF/PERSON_001"

# Or without collection: /{space}/{project}/{object}
instrument.responsible_person = "/LAB_SPACE/INSTRUMENTS/PERSON_001"
```

!!! note "Path validation"
    The path must:

    - Start with `/`
    - Have either 3 parts (space/project/object) or 4 parts (space/project/collection/object)
    - Point to an existing object in openBIS

## Combining Both Approaches

You can mix both approaches in the same parser:

```python
from bam_masterdata.parsing import AbstractParser
from bam_masterdata.datamodel.object_types import Person, Instrument

class InstrumentParser(AbstractParser):
    def parse(self, files, collection, logger):
        # Create a new person
        new_person = Person(name="Dr. Alice Johnson")
        new_person.code = "PERSON_NEW_001"
        collection.add(new_person)

        # Instrument 1: References the newly created person
        instrument1 = Instrument(name="Microscope A")
        instrument1.responsible_person = new_person  # Object instance
        collection.add(instrument1)

        # Instrument 2: References an existing person in openBIS
        instrument2 = Instrument(name="Microscope B")
        instrument2.responsible_person = "/LAB_SPACE/PROJECT/PERSON_EXISTING"  # Path
        collection.add(instrument2)
```

## Troubleshooting

### Error: "Object instance must have a 'code' attribute set"

**Cause**: You're trying to reference an object instance that doesn't have a code.

**Solution**: Set the `code` attribute before using the object as a reference:

```python
person = Person(name="Dr. Smith")
person.code = "PERSON_001"  # ✓ Set the code
instrument.responsible_person = person
```

### Error: "Invalid OBJECT path format"

**Cause**: The path string doesn't follow the required format.

**Solution**: Ensure your path:

- Starts with `/`
- Has 3 or 4 parts separated by `/`

```python
# ✗ Wrong
instrument.responsible_person = "PERSON_001"
instrument.responsible_person = "SPACE/PROJECT/PERSON_001"

# ✓ Correct
instrument.responsible_person = "/SPACE/PROJECT/PERSON_001"
instrument.responsible_person = "/SPACE/PROJECT/COLLECTION/PERSON_001"
```

### Error: "Failed to resolve OBJECT reference"

**Cause**: The path references an object that doesn't exist in openBIS.

**Solution**: Verify the object exists in openBIS at the specified path, or create it first:

```python
# Check if the object exists in openBIS before referencing
openbis = ologin(...)
try:
    obj = openbis.get_object("/SPACE/PROJECT/PERSON_001")
    print(f"Object exists: {obj.identifier}")
except:
    print("Object not found - create it first or use a different path")
```
