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