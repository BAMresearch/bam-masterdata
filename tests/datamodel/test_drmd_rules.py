"""
Document rules on the DRMD masterdata objects (README.md, section 6).

Every rule of drmd-business-rules.sch is exercised with the same mutations as the test suite of
the schema repository (tests/test_rules.py there), applied to the objects instead of the XML.
When DRMD_SCHEMA_DIR is set, the objects are also written as XML and validated with the real
Schematron rules, and both must report exactly the same rule identifiers.
"""

import copy
import functools
from pathlib import Path

import pytest

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
from tests.datamodel.drmd_rules import (
    BLOCKING,
    check_graph,
    is_compliant,
    schematron_rule_ids,
)
from tests.datamodel.drmd_validation import schema_validator
from tests.datamodel.drmd_xml import graph_to_xml, value, xml_to_graph

DATA_DIR = Path(__file__).parents[1] / "data" / "drmd"
CRM = "reference-material-certificate.xml"
PIS = "product-information-sheet.xml"
COVERAGE = "complete-coverage.xml"


@functools.cache
def _imported(name):
    return xml_to_graph(DATA_DIR / name, bam_oe="EXAMPLE_OE")


def fresh(name):
    """The objects of a test document, as a copy that a test may change."""
    return copy.deepcopy(_imported(name))


# -- helpers that change the objects ----------------------------------------------------------


def remove(graph, object_id):
    """Remove an object and every parent link it takes part in."""
    relationships = graph.collection.relationships
    for key, (parent_id, child_id) in list(relationships.items()):
        if object_id in (parent_id, child_id):
            del relationships[key]
    del graph.collection.attached_objects[object_id]


def add(graph, obj, child_id):
    """Add an object as parent of another object."""
    object_id = graph.collection.add(obj)
    obj.code = object_id
    graph.collection.add_relationship(object_id, child_id)
    return object_id


def of_type(graph, cls, owner=None):
    if owner is not None:
        return graph.parents(owner, cls)
    return [
        oid
        for oid, obj in graph.collection.attached_objects.items()
        if type(obj) is cls
    ]


def certified_sets(graph):
    return [
        p
        for p in of_type(graph, DrmdPropertySet, graph.document_id)
        if value(graph.obj(p), "drmd_is_certified")
    ]


def first_certified_result(graph):
    return graph.parents(certified_sets(graph)[0], DrmdResult)[0]


def single_certified_quantity(graph):
    """Keep only the first quantity of the first certified result, outside drmd:list."""
    result_id = first_certified_result(graph)
    first, *others = graph.parents(result_id, DrmdQuantity)
    for other in others:
        remove(graph, other)
    graph.obj(result_id).drmd_data_as_list = False
    return first


def clear_si(quantity):
    for attr in (
        "drmd_si_label",
        "drmd_quantity_kind",
        "drmd_si_value",
        "drmd_si_unit",
        "drmd_uncertainty_type",
        "drmd_expanded_uncertainty",
        "drmd_coverage_factor",
        "drmd_coverage_probability",
        "drmd_distribution",
    ):
        if value(quantity, attr) is not None:
            delattr(quantity, attr)


def to_real_list(graph):
    quantity_id = single_certified_quantity(graph)
    quantity = graph.obj(quantity_id)
    clear_si(quantity)
    quantity.drmd_value_type = "SI_REAL_LIST_XML_LIST"
    for position, number in enumerate((6.42, 3.15), 1):
        member = DrmdQuantity(
            drmd_value_type="SI_REAL",
            drmd_position=position,
            drmd_si_value=number,
            drmd_si_unit="\\percent",
        )
        add(graph, member, quantity_id)


def to_hybrid(graph, quantity_id):
    quantity = graph.obj(quantity_id)
    clear_si(quantity)
    quantity.drmd_value_type = "SI_HYBRID"
    member = DrmdQuantity(
        drmd_value_type="SI_REAL",
        drmd_position=1,
        drmd_si_value=6.42,
        drmd_si_unit="\\percent",
    )
    add(graph, member, quantity_id)


def drop_uncertainty(graph):
    quantity_id = single_certified_quantity(graph)
    del graph.obj(quantity_id).drmd_uncertainty_type


def unset(attr, owner="document"):
    def mutate(graph):
        targets = {
            "document": [graph.document_id],
            "materials": of_type(graph, ReferenceMaterial, graph.document_id),
            "persons": of_type(graph, DrmdRespPerson, graph.document_id),
        }[owner]
        for object_id in targets:
            delattr(graph.obj(object_id), attr)

    return mutate


def remove_all(cls, owner=None):
    def mutate(graph):
        owners = [None] if owner is None else owner(graph)
        for owner_id in owners:
            for object_id in of_type(graph, cls, owner_id):
                remove(graph, object_id)

    return mutate


def materials(graph):
    return of_type(graph, ReferenceMaterial, graph.document_id)


def minimum_sample_size(graph):
    for rm_id in materials(graph):
        for qid in graph.parents(rm_id, DrmdQuantity):
            if value(graph.obj(qid), "drmd_quantity_role") == "MINIMUM_SAMPLE_SIZE":
                remove(graph, qid)


def set_certified(flag):
    def mutate(graph):
        for pset_id in of_type(graph, DrmdPropertySet, graph.document_id):
            graph.obj(pset_id).drmd_is_certified = flag

    return mutate


def drop_validity(graph):
    del graph.document.drmd_validity_type
    del graph.document.date_expiration


def drop_list_uncertainty(graph):
    result_id = first_certified_result(graph)
    first = graph.parents(result_id, DrmdQuantity)[0]
    del graph.obj(first).drmd_uncertainty_type


# Each case: (Schematron rules expected, base document, mutation). The expected sets are the
# rules that drmd-business-rules.sch raises for the same change of the XML document.
SCHEMATRON_CASES = {
    "DRMD-001": ({"DRMD-001"}, CRM, unset("drmd_document_title")),
    "DRMD-002": ({"DRMD-002", "RMC-011"}, CRM, remove_all(ReferenceMaterial)),
    "DRMD-003": (
        {"DRMD-003", "RMC-002", "RMC-003", "RMC-005"},
        CRM,
        remove_all(DrmdPropertySet),
    ),
    "DRMD-004": ({"DRMD-004"}, CRM, unset("drmd_intended_use")),
    "DRMD-005": ({"DRMD-005"}, CRM, unset("drmd_storage_information")),
    "DRMD-006": ({"DRMD-006"}, CRM, unset("drmd_handling_instructions")),
    "DRMD-007": ({"DRMD-007"}, CRM, unset("name", "materials")),
    "DRMD-008": ({"DRMD-008"}, CRM, minimum_sample_size),
    "DRMD-009": ({"DRMD-009", "RMC-003"}, CRM, remove_all(DrmdResult)),
    "DRMD-010": ({"DRMD-010"}, CRM, unset("drmd_producer")),
    "DRMD-011": ({"DRMD-011"}, CRM, unset("version")),
    "DRMD-012": ({"DRMD-012"}, CRM, drop_validity),
    "DRMD-013": ({"DRMD-013"}, CRM, unset("drmd_commutability")),
    "DRMD-014": ({"DRMD-014", "RMC-005"}, CRM, remove_all(DrmdProcedure)),
    "DRMD-015": ({"DRMD-015"}, CRM, unset("drmd_health_and_safety")),
    "DRMD-016": ({"DRMD-016"}, CRM, remove_all(DrmdIdentifier, materials)),
    "RMC-001": ({"RMC-001"}, CRM, unset("drmd_metrological_traceability")),
    "RMC-002": ({"RMC-002", "RMC-005"}, CRM, set_certified(False)),
    "RMC-003": ({"RMC-003", "DRMD-009"}, CRM, remove_all(DrmdResult)),
    "RMC-005": (
        {"RMC-005", "DRMD-014"},
        CRM,
        remove_all(DrmdProcedure, certified_sets),
    ),
    "RMC-006": ({"RMC-006"}, CRM, drop_uncertainty),
    "RMC-007": ({"RMC-007"}, CRM, drop_list_uncertainty),
    "RMC-008": ({"RMC-008"}, CRM, to_real_list),
    "RMC-009": (
        {"RMC-009"},
        CRM,
        lambda g: to_hybrid(g, single_certified_quantity(g)),
    ),
    "RMC-010": (
        {"RMC-010", "RMC-012"},
        CRM,
        remove_all(DrmdRespPerson, lambda g: [g.document_id]),
    ),
    "RMC-011": ({"RMC-011"}, CRM, unset("description", "materials")),
    "RMC-012": ({"RMC-012"}, CRM, unset("drmd_role", "persons")),
    "PIS-001": ({"PIS-001", "PIS-003"}, PIS, set_certified(True)),
    "PIS-002": ({"PIS-002", "DRMD-009"}, PIS, remove_all(DrmdResult)),
    "PIS-003": ({"PIS-003", "PIS-001"}, PIS, set_certified(True)),
    "PIS-005": ({"PIS-005"}, PIS, unset("description", "materials")),
    # RMC-009 applies to data/quantity only; an si:hybrid inside drmd:list is outside its
    # scope, in the Schematron and in this mirror alike
    "hybrid in list": (
        set(),
        CRM,
        lambda g: to_hybrid(g, g.parents(first_certified_result(g), DrmdQuantity)[0]),
    ),
}


def _schematron_rule_ids_in_file() -> set[str]:
    validator = schema_validator()
    _, _, patterns = validator.schematron
    return {
        check["id"]
        for pattern in patterns
        for rule in pattern["rules"]
        for check in rule["checks"]
    }


@pytest.mark.parametrize("name", [CRM, PIS, COVERAGE])
def test_compliant_documents_raise_nothing(name):
    graph = fresh(name)
    findings = check_graph(graph)
    assert findings == []
    assert is_compliant(findings)


def _mutated(case):
    expected, base, mutate = SCHEMATRON_CASES[case]
    graph = fresh(base)
    mutate(graph)
    return expected, graph


@pytest.mark.parametrize("case", SCHEMATRON_CASES)
def test_schematron_rule(case):
    expected, graph = _mutated(case)
    findings = check_graph(graph)
    assert schematron_rule_ids(findings) == expected
    blocking = {f.rule_id for f in findings if f.severity in BLOCKING}
    assert is_compliant(findings) == (not blocking)


@pytest.mark.parametrize("case", SCHEMATRON_CASES)
def test_schematron_rule_matches_the_schematron_file(case):
    validator = schema_validator()
    if validator is None:
        pytest.skip("Schematron cross-check needs DRMD_SCHEMA_DIR and lxml")
    expected, graph = _mutated(case)
    severities = {f.rule_id: f.severity for f in check_graph(graph)}
    _, raised = validator.validate(graph_to_xml(graph))
    assert {f["rule_id"] for f in raised} == expected
    for finding in raised:
        assert severities[finding["rule_id"]] == finding["severity"]


def test_every_schematron_rule_is_mirrored():
    if schema_validator() is None:
        pytest.skip("needs DRMD_SCHEMA_DIR and lxml")
    mirrored = {
        rule for expected, _, _ in SCHEMATRON_CASES.values() for rule in expected
    }
    assert mirrored == _schematron_rule_ids_in_file()


# -- requirements of drmd.xsd and of writing the objects --------------------------------------


def _producer(graph):
    return value(graph.document, "drmd_producer")


def _quantity_with(graph, attr, wanted):
    return next(
        graph.obj(q)
        for q in of_type(graph, DrmdQuantity)
        if value(graph.obj(q), attr) == wanted
    )


def _clear_address(graph):
    producer = _producer(graph)
    for attr in ("drmd_street", "drmd_street_no", "drmd_post_code", "drmd_city"):
        delattr(producer, attr)
    delattr(producer, "drmd_country_code")


def _first_quantity(graph):
    return graph.obj(graph.parents(first_certified_result(graph), DrmdQuantity)[0])


def _duplicate_id(graph):
    persons = of_type(graph, DrmdRespPerson, graph.document_id)
    graph.obj(persons[1]).drmd_xml_id = value(graph.obj(persons[0]), "drmd_xml_id")


def _translation(graph):
    return graph.obj(of_type(graph, DrmdTranslation)[0])


def _file_without_content(graph):
    file_id = of_type(graph, DrmdFile)[0]
    graph.files.pop(file_id)


def _mixed_list(graph):
    members = [
        graph.obj(q)
        for q in of_type(graph, DrmdQuantity)
        if value(graph.obj(q), "drmd_si_label") in ("month_4", "month_8")
    ]
    del members[0].drmd_uncertainty_type
    del members[0].drmd_standard_uncertainty
    del members[0].drmd_distribution


def _mixed_hybrid(graph):
    hybrid = next(
        q
        for q in of_type(graph, DrmdQuantity)
        if value(graph.obj(q), "drmd_value_type") == "SI_HYBRID"
    )
    # turn the second si:real of the si:hybrid into an si:constant without uncertainty
    member = graph.obj(graph.parents(hybrid, DrmdQuantity)[1])
    for attr in (
        "drmd_uncertainty_type",
        "drmd_expanded_uncertainty",
        "drmd_coverage_factor",
        "drmd_coverage_probability",
    ):
        delattr(member, attr)
    member.drmd_value_type = "SI_CONSTANT"


def _file_with_target(graph, target):
    return next(
        f
        for f in of_type(graph, DrmdFile)
        if value(graph.obj(f), "drmd_target_property") == target
    )


def _unlink_blank(graph):
    blank = of_type(graph, DrmdPropertySet, graph.document_id)[1]
    for rm_id in graph.parents(blank, ReferenceMaterial):
        for key, (parent_id, child_id) in list(graph.collection.relationships.items()):
            if (parent_id, child_id) == (rm_id, blank):
                del graph.collection.relationships[key]


NOT_WRITTEN = "not written"

# (rule, severity, base document, mutation, is the generated XML invalid against drmd.xsd?)
# None: libxml2, which tools/validate.py uses, does not detect the problem (see the DRMD
# guidance, "Cross-reference & Identifier Conventions"); Xerces does.
# NOT_WRITTEN: graph_to_xml() cannot write the objects and raises ValueError.
STRUCTURE_CASES = {
    "schema version": (
        "XSD-SCHEMA-VERSION",
        "error",
        CRM,
        lambda g: setattr(g.document, "drmd_schema_version", "1.0"),
        True,
    ),
    "specific time without date": (
        "XSD-VALIDITY",
        "error",
        CRM,
        lambda g: delattr(g.document, "date_expiration"),
        True,
    ),
    "period with specific time": (
        "MODEL-UNUSED-VALUE",
        "warning",
        CRM,
        lambda g: setattr(g.document, "drmd_period", "P1Y"),
        False,
    ),
    "period format": (
        "XSD-DURATION",
        "error",
        COVERAGE,
        lambda g: setattr(g.document, "drmd_period", "2 years"),
        True,
    ),
    "language": (
        "XSD-LANGUAGE",
        "error",
        COVERAGE,
        lambda g: setattr(_translation(g), "drmd_language", "DE"),
        True,
    ),
    "translation in primary language": (
        "MODEL-TRANSLATION",
        "error",
        COVERAGE,
        lambda g: setattr(_translation(g), "drmd_language", "en"),
        False,
    ),
    "country code": (
        "XSD-COUNTRY-CODE",
        "error",
        CRM,
        lambda g: setattr(_producer(g), "drmd_country_code", "de"),
        True,
    ),
    "producer without address": (
        "XSD-PRODUCER-ADDRESS",
        "error",
        CRM,
        _clear_address,
        True,
    ),
    "latitude only": (
        "MODEL-COORDINATES",
        "error",
        COVERAGE,
        lambda g: delattr(_producer(g), "drmd_longitude"),
        False,
    ),
    "empty text": (
        "XSD-NOT-EMPTY",
        "error",
        CRM,
        lambda g: setattr(
            g.obj(of_type(g, DrmdRespPerson, g.document_id)[1]), "drmd_role", " "
        ),
        True,
    ),
    "result without quantity": (
        "XSD-RESULT-DATA",
        "error",
        PIS,
        remove_all(DrmdQuantity, lambda g: of_type(g, DrmdResult)),
        True,
    ),
    "value without unit": (
        "XSD-QUANTITY-VALUE",
        "error",
        CRM,
        lambda g: delattr(_first_quantity(g), "drmd_si_unit"),
        True,
    ),
    "expanded uncertainty without coverage factor": (
        "XSD-UNCERTAINTY",
        "error",
        CRM,
        lambda g: delattr(_first_quantity(g), "drmd_coverage_factor"),
        True,
    ),
    "coverage factor below 1": (
        "XSD-UNCERTAINTY",
        "error",
        CRM,
        lambda g: setattr(_first_quantity(g), "drmd_coverage_factor", 0.5),
        True,
    ),
    "coverage probability above 1": (
        "XSD-UNCERTAINTY",
        "error",
        CRM,
        lambda g: setattr(_first_quantity(g), "drmd_coverage_probability", 95.0),
        True,
    ),
    "standard uncertainty with expanded type": (
        "MODEL-UNUSED-VALUE",
        "warning",
        CRM,
        lambda g: setattr(_first_quantity(g), "drmd_standard_uncertainty", 0.04),
        False,
    ),
    "list with mixed uncertainty": (
        "MODEL-LIST",
        "error",
        COVERAGE,
        _mixed_list,
        NOT_WRITTEN,
    ),
    "constant with expanded uncertainty": (
        "MODEL-UNCERTAINTY",
        "error",
        COVERAGE,
        lambda g: setattr(
            _quantity_with(g, "drmd_si_label", "k_B"),
            "drmd_uncertainty_type",
            "EXPANDED_MU",
        ),
        False,
    ),
    "hybrid with mixed members": (
        "XSD-QUANTITY-VALUE",
        "error",
        COVERAGE,
        _mixed_hybrid,
        True,
    ),
    "date without time": (
        "XSD-DATE-TIME",
        "error",
        COVERAGE,
        lambda g: setattr(
            _quantity_with(g, "drmd_si_label", "z-average"),
            "drmd_si_date_time",
            "2026-03-01",
        ),
        NOT_WRITTEN,
    ),
    "file for a property the object does not have": (
        "MODEL-FILE",
        "error",
        COVERAGE,
        lambda g: setattr(
            g.obj(_file_with_target(g, "DRMD_HEALTH_AND_SAFETY")),
            "drmd_target_property",
            "DRMD_SAFETY",
        ),
        False,
    ),
    "material quantity without role": (
        "MODEL-QUANTITY-ROLE",
        "error",
        CRM,
        lambda g: setattr(
            _quantity_with(g, "drmd_quantity_kind", "Diameter"),
            "drmd_quantity_role",
            "RESULT_DATA",
        ),
        False,
    ),
    "file without content": (
        "XSD-FILE",
        "error",
        COVERAGE,
        _file_without_content,
        True,
    ),
    "duplicate XML ID": ("XSD-XML-ID", "error", CRM, _duplicate_id, True),
    "XML ID format": (
        "XSD-XML-ID",
        "error",
        CRM,
        lambda g: setattr(
            g.obj(of_type(g, DrmdRespPerson, g.document_id)[0]), "drmd_xml_id", "1st"
        ),
        True,
    ),
    "dangling XML reference": (
        "XSD-XML-REF-ID",
        "error",
        COVERAGE,
        lambda g: setattr(
            g.obj(of_type(g, DrmdRespPerson, g.document_id)[1]),
            "drmd_xml_ref_id",
            "respPerson_9",
        ),
        None,
    ),
    "digits below the significant digit": (
        "DSI-SIGNIFICANT-DIGIT",
        "warning",
        COVERAGE,
        lambda g: setattr(
            _quantity_with(g, "drmd_si_label", "z-average"), "drmd_si_value", 182.43
        ),
        False,
    ),
    "properties block without material": (
        "BP-MATERIAL-LINK",
        "warning",
        COVERAGE,
        _unlink_blank,
        False,
    ),
}


@pytest.mark.parametrize("case", STRUCTURE_CASES)
def test_structure_rule(case):
    rule_id, severity, base, mutate, invalid = STRUCTURE_CASES[case]
    graph = fresh(base)
    mutate(graph)
    findings = check_graph(graph)
    assert {(f.rule_id, f.severity) for f in findings} == {(rule_id, severity)}

    if invalid == NOT_WRITTEN:
        with pytest.raises(ValueError):
            graph_to_xml(graph)
        return
    validator = schema_validator()
    if validator is None:
        return
    errors, _ = validator.validate(graph_to_xml(graph))
    assert bool(errors) is bool(invalid)
