import importlib
import inspect
import pkgutil
import re

from bam_masterdata.metadata.definitions import (
    DataType,
    ObjectTypeDef,
    PropertyTypeAssignment,
)
from bam_masterdata.metadata.entities import ObjectType


def get_object_types(version: str) -> list[type[ObjectType]]:
    """
    Discover object type definitions belonging to one datamodel `version`.

    Searches the version's Python package and its subpackages. Only classes defined in their original
    module and declaring their own ObjectTypeDef are returned.

    Args:
        version (str): The datamodel version (i.e., subfolder) to search for, e.g. "v0", "v1", etc.

    Returns:
        list[type[ObjectType]]: A list of ObjectType subclasses defined in the specified datamodel version, sorted by module and class name.
    """
    if not re.fullmatch(r"v\d+", version):
        raise ValueError(f"Invalid datamodel version: {version!r}")

    package_name = f"bam_masterdata.datamodel.{version}"

    try:
        package = importlib.import_module(package_name)
    except ModuleNotFoundError as exc:
        if exc.name == package_name:
            raise ValueError(f"Datamodel version {version!r} does not exist.") from exc
        raise

    module_names = [package_name]

    module_names.extend(
        module_info.name
        for module_info in pkgutil.walk_packages(
            package.__path__,
            prefix=f"{package_name}.",
        )
    )

    object_types: set[type[ObjectType]] = set()

    for module_name in module_names:
        module = importlib.import_module(module_name)

        for _, cls in inspect.getmembers(module, inspect.isclass):
            if cls.__module__ != module.__name__:
                continue

            if not issubclass(cls, ObjectType):
                continue

            if not isinstance(cls.__dict__.get("defs"), ObjectTypeDef):
                continue

            object_types.add(cls)

    return sorted(
        object_types,
        key=lambda cls: (cls.__module__, cls.__qualname__),
    )


def validate_object_type_codes(object_types: list[type[ObjectType]]) -> None:
    """
    Validate unique object type codes within a datamodel version. For example:

    ```python
    from bam_masterdata.datamodel.v1 import Root, Activity, Entity, MaterialEntity


    validate_object_type_codes([Root, Activity, Entity, MaterialEntity])
    ```

    Args:
        object_types (list[type[ObjectType]]): The list of ObjectType subclasses to validate.
    """

    seen: dict[str, type[ObjectType]] = {}

    for cls in object_types:
        if not isinstance(cls, type) or not issubclass(cls, ObjectType):
            raise TypeError(f"{cls!r} is not an ObjectType subclass.")

        defs = cls.__dict__.get("defs")

        if not isinstance(defs, ObjectTypeDef):
            continue

        code = defs.code

        if code in seen and seen[code] is not cls:
            previous = seen[code]
            raise ValueError(
                f"Duplicate object type code '{code}': "
                f"{previous.__module__}.{previous.__qualname__} "
                f"and {cls.__module__}.{cls.__qualname__}."
            )

        seen[code] = cls


def validate_object_references(object_types: list[type[ObjectType]]) -> None:
    """
    Validate OBJECT reference targets within a selected datamodel. The supplied classes must belong
    to the same datamodel version. Inherited properties are included, respecting Python attribute overrides.

    Args:
        object_types (list[type[ObjectType]]): The list of ObjectType subclasses to validate.
    """

    validate_object_type_codes(object_types)

    known_codes = {
        defs.code
        for cls in object_types
        if isinstance(defs := cls.__dict__.get("defs"), ObjectTypeDef)
    }

    for cls in object_types:
        if not isinstance(cls, type) or not issubclass(cls, ObjectType):
            raise TypeError(f"{cls!r} is not an ObjectType subclass.")

        # Collect inherited assignments, allowing child classes to override
        # properties by their Python attribute names.
        properties: dict[str, PropertyTypeAssignment] = {}

        for base in reversed(cls.__mro__):
            if not issubclass(base, ObjectType):
                continue

            for name, value in base.__dict__.items():
                if isinstance(value, PropertyTypeAssignment):
                    properties[name] = value
                elif name in properties:
                    # A child can also replace an inherited property with
                    # an attribute that is not a PropertyTypeAssignment.
                    del properties[name]

        for name, prop in properties.items():
            if prop.data_type != DataType.OBJECT:
                continue

            if prop.object_code in (None, "(ALL)"):
                continue

            if prop.object_code not in known_codes:
                raise ValueError(
                    f"Unknown object_code '{prop.object_code}' "
                    f"in {cls.__name__}.{name}. "
                    "The referenced object type is not defined "
                    "in the selected datamodel."
                )
