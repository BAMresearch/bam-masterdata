#!/usr/bin/env bash
set -euo pipefail

# Move to the repository root, regardless of where the script is called.
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$REPO_ROOT"

echo "Exporting datamodel schemas..."
uv run python .github/scripts/export_schemas.py

echo "Starting Schema Explorer..."
cd frontend
pnpm dev
