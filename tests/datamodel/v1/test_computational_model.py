import inspect
import json

import pytest

from bam_masterdata.datamodel.v1 import activities, entities, vocabularies
from bam_masterdata.datamodel.v1.activities import (
    Analysis,
    AtomisticSimulation,
    BondingEnvironmentAnalysis,
    ChemicalBondingAnalysis,
    CreepTestDataProcessing,
    EquationOfStateFit,
    GeometryOptimization,
    MolecularDynamics,
    OrbitalProjection,
    ProjectionQualityAssessment,
    Simulation,
    SimulationAnalysis,
    SinglePointCalculation,
)
from bam_masterdata.datamodel.v1.entities import (
    BondingAnalysisParameters,
    BondingEnvironmentParameters,
    Context,
    ElectronicStructureParameters,
    EquationOfStateFitParameters,
    GeometryOptimizationParameters,
    InputSpecification,
    MolecularDynamicsParameters,
    OrbitalProjectionParameters,
    ProjectionQualityParameters,
)
from bam_masterdata.metadata.entities import VocabularyType

NEW_ACTIVITIES = [
    AtomisticSimulation,
    SinglePointCalculation,
    GeometryOptimization,
    MolecularDynamics,
    SimulationAnalysis,
    OrbitalProjection,
    ProjectionQualityAssessment,
    ChemicalBondingAnalysis,
    BondingEnvironmentAnalysis,
    EquationOfStateFit,
]

SIMULATION_ANALYSES = [
    OrbitalProjection,
    ProjectionQualityAssessment,
    ChemicalBondingAnalysis,
    BondingEnvironmentAnalysis,
    EquationOfStateFit,
]

SPECIFICATIONS = [
    ElectronicStructureParameters,
    GeometryOptimizationParameters,
    MolecularDynamicsParameters,
    EquationOfStateFitParameters,
    OrbitalProjectionParameters,
    ProjectionQualityParameters,
    BondingAnalysisParameters,
    BondingEnvironmentParameters,
]


@pytest.mark.parametrize(
    "cls", NEW_ACTIVITIES + SPECIFICATIONS, ids=lambda cls: cls.__name__
)
def test_types_can_be_instantiated_and_exported(cls):
    obj = cls()
    exported = obj.model_to_dict()
    assert exported["defs"]["code"] == cls.defs.code
    assert json.loads(obj.model_to_json()) == exported


@pytest.mark.parametrize("cls", SPECIFICATIONS, ids=lambda cls: cls.__name__)
def test_parameters_are_input_specifications(cls):
    assert issubclass(cls, InputSpecification)
    assert issubclass(cls, Context)


@pytest.mark.parametrize(
    "child, parent",
    [
        (AtomisticSimulation, Simulation),
        (SinglePointCalculation, AtomisticSimulation),
        (GeometryOptimization, AtomisticSimulation),
        (MolecularDynamics, AtomisticSimulation),
        (SimulationAnalysis, Analysis),
        (OrbitalProjection, SimulationAnalysis),
        (ProjectionQualityAssessment, SimulationAnalysis),
        (ChemicalBondingAnalysis, SimulationAnalysis),
        (BondingEnvironmentAnalysis, SimulationAnalysis),
        (EquationOfStateFit, SimulationAnalysis),
    ],
)
def test_activity_hierarchy(child, parent):
    assert issubclass(child, parent)


@pytest.mark.parametrize("cls", SIMULATION_ANALYSES, ids=lambda cls: cls.__name__)
def test_simulation_analyses_reference_one_analysed_system(cls):
    # Single-valued on purpose: every result of the analysis describes one system.
    prop = cls()._property_metadata["analysed_system"]
    assert prop.code == "ANALYSED_SYSTEM"
    assert prop.data_type == "OBJECT"
    assert prop.object_code == "SIMULATED_SYSTEM"
    assert not prop.multivalued


def test_analysed_system_is_not_on_every_analysis():
    # Non-simulation analyses (creep data processing) have no simulated system.
    assert issubclass(CreepTestDataProcessing, Analysis)
    assert not issubclass(CreepTestDataProcessing, SimulationAnalysis)
    assert "analysed_system" not in CreepTestDataProcessing()._property_metadata
    assert "analysed_system" not in Analysis()._property_metadata


def test_analysed_system_is_distinct_from_simulated_system():
    # SIMULATED_SYSTEM of simulations is multivalued and has no roles; the analysis subject is a separate property.
    props = SimulationAnalysis()._property_metadata
    assert "simulated_system" not in props
    assert Simulation()._property_metadata["simulated_system"].multivalued


def test_simulation_itself_is_not_extended():
    added = {
        "electronic_structure_parameters",
        "geometry_optimization_parameters",
        "molecular_dynamics_parameters",
        "pressure",
        "total_free_energy",
        "average_temperature",
    }
    assert not added & set(Simulation()._property_metadata)


@pytest.mark.parametrize(
    "activity, property_name, specification",
    [
        (
            AtomisticSimulation,
            "electronic_structure_parameters",
            ElectronicStructureParameters,
        ),
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
        (
            OrbitalProjection,
            "orbital_projection_parameters",
            OrbitalProjectionParameters,
        ),
        (
            ProjectionQualityAssessment,
            "projection_quality_parameters",
            ProjectionQualityParameters,
        ),
        (
            ChemicalBondingAnalysis,
            "bonding_analysis_parameters",
            BondingAnalysisParameters,
        ),
        (
            BondingEnvironmentAnalysis,
            "bonding_environment_parameters",
            BondingEnvironmentParameters,
        ),
    ],
)
def test_activities_reference_their_specification(
    activity, property_name, specification
):
    prop = activity()._property_metadata[property_name]
    assert prop.data_type == "OBJECT"
    assert prop.object_code == specification.defs.code


def test_ab_initio_md_is_md_with_electronic_structure_parameters():
    props = set(MolecularDynamics()._property_metadata)
    assert {
        "molecular_dynamics_parameters",
        "electronic_structure_parameters",
        "computational_method",
    } <= props


@pytest.mark.parametrize(
    "cls",
    [SinglePointCalculation, GeometryOptimization, MolecularDynamics],
    ids=lambda cls: cls.__name__,
)
def test_static_and_md_runs_have_potential_energy(cls):
    # Force-field single points and optimizations need a potential-energy result, not only the DFT energies.
    prop = cls()._property_metadata["final_potential_energy"]
    assert prop.code == "FINAL_POTENTIAL_ENERGY"
    assert prop.units == "eV"


def test_force_convergence_has_norm_selector():
    props = GeometryOptimizationParameters()._property_metadata
    assert props["force_convergence_norm"].vocabulary_code == "FORCE_CONVERGENCE_NORM"
    codes = {t.code for t in vocabularies.ForceConvergenceNorm().terms}
    assert codes == {"MAX_ATOM_NORM", "MAX_COMPONENT", "GLOBAL_VECTOR_NORM"}


def test_ionic_energy_convergence_absolute_and_relative():
    props = GeometryOptimizationParameters()._property_metadata
    assert props["ionic_energy_convergence"].units == "eV"
    assert props["ionic_relative_energy_convergence"].units is None


def test_md_velocity_temperature_is_separate_from_thermostat_targets():
    props = MolecularDynamicsParameters()._property_metadata
    assert props["velocity_initialization_temperature"].prev_versions == [
        "ATOM_MD_INIT_TEMP_IN_K:v0"
    ]
    for name in (
        "target_temperature_start",
        "target_temperature_end",
        "target_pressure_start",
        "target_pressure_end",
    ):
        assert name in props
    assert props["target_temperature_start"].prev_versions is None


def test_md_time_step_in_ps_like_v0():
    assert MolecularDynamicsParameters()._property_metadata["time_step"].units == "ps"


def test_geometry_optimization_records_stop_reason():
    prop = GeometryOptimization()._property_metadata["optimization_stop_reason"]
    assert prop.vocabulary_code == "OPTIMIZATION_STOP_REASON"
    assert prop.section == "Results"


def test_specifications_hold_no_results():
    # Structural check only: it looks at section labels, so it cannot tell whether a value in an input section is
    # really an input (e.g. requested vs. achieved duration). It does not prove that a value is an input.
    result_sections = {"Results", "Electronic Structure Results"}
    for cls in SPECIFICATIONS:
        assert not {p.section for p in cls().properties} & result_sections, cls.__name__


def _vocabulary_codes():
    return {
        c.defs.code
        for _, c in inspect.getmembers(vocabularies, inspect.isclass)
        if issubclass(c, VocabularyType) and c.__module__ == vocabularies.__name__
    }


@pytest.mark.parametrize(
    "cls", NEW_ACTIVITIES + SPECIFICATIONS, ids=lambda cls: cls.__name__
)
def test_vocabulary_and_object_references_resolve(cls):
    # PERSON is not defined in v1: it is an inherited dependency of the base objects (base_objects.py) and is
    # whitelisted here, so passing does not prove that v1 resolves on its own.
    vocab_codes = _vocabulary_codes()
    object_codes = {
        c.defs.code
        for module in (activities, entities)
        for _, c in inspect.getmembers(module, inspect.isclass)
        if hasattr(c, "defs") and c.__module__ == module.__name__
    } | {"PERSON", "ENTITY"}
    for prop in cls().properties:
        if prop.data_type == "CONTROLLEDVOCABULARY":
            assert prop.vocabulary_code in vocab_codes, prop.code
        if prop.data_type == "OBJECT":
            assert prop.object_code in object_codes, prop.code


@pytest.mark.parametrize(
    "cls",
    [
        c
        for _, c in inspect.getmembers(vocabularies, inspect.isclass)
        if issubclass(c, VocabularyType) and c.__module__ == vocabularies.__name__
    ],
    ids=lambda cls: cls.__name__,
)
def test_vocabulary_term_codes_are_unique(cls):
    codes = [term.code for term in cls().terms]
    assert codes
    assert len(codes) == len(set(codes))
