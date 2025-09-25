
# Understanding openBIS

openBIS is the foundational platform that powers the metadata management layer of the BAM Data Store. This section explains what openBIS is, how it works, and how the `bam-masterdata` package integrates with it.

## What is openBIS?

[openBIS](https://openbis.ch/) is an open-source framework for building scientific data management systems. It was originally developed at ETH Zurich for managing biological and biochemical research data but has evolved into a general-purpose platform for scientific data management.

*[Image placeholder: openBIS logo and overview diagram showing its role as a data management platform with connections to various data sources and user interfaces.]*

## Core Concepts in openBIS

### Spaces, Projects, and Experiments

openBIS organizes data in a hierarchical structure:

- **Spaces**: Top-level organizational units (e.g., research groups, departments)
- **Projects**: Major research initiatives within a space
- **Experiments**: Specific research activities within a project

*[Image placeholder: Hierarchical tree diagram showing Spaces → Projects → Experiments → Objects/Datasets structure with real examples from BAM research.]*

### Entities

openBIS manages several types of entities:

#### Samples (Objects)
Physical or conceptual objects being studied:
- Material samples (steel specimens, chemical compounds)
- Biological samples (cell cultures, tissue samples)
- Abstract concepts (protocols, procedures)

#### Datasets
Data files and their associated metadata:
- Raw measurement data
- Processed analysis results
- Documentation and reports
- Images and visualizations

#### Collections (Experiments)
Logical groupings of related samples and datasets:
- Measurement campaigns
- Experimental series
- Data analysis workflows

### Properties and Vocabularies

Every entity type can have **properties** that store specific information:
- **Free text**: Descriptions, notes, comments
- **Numbers**: Measurements, quantities, calculations
- **Dates**: Creation times, measurement dates, deadlines
- **Controlled vocabularies**: Standardized terms and categories

*[Image placeholder: Screenshot of openBIS property editor showing different property types and how they appear in the user interface.]*

## How BAM Masterdata Integrates with openBIS

### Schema Definition

The `bam-masterdata` package defines the structure that openBIS uses:

```python
# BAM Masterdata defines entity types
class Sample(ObjectType):
    defs = ObjectTypeDef(
        code="SAMPLE",
        description="A physical specimen for testing"
    )
    
    material_type = PropertyTypeAssignment(
        code="MATERIAL_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        property_label="Material Type",
        vocabulary="MATERIAL_TYPES"
    )

# This becomes an openBIS object type with properties
```

### Data Flow

1. **Schema Definition**: BAM Masterdata classes define structure
2. **Code Generation**: Python code generates openBIS configurations
3. **Deployment**: Configurations are uploaded to openBIS
4. **Data Entry**: Users create entities following the defined structure
5. **Validation**: openBIS enforces the rules defined in masterdata

*[Image placeholder: Data flow diagram showing the progression from BAM Masterdata Python classes through code generation to openBIS configuration and finally to data entry.]*

### API Integration

The package provides tools to interact with openBIS:

```python
from bam_masterdata.openbis.login import ologin
from bam_masterdata.openbis.get_entities import OpenbisEntities

# Connect to openBIS
openbis = ologin(url="https://openbis.bam.de", username="user", password="pass")

# Retrieve existing entities
entities = OpenbisEntities(openbis)
object_types = entities.get_object_dict()

# Create new entities
sample = Sample(code="SAMPLE_001", name="Test Sample")
openbis_sample = sample.to_openbis()
result = openbis.create_sample(openbis_sample)
```

## openBIS Architecture

### Client-Server Model

openBIS follows a client-server architecture:

- **Server**: Central database and business logic
- **Web Client**: Browser-based user interface
- **API**: Programmatic access for automation and integration
- **Desktop Tools**: Specialized applications for specific workflows

*[Image placeholder: Architecture diagram showing openBIS server in the center with various client types connecting to it (web browsers, API clients, desktop applications).]*

### Data Storage

openBIS separates metadata from data files:

- **Metadata**: Stored in relational database (PostgreSQL)
- **Data Files**: Stored on file systems with configurable storage
- **Indexing**: Search indices for fast metadata queries
- **Backup**: Separate strategies for metadata and data files

### Security Model

openBIS provides comprehensive access control:

- **Authentication**: User identity verification
- **Authorization**: Permission-based access to specific data
- **Audit Trail**: Complete logging of all data access and modifications
- **Data Privacy**: Support for sensitive and confidential data

## Benefits of Using openBIS

### For Data Management

**Structured Organization**: Hierarchical data organization with flexible relationships
**Metadata Standards**: Consistent property definitions across all data
**Version Control**: Track changes to data and metadata over time
**Search Capabilities**: Powerful queries across all metadata fields

### For Research Workflows

**Integration**: Connect with laboratory instruments and analysis software
**Automation**: Batch operations and workflow automation
**Collaboration**: Shared access with granular permissions
**Reproducibility**: Complete documentation of experimental conditions

### For Institutional Compliance

**Audit Trails**: Complete history of data access and modifications
**Data Integrity**: Validation rules and consistency checks
**Long-term Preservation**: Sustainable data storage and format migration
**Standards Compliance**: Support for research data management standards

*[Image placeholder: Benefits overview diagram with icons representing each benefit category and connecting lines showing relationships.]*

## openBIS vs. Other Data Management Systems

### Compared to File Systems
- **Structure**: Explicit relationships vs. folder hierarchies
- **Metadata**: Rich, searchable properties vs. filename conventions
- **Access Control**: Fine-grained permissions vs. file system permissions
- **Search**: Metadata-based queries vs. filename search

### Compared to Databases
- **Flexibility**: Schema evolution vs. fixed table structures
- **File Handling**: Native large file support vs. blob storage
- **User Interface**: Scientific workflows vs. database forms
- **Integration**: Laboratory instrument support vs. general applications

### Compared to Cloud Storage
- **Metadata**: Structured properties vs. basic file attributes
- **Relationships**: Explicit connections vs. folder organization
- **Validation**: Business rules vs. basic file operations
- **Scientific Features**: Research-specific functionality vs. general storage

## Working with openBIS Through BAM Masterdata

### Creating Entities

```python
# Define entity structure in Python
sample = Sample(
    code="BAM_SAMPLE_001",
    name="Steel Tensile Test Specimen",
    properties={
        "material_type": "Steel",
        "dimensions": "10x10x50 mm",
        "heat_treatment": "Normalized"
    }
)

# Convert to openBIS format and create
openbis_sample = sample.to_openbis()
result = openbis.create_sample(openbis_sample)
```

### Querying Data

```python
# Search for samples with specific properties
search_criteria = {
    "material_type": "Steel",
    "test_date": {"from": "2024-01-01", "to": "2024-12-31"}
}

samples = openbis.search_samples(search_criteria)
for sample in samples:
    print(f"Found sample: {sample.code} - {sample.properties}")
```

### Managing Relationships

```python
# Create relationships between entities
sample = openbis.get_sample("SAMPLE_001")
dataset = openbis.get_dataset("DATA_001")
instrument = openbis.get_sample("INSTRUMENT_001")

# Link dataset to sample and instrument
dataset.add_parent(sample)
dataset.set_property("measured_with", instrument.code)
openbis.update_dataset(dataset)
```

## Best Practices for openBIS Usage

### Entity Design
- **Consistent Naming**: Use standardized code formats
- **Rich Metadata**: Include comprehensive property definitions
- **Clear Relationships**: Explicitly define connections between entities
- **Validation Rules**: Implement quality checks for data entry

### Performance Optimization
- **Batch Operations**: Group related operations together
- **Efficient Queries**: Use indexed properties for search
- **Caching**: Store frequently accessed data locally
- **Connection Management**: Reuse openBIS connections

### Data Organization
- **Logical Hierarchies**: Structure spaces and projects meaningfully
- **Consistent Properties**: Use standardized vocabularies
- **Regular Cleanup**: Archive or delete obsolete data
- **Documentation**: Maintain clear descriptions and help text

*[Image placeholder: Best practices infographic showing the key recommendations organized in categories with checkmarks and visual icons.]*

## Common openBIS Operations

### Administrative Tasks
- Setting up new entity types
- Managing user permissions
- Configuring data storage locations
- Maintaining controlled vocabularies

### Research Activities
- Creating samples and experiments
- Uploading and linking datasets
- Searching for relevant data
- Generating reports and exports

### Integration Tasks
- Connecting laboratory instruments
- Importing data from external systems
- Exporting data to analysis tools
- Synchronizing with other databases

## Troubleshooting openBIS Issues

### Connection Problems
- Verify server URL and credentials
- Check network connectivity
- Confirm SSL/TLS configuration
- Review firewall settings

### Performance Issues
- Monitor database performance
- Check available disk space
- Review query complexity
- Optimize property indices

### Data Integrity
- Validate entity relationships
- Check property value consistency
- Verify controlled vocabulary terms
- Monitor audit logs for anomalies

openBIS provides a robust foundation for scientific data management, and the BAM Masterdata package makes it accessible to researchers through familiar Python interfaces. This combination enables sophisticated data organization while maintaining the flexibility needed for diverse research activities.