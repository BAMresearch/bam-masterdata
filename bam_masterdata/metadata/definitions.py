import datetime
import re
from enum import StrEnum
from typing import Any
from urllib.parse import urlsplit

from pint import DefinitionSyntaxError, UndefinedUnitError, UnitRegistry
from pydantic import BaseModel, Field, field_validator, model_validator

from bam_masterdata.utils import code_to_class_name


class DataType(StrEnum):
    """Enumeration of the data types available in openBIS."""

    BOOLEAN = "BOOLEAN"
    CONTROLLEDVOCABULARY = "CONTROLLEDVOCABULARY"
    DATE = "DATE"
    HYPERLINK = "HYPERLINK"
    INTEGER = "INTEGER"
    MULTILINE_VARCHAR = "MULTILINE_VARCHAR"
    OBJECT = "OBJECT"
    SAMPLE = "SAMPLE"
    REAL = "REAL"
    TIMESTAMP = "TIMESTAMP"
    VARCHAR = "VARCHAR"
    XML = "XML"
    JSON = "JSON"

    @property
    def pytype(self) -> type:
        """
        Maps the openBIS data type to its corresponding Python type.

        Returns:
            type: The native Python type of the openBIS data type.
        """
        mapping = {
            "BOOLEAN": bool,
            "DATE": datetime.date,
            "HYPERLINK": str,
            "INTEGER": int,
            "MULTILINE_VARCHAR": str,
            "REAL": float,
            "TIMESTAMP": datetime.datetime,
            "VARCHAR": str,
        }
        return mapping.get(self, None)


_UNIT_REGISTRY = UnitRegistry()
_UNIT_LABEL_PATTERN = re.compile(r"\[[^\]]+\]")
_UNIT_SUFFIX_PATTERN = re.compile(r"\bin \[[^\]]+\]")
_EXCEL_NAME_MAP = {
    "CollectionTypeDef": "EXPERIMENT_TYPE",
    "DatasetTypeDef": "DATASET_TYPE",
    "ObjectTypeDef": "SAMPLE_TYPE",
    "VocabularyTypeDef": "VOCABULARY_TYPE",
}
_EXCLUDED_EXCEL_HEADER_FIELDS = frozenset(
    {
        "iri",
        "id",
        "row_location",
        "prev_versions",
        "description_de",
        "property_label_de",
        "label_de",
    }
)
_PREV_VERSION_PATTERN = re.compile(
    r"^[A-Za-z0-9_$.]+:v[0-9]+$"
)  # example: "EXPERIMENTAL_STEP:v0"
_ONTOLOGY_ID_PATTERN = re.compile(
    r"^[A-Za-z][A-Za-z0-9]*_[0-9]+$"
)  # example: "BFO_0000001", "CHEBI_12345"


def _format_excel_header(field_name: str) -> str:
    """Convert a model field name into the header format used in openBIS Excel files."""
    return field_name.replace("_", " ").capitalize()


def _entity_type_for_model_id(model_name: str) -> str:
    """Map a definition model name to the entity family used by `code_to_class_name`."""
    return "property" if "PropertyType" in model_name else "object"


def _combine_translations(english: str, german: str | None) -> str:
    if "//" in english or not german:
        return english

    return f"{english}//{german}"


class EntityDef(BaseModel):
    """
    Abstract base class for all masterdata entity definitions. The entity definitions are immutable properties.
    This class provides a common interface (with common attributes like `code` and
    `description`.) for all entity definitions.
    """

    code: str = Field(
        ...,
        description="""
        Code string identifying the entity with an openBIS inventory definition. Note that:

        - Must be uppercase and separated by underscores, e.g. `'EXPERIMENTAL_STEP'`.
        - If the entity is native to openBIS, the code must start with a dollar sign, e.g. `'$NAME'`.
        - In the case of inheritance, it needs to be separated by dots, e.g. `'WELDING_EQUIPMENT.INSTRUMENT'`.
        """,
    )

    description: str = Field(
        ...,
        description="""
        Description of the entity. This is the human-readable text for the object and must be
        as complete and concise as possible. The German description can be added after the English
        description separated by a double slash (//), e.g. `'Chemical Substance//Chemische Substanz'`.
        """,
    )

    description_de: str | None = Field(
        default=None,
        description="""
        Optional German description of the entity.

        Note: The main `description` field is considered English. German translations should be provided
        separately instead of using the legacy 'English//German' format.
        """,
    )

    prev_versions: list[str] | None = Field(
        default=None,
        description="""
        references to previous versions of this entity.

        Each reference follows the format `"<code>:<version>"`, where `<code>` is the code of the entity and `<version>` is the version number.

        Examples:
            ["EXPERIMENTAL_STEP:v0", "EXPERIMENT:v1"]
        """,
    )

    iri: list[str] | None = Field(
        default=None,
        description="""
        List of ontology references associated with the entity.

        Each reference can be either:
        - An absolute HTTP(S) IRI, e.g. "https://w3id.org/pmd/co/PMD_0000001".
        - An OBO-style ontology identifier, e.g. "BFO_0000001".

        Duplicate references and empty lists are not allowed.
        """,
    )

    # INTERNAL FIELDS
    id: str | None = Field(
        default=None,
        description="""
        Identifier of the entity defined as the class name and used to serialize the entity definitions
        in other formats.
        """,
    )

    row_location: str | None = Field(
        default=None,
        description="""
        Row in the Excel at which the entity type field is defined. It is a string with the format `"<row-letter><row_number>"`.
        Example: "A1" ot "A107". This field is useful when checking the consistency of Excel files with multiple entity
        types defined to quickly locate the specific Excel cell which logs a message when applying the `checker` CLI.
        """,
    )

    @field_validator("code")
    @classmethod
    def validate_code(cls, value: str) -> str:
        """Validate entity codes against the allowed openBIS format."""
        if not value or not re.match(r"^[\w_\$\.\-\+]+$", value):
            raise ValueError(
                "`code` must follow the rules specified in the description: 1) Must be uppercase, "
                "2) separated by underscores, 3) start with a dollar sign if native to openBIS, "
                "4) separated by dots if there is inheritance."
            )
        return value

    @field_validator("description", "description_de")
    @classmethod
    def strip_description(cls, value: str | None) -> str | None:
        """Strip leading and trailing whitespace from descriptions."""
        return value.strip() if value is not None else None

    @field_validator("prev_versions")
    @classmethod
    def validate_prev_versions(cls, value: list[str] | None) -> list[str] | None:
        """Validate previous version references against the allowed openBIS format."""
        if value is None:
            return value

        if not value:
            raise ValueError("`prev_versions` must not be an empty list.")

        for reference in value:
            if not _PREV_VERSION_PATTERN.fullmatch(reference):
                raise ValueError(
                    f"Invalid previous version reference: {reference}. Must follow the format '<code>:v<version>', e.g. 'EXPERIMENTAL_STEP:v0'."
                )

        if len(value) != len(set(value)):
            raise ValueError("`prev_versions` contains duplicate references.")

        return value

    @field_validator("iri")
    @classmethod
    def validate_iri(
        cls,
        value: list[str] | None,
    ) -> list[str] | None:
        """Validate ontology references."""

        if value is None:
            return None

        if not value:
            raise ValueError("`iri` cannot be an empty list.")

        for reference in value:
            if not reference or reference != reference.strip():
                raise ValueError(f"Invalid ontology reference: {reference!r}")

            # Accept OBO-style identifiers.
            if _ONTOLOGY_ID_PATTERN.fullmatch(reference):
                continue

            # Otherwise, require an absolute HTTP(S) IRI.
            try:
                parsed = urlsplit(reference)
                valid_url = (
                    parsed.scheme in {"http", "https"}
                    and bool(parsed.hostname)
                    and not any(char.isspace() for char in reference)
                )
            except ValueError:
                valid_url = False

            if not valid_url:
                raise ValueError(
                    f"Invalid ontology reference: {reference!r}. "
                    "Expected an HTTP(S) IRI or an ontology identifier "
                    "such as 'BFO_0000001'."
                )

        if len(value) != len(set(value)):
            raise ValueError("`iri` contains duplicate references.")

        return value

    @property
    def name(self) -> str:
        return self.__class__.__name__

    @property
    def excel_name(self) -> str:
        """
        Returns the name of the entity in a format suitable for the openBIS Excel file.
        """
        return _EXCEL_NAME_MAP.get(self.name)

    @property
    def excel_headers_map(self) -> dict:
        """
        Maps the field keys of the Pydantic model into the openBIS Excel style headers.
        """
        return {
            field_name: _format_excel_header(field_name)
            for field_name in self.model_fields.keys()
            if field_name not in _EXCLUDED_EXCEL_HEADER_FIELDS
        }

    @property
    def openbis_description(self) -> str:
        """Return the description in the format expected by openBIS."""
        return _combine_translations(self.description, self.description_de)

    @model_validator(mode="after")
    @classmethod
    def model_id(cls, data: Any) -> Any:
        """
        Populate `id` based on the entity code and entity type.

        Args:
            data (Any): The data containing the fields values to validate.

        Returns:
            Any: The data with the validated fields.
        """
        data.id = code_to_class_name(
            code=data.code,
            entity_type=_entity_type_for_model_id(data.name),
        )
        return data


class BaseObjectTypeDef(EntityDef):
    """
    Definition class used for the common fields for `CollectionTypeDef`, `ObjectTypeDef`, and `DatasetTypeDef`.
    It adds the fields of `validation_script`.
    """

    validation_script: str | None = Field(
        default=None,
        description="""
        Script written in Jython used to validate the object type.
        """,
    )


class CollectionTypeDef(BaseObjectTypeDef):
    """
    Definition class for a collection type. E.g.:

    ```python
    class DefaultExperiment(BaseModel):
        defs = CollectionTypeDef(
            code='DEFAULT_EXPERIMENT',
            description='...',
            validation_script='DEFAULT_EXPERIMENT.date_range_validation',
        )
    ```
    """

    pass


class DatasetTypeDef(BaseObjectTypeDef):
    """
    Definition class for a data set type. E.g.:

    ```python
    class RawData(BaseModel):
        defs = DatasetTypeDef(
            code='RAW_DATA',
            description='...',
        )
    """

    # TODO add descriptions for `main_dataset_pattern` and `main_dataset_path`

    main_dataset_pattern: str | None = Field(
        default=None,
        description="""""",
    )

    main_dataset_path: str | None = Field(
        default=None,
        description="""""",
    )


class ObjectTypeDef(BaseObjectTypeDef):
    """
    Definition class for an object type. It adds the fields of `generated_code_prefix`, `auto_generate_codes`,
    and `validation_script` to the common attributes of a base object type definition. E.g.:

    ```python
    class Instrument(BaseModel):
        defs = ObjectTypeDef(
            code='INSTRUMENT',
            description='
            Measuring Instrument//Messger\u00e4t
            ',
            generated_code_prefix='INS',
        )
    ```
    """

    generated_code_prefix: str | None = Field(
        default=None,
        description="""
        A short prefix for the defined object type, e.g. 'CHEM'. If not specified, it is defined
        using the first 3 characters of `code`.
        """,
    )

    auto_generate_codes: bool = Field(
        True,
        description="""
        Boolean used to generate codes using `generated_code_prefix` plus a unique number. Set to
        True by default.
        """,
    )

    @model_validator(mode="after")
    @classmethod
    def model_validator_after_init(cls, data: Any) -> Any:
        """
        Ensure `generated_code_prefix` is set after initialization.

        Args:
            data (Any): The data containing the fields values to validate.

        Returns:
            Any: The data with the validated fields.
        """
        # If `generated_code_prefix` is not set, use the first 3 characters of `code`
        if not data.generated_code_prefix:
            data.generated_code_prefix = data.code[:3]

        return data


class PropertyTypeDef(EntityDef):
    """
    Definition class for a property type. It adds the fields of `property_label`, `data_type`,
    `vocabulary_code`, `metadata`, `dynamic_script`, and `multivalued` to the common attributes of
    an entity definition.

    This class is used as an abstract layer for `PropertyTypeAssignment`, as in openBIS a PropertyType
    definition has less fields than when it is actually assigned to an entity type.
    """

    property_label: str = Field(
        ...,
        description="""
        Label that appears in the inventory view. This is the human-readable text for the property
        type definition, and it typically coincides with the `code`, e.g., `'Monitoring date'` for the
        `MONITORING_DATE` property type.
        """,
    )

    property_label_de: str | None = Field(
        default=None,
        description="Optional German label of the property.",
    )

    units: str | None = Field(
        default=None,
        description="""
        Optional units for the property type, expressed in pint format. Read more about pint
        units in https://github.com/hgrecco/pint/blob/master/pint/default_en.txt.

        When provided, the `property_label` is automatically suffixed with `in [units]` unless
        it already contains a units suffix in square brackets (legacy feature).
        """,
    )

    data_type: DataType = Field(
        ...,
        description="""
        The data type of the property, i.e., if it is an integer, float, string, etc. The allowed
        data types in openBIS are:
            - `BOOLEAN`
            - `CONTROLLEDVOCABULARY`
            - `DATE`
            - `HYPERLINK`
            - `INTEGER`
            - `MATERIAL`
            - `MULTILINE_VARCHAR`
            - `OBJECT`
            - `SAMPLE`
            - `REAL`
            - `TIMESTAMP`
            - `VARCHAR`
            - `XML`

        These are defined as an enumeration in the `DataType` class.

        Read more in https://openbis.readthedocs.io/en/latest/uncategorized/register-master-data-via-the-admin-interface.html#data-types-available-in-openbis.
        """,
    )

    vocabulary_code: str | None = Field(
        default=None,
        description="""
        String identifying the controlled vocabulary used for the data type of the property. This is
        thus only relevant if `data_type == 'CONTROLLEDVOCABULARY'`.
        """,
    )

    object_code: str | None = Field(
        default=None,
        description="""
        String identifying the object type used for the data type of the property. This is only
        relevant if `data_type == 'OBJECT'`.
        """,
    )

    # TODO add descriptions for `dynamic_script`

    metadata: dict | None = Field(
        default=None,
        description="""
        General metadata written in a dictionary format. This is used to store additional information
        about the property type, e.g., `{'unit': 'm', 'precision': 2}`.
        """,
    )

    dynamic_script: str | None = Field(
        default=None,
        description="""""",
    )

    ordinal: int | None = Field(
        default=None,
        description="""
        Ordinal of the property type. This is used to order the properties in the inventory view
        """,
    )

    @field_validator("units")
    @classmethod
    def validate_units(cls, value: str | None) -> str | None:
        """
        Validate the optional units string using pint's unit registry.

        Args:
            value: Units string in pint format, or None.

        Returns:
            The validated units string (or None).

        Raises:
            ValueError: If the units string is not recognized by pint.
        """
        if value is None:
            return value
        try:
            _UNIT_REGISTRY.Unit(value)
        except (UndefinedUnitError, DefinitionSyntaxError) as exc:
            raise ValueError(f"Invalid units format: {value}") from exc
        return value

    @property
    def openbis_property_label(self) -> str:
        return _combine_translations(self.property_label, self.property_label_de)

    @model_validator(mode="after")
    @classmethod
    def apply_units_to_property_label(cls, data: Any) -> Any:
        """
        Enforce the `in [units]` suffix in `property_label` when units are provided.

        If the label already contains a bracketed unit, it must include the
        exact `in [units]` format or validation fails. Otherwise, the suffix
        is appended.

        Args:
            data (Any): The data containing the fields values to validate.

        Returns:
            Any: The data with the updated label (if needed).

        Raises:
            ValueError: If a bracketed unit exists without the `in [units]` suffix.
        """
        if data.units:
            if _UNIT_LABEL_PATTERN.search(data.property_label):
                if not _UNIT_SUFFIX_PATTERN.search(data.property_label):
                    raise ValueError(
                        "property_label with units must include 'in [units]'"
                    )
            else:
                data.property_label += f" in [{data.units}]"
        return data


class PropertyTypeAssignment(PropertyTypeDef):
    """
    Base class used to define properties inside `ObjectType`, `CollectionType`, or `DatasetType`.
    This is used to construct these types by assigning property types to them. It adds the fields
    of `mandatory`, `show_in_edit_views`, `section`, `unique`, and `internal_assignment` to the common
    attributes of a property type definition. E.g.:

    ```python
    class Instrument(ObjectType):
        defs = ObjectTypeDef(
            code='INSTRUMENT',
            description='
            Measuring Instrument//Messger\u00e4t
            ',
            generated_code_prefix='INS',
        )

        alias = PropertyTypeAssignment(
            code='ALIAS',
            data_type='VARCHAR',
            property_label='Alternative name',
            description='
            e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname//z.B. Abkürzung oder Spitzname
            ',
            mandatory=False,
            show_in_edit_views=True,
            section='General information',
        )

        # ... other property type assignments here ...
    ```
    """

    mandatory: bool = Field(
        ...,
        description="""
        If `True`, the property is mandatory and has to be set during instantiation of the object type.
        If `False`, the property is optional.
        """,
    )

    show_in_edit_views: bool = Field(
        True,
        description="""
        If `True`, the property is shown in the edit views of the ELN in the object type instantiation.
        If `False`, the property is hidden.
        Set to `True` by default.
        """,
    )

    section: str = Field(
        ...,
        description="""
        Section to which the property type belongs to. E.g., `'General Information'`.
        """,
    )

    # TODO add descriptions for `unique` and `internal_assignment`

    unique: str | None = Field(
        default=None,
        description="""""",
    )

    internal_assignment: str | None = Field(
        default=None,
        description="""""",
    )


class VocabularyTypeDef(EntityDef):
    """
    Definition class for a vocabulary type. It adds the fields of `url_template` to the common attributes of
    an entity definition. E.g.:

    ```python
    class DocumentType(VocabularyType):
        defs = VocabularyTypeDef(
            code='DOCUMENT_TYPE',
            description='Document type//Dokumententypen',
        )
    ```
    """

    # TODO add descriptions for `url_template`

    url_template: str | None = Field(
        default=None,
        description="""""",
    )


class VocabularyTerm(VocabularyTypeDef):
    """
    Base class used to define terms inside a `VocabularyType`. This is used to construct the vocabulary types
    by assigning vocabulary terms to them. It adds the fields of `label` and `official` to the common attributes
    of a vocabulary type definition. E.g.:

    ```python
    class DocumentType(VocabularyType):
        defs = VocabularyTypeDef(
            code='DOCUMENT_TYPE',
            description='Document type//Dokumententypen',
        )

        acceptance_certificate = VocabularyTerm(
            code='ACCEPTANCE_CERTIFICATE',
            label='Acceptance Certificate',
            description='Acceptance Certificate//Abnahmezeugnis',
        )

        calibration_certificate = VocabularyTerm(
            code='CALIBRATION_CERTIFICATE',
            label='Calibration Certificate',
            description='Calibration Certificate//Kalibrierschein',
        )

        # ... other vocabulary term definitions here ...
    """

    # TODO add descriptions for `label` and `official`

    label: str = Field(
        ...,
        description="""""",
    )

    label_de: str | None = Field(
        default=None,
        description="Optional German label of the vocabulary term.",
    )

    official: bool = Field(
        True,
        description="""""",
    )

    @field_validator("code")
    @classmethod
    def validate_code_length(cls, value: str) -> str:
        if len(value) > 50:
            raise ValueError(
                f"VocabularyTerm code must not exceed 50 characters (got {len(value)} characters)."
            )
        return value

    @property
    def openbis_label(self) -> str:
        return _combine_translations(self.label, self.label_de)
