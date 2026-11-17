"""Offline archive regression tests; no live openBIS or NOMAD access."""

import importlib
import json
import random
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

BATTERY = Path(__file__).parents[1] / "data/battery_lab"
SYNTHETIC = Path(__file__).parents[1] / "data/nomad_synthetic"


def battery_parser(version, files=None, exclude_template=True):
    root = BATTERY.parent
    profile = json.loads((root / "nomad_hzb_profile.json").read_text())
    sources = [
        ArchiveSource(root / source["path"], source["upload_id"], source["mainfile"])
        for source in profile["sources"]
    ]
    files = [Path(source.path) for source in sources] if files is None else files
    return NomadParser(
        HZBBatteryMapping(
            target_version=version, quantity_profile=profile["quantity_profile"]
        ),
        sources,
        exclude={root / path: reason for path, reason in profile["exclude"].items()}
        if exclude_template
        else None,
    ), files


def run_battery(version):
    parser, files = battery_parser(version)
    collection = CollectionType()
    parser.parse(files, collection, Mock())
    objects = {obj.name: obj for obj in parser.report.objects.values()}
    return parser, collection, objects


@pytest.mark.parametrize("version", ["v0", "v1"])
def test_actual_hzb_values_identity_and_provenance(version):
    parser, collection, objects = run_battery(version)
    assert len(collection.attached_objects) == 21
    assert len(collection.relationships) == 18
    assert len(parser.report.relationships) == 22  # 18 flow, 2 membership, 2 aliases
    # Assert every observed cross-file reference, the synthesis output, and both
    # local step memberships/task aliases by endpoints and semantic roles.
    assert {
        (
            parser.report.objects[r.parent].name,
            parser.report.objects[r.child].name,
            r.role,
        )
        for r in parser.report.relationships
    } == {
        ("polypropylene for separator", "pp separator stock", "input"),
        ("carbon sulfur sheet", "cs cathode 001", "source_sheet"),
        ("cs cathode 001", "first complete coin cell", "working_electrode"),
        ("Li anode", "first complete coin cell", "counter_electrode"),
        ("pp seperator sample", "first complete coin cell", "separator"),
        ("electrolyte sample", "first complete coin cell", "electrolyte"),
        ("Li chip stock", "Li anode", "source_sheet"),
        ("Sulfur", "Conventional procedure", "input"),
        ("super p", "Conventional procedure", "input"),
        ("Electrolyte solution", "electrolyte sample", "source_stock"),
        ("1,3-Dioxolan", "Electrolyte solution", "solvent"),
        ("1,2-Dimethoxyethan", "Electrolyte solution", "solvent"),
        ("LiTFSI", "Electrolyte solution", "electrolyte salt"),
        ("LiNO3", "Electrolyte solution", "electrolyte salt"),
        ("NMP", "carbon sulfur sheet", "solvent"),
        ("sulfur carbon powder", "carbon sulfur sheet", "active material"),
        ("pp separator stock", "pp seperator sample", "source_stock"),
        ("Conventional procedure", "sulfur carbon powder", "synthesis_output"),
        ("Conventional procedure", "Mixing", "has_step"),
        ("Conventional procedure", "Heating", "has_step"),
        ("Conventional procedure", "Mixing", "workflow_task_alias"),
        ("Conventional procedure", "Heating", "workflow_task_alias"),
    }
    memberships = {
        parser.report.objects[r.child].name: r.qualifiers
        for r in parser.report.relationships
        if r.role == "has_step"
    }
    assert memberships == {"Mixing": {"order": 1}, "Heating": {"order": 2}}
    assert sum(d.code == "excluded" for d in parser.report.diagnostics) == 1
    cell = objects["first complete coin cell"]
    cathode = objects["cs cathode 001"]
    anode = objects["Li anode"]
    assert cell.working_electrode is cathode
    assert cell.counter_electrode is anode
    assert cell.separator is objects["pp seperator sample"]
    assert cell.electrolyte is objects["electrolyte sample"]
    assert cathode.electrode_sheet is objects["carbon sulfur sheet"]
    assert anode.electrode_sheet is objects["Li chip stock"]
    assert cell.case_id == "operando" and cell.case_crimp == "manual"
    assert cathode.thickness == 220.0 and cathode.mass == 0.006
    assert cathode.diameter == 14.0 and cathode.shape == "CIRCLE"
    sheet = objects["carbon sulfur sheet"]
    assert (sheet.length, sheet.width, sheet.area) == (100.0, 200.0, 200.0)
    assert sheet.shape == "RECTANGLE"
    assert "<p>" in sheet.description
    assert sheet.casting_procedure == "Doctor blade casting"
    assert objects["electrolyte sample"].volume == 0.08
    assert objects["Electrolyte solution"].volume == 20.0
    sulfur = objects["Sulfur"]
    assert sulfur.cas_number == "7704-34-9"
    assert sulfur.chemical_formula_descriptive == "S"
    assert sulfur.pubchem_cid == 5362487
    assert getattr(sulfur, "mass_molar" if version == "v0" else "molar_mass") == 32.07
    assert sulfur.product_weight == 50.0
    assert sulfur.shipping_datetime == "2026-06-01T13:44:00.000Z"
    assert sulfur.opening_datetime == "2026-07-01T13:44:00.000Z"
    assert isinstance(sulfur.manufacturer, PropertyTypeAssignment)
    assert isinstance(
        sulfur.responsible_person if version == "v0" else sulfur.responsible_persons,
        PropertyTypeAssignment,
    )
    assert objects["pp separator stock"].product_number == " Lib-PP6025"
    source = json.loads(objects["NMP"].source_record)
    assert (
        source["archive"]["data"]["elemental_composition"][0]["atomic_fraction"]
        == 0.3125
    )
    assert source["quantity_profile"] == "hzb-fixtures-20260701"
    assert source["archive"]["data"]["pure_substance"]["molecular_mass"] == 99.068413911
    powder = objects["sulfur carbon powder"]
    synthesis = objects["Conventional procedure"]
    psource, ssource = (
        json.loads(powder.source_record),
        json.loads(synthesis.source_record),
    )
    assert psource["archive"]["data"]["yield_percent"] == 0.8
    assert psource["archive"]["data"]["aggregated_elements"] == ["S"]
    assert psource["source"] != ssource["source"] and powder.code != synthesis.code
    assert ssource["pointer"] == "/data/synthesis"
    assert ssource["archive"]["data"]["synthesis"]["location"] == "LS224"
    assert objects["Mixing"].step_order == 1 and objects["Heating"].step_order == 2
    assert (
        len([r for r in parser.report.relationships if r.role == "workflow_task_alias"])
        == 2
    )
    assert any(
        r.parent == next(k for k, v in parser.report.objects.items() if v is synthesis)
        and r.child == next(k for k, v in parser.report.objects.items() if v is powder)
        for r in parser.report.relationships
    )
    amounts = [
        r.qualifiers["normalized_quantities"]
        for r in parser.report.relationships
        if "normalized_quantities" in r.qualifiers
    ]
    assert any(
        q.get("concentration_mol")
        == {"value": pytest.approx(1000.0), "unit": "mol/m^3"}
        for q in amounts
    )
    assert any(
        q.get("volume") == {"value": pytest.approx(1e-5), "unit": "m^3"}
        for q in amounts
    )
    sheet_source = json.loads(sheet.source_record)
    assert (
        sheet_source["archive"]["data"]["electrode_materials"][0]["wt_percent"] == 0.49
    )
    assert any(d.code == "unconfirmed_scale" for d in parser.report.diagnostics)
    assert any(d.code == "empty_component" for d in parser.report.diagnostics)
    assert any(
        "/data/notes/description" in d.message
        for d in parser.report.diagnostics
        if d.code == "retained_fields"
    )
    # Portable instance graph serialization retains scalar OBJECT identity and source JSON.
    serialized = json.loads(parser.report.to_json())
    assert len(serialized["objects"]) == 21
    serialized_cell = next(
        obj for obj in serialized["objects"] if obj["code"] == cell.code
    )
    prop = cell._property_metadata["working_electrode"].code
    assert serialized_cell["properties"][prop] == cathode.code
    assert json.loads(sulfur.to_json())["source_record"] == sulfur.source_record


@pytest.mark.parametrize("version", ["v0", "v1"])
def test_hzb_order_independent_and_known_reference_id(version):
    parser, files = battery_parser(version)
    parser.parse(files, CollectionType(), Mock())
    first = parser.report.to_json()
    random.Random(404).shuffle(files)
    parser.parse(files, CollectionType(), Mock())
    assert parser.report.to_json() == first
    assert (
        entry_id("trREfWORRlSa6Ql02biQyw", "cs_cathode_001.archive.json")
        == "1TUOZoR7igwnJnpi3IQPY7ucQwBc"
    )
    # Names cannot select the mapping: preserve mainfile identity while renaming a local copy.


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


def test_incomplete_archive_fails_without_mutating_destination():
    parser, files = battery_parser("v0", exclude_template=False)
    collection = CollectionType()
    with pytest.raises(MappingError, match="missing mandatory value /data/name"):
        parser.parse(files, collection, Mock())
    assert not collection.attached_objects and not collection.relationships
    assert parser.report is None


def modified_archive(tmp_path, source, mutate):
    document = json.loads(source.read_text())
    mutate(document)
    target = tmp_path / source.name
    target.write_text(json.dumps(document))
    return target, ArchiveSource(target, source.parent.name, source.name)


@pytest.mark.parametrize(
    "mutation, match",
    [
        (lambda d: d["data"].update(m_def="unrecognized.Schema"), "unsupported schema"),
        (
            lambda d: d["data"].update(m_def_id="future-version"),
            "unsupported schema hash",
        ),
        (lambda d: d["data"].pop("lab_id"), "missing mandatory value /data/lab_id"),
        (lambda d: d["data"].update(name=""), "missing mandatory text /data/name"),
        (
            lambda d: d["data"].update(datetime="2026-01-01T00:00:00"),
            "explicit UTC offset",
        ),
    ],
)
def test_schema_and_required_field_errors(tmp_path, mutation, match):
    original = next(path for path in BATTERY.rglob("Sulfur.archive.json"))
    path, source = modified_archive(tmp_path, original, mutation)
    parser = NomadParser(
        HZBBatteryMapping(
            target_version="v1", quantity_profile="hzb-fixtures-20260701"
        ),
        [source],
    )
    with pytest.raises(MappingError, match=match):
        parser.parse([path], CollectionType(), Mock())


@pytest.mark.parametrize(
    "reference, match",
    [
        ("../uploads/unknown/archive/missing#/data", "Unresolved archive reference"),
        ("https://example.org/archive/x#/data", "Unsupported archive reference"),
        ("#/data/not_present", "Unresolved section pointer"),
        ("#/data", "exact target"),
    ],
)
def test_reference_failures_are_atomic(tmp_path, reference, match):
    original = next(BATTERY.rglob("cs_cathode_001.archive.json"))
    path, source = modified_archive(
        tmp_path, original, lambda d: d["data"].update(electrode_sheet=reference)
    )
    parser = NomadParser(
        HZBBatteryMapping(
            target_version="v1", quantity_profile="hzb-fixtures-20260701"
        ),
        [source],
    )
    collection = CollectionType()
    with pytest.raises(MappingError, match=match):
        parser.parse([path], collection, Mock())
    assert not collection.attached_objects and not collection.relationships


def test_unknown_geometry_hash_and_missing_component_reference(tmp_path):
    original = next(BATTERY.rglob("Li_chip_stock.archive.json"))

    def change(document):
        document["data"]["dimensions_and_weights"]["shape"]["m_def_id"] = "unknown"

    path, source = modified_archive(tmp_path, original, change)
    parser = NomadParser(
        HZBBatteryMapping(
            target_version="v0", quantity_profile="hzb-fixtures-20260701"
        ),
        [source],
    )
    with pytest.raises(MappingError, match="unsupported nested schema hash"):
        parser.parse([path], CollectionType(), Mock())
    original = next(BATTERY.rglob("Sulfur.archive.json"))
    path, source = modified_archive(
        tmp_path, original, lambda d: d["data"].update(chemicals=[{"role": "solvent"}])
    )
    parser.sources = {path.resolve(): source}
    with pytest.raises(MappingError, match="component has no chemical reference"):
        parser.parse([path], CollectionType(), Mock())


def test_duplicate_source_identity(tmp_path):
    original = next(BATTERY.rglob("Sulfur.archive.json"))
    second = tmp_path / "other.json"
    second.write_text(original.read_text())
    source = ArchiveSource(second, original.parent.name, original.name)
    parser = NomadParser(
        HZBBatteryMapping(
            target_version="v0", quantity_profile="hzb-fixtures-20260701"
        ),
        [ArchiveSource(original, original.parent.name, original.name), source],
    )
    parser.parse([original, second], CollectionType(), Mock())
    assert len(parser.report.objects) == 1
    assert any(d.code == "duplicate_input" for d in parser.report.diagnostics)
    data = json.loads(second.read_text())
    data["data"]["name"] = "conflict"
    second.write_text(json.dumps(data))
    with pytest.raises(MappingError, match="duplicate source identity"):
        parser.parse([second, original], CollectionType(), Mock())


def test_units_and_explicit_profile():
    context = ArchiveContext([], "test", "v1")
    assert context.quantity(0.08, "mL", "uL") == pytest.approx(80)
    assert context.quantity(0.006, "g", "mg") == pytest.approx(6)
    assert context.quantity(220, "um", "mm") == pytest.approx(0.22)
    for value, source, target in [
        (1, "unobtainium", "g"),
        (1, "g", "mL"),
        (True, "g", "g"),
        (float("inf"), "g", "g"),
    ]:
        with pytest.raises(MappingError):
            context.quantity(value, source, target)
    with pytest.raises(MappingError, match="quantity profile"):
        HZBBatteryMapping(target_version="v1", quantity_profile="guess")
    with pytest.raises(MappingError, match="target version"):
        HZBBatteryMapping(target_version="v2", quantity_profile="hzb-fixtures-20260701")


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


@pytest.mark.parametrize("runner_type", [RunParsers, RunParsersWithTransactions])
@pytest.mark.parametrize("version", ["v0", "v1"])
def test_hzb_existing_runner_mock_compatibility(runner_type, version):
    parser, files = battery_parser(version)
    openbis = openbis_runner_mock()
    runner = runner_type(
        openbis=openbis,
        space_name="TEST_SPACE",
        project_name="TEST_PROJECT",
        collection_name="TEST_COLLECTION",
        files_parser={parser: [str(p) for p in files]},
    )
    runner.run()
    assert len(openbis.new_object.call_args_list) == 21
    cell = next(
        obj
        for obj in parser.report.objects.values()
        if obj.name == "first complete coin cell"
    )
    call = next(
        call.kwargs
        for call in openbis.new_object.call_args_list
        if call.kwargs["code"] == cell.code
    )
    field = cell._property_metadata["working_electrode"].code.lower()
    assert call["props"][field].endswith("/" + cell.working_electrode.code)
    assert (
        json.loads(call["props"]["source_record"])["archive"]["data"]["case_crimp"]
        == "manual"
    )


def test_explicit_identity_survives_filename_change_and_metadata_conflict(tmp_path):
    original = next(BATTERY.rglob("Sulfur.archive.json"))
    renamed = tmp_path / "arbitrary-file.json"
    renamed.write_text(original.read_text())
    parser = NomadParser(
        HZBBatteryMapping(
            target_version="v1", quantity_profile="hzb-fixtures-20260701"
        ),
        [ArchiveSource(renamed, original.parent.name, original.name)],
    )
    parser.parse([renamed], CollectionType(), Mock())
    key = next(iter(parser.report.objects))
    assert key.entry_id == "69P69T9QcaSTTApwcuJLmRKpchxf"
    data = json.loads(renamed.read_text())
    data["metadata"] = {"upload_id": "conflicting"}
    renamed.write_text(json.dumps(data))
    with pytest.raises(MappingError, match="conflicting source metadata upload_id"):
        parser.parse([renamed], CollectionType(), Mock())
    with pytest.raises(MappingError, match="missing source identity"):
        NomadParser(SyntheticSoftwareMapping(target_version="v1")).parse(
            [original], CollectionType(), Mock()
        )


def test_explicit_profile_covers_recursive_inventory():
    profile = json.loads((BATTERY.parent / "nomad_hzb_profile.json").read_text())
    assert {Path(s["path"]) for s in profile["sources"]} == {
        p.relative_to(BATTERY.parent) for p in BATTERY.rglob("*.archive.json")
    }
    assert len(profile["sources"]) == 19


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
def test_synthetic_component_masses_use_section_specific_profile_units(
    tmp_path, version
):
    """Synthetic variations: actual HZB fixtures omit component mass fields."""
    original = next(BATTERY.rglob("carbon_sulfur_sheet.archive.json"))

    def add_masses(document):
        document["data"]["chemicals"][0]["mass"] = 1  # BS_ChemicalReference: gram
        document["data"]["electrode_materials"][0]["mass"] = (
            1  # ActiveMaterialComponent: milligram
        )

    path, source = modified_archive(tmp_path, original, add_masses)
    parser, files = battery_parser(version)
    parser.sources[path.resolve()] = source
    files = [path if file == original else file for file in files]
    parser.parse(files, CollectionType(), Mock())
    rows = {
        relation.role: relation.qualifiers
        for relation in parser.report.relationships
        if parser.report.objects[relation.child].name == "carbon sulfur sheet"
    }
    assert rows["solvent"]["normalized_quantities"]["mass"] == {
        "value": pytest.approx(1e-3),
        "unit": "kg",
    }
    assert rows["active material"]["normalized_quantities"]["mass"] == {
        "value": pytest.approx(1e-6),
        "unit": "kg",
    }
    assert rows["solvent"]["source_row"]["mass"] == 1
    assert rows["active material"]["source_row"]["mass"] == 1


@pytest.mark.parametrize(
    "filename, subsection, wrong_schema, wrong_hash",
    [
        (
            "Sulfur.archive.json",
            ("pure_substance",),
            "nomad_battery_space.schema_packages.utilities.geometry.CircleGeometry",
            "1e38604aef43d4a409d9596ad0467de1f78a49b3",
        ),
        (
            "Li_chip_stock.archive.json",
            ("dimensions_and_weights",),
            "nomad_battery_space.schema_packages.utilities.dimensions.VolumeAndWeights",
            "c2ef11b16a35e4f33d162888193a5f19cf513362",
        ),
        (
            "Electrolyte_solution.archive.json",
            ("volume_and_weights",),
            "nomad_battery_space.schema_packages.utilities.dimensions.DimensionsAndWeights",
            "417ba7756e5f36ac8e1bc25e5a8a94df5a83a390",
        ),
        (
            "Li_chip_stock.archive.json",
            ("dimensions_and_weights", "shape"),
            "nomad.datamodel.metainfo.basesections.v1.PubChemPureSubstanceSection",
            "c791a67f2948054b5b24584fdd865478c0024779",
        ),
    ],
)
def test_recognized_nested_schema_cannot_be_used_at_wrong_path(
    tmp_path, filename, subsection, wrong_schema, wrong_hash
):
    original = next(BATTERY.rglob(filename))

    def replace_schema(document):
        section = document["data"]
        for part in subsection:
            section = section[part]
        section.update(m_def=wrong_schema, m_def_id=wrong_hash)

    path, source = modified_archive(tmp_path, original, replace_schema)
    parser = NomadParser(
        HZBBatteryMapping(
            target_version="v1", quantity_profile="hzb-fixtures-20260701"
        ),
        [source],
    )
    with pytest.raises(MappingError, match="unsupported nested schema .* at this path"):
        parser.parse([path], CollectionType(), Mock())


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
