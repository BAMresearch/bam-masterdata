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


This API reference provides comprehensive documentation for all public classes and functions in the BAM Masterdata package. For more detailed examples and usage patterns, see the How-to Guides and Tutorial sections.