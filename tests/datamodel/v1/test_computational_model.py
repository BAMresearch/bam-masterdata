import pytest

from bam_masterdata.datamodel.v1.activities import (
    Analysis,
    CreepTestDataProcessing,
    EquationOfStateFit,
    GeometryOptimization,
    MolecularDynamics,
    Simulation,
    SimulationAnalysis,
    SinglePointCalculation,
)
from bam_masterdata.datamodel.v1.entities import (
    ElectronicStructureParameters,
    EquationOfStateFitParameters,
    GeometryOptimizationParameters,
    MolecularDynamicsParameters,
)

SIMULATION_ANALYSES = [
    EquationOfStateFit,
]

SPECIFICATIONS = [
    ElectronicStructureParameters,
    GeometryOptimizationParameters,
    MolecularDynamicsParameters,
    EquationOfStateFitParameters,
]


@pytest.mark.parametrize("cls", SIMULATION_ANALYSES, ids=lambda cls: cls.__name__)
def test_simulation_analyses_reference_one_analysed_system(cls):
    # Single-valued on purpose: every result of the analysis describes one system.
    prop = cls()._property_metadata["analysed_system"]
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
        "final_pressure",
        "total_free_energy",
        "average_temperature",
    }
    assert not added & set(Simulation()._property_metadata)


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
def test_simulation_tasks_preserve_shared_configuration_properties(cls):
    assert cls.get_hierarchy() == [
        "ROOT",
        "ACTIVITY",
        "COMPUTATION",
        "SIMULATION",
        cls.defs.code,
    ]
    obj = cls()
    props = obj._property_metadata
    expected = {
        "initial_system",
        "final_system",
        "electronic_structure_parameters",
        "max_force_norm",
        "max_force_component",
        "force_vector_norm",
        "final_pressure",
        "final_potential_energy",
        "scf_converged",
        "n_irreducible_kpoints",
        "total_free_energy",
        "total_energy_without_entropy",
        "total_energy_zero_smearing",
        "fermi_energy",
        "total_magnetic_moment",
    }
    assert expected <= props.keys()
    exported_codes = [prop["code"] for prop in obj.model_to_dict()["properties"]]
    for name in expected:
        assert exported_codes.count(props[name].code) == 1


def test_md_velocity_temperature_is_separate_from_thermostat_targets():
    props = MolecularDynamicsParameters()._property_metadata
    assert "velocity_initialization_temperature" in props
    for name in (
        "target_temperature_start",
        "target_temperature_end",
        "target_pressure_start",
        "target_pressure_end",
    ):
        assert name in props
    assert props["target_temperature_start"].prev_versions is None


def test_specifications_hold_no_results():
    # Structural check only: it looks at section labels, so it cannot tell whether a value in an input section is
    # really an input (e.g. requested vs. achieved duration). It does not prove that a value is an input.
    result_sections = {"Results", "Electronic Structure Results"}
    for cls in SPECIFICATIONS:
        assert not {p.section for p in cls().properties} & result_sections, cls.__name__
