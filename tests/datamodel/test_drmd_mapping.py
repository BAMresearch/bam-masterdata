"""Round trip DRMD XML -> DRMD masterdata objects -> DRMD XML (README.md, sections 4 and 11)."""

import copy
import datetime
import functools
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

from bam_masterdata.datamodel.drmd.object_types import (
    DrmdFile,
    DrmdPropertySet,
    DrmdQuantity,
    DrmdRespPerson,
    DrmdResult,
    DrmdStatement,
    DrmdTranslation,
    ReferenceMaterial,
)
from tests.datamodel import drmd_check
from tests.datamodel.drmd_rules import check_graph
from tests.datamodel.drmd_validation import schema_validator
from tests.datamodel.drmd_xml import (
    NS,
    UnsupportedContentError,
    compare_documents,
    format_decimal,
    format_plain,
    format_timestamp,
    graph_to_xml,
    q,
    value,
    xml_to_graph,
)

DATA_DIR = Path(__file__).parents[1] / "data" / "drmd"
DOCUMENTS = [
    "complete-coverage.xml",
    "reference-material-certificate.xml",
    "product-information-sheet.xml",
]
BAM_OE = "EXAMPLE_OE"

# si:decimalType of D-SI v2.2.1
DSI_DECIMAL = re.compile(r"[-+]?((\d*\.\d+)|(\d+\.\d*)|(\d+\.?))([Ee][-+]?\d+)?|NaN")


@functools.cache
def _imported(name: str):
    return xml_to_graph(DATA_DIR / name, bam_oe=BAM_OE)


def imported(name: str):
    """The objects of a test document, as a copy that a test may change."""
    return copy.deepcopy(_imported(name))


def load(name: str) -> ET.ElementTree:
    return ET.parse(DATA_DIR / name)


def to_bytes(tree: ET.ElementTree) -> bytes:
    return ET.tostring(tree.getroot(), encoding="utf-8", xml_declaration=True)


def objects(graph, cls) -> list:
    return [
        oid
        for oid, obj in graph.collection.attached_objects.items()
        if type(obj) is cls
    ]


@pytest.mark.parametrize("name", DOCUMENTS)
def test_round_trip_keeps_the_document(name):
    graph = imported(name)
    assert graph.warnings == []
    regenerated = graph_to_xml(graph)
    assert compare_documents(DATA_DIR / name, regenerated) == []
    assert check_graph(graph) == []


@pytest.mark.parametrize("name", DOCUMENTS)
def test_regenerated_document_is_valid(name):
    validator = schema_validator()
    if validator is None:
        pytest.skip(
            "set DRMD_SCHEMA_DIR to the DRMD schema repository and install lxml"
        )
    regenerated = graph_to_xml(imported(name))
    errors, findings = validator.validate(regenerated)
    assert errors == []
    assert findings == []


def test_mapping_of_the_coverage_document():
    graph = imported("complete-coverage.xml")
    document = graph.document
    assert value(document, "drmd_document_title") == "REFERENCE_MATERIAL_CERTIFICATE"
    assert value(document, "drmd_language") == "en"
    assert value(document, "drmd_validity_type") == "TIME_AFTER_DISPATCH"
    assert value(document, "drmd_dispatch_date") == datetime.date(2026, 4, 15)
    assert value(document, "drmd_period") == "P2Y"
    assert value(document, "drmd_handling_instructions").count("\n\n") == 1

    producer = value(document, "drmd_producer")
    assert value(producer, "drmd_city") == "Berlin"
    assert value(producer, "drmd_latitude") == pytest.approx(52.4316)

    # translations are parents that name the translated property
    languages = {
        (
            value(graph.obj(t), "drmd_target_property"),
            value(graph.obj(t), "drmd_language"),
        )
        for t in graph.parents(graph.document_id, DrmdTranslation)
    }
    assert ("DRMD_INTENDED_USE", "de") in languages

    # properties blocks are linked to the reference material they describe
    certified, blank = graph.parents(graph.document_id, DrmdPropertySet)
    material = graph.obj(graph.parents(certified, ReferenceMaterial)[0])
    assert value(material, "name").startswith("Polypropylene nanoparticles")
    assert value(graph.obj(certified), "drmd_is_certified") is True
    assert value(graph.obj(blank), "drmd_is_certified") is False

    # an si:realListXMLList is one quantity with one parent quantity per list element
    stability = graph.parents(certified, DrmdResult)[1]
    (series,) = graph.parents(stability, DrmdQuantity)
    members = [graph.obj(m) for m in graph.parents(series, DrmdQuantity)]
    assert [value(m, "drmd_si_value") for m in members] == [182.1, 182.9, 181.8]
    assert {value(m, "drmd_quantity_kind") for m in members} == {"Diameter"}
    assert {value(m, "drmd_uncertainty_type") for m in members} == {"STANDARD_MU"}

    # @id and @refId are kept in the "Document Structure" section
    persons = [graph.obj(p) for p in graph.parents(graph.document_id, DrmdRespPerson)]
    assert value(persons[1], "drmd_xml_ref_id") == "respPerson_1"
    assert value(persons[0], "drmd_dcc_ref_type") == "basic_certificateIdentification"

    # embedded files are DRMD_FILE parents; the target property says where they belong
    targets = sorted(
        value(graph.obj(f), "drmd_target_property") or "-"
        for f in objects(graph, DrmdFile)
    )
    assert targets == [
        "-",
        "-",
        "DESCRIPTION",
        "DRMD_HEALTH_AND_SAFETY",
        "DRMD_STATEMENT_TEXT",
    ]
    statements = graph.parents(graph.document_id, DrmdStatement)
    assert value(graph.obj(statements[1]), "drmd_formula_latex") == r"U = k \cdot u_c"


def test_embedded_files_are_stored_as_datasets(tmp_path):
    source = DATA_DIR / "complete-coverage.xml"
    graph = xml_to_graph(source, bam_oe=BAM_OE, file_dir=tmp_path)
    for file_id in objects(graph, DrmdFile):
        (path,) = graph.obj(file_id).datasets
        assert Path(path).read_bytes() == graph.files[file_id]
    # the export reads the dataset files, not the bytes kept by the import
    graph.files.clear()
    assert compare_documents(source, graph_to_xml(graph)) == []


@pytest.mark.parametrize(
    "number, digit, expected",
    [
        (6.42, None, "6.42"),
        (0.5, -2, "0.50"),
        (-0.5, -2, "-0.50"),
        (20.0, -1, "20.0"),
        (6.4237, -2, "6.4237"),  # digits are never removed
        (0.0, -3, "0.000"),
        (1500.0, None, "1500"),
        (1.03e9, None, "1.03e9"),
        (1.03e9, 7, "1.03e9"),
        (1.03e9, 6, "1.030e9"),
        (1234567.0, None, "1234567"),
        (12345678.0, None, "1.2345678e7"),
        (2.4e15, None, "2.4e15"),
        (1.380649e-23, None, "1.380649e-23"),
        (0.0001, None, "0.0001"),
        (0.000012, None, "1.2e-5"),
        (float("nan"), None, "NaN"),
    ],
)
def test_format_decimal(number, digit, expected):
    assert format_decimal(number, digit) == expected
    assert DSI_DECIMAL.fullmatch(expected)


def test_format_decimal_rejects_infinity():
    with pytest.raises(ValueError):
        format_decimal(float("inf"))


def test_format_plain_and_timestamp():
    assert format_plain(2.0) == "2"
    assert format_plain(0.95) == "0.95"
    assert format_plain(1.0) == "1"
    assert format_timestamp("2026-03-01T10:00:00Z") == "2026-03-01T10:00:00Z"
    assert format_timestamp("2026-03-01 10:00:00") == "2026-03-01T10:00:00"
    assert format_timestamp("2026-03-01 10:00 +0100") == "2026-03-01T10:00:00+01:00"
    assert (
        format_timestamp(datetime.datetime(2026, 3, 1, 10, 0, 0))
        == "2026-03-01T10:00:00"
    )
    with pytest.raises(ValueError):
        format_timestamp("01.03.2026")


def _first_certified_real(tree: ET.ElementTree) -> ET.Element:
    return tree.getroot().find(
        "drmd:propertiesList/drmd:properties/drmd:results/drmd:result/drmd:data"
        "/drmd:list/drmd:quantity/si:real",
        NS,
    )


def test_deprecated_dsi_uncertainty_is_written_in_the_current_form():
    tree = load("reference-material-certificate.xml")
    real = _first_certified_real(tree)
    real.remove(real.find("si:measurementUncertaintyUnivariate", NS))
    deprecated = ET.SubElement(real, q("si:expandedUnc"))
    for tag, text in (
        ("si:uncertainty", "0.08"),
        ("si:coverageFactor", "2"),
        ("si:coverageProbability", "0.95"),
    ):
        ET.SubElement(deprecated, q(tag)).text = text
    graph = xml_to_graph(to_bytes(tree), bam_oe=BAM_OE)
    regenerated = ET.fromstring(graph_to_xml(graph))
    current = regenerated.find(
        ".//drmd:quantity/si:real/si:measurementUncertaintyUnivariate/si:expandedMU", NS
    )
    assert current.find("si:valueExpandedMU", NS).text == "0.08"
    assert current.find("si:coverageFactor", NS).text == "2"
    assert regenerated.find(".//si:expandedUnc", NS) is None


def test_list_entries_given_once_apply_to_every_value():
    tree = load("complete-coverage.xml")
    series = tree.getroot().find(".//si:realListXMLList", NS)
    series.find("si:unitXMLList", NS).text = r"\nano\metre"
    graph = xml_to_graph(to_bytes(tree), bam_oe=BAM_OE)
    units = {
        value(graph.obj(q_id), "drmd_si_unit")
        for q_id in objects(graph, DrmdQuantity)
        if value(graph.obj(q_id), "drmd_si_label") in ("month_4", "month_8", "month_12")
    }
    assert units == {r"\nano\metre"}
    regenerated = ET.fromstring(graph_to_xml(graph))
    unit_list = regenerated.find(".//si:realListXMLList/si:unitXMLList", NS).text
    assert unit_list.split() == [r"\nano\metre"] * 3


def test_content_outside_the_datamodel_is_reported():
    tree = load("complete-coverage.xml")
    root = tree.getroot()
    description = root.find("drmd:materials/drmd:material/drmd:description", NS)
    heading = ET.Element(q("dcc:name"))
    ET.SubElement(heading, q("dcc:content"), lang="en").text = "Material description"
    description.insert(0, heading)
    description.find("dcc:content", NS).set("id", "content_1")
    metadata = root.find(".//dcc:metaData", NS)
    country = ET.Element(q("dcc:countryCodeISO3166_1"))
    country.text = "DE"
    metadata.insert(2, country)
    ET.SubElement(root, q("ds:Signature"))

    graph = xml_to_graph(to_bytes(tree), bam_oe=BAM_OE)
    report = "\n".join(graph.warnings)
    assert (
        "heading dcc:name of /drmd:digitalReferenceMaterialDocument/drmd:materials"
        in report
    )
    assert "dcc:countryCodeISO3166_1" in report
    assert "attribute id of" in report and "dcc:content" in report
    assert "ds:Signature" in report
    assert len(graph.warnings) == 4


def test_values_that_cannot_be_held_raise():
    tree = load("reference-material-certificate.xml")
    real = _first_certified_real(tree)
    real.tag = q("si:complex")
    with pytest.raises(UnsupportedContentError, match="si:complex is not modelled"):
        xml_to_graph(to_bytes(tree), bam_oe=BAM_OE)


def test_value_element_in_the_wrong_namespace_is_reported():
    """drmd.xsd allows only the dcc:/si: value elements of dcc:primitiveQuantityType."""
    tree = load("complete-coverage.xml")
    no_quantity = tree.getroot().find(".//drmd:quantity/dcc:noQuantity", NS)
    no_quantity.tag = q("drmd:noQuantity")
    with pytest.raises(
        UnsupportedContentError,
        match=r"drmd:noQuantity is not allowed by drmd\.xsd: the value element must be "
        r"dcc:noQuantity \(namespace https://ptb\.de/dcc\)",
    ):
        xml_to_graph(to_bytes(tree), bam_oe=BAM_OE)


def test_incomplete_objects_are_exported_for_validation():
    graph = imported("product-information-sheet.xml")
    del graph.document.drmd_document_title
    del graph.document.drmd_producer
    root = ET.fromstring(graph_to_xml(graph))
    assert root.find(".//drmd:titleOfTheDocument", NS) is None
    assert root.find(".//drmd:referenceMaterialProducer", NS) is None


def test_readme_example():
    """The example in README.md, section 8.3, runs and gives a compliant certificate."""
    readme = Path(__file__).parents[2] / "bam_masterdata/datamodel/drmd/README.md"
    text = readme.read_text(encoding="utf-8")
    block = text.split("<!-- example: minimal certificate -->")[1]
    code = block.split("```python\n")[1].split("```")[0]
    namespace: dict = {}
    exec(compile(code, str(readme), "exec"), namespace)
    assert namespace["findings"] == []
    regenerated = ET.fromstring(namespace["xml"])
    assert regenerated.find(".//drmd:properties", NS).get("isCertified") == "true"
    validator = schema_validator()
    if validator is not None:
        assert validator.validate(namespace["xml"]) == ([], [])


def test_check_command(tmp_path):
    """`python -m tests.datamodel.drmd_check` passes the test documents and reports problems."""
    sources = [DATA_DIR / name for name in DOCUMENTS]
    arguments = [str(s) for s in sources] + ["--output-dir", str(tmp_path)]
    assert drmd_check.main(arguments) == 0
    for source in sources:
        assert (tmp_path / f"{source.stem}_regenerated.xml").is_file()

    tree = load("product-information-sheet.xml")
    tree.getroot().find(".//drmd:statements/drmd:intendedUse", NS).set("id", "use")
    changed = tmp_path / "changed.xml"
    changed.write_bytes(to_bytes(tree))
    assert drmd_check.main([str(changed), "--output-dir", str(tmp_path)]) == 1

    other = tmp_path / "other.xml"
    other.write_text('<document xmlns="urn:other"/>', encoding="utf-8")
    assert drmd_check.main([str(other), "--output-dir", str(tmp_path)]) == 1
