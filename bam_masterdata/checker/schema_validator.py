from bam_masterdata.metadata.definitions import ObjectTypeDef
from bam_masterdata.metadata.entities import ObjectType


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
