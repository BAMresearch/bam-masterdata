"""
Document rules of the DRMD, evaluated on the DRMD masterdata objects.

openBIS checks one object at a time and only knows "mandatory" or "optional". Most DRMD
requirements depend on the document type (reference material certificate or product
information sheet) or involve several objects, so they are checked here on the objects of one
document before an XML document is generated. `check_graph()` reports:

- the rules of drmd-business-rules.sch (identifiers DRMD-nnn, RMC-nnn, PIS-nnn) with the same
  identifier, severity and scope as the Schematron assertion. Each check is written next to the
  XPath it mirrors, so that both can be compared line by line;
- requirements of drmd.xsd and its supporting schemas (DCC, D-SI) that a mandatory flag cannot
  express, e.g. "an expanded uncertainty needs a coverage factor" (identifiers XSD-...); the
  generated document would fail XSD validation;
- conditions for writing the objects unambiguously, e.g. "latitude and longitude only together"
  (identifiers MODEL-...); otherwise values would be left out or could not be read back;
- the D-SI meaning of si:significantDigit (DSI-SIGNIFICANT-DIGIT) and one recommendation of
  the DRMD guidance, the link between properties blocks and materials in documents with
  several materials (BP-MATERIAL-LINK).

The generated XML must still be validated with drmd.xsd and drmd-business-rules.sch; this
module lets a producer see and fix problems in openBIS, where the data is maintained.
"""

from __future__ import annotations

import math
import re
from dataclasses import dataclass
from decimal import Decimal

from bam_masterdata.datamodel.drmd.object_types import (
    DrmdFile,
    DrmdIdentifier,
    DrmdProcedure,
    DrmdPropertySet,
    DrmdQuantity,
    DrmdRespPerson,
    DrmdResult,
    DrmdTranslation,
    ReferenceMaterial,
)
from bam_masterdata.metadata.definitions import DataType
from tests.datamodel.drmd_xml import (
    ADDRESS_PROPERTIES,
    TIMESTAMP,
    DrmdGraph,
    property_code,
    tokens,
    value,
)

ERROR = "error"
CONDITIONAL_ERROR = "conditional-error"
WARNING = "warning"
BLOCKING = (ERROR, CONDITIONAL_ERROR)

CRM = "REFERENCE_MATERIAL_CERTIFICATE"
PIS = "PRODUCT_INFORMATION_SHEET"

SCHEMA_VERSION = re.compile(r"\d+\.\d+\.\d+")
LANGUAGE = re.compile(r"[a-z]{2}")
COUNTRY_CODE = re.compile(r"[A-Z]{2}")
NCNAME = re.compile(r"[A-Za-z_][\w.\-]*")
# xs:duration
DURATION = re.compile(
    r"-?P(?=\d|T\d)(\d+Y)?(\d+M)?(\d+D)?(T(?=\d)(\d+H)?(\d+M)?(\d+(\.\d+)?S)?)?"
)

# Properties of DRMD_QUANTITY that each uncertainty type writes
UNCERTAINTY_FIELDS = {
    None: [],
    "STANDARD_MU": ["drmd_standard_uncertainty"],
    "EXPANDED_MU": [
        "drmd_expanded_uncertainty",
        "drmd_coverage_factor",
        "drmd_coverage_probability",
    ],
    "COVERAGE_INTERVAL_MU": [
        "drmd_standard_uncertainty",
        "drmd_interval_min",
        "drmd_interval_max",
        "drmd_coverage_probability",
    ],
}
ALL_UNCERTAINTY_FIELDS = [
    "drmd_standard_uncertainty",
    "drmd_expanded_uncertainty",
    "drmd_coverage_factor",
    "drmd_coverage_probability",
    "drmd_interval_min",
    "drmd_interval_max",
    "drmd_distribution",
]
# Properties of DRMD_QUANTITY that only si:real and si:constant write
SI_FIELDS = [
    "drmd_si_label",
    "drmd_quantity_kind",
    "drmd_si_value",
    "drmd_si_unit",
    "drmd_significant_digit",
    "drmd_si_date_time",
    "drmd_uncertainty_type",
    *ALL_UNCERTAINTY_FIELDS,
]


@dataclass(frozen=True)
class Finding:
    """One rule that a document does not meet."""

    rule_id: str
    severity: str
    message: str
    object_id: str | None = None


def is_compliant(findings: list[Finding]) -> bool:
    """True if no finding blocks compliance (errors and conditional errors do)."""
    return not any(f.severity in BLOCKING for f in findings)


def _is_set(text) -> bool:
    return text is not None and str(text).strip() != ""


class _Checker:
    def __init__(self, graph: DrmdGraph):
        self.graph = graph
        self.doc_id = graph.document_id
        self.document = graph.document
        self.findings: list[Finding] = []

    def add(
        self, rule_id: str, severity: str, message: str, object_id: str | None
    ) -> None:
        self.findings.append(Finding(rule_id, severity, message, object_id))

    def has_rich(self, object_id: str, attr: str) -> bool:
        """True if the rich-content element of a property would be written (text or file)."""
        obj = self.graph.obj(object_id)
        return value(obj, attr) is not None or bool(
            self.graph.files_of(object_id, property_code(obj, attr))
        )

    def quantities_of_result(self, result_id: str) -> tuple[list[str], bool]:
        """Quantities of a result and whether they are written inside drmd:list."""
        quantities = self.graph.parents(result_id, DrmdQuantity)
        as_list = bool(value(self.graph.obj(result_id), "drmd_data_as_list"))
        return quantities, as_list or len(quantities) > 1

    # -- drmd-business-rules.sch -------------------------------------------------------------

    def schematron(self) -> None:
        graph, doc_id, document = self.graph, self.doc_id, self.document
        materials = graph.parents(doc_id, ReferenceMaterial)
        psets = graph.parents(doc_id, DrmdPropertySet)
        persons = graph.parents(doc_id, DrmdRespPerson)
        results = {pset: graph.parents(pset, DrmdResult) for pset in psets}

        # Pattern "shared-structural-rules"
        # context drmd:digitalReferenceMaterialDocument
        if value(document, "drmd_document_title") is None:  # drmd:titleOfTheDocument
            self.add(
                "DRMD-001",
                ERROR,
                "The document type (titleOfTheDocument) is missing.",
                doc_id,
            )
        if not materials:  # drmd:materials/drmd:material
            self.add(
                "DRMD-002", ERROR, "The document has no reference material.", doc_id
            )
        if not psets:  # drmd:propertiesList/drmd:properties
            self.add("DRMD-003", ERROR, "The document has no properties block.", doc_id)

        # context drmd:statements
        for rule_id, severity, attr, text in (
            ("DRMD-004", ERROR, "drmd_intended_use", "intended use"),
            ("DRMD-005", ERROR, "drmd_storage_information", "storage information"),
            (
                "DRMD-006",
                ERROR,
                "drmd_handling_instructions",
                "instructions for handling and use",
            ),
            (
                "DRMD-013",
                CONDITIONAL_ERROR,
                "drmd_commutability",
                "commutability statement",
            ),
            (
                "DRMD-015",
                WARNING,
                "drmd_health_and_safety",
                "health and safety information",
            ),
        ):
            if not self.has_rich(doc_id, attr):
                self.add(rule_id, severity, f"The document has no {text}.", doc_id)

        # context drmd:materials/drmd:material
        for rm_id in materials:
            if value(graph.obj(rm_id), "name") is None:  # drmd:name
                self.add(
                    "DRMD-007", ERROR, "The reference material has no name.", rm_id
                )
            roles = {
                value(graph.obj(qid), "drmd_quantity_role")
                for qid in graph.parents(rm_id, DrmdQuantity)
            }
            if "MINIMUM_SAMPLE_SIZE" not in roles:  # drmd:minimumSampleSize
                self.add(
                    "DRMD-008",
                    CONDITIONAL_ERROR,
                    "The reference material states no minimum sample size.",
                    rm_id,
                )
            if not graph.parents(rm_id, DrmdIdentifier):  # drmd:materialIdentifiers/...
                self.add(
                    "DRMD-016",
                    ERROR,
                    "The reference material has no material identifier.",
                    rm_id,
                )

        # context drmd:propertiesList/drmd:properties
        for pset_id in psets:
            if not results[pset_id]:  # drmd:results/drmd:result
                self.add(
                    "DRMD-009", ERROR, "The properties block has no result.", pset_id
                )
            if not graph.parents(pset_id, DrmdProcedure):  # drmd:procedures
                self.add(
                    "DRMD-014",
                    CONDITIONAL_ERROR,
                    "The properties block names no measurement procedure.",
                    pset_id,
                )

        # context drmd:administrativeData
        if value(document, "drmd_producer") is None:  # drmd:referenceMaterialProducer
            self.add(
                "DRMD-010", ERROR, "The reference material producer is missing.", doc_id
            )

        # context drmd:administrativeData/drmd:coreData
        if value(document, "drmd_validity_type") is None:  # drmd:validity
            self.add("DRMD-012", ERROR, "The period of validity is missing.", doc_id)
        if value(document, "version") is None:  # drmd:documentVersion
            self.add("DRMD-011", ERROR, "The document version is missing.", doc_id)

        title = value(document, "drmd_document_title")
        certified = [
            p for p in psets if value(graph.obj(p), "drmd_is_certified") is True
        ]
        any_result = any(results[p] for p in psets)

        # Pattern "rmc-document-rules": titleOfTheDocument = 'referenceMaterialCertificate'
        if title == CRM:
            # drmd:statements/drmd:metrologicalTraceability
            if not self.has_rich(doc_id, "drmd_metrological_traceability"):
                self.add(
                    "RMC-001",
                    ERROR,
                    "A certificate needs a metrological traceability statement.",
                    doc_id,
                )
            # drmd:propertiesList/drmd:properties[@isCertified = 'true']
            if not certified:
                self.add(
                    "RMC-002",
                    ERROR,
                    "A certificate needs a certified properties block.",
                    doc_id,
                )
            # drmd:propertiesList/drmd:properties/drmd:results/drmd:result
            if not any_result:
                self.add(
                    "RMC-003", ERROR, "A certificate needs property values.", doc_id
                )
            # drmd:propertiesList/drmd:properties[@isCertified = 'true']/drmd:procedures
            if not any(graph.parents(p, DrmdProcedure) for p in certified):
                self.add(
                    "RMC-005",
                    WARNING,
                    "No certified properties block names its measurement procedures.",
                    doc_id,
                )
            # drmd:administrativeData/drmd:respPersons
            if not persons:
                self.add(
                    "RMC-010", ERROR, "A certificate needs responsible persons.", doc_id
                )
            # drmd:respPersons/dcc:respPerson[normalize-space(dcc:role) != '']
            if not any(_is_set(value(graph.obj(p), "drmd_role")) for p in persons):
                self.add(
                    "RMC-012",
                    ERROR,
                    "No responsible person states a function (role).",
                    doc_id,
                )
            # drmd:materials/drmd:material/drmd:description (any material)
            if not any(self.has_rich(rm, "description") for rm in materials):
                self.add(
                    "RMC-011",
                    ERROR,
                    "A certificate needs a material description.",
                    doc_id,
                )

            # Pattern "rmc-certified-property-rules"
            # //drmd:properties[@isCertified = 'true']//drmd:result/drmd:data/...
            for pset_id in certified:
                for result_id in results[pset_id]:
                    quantities, as_list = self.quantities_of_result(result_id)
                    for quantity_id in quantities:
                        self.certified_quantity(quantity_id, as_list)

        # Pattern "pis-document-rules": titleOfTheDocument = 'productInformationSheet'
        if title == PIS:
            # not(drmd:propertiesList/drmd:properties[@isCertified = 'true'])
            if certified:
                self.add(
                    "PIS-001",
                    ERROR,
                    "A product information sheet must not contain certified values.",
                    doc_id,
                )
            # drmd:propertiesList/drmd:properties/drmd:results/drmd:result
            if not any_result:
                self.add(
                    "PIS-002",
                    ERROR,
                    "A product information sheet needs results.",
                    doc_id,
                )
            # //drmd:properties: not(@isCertified = 'true')
            for pset_id in certified:
                self.add(
                    "PIS-003",
                    ERROR,
                    "This properties block must not be marked certified.",
                    pset_id,
                )
            # //drmd:materials/drmd:material: drmd:description
            for rm_id in materials:
                if not self.has_rich(rm_id, "description"):
                    self.add(
                        "PIS-005",
                        WARNING,
                        "The material has no description (recommended).",
                        rm_id,
                    )

    def certified_quantity(self, quantity_id: str, as_list: bool) -> None:
        graph = self.graph
        quantity = graph.obj(quantity_id)
        kind = value(quantity, "drmd_value_type")
        has_uncertainty = value(quantity, "drmd_uncertainty_type") is not None
        members = [graph.obj(m) for m in graph.parents(quantity_id, DrmdQuantity)]
        if as_list:
            # .../drmd:data/drmd:list/drmd:quantity[si:real]
            if kind == "SI_REAL" and not has_uncertainty:
                self.add(
                    "RMC-007",
                    ERROR,
                    "A certified value in a list has no measurement uncertainty.",
                    quantity_id,
                )
            return
        # .../drmd:data/drmd:quantity[si:real]
        if kind == "SI_REAL" and not has_uncertainty:
            self.add(
                "RMC-006",
                ERROR,
                "A certified value has no measurement uncertainty.",
                quantity_id,
            )
        # .../drmd:data/drmd:quantity[si:realListXMLList]
        if kind == "SI_REAL_LIST_XML_LIST" and all(
            value(m, "drmd_uncertainty_type") is None for m in members
        ):
            self.add(
                "RMC-008",
                ERROR,
                "A certified list of values has no measurement uncertainty.",
                quantity_id,
            )
        # .../drmd:data/drmd:quantity[si:hybrid]: not(si:hybrid/si:real[no uncertainty])
        if kind == "SI_HYBRID" and any(
            value(m, "drmd_value_type") == "SI_REAL"
            and value(m, "drmd_uncertainty_type") is None
            for m in members
        ):
            self.add(
                "RMC-009",
                ERROR,
                "A value of a certified si:hybrid has no measurement uncertainty.",
                quantity_id,
            )

    # -- drmd.xsd, DCC and D-SI (XSD-...) and writing the objects (MODEL-...) ----------------

    def structure(self) -> None:
        graph, doc_id, document = self.graph, self.doc_id, self.document
        version = value(document, "drmd_schema_version")
        if not (version and SCHEMA_VERSION.fullmatch(version)):
            self.add(
                "XSD-SCHEMA-VERSION",
                ERROR,
                "The DRMD schema version must be written as major.minor.patch, e.g. 1.0.0.",
                doc_id,
            )
        self.validity()
        self.producer_location()
        for object_id, obj in graph.collection.attached_objects.items():
            self.texts_and_codes(object_id, obj)
            if isinstance(obj, DrmdQuantity):
                self.quantity(object_id, obj)
            elif isinstance(obj, DrmdResult):
                if not graph.parents(object_id, DrmdQuantity):
                    self.add(
                        "XSD-RESULT-DATA",
                        ERROR,
                        "The result has no quantity.",
                        object_id,
                    )
            elif isinstance(obj, DrmdTranslation):
                self.translation(object_id, obj)
            elif isinstance(obj, DrmdFile):
                self.file(object_id, obj)
        for rm_id in graph.parents(doc_id, ReferenceMaterial):
            for quantity_id in graph.parents(rm_id, DrmdQuantity):
                role = value(graph.obj(quantity_id), "drmd_quantity_role")
                if role not in ("MINIMUM_SAMPLE_SIZE", "ITEM_QUANTITIES"):
                    self.add(
                        "MODEL-QUANTITY-ROLE",
                        ERROR,
                        "A quantity of a reference material needs the role "
                        "MINIMUM_SAMPLE_SIZE or ITEM_QUANTITIES; otherwise it is not written.",
                        quantity_id,
                    )
        self.xml_ids()

    def unused(self, object_id: str, attrs: list[str], reason: str) -> None:
        obj = self.graph.obj(object_id)
        found = [property_code(obj, a) for a in attrs if value(obj, a) is not None]
        if found:
            self.add(
                "MODEL-UNUSED-VALUE",
                WARNING,
                f"{', '.join(found)} is not written {reason}.",
                object_id,
            )

    def validity(self) -> None:
        document, doc_id = self.document, self.doc_id
        kind = value(document, "drmd_validity_type")
        if kind == "SPECIFIC_TIME" and value(document, "date_expiration") is None:
            self.add(
                "XSD-VALIDITY",
                ERROR,
                "Validity SPECIFIC_TIME needs an expiration date.",
                doc_id,
            )
        if kind == "TIME_AFTER_DISPATCH" and not _is_set(
            value(document, "drmd_period")
        ):
            self.add(
                "XSD-VALIDITY",
                ERROR,
                "Validity TIME_AFTER_DISPATCH needs a period.",
                doc_id,
            )
        other_fields = {
            "UNTIL_REVOKED": ["date_expiration", "drmd_period", "drmd_dispatch_date"],
            "TIME_AFTER_DISPATCH": ["date_expiration"],
            "SPECIFIC_TIME": ["drmd_period", "drmd_dispatch_date"],
        }.get(kind, [])
        self.unused(doc_id, other_fields, f"for validity type {kind}")

    def producer_location(self) -> None:
        producer = value(self.document, "drmd_producer")
        if producer is None:
            return
        fields = [attr for _, attr in ADDRESS_PROPERTIES] + [
            "drmd_address_further",
            "drmd_latitude",
        ]
        if not any(value(producer, f) is not None for f in fields):
            self.add(
                "XSD-PRODUCER-ADDRESS",
                ERROR,
                "The producer needs at least one address element (dcc:location).",
                producer.code,
            )

    def texts_and_codes(self, object_id: str, obj) -> None:
        for attr, meta in obj._property_metadata.items():
            text = value(obj, attr)
            if (
                meta.data_type in (DataType.VARCHAR, DataType.HYPERLINK)
                and isinstance(text, str)
                and not text.strip()
            ):
                self.add(
                    "XSD-NOT-EMPTY",
                    ERROR,
                    f"{meta.code} is set to an empty text; leave it unset instead.",
                    object_id,
                )
        lang = value(obj, "drmd_language")
        if lang is not None and not LANGUAGE.fullmatch(lang):
            self.add(
                "XSD-LANGUAGE",
                ERROR,
                f"Language {lang!r} is not an ISO 639-1 code of two lower-case letters.",
                object_id,
            )
        code = value(obj, "drmd_country_code")
        if code is not None and not COUNTRY_CODE.fullmatch(code):
            self.add(
                "XSD-COUNTRY-CODE",
                ERROR,
                f"Country code {code!r} is not ISO 3166-1 alpha-2 (two upper-case letters).",
                object_id,
            )
        period = value(obj, "drmd_period")
        if _is_set(period) and not DURATION.fullmatch(period):
            self.add(
                "XSD-DURATION",
                ERROR,
                f"Period {period!r} is not an ISO 8601 duration such as P2Y.",
                object_id,
            )
        latitude, longitude = value(obj, "drmd_latitude"), value(obj, "drmd_longitude")
        if (latitude is None) != (longitude is None):
            self.add(
                "MODEL-COORDINATES",
                ERROR,
                "Latitude and longitude are written only together.",
                object_id,
            )
        elif latitude is not None and not (
            -90 <= latitude <= 90 and -180 <= longitude <= 180
        ):
            self.add(
                "MODEL-COORDINATES",
                ERROR,
                "Latitude or longitude is outside the WGS84 range.",
                object_id,
            )

    def quantity(self, quantity_id: str, quantity: DrmdQuantity) -> None:
        graph = self.graph
        kind = value(quantity, "drmd_value_type")
        members = [graph.obj(m) for m in graph.parents(quantity_id, DrmdQuantity)]
        reason = f"for value type {kind}"
        if kind in ("SI_REAL", "SI_CONSTANT"):
            self.si_value(quantity_id, quantity)
            self.uncertainty(quantity_id, quantity, constant=kind == "SI_CONSTANT")
        else:
            self.unused(quantity_id, SI_FIELDS, reason)
        if kind == "SI_HYBRID":
            kinds = {value(m, "drmd_value_type") for m in members}
            if len(kinds) != 1 or not kinds <= {
                "SI_REAL",
                "SI_CONSTANT",
                "SI_REAL_LIST_XML_LIST",
            }:
                self.add(
                    "XSD-QUANTITY-VALUE",
                    ERROR,
                    "An si:hybrid needs member quantities of one value type "
                    "(SI_REAL, SI_CONSTANT or SI_REAL_LIST_XML_LIST).",
                    quantity_id,
                )
        elif kind == "SI_REAL_LIST_XML_LIST":
            self.real_list(quantity_id, members)
        elif members:
            self.add(
                "MODEL-UNUSED-VALUE",
                WARNING,
                f"Parent quantities are not written {reason}.",
                quantity_id,
            )
        if kind != "DCC_NO_QUANTITY":
            self.unused(quantity_id, ["drmd_no_quantity_text"], reason)
        if kind != "DCC_CHARS_XML_LIST":
            self.unused(quantity_id, ["drmd_chars_list"], reason)

    def si_value(self, quantity_id: str, quantity: DrmdQuantity) -> None:
        number = value(quantity, "drmd_si_value")
        if number is None or not _is_set(value(quantity, "drmd_si_unit")):
            self.add(
                "XSD-QUANTITY-VALUE",
                ERROR,
                "A D-SI value needs a value and a unit.",
                quantity_id,
            )
        elif math.isinf(number):
            self.add(
                "XSD-QUANTITY-VALUE",
                ERROR,
                "D-SI does not allow infinite values.",
                quantity_id,
            )
        stamp = value(quantity, "drmd_si_date_time")
        if stamp is not None and TIMESTAMP.fullmatch(str(stamp).strip()) is None:
            self.add(
                "XSD-DATE-TIME",
                ERROR,
                f"{stamp!r} is not a date and time.",
                quantity_id,
            )
        digit = value(quantity, "drmd_significant_digit")
        if number is not None and digit is not None and math.isfinite(number):
            exponent = Decimal(repr(float(number))).normalize().as_tuple().exponent
            if exponent < digit:
                self.add(
                    "DSI-SIGNIFICANT-DIGIT",
                    WARNING,
                    f"The value {number!r} has digits below the significant digit "
                    f"10^{digit}.",
                    quantity_id,
                )

    def uncertainty(
        self, quantity_id: str, quantity: DrmdQuantity, constant: bool
    ) -> None:
        kind = value(quantity, "drmd_uncertainty_type")
        if constant and kind not in (None, "STANDARD_MU"):
            self.add(
                "MODEL-UNCERTAINTY",
                ERROR,
                "An si:constant takes only a standard uncertainty (STANDARD_MU).",
                quantity_id,
            )
            return
        needed = UNCERTAINTY_FIELDS[kind]
        missing = [
            property_code(quantity, a) for a in needed if value(quantity, a) is None
        ]
        if missing:
            self.add(
                "XSD-UNCERTAINTY",
                ERROR,
                f"Uncertainty type {kind} needs {', '.join(missing)}.",
                quantity_id,
            )
        # si:distribution belongs to the uncertainty block of si:real, but stands alone in
        # si:constant
        written = needed + (["drmd_distribution"] if kind or constant else [])
        self.unused(
            quantity_id,
            [a for a in ALL_UNCERTAINTY_FIELDS if a not in written],
            f"for uncertainty type {kind}",
        )
        factor = value(quantity, "drmd_coverage_factor")
        if factor is not None and not math.isnan(factor) and factor < 1:
            self.add(
                "XSD-UNCERTAINTY",
                ERROR,
                "The coverage factor must be at least 1.",
                quantity_id,
            )
        probability = value(quantity, "drmd_coverage_probability")
        if (
            probability is not None
            and not math.isnan(probability)
            and not 0 <= probability <= 1
        ):
            self.add(
                "XSD-UNCERTAINTY",
                ERROR,
                "The coverage probability must lie between 0 and 1.",
                quantity_id,
            )

    def real_list(self, quantity_id: str, members: list[DrmdQuantity]) -> None:
        if not members or any(
            value(m, "drmd_value_type") != "SI_REAL" for m in members
        ):
            self.add(
                "XSD-QUANTITY-VALUE",
                ERROR,
                "An si:realListXMLList needs member quantities of value type SI_REAL.",
                quantity_id,
            )
            return
        for attr in (
            "drmd_si_label",
            "drmd_quantity_kind",
            "drmd_significant_digit",
            "drmd_si_date_time",
            "drmd_distribution",
        ):
            given = [value(m, attr) is not None for m in members]
            if any(given) and not all(given):
                self.add(
                    "MODEL-LIST",
                    ERROR,
                    f"{property_code(members[0], attr)} must be set for all list "
                    "elements or for none.",
                    quantity_id,
                )
        for attr in ("drmd_uncertainty_type", "drmd_quantity_kind"):
            if len({value(m, attr) for m in members}) > 1:
                self.add(
                    "MODEL-LIST",
                    ERROR,
                    f"All list elements need the same {property_code(members[0], attr)}.",
                    quantity_id,
                )
        for attr in ("drmd_si_label", "drmd_si_unit", "drmd_distribution"):
            if any(" " in (value(m, attr) or "").strip() for m in members):
                self.add(
                    "MODEL-LIST",
                    ERROR,
                    f"{property_code(members[0], attr)} of a list element must not "
                    "contain spaces, because the XML list is separated by spaces.",
                    quantity_id,
                )

    def translation(self, translation_id: str, translation: DrmdTranslation) -> None:
        graph = self.graph
        if value(translation, "drmd_language") == value(self.document, "drmd_language"):
            self.add(
                "MODEL-TRANSLATION",
                ERROR,
                "A translation must not use the primary language of the document.",
                translation_id,
            )
        target = value(translation, "drmd_target_property")
        for owner_id in graph.children(translation_id):
            owner = graph.obj(owner_id)
            codes = {meta.code: attr for attr, meta in owner._property_metadata.items()}
            if target not in codes or value(owner, codes[target]) is None:
                self.add(
                    "MODEL-TRANSLATION",
                    ERROR,
                    f"The translated property {target} is not set on the linked object.",
                    translation_id,
                )

    def file(self, file_id: str, file: DrmdFile) -> None:
        graph = self.graph
        if len(file.datasets) > 1:
            self.add(
                "MODEL-FILE",
                ERROR,
                "A DRMD_FILE object holds exactly one file.",
                file_id,
            )
        elif graph.file_bytes(file_id) is None:
            self.add(
                "XSD-FILE",
                ERROR,
                "The DRMD_FILE object has no file attached (dcc:dataBase64).",
                file_id,
            )
        target = value(file, "drmd_target_property")
        for owner_id in graph.children(file_id):
            owner = graph.obj(owner_id)
            if target:
                if target not in {m.code for m in owner._property_metadata.values()}:
                    self.add(
                        "MODEL-FILE",
                        ERROR,
                        f"The linked object has no property {target}.",
                        file_id,
                    )
            elif owner_id != self.doc_id and len(graph.files_of(owner_id, None)) > 1:
                self.add(
                    "XSD-FILE",
                    ERROR,
                    "A producer or responsible person takes at most one file without "
                    "target property (dcc:descriptionData).",
                    file_id,
                )

    def xml_ids(self) -> None:
        graph = self.graph
        seen: dict[str, str] = {}
        for object_id, obj in graph.collection.attached_objects.items():
            xml_id = value(obj, "drmd_xml_id")
            if xml_id is None:
                continue
            if not NCNAME.fullmatch(xml_id):
                self.add(
                    "XSD-XML-ID",
                    ERROR,
                    f"XML ID {xml_id!r} must start with a letter or '_' and contain "
                    "no spaces or colons.",
                    object_id,
                )
            if xml_id in seen:
                self.add(
                    "XSD-XML-ID",
                    ERROR,
                    f"XML ID {xml_id!r} is used by more than one object.",
                    object_id,
                )
            seen[xml_id] = object_id
        for object_id, obj in graph.collection.attached_objects.items():
            for ref in tokens(value(obj, "drmd_xml_ref_id")):
                if ref not in seen:
                    self.add(
                        "XSD-XML-REF-ID",
                        ERROR,
                        f"XML reference {ref!r} points to no XML ID of the document.",
                        object_id,
                    )

    # -- DRMD guidance -----------------------------------------------------------------------

    def guidance(self) -> None:
        graph, doc_id = self.graph, self.doc_id
        if len(graph.parents(doc_id, ReferenceMaterial)) > 1:
            for pset_id in graph.parents(doc_id, DrmdPropertySet):
                if not graph.parents(pset_id, ReferenceMaterial):
                    self.add(
                        "BP-MATERIAL-LINK",
                        WARNING,
                        "In a document with several materials, link every properties block "
                        "to its reference material.",
                        pset_id,
                    )


def check_graph(graph: DrmdGraph) -> list[Finding]:
    """Check the objects of one DRMD document; see the module docstring for the rule sets."""
    checker = _Checker(graph)
    checker.schematron()
    checker.structure()
    checker.guidance()
    return checker.findings


def schematron_rule_ids(findings: list[Finding]) -> set[str]:
    """Identifiers of the findings that correspond to drmd-business-rules.sch."""
    return {
        f.rule_id for f in findings if f.rule_id.split("-")[0] in ("DRMD", "RMC", "PIS")
    }
