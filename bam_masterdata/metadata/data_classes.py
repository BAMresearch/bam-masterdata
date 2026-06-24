import json
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from lxml import etree


class Resource:
    """
    Base class for all resources.

    A resource represents a data source (e.g. XML, JSON)
    that can be queried using a selector language.
    """

    def query(self, selector: str, selector_type: str) -> Any:
        raise NotImplementedError("Resource.query must be implemented in subclasses")


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


# -------------------------
# MAPPING
# -------------------------


@dataclass
class FieldMapping:
    """
    Defines how one field is extracted from a resource.

    Attributes:
        source: filename/key in resources dict
        selector: query expression (XPath or dot notation)
        selector_type: "xpath" or "jsonpath"
        transform: optional conversion function (e.g. float, int)
    """

    source: str
    selector: str
    selector_type: str
    transform: Callable[[Any], Any] | None = None


@dataclass
class ObjectMapping:
    """
    Defines how a target object is constructed from multiple fields.
    """

    target: type
    fields: dict[str, FieldMapping]


# -------------------------
# BUILDER
# -------------------------


class ObjectBuilder:
    """
    Builds domain objects from resources based on an ObjectMapping.

    Example:
        builder = ObjectBuilder(mapping)
        obj = builder.build(resources)
    """

    def __init__(self, mapping: ObjectMapping):
        self.mapping = mapping

    def build(self, resources: dict[str, Resource]):
        """
        Create an instance of the target class.

        Args:
            resources: dict of loaded resources (XML/JSON/etc.)

        Raises:
            KeyError: if a required resource is missing
            ValueError: if query or transformation fails
        """
        values = {}

        for field_name, field_mapping in self.mapping.fields.items():
            # --- resource lookup ---
            try:
                resource = resources[field_mapping.source]
            except KeyError as e:
                raise KeyError(
                    f"Resource '{field_mapping.source}' not found. "
                    f"Available: {list(resources.keys())}"
                ) from e

            # --- query execution ---
            try:
                value = resource.query(
                    field_mapping.selector,
                    field_mapping.selector_type,
                )
            except Exception as e:
                raise ValueError(
                    f"Query failed for field '{field_name}' "
                    f"using selector '{field_mapping.selector}'"
                ) from e

            # --- transformation ---
            try:
                if field_mapping.transform:
                    value = field_mapping.transform(value)
            except Exception as e:
                raise ValueError(
                    f"Transform failed for field '{field_name}' with value {value}"
                ) from e

            values[field_name] = value

        try:
            return self.mapping.target(**values)
        except Exception as e:
            raise TypeError(
                f"Failed to construct {self.mapping.target.__name__} "
                f"with values {values}"
            ) from e
