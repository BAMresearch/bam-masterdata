# Getting Started with BAM Masterdata

This tutorial will guide you through your first interaction with the `bam-masterdata` package, helping you understand its core concepts and basic functionality.

## What is BAM Masterdata?

The `bam-masterdata` package defines and handles the masterdata schemas used in the BAM Data Store project. It provides Python classes and utilities for working with different types of entities in the research data management system.

*[Image placeholder: Architecture overview diagram showing the relationship between BAM Masterdata, openBIS, and the BAM Data Store. The diagram should illustrate data flow and the role of masterdata schemas in the system.]*

## Installation and Setup

### Prerequisites

- Python 3.9 or higher (up to 3.12)
- Virtual environment (recommended)

### Step 1: Create a Virtual Environment

We strongly recommend using a virtual environment to avoid conflicts with other packages.

**Using venv:**
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

**Using conda:**
```bash
conda create --name bam-masterdata python=3.12
conda activate bam-masterdata
```

### Step 2: Install the Package

```bash
pip install --upgrade pip
pip install bam-masterdata
```

!!! tip "Faster Installation"
    For faster installation, you can use [`uv`](https://docs.astral.sh/uv/):
    ```bash
    pip install uv
    uv pip install bam-masterdata
    ```

### Step 3: Verify Installation

Let's verify that the installation was successful:

```python
import bam_masterdata
print(f"BAM Masterdata version: {bam_masterdata.__version__}")
```

## Your First BAM Masterdata Experience

### Understanding Entity Types

The BAM Masterdata system organizes information into different entity types:

- **Object Types**: Physical or conceptual objects (samples, instruments, people)
- **Collection Types**: Groups of related objects (experiments, projects)
- **Dataset Types**: Data files and their metadata
- **Vocabulary Types**: Controlled vocabularies for standardized values

*[Image placeholder: Entity relationship diagram showing the four main entity types and their relationships. Should include sample instances of each type.]*

### Creating Your First Entity

Let's create a simple sample object:

```python
from bam_masterdata.datamodel.object_types import Sample

# Create a new sample instance
my_sample = Sample(
    code="SAMPLE_001",
    name="Steel Test Sample",
    description="A steel sample for mechanical testing"
)

print(f"Created sample: {my_sample.code}")
print(f"Sample name: {my_sample.name}")
```

### Working with Properties

Entities have properties that store specific information:

```python
# Access properties
print("Sample properties:")
for prop_name, prop_value in my_sample.properties.items():
    print(f"  {prop_name}: {prop_value}")

# Set a property
my_sample.set_property("material_type", "Steel")
my_sample.set_property("dimensions", "10x10x10 mm")
```

### Exploring Available Entity Types

Let's see what types of entities are available:

```python
from bam_masterdata.datamodel import dataset_types, object_types, collection_types

# List some available dataset types
print("Available dataset types:")
for attr_name in dir(dataset_types):
    if not attr_name.startswith('_'):
        cls = getattr(dataset_types, attr_name)
        if hasattr(cls, 'defs'):
            print(f"  - {attr_name}: {cls.defs.description}")
```

### Converting to Different Formats

The package supports various export formats:

```python
# Convert to dictionary
sample_dict = my_sample.to_dict()
print("Sample as dictionary:", sample_dict)

# Convert to JSON
sample_json = my_sample.to_json()
print("Sample as JSON:", sample_json)
```

## Working with Real Data

### Loading from Excel

*[Image placeholder: Screenshot of an Excel file with masterdata structure showing columns for entity definitions, properties, and relationships.]*

```python
from bam_masterdata.excel.excel_to_entities import MasterdataExcelExtractor

# Initialize the extractor
extractor = MasterdataExcelExtractor()

# Load entities from Excel file
# entities = extractor.excel_to_entities("path/to/your/masterdata.xlsx")
```

### Using the Command Line Interface

The package provides a CLI for common operations:

```bash
# Export current masterdata to Excel
bam-masterdata export-to-excel output.xlsx

# Check masterdata consistency
bam-masterdata checker

# Fill masterdata from OpenBIS
bam-masterdata fill-masterdata
```

*[Image placeholder: Terminal screenshot showing the CLI commands in action with sample output.]*

## Next Steps

Now that you've completed this tutorial, you can:

1. **Explore How-to Guides**: Learn specific tasks and workflows
2. **Read the Explanations**: Understand the concepts behind the system
3. **Browse the API Reference**: Dive deep into specific classes and methods

### Development Setup

If you want to contribute or modify the package:

```bash
git clone https://github.com/BAMresearch/bam-masterdata.git
cd bam-masterdata
python3 -m venv .venv
source .venv/bin/activate
./scripts/install_python_dependencies.sh
```

### Common Issues and Solutions

**Issue**: Import errors when using the package
**Solution**: Ensure your virtual environment is activated and all dependencies are installed

**Issue**: Excel file not loading correctly
**Solution**: Check that your Excel file follows the expected masterdata schema format

For more troubleshooting tips, see our How-to Guides section.
