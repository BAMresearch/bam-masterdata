
# Collection Types Reference

This section provides comprehensive documentation for all collection types available in the BAM Masterdata system. Collection types define how samples and datasets are organized into logical groups that represent experiments, projects, or other research activities.

## Overview

Collection types (also known as experiment types in openBIS) represent containers that group related samples and datasets. They provide structure for organizing research activities and enable tracking of relationships between different research objects.

*[Image placeholder: Collection hierarchy diagram showing how collections contain samples and datasets, with relationships between different collection types.]*

## Base Collection Type

::: bam_masterdata.metadata.entities.CollectionType
    options:
      show_root_heading: true
      show_source: false
      members:
        - defs
        - to_dict
        - to_json
        - to_openbis
        - add
        - remove
        - add_relationship
        - remove_relationship
        - get_type
        - create_type

## Collection Type Definitions

::: bam_masterdata.metadata.definitions.CollectionTypeDef
    options:
      show_root_heading: true
      show_source: false

## Available Collection Types

### Default Collection

::: bam_masterdata.datamodel.collection_types.Collection
    options:
      show_root_heading: true
      show_source: false

The base collection type that provides fundamental properties and structure for all collections.

**Core Properties:**
- Name and description
- Start and end dates
- Status tracking
- Participant information

### Default Experiment

::: bam_masterdata.datamodel.collection_types.DefaultExperiment
    options:
      show_root_heading: true
      show_source: false

Standard experimental collection for general research activities.

**Key Features:**
- Experimental design documentation
- Protocol references
- Participant tracking
- Equipment usage records

### Measurements Collection

::: bam_masterdata.datamodel.collection_types.MeasurementsCollection
    options:
      show_root_heading: true
      show_source: false

Specialized collection for measurement campaigns and data acquisition activities.

**Measurement-Specific Properties:**
- Measurement conditions
- Instrument configuration
- Data acquisition parameters
- Quality control information

*[Image placeholder: Measurement workflow diagram showing how samples flow through measurement collections with associated instruments and resulting datasets.]*

## Collection Structure and Relationships

### Hierarchical Organization

Collections exist within a hierarchical structure:

```
Space (Research Group)
├── Project (Research Initiative)
    ├── Collection (Experiment/Study)
        ├── Samples (Research Objects)
        └── Datasets (Data Files)
```

### Relationship Types

Collections can have various relationships:

**Contains Relationships:**
- Collections → Samples
- Collections → Datasets
- Collections → Sub-collections

**Association Relationships:**
- Collection ↔ Instruments (used in)
- Collection ↔ Protocols (follows)
- Collection ↔ Personnel (conducted by)

*[Image placeholder: Network diagram showing the various relationship types between collections and other entities in the system.]*

## Usage Examples

### Creating Collection Instances

```python
from bam_masterdata.datamodel.collection_types import MeasurementsCollection
from datetime import date

# Create a measurements collection
measurement_campaign = MeasurementsCollection(
    code="MEAS_CAMPAIGN_2024_001",
    name="Steel Fatigue Testing Campaign 2024",
    description="Comprehensive fatigue testing of various steel alloys"
)

# Set collection properties
measurement_campaign.set_property("start_date", date(2024, 1, 15))
measurement_campaign.set_property("end_date", date(2024, 6, 30))
measurement_campaign.set_property("principal_investigator", "Dr. Jane Smith")
measurement_campaign.set_property("measurement_type", "Fatigue Testing")
```

### Adding Samples to Collections

```python
from bam_masterdata.datamodel.object_types import Sample

# Create samples
steel_sample_1 = Sample(code="STEEL_001", name="High Carbon Steel Specimen")
steel_sample_2 = Sample(code="STEEL_002", name="Low Carbon Steel Specimen")

# Add samples to collection
measurement_campaign.add(steel_sample_1)
measurement_campaign.add(steel_sample_2)

# Verify samples are in collection
samples_in_collection = measurement_campaign.get_samples()
print(f"Collection contains {len(samples_in_collection)} samples")
```

### Managing Collection Relationships

```python
# Create relationships with instruments
from bam_masterdata.datamodel.object_types import Instrument

fatigue_tester = Instrument(code="FATIGUE_001", name="Universal Testing Machine")

# Add relationship
measurement_campaign.add_relationship("uses_instrument", fatigue_tester)

# Access relationships
instruments = measurement_campaign.get_relationships("uses_instrument")
print(f"Collection uses {len(instruments)} instruments")
```

### Working with Datasets in Collections

```python
from bam_masterdata.datamodel.dataset_types import RawData, AnalyzedData

# Create datasets
raw_data = RawData(
    code="FATIGUE_RAW_001",
    name="Raw fatigue test data for STEEL_001"
)

analyzed_data = AnalyzedData(
    code="FATIGUE_ANALYSIS_001", 
    name="Fatigue analysis results for STEEL_001"
)

# Associate datasets with collection
raw_data.set_collection(measurement_campaign)
analyzed_data.set_collection(measurement_campaign)

# Link datasets to specific samples
raw_data.add_relationship("measured_sample", steel_sample_1)
analyzed_data.add_relationship("analyzed_sample", steel_sample_1)
```

## Collection Lifecycle Management

### Planning Phase

```python
# Create collection with planning information
collection = MeasurementsCollection(
    code="FUTURE_STUDY_001",
    name="Planned Corrosion Study",
    status="PLANNED"
)

collection.set_property("planned_start", date(2024, 9, 1))
collection.set_property("estimated_duration_months", 12)
collection.set_property("required_samples", 50)
collection.set_property("budget_allocated", 25000.00)
```

### Execution Phase

```python
# Update collection status and add actual data
collection.set_property("status", "ACTIVE")
collection.set_property("actual_start", date(2024, 9, 15))

# Add samples as they are created
for i in range(10):
    sample = Sample(code=f"CORR_SAMPLE_{i:03d}")
    collection.add(sample)

# Track progress
collection.set_property("completion_percentage", 25.0)
```

### Completion Phase

```python
# Finalize collection
collection.set_property("status", "COMPLETED")
collection.set_property("actual_end", date(2025, 2, 28))
collection.set_property("final_sample_count", 48)
collection.set_property("completion_percentage", 100.0)

# Add final reports
final_report = Document(
    code="CORR_FINAL_REPORT",
    name="Final Corrosion Study Report"
)
collection.add(final_report)
```

## Advanced Collection Operations

### Collection Templates

```python
def create_standard_measurement_collection(
    code: str,
    name: str,
    measurement_type: str,
    investigator: str
) -> MeasurementsCollection:
    """Create a standardized measurement collection."""
    
    collection = MeasurementsCollection(code=code, name=name)
    
    # Set standard properties
    collection.set_property("measurement_type", measurement_type)
    collection.set_property("principal_investigator", investigator)
    collection.set_property("status", "PLANNED")
    collection.set_property("data_classification", "INTERNAL")
    
    # Add standard protocols
    standard_protocols = get_standard_protocols(measurement_type)
    for protocol in standard_protocols:
        collection.add_relationship("follows_protocol", protocol)
    
    return collection
```

### Batch Collection Operations

```python
def create_parallel_collections(
    base_name: str,
    conditions: list,
    template_collection: MeasurementsCollection
) -> list:
    """Create multiple collections with different conditions."""
    
    collections = []
    
    for i, condition in enumerate(conditions):
        # Clone template
        new_collection = template_collection.copy()
        new_collection.code = f"{base_name}_{condition}_{i:02d}"
        new_collection.name = f"{base_name} - {condition}"
        
        # Set condition-specific properties
        new_collection.set_property("test_condition", condition)
        
        collections.append(new_collection)
    
    return collections
```

### Collection Analytics

```python
def analyze_collection_progress(collection: MeasurementsCollection) -> dict:
    """Analyze the progress and status of a collection."""
    
    samples = collection.get_samples()
    datasets = collection.get_datasets()
    
    # Calculate statistics
    total_samples = len(samples)
    samples_with_data = len([s for s in samples if s.has_datasets()])
    completion_rate = (samples_with_data / total_samples) * 100 if total_samples > 0 else 0
    
    # Analyze dataset types
    dataset_types = {}
    for dataset in datasets:
        dtype = dataset.get_type()
        dataset_types[dtype] = dataset_types.get(dtype, 0) + 1
    
    return {
        "total_samples": total_samples,
        "samples_with_data": samples_with_data,
        "completion_rate": completion_rate,
        "dataset_types": dataset_types,
        "total_datasets": len(datasets)
    }
```

## Integration with openBIS

### Creating Collections in openBIS

```python
from bam_masterdata.openbis.login import ologin

# Connect to openBIS
openbis = ologin(url="https://openbis.bam.de", username="researcher")

# Convert BAM collection to openBIS format
openbis_collection = measurement_campaign.to_openbis()

# Create in openBIS
result = openbis.create_experiment(openbis_collection)
print(f"Created collection with ID: {result.identifier}")
```

### Synchronizing Collection Data

```python
def sync_collection_with_openbis(
    collection: MeasurementsCollection,
    openbis_connection
) -> bool:
    """Synchronize collection data with openBIS."""
    
    try:
        # Update collection metadata
        openbis_exp = openbis_connection.get_experiment(collection.code)
        
        for prop_name, prop_value in collection.properties.items():
            setattr(openbis_exp, prop_name, prop_value)
        
        openbis_exp.save()
        
        # Sync related samples
        for sample in collection.get_samples():
            sync_sample_with_openbis(sample, openbis_connection)
        
        return True
        
    except Exception as e:
        print(f"Synchronization failed: {e}")
        return False
```

## Collection Validation and Quality Control

### Validation Rules

```python
from bam_masterdata.checker.masterdata_validator import MasterdataValidator

def validate_collection_completeness(collection: MeasurementsCollection) -> list:
    """Validate that a collection has all required components."""
    
    errors = []
    
    # Check required properties
    required_props = ["principal_investigator", "start_date", "measurement_type"]
    for prop in required_props:
        if not collection.get_property(prop):
            errors.append(f"Missing required property: {prop}")
    
    # Check sample requirements
    samples = collection.get_samples()
    if len(samples) == 0:
        errors.append("Collection must contain at least one sample")
    
    # Check dataset associations
    for sample in samples:
        if not sample.has_datasets():
            errors.append(f"Sample {sample.code} has no associated datasets")
    
    return errors
```

### Quality Metrics

```python
def calculate_collection_quality_score(collection: MeasurementsCollection) -> float:
    """Calculate a quality score for the collection."""
    
    score = 0.0
    max_score = 100.0
    
    # Completeness (40 points)
    required_props = ["principal_investigator", "start_date", "description"]
    filled_props = sum(1 for prop in required_props if collection.get_property(prop))
    score += (filled_props / len(required_props)) * 40
    
    # Data richness (30 points)
    samples = collection.get_samples()
    if samples:
        samples_with_data = sum(1 for s in samples if s.has_datasets())
        score += (samples_with_data / len(samples)) * 30
    
    # Documentation (20 points)
    has_protocol = bool(collection.get_relationships("follows_protocol"))
    has_description = bool(collection.get_property("description"))
    score += (has_protocol + has_description) * 10
    
    # Metadata quality (10 points)
    metadata_fields = ["status", "measurement_type", "data_classification"]
    filled_metadata = sum(1 for field in metadata_fields if collection.get_property(field))
    score += (filled_metadata / len(metadata_fields)) * 10
    
    return min(score, max_score)
```

*[Image placeholder: Quality dashboard showing collection completeness, data coverage, and quality metrics with progress bars and status indicators.]*

## Best Practices

### Collection Design
- Use descriptive, systematic naming conventions
- Define clear scope and objectives
- Plan sample and dataset organization upfront
- Include sufficient metadata for future understanding

### Data Organization
- Group related samples logically
- Maintain consistent property usage
- Document experimental conditions thoroughly
- Link related collections appropriately

### Lifecycle Management
- Update status regularly during execution
- Track progress against planned milestones
- Document deviations from original plan
- Archive completed collections systematically

### Collaboration
- Define clear roles and responsibilities
- Share access appropriately
- Maintain communication logs
- Document decision rationale

## Complete Collection Type List

All available collection types in the BAM Masterdata system:

::: bam_masterdata.datamodel.collection_types
    options:
      show_root_heading: false
      show_source: false
      filters:
        - "!^_"