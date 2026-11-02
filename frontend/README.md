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

### 2. Generate the schema definitions

The frontend uses JSON files generated from the Python datamodel.

From the **repository root**, run:

```bash
uv run python .github/scripts/export_schemas.py
```

This generates:

```text
frontend/public/data/
├── schema-v0.json
└── schema-v1.json
```

**Important:** When modifying object types, properties, or relationships in the Python datamodel, regenerate these JSON files to reflect the changes in the Schema Explorer.

### 3. Start the development server

From `frontend/`:

```bash
pnpm dev
```

Vite starts a local development server with hot module replacement (HMR).

Changes to React components and CSS are reflected automatically. Changes to Python datamodel definitions require regenerating the corresponding JSON files.

### 4. Build and validate

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

The application is intended to be published through GitHub Pages alongside the BAM Masterdata documentation.
