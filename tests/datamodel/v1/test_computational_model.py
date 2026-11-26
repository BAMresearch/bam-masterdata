import ast
from pathlib import Path

import pytest

from bam_masterdata.checker.schema_validator import get_object_types
from bam_masterdata.datamodel import v1
from bam_masterdata.datamodel.v1.activities import (
    Computation,
    EquationOfStateFit,
    GeometryOptimization,
    MolecularDynamics,
    Simulation,
    SinglePointCalculation,
)
from bam_masterdata.datamodel.v1.entities import (
    CalculationDatum,
    ElectronicStructureParameters,
    EquationOfStateFitParameters,
    GeometryOptimizationParameters,
    MolecularDynamicsParameters,
    ParameterSet,
)

RESULT_SECTIONS = {"Results", "Electronic Structure Results"}
GENERAL_SECTIONS = {"General Information"}

ACTIVITY_RESULTS = [
    (SinglePointCalculation, "single_point_results"),
    (GeometryOptimization, "geometry_optimization_results"),
    (MolecularDynamics, "molecular_dynamics_results"),
    (EquationOfStateFit, "equation_of_state_fit_results"),
]

EXECUTION_PROPERTIES = {
    "executed_on",
    "walltime_h",
    "core_time_h",
    "n_cores",
    "n_gpus",
    "n_threads",
    "hpc_job_queue",
    "hpc_job_id",
}

# IRIs allowed in datamodel/v1 for the computation schema (verified against PMDco, OBO, ASMO, CMSO).
ALLOWED_NEW_IRIS = {
    "https://w3id.org/pmd/co/PMD_0000583",
    "https://w3id.org/pmd/co/PMD_0000933",
    "https://w3id.org/pmd/co/PMD_0000862",
    "https://w3id.org/pmd/co/PMD_0000931",
    "https://w3id.org/pmd/co/PMD_0000582",
    "https://w3id.org/pmd/co/PMD_0025035",
    "http://purl.obolibrary.org/obo/IAO_0000027",
    "http://purl.obolibrary.org/obo/IAO_0000109",
    "http://purl.obolibrary.org/obo/IAO_0000136",
    "http://purl.obolibrary.org/obo/OBI_0000293",
    "http://purl.obolibrary.org/obo/OBI_0000299",
    "http://purl.obolibrary.org/obo/RO_0000057",
    "http://purls.helmholtz-metadaten.de/cmso/ComputationalSample",
}
# IRIs that were already in datamodel/v1 on dev and are inherited by the computation types.
PREEXISTING_IRIS = {
    "http://purl.obolibrary.org/obo/BFO_0000001",
    "http://purl.obolibrary.org/obo/BFO_0000002",
    "http://purl.obolibrary.org/obo/BFO_0000015",
    "http://purl.obolibrary.org/obo/BFO_0000040",
    "http://purl.obolibrary.org/obo/IAO_0000010",
    "http://purl.obolibrary.org/obo/IAO_0000030",
    "http://www.w3.org/ns/prov#Activity",
    "http://www.w3.org/ns/prov#Entity",
    "https://w3id.org/pmd/co/PMD_0000602",
}
ASMO_PREFIX = "https://purls.helmholtz-metadaten.de/asmo/"
COMPUTATION_MODULES = (
    "bam_masterdata.datamodel.v1.activities",
    "bam_masterdata.datamodel.v1.entities",
)


def _computation_types():
    """Object types of the computation schema: computations and the entities they use."""
    used = (Computation, ParameterSet, CalculationDatum)
    names = {
        "SIMULATED_SYSTEM",
        "COMPUTATIONAL_METHOD",
        "HPC",
        "DATA_ITEM",
        "MEASUREMENT_DATUM",
    }
    return [
        cls
        for cls in get_object_types("v1")
        if issubclass(cls, used) or cls.defs.code in names
    ]


@pytest.mark.parametrize(
    "activity, property_name", ACTIVITY_RESULTS, ids=lambda x: getattr(x, "__name__", x)
)
def test_activities_link_to_one_results_type(activity, property_name):
    prop = activity()._property_metadata[property_name]
    assert not prop.multivalued
    targets = [
        cls for cls in get_object_types("v1") if cls.defs.code == prop.object_code
    ]
    assert len(targets) == 1
    assert issubclass(targets[0], CalculationDatum)


def test_results_types_describe_a_simulated_system():
    for cls in CalculationDatum.__subclasses__():
        prop = cls()._property_metadata["described_system"]
        assert prop.object_code == "SIMULATED_SYSTEM"


def test_results_types_hold_only_results():
    for cls in CalculationDatum.__subclasses__():
        sections = {prop.section for prop in cls().properties}
        assert sections <= RESULT_SECTIONS | GENERAL_SECTIONS, cls.__name__


def test_parameter_sets_hold_no_results():
    for cls in get_object_types("v1"):
        if issubclass(cls, ParameterSet):
            sections = {prop.section for prop in cls().properties}
            assert not sections & RESULT_SECTIONS, cls.__name__


def test_execution_details_belong_to_computation():
    assert EXECUTION_PROPERTIES <= set(Computation()._property_metadata)
    declared_on_simulation = {
        name for name, value in vars(Simulation).items() if name in EXECUTION_PROPERTIES
    }
    assert not declared_on_simulation
    assert Computation()._property_metadata["executed_on"].object_code == "HPC"


@pytest.mark.parametrize(
    "activity, property_name, specification",
    [
        *[
            (cls, "electronic_structure_parameters", ElectronicStructureParameters)
            for cls in (SinglePointCalculation, GeometryOptimization, MolecularDynamics)
        ],
        (
            GeometryOptimization,
            "geometry_optimization_parameters",
            GeometryOptimizationParameters,
        ),
        (
            MolecularDynamics,
            "molecular_dynamics_parameters",
            MolecularDynamicsParameters,
        ),
        (
            EquationOfStateFit,
            "equation_of_state_fit_parameters",
            EquationOfStateFitParameters,
        ),
    ],
)
def test_activities_reference_their_specification(
    activity, property_name, specification
):
    prop = activity()._property_metadata[property_name]
    assert prop.object_code == specification.defs.code


def test_mixins_are_not_object_types():
    assert not [cls for cls in get_object_types("v1") if cls.__name__.startswith("_")]


def test_computation_schema_uses_only_allowed_iris():
    unexpected = set()
    for cls in _computation_types():
        if cls.__module__ not in COMPUTATION_MODULES:
            continue
        iris = list(cls.defs.iri or [])
        iris += [iri for prop in cls().properties for iri in (prop.iri or [])]
        unexpected |= {
            iri
            for iri in iris
            if iri not in ALLOWED_NEW_IRIS | PREEXISTING_IRIS
            and not iri.startswith(ASMO_PREFIX)
        }
    assert not unexpected, unexpected


def test_classes_without_defs_are_private_mixins():
    # The hierarchy comment generator leaves out classes whose name starts with "_".
    # A mixin without the underscore would be drawn as a parent type, so require it.
    offending = []
    for path in sorted(Path(v1.__file__).parent.rglob("*.py")):
        for node in ast.parse(path.read_text(encoding="utf-8")).body:
            if not isinstance(node, ast.ClassDef) or node.name.startswith("_"):
                continue
            has_defs = any(
                isinstance(stmt, ast.Assign)
                and any(
                    getattr(target, "id", None) == "defs" for target in stmt.targets
                )
                for stmt in node.body
            )
            if not has_defs:
                offending.append(f"{path.name}:{node.name}")
    assert not offending, offending
