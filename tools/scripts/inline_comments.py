import argparse
import json
import re
from pathlib import Path

PATTERNS = {
    "questions": re.compile(r"^\s*#\s*\?(.*)"),
    "todos": re.compile(r"^\s*#\s*TODO(.*)", re.IGNORECASE),
    "checks": re.compile(r"^\s*#\s*!(.*)"),
}


def extract_markers(root: Path):
    results = {
        "questions": [],
        "todos": [],
        "checks": [],
    }

    for pyfile in root.rglob("*.py"):
        try:
            lines = pyfile.read_text(encoding="utf-8").splitlines()
        except Exception as exc:
            print(f"Skipping {pyfile}: {exc}")
            continue

        for lineno, line in enumerate(lines, start=1):
            for category, pattern in PATTERNS.items():
                match = pattern.search(line)

                if match:
                    results[category].append(
                        {
                            "file": str(pyfile.relative_to(root)),
                            "line": lineno,
                            "text": match.group(1).strip(),
                            "raw": line.strip(),
                        }
                    )

    return results


def write_outputs(results, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)

    for category, items in results.items():
        outfile = output_dir / f"{category}.json"

        with outfile.open("w", encoding="utf-8") as f:
            json.dump(items, f, indent=2, ensure_ascii=False)

        print(f"Wrote {outfile} ({len(items)} entries)")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Extract special inline comments from Python modules."
    )

    parser.add_argument(
        "path",
        type=Path,
        help="Path to the Python module/package",
    )

    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=Path("."),
        help="Directory where JSON files will be written",
    )

    return parser.parse_args()


def main():
    args = parse_args()

    if not args.path.exists():
        raise SystemExit(f"Path does not exist: {args.path}")

    results = extract_markers(args.path)
    write_outputs(results, args.output_dir)


if __name__ == "__main__":
    main()
