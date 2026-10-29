"""
Reference mapping between DRMD XML documents and the DRMD masterdata objects.

`xml_to_graph()` reads a Digital Reference Material Document (drmd.xsd v1.0.0) into objects of
the types defined in `bam_masterdata/datamodel/drmd/`, and `graph_to_xml()` writes such objects
back into a DRMD document. Both functions implement the mapping table documented in
`bam_masterdata/datamodel/drmd/README.md`. The tests use them to show that the datamodel holds
every element of a DRMD document, and a certificate generator can follow `graph_to_xml()`.

Conventions (see README.md for the full list):

- Repeating XML elements are separate objects linked as openBIS parents of the object that
  contains them ("component -> container"), ordered by `DRMD_POSITION`.
- Text is stored in the primary language of the document (`DRMD.DRMD_LANGUAGE`); every other
  language is stored in a `DRMD_TRANSLATION` parent that names the property it translates.
- Embedded files are `DRMD_FILE` parents; the file itself is a dataset of that object.
- Controlled vocabulary terms keep the exact XML token in their label.
"""

from __future__ import annotations

import base64
import datetime
import decimal
import difflib
import math
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from decimal import Decimal
from pathlib import Path

from bam_masterdata.datamodel.drmd.object_types import (
    Drmd,
    DrmdFile,
    DrmdIdentifier,
    DrmdMaterialClass,
    DrmdMetadata,
    DrmdProcedure,
    DrmdProducer,
    DrmdPropertySet,
    DrmdQuantity,
    DrmdRespPerson,
    DrmdResult,
    DrmdStatement,
    DrmdTranslation,
    ReferenceMaterial,
)
from bam_masterdata.datamodel.drmd.vocabularies import (
    DrmdConformity,
    DrmdDocumentTitle,
    DrmdRefType,
    DrmdUncertaintyType,
)
from bam_masterdata.metadata.definitions import PropertyTypeAssignment
from bam_masterdata.metadata.entities import CollectionType, ObjectType

DRMD_NS = "urn:drmd:schema"
DCC_NS = "https://ptb.de/dcc"
SI_NS = "https://ptb.de/si"
DS_NS = "http://www.w3.org/2000/09/xmldsig#"
XSI_NS = "http://www.w3.org/2001/XMLSchema-instance"
NS = {"drmd": DRMD_NS, "dcc": DCC_NS, "si": SI_NS, "ds": DS_NS}

for _prefix, _uri in NS.items():
    ET.register_namespace(_prefix, _uri)


class UnsupportedContentError(ValueError):
    """Raised for DRMD content that the datamodel cannot hold without changing its meaning."""


def q(name: str) -> str:
    """Convert a prefixed name such as 'dcc:content' into ElementTree notation."""
    prefix, local = name.split(":")
    return f"{{{NS[prefix]}}}{local}"


# The value choice of dcc:primitiveQuantityType (supporting/dcc.xsd), which drmd:quantity,
# dcc:itemQuantity and dcc:usedMethodQuantity share
VALUE_CHOICE = (
    "dcc:noQuantity",
    "dcc:charsXMLList",
    "si:real",
    "si:hybrid",
    "si:complex",
    "si:constant",
    "si:realListXMLList",
    "si:complexListXMLList",
)


def unsupported_value_message(path: str) -> str:
    """Explain why the value element at `path` cannot be imported."""
    name = path.rsplit("/", 1)[-1]
    if name in VALUE_CHOICE:
        # valid DRMD, but the datamodel has no properties for it (README, section 13)
        return f"{path} is not modelled"
    local = name.split(":")[-1]
    expected = [choice for choice in VALUE_CHOICE if choice.split(":")[1] == local]
    if expected:
        return (
            f"{path} is not allowed by drmd.xsd: the value element must be "
            f"{expected[0]} (namespace {NS[expected[0].split(':')[0]]})"
        )
    return (
        f"{path} is not allowed by drmd.xsd: the value element must be one of "
        + ", ".join(VALUE_CHOICE)
    )


def local_name(tag: str) -> str:
    return tag.split("}")[1] if "}" in tag else tag


def _label_to_code(vocabulary) -> dict[str, str]:
    return {term.label: term.code for term in vocabulary().terms}


def _code_to_label(vocabulary) -> dict[str, str]:
    return {term.code: term.label for term in vocabulary().terms}


TITLE_CODE = _label_to_code(DrmdDocumentTitle)
TITLE_LABEL = _code_to_label(DrmdDocumentTitle)
REF_TYPE_CODE = _label_to_code(DrmdRefType)
REF_TYPE_LABEL = _code_to_label(DrmdRefType)
CONFORMITY_CODE = _label_to_code(DrmdConformity)
CONFORMITY_LABEL = _code_to_label(DrmdConformity)
UNCERTAINTY_LABEL = _code_to_label(DrmdUncertaintyType)

# Named statements of drmd:statements, in schema order: XML element -> DRMD property attribute
STATEMENT_PROPERTIES = [
    ("intendedUse", "drmd_intended_use"),
    ("commutability", "drmd_commutability"),
    ("storageInformation", "drmd_storage_information"),
    ("instructionsForHandlingAndUse", "drmd_handling_instructions"),
    ("metrologicalTraceability", "drmd_metrological_traceability"),
    ("healthAndSafetyInformation", "drmd_health_and_safety"),
    ("subcontractors", "drmd_subcontractors"),
    ("legalNotice", "drmd_legal_notice"),
    ("referenceToCertificationReport", "drmd_certification_report"),
]

# Address elements of dcc:locationType (an unordered choice), in the order they are written
ADDRESS_PROPERTIES = [
    ("street", "drmd_street"),
    ("streetNo", "drmd_street_no"),
    ("postOfficeBox", "drmd_post_office_box"),
    ("postCode", "drmd_post_code"),
    ("city", "drmd_city"),
    ("state", "drmd_state"),
    ("countryCode", "drmd_country_code"),
]

CONTACT_PROPERTIES = [
    ("eMail", "email"),
    ("phone", "telephone"),
    ("fax", "drmd_fax"),
    ("link", "homepage"),
]

CRYPT_PROPERTIES = [
    ("cryptElectronicSeal", "drmd_electronic_seal"),
    ("cryptElectronicSignature", "drmd_electronic_signature"),
    ("cryptElectronicTimeStamp", "drmd_electronic_timestamp"),
]

# Elements of dcc:statementMetaDataType not held by the datamodel (README.md, section 13)
METADATA_NOT_MODELLED = [
    "countryCodeISO3166_1",
    "validXMLList",
    "respAuthority",
    "conformityXMLList",
    "data",
    "location",
]


# ---------------------------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------------------------


def value(obj: ObjectType, attr: str):
    """Return the value of an assigned property, or None when it is not set or not assigned."""
    result = getattr(obj, attr, None)
    return None if isinstance(result, PropertyTypeAssignment) else result


def property_code(obj: ObjectType, attr: str) -> str:
    return obj._property_metadata[attr].code


def normalize_text(text: str | None) -> str:
    """Collapse layout whitespace of XML text while keeping paragraph breaks."""
    if not text:
        return ""
    paragraphs = re.split(r"\n\s*\n", text.strip())
    return "\n\n".join(" ".join(p.split()) for p in paragraphs if p.strip())


def tokens(text: str | None) -> list[str]:
    return (text or "").split()


def _bool(text: str) -> bool:
    return text.strip() in ("true", "1")


def _xml_bool(flag: bool) -> str:
    return "true" if flag else "false"


def _decimal_text(number: Decimal) -> str:
    sign, digits, _ = number.as_tuple()
    adjusted = number.adjusted()
    if number.is_zero() or -5 < adjusted < 7:
        return format(number, "f")
    mantissa = "".join(str(d) for d in digits)
    if len(mantissa) > 1:
        mantissa = f"{mantissa[0]}.{mantissa[1:]}"
    return f"{'-' if sign else ''}{mantissa}e{adjusted}"


def format_decimal(
    number: float | None, significant_digit: int | None = None
) -> str | None:
    """Write a float in the D-SI decimal format (si:decimalType).

    The shortest text that reads back as the same float is used. If `significant_digit`
    (si:significantDigit, the power of ten of the last significant digit) is given, trailing
    zeros are added up to that digit, e.g. 0.5 with -2 gives "0.50". Digits are never removed,
    so a stored value is never rounded. Very large and very small magnitudes are written with
    an exponent, e.g. 1.03e9.
    """
    if number is None:
        return None
    if math.isnan(number):
        return "NaN"
    if math.isinf(number):
        raise ValueError("D-SI does not allow infinite values")
    with decimal.localcontext() as context:
        context.prec = 100
        exact = Decimal(repr(float(number))).normalize()
        if (
            significant_digit is not None
            and exact.as_tuple().exponent > significant_digit
        ):
            exact = exact.quantize(Decimal(1).scaleb(significant_digit))
        return _decimal_text(exact)


def format_plain(number: float | None) -> str | None:
    """Write a float without exponent (si:kValueType and si:probabilityValueType)."""
    if number is None:
        return None
    if math.isnan(number):
        return "NaN"
    with decimal.localcontext() as context:
        context.prec = 100
        return format(Decimal(repr(float(number))).normalize(), "f")


TIMESTAMP = re.compile(
    r"(\d{4}-\d{2}-\d{2})[ T](\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?)\s*(Z|[+-]\d{2}:?\d{2})?"
)


def format_timestamp(stamp: str | datetime.datetime) -> str:
    """Write an openBIS TIMESTAMP value as xs:dateTime."""
    if isinstance(stamp, datetime.datetime):
        return stamp.isoformat()
    match = TIMESTAMP.fullmatch(str(stamp).strip())
    if match is None:
        raise ValueError(f"{stamp!r} is not a date and time")
    day, time, zone = match.groups()
    if len(time) == 5:
        time += ":00"
    if zone and zone != "Z" and ":" not in zone:
        zone = f"{zone[:3]}:{zone[3:]}"
    return f"{day}T{time}{zone or ''}"


# ---------------------------------------------------------------------------------------------
# The object graph
# ---------------------------------------------------------------------------------------------


@dataclass
class DrmdGraph:
    """The objects of one DRMD document and their parent links.

    `files` holds the content of embedded files by object id when they are not (yet) stored
    as datasets; a `DRMD_FILE` object with a dataset path in `datasets` takes that file instead.
    """

    collection: CollectionType
    document_id: str
    warnings: list[str] = field(default_factory=list)
    files: dict[str, bytes] = field(default_factory=dict)

    def obj(self, object_id: str) -> ObjectType:
        return self.collection.attached_objects[object_id]

    def parents(self, object_id: str, object_class: type | None = None) -> list[str]:
        """Parents of an object, ordered by DRMD_POSITION and then by insertion order."""
        order = {oid: i for i, oid in enumerate(self.collection.attached_objects)}
        found = set()
        for parent_id, child_id in self.collection.relationships.values():
            if child_id != object_id:
                continue
            if (
                object_class is not None
                and type(self.obj(parent_id)) is not object_class
            ):
                continue
            found.add(parent_id)

        def key(oid: str):
            position = value(self.obj(oid), "drmd_position")
            return (position if position is not None else math.inf, order[oid])

        return sorted(found, key=key)

    def children(self, object_id: str, object_class: type | None = None) -> list[str]:
        found = []
        for parent_id, child_id in self.collection.relationships.values():
            if parent_id == object_id and (
                object_class is None or type(self.obj(child_id)) is object_class
            ):
                found.append(child_id)
        return found

    @property
    def document(self) -> Drmd:
        return self.obj(self.document_id)

    def translations(self, object_id: str) -> dict[str, dict[str, str]]:
        """Translations of an object as {property code: {language: text}}."""
        result: dict[str, dict[str, str]] = {}
        for tid in self.parents(object_id, DrmdTranslation):
            translation = self.obj(tid)
            result.setdefault(value(translation, "drmd_target_property"), {})[
                value(translation, "drmd_language")
            ] = value(translation, "drmd_translated_text")
        return result

    def files_of(self, object_id: str, target: str | None) -> list[str]:
        """DRMD_FILE parents of an object that belong to the given property code (None: own files)."""
        return [
            fid
            for fid in self.parents(object_id, DrmdFile)
            if (value(self.obj(fid), "drmd_target_property") or None) == target
        ]

    def file_bytes(self, file_id: str) -> bytes | None:
        datasets = self.obj(file_id).datasets
        if len(datasets) > 1:
            raise ValueError(f"DRMD_FILE {file_id} must hold exactly one file")
        if datasets:
            return Path(datasets[0]).read_bytes()
        return self.files.get(file_id)


# ---------------------------------------------------------------------------------------------
# XML -> objects
# ---------------------------------------------------------------------------------------------


class _Importer:
    def __init__(self, root: ET.Element, bam_oe: str, file_dir: str | Path | None):
        if root.tag != q("drmd:digitalReferenceMaterialDocument"):
            raise UnsupportedContentError(
                f"the root element is {root.tag}, but a DRMD 1.0.0 document starts with "
                f"{q('drmd:digitalReferenceMaterialDocument')}; validate the file with "
                "tools/validate.py of the DRMD schema repository"
            )
        self.root = root
        self.bam_oe = bam_oe
        self.file_dir = Path(file_dir) if file_dir is not None else None
        self.collection = CollectionType()
        self.warnings: list[str] = []
        self.files: dict[str, bytes] = {}
        self.consumed: set[tuple[int, str]] = set()
        self.parent_map = {child: parent for parent in root.iter() for child in parent}
        first = root.find(
            "drmd:administrativeData/drmd:referenceMaterialProducer/drmd:name/dcc:content",
            NS,
        )
        self.language = first.get("lang") if first is not None else None

    # -- generic helpers ---------------------------------------------------------------------

    def add(self, obj: ObjectType) -> str:
        object_id = self.collection.add(obj)
        obj.code = object_id
        return object_id

    def link(self, parent_id: str, child_id: str) -> None:
        self.collection.add_relationship(parent_id, child_id)

    def attr(self, element: ET.Element, name: str) -> str | None:
        """Read an attribute and record it as imported."""
        self.consumed.add((id(element), name))
        return element.get(name)

    def path(self, element: ET.Element) -> str:
        prefixes = {f"{{{uri}}}": prefix for prefix, uri in NS.items()}
        names = []
        while element is not None:
            namespace = element.tag[: element.tag.find("}") + 1]
            prefix = prefixes.get(namespace)
            names.append(
                f"{prefix}:{local_name(element.tag)}" if prefix else element.tag
            )
            element = self.parent_map.get(element)
        return "/" + "/".join(reversed(names))

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def skip(self, element: ET.Element, message: str | None) -> None:
        """Report an element that is not imported; its attributes need no separate report."""
        if message:
            self.warn(message)
        for node in element.iter():
            for name in node.attrib:
                self.consumed.add((id(node), name))

    def child_text(self, element: ET.Element, name: str) -> str | None:
        child = element.find(name, NS)
        if child is None:
            return None
        return (child.text or "").strip()

    def linking(
        self, obj: ObjectType, element: ET.Element, dcc: bool, ref_id: bool = True
    ) -> None:
        """Store @id, @refId and @refType in the "Document Structure" properties."""
        xml_id = self.attr(element, "id")
        if xml_id:
            obj.drmd_xml_id = xml_id.strip()
        if ref_id:
            refs = tokens(self.attr(element, "refId"))
            if refs:
                obj.drmd_xml_ref_id = " ".join(refs)
        ref_type = self.attr(element, "refType")
        if ref_type:
            if dcc:
                obj.drmd_dcc_ref_type = " ".join(ref_type.split())
            else:
                obj.drmd_ref_type = REF_TYPE_CODE[ref_type.strip()]

    def primary(self, element: ET.Element | None) -> str | None:
        """Text of the dcc:content elements in the primary language (None if there is none)."""
        if element is None:
            return None
        return self._split_contents(element)[0]

    def _split_contents(self, element: ET.Element) -> tuple[str | None, dict[str, str]]:
        primary: list[str] = []
        others: dict[str, list[str]] = {}
        contents = element.findall("dcc:content", NS)
        for content in contents:
            lang = self.attr(content, "lang")
            text = normalize_text(content.text)
            if lang is None or lang == self.language:
                primary.append(text)
            else:
                others.setdefault(lang, []).append(text)
        if not primary and contents:
            raise UnsupportedContentError(
                f"{self.path(element)} has no text in the document language {self.language!r}"
            )
        joined = "\n\n".join(primary) if primary else None
        return joined, {k: "\n\n".join(v) for k, v in others.items()}

    def translate(
        self, object_id: str, obj: ObjectType, attr: str, translations: dict[str, str]
    ) -> None:
        for lang, text in translations.items():
            translation = DrmdTranslation(
                drmd_language=lang,
                drmd_target_property=property_code(obj, attr),
                drmd_translated_text=text,
            )
            self.link(self.add(translation), object_id)

    def text(
        self, object_id: str, obj: ObjectType, attr: str, element: ET.Element | None
    ) -> None:
        """Store a dcc:textType element (only dcc:content) in a text property."""
        if element is None:
            return
        primary, translations = self._split_contents(element)
        setattr(obj, attr, primary)
        self.translate(object_id, obj, attr, translations)

    def rich(
        self,
        object_id: str,
        obj: ObjectType,
        attr: str,
        element: ET.Element | None,
        heading_attr: str | None = None,
        formula_attr: str | None = None,
    ) -> None:
        """Store a dcc:richContentType element: text, translations, embedded files.

        A heading (dcc:name) and a LaTeX formula are kept only where the datamodel has a
        property for them (drmd:statement); elsewhere they are reported as not imported.
        """
        if element is None:
            return
        heading = element.find("dcc:name", NS)
        if heading is not None:
            if heading_attr:
                self.text(object_id, obj, heading_attr, heading)
            else:
                self.skip(
                    heading, f"heading dcc:name of {self.path(element)} is not modelled"
                )
        formulas = element.findall("dcc:formula", NS)
        if formulas:
            latex = formulas[0].find("dcc:latex", NS)
            if formula_attr and len(formulas) == 1 and latex is not None:
                setattr(obj, formula_attr, (latex.text or "").strip())
            else:
                self.warn(
                    f"dcc:formula in {self.path(element)} is not modelled "
                    "(one LaTeX formula per drmd:statement is)"
                )
                for formula in formulas:
                    self.skip(formula, None)
        primary, translations = self._split_contents(element)
        if primary is not None:
            setattr(obj, attr, primary)
        self.translate(object_id, obj, attr, translations)
        for position, file in enumerate(element.findall("dcc:file", NS), 1):
            self.link(
                self.byte_data(file, position, property_code(obj, attr)), object_id
            )

    def byte_data(self, element: ET.Element, position: int, target: str | None) -> str:
        """Store a dcc:byteDataType element as DRMD_FILE; the bytes become its dataset."""
        file = DrmdFile(
            drmd_position=position,
            drmd_file_name=self.child_text(element, "dcc:fileName"),
            drmd_mime_type=self.child_text(element, "dcc:mimeType"),
        )
        if target:
            file.drmd_target_property = target
        self.linking(file, element, dcc=True)
        file_id = self.add(file)
        self.text(file_id, file, "name", element.find("dcc:name", NS))
        self.rich(file_id, file, "description", element.find("dcc:description", NS))
        encoded = element.find("dcc:dataBase64", NS).text or ""
        content = base64.b64decode("".join(encoded.split()))
        self.files[file_id] = content
        if self.file_dir is not None:
            path = self.file_dir / file_id / Path(file.drmd_file_name).name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
            file.add_dataset(str(path))
        return file_id

    def lines(self, obj: ObjectType, element: ET.Element, attr: str, tag: str) -> None:
        values = [(e.text or "").strip() for e in element.findall(tag, NS)]
        if values:
            setattr(obj, attr, "\n".join(values))

    # -- document ----------------------------------------------------------------------------

    def run(self) -> DrmdGraph:
        root = self.root
        admin = root.find("drmd:administrativeData", NS)
        core = admin.find("drmd:coreData", NS)
        statements = root.find("drmd:statements", NS)

        producer_id = self.producer(admin.find("drmd:referenceMaterialProducer", NS))
        document = Drmd(
            drmd_schema_version=self.attr(root, "schemaVersion"),
            drmd_document_title=TITLE_CODE[
                self.child_text(core, "drmd:titleOfTheDocument")
            ],
            uuid=self.child_text(core, "drmd:uniqueIdentifier"),
            version=self.child_text(core, "drmd:documentVersion"),
        )
        # the location of the schema is not part of the document content
        self.consumed.add((id(root), f"{{{XSI_NS}}}schemaLocation"))
        if self.language:
            document.drmd_language = self.language
        self.validity(document, core.find("drmd:validity", NS))
        document.drmd_producer = self.collection.attached_objects[producer_id]
        for tag, attr in STATEMENT_PROPERTIES:
            element = statements.find(f"drmd:{tag}", NS)
            text = self.primary(element)
            if text is None and element is not None:
                # a statement that holds only files; mandatory text properties need a value
                if document._property_metadata[attr].mandatory:
                    text = ""
            if text is not None:
                setattr(document, attr, text)
        comment = root.find("drmd:comment", NS)
        if comment is not None:
            document.drmd_comment = normalize_text(comment.text)
        document_id = self.add(document)

        for tag, attr in STATEMENT_PROPERTIES:
            self.rich(document_id, document, attr, statements.find(f"drmd:{tag}", NS))

        for position, element in enumerate(
            core.findall("drmd:documentIdentifiers/drmd:documentIdentifier", NS), 1
        ):
            self.link(self.identifier(element, position), document_id)

        for position, element in enumerate(
            admin.findall("drmd:respPersons/dcc:respPerson", NS), 1
        ):
            self.link(self.resp_person(element, position), document_id)

        material_ids: dict[str, str] = {}
        for position, element in enumerate(
            root.findall("drmd:materials/drmd:material", NS), 1
        ):
            rm_id = self.material(element, position)
            self.link(rm_id, document_id)
            for identifier in element.findall(
                "drmd:materialIdentifiers/drmd:materialIdentifier", NS
            ):
                if identifier.get("id"):
                    material_ids[identifier.get("id").strip()] = rm_id

        for position, element in enumerate(
            root.findall("drmd:propertiesList/drmd:properties", NS), 1
        ):
            self.link(self.property_set(element, position, material_ids), document_id)

        for position, element in enumerate(statements.findall("drmd:statement", NS), 1):
            self.link(self.statement(element, position), document_id)

        for position, element in enumerate(root.findall("drmd:document", NS), 1):
            self.link(self.byte_data(element, position, None), document_id)

        if root.find("ds:Signature", NS) is not None:
            self.warn(
                "ds:Signature is created when the generated document is signed; not imported"
            )
        self.report_unread_attributes()
        return DrmdGraph(self.collection, document_id, self.warnings, self.files)

    def report_unread_attributes(self) -> None:
        signature = self.root.find("ds:Signature", NS)
        skipped = {id(e) for e in signature.iter()} if signature is not None else set()
        for element in self.root.iter():
            if id(element) in skipped:
                continue
            for name in element.attrib:
                if (id(element), name) not in self.consumed:
                    self.warn(
                        f"attribute {name} of {self.path(element)} is not modelled"
                    )

    def validity(self, document: Drmd, element: ET.Element) -> None:
        child = element[0]
        kind = local_name(child.tag)
        if kind == "untilRevoked":
            document.drmd_validity_type = "UNTIL_REVOKED"
        elif kind == "timeAfterDispatch":
            document.drmd_validity_type = "TIME_AFTER_DISPATCH"
            dispatch = self.child_text(child, "drmd:dispatchDate")
            if dispatch:
                document.drmd_dispatch_date = datetime.date.fromisoformat(dispatch)
            document.drmd_period = self.child_text(child, "drmd:period")
        else:
            document.drmd_validity_type = "SPECIFIC_TIME"
            document.date_expiration = datetime.date.fromisoformat(child.text.strip())

    # -- administrative data -----------------------------------------------------------------

    def contact(self, obj: ObjectType, contact: ET.Element) -> None:
        """Contact details and postal address of dcc:contactType / dcc:contactNotStrictType."""
        for tag, attr in CONTACT_PROPERTIES:
            text = self.child_text(contact, f"dcc:{tag}")
            if text is not None:
                setattr(obj, attr, text)
        location = contact.find("dcc:location", NS)
        if location is None:
            return
        for tag, attr in ADDRESS_PROPERTIES:
            found = location.findall(f"dcc:{tag}", NS)
            if len(found) > 1:
                self.warn(
                    f"only the first dcc:{tag} of {self.path(location)} is modelled"
                )
                for extra in found[1:]:
                    self.skip(extra, None)
            if found:
                setattr(obj, attr, (found[0].text or "").strip())
        coordinates = location.find("dcc:positionCoordinates", NS)
        if coordinates is not None:
            self.coordinates(obj, coordinates)

    def contact_files(
        self, object_id: str, obj: ObjectType, contact: ET.Element
    ) -> None:
        location = contact.find("dcc:location", NS)
        if location is not None:
            further = location.findall("dcc:further", NS)
            if len(further) > 1:
                self.warn(
                    f"only the first dcc:further of {self.path(location)} is modelled"
                )
                for extra in further[1:]:
                    self.skip(extra, None)
            if further:
                self.rich(object_id, obj, "drmd_address_further", further[0])
        data = contact.find("dcc:descriptionData", NS)
        if data is not None:
            self.link(self.byte_data(data, 1, None), object_id)

    def coordinates(self, obj: ObjectType, element: ET.Element) -> None:
        system = self.child_text(element, "dcc:positionCoordinateSystem") or ""
        first = element.find("dcc:positionCoordinate1", NS)
        second = element.find("dcc:positionCoordinate2", NS)
        units = {self.child_text(c, "si:unit") for c in (first, second)}
        extra = [
            name
            for name in ("dcc:reference", "dcc:declaration", "dcc:positionCoordinate3")
            if element.find(name, NS) is not None
        ]
        detailed = any(
            child.tag not in (q("si:label"), q("si:value"), q("si:unit"))
            for coordinate in (first, second)
            for child in coordinate
        )
        if system.upper() != "WGS84" or units != {"\\degree"} or extra or detailed:
            self.skip(
                element,
                f"{self.path(element)} is not WGS84 latitude/longitude in \\degree; "
                "not imported",
            )
            return
        obj.drmd_latitude = float(self.child_text(first, "si:value"))
        obj.drmd_longitude = float(self.child_text(second, "si:value"))

    def producer(self, element: ET.Element) -> str:
        contact = element.find("drmd:contact", NS)
        producer = DrmdProducer(
            name=self.primary(element.find("drmd:name", NS)),
            drmd_contact_name=self.primary(contact.find("dcc:name", NS)),
        )
        self.contact(producer, contact)
        for tag, attr in CRYPT_PROPERTIES:
            text = self.child_text(element, f"drmd:{tag}")
            if text is not None:
                setattr(producer, attr, _bool(text))
        producer_id = self.add(producer)
        self.text(producer_id, producer, "name", element.find("drmd:name", NS))
        self.text(
            producer_id, producer, "drmd_contact_name", contact.find("dcc:name", NS)
        )
        self.contact_files(producer_id, producer, contact)
        for position, identifier in enumerate(
            element.findall(
                "drmd:organizationIdentifiers/drmd:organizationIdentifier", NS
            ),
            1,
        ):
            self.link(self.identifier(identifier, position), producer_id)
        return producer_id

    def resp_person(self, element: ET.Element, position: int) -> str:
        person = element.find("dcc:person", NS)
        resp = DrmdRespPerson(
            drmd_position=position, name=self.primary(person.find("dcc:name", NS))
        )
        self.linking(resp, element, dcc=True)
        self.contact(resp, person)
        role = self.child_text(element, "dcc:role")
        if role is not None:
            resp.drmd_role = role
        signer = self.child_text(element, "dcc:mainSigner")
        if signer is not None:
            resp.drmd_main_signer = _bool(signer)
        for tag, attr in CRYPT_PROPERTIES:
            text = self.child_text(element, f"dcc:{tag}")
            if text is not None:
                setattr(resp, attr, _bool(text))
        resp_id = self.add(resp)
        self.text(resp_id, resp, "name", person.find("dcc:name", NS))
        self.contact_files(resp_id, resp, person)
        self.rich(resp_id, resp, "description", element.find("dcc:description", NS))
        return resp_id

    def identifier(self, element: ET.Element, position: int) -> str:
        identifier = DrmdIdentifier(
            drmd_scheme=self.child_text(element, "drmd:scheme"),
            drmd_identifier_value=self.child_text(element, "drmd:value"),
            drmd_position=position,
        )
        link = self.child_text(element, "drmd:link")
        if link is not None:
            identifier.drmd_link = link
        self.linking(identifier, element, dcc=False)
        return self.add(identifier)

    # -- materials ---------------------------------------------------------------------------

    def material(self, element: ET.Element, position: int) -> str:
        rm = ReferenceMaterial(
            drmd_position=position,
            bam_oe=self.bam_oe,
            name=self.primary(element.find("drmd:name", NS)),
        )
        rm_id = self.add(rm)
        self.text(rm_id, rm, "name", element.find("drmd:name", NS))
        self.rich(rm_id, rm, "description", element.find("drmd:description", NS))
        for index, cls in enumerate(element.findall("drmd:materialClass", NS), 1):
            material_class = DrmdMaterialClass(
                drmd_scheme=self.child_text(cls, "drmd:reference"),
                drmd_class_id=self.child_text(cls, "drmd:classID"),
                drmd_position=index,
            )
            link = self.child_text(cls, "drmd:link")
            if link is not None:
                material_class.drmd_link = link
            self.linking(material_class, cls, dcc=False)
            self.link(self.add(material_class), rm_id)
        index = 0
        for container, role in (
            ("drmd:minimumSampleSize", "MINIMUM_SAMPLE_SIZE"),
            ("drmd:itemQuantities", "ITEM_QUANTITIES"),
        ):
            for item in element.findall(f"{container}/dcc:itemQuantity", NS):
                index += 1
                self.link(self.quantity(item, index, role), rm_id)
        for index, identifier in enumerate(
            element.findall("drmd:materialIdentifiers/drmd:materialIdentifier", NS), 1
        ):
            self.link(self.identifier(identifier, index), rm_id)
        return rm_id

    # -- properties --------------------------------------------------------------------------

    def property_set(
        self, element: ET.Element, position: int, material_ids: dict[str, str]
    ) -> str:
        pset = DrmdPropertySet(
            drmd_position=position, name=self.primary(element.find("drmd:name", NS))
        )
        certified = self.attr(element, "isCertified")
        if certified is not None:
            pset.drmd_is_certified = _bool(certified)
        self.linking(pset, element, dcc=False, ref_id=False)
        # @refId pointing at a material identifier becomes a link to the reference material
        # ("Convention B" of the DRMD guidance); any other reference is kept as written
        materials, others = [], []
        for ref in tokens(self.attr(element, "refId")):
            if ref in material_ids:
                if material_ids[ref] not in materials:
                    materials.append(material_ids[ref])
            else:
                others.append(ref)
        if others:
            pset.drmd_xml_ref_id = " ".join(others)
        pset_id = self.add(pset)
        for rm_id in materials:
            self.link(rm_id, pset_id)
        self.text(pset_id, pset, "name", element.find("drmd:name", NS))
        self.rich(pset_id, pset, "description", element.find("drmd:description", NS))
        for index, method in enumerate(
            element.findall("drmd:procedures/dcc:usedMethod", NS), 1
        ):
            self.link(self.procedure(method, index), pset_id)
        for index, result in enumerate(
            element.findall("drmd:results/drmd:result", NS), 1
        ):
            self.link(self.result(result, index), pset_id)
        for index, metadata in enumerate(
            element.findall("drmd:measurementMetaData/dcc:metaData", NS), 1
        ):
            self.link(self.metadata(metadata, index), pset_id)
        return pset_id

    def procedure(self, element: ET.Element, position: int) -> str:
        method = DrmdProcedure(
            drmd_position=position, name=self.primary(element.find("dcc:name", NS))
        )
        self.linking(method, element, dcc=True)
        self.lines(method, element, "drmd_norms", "dcc:norm")
        self.lines(method, element, "reference", "dcc:reference")
        self.lines(method, element, "drmd_links", "dcc:link")
        method_id = self.add(method)
        self.text(method_id, method, "name", element.find("dcc:name", NS))
        self.rich(method_id, method, "description", element.find("dcc:description", NS))
        for index, item in enumerate(
            element.findall("dcc:usedMethodQuantities/dcc:usedMethodQuantity", NS), 1
        ):
            self.link(self.quantity(item, index, "USED_METHOD_QUANTITIES"), method_id)
        return method_id

    def metadata(self, element: ET.Element, position: int) -> str:
        for tag in METADATA_NOT_MODELLED:
            found = element.findall(f"dcc:{tag}", NS)
            if found:
                self.warn(f"dcc:{tag} of {self.path(element)} is not modelled")
                for extra in found:
                    self.skip(extra, None)
        meta = DrmdMetadata(drmd_position=position)
        self.linking(meta, element, dcc=True)
        for tag, attr in (
            ("convention", "drmd_convention"),
            ("period", "drmd_period"),
            ("nonSIDefinition", "drmd_non_si_definition"),
            ("nonSIUnit", "drmd_non_si_unit"),
        ):
            text = self.child_text(element, f"dcc:{tag}")
            if text is not None:
                setattr(meta, attr, normalize_text(text))
        for tag, attr in (("traceable", "drmd_traceable"), ("valid", "drmd_valid")):
            text = self.child_text(element, f"dcc:{tag}")
            if text is not None:
                setattr(meta, attr, _bool(text))
        date = self.child_text(element, "dcc:date")
        if date is not None:
            meta.drmd_metadata_date = datetime.date.fromisoformat(date)
        conformity = self.child_text(element, "dcc:conformity")
        if conformity is not None:
            meta.drmd_conformity = CONFORMITY_CODE[conformity]
        self.lines(meta, element, "drmd_norms", "dcc:norm")
        self.lines(meta, element, "reference", "dcc:reference")
        self.lines(meta, element, "drmd_links", "dcc:link")
        meta_id = self.add(meta)
        self.text(meta_id, meta, "name", element.find("dcc:name", NS))
        self.rich(meta_id, meta, "description", element.find("dcc:description", NS))
        self.rich(
            meta_id, meta, "drmd_declaration", element.find("dcc:declaration", NS)
        )
        return meta_id

    def result(self, element: ET.Element, position: int) -> str:
        data = element.find("drmd:data", NS)
        listed = data.find("drmd:list", NS)
        result = DrmdResult(
            drmd_position=position,
            name=self.primary(element.find("drmd:name", NS)),
            drmd_data_as_list=listed is not None,
        )
        self.linking(result, element, dcc=False)
        result_id = self.add(result)
        self.text(result_id, result, "name", element.find("drmd:name", NS))
        self.rich(
            result_id, result, "description", element.find("drmd:description", NS)
        )
        container = listed if listed is not None else data
        for index, item in enumerate(container.findall("drmd:quantity", NS), 1):
            self.link(self.quantity(item, index, "RESULT_DATA"), result_id)
        return result_id

    def statement(self, element: ET.Element, position: int) -> str:
        statement = DrmdStatement(drmd_position=position)
        self.linking(statement, element, dcc=True)
        statement_id = self.add(statement)
        self.rich(
            statement_id,
            statement,
            "drmd_statement_text",
            element,
            heading_attr="name",
            formula_attr="drmd_formula_latex",
        )
        return statement_id

    # -- quantities --------------------------------------------------------------------------

    def quantity(self, element: ET.Element, position: int, role: str) -> str:
        quantity = DrmdQuantity(drmd_position=position, drmd_quantity_role=role)
        self.linking(quantity, element, dcc=True)
        payload = next(
            child
            for child in element
            if child.tag
            not in (q("dcc:name"), q("dcc:description"), q("drmd:propertyIdentifiers"))
        )
        kind = payload.tag
        if kind == q("si:real"):
            quantity.drmd_value_type = "SI_REAL"
            self.real(quantity, payload)
        elif kind == q("si:constant"):
            quantity.drmd_value_type = "SI_CONSTANT"
            self.constant(quantity, payload)
        elif kind == q("si:hybrid"):
            quantity.drmd_value_type = "SI_HYBRID"
        elif kind == q("si:realListXMLList"):
            quantity.drmd_value_type = "SI_REAL_LIST_XML_LIST"
        elif kind == q("dcc:noQuantity"):
            quantity.drmd_value_type = "DCC_NO_QUANTITY"
        elif kind == q("dcc:charsXMLList"):
            quantity.drmd_value_type = "DCC_CHARS_XML_LIST"
            quantity.drmd_chars_list = " ".join(tokens(payload.text))
        else:
            raise UnsupportedContentError(unsupported_value_message(self.path(payload)))
        quantity_id = self.add(quantity)
        self.text(quantity_id, quantity, "name", element.find("dcc:name", NS))
        self.rich(
            quantity_id, quantity, "description", element.find("dcc:description", NS)
        )
        if kind == q("dcc:noQuantity"):
            self.rich(quantity_id, quantity, "drmd_no_quantity_text", payload)
        elif kind == q("si:hybrid"):
            for index, member in enumerate(payload, 1):
                self.link(self.member(member, index), quantity_id)
        elif kind == q("si:realListXMLList"):
            for member_id in self.real_list(payload):
                self.link(member_id, quantity_id)
        for index, identifier in enumerate(
            element.findall("drmd:propertyIdentifiers/drmd:propertyIdentifier", NS), 1
        ):
            self.link(self.identifier(identifier, index), quantity_id)
        return quantity_id

    def member(self, element: ET.Element, position: int) -> str:
        """A member of si:hybrid: si:real, si:constant or si:realListXMLList."""
        member = DrmdQuantity(drmd_position=position)
        if element.tag == q("si:real"):
            member.drmd_value_type = "SI_REAL"
            self.real(member, element)
            return self.add(member)
        if element.tag == q("si:constant"):
            member.drmd_value_type = "SI_CONSTANT"
            self.constant(member, element)
            return self.add(member)
        if element.tag == q("si:realListXMLList"):
            member.drmd_value_type = "SI_REAL_LIST_XML_LIST"
            member_id = self.add(member)
            for item_id in self.real_list(element):
                self.link(item_id, member_id)
            return member_id
        raise UnsupportedContentError(
            f"{self.path(element)} in si:hybrid is not modelled"
        )

    def si_common(self, quantity: DrmdQuantity, element: ET.Element) -> None:
        for tag, attr in (
            ("si:label", "drmd_si_label"),
            ("si:quantityTypeQUDT", "drmd_quantity_kind"),
            ("si:unit", "drmd_si_unit"),
            ("si:dateTime", "drmd_si_date_time"),
        ):
            text = self.child_text(element, tag)
            if text is not None:
                setattr(quantity, attr, text)
        quantity.drmd_si_value = float(self.child_text(element, "si:value"))
        digit = self.child_text(element, "si:significantDigit")
        if digit is not None:
            quantity.drmd_significant_digit = int(digit)

    def real(self, quantity: DrmdQuantity, element: ET.Element) -> None:
        self.si_common(quantity, element)
        univariate = element.find("si:measurementUncertaintyUnivariate", NS)
        if univariate is not None:
            block = univariate[0]
            kind, fields = {
                "standardMU": ("STANDARD_MU", {"valueStandardMU": "standard"}),
                "expandedMU": ("EXPANDED_MU", {"valueExpandedMU": "expanded"}),
                "coverageIntervalMU": (
                    "COVERAGE_INTERVAL_MU",
                    {"valueStandardMU": "standard"},
                ),
            }[local_name(block.tag)]
            self.uncertainty(quantity, block, kind, fields)
        # deprecated D-SI forms, mapped onto the current ones with the same content
        expanded = element.find("si:expandedUnc", NS)
        if expanded is not None:
            self.uncertainty(
                quantity, expanded, "EXPANDED_MU", {"uncertainty": "expanded"}
            )
        interval = element.find("si:coverageInterval", NS)
        if interval is not None:
            self.uncertainty(
                quantity, interval, "COVERAGE_INTERVAL_MU", {"standardUnc": "standard"}
            )

    def uncertainty(
        self,
        quantity: DrmdQuantity,
        element: ET.Element,
        kind: str,
        value_fields: dict[str, str],
    ) -> None:
        quantity.drmd_uncertainty_type = kind
        for tag, target in value_fields.items():
            setattr(
                quantity,
                f"drmd_{target}_uncertainty",
                float(self.child_text(element, f"si:{tag}")),
            )
        for tag, attr in (
            ("coverageFactor", "drmd_coverage_factor"),
            ("coverageProbability", "drmd_coverage_probability"),
            ("intervalMin", "drmd_interval_min"),
            ("intervalMax", "drmd_interval_max"),
        ):
            text = self.child_text(element, f"si:{tag}")
            if text is not None:
                setattr(quantity, attr, float(text))
        distribution = self.child_text(element, "si:distribution")
        if distribution is not None:
            quantity.drmd_distribution = distribution

    def constant(self, quantity: DrmdQuantity, element: ET.Element) -> None:
        self.si_common(quantity, element)
        # si:uncertainty is the deprecated name of si:valueStandardMU
        standard = self.child_text(element, "si:valueStandardMU")
        if standard is None:
            standard = self.child_text(element, "si:uncertainty")
        if standard is not None:
            quantity.drmd_uncertainty_type = "STANDARD_MU"
            quantity.drmd_standard_uncertainty = float(standard)
        distribution = self.child_text(element, "si:distribution")
        if distribution is not None:
            quantity.drmd_distribution = distribution

    def real_list(self, element: ET.Element) -> list[str]:
        """Split an si:realListXMLList into one member quantity per list element."""
        for unsupported in (
            "si:measurementUncertaintyMultivariateXMLList",
            "si:ellipsoidalRegionXMLList",
            "si:rectangularRegionXMLList",
        ):
            if element.find(unsupported, NS) is not None:
                raise UnsupportedContentError(f"{unsupported} is not modelled")
        values = tokens(self.child_text(element, "si:valueXMLList"))
        count = len(values)

        def column(block: ET.Element, tag: str) -> list[str] | None:
            found = block.find(f"si:{tag}", NS)
            if found is None:
                return None
            items = tokens(found.text)
            # D-SI allows one entry that applies to every list element
            if len(items) == 1 and count > 1:
                return items * count
            if len(items) != count:
                raise UnsupportedContentError(
                    f"si:{tag} has {len(items)} entries for {count} values"
                )
            return items

        columns = {
            "drmd_si_label": column(element, "labelXMLList"),
            "drmd_quantity_kind": column(element, "quantityTypeQUDTXMLList"),
            "drmd_si_unit": column(element, "unitXMLList"),
            "drmd_significant_digit": column(element, "significantDigitXMLList"),
            "drmd_si_date_time": column(element, "dateTimeXMLList"),
        }
        kind, block, value_tag = None, None, None
        univariate = element.find("si:measurementUncertaintyUnivariateXMLList", NS)
        if univariate is not None:
            block = univariate[0]
            kind, value_tag = {
                "standardMUXMLList": ("STANDARD_MU", "valueStandardMUXMLList"),
                "expandedMUXMLList": ("EXPANDED_MU", "valueExpandedMUXMLList"),
                "coverageIntervalMUXMLList": (
                    "COVERAGE_INTERVAL_MU",
                    "valueStandardMUXMLList",
                ),
            }[local_name(block.tag)]
        # deprecated D-SI forms
        for tag, (deprecated_kind, deprecated_value_tag) in {
            "expandedUncXMLList": ("EXPANDED_MU", "uncertaintyXMLList"),
            "coverageIntervalXMLList": ("COVERAGE_INTERVAL_MU", "standardUncXMLList"),
        }.items():
            found = element.find(f"si:{tag}", NS)
            if found is not None:
                block, kind, value_tag = found, deprecated_kind, deprecated_value_tag
        uncertainty: dict[str, list[str] | None] = {}
        if block is not None:
            target = (
                "drmd_expanded_uncertainty"
                if kind == "EXPANDED_MU"
                else "drmd_standard_uncertainty"
            )
            uncertainty[target] = column(block, value_tag)
            for tag, attr in (
                ("coverageFactorXMLList", "drmd_coverage_factor"),
                ("coverageProbabilityXMLList", "drmd_coverage_probability"),
                ("intervalMinXMLList", "drmd_interval_min"),
                ("intervalMaxXMLList", "drmd_interval_max"),
                ("distributionXMLList", "drmd_distribution"),
            ):
                uncertainty[attr] = column(block, tag)

        member_ids = []
        for index in range(count):
            member = DrmdQuantity(drmd_position=index + 1, drmd_value_type="SI_REAL")
            member.drmd_si_value = float(values[index])
            for attr, items in columns.items():
                if items is not None:
                    item = items[index]
                    setattr(
                        member,
                        attr,
                        int(item) if attr == "drmd_significant_digit" else item,
                    )
            if kind:
                member.drmd_uncertainty_type = kind
                for attr, items in uncertainty.items():
                    if items is not None:
                        item = items[index]
                        setattr(
                            member,
                            attr,
                            item if attr == "drmd_distribution" else float(item),
                        )
            member_ids.append(self.add(member))
        return member_ids


def xml_to_graph(
    source: str | Path | bytes, bam_oe: str, file_dir: str | Path | None = None
) -> DrmdGraph:
    """Read a DRMD document into DRMD masterdata objects.

    The document is expected to be valid against drmd.xsd; validate it first.

    Args:
        source: Path to the XML file, or the XML document as bytes.
        bam_oe: BAM organisational entity of the reference material (mandatory in SAMPLE).
        file_dir: Folder in which embedded files are written and attached to their `DRMD_FILE`
            object as dataset paths. Without it, the files are kept in `DrmdGraph.files`.

    Returns:
        The objects and their links. `warnings` lists every part of the document that the
        datamodel does not hold (see README.md, section 13 "Scope").
    """
    if isinstance(source, bytes):
        root = ET.fromstring(source)
    else:
        root = ET.parse(source).getroot()
    return _Importer(root, bam_oe, file_dir).run()


# ---------------------------------------------------------------------------------------------
# objects -> XML
# ---------------------------------------------------------------------------------------------


class _Exporter:
    def __init__(self, graph: DrmdGraph):
        self.graph = graph
        self.document = graph.document
        self.language = value(self.document, "drmd_language")
        self.xml_ids: dict[str, str] = {}
        self.material_anchor: dict[str, str] = {}
        self.assign_ids()

    def assign_ids(self) -> None:
        """Collect the given XML IDs and create the anchors needed for properties/@refId.

        A properties block refers to its reference material through an identifier of that
        material, because drmd:material has no @id. The first identifier of the material that
        already has an XML ID is used; otherwise the first identifier gets the ID "matid_<n>".
        """
        graph = self.graph
        for object_id, obj in graph.collection.attached_objects.items():
            xml_id = value(obj, "drmd_xml_id")
            if xml_id:
                self.xml_ids[object_id] = xml_id
        used = set(self.xml_ids.values())
        counter = 0
        for pset_id in graph.parents(graph.document_id, DrmdPropertySet):
            for rm_id in graph.parents(pset_id, ReferenceMaterial):
                if rm_id in self.material_anchor:
                    continue
                identifiers = graph.parents(rm_id, DrmdIdentifier)
                if not identifiers:
                    # nothing to refer to; check_graph() reports DRMD-016
                    continue
                named = [i for i in identifiers if i in self.xml_ids]
                if named:
                    anchor = self.xml_ids[named[0]]
                else:
                    counter += 1
                    while f"matid_{counter}" in used:
                        counter += 1
                    anchor = f"matid_{counter}"
                    used.add(anchor)
                    self.xml_ids[identifiers[0]] = anchor
                self.material_anchor[rm_id] = anchor

    # -- generic helpers ---------------------------------------------------------------------

    def sub(self, parent: ET.Element, name: str, text: str | None = None) -> ET.Element:
        element = ET.SubElement(parent, q(name))
        if text is not None:
            element.text = str(text).strip()
        return element

    def opt(self, parent: ET.Element, name: str, text: str | None) -> None:
        """Write an element only if its value is set.

        Missing mandatory values are left out instead of stopping the export, so that the
        XSD and Schematron validation of the generated document name what is missing.
        """
        if text is not None:
            self.sub(parent, name, text)

    def linking(
        self,
        element: ET.Element,
        object_id: str,
        dcc: bool,
        extra_refs: list[str] | None = None,
    ) -> None:
        obj = self.graph.obj(object_id)
        if object_id in self.xml_ids:
            element.set("id", self.xml_ids[object_id])
        refs = list(
            dict.fromkeys((extra_refs or []) + tokens(value(obj, "drmd_xml_ref_id")))
        )
        if refs:
            element.set("refId", " ".join(refs))
        if dcc:
            ref_type = value(obj, "drmd_dcc_ref_type")
            if ref_type:
                element.set("refType", " ".join(ref_type.split()))
        else:
            ref_type = value(obj, "drmd_ref_type")
            if ref_type:
                element.set("refType", REF_TYPE_LABEL[ref_type])

    def contents(self, parent: ET.Element, object_id: str, attr: str) -> None:
        """Write dcc:content elements: primary language first, then the translations.

        Paragraphs (separated by a blank line) are written as separate dcc:content elements.
        """
        obj = self.graph.obj(object_id)
        text = value(obj, attr)
        if text is not None:
            for paragraph in text.split("\n\n"):
                content = self.sub(parent, "dcc:content", paragraph)
                if self.language:
                    content.set("lang", self.language)
        translations = self.graph.translations(object_id).get(
            property_code(obj, attr), {}
        )
        for lang, translated in translations.items():
            for paragraph in translated.split("\n\n"):
                self.sub(parent, "dcc:content", paragraph).set("lang", lang)

    def text_element(
        self, parent: ET.Element, name: str, object_id: str, attr: str
    ) -> ET.Element | None:
        """Write a dcc:textType element."""
        if value(self.graph.obj(object_id), attr) is None:
            return None
        element = self.sub(parent, name)
        self.contents(element, object_id, attr)
        return element

    def rich_element(
        self, parent: ET.Element, name: str, object_id: str, attr: str
    ) -> ET.Element | None:
        """Write a dcc:richContentType element: text, translations and embedded files."""
        obj = self.graph.obj(object_id)
        files = self.graph.files_of(object_id, property_code(obj, attr))
        if value(obj, attr) is None and not files:
            return None
        element = self.sub(parent, name)
        self.contents(element, object_id, attr)
        for file_id in files:
            self.byte_data(element, "dcc:file", file_id)
        return element

    def byte_data(self, parent: ET.Element, name: str, file_id: str) -> None:
        file = self.graph.obj(file_id)
        element = self.sub(parent, name)
        self.linking(element, file_id, dcc=True)
        self.text_element(element, "dcc:name", file_id, "name")
        self.rich_element(element, "dcc:description", file_id, "description")
        self.opt(element, "dcc:fileName", value(file, "drmd_file_name"))
        self.opt(element, "dcc:mimeType", value(file, "drmd_mime_type"))
        content = self.graph.file_bytes(file_id)
        if content is not None:
            self.sub(
                element, "dcc:dataBase64", base64.b64encode(content).decode("ascii")
            )

    def lines(self, parent: ET.Element, obj: ObjectType, attr: str, tag: str) -> None:
        for line in (value(obj, attr) or "").splitlines():
            if line.strip():
                self.sub(parent, tag, line)

    # -- document ----------------------------------------------------------------------------

    def run(self) -> ET.Element:
        graph, document = self.graph, self.document
        doc_id = graph.document_id
        root = ET.Element(q("drmd:digitalReferenceMaterialDocument"))
        if value(document, "drmd_schema_version") is not None:
            root.set("schemaVersion", value(document, "drmd_schema_version"))

        admin = self.sub(root, "drmd:administrativeData")
        core = self.sub(admin, "drmd:coreData")
        self.opt(
            core,
            "drmd:titleOfTheDocument",
            TITLE_LABEL.get(value(document, "drmd_document_title")),
        )
        self.opt(core, "drmd:uniqueIdentifier", value(document, "uuid"))
        self.opt(core, "drmd:documentVersion", value(document, "version"))
        identifiers = graph.parents(doc_id, DrmdIdentifier)
        if identifiers:
            container = self.sub(core, "drmd:documentIdentifiers")
            for identifier_id in identifiers:
                self.identifier(container, "drmd:documentIdentifier", identifier_id)
        if value(document, "drmd_validity_type") is not None:
            self.validity(self.sub(core, "drmd:validity"))
        if value(document, "drmd_producer") is not None:
            self.producer(self.sub(admin, "drmd:referenceMaterialProducer"))
        persons = graph.parents(doc_id, DrmdRespPerson)
        if persons:
            container = self.sub(admin, "drmd:respPersons")
            for person_id in persons:
                self.resp_person(container, person_id)

        container = self.sub(root, "drmd:materials")
        for rm_id in graph.parents(doc_id, ReferenceMaterial):
            self.material(container, rm_id)

        container = self.sub(root, "drmd:propertiesList")
        for pset_id in graph.parents(doc_id, DrmdPropertySet):
            self.property_set(container, pset_id)

        statements = self.sub(root, "drmd:statements")
        for tag, attr in STATEMENT_PROPERTIES:
            self.rich_element(statements, f"drmd:{tag}", doc_id, attr)
        for statement_id in graph.parents(doc_id, DrmdStatement):
            self.statement(statements, statement_id)

        comment = value(document, "drmd_comment")
        if comment is not None:
            self.sub(root, "drmd:comment", comment)
        for file_id in graph.files_of(doc_id, None):
            self.byte_data(root, "drmd:document", file_id)
        return root

    def validity(self, element: ET.Element) -> None:
        document = self.document
        kind = value(document, "drmd_validity_type")
        if kind == "UNTIL_REVOKED":
            self.sub(element, "drmd:untilRevoked", "true")
        elif kind == "TIME_AFTER_DISPATCH":
            after = self.sub(element, "drmd:timeAfterDispatch")
            dispatch = value(document, "drmd_dispatch_date")
            if dispatch is not None:
                self.sub(after, "drmd:dispatchDate", dispatch.isoformat())
            self.opt(after, "drmd:period", value(document, "drmd_period"))
        else:
            expiration = value(document, "date_expiration")
            if expiration is not None:
                self.sub(element, "drmd:specificTime", expiration.isoformat())

    def identifier(self, parent: ET.Element, name: str, identifier_id: str) -> None:
        identifier = self.graph.obj(identifier_id)
        element = self.sub(parent, name)
        self.linking(element, identifier_id, dcc=False)
        self.opt(element, "drmd:scheme", value(identifier, "drmd_scheme"))
        self.opt(element, "drmd:value", value(identifier, "drmd_identifier_value"))
        link = value(identifier, "drmd_link")
        if link:
            self.sub(element, "drmd:link", link)

    def contact(
        self, element: ET.Element, object_id: str, location_required: bool
    ) -> None:
        """Contact details, location and description data of a producer or person."""
        obj = self.graph.obj(object_id)
        for tag, attr in CONTACT_PROPERTIES:
            text = value(obj, attr)
            if text is not None:
                self.sub(element, f"dcc:{tag}", text)
        address = [(tag, value(obj, attr)) for tag, attr in ADDRESS_PROPERTIES]
        further = self.graph.files_of(object_id, "DRMD_ADDRESS_FURTHER")
        latitude = value(obj, "drmd_latitude")
        longitude = value(obj, "drmd_longitude")
        has_location = (
            any(text is not None for _, text in address)
            or value(obj, "drmd_address_further") is not None
            or further
            or (latitude is not None and longitude is not None)
        )
        if has_location or location_required:
            location = self.sub(element, "dcc:location")
            for tag, text in address:
                if text is not None:
                    self.sub(location, f"dcc:{tag}", text)
            self.rich_element(
                location, "dcc:further", object_id, "drmd_address_further"
            )
            if latitude is not None and longitude is not None:
                coordinates = self.sub(location, "dcc:positionCoordinates")
                self.sub(coordinates, "dcc:positionCoordinateSystem", "WGS84")
                for name, number, label in (
                    ("dcc:positionCoordinate1", latitude, "latitude"),
                    ("dcc:positionCoordinate2", longitude, "longitude"),
                ):
                    coordinate = self.sub(coordinates, name)
                    self.sub(coordinate, "si:label", label)
                    self.sub(coordinate, "si:value", format_decimal(number))
                    self.sub(coordinate, "si:unit", "\\degree")
        for file_id in self.graph.files_of(object_id, None):
            self.byte_data(element, "dcc:descriptionData", file_id)

    def producer(self, element: ET.Element) -> None:
        producer = value(self.document, "drmd_producer")
        producer_id = producer.code
        self.text_element(element, "drmd:name", producer_id, "name")
        contact = self.sub(element, "drmd:contact")
        self.text_element(contact, "dcc:name", producer_id, "drmd_contact_name")
        self.contact(contact, producer_id, location_required=True)
        for tag, attr in CRYPT_PROPERTIES:
            flag = value(producer, attr)
            if flag is not None:
                self.sub(element, f"drmd:{tag}", _xml_bool(flag))
        identifiers = self.graph.parents(producer_id, DrmdIdentifier)
        if identifiers:
            container = self.sub(element, "drmd:organizationIdentifiers")
            for identifier_id in identifiers:
                self.identifier(container, "drmd:organizationIdentifier", identifier_id)

    def resp_person(self, parent: ET.Element, person_id: str) -> None:
        resp = self.graph.obj(person_id)
        element = self.sub(parent, "dcc:respPerson")
        self.linking(element, person_id, dcc=True)
        person = self.sub(element, "dcc:person")
        self.text_element(person, "dcc:name", person_id, "name")
        self.contact(person, person_id, location_required=False)
        self.rich_element(element, "dcc:description", person_id, "description")
        role = value(resp, "drmd_role")
        if role is not None:
            self.sub(element, "dcc:role", role)
        signer = value(resp, "drmd_main_signer")
        if signer is not None:
            self.sub(element, "dcc:mainSigner", _xml_bool(signer))
        for tag, attr in CRYPT_PROPERTIES:
            flag = value(resp, attr)
            if flag is not None:
                self.sub(element, f"dcc:{tag}", _xml_bool(flag))

    def material(self, parent: ET.Element, rm_id: str) -> None:
        graph = self.graph
        element = self.sub(parent, "drmd:material")
        self.text_element(element, "drmd:name", rm_id, "name")
        self.rich_element(element, "drmd:description", rm_id, "description")
        for class_id in graph.parents(rm_id, DrmdMaterialClass):
            material_class = graph.obj(class_id)
            cls = self.sub(element, "drmd:materialClass")
            self.linking(cls, class_id, dcc=False)
            self.opt(cls, "drmd:reference", value(material_class, "drmd_scheme"))
            self.opt(cls, "drmd:classID", value(material_class, "drmd_class_id"))
            link = value(material_class, "drmd_link")
            if link:
                self.sub(cls, "drmd:link", link)
        quantities = graph.parents(rm_id, DrmdQuantity)
        for container, role in (
            ("drmd:minimumSampleSize", "MINIMUM_SAMPLE_SIZE"),
            ("drmd:itemQuantities", "ITEM_QUANTITIES"),
        ):
            selected = [
                qid
                for qid in quantities
                if value(graph.obj(qid), "drmd_quantity_role") == role
            ]
            if selected:
                block = self.sub(element, container)
                for quantity_id in selected:
                    self.quantity(block, "dcc:itemQuantity", quantity_id)
        identifiers = graph.parents(rm_id, DrmdIdentifier)
        if identifiers:
            block = self.sub(element, "drmd:materialIdentifiers")
            for identifier_id in identifiers:
                self.identifier(block, "drmd:materialIdentifier", identifier_id)

    def property_set(self, parent: ET.Element, pset_id: str) -> None:
        graph = self.graph
        pset = graph.obj(pset_id)
        element = self.sub(parent, "drmd:properties")
        anchors = [
            self.material_anchor[rm_id]
            for rm_id in graph.parents(pset_id, ReferenceMaterial)
            if rm_id in self.material_anchor
        ]
        self.linking(element, pset_id, dcc=False, extra_refs=anchors)
        certified = value(pset, "drmd_is_certified")
        if certified is not None:
            element.set("isCertified", _xml_bool(certified))
        self.text_element(element, "drmd:name", pset_id, "name")
        self.rich_element(element, "drmd:description", pset_id, "description")
        methods = graph.parents(pset_id, DrmdProcedure)
        if methods:
            block = self.sub(element, "drmd:procedures")
            for method_id in methods:
                self.procedure(block, method_id)
        block = self.sub(element, "drmd:results")
        for result_id in graph.parents(pset_id, DrmdResult):
            self.result(block, result_id)
        metadata = graph.parents(pset_id, DrmdMetadata)
        if metadata:
            block = self.sub(element, "drmd:measurementMetaData")
            for meta_id in metadata:
                self.metadata(block, meta_id)

    def procedure(self, parent: ET.Element, method_id: str) -> None:
        method = self.graph.obj(method_id)
        element = self.sub(parent, "dcc:usedMethod")
        self.linking(element, method_id, dcc=True)
        self.text_element(element, "dcc:name", method_id, "name")
        self.rich_element(element, "dcc:description", method_id, "description")
        self.lines(element, method, "drmd_norms", "dcc:norm")
        self.lines(element, method, "reference", "dcc:reference")
        self.lines(element, method, "drmd_links", "dcc:link")
        quantities = self.graph.parents(method_id, DrmdQuantity)
        if quantities:
            block = self.sub(element, "dcc:usedMethodQuantities")
            for quantity_id in quantities:
                self.quantity(block, "dcc:usedMethodQuantity", quantity_id)

    def metadata(self, parent: ET.Element, meta_id: str) -> None:
        meta = self.graph.obj(meta_id)
        element = self.sub(parent, "dcc:metaData")
        self.linking(element, meta_id, dcc=True)
        self.text_element(element, "dcc:name", meta_id, "name")
        self.rich_element(element, "dcc:description", meta_id, "description")
        convention = value(meta, "drmd_convention")
        if convention is not None:
            self.sub(element, "dcc:convention", convention)
        traceable = value(meta, "drmd_traceable")
        if traceable is not None:
            self.sub(element, "dcc:traceable", _xml_bool(traceable))
        self.lines(element, meta, "drmd_norms", "dcc:norm")
        self.lines(element, meta, "reference", "dcc:reference")
        self.lines(element, meta, "drmd_links", "dcc:link")
        self.rich_element(element, "dcc:declaration", meta_id, "drmd_declaration")
        valid = value(meta, "drmd_valid")
        if valid is not None:
            self.sub(element, "dcc:valid", _xml_bool(valid))
        date = value(meta, "drmd_metadata_date")
        if date is not None:
            self.sub(element, "dcc:date", date.isoformat())
        period = value(meta, "drmd_period")
        if period is not None:
            self.sub(element, "dcc:period", period)
        conformity = value(meta, "drmd_conformity")
        if conformity is not None:
            self.sub(element, "dcc:conformity", CONFORMITY_LABEL[conformity])
        for attr, tag in (
            ("drmd_non_si_definition", "dcc:nonSIDefinition"),
            ("drmd_non_si_unit", "dcc:nonSIUnit"),
        ):
            text = value(meta, attr)
            if text is not None:
                self.sub(element, tag, text)

    def result(self, parent: ET.Element, result_id: str) -> None:
        result = self.graph.obj(result_id)
        element = self.sub(parent, "drmd:result")
        self.linking(element, result_id, dcc=False)
        self.text_element(element, "drmd:name", result_id, "name")
        self.rich_element(element, "drmd:description", result_id, "description")
        data = self.sub(element, "drmd:data")
        quantities = self.graph.parents(result_id, DrmdQuantity)
        if value(result, "drmd_data_as_list") or len(quantities) > 1:
            data = self.sub(data, "drmd:list")
        for quantity_id in quantities:
            self.quantity(data, "drmd:quantity", quantity_id)

    def statement(self, parent: ET.Element, statement_id: str) -> None:
        statement = self.graph.obj(statement_id)
        element = self.sub(parent, "drmd:statement")
        self.linking(element, statement_id, dcc=True)
        self.text_element(element, "dcc:name", statement_id, "name")
        self.contents(element, statement_id, "drmd_statement_text")
        for file_id in self.graph.files_of(statement_id, "DRMD_STATEMENT_TEXT"):
            self.byte_data(element, "dcc:file", file_id)
        formula = value(statement, "drmd_formula_latex")
        if formula is not None:
            self.sub(self.sub(element, "dcc:formula"), "dcc:latex", formula)

    # -- quantities --------------------------------------------------------------------------

    def quantity(self, parent: ET.Element, name: str, quantity_id: str) -> None:
        graph = self.graph
        quantity = graph.obj(quantity_id)
        element = self.sub(parent, name)
        self.linking(element, quantity_id, dcc=True)
        self.text_element(element, "dcc:name", quantity_id, "name")
        self.rich_element(element, "dcc:description", quantity_id, "description")
        kind = value(quantity, "drmd_value_type")
        if kind == "SI_REAL":
            self.real(element, quantity)
        elif kind == "SI_CONSTANT":
            self.constant(element, quantity)
        elif kind == "SI_HYBRID":
            hybrid = self.sub(element, "si:hybrid")
            for member_id in graph.parents(quantity_id, DrmdQuantity):
                member = graph.obj(member_id)
                member_kind = value(member, "drmd_value_type")
                if member_kind == "SI_REAL":
                    self.real(hybrid, member)
                elif member_kind == "SI_CONSTANT":
                    self.constant(hybrid, member)
                else:
                    self.real_list(hybrid, member_id)
        elif kind == "SI_REAL_LIST_XML_LIST":
            self.real_list(element, quantity_id)
        elif kind == "DCC_NO_QUANTITY":
            no_quantity = self.rich_element(
                element, "dcc:noQuantity", quantity_id, "drmd_no_quantity_text"
            )
            if no_quantity is None:
                self.sub(element, "dcc:noQuantity")
        elif kind == "DCC_CHARS_XML_LIST":
            self.sub(
                element, "dcc:charsXMLList", value(quantity, "drmd_chars_list") or ""
            )
        if name == "drmd:quantity":
            identifiers = graph.parents(quantity_id, DrmdIdentifier)
            if identifiers:
                block = self.sub(element, "drmd:propertyIdentifiers")
                for identifier_id in identifiers:
                    self.identifier(block, "drmd:propertyIdentifier", identifier_id)

    def si_common(self, element: ET.Element, quantity: DrmdQuantity) -> int | None:
        digit = value(quantity, "drmd_significant_digit")
        for attr, tag in (
            ("drmd_si_label", "si:label"),
            ("drmd_quantity_kind", "si:quantityTypeQUDT"),
        ):
            text = value(quantity, attr)
            if text is not None:
                self.sub(element, tag, text)
        self.opt(
            element, "si:value", format_decimal(value(quantity, "drmd_si_value"), digit)
        )
        self.opt(element, "si:unit", value(quantity, "drmd_si_unit"))
        if digit is not None:
            self.sub(element, "si:significantDigit", str(digit))
        stamp = value(quantity, "drmd_si_date_time")
        if stamp is not None:
            self.sub(element, "si:dateTime", format_timestamp(stamp))
        return digit

    @staticmethod
    def uncertainty_digit(digit: int | None) -> int | None:
        """Uncertainties are written with at least as many decimals as the value."""
        return digit if digit is not None and digit < 0 else None

    def real(self, parent: ET.Element, quantity: DrmdQuantity) -> None:
        element = self.sub(parent, "si:real")
        digit = self.uncertainty_digit(self.si_common(element, quantity))
        kind = value(quantity, "drmd_uncertainty_type")
        if kind is None:
            return
        univariate = self.sub(element, "si:measurementUncertaintyUnivariate")
        block = self.sub(univariate, f"si:{UNCERTAINTY_LABEL[kind]}")
        if kind == "EXPANDED_MU":
            self.opt(
                block,
                "si:valueExpandedMU",
                format_decimal(value(quantity, "drmd_expanded_uncertainty"), digit),
            )
            self.opt(
                block,
                "si:coverageFactor",
                format_plain(value(quantity, "drmd_coverage_factor")),
            )
        else:
            self.opt(
                block,
                "si:valueStandardMU",
                format_decimal(value(quantity, "drmd_standard_uncertainty"), digit),
            )
            if kind == "COVERAGE_INTERVAL_MU":
                for attr, tag in (
                    ("drmd_interval_min", "si:intervalMin"),
                    ("drmd_interval_max", "si:intervalMax"),
                ):
                    self.opt(block, tag, format_decimal(value(quantity, attr), digit))
        if kind in ("EXPANDED_MU", "COVERAGE_INTERVAL_MU"):
            self.opt(
                block,
                "si:coverageProbability",
                format_plain(value(quantity, "drmd_coverage_probability")),
            )
        distribution = value(quantity, "drmd_distribution")
        if distribution is not None:
            self.sub(block, "si:distribution", distribution)

    def constant(self, parent: ET.Element, quantity: DrmdQuantity) -> None:
        element = self.sub(parent, "si:constant")
        digit = self.uncertainty_digit(self.si_common(element, quantity))
        standard = value(quantity, "drmd_standard_uncertainty")
        if standard is not None:
            self.opt(element, "si:valueStandardMU", format_decimal(standard, digit))
        distribution = value(quantity, "drmd_distribution")
        if distribution is not None:
            self.sub(element, "si:distribution", distribution)

    def real_list(self, parent: ET.Element, quantity_id: str) -> None:
        graph = self.graph
        members = [graph.obj(m) for m in graph.parents(quantity_id, DrmdQuantity)]
        element = self.sub(parent, "si:realListXMLList")

        def column(attr: str, formatter=str) -> str | None:
            values = [value(m, attr) for m in members]
            if all(v is None for v in values):
                return None
            if any(v is None for v in values):
                raise ValueError(
                    f"{attr} must be set for all list elements or for none"
                )
            return " ".join(formatter(v) for v in values)

        def numbers(attr: str) -> str:
            return " ".join(
                format_decimal(
                    value(m, attr),
                    self.uncertainty_digit(value(m, "drmd_significant_digit"))
                    if attr != "drmd_si_value"
                    else value(m, "drmd_significant_digit"),
                )
                for m in members
            )

        text = column("drmd_si_label")
        if text is not None:
            self.sub(element, "si:labelXMLList", text)
        # D-SI types si:quantityTypeQUDTXMLList as one quantity kind for the whole list
        kinds = {value(m, "drmd_quantity_kind") for m in members}
        if kinds != {None}:
            if len(kinds) != 1:
                raise ValueError("all list elements need the same quantity kind")
            self.sub(element, "si:quantityTypeQUDTXMLList", kinds.pop())
        self.sub(element, "si:valueXMLList", numbers("drmd_si_value"))
        self.sub(element, "si:unitXMLList", column("drmd_si_unit"))
        text = column("drmd_significant_digit")
        if text is not None:
            self.sub(element, "si:significantDigitXMLList", text)
        text = column("drmd_si_date_time", format_timestamp)
        if text is not None:
            self.sub(element, "si:dateTimeXMLList", text)
        kinds = {value(m, "drmd_uncertainty_type") for m in members}
        if kinds == {None}:
            return
        if len(kinds) != 1:
            raise ValueError("all list elements need the same uncertainty type")
        kind = kinds.pop()
        univariate = self.sub(element, "si:measurementUncertaintyUnivariateXMLList")
        block = self.sub(univariate, f"si:{UNCERTAINTY_LABEL[kind]}XMLList")
        if kind == "EXPANDED_MU":
            self.sub(
                block, "si:valueExpandedMUXMLList", numbers("drmd_expanded_uncertainty")
            )
            self.sub(
                block,
                "si:coverageFactorXMLList",
                column("drmd_coverage_factor", format_plain),
            )
        else:
            self.sub(
                block, "si:valueStandardMUXMLList", numbers("drmd_standard_uncertainty")
            )
            if kind == "COVERAGE_INTERVAL_MU":
                self.sub(block, "si:intervalMinXMLList", numbers("drmd_interval_min"))
                self.sub(block, "si:intervalMaxXMLList", numbers("drmd_interval_max"))
        if kind in ("EXPANDED_MU", "COVERAGE_INTERVAL_MU"):
            self.sub(
                block,
                "si:coverageProbabilityXMLList",
                column("drmd_coverage_probability", format_plain),
            )
        text = column("drmd_distribution")
        if text is not None:
            self.sub(block, "si:distributionXMLList", text)


def graph_to_xml(graph: DrmdGraph) -> bytes:
    """Write the DRMD masterdata objects of one document as DRMD XML (UTF-8 bytes)."""
    root = _Exporter(graph).run()
    ET.indent(root)
    text = ET.tostring(root, encoding="unicode")
    return f'<?xml version="1.0" encoding="UTF-8"?>\n{text}\n'.encode()


# ---------------------------------------------------------------------------------------------
# Comparing documents
# ---------------------------------------------------------------------------------------------

_NUMBER = re.compile(r"[-+]?(\d+\.?\d*|\.\d+)([eE][-+]?\d+)?")
_BOOLEAN_ELEMENTS = {
    "untilRevoked",
    "mainSigner",
    "cryptElectronicSeal",
    "cryptElectronicSignature",
    "cryptElectronicTimeStamp",
    "traceable",
    "valid",
}


def _normalize_number(token: str) -> str:
    if not _NUMBER.fullmatch(token):
        return token
    with decimal.localcontext() as context:
        context.prec = 100
        return format(Decimal(token).normalize(), "E")


def canonical_form(
    source: str | Path | bytes, skip: tuple[str, ...] = ("ds:Signature",)
) -> list[str]:
    """Outline of a DRMD document for comparison, one line per element.

    Element order is kept. Layout whitespace, the spelling of numbers in D-SI elements
    (1.03e9 = 1030000000), the spelling of booleans (1 = true), line breaks in Base64 data and
    the order of tokens in @refId are normalised, because they do not change the content.
    """
    root = (
        ET.fromstring(source)
        if isinstance(source, bytes)
        else ET.parse(source).getroot()
    )
    skipped = {q(name) for name in skip}
    prefixes = {uri: prefix for prefix, uri in NS.items()}
    lines: list[str] = []

    def label(tag: str) -> str:
        uri, _, local = tag[1:].partition("}")
        return f"{prefixes.get(uri, uri)}:{local}"

    def walk(element: ET.Element, depth: int) -> None:
        if element.tag in skipped:
            return
        local = local_name(element.tag)
        text = " ".join((element.text or "").split())
        if local == "dataBase64":
            text = "".join(text.split())
        elif element.tag.startswith(f"{{{SI_NS}}}"):
            text = " ".join(_normalize_number(t) for t in text.split())
        elif local in _BOOLEAN_ELEMENTS:
            text = {"1": "true", "0": "false"}.get(text, text)
        attributes = []
        for name, attribute in sorted(element.attrib.items()):
            attribute = " ".join(attribute.split())
            if name == "refId":
                attribute = " ".join(sorted(attribute.split()))
            if name == "isCertified":
                attribute = {"1": "true", "0": "false"}.get(attribute, attribute)
            attributes.append(f"@{local_name(name)}={attribute}")
        line = "  " * depth + label(element.tag)
        if attributes:
            line += " [" + " ".join(attributes) + "]"
        if text:
            line += " = " + text
        lines.append(line)
        for child in element:
            if isinstance(child.tag, str):
                walk(child, depth + 1)

    walk(root, 0)
    return lines


def compare_documents(
    original: str | Path | bytes, regenerated: str | Path | bytes
) -> list[str]:
    """Differences between two DRMD documents as unified diff lines (empty if they match)."""
    return list(
        difflib.unified_diff(
            canonical_form(original),
            canonical_form(regenerated),
            "original",
            "regenerated",
            lineterm="",
        )
    )
