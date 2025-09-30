# API Reference

This section provides comprehensive API documentation for all modules, classes, and functions in the BAM Masterdata package.

## Core Modules

### Metadata Framework

#### Entity Classes

::: bam_masterdata.metadata.entities
    options:
      show_root_heading: true
      show_source: false
      members:
        - BaseEntity
        - ObjectType
        - CollectionType
        - DatasetType
        - VocabularyType

#### Definition Classes

::: bam_masterdata.metadata.definitions
    options:
      show_root_heading: true
      show_source: false
      members:
        - EntityDef
        - ObjectTypeDef
        - CollectionTypeDef
        - DatasetTypeDef
        - VocabularyTypeDef
        - PropertyTypeDef
        - PropertyTypeAssignment
        - VocabularyTerm

#### Entity Dictionary

::: bam_masterdata.metadata.entities_dict
    options:
      show_root_heading: true
      show_source: false

### Command Line Interface

#### Main CLI

::: bam_masterdata.cli.cli
    options:
      show_root_heading: true
      show_source: false

#### Code Generation

::: bam_masterdata.cli.fill_masterdata
    options:
      show_root_heading: true
      show_source: false
      members:
        - MasterdataCodeGenerator

#### Data Import/Export

::: bam_masterdata.cli.excel_to_entities
    options:
      show_root_heading: true
      show_source: false
      members:
        - MasterdataExcelExtractor

::: bam_masterdata.cli.entities_to_excel
    options:
      show_root_heading: true
      show_source: false

::: bam_masterdata.cli.entities_to_rdf
    options:
      show_root_heading: true
      show_source: false

### Excel Integration

::: bam_masterdata.excel.excel_to_entities
    options:
      show_root_heading: true
      show_source: false
      members:
        - MasterdataExcelExtractor

### openBIS Integration

#### Authentication

::: bam_masterdata.openbis.login
    options:
      show_root_heading: true
      show_source: false

#### Entity Retrieval

::: bam_masterdata.openbis.get_entities
    options:
      show_root_heading: true
      show_source: false
      members:
        - OpenbisEntities

### Validation and Checking

#### Masterdata Checker

::: bam_masterdata.checker.checker
    options:
      show_root_heading: true
      show_source: false
      members:
        - MasterdataChecker

#### Validator

::: bam_masterdata.checker.masterdata_validator
    options:
      show_root_heading: true
      show_source: false
      members:
        - MasterdataValidator

#### Source Loader

::: bam_masterdata.checker.source_loader
    options:
      show_root_heading: true
      show_source: false
      members:
        - SourceLoader

### Parsing Framework

::: bam_masterdata.parsing.parsing
    options:
      show_root_heading: true
      show_source: false
      members:
        - AbstractParser

### Utilities

::: bam_masterdata.utils.utils
    options:
      show_root_heading: true
      show_source: false

::: bam_masterdata.utils.paths
    options:
      show_root_heading: true
      show_source: false

### Logging

::: bam_masterdata.logger
    options:
      show_root_heading: true
      show_source: false

## Data Model Classes

### Object Types

All object type classes from the datamodel:

::: bam_masterdata.datamodel.object_types
    options:
      show_root_heading: true
      show_source: false
      group_by_category: true
      filters:
        - "!^_"

### Dataset Types

All dataset type classes from the datamodel:

::: bam_masterdata.datamodel.dataset_types
    options:
      show_root_heading: true
      show_source: false
      group_by_category: true
      filters:
        - "!^_"

### Collection Types

All collection type classes from the datamodel:

::: bam_masterdata.datamodel.collection_types
    options:
      show_root_heading: true
      show_source: false
      group_by_category: true
      filters:
        - "!^_"

### Vocabulary Types

All vocabulary type classes from the datamodel:

::: bam_masterdata.datamodel.vocabulary_types
    options:
      show_root_heading: true
      show_source: false
      group_by_category: true
      filters:
        - "!^_"

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

## Error Handling

The package defines several exception types for different error conditions:

```python
from bam_masterdata.exceptions import (
    ValidationError,
    EntityNotFoundError,
    DuplicateEntityError,
    ConfigurationError
)

try:
    # Perform operations
    result = some_operation()
except ValidationError as e:
    print(f"Validation failed: {e}")
except EntityNotFoundError as e:
    print(f"Entity not found: {e}")
except DuplicateEntityError as e:
    print(f"Duplicate entity: {e}")
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

## Advanced Usage

### Custom Entity Types

You can create custom entity types by extending the base classes:

```python
from bam_masterdata.metadata.entities import ObjectType
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment

class CustomSample(ObjectType):
    defs = ObjectTypeDef(
        code="CUSTOM_SAMPLE",
        description="Custom sample type with specific properties"
    )
    
    custom_property = PropertyTypeAssignment(
        code="CUSTOM_PROP",
        data_type="VARCHAR",
        property_label="Custom Property",
        description="A custom property for this sample type",
        mandatory=True
    )
```

### Custom Validators

```python
from bam_masterdata.checker.masterdata_validator import MasterdataValidator

class CustomValidator(MasterdataValidator):
    def validate_custom_rules(self, entities_dict):
        """Implement custom validation rules."""
        errors = []
        
        # Custom validation logic here
        for entity_type, entities in entities_dict.items():
            for entity_id, entity_data in entities.items():
                # Validate specific conditions
                if not self.check_custom_condition(entity_data):
                    errors.append(f"Custom validation failed for {entity_id}")
        
        return errors
    
    def check_custom_condition(self, entity_data):
        """Check a custom condition."""
        # Implement your custom logic
        return True
```

### Batch Operations

```python
from bam_masterdata.utils.batch import BatchProcessor

# Process entities in batches
processor = BatchProcessor(batch_size=100)

entities_to_process = list(object_types.values())
results = processor.process_batches(entities_to_process, processing_function)

# Handle results
for result in results:
    if result.success:
        print(f"Processed {result.entity_count} entities")
    else:
        print(f"Batch failed: {result.error}")
```

This API reference provides comprehensive documentation for all public classes and functions in the BAM Masterdata package. For more detailed examples and usage patterns, see the How-to Guides and Tutorial sections.