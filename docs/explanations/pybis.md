
# Understanding pyBIS

pyBIS is the Python client library that enables programmatic access to openBIS systems. This section explains how pyBIS works, its relationship to the BAM Masterdata package, and how to use it effectively for research data management.

## What is pyBIS?

[pyBIS](https://pybis.readthedocs.io/) is a Python library that provides a high-level interface to openBIS servers. It abstracts the complexity of the openBIS API and offers Pythonic methods for common data management operations.

*[Image placeholder: Diagram showing pyBIS as a bridge between Python applications and openBIS servers, with arrows indicating data flow and API calls.]*

## Key Features of pyBIS

### Object-Oriented Interface
pyBIS represents openBIS entities as Python objects:
- Samples become `Sample` objects
- Datasets become `DataSet` objects  
- Experiments become `Experiment` objects
- Properties are accessible as object attributes

### Lazy Loading
Objects are loaded on-demand to improve performance:
```python
# This doesn't fetch data immediately
sample = openbis.get_sample('/SPACE/SAMPLE_001')

# Data is fetched when you access properties
print(sample.code)  # Now the data is loaded
```

### Batch Operations
Efficient handling of multiple operations:
```python
# Create multiple samples at once
samples = [
    openbis.new_sample(code=f'SAMPLE_{i}', type='SAMPLE_TYPE')
    for i in range(100)
]
openbis.save_all(samples)
```

## Integration with BAM Masterdata

### Complementary Roles

**BAM Masterdata**: Defines the structure and schemas
- Entity type definitions
- Property specifications  
- Validation rules
- Code generation

**pyBIS**: Provides runtime access and manipulation
- Creating and updating entities
- Querying existing data
- File upload and download
- Relationship management

*[Image placeholder: Venn diagram showing the overlap and distinct roles of BAM Masterdata (schema definition) and pyBIS (runtime operations).]*

### Code Example: Integration Pattern

```python
from bam_masterdata.datamodel.object_types import Sample as BamSample
from bam_masterdata.openbis.login import ologin

# Connect using BAM's authentication helper
openbis = ologin(url="https://openbis.bam.de", user="researcher")

# Create entity using BAM Masterdata structure
bam_sample = BamSample(
    code="STEEL_001",
    name="High-strength steel specimen",
    properties={
        "material_type": "Steel",
        "composition": "Fe-C-Mn alloy"
    }
)

# Convert to pyBIS format
pybis_sample = openbis.new_sample(
    code=bam_sample.code,
    type=bam_sample.defs.code,
    space='/MATERIALS'
)

# Set properties defined in masterdata
for prop_code, value in bam_sample.properties.items():
    setattr(pybis_sample, prop_code.lower(), value)

# Save to openBIS
pybis_sample.save()
```

## Core pyBIS Operations

### Connection and Authentication

```python
import pybis

# Connect to openBIS server
openbis = pybis.Openbis('https://openbis.example.com')
openbis.login('username', 'password')

# Alternative: use session token
openbis.set_token('your_session_token')
```

### Creating Entities

```python
# Create a new sample
sample = openbis.new_sample(
    code='SAMPLE_001',
    type='MATERIAL_SAMPLE',
    space='/RESEARCH_GROUP_A'
)

# Set properties
sample.material_type = 'Steel'
sample.dimensions = '10x10x50 mm'
sample.save()

# Create an experiment
experiment = openbis.new_experiment(
    code='EXP_001',
    type='MEASUREMENT_EXPERIMENT',
    project='/RESEARCH_GROUP_A/PROJECT_001'
)
experiment.save()
```

### Querying Data

```python
# Get all samples of a specific type
samples = openbis.get_samples(type='MATERIAL_SAMPLE')

# Search with criteria
steel_samples = openbis.get_samples(
    type='MATERIAL_SAMPLE',
    material_type='Steel'
)

# Complex queries
from datetime import date
recent_samples = openbis.get_samples(
    registration_date_from=date(2024, 1, 1),
    registrator='researcher@bam.de'
)
```

### Working with Datasets

```python
# Create a dataset
dataset = openbis.new_dataset(
    type='RAW_DATA',
    experiment='/SPACE/PROJECT/EXP_001',
    files=['data.csv', 'metadata.json']
)

# Upload files
dataset.upload(['local_file.txt'], target_dir='uploaded/')
dataset.save()

# Download files
dataset.download(destination='./downloads/')

# Link dataset to samples
dataset.sample = sample
dataset.save()
```

*[Image placeholder: Workflow diagram showing the typical sequence of operations: connect → query → create → upload → link → save.]*

## Advanced pyBIS Features

### Relationship Management

```python
# Parent-child relationships
child_sample = openbis.new_sample(code='CHILD_001', type='DERIVED_SAMPLE')
child_sample.parents = [parent_sample]
child_sample.save()

# Many-to-many relationships through properties
sample.measured_with = [instrument1.code, instrument2.code]
sample.save()
```

### Bulk Operations

```python
# Efficient batch updates
samples_to_update = openbis.get_samples(project='/SPACE/PROJECT')
for sample in samples_to_update:
    sample.updated_date = date.today()

# Save all at once
openbis.save_all(samples_to_update)
```

### File Management

```python
# Upload multiple files
dataset.upload([
    'experiment_data.csv',
    'analysis_results.xlsx',
    'plot.png'
])

# Organize files in directories
dataset.upload('raw_data.csv', target_dir='raw/')
dataset.upload('processed_data.csv', target_dir='processed/')

# Download specific files
dataset.download(files=['analysis_results.xlsx'])
```

### Error Handling

```python
try:
    sample = openbis.get_sample('/SPACE/NONEXISTENT')
except pybis.exceptions.NotFound:
    print("Sample not found")
    
try:
    sample.save()
except pybis.exceptions.ValidationError as e:
    print(f"Validation failed: {e}")
```

## Performance Considerations

### Connection Management

```python
# Reuse connections
class BAMDataManager:
    def __init__(self, url, username, password):
        self.openbis = pybis.Openbis(url)
        self.openbis.login(username, password)
    
    def create_sample(self, sample_data):
        # Use the persistent connection
        sample = self.openbis.new_sample(**sample_data)
        return sample.save()
```

### Lazy Loading Optimization

```python
# Load related data efficiently
samples = openbis.get_samples(type='MATERIAL_SAMPLE')

# This triggers individual API calls (inefficient)
for sample in samples:
    print(sample.experiment.code)

# Better: use batch loading
experiments = {s.experiment.permId: s.experiment for s in samples}
for sample in samples:
    exp = experiments[sample.experiment.permId]
    print(exp.code)
```

### Caching Strategies

```python
from functools import lru_cache

class CachedBAMClient:
    def __init__(self, openbis):
        self.openbis = openbis
    
    @lru_cache(maxsize=128)
    def get_sample_cached(self, code):
        return self.openbis.get_sample(code)
    
    def invalidate_cache(self):
        self.get_sample_cached.cache_clear()
```

## Common Usage Patterns

### Data Import Pipeline

```python
def import_measurement_data(csv_file, experiment_code):
    # Read measurement data
    import pandas as pd
    data = pd.read_csv(csv_file)
    
    # Get or create experiment
    experiment = openbis.get_experiment(experiment_code)
    
    # Create samples from data
    samples = []
    for _, row in data.iterrows():
        sample = openbis.new_sample(
            code=row['sample_id'],
            type='MEASUREMENT_SAMPLE',
            experiment=experiment
        )
        
        # Set properties from CSV columns
        for column, value in row.items():
            if column != 'sample_id':
                setattr(sample, column.lower(), value)
        
        samples.append(sample)
    
    # Batch save
    openbis.save_all(samples)
    
    # Create dataset with original file
    dataset = openbis.new_dataset(
        type='IMPORTED_DATA',
        experiment=experiment,
        files=[csv_file]
    )
    dataset.save()
    
    return samples, dataset
```

### Quality Control Workflow

```python
def validate_and_flag_samples(sample_codes):
    samples = [openbis.get_sample(code) for code in sample_codes]
    validation_results = []
    
    for sample in samples:
        # Perform quality checks
        issues = []
        
        if not sample.material_type:
            issues.append("Missing material type")
        
        if not sample.dimensions:
            issues.append("Missing dimensions")
        
        # Update sample with validation results
        if issues:
            sample.quality_status = "FAILED"
            sample.quality_issues = "; ".join(issues)
        else:
            sample.quality_status = "PASSED"
            sample.quality_issues = ""
        
        validation_results.append({
            'code': sample.code,
            'status': sample.quality_status,
            'issues': issues
        })
    
    # Save all updates
    openbis.save_all(samples)
    
    return validation_results
```

### Reporting and Analytics

```python
def generate_project_report(project_code):
    # Get all entities in project
    project = openbis.get_project(project_code)
    experiments = openbis.get_experiments(project=project)
    
    report = {
        'project': project.code,
        'description': project.description,
        'experiments': []
    }
    
    for exp in experiments:
        samples = openbis.get_samples(experiment=exp)
        datasets = openbis.get_datasets(experiment=exp)
        
        exp_data = {
            'code': exp.code,
            'type': exp.type.code,
            'sample_count': len(samples),
            'dataset_count': len(datasets),
            'total_files': sum(len(ds.files) for ds in datasets)
        }
        report['experiments'].append(exp_data)
    
    return report
```

## Integration with Analysis Tools

### Jupyter Notebooks

```python
# Cell 1: Setup
import pybis
import pandas as pd
import matplotlib.pyplot as plt

openbis = pybis.Openbis('https://openbis.bam.de')
openbis.login_with_token('your_token')

# Cell 2: Data retrieval
samples = openbis.get_samples(
    type='MEASUREMENT_SAMPLE',
    experiment='/SPACE/PROJECT/MEASUREMENT_CAMPAIGN'
)

# Convert to DataFrame for analysis
data = pd.DataFrame([
    {
        'code': s.code,
        'temperature': s.temperature,
        'pressure': s.pressure,
        'yield_strength': s.yield_strength
    }
    for s in samples
])

# Cell 3: Analysis and visualization
plt.scatter(data['temperature'], data['yield_strength'])
plt.xlabel('Temperature (°C)')
plt.ylabel('Yield Strength (MPa)')
plt.title('Temperature vs Yield Strength')
```

### Automated Workflows

```python
import schedule
import time

def daily_data_sync():
    """Sync data from instruments to openBIS daily."""
    
    # Connect to openBIS
    openbis = pybis.Openbis('https://openbis.bam.de')
    openbis.login('automation_user', 'password')
    
    # Check for new instrument data
    new_files = scan_instrument_directory('/instrument_data/')
    
    for file_path in new_files:
        # Create dataset
        dataset = openbis.new_dataset(
            type='INSTRUMENT_DATA',
            experiment='/AUTOMATED/DAILY_IMPORT'
        )
        dataset.upload([file_path])
        dataset.save()
        
        # Move processed file
        archive_file(file_path)

# Schedule daily execution
schedule.every().day.at("02:00").do(daily_data_sync)

while True:
    schedule.run_pending()
    time.sleep(3600)  # Check every hour
```

*[Image placeholder: Integration diagram showing pyBIS connecting to various tools: Jupyter notebooks, automated scripts, analysis pipelines, and reporting systems.]*

## Best Practices for pyBIS Usage

### Security
- Use environment variables for credentials
- Implement proper session management
- Regularly rotate API tokens
- Audit access patterns

### Performance
- Batch operations when possible
- Use lazy loading appropriately
- Implement caching for frequently accessed data
- Monitor API call patterns

### Error Handling
- Implement comprehensive exception handling
- Provide meaningful error messages
- Log operations for debugging
- Implement retry logic for transient failures

### Code Organization
- Create reusable utility functions
- Implement data access layers
- Use configuration files for server settings
- Maintain clear documentation

pyBIS serves as the runtime engine that brings BAM Masterdata schemas to life, enabling researchers to interact with their data programmatically while maintaining the structure and validation rules defined in the masterdata schemas.