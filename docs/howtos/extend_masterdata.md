# How-to: Extend the Current Masterdata

This guide describes the recommended contribution workflow for extending BAM masterdata definitions.

## Contribution pipeline

### 1. Open an issue first

Start by opening an issue in GitHub:

- [Open issues in `bam-masterdata`](https://github.com/BAMresearch/bam-masterdata/issues)

In the issue, describe:

- which entity types/properties/vocabularies you want to add or change,
- why the change is needed,
- expected impact on existing data/parsers,
- and whether you will contribute Python modules or an Excel file.

### 2. Clone or fork the repository

Use either direct clone (if you have write access) or fork + clone:

```bash
git clone https://github.com/BAMresearch/bam-masterdata.git
cd bam-masterdata
git checkout -b <issue-number>-<short-topic>
```

### 3. Choose your implementation path

#### Path A: Edit the core BAM datamodel files

Modify the existing files in:

- `bam_masterdata/datamodel/object_types.py`: for new Object Types
- `bam_masterdata/datamodel/vocabulary_types.py`: for new Vocabularies

This is the direct path if you are proposing changes to the central BAM model.

#### Path B: Define a separate application datamodel folder

If you maintain an application-specific model, create a dedicated folder with your own modules (same structure and naming):

```text
.
└── bam_masterdata/
    └── datamodel/
        ├── object_types.py
        ├── vocabulary_types.py
        └── <your-new-application-folder>/
            ├── object_types.py
            └── vocabulary_types.py
```

The CLI can process a directory of Python modules, so this folder can be validated and compared against the base definitions in the BAM Masterdata.

### 4. Validate before opening a PR

Run project tests:

```bash
python -m pytest -sv tests
```

If you created/updated a separate datamodel folder, run the checker in `individual` mode:

```bash
bam_masterdata checker \
  --file-path ./bam_masterdata/datamodel/<your-new-application-folder>/ \
  --mode individual \
  --datamodel-path ./bam_masterdata/datamodel
```

### 5. Submit a pull request for review

Create a PR linked to the issue and include:

- a short change summary,
- rationale for each new/changed type or property,
- compatibility notes (especially renamed/removed fields),
- and checker/test results.

## Alternative: Submit only an Excel file

If you prefer not to edit Python modules directly, you can submit a `masterdata.xlsx` through the GitHub issue.

Maintainers (or you) can generate Python modules from that Excel file using:

```bash
bam_masterdata fill_masterdata \
  --excel-file /<path-to-your-excel-masterdata-file>/masterdata.xlsx \
  --export-dir ./bam_masterdata/datamodel/<your-new-application-folder>/ \
  --row-cell-info=True
```

This command converts Excel masterdata into Python `*_types.py` modules that can then be validated and reviewed in a PR.

!!! note
    You can also export an existing model to Excel first (for templating/comparison) with:
    ```bash
    bam_masterdata export_to_excel --export-dir ./artifacts
    ```

!!! warning "Planned transition in 2026"
    The current masterdata is expected to transition to a new [BFO](https://basic-formal-ontology.org/)- and [IAO](https://obofoundry.org/ontology/iao.html)-compliant version in **Q3-Q4 2026** (approximately **July 1, 2026 to December 31, 2026**).
    If possible, when proposing changes now, include short mapping notes (e.g., inline comments) to ease migration to the upcoming ontology-aligned model.
