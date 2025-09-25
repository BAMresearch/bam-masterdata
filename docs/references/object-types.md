# Object Types Reference

This section provides comprehensive documentation for all object types available in the BAM Masterdata system. Object types define the structure and properties of research objects such as samples, instruments, people, and protocols.

## Overview

Object types represent physical or conceptual entities in the research workflow. They define what information can be stored about different types of research objects and how these objects relate to each other.

*[Image placeholder: Object type hierarchy diagram showing the main categories (Samples, Instruments, Personnel, Protocols, etc.) and their relationships within the research workflow.]*

## Base Object Type

::: bam_masterdata.metadata.entities.ObjectType
    options:
      show_root_heading: true
      show_source: false
      members:
        - defs
        - to_dict
        - to_json
        - to_openbis
        - add_relationship
        - remove_relationship
        - get_type
        - create_type

## Object Type Definitions

::: bam_masterdata.metadata.definitions.ObjectTypeDef
    options:
      show_root_heading: true
      show_source: false

## Research Objects

### Samples

::: bam_masterdata.datamodel.object_types.Sample
    options:
      show_root_heading: true
      show_source: false

The fundamental sample type for all research specimens and materials.

**Core Properties:**
- Material identification
- Physical dimensions
- Preparation methods
- Storage conditions
- Quality indicators

#### Specialized Sample Types

**Chemical Samples:**

::: bam_masterdata.datamodel.object_types.Chemical
    options:
      show_root_heading: true
      show_source: false

Chemical compounds, reagents, and solutions.

**Biological Samples:**

::: bam_masterdata.datamodel.object_types.Organism
    options:
      show_root_heading: true
      show_source: false

Biological organisms and specimens.

**Material Samples:**

::: bam_masterdata.datamodel.object_types.Steel
    options:
      show_root_heading: true
      show_source: false

Steel samples with metallurgical properties.

::: bam_masterdata.datamodel.object_types.Aluminium
    options:
      show_root_heading: true
      show_source: false

Aluminum samples and alloys.

### Instruments and Equipment

::: bam_masterdata.datamodel.object_types.Instrument
    options:
      show_root_heading: true
      show_source: false

Base class for all analytical and testing instruments.

**Instrument Categories:**

**Testing Machines:**

::: bam_masterdata.datamodel.object_types.TestingMachine
    options:
      show_root_heading: true
      show_source: false

Mechanical testing equipment for material characterization.

**Spectroscopy Instruments:**

::: bam_masterdata.datamodel.object_types.Ftir
    options:
      show_root_heading: true
      show_source: false

Fourier-transform infrared spectrometers.

::: bam_masterdata.datamodel.object_types.Nmr
    options:
      show_root_heading: true
      show_source: false

Nuclear magnetic resonance spectrometers.

**Microscopy Equipment:**

::: bam_masterdata.datamodel.object_types.Sem
    options:
      show_root_heading: true
      show_source: false

Scanning electron microscopes.

::: bam_masterdata.datamodel.object_types.Tem
    options:
      show_root_heading: true
      show_source: false

Transmission electron microscopes.

### Personnel

::: bam_masterdata.datamodel.object_types.Person
    options:
      show_root_heading: true
      show_source: false

Personnel involved in research activities.

**Key Properties:**
- Contact information
- Institutional affiliation
- Research expertise
- Role and responsibilities
- Access permissions

### Protocols and Procedures

::: bam_masterdata.datamodel.object_types.GeneralProtocol
    options:
      show_root_heading: true
      show_source: false

Standard operating procedures and experimental protocols.

::: bam_masterdata.datamodel.object_types.Sop
    options:
      show_root_heading: true
      show_source: false

Standard Operating Procedures with detailed step-by-step instructions.

### Organizational Objects

#### Projects

::: bam_masterdata.datamodel.object_types.Project
    options:
      show_root_heading: true
      show_source: false

Research projects and initiatives.

**Project Properties:**
- Funding information
- Timeline and milestones
- Participant roles
- Deliverables and outcomes

#### Storage and Inventory

::: bam_masterdata.datamodel.object_types.Storage
    options:
      show_root_heading: true
      show_source: false

Storage locations and containers.

::: bam_masterdata.datamodel.object_types.StoragePosition
    options:
      show_root_heading: true
      show_source: false

Specific positions within storage systems.

#### Supply Chain

::: bam_masterdata.datamodel.object_types.Supplier
    options:
      show_root_heading: true
      show_source: false

Suppliers and vendors.

::: bam_masterdata.datamodel.object_types.Product
    options:
      show_root_heading: true
      show_source: false

Products and materials available from suppliers.

::: bam_masterdata.datamodel.object_types.Order
    options:
      show_root_heading: true
      show_source: false

Purchase orders and procurement requests.

## Computational Objects

### Software and Code

::: bam_masterdata.datamodel.object_types.SoftwareCode
    options:
      show_root_heading: true
      show_source: false

Software applications and code repositories.

::: bam_masterdata.datamodel.object_types.JupyterNotebook
    options:
      show_root_heading: true
      show_source: false

Jupyter notebooks for interactive analysis.

### Computational Resources

::: bam_masterdata.datamodel.object_types.Hpc
    options:
      show_root_heading: true
      show_source: false

High-performance computing resources and clusters.

::: bam_masterdata.datamodel.object_types.LocalWorkstation
    options:
      show_root_heading: true
      show_source: false

Local computational workstations.

### Simulation Objects

::: bam_masterdata.datamodel.object_types.InteratomicPotential
    options:
      show_root_heading: true
      show_source: false

Interatomic potentials for molecular dynamics simulations.

::: bam_masterdata.datamodel.object_types.Pseudopotential
    options:
      show_root_heading: true
      show_source: false

Pseudopotentials for electronic structure calculations.

*[Image placeholder: Computational workflow diagram showing the relationship between software objects, computational resources, and simulation parameters.]*

## Complete Object Type List

All available object types in the BAM Masterdata system:

::: bam_masterdata.datamodel.object_types
    options:
      show_root_heading: false
      show_source: false
      filters:
        - "!^_"