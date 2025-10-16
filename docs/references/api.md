# API Reference

This API reference provides comprehensive documentation for all public classes and functions in the BAM Masterdata package. For more detailed examples and usage patterns, see the How-to Guides and Tutorial sections.

<!--
-------------------------------------------------------------
metadata/
-------------------------------------------------------------
-->

::: bam_masterdata.metadata.entities
    options:
      show_root_heading: true
      members:
        - BaseEntity
        - ObjectType
        - CollectionType
        - DatasetType
        - VocabularyType

---

::: bam_masterdata.metadata.definitions
    options:
      show_root_heading: true
      members:
        - EntityDef
        - ObjectTypeDef
        - CollectionTypeDef
        - DatasetTypeDef
        - VocabularyTypeDef
        - PropertyTypeDef
        - PropertyTypeAssignment
        - VocabularyTerm

---

::: bam_masterdata.metadata.entities_dict
    options:
      show_root_heading: true
      members:
        - EntitiesDict

---

<!--
-------------------------------------------------------------
cli/
-------------------------------------------------------------
-->

<!-- ::: bam_masterdata.cli.cli
    options:
      show_root_heading: true
      show_source: false -->

::: bam_masterdata.cli.fill_masterdata
    options:
      show_root_heading: true
      members:
        - MasterdataCodeGenerator

---

::: bam_masterdata.cli.excel_to_entities
    options:
      show_root_heading: true
      members:
        - MasterdataExcelExtractor

---

::: bam_masterdata.cli.entities_to_excel
    options:
      show_root_heading: true

---

::: bam_masterdata.cli.entities_to_rdf
    options:
      show_root_heading: true

---

::: bam_masterdata.cli.run_parser
    options:
      show_root_heading: true

---


<!--
-------------------------------------------------------------
excel/
-------------------------------------------------------------
-->

::: bam_masterdata.excel.excel_to_entities
    options:
      show_root_heading: true
      members:
        - MasterdataExcelExtractor

---

<!--
-------------------------------------------------------------
openbis/
-------------------------------------------------------------
-->

::: bam_masterdata.openbis.login
    options:
      show_root_heading: true

---

::: bam_masterdata.openbis.get_entities
    options:
      show_root_heading: true
      members:
        - OpenbisEntities

---

<!--
-------------------------------------------------------------
checker/
-------------------------------------------------------------
-->

::: bam_masterdata.checker.checker
    options:
      show_root_heading: true
      members:
        - MasterdataChecker

---

::: bam_masterdata.checker.masterdata_validator
    options:
      show_root_heading: true
      members:
        - MasterdataValidator

---

::: bam_masterdata.checker.source_loader
    options:
      show_root_heading: true
      members:
        - SourceLoader

---

<!--
-------------------------------------------------------------
parsing/
-------------------------------------------------------------
-->

::: bam_masterdata.parsing.parsing
    options:
      show_root_heading: true
      members:
        - AbstractParser

---

<!--
-------------------------------------------------------------
utils/
-------------------------------------------------------------
-->

::: bam_masterdata.utils.utils
    options:
      show_root_heading: true

---

::: bam_masterdata.utils.paths
    options:
      show_root_heading: true

---