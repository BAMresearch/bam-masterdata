# How To: Creating instances of object types and populate them with metadata

### Goal:

By the end of this guide, you will know how to create instances of object types defined in **bam-masterdata** and populate them with metadata.
You will learn how to use the available object types, assign values to their properties, and understand how these objects fit into the masterdata workflow.

### Requirements

To follow this guide, you will need:

- **Python ≥ 3.10** installed
- Access to the **bam-masterdata** repository or package
- Basic Python knowledge (functions, classes, error handling)
- A working development environment (e.g., VS Code, PyCharm, or terminal + editor)

---

## 1. Installation & Setup

Install the package with:

```bash
pip install bam-masterdata
```

If you work from a local clone of the repo:

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

All accessable Object Types are in bam_masterdata.datamodel.object_types with their
attributes.


UMl Diagramm?

> Tip: Keep a short table in your docs listing key properties and which are required.

---

## 3. Creating Instances

Minimal example creating an `ExperimentalStep`:

```python
from bam_masterdata.datamodel.object_types import ExperimentalStep

object_type = ExperimentalStep()

```

If your objects require specific fields, provide them at construction time to avoid validation errors. This can be checked using:

```python
test_type = Storage() # has mandatory value
print([key for key, value in test_type._property_metadata.items() if value.mandatory])
# Out: ['storage_storage_validation_level']
```

---

## 4 Assigning Metadata

Add descriptive fields and a metadata dictionary:

```python
from bam_masterdata.datamodel.object_types import ExperimentalStep

object_type = ExperimentalStep()
print(list(object_type._property_metadata.keys()))  # List of populable Attributes
# -> Out: ['name', 'show_in_project_overview', 'finished_flag', 'start_date', ..... ]
setattr(object_type, "name", "My Experimental Step") # Sets property
print(object_type.name)  # Out: My Experimental Step
```

Dates (ISO 8601) and structured values work well:

```python
from datetime import date

object_type.start_date = date.today().isoformat()
```

---

## 5) Validation & Error Handling

Validate object integrity before saving or exporting:

```python
try:
    customer.validate()  # may raise ValueError/ValidationError depending on your lib
except Exception as e:
    print(f"Validation error: {e}")
```

> Tip: Validate early and often, especially before persisting or sending data across services.

---

## 6) Serialization & I/O

Convert to plain Python structures for storage or transport:

```python
import json

as_dict = customer.to_dict()      # or: dataclasses.asdict(), model_dump(), etc.
print(json.dumps(as_dict, indent=2))
```

Save to a JSON file:

```python
with open("customer.json", "w", encoding="utf-8") as f:
    json.dump(as_dict, f, ensure_ascii=False, indent=2)
```

Batch processing a list of objects:

```python
customers = [
    Customer(id="CUST-001", name="Example Corp"),
    Customer(id="CUST-002", name="Another Co")
]

payload = [c.to_dict() for c in customers]
with open("customers.json", "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)
```

---

## 7) Linking Objects (Optional)

If objects reference each other, store IDs or dedicated link objects:

```python
from bam_masterdata.objects import Asset

asset = Asset(id="ASSET-100", name="Edge Gateway")
asset.owner_id = customer.id  # reference by foreign key / ID
```

Or use a relationship object if your library provides one.

---

## 8) Putting It Into the Masterdata Workflow

Typical steps:
1. Create/collect objects (possibly from CSVs or APIs).
2. Enrich with metadata (standardized keys, types, and formats).
3. Validate.
4. Serialize to JSON or call your masterdata service API.
5. Log results and handle errors/retries.

Example stub for an API call (pseudo-code):

```python
import requests, json

payload = customer.to_dict()
resp = requests.post("https://masterdata.example/api/v1/customers", json=payload, timeout=10)
resp.raise_for_status()
```

---

## 9) Troubleshooting

- **ImportError / ModuleNotFoundError**: Check your virtualenv and installation path (`pip show bam-masterdata`).
- **Validation errors**: Ensure required fields are present and types/values match expectations.
- **Serialization issues**: Convert non-JSON types (dates, Decimals) to strings or numbers first.
- **Version mismatches**: Pin compatible versions in `requirements.txt` or `pyproject.toml`.

---

## 10) Summary & Next Steps

You created objects, added metadata, validated them, serialized to JSON, and saw how to link objects within a masterdata workflow.

**Next steps:**
- Define a shared metadata schema and enumerations (regions, sectors, tags).
- Implement relationship modeling and referential checks.
- Add automated validation in CI (unit tests + sample fixtures).
- Provide CLI/Notebooks for batch imports and audits.
