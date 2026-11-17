"""HZB battery mapping with caller-verified source schema revisions.

Units are selected by the named laboratory profile, never inferred from numeric
magnitudes. Callers must supply the exact schema IDs they have inspected; no
laboratory records or default schema revision allowlist are bundled here.
"""

import importlib
from datetime import datetime

from .core import ArchiveContext, MappingError

_PACKAGE = "nomad_battery_space.schema_packages."
_BASE = _PACKAGE + "hzb_bs_package."
_ASSEMBLY = _PACKAGE + "hzb_bs_assembly_package."
_SCHEMAS = {
    _BASE + "BS_Chemical": "ChemicalStock",
    _BASE + "ElectrodeMaterial": "ElectrodeMaterial",
    _BASE + "ElectrodeSheet": "ElectrodeSheet",
    _BASE + "ElectrolyteStock": "ElectrolyteStock",
    _BASE + "SeparatorStock": "SeparatorStock",
    _BASE + "ElectrodeSample": "ElectrodeSample",
    _BASE + "ElectrolyteSample": "ElectrolyteSample",
    _BASE + "SeparatorSample": "SeparatorSample",
    _ASSEMBLY + "CoinCellBattery": "CoinCell",
}
_NESTED_SCHEMAS = {
    _PACKAGE + "utilities.dimensions.DimensionsAndWeights",
    _PACKAGE + "utilities.dimensions.VolumeAndWeights",
    _PACKAGE + "utilities.geometry.CircleGeometry",
    _PACKAGE + "utilities.geometry.RectangleGeometry",
    "nomad.datamodel.metainfo.basesections.v1.PubChemPureSubstanceSection",
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

    def __init__(
        self,
        *,
        target_version: str,
        quantity_profile: str,
        schema_ids: dict[str, set[str]],
    ):
        if target_version not in ("v0", "v1"):
            raise MappingError(f"Unsupported target version: {target_version}")
        if quantity_profile != "hzb-laboratory-units-v1":
            raise MappingError(
                "Select the explicit hzb-laboratory-units-v1 quantity profile"
            )
        if not isinstance(schema_ids, dict) or not schema_ids:
            raise MappingError(
                "Supply explicit inspected schema_ids for the HZB mapping"
            )
        supported = set(_SCHEMAS) | _NESTED_SCHEMAS
        for name, ids in schema_ids.items():
            if name not in supported:
                raise MappingError(f"Unsupported configured schema: {name}")
            if (
                not isinstance(ids, (set, frozenset, list, tuple))
                or not ids
                or any(not isinstance(value, str) or not value.strip() for value in ids)
            ):
                raise MappingError(
                    f"schema_ids[{name!r}] requires a nonempty collection of explicit IDs"
                )
        self.schema_ids = {name: frozenset(ids) for name, ids in schema_ids.items()}
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
            # Inline subsections without schema tags use the explicitly selected
            # parent schema/profile's field layout.
            if "m_def_id" in section:
                raise MappingError(f"{archive.key()}{path}: schema hash without m_def")
            return
        name = context.value(archive, path + "/m_def")
        if name not in _NESTED_SCHEMAS or name not in expected_schemas:
            raise MappingError(
                f"{archive.key()}{path}: unsupported nested schema {name} at this path"
            )
        if context.value(archive, path + "/m_def_id", None) not in self.schema_ids.get(
            name, ()
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
            class_name = _SCHEMAS[schema]
            cls = getattr(self.targets, class_name)
            values = self._values(context, archive, cls)
            if context.value(
                archive, "/data/m_def_id", None
            ) not in self.schema_ids.get(schema, ()):
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
