
# Controlled Vocabulary Reference

This section provides comprehensive documentation for all controlled vocabularies available in the BAM Masterdata system. Controlled vocabularies ensure data consistency by providing standardized terms for specific fields and properties.

## Overview

Controlled vocabularies are predefined sets of terms that can be used as values for specific properties. They ensure data consistency, enable better search capabilities, and facilitate data integration across different systems and research groups.

*[Image placeholder: Controlled vocabulary concept diagram showing how standardized terms flow from vocabulary definitions into property values and enable consistent data entry and searching.]*

## Base Vocabulary Type

::: bam_masterdata.metadata.entities.VocabularyType
    options:
      show_root_heading: true
      show_source: false
      members:
        - defs
        - terms
        - to_dict
        - to_json
        - to_openbis
        - get_vocabulary_class
        - get_type
        - create_type

## Vocabulary Type Definitions

::: bam_masterdata.metadata.definitions.VocabularyTypeDef
    options:
      show_root_heading: true
      show_source: false

## Vocabulary Terms

::: bam_masterdata.metadata.definitions.VocabularyTerm
    options:
      show_root_heading: true
      show_source: false

## Technical and System Vocabularies

### Storage Format

::: bam_masterdata.datamodel.vocabulary_types.StorageFormat
    options:
      show_root_heading: true
      show_source: false

Defines standard file and data storage formats used throughout the system.

**Common Terms:**
- CSV (Comma-Separated Values)
- JSON (JavaScript Object Notation)  
- HDF5 (Hierarchical Data Format 5)
- XLSX (Excel Spreadsheet)
- PDF (Portable Document Format)

### Default Collection Views

::: bam_masterdata.datamodel.vocabulary_types.DefaultCollectionViews
    options:
      show_root_heading: true
      show_source: false

Standard viewing modes and display options for collections in the user interface.

## Instrumentation and Equipment

### Instrument Status

::: bam_masterdata.datamodel.vocabulary_types.InstrumentStatus
    options:
      show_root_heading: true
      show_source: false

Standardized status values for instruments and equipment.

**Status Categories:**
- OPERATIONAL: Fully functional and available
- MAINTENANCE: Under scheduled maintenance
- REPAIR: Being repaired or out of service
- CALIBRATION: Undergoing calibration procedures
- RETIRED: No longer in active use

### Testing Machine Types

::: bam_masterdata.datamodel.vocabulary_types.TestingMachineDriveType
    options:
      show_root_heading: true
      show_source: false

Drive mechanisms for testing machines.

::: bam_masterdata.datamodel.vocabulary_types.TestingMachineLoadType
    options:
      show_root_heading: true
      show_source: false

Load application methods for testing machines.

*[Image placeholder: Equipment classification diagram showing different types of testing machines, their drive mechanisms, and load types with visual icons.]*

## Materials and Specimens

### Material Types and Properties

::: bam_masterdata.datamodel.vocabulary_types.BuildingMaterialType
    options:
      show_root_heading: true
      show_source: false

Categories of building and construction materials.

::: bam_masterdata.datamodel.vocabulary_types.PhysicalState
    options:
      show_root_heading: true
      show_source: false

Physical states of materials and specimens.

### Material Scales

::: bam_masterdata.datamodel.vocabulary_types.MatScale
    options:
      show_root_heading: true
      show_source: false

Scale levels for material characterization and modeling.

**Scale Hierarchy:**
- ATOMIC: Individual atoms and bonds
- MOLECULAR: Molecular structures and interactions
- NANO: Nanoscale features and properties
- MICRO: Microscale structure and behavior
- MESO: Mesoscale phenomena
- MACRO: Macroscopic properties and behavior

### Material Structures

::: bam_masterdata.datamodel.vocabulary_types.MatStructure
    options:
      show_root_heading: true
      show_source: false

Structural classifications for materials.

::: bam_masterdata.datamodel.vocabulary_types.BravaisLattice
    options:
      show_root_heading: true
      show_source: false

Crystallographic lattice types for crystalline materials.

## Chemical and Biological Categories

### Chemical Product Categories

::: bam_masterdata.datamodel.vocabulary_types.ChemicalProductCategory
    options:
      show_root_heading: true
      show_source: false

Classification system for chemical products and reagents.

### Organism Classifications

::: bam_masterdata.datamodel.vocabulary_types.OrganismGroup
    options:
      show_root_heading: true
      show_source: false

Taxonomic and functional groupings for biological organisms.

::: bam_masterdata.datamodel.vocabulary_types.OrganismRiskGroup
    options:
      show_root_heading: true
      show_source: false

Biosafety risk classifications for organisms.

### Genetic Engineering

::: bam_masterdata.datamodel.vocabulary_types.GentechSafetyLevel
    options:
      show_root_heading: true
      show_source: false

Safety levels for genetic engineering activities.

::: bam_masterdata.datamodel.vocabulary_types.PlasmidOri
    options:
      show_root_heading: true
      show_source: false

Origin of replication types for plasmids.

## Analytical Methods and Techniques

### Spectroscopy

::: bam_masterdata.datamodel.vocabulary_types.FtirAccessories
    options:
      show_root_heading: true
      show_source: false

Accessories and configurations for FTIR spectroscopy.

::: bam_masterdata.datamodel.vocabulary_types.OpticalSpectrometerType
    options:
      show_root_heading: true
      show_source: false

Types of optical spectrometers and their configurations.

### Nuclear Magnetic Resonance

::: bam_masterdata.datamodel.vocabulary_types.NmrExperimentTypes
    options:
      show_root_heading: true
      show_source: false

Standard NMR experiment types and pulse sequences.

::: bam_masterdata.datamodel.vocabulary_types.NmrNuclei
    options:
      show_root_heading: true
      show_source: false

Nuclear isotopes commonly studied with NMR.

::: bam_masterdata.datamodel.vocabulary_types.NmrSolvents
    options:
      show_root_heading: true
      show_source: false

Standard solvents used in NMR experiments.

### Mass Spectrometry

::: bam_masterdata.datamodel.vocabulary_types.MassSpecType
    options:
      show_root_heading: true
      show_source: false

Types of mass spectrometers and ionization methods.

*[Image placeholder: Analytical techniques overview showing different instrument families (spectroscopy, chromatography, microscopy) with their vocabulary categories.]*

## Computational and Simulation

### Electronic Structure Calculations

::: bam_masterdata.datamodel.vocabulary_types.AtomisticCalcType
    options:
      show_root_heading: true
      show_source: false

Types of atomistic calculations and simulations.

::: bam_masterdata.datamodel.vocabulary_types.AtomXcFunctional
    options:
      show_root_heading: true
      show_source: false

Exchange-correlation functionals for density functional theory.

::: bam_masterdata.datamodel.vocabulary_types.ElectronicSmearing
    options:
      show_root_heading: true
      show_source: false

Electronic smearing methods for band structure calculations.

### Pseudopotentials

::: bam_masterdata.datamodel.vocabulary_types.PseudopotFunctional
    options:
      show_root_heading: true
      show_source: false

Functional types used in pseudopotential generation.

::: bam_masterdata.datamodel.vocabulary_types.PseudopotType
    options:
      show_root_heading: true
      show_source: false

Categories of pseudopotentials (norm-conserving, ultrasoft, PAW).

### Molecular Dynamics

::: bam_masterdata.datamodel.vocabulary_types.AtomPotentialStyle
    options:
      show_root_heading: true
      show_source: false

Interatomic potential styles for molecular dynamics simulations.

::: bam_masterdata.datamodel.vocabulary_types.ThermodynEnsemble
    options:
      show_root_heading: true
      show_source: false

Thermodynamic ensembles for molecular dynamics simulations.

## Organizational and Administrative

### BAM-Specific Classifications

::: bam_masterdata.datamodel.vocabulary_types.BamFieldOfActivity
    options:
      show_root_heading: true
      show_source: false

Research fields and activities at BAM.

::: bam_masterdata.datamodel.vocabulary_types.BamFocusArea
    options:
      show_root_heading: true
      show_source: false

Strategic focus areas within BAM.

::: bam_masterdata.datamodel.vocabulary_types.BamOe
    options:
      show_root_heading: true
      show_source: false

Organizational units (Organisationseinheiten) within BAM.

### Location and Infrastructure

::: bam_masterdata.datamodel.vocabulary_types.BamLocation
    options:
      show_root_heading: true
      show_source: false

Physical locations within BAM facilities.

::: bam_masterdata.datamodel.vocabulary_types.BamHouse
    options:
      show_root_heading: true
      show_source: false

Building designations at BAM.

::: bam_masterdata.datamodel.vocabulary_types.BamFloor
    options:
      show_root_heading: true
      show_source: false

Floor levels within BAM buildings.

::: bam_masterdata.datamodel.vocabulary_types.BamRoom
    options:
      show_root_heading: true
      show_source: false

Room designations within BAM facilities.

### Personnel and Status

::: bam_masterdata.datamodel.vocabulary_types.PersonStatus
    options:
      show_root_heading: true
      show_source: false

Employment and affiliation status for personnel.

::: bam_masterdata.datamodel.vocabulary_types.ProjectStatus
    options:
      show_root_heading: true
      show_source: false

Status categories for research projects.

*[Image placeholder: BAM organizational chart showing the relationship between focus areas, organizational units, and locations with their corresponding vocabulary terms.]*

## Usage Examples

### Working with Vocabulary Terms

```python
from bam_masterdata.datamodel.vocabulary_types import InstrumentStatus, MaterialTypes

# Access vocabulary terms
status_vocab = InstrumentStatus()
available_statuses = status_vocab.terms

for term_code, term_data in available_statuses.items():
    print(f"Status: {term_code} - {term_data['label']}")
    print(f"Description: {term_data.get('description', 'N/A')}")
```

### Validating Property Values

```python
def validate_instrument_status(status_value: str) -> bool:
    """Validate that a status value is allowed."""
    status_vocab = InstrumentStatus()
    return status_value in status_vocab.terms.keys()

# Usage
if validate_instrument_status("OPERATIONAL"):
    print("Valid status")
else:
    print("Invalid status - must be one of:", list(status_vocab.terms.keys()))
```

### Creating Custom Vocabularies

```python
from bam_masterdata.metadata.entities import VocabularyType
from bam_masterdata.metadata.definitions import VocabularyTypeDef, VocabularyTerm

class CustomLabStatus(VocabularyType):
    defs = VocabularyTypeDef(
        code="CUSTOM_LAB_STATUS",
        description="Custom laboratory status vocabulary"
    )
    
    terms = {
        "SETUP": VocabularyTerm(
            code="SETUP",
            label="Setting Up",
            description="Laboratory is being prepared"
        ),
        "ACTIVE": VocabularyTerm(
            code="ACTIVE", 
            label="Active",
            description="Laboratory is operational"
        ),
        "CLEANUP": VocabularyTerm(
            code="CLEANUP",
            label="Cleaning Up", 
            description="Laboratory is being cleaned"
        )
    }
```

### Using Vocabularies in Entity Properties

```python
from bam_masterdata.datamodel.object_types import Instrument

# Create instrument with vocabulary-controlled status
instrument = Instrument(
    code="FTIR_001",
    name="FTIR Spectrometer Alpha"
)

# Set status using vocabulary term
instrument.set_property("status", "OPERATIONAL")  # Must match vocabulary

# Set instrument type using vocabulary
instrument.set_property("instrument_type", "SPECTROSCOPY")
```

## Vocabulary Maintenance and Updates

### Adding New Terms

```python
def add_vocabulary_term(
    vocab_class: VocabularyType,
    term_code: str,
    term_label: str,
    term_description: str = ""
) -> VocabularyType:
    """Add a new term to an existing vocabulary."""
    
    new_term = VocabularyTerm(
        code=term_code,
        label=term_label,
        description=term_description
    )
    
    # Add to vocabulary (this would typically be done through proper update mechanisms)
    vocab_class.terms[term_code] = new_term
    
    return vocab_class
```

### Vocabulary Synchronization

```python
from bam_masterdata.openbis.login import ologin

def sync_vocabulary_with_openbis(vocab: VocabularyType, openbis_connection):
    """Synchronize vocabulary with openBIS."""
    
    # Convert to openBIS format
    openbis_vocab = vocab.to_openbis()
    
    # Check if vocabulary exists
    try:
        existing_vocab = openbis_connection.get_vocabulary(vocab.defs.code)
        # Update existing vocabulary
        existing_vocab.terms = openbis_vocab.terms
        existing_vocab.save()
    except:
        # Create new vocabulary
        openbis_connection.create_vocabulary(openbis_vocab)
```

## Quality Control and Validation

### Vocabulary Consistency Checks

```python
def check_vocabulary_consistency(vocab: VocabularyType) -> list:
    """Check vocabulary for consistency issues."""
    
    issues = []
    
    # Check for duplicate labels
    labels = [term.label for term in vocab.terms.values()]
    duplicates = set([label for label in labels if labels.count(label) > 1])
    if duplicates:
        issues.append(f"Duplicate labels found: {duplicates}")
    
    # Check for empty descriptions
    empty_descriptions = [
        code for code, term in vocab.terms.items()
        if not term.description.strip()
    ]
    if empty_descriptions:
        issues.append(f"Terms with empty descriptions: {empty_descriptions}")
    
    # Check naming conventions
    for code, term in vocab.terms.items():
        if not code.isupper():
            issues.append(f"Term code should be uppercase: {code}")
    
    return issues
```

### Usage Analytics

```python
def analyze_vocabulary_usage(vocab_code: str, entity_data: dict) -> dict:
    """Analyze how vocabulary terms are used in actual data."""
    
    usage_stats = {}
    total_uses = 0
    
    # Count usage of each term
    for entity_type, entities in entity_data.items():
        for entity_id, entity in entities.items():
            properties = entity.get("properties", {})
            for prop_name, prop_value in properties.items():
                if isinstance(prop_value, str) and prop_value in vocab_code:
                    usage_stats[prop_value] = usage_stats.get(prop_value, 0) + 1
                    total_uses += 1
    
    # Calculate percentages
    usage_percentages = {
        term: (count / total_uses * 100) if total_uses > 0 else 0
        for term, count in usage_stats.items()
    }
    
    return {
        "total_uses": total_uses,
        "term_counts": usage_stats,
        "term_percentages": usage_percentages,
        "unused_terms": []  # Terms defined but never used
    }
```

*[Image placeholder: Vocabulary usage dashboard showing term frequency, usage trends over time, and identification of unused or underutilized terms.]*

## Best Practices

### Vocabulary Design
- Use clear, unambiguous term labels
- Provide comprehensive descriptions
- Follow consistent naming conventions
- Consider hierarchical relationships where appropriate

### Term Management
- Regular review and updates
- Remove obsolete terms carefully
- Document changes and rationale
- Maintain backward compatibility when possible

### Integration
- Validate property values against vocabularies
- Use vocabulary terms consistently across systems
- Provide user-friendly term selection interfaces
- Support term translation for international use

### Documentation
- Maintain clear definitions for each term
- Include usage examples and context
- Document relationships between vocabularies
- Provide migration guides for vocabulary changes

## Complete Vocabulary Type List

All available controlled vocabularies in the BAM Masterdata system:

::: bam_masterdata.datamodel.vocabulary_types
    options:
      show_root_heading: false
      show_source: false
      filters:
        - "!^_"