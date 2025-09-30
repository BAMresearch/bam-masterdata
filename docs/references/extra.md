## Usage Examples

### Basic Entity Operations

```python
from bam_masterdata.datamodel.object_types import Sample
from bam_masterdata.datamodel.dataset_types import RawData
from bam_masterdata.datamodel.collection_types import MeasurementsCollection

# Create entities
sample = Sample(code="SAMPLE_001", name="Test Sample")
dataset = RawData(code="DATA_001", name="Raw measurement data")
collection = MeasurementsCollection(code="COLL_001", name="Test Collection")

# Convert to different formats
sample_dict = sample.to_dict()
sample_json = sample.to_json()
openbis_sample = sample.to_openbis()
```

### Excel Integration

```python
from bam_masterdata.excel.excel_to_entities import MasterdataExcelExtractor
import openpyxl

# Load Excel file
workbook = openpyxl.load_workbook("masterdata.xlsx")

# Extract entities
extractor = MasterdataExcelExtractor()
entities = extractor.excel_to_entities(workbook)

# Access extracted data
object_types = entities.get("object_types", {})
dataset_types = entities.get("dataset_types", {})
```

### openBIS Operations

```python
from bam_masterdata.openbis.login import ologin
from bam_masterdata.openbis.get_entities import OpenbisEntities

# Connect to openBIS
openbis = ologin(url="https://openbis.example.com", username="user", password="pass")

# Retrieve entities
openbis_entities = OpenbisEntities(openbis)
object_dict = openbis_entities.get_object_dict()
dataset_dict = openbis_entities.get_dataset_dict()
```

### Validation

```python
from bam_masterdata.checker.masterdata_validator import MasterdataValidator

# Validate entities
validator = MasterdataValidator()
entities_dict = {
    "object_types": object_types,
    "dataset_types": dataset_types
}

result = validator.validate(entities_dict)
if not result.is_valid:
    for error in result.errors:
        print(f"Validation error: {error}")
```

### Code Generation

```python
from bam_masterdata.cli.fill_masterdata import MasterdataCodeGenerator

# Generate Python code from entity definitions
generator = MasterdataCodeGenerator(
    objects=object_types,
    datasets=dataset_types,
    collections=collection_types,
    vocabularies=vocabulary_types
)

# Generate code for different entity types
object_code = generator.generate_object_types()
dataset_code = generator.generate_dataset_types()
vocab_code = generator.generate_vocabulary_types()
```

## Type Definitions

### Entity Definitions

The package uses several base definition classes that define the structure of entities:

- `EntityDef`: Base definition class for all entities
- `ObjectTypeDef`: Defines object type structure
- `DatasetTypeDef`: Defines dataset type structure
- `CollectionTypeDef`: Defines collection type structure
- `VocabularyTypeDef`: Defines vocabulary structure

### Property Definitions

Properties are defined using:

- `PropertyTypeDef`: Basic property definition
- `PropertyTypeAssignment`: Property assignment to entity types
- `VocabularyTerm`: Individual terms in controlled vocabularies

### Data Types

The system supports several data types for properties:

- `VARCHAR`: Variable-length character strings
- `MULTILINE_VARCHAR`: Multi-line text
- `INTEGER`: Whole numbers
- `REAL`: Floating-point numbers
- `BOOLEAN`: True/false values
- `TIMESTAMP`: Date and time values
- `CONTROLLEDVOCABULARY`: Values from controlled vocabularies
- `XML`: Structured XML data
```

## Configuration

The package can be configured through various mechanisms:

### Environment Variables

- `BAM_MASTERDATA_CONFIG_PATH`: Path to configuration file
- `OPENBIS_URL`: Default openBIS server URL
- `OPENBIS_USERNAME`: Default username for openBIS
- `LOG_LEVEL`: Logging level (DEBUG, INFO, WARNING, ERROR)

### Configuration File

```yaml
# config.yaml
openbis:
  url: "https://openbis.example.com"
  username: "default_user"
  timeout: 30

validation:
  strict_mode: true
  required_properties: ["name", "description"]

logging:
  level: "INFO"
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
```

### Programmatic Configuration

```python
from bam_masterdata.config import Configuration

# Load configuration
config = Configuration.load_from_file("config.yaml")

# Override specific settings
config.set("openbis.url", "https://my-openbis.com")
config.set("validation.strict_mode", False)

# Apply configuration
Configuration.apply(config)
```




## Working with Entity Types

### How to Create Custom Entity Types

```python
from bam_masterdata.metadata.entities import ObjectType
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment

class MyCustomObject(ObjectType):
    defs = ObjectTypeDef(
        code="MY_CUSTOM_OBJECT",
        description="A custom object type for specific needs"
    )

    custom_property = PropertyTypeAssignment(
        code="CUSTOM_PROP",
        data_type="VARCHAR",
        property_label="Custom Property",
        description="A custom property for this object",
        mandatory=True,
        section="Custom Section"
    )
```

### How to Query Available Properties

```python
from bam_masterdata.datamodel.object_types import Sample

# Get all available properties for a Sample
sample = Sample()
properties = sample.get_property_metadata()

for prop_code, metadata in properties.items():
    print(f"Property: {prop_code}")
    print(f"  Label: {metadata.property_label}")
    print(f"  Type: {metadata.data_type}")
    print(f"  Mandatory: {metadata.mandatory}")
    print()
```

### How to Validate Entity Data

```python
from bam_masterdata.checker.masterdata_validator import MasterdataValidator

# Create validator
validator = MasterdataValidator()

# Validate your entity data
entities_dict = {"object_types": {"SAMPLE_001": sample.to_dict()}}
validation_result = validator.validate(entities_dict)

if validation_result.is_valid:
    print("✓ Validation passed")
else:
    print("✗ Validation failed:")
    for error in validation_result.errors:
        print(f"  - {error}")
```

## Data Import and Export

### How to Import from Excel Files

*[Image placeholder: Excel spreadsheet template showing the correct structure for masterdata import with headers, entity types, properties, and sample data rows.]*

```python
from bam_masterdata.excel.excel_to_entities import MasterdataExcelExtractor

# Initialize extractor
extractor = MasterdataExcelExtractor()

# Load workbook
import openpyxl
workbook = openpyxl.load_workbook("masterdata.xlsx")

# Extract entities
entities = extractor.excel_to_entities(workbook)

# Access extracted data
object_types = entities.get("object_types", {})
dataset_types = entities.get("dataset_types", {})
print(f"Loaded {len(object_types)} object types")
print(f"Loaded {len(dataset_types)} dataset types")
```

### How to Export to Excel

```python
from bam_masterdata.cli.entities_to_excel import entities_to_excel
from bam_masterdata.metadata.entities_dict import EntitiesDict

# Prepare your entities data
entities_dict = EntitiesDict({
    "object_types": {"SAMPLE_001": sample.to_dict()},
    "dataset_types": {},
    "collection_types": {},
    "vocabulary_types": {}
})

# Export to Excel
entities_to_excel(entities_dict, "output.xlsx")
print("✓ Exported to output.xlsx")
```

### How to Export to JSON

```python
import json

# Single entity to JSON
entity_json = sample.to_json()

# Multiple entities to JSON
entities_dict = {
    "object_types": {
        "SAMPLE_001": sample.to_dict()
    }
}

with open("entities.json", "w") as f:
    json.dump(entities_dict, f, indent=2)
```

### How to Export to RDF

```python
from bam_masterdata.cli.entities_to_rdf import entities_to_rdf, rdf_graph_init

# Initialize RDF graph
graph = rdf_graph_init()

# Add entities to graph
entities_to_rdf(entities_dict, graph)

# Save to file
graph.serialize(destination="entities.ttl", format="turtle")
print("✓ Exported to entities.ttl")
```

## Working with OpenBIS

### How to Connect to OpenBIS

```python
from bam_masterdata.openbis.login import ologin

# Connect to OpenBIS instance
openbis = ologin(
    url="https://your-openbis-instance.com",
    username="your_username",
    password="your_password"
)

print(f"✓ Connected to OpenBIS: {openbis.get_server_information()}")
```

### How to Retrieve Entities from OpenBIS

```python
from bam_masterdata.openbis.get_entities import OpenbisEntities

# Initialize entities extractor
entities_extractor = OpenbisEntities(openbis)

# Get all object types
object_types = entities_extractor.get_object_dict()
print(f"Retrieved {len(object_types)} object types from OpenBIS")

# Get specific vocabulary
vocabularies = entities_extractor.get_vocabulary_dict()
storage_formats = vocabularies.get("STORAGE_FORMAT", {})
print(f"Storage format terms: {list(storage_formats.get('terms', {}).keys())}")
```

### How to Push Data to OpenBIS

*[Image placeholder: Screenshot of OpenBIS interface showing uploaded masterdata with entity browser and property views.]*

```python
# Create entities in OpenBIS
for obj_code, obj_data in object_types.items():
    obj_type = ObjectType.from_dict(obj_data)
    openbis_obj = obj_type.to_openbis()

    # Register with OpenBIS
    result = openbis.create_object_type(openbis_obj)
    print(f"✓ Created object type: {obj_code}")
```

## Command Line Operations

### How to Use the CLI for Bulk Operations

```bash
# Export all masterdata to Excel
bam-masterdata export-to-excel masterdata_export.xlsx

# Export specific entity types to JSON
bam-masterdata export-to-json --entity-types object_types dataset_types output.json

# Run consistency checker
bam-masterdata checker --verbose

# Fill masterdata from OpenBIS
bam-masterdata fill-masterdata --url https://openbis.example.com --username user
```

### How to Generate Code from Masterdata

```python
from bam_masterdata.cli.fill_masterdata import MasterdataCodeGenerator

# Initialize code generator with entities data
generator = MasterdataCodeGenerator(
    objects=object_types,
    datasets=dataset_types,
    collections=collection_types,
    vocabularies=vocabulary_types
)

# Generate Python code for dataset types
dataset_code = generator.generate_dataset_types()

# Save to file
with open("generated_dataset_types.py", "w") as f:
    f.write(dataset_code)

print("✓ Generated dataset types code")
```

## Advanced Usage

### How to Create Custom Validators

```python
from bam_masterdata.checker.masterdata_validator import MasterdataValidator

class CustomValidator(MasterdataValidator):
    def validate_custom_rules(self, entities_dict):
        """Add custom validation rules."""
        errors = []

        # Example: Check that all samples have required properties
        for obj_code, obj_data in entities_dict.get("object_types", {}).items():
            if obj_data.get("code", "").startswith("SAMPLE_"):
                required_props = ["material_type", "dimensions"]
                for prop in required_props:
                    if prop not in obj_data.get("properties", {}):
                        errors.append(f"Sample {obj_code} missing required property: {prop}")

        return errors

# Use custom validator
validator = CustomValidator()
custom_errors = validator.validate_custom_rules(entities_dict)
```

### How to Handle Large Datasets

```python
import multiprocessing
from concurrent.futures import ProcessPoolExecutor

def process_entity_batch(entities_batch):
    """Process a batch of entities."""
    results = []
    for entity_data in entities_batch:
        # Process individual entity
        entity = ObjectType.from_dict(entity_data)
        results.append(entity.to_dict())
    return results

# Process entities in parallel
entities_list = list(object_types.values())
batch_size = 100
batches = [entities_list[i:i+batch_size] for i in range(0, len(entities_list), batch_size)]

with ProcessPoolExecutor() as executor:
    results = list(executor.map(process_entity_batch, batches))

print(f"✓ Processed {len(entities_list)} entities in {len(batches)} batches")
```

### How to Extend Entity Relationships

```python
# Add relationships between entities
sample = Sample(code="SAMPLE_001")
instrument = Instrument(code="INSTR_001")

# Create relationship
sample.add_relationship("measured_with", instrument)

# Access relationships
relationships = sample.get_relationships()
print(f"Sample relationships: {relationships}")
```

## Troubleshooting Common Issues

### Memory Issues with Large Files

```python
# Use streaming for large Excel files
import pandas as pd

# Read Excel in chunks
chunk_size = 1000
for chunk in pd.read_excel("large_file.xlsx", chunksize=chunk_size):
    # Process chunk
    entities_batch = extractor.process_chunk(chunk)
    # Save incrementally
```

### Performance Optimization

```python
# Use caching for repeated operations
from functools import lru_cache

@lru_cache(maxsize=128)
def get_cached_entity(entity_code):
    return entity_registry.get(entity_code)

# Batch operations instead of individual calls
entities_to_create = []
for entity_data in batch_data:
    entities_to_create.append(ObjectType.from_dict(entity_data))

# Create all at once
result = openbis.create_objects(entities_to_create)
```