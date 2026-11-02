from pathlib import Path

from bam_masterdata.schema_explorer.exporter import write_schema

REPO_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = REPO_ROOT / "frontend" / "public" / "data"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for version in ("v0", "v1"):
        output = OUTPUT_DIR / f"schema-{version}.json"
        write_schema(version, output)
        print(f"Exported {version}: {output}")


if __name__ == "__main__":
    main()
