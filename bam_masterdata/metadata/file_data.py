from collections.abc import Callable
from typing import Any

from pydantic.dataclasses import dataclass


class Resource:
    """
    Base class for all resources.

    A resource represents a data source (e.g. XML, JSON)
    that can be queried using a selector language.
    """

    def query(self, selector: str, selector_type: str) -> Any:
        raise NotImplementedError("Resource.query must be implemented in subclasses")


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
