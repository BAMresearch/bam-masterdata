# BAM Masterdata Schema Explorer

An interactive web application for exploring and visualizing the [BAM Masterdata](https://github.com/BAMresearch/bam-masterdata) schemas.

The Schema Explorer provides two views:

- **Graph:** Interactive visualization of object types and their inheritance relationships, with hierarchy-depth filtering, search, and navigation.
- **Object Browser:** Browse object types, inspect their properties and ontology references, and explore relationships.

The application supports multiple datamodel versions (currently `v0` and `v1`).

## Architecture

The Schema Explorer is built with **React, TypeScript, Vite, and Cytoscape.js**.

It is a static frontend that consumes JSON files generated from the Python datamodel definitions.

```text
bam_masterdata/datamodel/
    ├── v0/
    └── v1/
         │
         ▼
Python schema exporter
         │
         ▼
frontend/public/data/schema-v*.json
         │
         ▼
React + Cytoscape.js
```

The Python exporter (`bam_masterdata/schema_explorer/`) extracts object type definitions, properties, inheritance relationships, OBJECT references, and ontology annotations.

The frontend reads these exported definitions without requiring a backend, database connection, or running Python service.

## Development

### Prerequisites

- [Python](https://www.python.org/) and [uv](https://docs.astral.sh/uv/)
- [Node.js](https://nodejs.org/)
- [pnpm](https://pnpm.io/)

### 1. Install dependencies

From the repository root, install the Python dependencies:

```bash
uv sync
```

Then install the frontend dependencies:

```bash
cd frontend
pnpm install
```

### 2. Generate schema definitions and launch app locally

From the **repository root**, run:

```bash
./tools/scripts/dev_schema_explorer.sh
```

This regenerates the schema JSON files from the Python datamodel and starts
the Vite development server.

The schema JSON files are in:

```text
frontend/public/data/
├── schema-v0.json
└── schema-v1.json
```

**Note 1:** When modifying object types, properties, or relationships in the Python datamodel, regenerate these JSON files to reflect the changes in the Schema Explorer.

**Note 2:** Changes to React components and CSS are reflected automatically. Changes to Python datamodel definitions require regenerating the corresponding JSON files.

### 3. Build and validate

Before committing frontend changes, run:

```bash
pnpm lint
pnpm build
```

To preview the production build locally:

```bash
pnpm preview
```

The production files are generated in `frontend/dist/`.

## Relationship with the datamodel

The Python datamodel is the **source of truth** for the Schema Explorer.

The frontend does not define object types or relationships independently. Instead, it visualizes the information provided by the schema exporter.

The exported data includes:

- Object type identifiers, names, and descriptions.
- Property definitions and assignments.
- Python class inheritance relationships.
- References between object types.
- Ontology annotations, when available.

The graph currently visualizes inheritance relationships, while the Object Browser provides access to property definitions and other metadata.

The Schema Explorer is intended for **read-only visualization and navigation**. Changes to the datamodel must be made in the Python source code.

## Deployment

The Schema Explorer is deployed to GitHub Pages alongside the BAM Masterdata documentation.

The deployment is managed by `.github/workflows/docs.yml` and runs automatically when changes are pushed to main.

The workflow:

1. Builds the documentation using Zensical.
2. Generates the schema JSON files from the Python datamodel using .github/scripts/export_schemas.py.
3. Installs the frontend dependencies and builds the React application.
4. Copies the generated frontend into site/schema-explorer/.
5. Publishes the combined site to GitHub Pages.

The deployed application is available at:

https://bamresearch.github.io/bam-masterdata/schema-explorer/

The Python datamodel remains the source of truth. Schema JSON files are regenerated during deployment and are not tracked by Git.

Changes to the frontend or datamodel become available on the website after they are merged into main and the deployment workflow completes successfully.
