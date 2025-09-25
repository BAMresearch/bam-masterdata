
# Dataset Types Reference

This section provides comprehensive documentation for all dataset types available in the BAM Masterdata system. Dataset types define the structure and properties of data files and their associated metadata.

## Overview

Dataset types in BAM Masterdata represent different categories of research data files. Each type has specific properties that capture relevant metadata for that category of data.

*[Image placeholder: Dataset type hierarchy diagram showing the main categories (Raw Data, Processed Data, Analysis Results, etc.) and their relationships.]*

## Base Dataset Type

::: bam_masterdata.metadata.entities.DatasetType
    options:
      show_root_heading: true
      show_source: false
      members:
        - defs
        - to_dict
        - to_json
        - to_openbis
        - get_type
        - create_type

## Dataset Type Definitions

::: bam_masterdata.metadata.definitions.DatasetTypeDef
    options:
      show_root_heading: true
      show_source: false

## Available Dataset Types

### Raw Data

::: bam_masterdata.datamodel.dataset_types.RawData
    options:
      show_root_heading: true
      show_source: false

Raw data represents unprocessed data directly from instruments or experiments.

**Common Properties:**
- Name and description
- File format information
- Acquisition parameters
- Quality indicators

### Processed Data

::: bam_masterdata.datamodel.dataset_types.ProcessedData
    options:
      show_root_heading: true
      show_source: false

Processed data includes data that has undergone initial processing, cleaning, or calibration.

### Analyzed Data

::: bam_masterdata.datamodel.dataset_types.AnalyzedData
    options:
      show_root_heading: true
      show_source: false

Analyzed data represents the results of computational analysis or statistical processing.

### Documents

::: bam_masterdata.datamodel.dataset_types.Document
    options:
      show_root_heading: true
      show_source: false

Document datasets include reports, protocols, specifications, and other textual materials.

**Key Properties:**
- Author information
- Version tracking
- Document type classification
- Language specification

### Figures and Visualizations

::: bam_masterdata.datamodel.dataset_types.Figure
    options:
      show_root_heading: true
      show_source: false

Base class for all figure types including plots, schematics, and other visual representations.

**Technical Properties:**
- Image resolution (horizontal/vertical)
- DPI (dots per inch)
- File format
- Color depth
- Compression settings

#### Plots

::: bam_masterdata.datamodel.dataset_types.Plot
    options:
      show_root_heading: true
      show_source: false

Scientific plots and charts with axis information and legends.

#### Schematics

::: bam_masterdata.datamodel.dataset_types.Schematic
    options:
      show_root_heading: true
      show_source: false

Technical drawings, diagrams, and schematic representations.

#### Simulation Visualizations

::: bam_masterdata.datamodel.dataset_types.SimVis
    options:
      show_root_heading: true
      show_source: false

Visualizations from computational simulations and modeling.

### Computational Data

#### Material Models

::: bam_masterdata.datamodel.dataset_types.MatModel
    options:
      show_root_heading: true
      show_source: false

Computational models of materials including structure files and parameter sets.

#### Pseudopotentials

::: bam_masterdata.datamodel.dataset_types.Pseudopot
    options:
      show_root_heading: true
      show_source: false

Pseudopotential files used in electronic structure calculations.

#### Interaction Potentials

::: bam_masterdata.datamodel.dataset_types.IntPot
    options:
      show_root_heading: true
      show_source: false

Interatomic potential models for molecular dynamics simulations.

### Code and Workflows

#### Source Code

::: bam_masterdata.datamodel.dataset_types.SourceCode
    options:
      show_root_heading: true
      show_source: false

Source code files including scripts, programs, and libraries.

#### Analysis Notebooks

::: bam_masterdata.datamodel.dataset_types.AnalysisNotebook
    options:
      show_root_heading: true
      show_source: false

Jupyter notebooks and other interactive analysis documents.

#### Computational Environments

::: bam_masterdata.datamodel.dataset_types.CompEnv
    options:
      show_root_heading: true
      show_source: false

Computational environment specifications including dependencies and configurations.

### Specialized Data Types

#### Test Files

::: bam_masterdata.datamodel.dataset_types.TestFile
    options:
      show_root_heading: true
      show_source: false

Files used for testing and validation purposes.

#### Log Files

::: bam_masterdata.datamodel.dataset_types.LogFile
    options:
      show_root_heading: true
      show_source: false

System logs, instrument logs, and process monitoring data.

#### ELN Previews

::: bam_masterdata.datamodel.dataset_types.ElnPreview
    options:
      show_root_heading: true
      show_source: false

Preview images and summaries for Electronic Lab Notebook entries.

## Property Type Assignments

Dataset properties are defined using property type assignments:

::: bam_masterdata.metadata.definitions.PropertyTypeAssignment
    options:
      show_root_heading: true
      show_source: false

## Usage Examples

### Creating Dataset Instances

```python
from bam_masterdata.datamodel.dataset_types import RawData, Plot

# Create a raw data instance
raw_data = RawData(
    code="RAW_001",
    name="Temperature Measurement Data"
)

# Create a plot instance  
plot = Plot(
    code="PLOT_001",
    name="Temperature vs Time Plot"
)

# Set properties
plot.set_property("plot_type", "Line Plot")
plot.set_property("x_axis_label", "Time (s)")
plot.set_property("y_axis_label", "Temperature (°C)")
```

### Converting to Different Formats

```python
# Convert to dictionary
data_dict = raw_data.to_dict()

# Convert to JSON
data_json = raw_data.to_json()

# Convert to openBIS format
openbis_data = raw_data.to_openbis()
```

### Working with Properties

```python
# Get all properties
properties = raw_data.get_property_metadata()

# Check if a property is mandatory
file_format_prop = properties.get("FILE_FORMAT")
if file_format_prop and file_format_prop.mandatory:
    print("File format is required")

# Access property definitions
print(f"Property label: {file_format_prop.property_label}")
print(f"Data type: {file_format_prop.data_type}")
print(f"Description: {file_format_prop.description}")
```

## Data Validation

Dataset types include built-in validation:

```python
from bam_masterdata.checker.masterdata_validator import MasterdataValidator

# Validate dataset data
validator = MasterdataValidator()
dataset_dict = {"dataset_types": {"RAW_001": raw_data.to_dict()}}

result = validator.validate(dataset_dict)
if not result.is_valid:
    for error in result.errors:
        print(f"Validation error: {error}")
```

*[Image placeholder: Validation workflow diagram showing the steps from dataset creation through validation to final storage in openBIS.]*

## Best Practices

### Naming Conventions
- Use descriptive, consistent naming schemes
- Include version information when appropriate
- Follow institutional naming standards

### Property Usage
- Fill all mandatory properties
- Use controlled vocabularies when available
- Provide clear, descriptive values

### File Organization
- Group related files in logical collections
- Use meaningful file names
- Include appropriate metadata files

### Version Management
- Track dataset versions systematically
- Document changes between versions
- Maintain backward compatibility when possible

## Complete Dataset Type List

All available dataset types in the BAM Masterdata system:

::: bam_masterdata.datamodel.dataset_types
    options:
      show_root_heading: false
      show_source: false
      filters:
        - "!^_"
      group_by_category: true