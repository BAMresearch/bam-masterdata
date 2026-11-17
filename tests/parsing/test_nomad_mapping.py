"""Offline tests with synthetic archives only; no laboratory data or service access."""

import base64
import hashlib
import importlib
import json
from pathlib import Path
from unittest.mock import Mock

import pytest

from bam_masterdata.checker.schema_validator import (
    get_object_types,
    validate_object_type_codes,
)
from bam_masterdata.cli.run_parser import RunParsers, RunParsersWithTransactions
from bam_masterdata.datamodel.v0.object_types import Chemical, Sample
from bam_masterdata.datamodel.v1.base_objects import Activity
from bam_masterdata.datamodel.v1.entities import Device
from bam_masterdata.metadata.definitions import PropertyTypeAssignment
from bam_masterdata.metadata.entities import CollectionType
from bam_masterdata.parsing.nomad import (
    ArchiveContext,
    ArchiveSource,
    MappingError,
    NomadParser,
    entry_id,
)
from bam_masterdata.parsing.nomad.example_software import SyntheticSoftwareMapping
from bam_masterdata.parsing.nomad.hzb import HZBBatteryMapping
from tests.conftest import openbis_runner_mock

SYNTHETIC = Path(__file__).parents[1] / "data/nomad_synthetic"
BASE = "nomad_battery_space.schema_packages.hzb_bs_package."
ASSEMBLY = "nomad_battery_space.schema_packages.hzb_bs_assembly_package."
UTILITIES = "nomad_battery_space.schema_packages.utilities."
PURE = "nomad.datamodel.metainfo.basesections.v1.PubChemPureSubstanceSection"
REVISION = "synthetic-schema-revision"  # Placeholder, never a verified HZB hash.
UPLOAD = "synthetic-hzb-upload"
SCHEMA_IDS = {
    **{
        BASE + name: {REVISION}
        for name in (
            "BS_Chemical",
            "ElectrodeMaterial",
            "ElectrodeSheet",
            "ElectrolyteStock",
            "SeparatorStock",
            "ElectrodeSample",
            "ElectrolyteSample",
            "SeparatorSample",
        )
    },
    ASSEMBLY + "CoinCellBattery": {REVISION},
    **{
        UTILITIES + name: {REVISION}
        for name in (
            "dimensions.DimensionsAndWeights",
            "dimensions.VolumeAndWeights",
            "geometry.CircleGeometry",
            "geometry.RectangleGeometry",
        )
    },
    PURE: {REVISION},
}


def mapping(version="v1", **overrides):
    return HZBBatteryMapping(
        **{
            "target_version": version,
            "quantity_profile": "hzb-laboratory-units-v1",
            "schema_ids": SCHEMA_IDS,
            **overrides,
        }
    )


def section(schema, **values):
    return {"m_def": schema, "m_def_id": REVISION, **values}


def write_archive(tmp_path, slug, schema, **values):
    """Generate a deliberately synthetic record, never a replacement laboratory export."""
    path = tmp_path / f"{slug}.json"
    path.write_text(
        json.dumps(
            {
                "metadata": {"upload_id": UPLOAD, "mainfile": path.name},
                "data": section(
                    schema,
                    name=f"Synthetic {slug}",
                    lab_id=f"synthetic-{slug}",
                    **values,
                ),
            }
        )
    )
    return path


def reference(slug, fragment="/data"):
    return f"../uploads/{UPLOAD}/archive/{entry_id(UPLOAD, slug + '.json')}#{fragment}"


@pytest.fixture
def hzb_files(tmp_path):
    """Small synthetic graph with shared electrodes and an ordered workflow."""
    chemical = write_archive(
        tmp_path,
        "chemical",
        BASE + "BS_Chemical",
        description="Synthetic chemical description",
        datetime="2030-01-02T03:04:05+00:00",
        pure_substance=section(PURE, molecular_formula="X2", molar_mass=42.5),
        product_info={"product_weight": 2, "opening_date": "2030-01-02T03:04:05+00:00"},
        elemental_composition=[{"element": "X", "atomic_fraction": 0.5}],
    )
    material = write_archive(
        tmp_path,
        "material",
        BASE + "ElectrodeMaterial",
        chemicals=[{"chemical": reference("chemical", "data"), "role": "precursor"}],
        synthesis={
            "name": "Synthetic synthesis",
            "lab_id": "synthetic-material",
            "steps": [{"name": "Synthetic step"}],
        },
        yield_percent=0.3,
    )
    document = json.loads(material.read_text())
    document["workflow2"] = {
        "tasks": [{"name": "Synthetic step", "section": "#/data/synthesis/steps/0"}]
    }
    material.write_text(json.dumps(document))
    sheet = write_archive(
        tmp_path,
        "sheet",
        BASE + "ElectrodeSheet",
        chemicals=[{"chemical": reference("chemical"), "role": "solvent", "mass": 1}],
        electrode_materials=[
            {
                "material": reference("material"),
                "role": "active material",
                "mass": 1,
                "wt_percent": 0.25,
            }
        ],
        dimensions_and_weights=section(
            UTILITIES + "dimensions.DimensionsAndWeights",
            thickness=50,
            shape=section(
                UTILITIES + "geometry.RectangleGeometry", length=4, width=5, area=0.2
            ),
        ),
    )
    electrode = write_archive(
        tmp_path,
        "electrode",
        BASE + "ElectrodeSample",
        electrode_sheet=reference("sheet"),
        dimensions_and_weights={
            "mass": 0.002,
            "shape": section(UTILITIES + "geometry.CircleGeometry", diameter=8),
        },
    )
    cell = write_archive(
        tmp_path,
        "cell",
        ASSEMBLY + "CoinCellBattery",
        working_electrode=reference("electrode"),
        counter_electrode=reference("electrode"),
    )
    return {
        "chemical": chemical,
        "material": material,
        "sheet": sheet,
        "electrode": electrode,
        "cell": cell,
    }


def change(path, mutate):
    document = json.loads(path.read_text())
    mutate(document)
    path.write_text(json.dumps(document))


@pytest.mark.parametrize("version", ["v0", "v1"])
def test_synthetic_hzb_values_roles_identity_and_order(version, hzb_files):
    parser = NomadParser(mapping(version))
    files = list(hzb_files.values())
    collection = CollectionType()
    parser.parse(files, collection, Mock())
    objects = {obj.name: obj for obj in parser.report.objects.values()}
    chemical = objects["Synthetic chemical"]
    sheet = objects["Synthetic sheet"]
    electrode = objects["Synthetic electrode"]
    cell = objects["Synthetic cell"]
    assert cell.working_electrode is electrode and cell.counter_electrode is electrode
    assert electrode.electrode_sheet is sheet
    assert (sheet.thickness, sheet.length, sheet.width, sheet.area, sheet.shape) == (
        50.0,
        4.0,
        5.0,
        0.2,
        "RECTANGLE",
    )
    assert electrode.mass == 0.002 and electrode.diameter == 8.0
    assert chemical.chemical_formula_descriptive == "X2"
    assert getattr(chemical, "mass_molar" if version == "v0" else "molar_mass") == 42.5
    assert chemical.product_weight == 2.0
    assert chemical.opening_datetime == "2030-01-02T03:04:05+00:00"
    assert chemical.record_datetime == chemical.opening_datetime
    source = json.loads(chemical.source_record)
    assert (
        source["archive"]["data"]["elemental_composition"][0]["atomic_fraction"] == 0.5
    )
    assert source["quantity_profile"] == "hzb-laboratory-units-v1"
    assert len(objects) == 7 and len(collection.relationships) == 6
    assert {
        (
            parser.report.objects[r.parent].name,
            parser.report.objects[r.child].name,
            r.role,
        )
        for r in parser.report.relationships
    } == {
        ("Synthetic chemical", "Synthetic synthesis", "precursor"),
        ("Synthetic synthesis", "Synthetic material", "synthesis_output"),
        ("Synthetic synthesis", "Synthetic step", "has_step"),
        ("Synthetic synthesis", "Synthetic step", "workflow_task_alias"),
        ("Synthetic chemical", "Synthetic sheet", "solvent"),
        ("Synthetic material", "Synthetic sheet", "active material"),
        ("Synthetic sheet", "Synthetic electrode", "source_sheet"),
        ("Synthetic electrode", "Synthetic cell", "working_electrode"),
        ("Synthetic electrode", "Synthetic cell", "counter_electrode"),
    }
    rows = {
        r.role: r.qualifiers
        for r in parser.report.relationships
        if r.child == next(k for k, v in parser.report.objects.items() if v is sheet)
    }
    assert rows["solvent"]["normalized_quantities"]["mass"] == {
        "value": pytest.approx(1e-3),
        "unit": "kg",
    }
    assert rows["active material"]["normalized_quantities"]["mass"] == {
        "value": pytest.approx(1e-6),
        "unit": "kg",
    }
    assert objects["Synthetic step"].step_order == 1
    assert objects["Synthetic synthesis"].code != objects["Synthetic material"].code
    assert (
        json.loads(objects["Synthetic material"].source_record)["archive"]["data"][
            "yield_percent"
        ]
        == 0.3
    )
    assert any(d.code == "unconfirmed_scale" for d in parser.report.diagnostics)
    assert any(d.code == "retained_fields" for d in parser.report.diagnostics)
    first = parser.report.to_json()
    parser.parse(list(reversed(files)), CollectionType(), Mock())
    assert parser.report.to_json() == first
    serialized = json.loads(first)
    cell_data = next(obj for obj in serialized["objects"] if obj["code"] == cell.code)
    assert (
        cell_data["properties"][cell._property_metadata["working_electrode"].code]
        == electrode.code
    )


@pytest.mark.parametrize("version", ["v0", "v1"])
@pytest.mark.parametrize(
    "stock,sample,attribute",
    [
        ("ElectrolyteStock", "ElectrolyteSample", "electrolyte_stock"),
        ("SeparatorStock", "SeparatorSample", "separator_stock"),
    ],
)
def test_synthetic_stock_references(tmp_path, version, stock, sample, attribute):
    stock_path = write_archive(tmp_path, "stock", BASE + stock)
    sample_path = write_archive(
        tmp_path, "sample", BASE + sample, **{attribute: reference("stock")}
    )
    parser = NomadParser(mapping(version))
    parser.parse([sample_path, stock_path], CollectionType(), Mock())
    objects = {obj.name: obj for obj in parser.report.objects.values()}
    assert getattr(objects["Synthetic sample"], attribute) is objects["Synthetic stock"]


@pytest.mark.parametrize(
    "mutate,match",
    [
        (lambda d: d["data"].update(m_def="unrecognized.Schema"), "unsupported schema"),
        (
            lambda d: d["data"].update(m_def_id="unapproved-revision"),
            "unsupported schema hash",
        ),
        (lambda d: d["data"].pop("lab_id"), "missing mandatory value /data/lab_id"),
        (lambda d: d["data"].update(name=""), "missing mandatory text /data/name"),
        (
            lambda d: d["data"].update(datetime="2030-01-02T03:04:05"),
            "explicit UTC offset",
        ),
    ],
)
def test_synthetic_hzb_schema_errors_are_atomic(hzb_files, mutate, match):
    change(hzb_files["chemical"], mutate)
    collection = CollectionType()
    parser = NomadParser(mapping())
    with pytest.raises(MappingError, match=match):
        parser.parse(list(hzb_files.values()), collection, Mock())
    assert (
        not collection.attached_objects
        and not collection.relationships
        and parser.report is None
    )


@pytest.mark.parametrize(
    "ref,match",
    [
        (
            "../uploads/synthetic-missing/archive/missing#/data",
            "Unresolved archive reference",
        ),
        ("https://example.invalid/archive#/data", "Unsupported archive reference"),
        ("#/data/missing", "Unresolved section pointer"),
        ("#/data", "exact target"),
    ],
)
def test_synthetic_reference_errors(hzb_files, ref, match):
    change(hzb_files["electrode"], lambda d: d["data"].update(electrode_sheet=ref))
    collection = CollectionType()
    with pytest.raises(MappingError, match=match):
        NomadParser(mapping()).parse(list(hzb_files.values()), collection, Mock())
    assert not collection.attached_objects


@pytest.mark.parametrize(
    "schema,subsection,wrong_schema",
    [
        ("BS_Chemical", "pure_substance", UTILITIES + "geometry.CircleGeometry"),
        (
            "ElectrodeSheet",
            "dimensions_and_weights",
            UTILITIES + "dimensions.VolumeAndWeights",
        ),
        (
            "ElectrolyteStock",
            "volume_and_weights",
            UTILITIES + "dimensions.DimensionsAndWeights",
        ),
    ],
)
def test_nested_schema_kind_is_path_specific(
    tmp_path, schema, subsection, wrong_schema
):
    path = write_archive(
        tmp_path, "wrong-kind", BASE + schema, **{subsection: section(wrong_schema)}
    )
    with pytest.raises(MappingError, match="unsupported nested schema .* at this path"):
        NomadParser(mapping()).parse([path], CollectionType(), Mock())


@pytest.mark.parametrize("revision", [None, "unapproved-nested-revision"])
def test_named_nested_schema_needs_explicit_approved_id(hzb_files, revision):
    def mutate(document):
        pure = document["data"]["pure_substance"]
        if revision is None:
            pure.pop("m_def_id")
        else:
            pure["m_def_id"] = revision

    change(hzb_files["chemical"], mutate)
    with pytest.raises(MappingError, match="unsupported nested schema hash"):
        NomadParser(mapping()).parse([hzb_files["chemical"]], CollectionType(), Mock())


def test_explicit_schema_configuration():
    for config in (
        {},
        {BASE + "BS_Chemical": set()},
        {BASE + "BS_Chemical": "revision"},
        {"unsupported.Schema": {"revision"}},
    ):
        with pytest.raises(MappingError):
            mapping(schema_ids=config)
    with pytest.raises(MappingError, match="quantity profile"):
        mapping(quantity_profile="guess")
    with pytest.raises(MappingError, match="target version"):
        mapping(version="v2")
    # A caller-supplied whitelist is copied, never a mutable or implicit global default.
    supplied = {BASE + "BS_Chemical": {REVISION}}
    configured = mapping(schema_ids=supplied)
    supplied[BASE + "BS_Chemical"].add("later-change")
    assert configured.schema_ids[BASE + "BS_Chemical"] == frozenset({REVISION})


@pytest.mark.parametrize("omitted", [BASE + "BS_Chemical", PURE])
def test_encountered_schema_must_have_explicit_revision_configuration(
    hzb_files, omitted
):
    configured = {name: ids for name, ids in SCHEMA_IDS.items() if name != omitted}
    with pytest.raises(MappingError, match="unsupported (nested )?schema hash"):
        NomadParser(mapping(schema_ids=configured)).parse(
            [hzb_files["chemical"]], CollectionType(), Mock()
        )


def test_missing_schema_config_is_not_an_implicit_fallback():
    with pytest.raises(TypeError, match="schema_ids"):
        HZBBatteryMapping(
            target_version="v1", quantity_profile="hzb-laboratory-units-v1"
        )


def test_source_identity_is_explicit_and_duplicate_conflicts_fail(tmp_path, hzb_files):
    original = hzb_files["chemical"]
    renamed = tmp_path / "arbitrary.json"
    renamed.write_text(original.read_text())
    parser = NomadParser(mapping())
    parser.parse([original, renamed], CollectionType(), Mock())
    assert len(parser.report.objects) == 1
    assert any(d.code == "duplicate_input" for d in parser.report.diagnostics)
    change(renamed, lambda d: d["data"].update(name="conflicting"))
    with pytest.raises(MappingError, match="duplicate source identity"):
        parser.parse([original, renamed], CollectionType(), Mock())
    change(renamed, lambda d: d.pop("metadata"))
    parser = NomadParser(mapping(), [ArchiveSource(renamed, UPLOAD, original.name)])
    parser.parse([renamed], CollectionType(), Mock())
    assert next(iter(parser.report.objects)).entry_id == entry_id(UPLOAD, original.name)
    with pytest.raises(MappingError, match="missing source identity"):
        NomadParser(mapping()).parse([renamed], CollectionType(), Mock())
    change(renamed, lambda d: d.update(metadata={"upload_id": "synthetic-conflict"}))
    with pytest.raises(MappingError, match="conflicting source metadata upload_id"):
        parser.parse([renamed], CollectionType(), Mock())


def test_generic_entry_id_and_unit_conversion():
    upload, mainfile = "example-upload", "nested/example.json"
    expected = base64.urlsafe_b64encode(
        hashlib.sha512((upload + mainfile).encode()).digest()
    )[:28].decode()
    assert entry_id(upload, mainfile) == expected
    assert entry_id(upload, mainfile, "child") != expected
    context = ArchiveContext([], "synthetic-test", "v1")
    assert context.quantity(2.5, "mL", "uL") == pytest.approx(2500)
    for value, source, target in [
        (1, "unknown-unit", "g"),
        (1, "g", "mL"),
        (True, "g", "g"),
        (float("inf"), "g", "g"),
    ]:
        with pytest.raises(MappingError):
            context.quantity(value, source, target)


@pytest.mark.parametrize("runner_type", [RunParsers, RunParsersWithTransactions])
@pytest.mark.parametrize("version", ["v0", "v1"])
def test_synthetic_hzb_runner_mock_compatibility(hzb_files, runner_type, version):
    parser = NomadParser(mapping(version))
    openbis = openbis_runner_mock()
    runner = runner_type(
        openbis=openbis,
        space_name="TEST_SPACE",
        project_name="TEST_PROJECT",
        collection_name="TEST_COLLECTION",
        files_parser={parser: [str(p) for p in hzb_files.values()]},
    )
    runner.run()
    assert len(openbis.new_object.call_args_list) == 7
    cell = next(
        obj for obj in parser.report.objects.values() if obj.name == "Synthetic cell"
    )
    call = next(
        call.kwargs
        for call in openbis.new_object.call_args_list
        if call.kwargs["code"] == cell.code
    )
    assert call["props"][
        cell._property_metadata["working_electrode"].code.lower()
    ].endswith("/" + cell.working_electrode.code)
    assert (
        json.loads(call["props"]["source_record"])["archive"]["data"]["name"]
        == "Synthetic cell"
    )


@pytest.mark.parametrize("version", ["v0", "v1"])
def test_battery_schemas_and_scoped_mandatory_overrides(version):
    classes = get_object_types(version)
    validate_object_type_codes(classes)
    battery_classes = [cls for cls in classes if ".batteries." in cls.__module__]
    assert len(battery_classes) == 9
    # Validate the new exact references against the whole selected catalog. Existing
    # v1 forward references outside this change are intentionally checked separately.
    codes = {cls.defs.code for cls in classes}
    for cls in battery_classes:
        model = json.loads(cls().model_to_json())
        assert model["defs"]["code"] == cls.defs.code
        for prop in cls()._property_metadata.values():
            if prop.data_type == "OBJECT" and prop.object_code not in (None, "(ALL)"):
                assert prop.object_code in codes
    module = importlib.import_module(
        f"bam_masterdata.datamodel.{version}.batteries.object_types"
    )
    assert (
        module.CoinCell.working_electrode.object_code
        == module.ElectrodeSample.defs.code
    )
    assert (
        module.ElectrodeSample.electrode_sheet.object_code
        == module.ElectrodeSheet.defs.code
    )
    if version == "v0":
        assert (
            Chemical.manufacturer.mandatory and Chemical.hazardous_substance.mandatory
        )
        assert Chemical.bam_oe.mandatory and Chemical.bam_location_complete.mandatory
        assert Sample.bam_oe.mandatory
        assert not module.ChemicalStock.manufacturer.mandatory
        assert not module.ElectrodeSample.bam_oe.mandatory
    else:
        assert (
            Activity.inputs.object_code == "ENTITY"
            and Activity.outputs.object_code == "ENTITY"
        )
        assert issubclass(module.CoinCell, Device)
    # The vocabulary setter must choose this version's vocabulary directory.
    assert (
        module.ElectrodeSample(
            name="x",
            **({"lab_id": "x"} if version == "v0" else {"sample_id": "x"}),
            shape="CIRCLE",
        ).shape
        == "CIRCLE"
    )
    with pytest.raises(ValueError, match="not in the list"):
        module.ElectrodeSample(shape="SPHERE")


@pytest.mark.parametrize("version", ["v0", "v1"])
def test_synthetic_nonbattery_extension_without_shared_code_changes(version):
    parser = NomadParser(SyntheticSoftwareMapping(target_version=version))
    files = list(SYNTHETIC.glob("*.json"))
    collection = CollectionType()
    parser.parse(files, collection, Mock())
    objects = {obj.name: obj for obj in parser.report.objects.values()}
    software, execution = objects["Synthetic solver"], objects["Synthetic execution"]
    assert execution.software is software
    assert execution.duration == 120.0
    assert software.version == "1.2"
    assert getattr(
        execution, "finished_flag" if version == "v0" else "activity_status"
    ) == (True if version == "v0" else "COMPLETED")
    assert len(collection.relationships) == 1
    assert json.loads(execution.source_record)["archive"]["data"]["duration"] == {
        "value": 2,
        "unit": "minute",
    }
    classes = [type(software), type(execution)]
    # Include referenced inherited v1 forward targets only when validating its
    # demonstration's own scalar software relation (other base APIs unchanged).
    assert execution._property_metadata["software"].object_code == software.defs.code
    validate_object_type_codes(classes)
    assert "battery" not in parser.report.to_json().lower()
    first = parser.report.to_json()
    parser.parse(list(reversed(files)), CollectionType(), Mock())
    assert parser.report.to_json() == first


@pytest.mark.parametrize(
    "field, value, match",
    [
        ("duration", {"value": 2, "unit": "unknown-unit"}, "Unsupported conversion"),
        ("status", "guessed", "Unsupported synthetic status"),
    ],
)
def test_nonbattery_mapping_errors_are_local_and_atomic(tmp_path, field, value, match):
    source = SYNTHETIC / "execution.archive.json"
    data = json.loads(source.read_text())
    data["data"][field] = value
    changed = tmp_path / "run.json"
    changed.write_text(json.dumps(data))
    parser = NomadParser(SyntheticSoftwareMapping(target_version="v1"))
    collection = CollectionType()
    with pytest.raises(MappingError, match=match):
        parser.parse([SYNTHETIC / "software.archive.json", changed], collection, Mock())
    assert not collection.attached_objects


@pytest.mark.parametrize("version", ["v0", "v1"])
def test_required_object_reference_can_be_bound_after_creation(version):
    mapping = SyntheticSoftwareMapping(target_version=version)

    class RequiredExecution(mapping.execution_type):
        software = mapping.execution_type.software.model_copy(
            update={"mandatory": True}
        )

    mapping.execution_type = RequiredExecution
    parser = NomadParser(mapping)
    parser.parse(list(SYNTHETIC.glob("*.json")), CollectionType(), Mock())
    objects = {obj.name: obj for obj in parser.report.objects.values()}
    assert objects["Synthetic execution"].software is objects["Synthetic solver"]

    class MissingReferenceMapping:
        mapping_id = "synthetic-missing-reference/1"
        target_version = version

        def map(self, context):
            for archive in context.archives:
                context.create(
                    archive, RequiredExecution, {"name": "Unbound execution"}
                )

    parser = NomadParser(MissingReferenceMapping())
    collection = CollectionType()
    with pytest.raises(MappingError, match="missing mandatory target value software"):
        parser.parse([SYNTHETIC / "execution.archive.json"], collection, Mock())
    assert not collection.attached_objects and not collection.relationships
    assert parser.report is None

    class MissingNameMapping(MissingReferenceMapping):
        def map(self, context):
            for archive in context.archives:
                context.create(archive, RequiredExecution, {})

    with pytest.raises(MappingError, match="missing mandatory target value name"):
        NomadParser(MissingNameMapping()).parse(
            [SYNTHETIC / "execution.archive.json"], collection, Mock()
        )
    assert not collection.attached_objects


@pytest.mark.parametrize("version", ["v0", "v1"])
def test_two_synthetic_consumers_share_one_software_object(tmp_path, version):
    """Synthetic shared-target batch; duplicates are consumers, not target inputs."""
    second = json.loads((SYNTHETIC / "execution.archive.json").read_text())
    second["metadata"]["mainfile"] = "second-execution.archive.json"
    second["data"]["name"] = "Second execution"
    second_path = tmp_path / "second-execution.json"
    second_path.write_text(json.dumps(second))
    files = [second_path, *SYNTHETIC.glob("*.json")]
    parser = NomadParser(SyntheticSoftwareMapping(target_version=version))
    parser.parse(files, CollectionType(), Mock())
    objects = {obj.name: obj for obj in parser.report.objects.values()}
    assert len(objects) == 3
    assert objects["Synthetic execution"].software is objects["Synthetic solver"]
    assert objects["Second execution"].software is objects["Synthetic solver"]
    assert (
        sum(
            obj.defs.code == objects["Synthetic solver"].defs.code
            for obj in objects.values()
        )
        == 1
    )
    assert len(parser.report.relationships) == 2
    first = parser.report.to_json()
    parser.parse(list(reversed(files)), CollectionType(), Mock())
    assert parser.report.to_json() == first
