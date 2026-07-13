import json
from pathlib import Path
from typing import Any

from lxml import etree
from metadata import Resource
from pydantic.dataclasses import dataclass

# -------------------------
# XML RESOURCE
# -------------------------


@dataclass
class XMLResource(Resource):
    """
    XML file wrapper using lxml.

    Supports XPath queries.
    """

    path: Path

    def __post_init__(self):
        try:
            self.tree = etree.parse(str(self.path))
        except OSError as e:
            raise FileNotFoundError(
                f"XML file not found or unreadable: {self.path}"
            ) from e
        except etree.XMLSyntaxError as e:
            raise ValueError(f"Invalid XML syntax in file: {self.path}") from e

    def query(self, selector: str, selector_type: str) -> Any:
        """
        Execute an XPath query on the XML document.
        """
        if selector_type != "xpath":
            raise ValueError(f"Unsupported selector type for XML: {selector_type}")

        try:
            result = self.tree.xpath(selector)
        except Exception as e:
            raise ValueError(f"Invalid XPath expression: {selector}") from e

        if not result:
            return None

        return result[0] if len(result) == 1 else result


# -------------------------
# JSON RESOURCE
# -------------------------


@dataclass
class JSONResource(Resource):
    """
    JSON file wrapper.

    Supports dot-notation queries like:
    "sample.name"
    """

    path: Path

    def __post_init__(self):
        try:
            with open(self.path, encoding="utf-8") as f:
                self.data = json.load(f)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"JSON file not found: {self.path}") from e
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in file: {self.path}") from e

    def query(self, selector: str, selector_type: str) -> Any:
        """
        Resolve a dot-separated path inside JSON.
        Example: "instrument.voltage"
        """
        if selector_type != "jsonpath":
            raise ValueError(f"Unsupported selector type for JSON: {selector_type}")

        try:
            value = self.data
            for key in selector.split("."):
                value = value[key]
            return value
        except KeyError as e:
            raise KeyError(f"Key '{key}' not found in JSON path '{selector}'") from e
        except TypeError as e:
            raise ValueError(f"Invalid structure while resolving '{selector}'") from e
