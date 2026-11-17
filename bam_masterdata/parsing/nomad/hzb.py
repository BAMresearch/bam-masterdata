"""Mapping of the explicitly approved July 2026 HZB battery fixture schemas.

Units are selected by the named profile, never inferred from numeric magnitudes.
The current upstream definitions informed the profile but are not asserted to
reproduce the archived schema hashes. Original claims are retained unchanged.
"""

import importlib
from datetime import datetime

from .core import ArchiveContext, MappingError

_PACKAGE = "nomad_battery_space.schema_packages."
_BASE = _PACKAGE + "hzb_bs_package."
_ASSEMBLY = _PACKAGE + "hzb_bs_assembly_package."
_SCHEMAS = {
    _BASE + "BS_Chemical": (
        "ChemicalStock",
        {"a890d00a32114b167c346a1b77bb4b0b6684647e"},
    ),
    _BASE + "ElectrodeMaterial": (
        "ElectrodeMaterial",
        {"da3dc4603bd0041c6533ad2744a20d520aa4874f"},
    ),
    _BASE + "ElectrodeSheet": (
        "ElectrodeSheet",
        {
            "5e5a8c5eb2e26738b98527463721b048f5df2700",
            "ee83cc49256b525f2ff0c3be4114b36430070592",
        },
    ),
    _BASE + "ElectrolyteStock": (
        "ElectrolyteStock",
        {"f0fdf25cb3f6ac969fe07cdd7d02faf4958b268b"},
    ),
    _BASE + "SeparatorStock": (
        "SeparatorStock",
        {"366d860afc6082a5cf5f65447310304524b10ccd"},
    ),
    _BASE + "ElectrodeSample": (
        "ElectrodeSample",
        {"e89299a9a5000e66167a25256b2657a9b7034d81"},
    ),
    _BASE + "ElectrolyteSample": (
        "ElectrolyteSample",
        {"d818862e3a928e841e7eb0257fca23f5dbdba58b"},
    ),
    _BASE + "SeparatorSample": (
        "SeparatorSample",
        {"10970052e1adc650de1a77215385620afb47f141"},
    ),
    _ASSEMBLY + "CoinCellBattery": (
        "CoinCell",
        {"2ed2217e330c535a18e8e9e3a9c7fea54d92a1c8"},
    ),
}
_NESTED_SCHEMAS = {
    _PACKAGE + "utilities.dimensions.DimensionsAndWeights": {
        "417ba7756e5f36ac8e1bc25e5a8a94df5a83a390"
    },
    _PACKAGE + "utilities.dimensions.VolumeAndWeights": {
        "c2ef11b16a35e4f33d162888193a5f19cf513362"
    },
    _PACKAGE + "utilities.geometry.CircleGeometry": {
        "1e38604aef43d4a409d9596ad0467de1f78a49b3"
    },
    _PACKAGE + "utilities.geometry.RectangleGeometry": {
        "3a0acb067f054e91ebc2d1f007a3ca5bfef75818",
        "c2af99b498e9781941d27b19fb11c89d453ae94a",
    },
    "nomad.datamodel.metainfo.basesections.v1.PubChemPureSubstanceSection": {
        "c791a67f2948054b5b24584fdd865478c0024779"
    },
}
_UNITS = {
    "thickness": "um",
    "mass": "g",
    "length": "mm",
    "width": "mm",
    "diameter": "mm",
    "area": "cm^2",
    "volume": "mL",
}


class HZBBatteryMapping:
    mapping_id = "hzb-battery/1"

    def __init__(self, *, target_version: str, quantity_profile: str):
        if target_version not in ("v0", "v1"):
            raise MappingError(f"Unsupported target version: {target_version}")
        if quantity_profile != "hzb-fixtures-20260701":
            raise MappingError(
                "Select the explicitly approved hzb-fixtures-20260701 quantity profile"
            )
        self.target_version = target_version
        self.quantity_profile = quantity_profile
        self.targets = importlib.import_module(
            f"bam_masterdata.datamodel.{target_version}.batteries.object_types"
        )
        activities = importlib.import_module(
            f"bam_masterdata.datamodel.{target_version}."
            + ("object_types" if target_version == "v0" else "activities")
        )
        if target_version == "v0":
            self.synthesis_type = self.step_type = activities.ExperimentalStep
        else:
            self.synthesis_type, self.step_type = (
                activities.Synthesis,
                activities.Processing,
            )

    def _timestamp(self, context, archive, path):
        value = context.value(archive, path)
        if not isinstance(value, str):
            raise MappingError(f"{archive.key()}{path}: expected timestamp string")
        try:
            parsed = datetime.fromisoformat(value)
        except ValueError as exc:
            raise MappingError(f"{archive.key()}{path}: invalid timestamp") from exc
        if parsed.utcoffset() is None:
            raise MappingError(
                f"{archive.key()}{path}: timestamp needs an explicit UTC offset"
            )
        return value

    def _nested_schema(self, context, archive, path, section, expected_schemas):
        if "m_def" not in section:
            # Several observed inline subsections omit schema tags. Their parent
            # schema/profile establishes the field layout explicitly.
            if "m_def_id" in section:
                raise MappingError(f"{archive.key()}{path}: schema hash without m_def")
            return
        name = context.value(archive, path + "/m_def")
        allowed = _NESTED_SCHEMAS.get(name)
        if allowed is None or name not in expected_schemas:
            raise MappingError(
                f"{archive.key()}{path}: unsupported nested schema {name} at this path"
            )
        if (
            "m_def_id" in section
            and context.value(archive, path + "/m_def_id") not in allowed
        ):
            raise MappingError(f"{archive.key()}{path}: unsupported nested schema hash")

    def _values(self, context, archive, cls):
        data = archive.document["data"]
        values = {"name": context.required_text(archive, "/data/name")}
        lab_id = context.required_text(archive, "/data/lab_id")
        identifier = (
            "lab_id"
            if self.target_version == "v0"
            or cls.__name__ in ("ChemicalStock", "CoinCell")
            else ("sample_id" if cls.__name__.endswith("Sample") else "material_id")
        )
        values[identifier] = lab_id
        meta = cls()._property_metadata
        if "datetime" in data:
            values["record_datetime"] = self._timestamp(
                context, archive, "/data/datetime"
            )
        for name in ("description", "casting_procedure", "case_id", "case_crimp"):
            if name in data:
                values[name] = context.value(archive, "/data/" + name)
        product = data.get("product_info", {})
        for source, target in (
            ("supplier", "supplier"),
            ("lot_number", "lot_number"),
            ("product_number", "product_number"),
        ):
            if source in product and target in meta:
                values[target] = context.value(archive, "/data/product_info/" + source)
        for source, target in (
            ("shipping_date", "shipping_datetime"),
            ("opening_date", "opening_datetime"),
        ):
            if source in product and target in meta:
                values[target] = self._timestamp(
                    context, archive, "/data/product_info/" + source
                )
        for source, target, unit in (
            ("product_weight", "product_weight", "g"),
            ("product_volume", "product_volume", "mL"),
        ):
            if source in product and target in meta:
                values[target] = context.quantity(
                    context.value(archive, "/data/product_info/" + source),
                    unit,
                    meta[target].units,
                )
        pure = data.get("pure_substance", {})
        if pure:
            self._nested_schema(
                context,
                archive,
                "/data/pure_substance",
                pure,
                {
                    "nomad.datamodel.metainfo.basesections.v1.PubChemPureSubstanceSection"
                },
            )
        fields = {
            "iupac_name": "iupac_name",
            "cas_number": "cas_number",
            "molecular_formula": "chemical_formula_descriptive",
            "inchi": "inchi",
            "inchi_key": "inchi_key",
            "smile": "smiles",
            "pub_chem_cid": "pubchem_cid",
            "pub_chem_link": "pubchem_link",
        }
        for source, target in fields.items():
            if source in pure and target in meta:
                values[target] = context.value(
                    archive, "/data/pure_substance/" + source
                )
        if "molar_mass" in pure:
            target = "mass_molar" if self.target_version == "v0" else "molar_mass"
            values[target] = context.quantity(
                context.value(archive, "/data/pure_substance/molar_mass"),
                "g/mol",
                "g/mol",
            )
        for subsection in ("dimensions_and_weights", "volume_and_weights"):
            dimensions = data.get(subsection, {})
            if not dimensions:
                continue
            path = "/data/" + subsection
            expected = (
                "DimensionsAndWeights"
                if subsection == "dimensions_and_weights"
                else "VolumeAndWeights"
            )
            self._nested_schema(
                context,
                archive,
                path,
                dimensions,
                {_PACKAGE + "utilities.dimensions." + expected},
            )
            for name in ("thickness", "mass", "volume"):
                if name in dimensions and name in meta:
                    values[name] = context.quantity(
                        context.value(archive, path + "/" + name),
                        _UNITS[name],
                        meta[name].units,
                    )
            if "shape" in dimensions:
                shape = dimensions["shape"]
                shape_path = path + "/shape"
                self._nested_schema(
                    context,
                    archive,
                    shape_path,
                    shape,
                    {
                        _PACKAGE + "utilities.geometry.CircleGeometry",
                        _PACKAGE + "utilities.geometry.RectangleGeometry",
                    },
                )
                schema = context.required_text(archive, shape_path + "/m_def")
                vocabulary = {
                    _PACKAGE + "utilities.geometry.CircleGeometry": "CIRCLE",
                    _PACKAGE + "utilities.geometry.RectangleGeometry": "RECTANGLE",
                }
                if schema not in vocabulary:
                    raise MappingError(f"Unsupported geometry schema {schema}")
                values["shape"] = vocabulary[schema]
                for name in ("length", "width", "diameter", "area"):
                    if name in shape:
                        values[name] = context.quantity(
                            context.value(archive, shape_path + "/" + name),
                            _UNITS[name],
                            meta[name].units,
                        )
        return values

    def map(self, context: ArchiveContext) -> None:
        # Materialize all identities before resolving references between files.
        for archive in context.archives:
            schema = context.required_text(archive, "/data/m_def")
            if schema not in _SCHEMAS:
                raise MappingError(
                    f"{archive.source.path}: unsupported schema {schema}"
                )
            class_name, hashes = _SCHEMAS[schema]
            cls = getattr(self.targets, class_name)
            values = self._values(context, archive, cls)
            if context.value(archive, "/data/m_def_id", None) not in hashes:
                raise MappingError(
                    f"{archive.source.path}: unsupported schema hash for {schema}"
                )
            context.create(archive, cls, values, profile=self.quantity_profile)
            data = archive.document["data"]
            if "yield_percent" in data:
                context.diagnostic(
                    archive,
                    "/data/yield_percent",
                    "unconfirmed_scale",
                    "Retained exact value; no percent/fraction normalization",
                )
            if "synthesis" in data:
                synthesis = data["synthesis"]
                parent = context.create(
                    archive,
                    self.synthesis_type,
                    {"name": context.required_text(archive, "/data/synthesis/name")},
                    pointer="/data/synthesis",
                    profile=self.quantity_profile,
                )
                context.relate(
                    parent,
                    archive.key(),
                    role="synthesis_output",
                    source_pointer="/data/synthesis",
                )
                for index, step in enumerate(synthesis.get("steps", [])):
                    pointer = f"/data/synthesis/steps/{index}"
                    key = context.create(
                        archive,
                        self.step_type,
                        {
                            "name": context.required_text(archive, pointer + "/name"),
                            "step_order": index + 1,
                        },
                        pointer=pointer,
                        profile=self.quantity_profile,
                    )
                    context.relate(
                        parent,
                        key,
                        role="has_step",
                        source_pointer=pointer,
                        qualifiers={"order": index + 1},
                        provenance=False,
                    )

        scalar = {
            "electrode_sheet": "source_sheet",
            "electrolyte_stock": "source_stock",
            "separator_stock": "source_stock",
            "working_electrode": "working_electrode",
            "counter_electrode": "counter_electrode",
            "separator": "separator",
            "electrolyte": "electrolyte",
        }
        for archive in context.archives:
            data = archive.document["data"]
            owner = archive.key()
            for attribute, role in scalar.items():
                if attribute in data:
                    context.reference(
                        archive,
                        owner,
                        "/data/" + attribute,
                        attribute=attribute,
                        role=role,
                    )
            for section, reference_field in (
                ("chemicals", "chemical"),
                ("electrode_materials", "material"),
            ):
                for index, component in enumerate(data.get(section, [])):
                    pointer = f"/data/{section}/{index}"
                    if not component:
                        context.diagnostic(
                            archive,
                            pointer,
                            "empty_component",
                            "Empty placeholder retained; no object or relationship invented",
                        )
                        continue
                    if reference_field not in component:
                        raise MappingError(
                            f"{archive.key()}{pointer}: component has no {reference_field} reference"
                        )
                    target_owner = (
                        archive.key("/data/synthesis")
                        if "synthesis" in data and section == "chemicals"
                        else owner
                    )
                    qualifiers = {"source_row": component}
                    normalized = {}
                    for quantity, source_unit, target_unit in (
                        ("volume", "mL", "m^3"),
                        ("mass", "g" if section == "chemicals" else "mg", "kg"),
                        ("concentration_mol", "mol/L", "mol/m^3"),
                    ):
                        if quantity in component:
                            value = context.value(archive, pointer + "/" + quantity)
                            normalized[quantity] = {
                                "value": context.quantity(
                                    value, source_unit, target_unit
                                ),
                                "unit": target_unit,
                            }
                    if normalized:
                        qualifiers["normalized_quantities"] = normalized
                    role = component.get("role", "input")
                    if "role" in component:
                        context.value(archive, pointer + "/role")
                    if "wt_percent" in component:
                        context.diagnostic(
                            archive,
                            pointer + "/wt_percent",
                            "unconfirmed_scale",
                            "Retained exact value; no percent/fraction normalization",
                        )
                    target = context.reference(
                        archive,
                        target_owner,
                        pointer + "/" + reference_field,
                        role=role,
                        qualifiers=qualifiers,
                    )
                    expected = (
                        self.targets.ChemicalStock
                        if section == "chemicals"
                        else self.targets.ElectrodeMaterial
                    )
                    if context.objects[target].defs.code != expected.defs.code:
                        raise MappingError(
                            f"{archive.key()}{pointer}: wrong exact component target; expected {expected.defs.code}"
                        )
            for index, task in enumerate(
                archive.document.get("workflow2", {}).get("tasks", [])
            ):
                pointer = f"/workflow2/tasks/{index}"
                reference = context.value(archive, pointer + "/section")
                target = context.resolve(archive, reference)
                if not target.pointer.startswith("/data/synthesis/steps/"):
                    raise MappingError(
                        f"{archive.key()}{pointer}: workflow task must alias an existing synthesis step"
                    )
                if task.get("name") != context.objects[target].name:
                    raise MappingError(
                        f"{archive.key()}{pointer}: workflow task name differs from referenced step"
                    )
                context.value(archive, pointer + "/name")
                context.relate(
                    archive.key("/data/synthesis"),
                    target,
                    role="workflow_task_alias",
                    source_pointer=pointer,
                    provenance=False,
                )
