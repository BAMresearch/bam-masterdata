# Computation schema (datamodel v1)

This page describes how computations are modelled in `datamodel/v1`, how the model relates to [nomad-simulations](https://github.com/nomad-coe/nomad-simulations) and to [PMDco](https://github.com/materialdigital/core-ontology), and how v0 records are migrated. The schema itself is code-agnostic. Everything that depends on a specific code (VASP, LAMMPS, pyiron) is collected on this page.

## Crosswalk

| Concept | nomad-simulations | v1 | PMDco and related ontologies |
|-|-|-|-|
| The run | `Simulation` | `SIMULATION` and one subtype per task | simulation process (PMD_0000933), a computing process (PMD_0000583) |
| Kind of task | workflow classes `SinglePoint`, `GeometryOptimization`, `MolecularDynamics`, `EquationOfState` | `SINGLE_POINT_CALCULATION`, `GEOMETRY_OPTIMIZATION`, `MOLECULAR_DYNAMICS`, `MONTE_CARLO_SIMULATION`, `NUDGED_ELASTIC_BAND`, `EQUATION_OF_STATE_FIT` | Monte Carlo simulation (PMD_0000862); the other subtypes have no IRI |
| Physics | `ModelMethod` (`DFT`, force fields, `contributions`) | `COMPUTATIONAL_METHOD` | simulation method specification (PMD_0000931) |
| Numerics | `numerical_settings` (`KMesh`, `Smearing`, `SelfConsistency`, `Pseudopotential`) and the workflow `method` | `ParameterSet` subtypes | part of the plan specification |
| Structure | `ModelSystem` | `SIMULATED_SYSTEM` | information content entity (IAO_0000030); CMSO computational sample |
| Material it models | (not modelled) | `REPRESENTED_MATERIAL` on `SIMULATED_SYSTEM` | is about (IAO_0000136); CMSO `hasMaterial` |
| Results | workflow `results`, `Outputs` | `*_RESULTS` types under `CALCULATION_DATUM` | calculation datum (PMD_0025035) |
| System the results describe | `Outputs.model_system_ref` | `DESCRIBED_SYSTEM` | is about (IAO_0000136) |
| Program | `Program` | `SOFTWARE` | software (IAO_0000010) |
| Where it ran | (not modelled) | `HPC`, linked by `EXECUTED_ON` | computing device (PMD_0000582), has participant (RO_0000057) |
| Chaining runs | workflow tasks | openBIS parent-child | process chain pattern (precedes, preceded by) |

`COMPUTATIONAL_METHOD` is one flat type with a `METHOD_TYPE` vocabulary instead of subtypes such as `DFT` and force fields. In openBIS an OBJECT property accepts only the exact type it names, so subtypes would break the `COMPUTATIONAL_METHOD` link on `Computation`.

### ModelSystem and SimulatedSystem

| nomad-simulations `ModelSystem` | v1 `SIMULATED_SYSTEM` |
|-|-|
| `type` | `SYSTEM_TYPE` |
| `dimensionality` | `DIMENSIONALITY` |
| `n_particles` | `N_PARTICLES` |
| `total_charge`, `total_spin_multiplicity` | `TOTAL_CHARGE`, `TOTAL_SPIN_MULTIPLICITY` |
| `chemical_formula` (descriptive, reduced, iupac, hill, anonymous) | `CHEMICAL_FORMULA_*` |
| `lattice_vectors`, `periodic_boundary_conditions`, `volume` | `LATTICE_VECTORS`, `PERIODIC_A/B/C`, `CELL_VOLUME` |
| `symmetry` (`GlobalCrystalSymmetry`) | the properties in the section "Symmetry Details" |
| `lattice_type` `r - trigonal` | `LATTICE_TYPE` = `HEXAGONAL` with `LATTICE_CENTERING` = `RHOMBOHEDRAL` |
| `positions`, `velocities`, `particle_states`, `sub_systems`, `representations` | not properties: the structure is attached as a file to the object |
| `is_representative`, `time_step`, `branch_label`, `branch_depth` | not needed: each SimulatedSystem object is one system, and its role in a run is given by the link that points to it |

## How objects are linked

| Link | From | To | Meaning | PMDco relation |
|-|-|-|-|-|
| openBIS parents | a computation | earlier computations | the computations whose outputs this computation used | process chain |
| `INITIAL_SYSTEM` | simulation | `SIMULATED_SYSTEM` | system at the start | has specified input (OBI_0000293) |
| `FINAL_SYSTEM` | simulation | `SIMULATED_SYSTEM` | system at the end | has specified output (OBI_0000299) |
| `SIMULATED_SYSTEM` | simulation | `SIMULATED_SYSTEM` | all systems involved | (none) |
| `*_RESULTS` | computation | its results type | the results of this computation | has specified output (OBI_0000299) |
| `DESCRIBED_SYSTEM` | results | `SIMULATED_SYSTEM` | the system the results are about | is about (IAO_0000136) |
| `REPRESENTED_MATERIAL` | `SIMULATED_SYSTEM` | `MATERIAL` or `SAMPLE` (unrestricted) | the material the system is a model of | is about (IAO_0000136) |
| `EXECUTED_ON` | computation | `HPC` | the cluster the computation ran on | has participant (RO_0000057) |
| `COMPUTATIONAL_METHOD`, `*_PARAMETERS` | computation | method or parameter set | the plan the computation followed | (no single relation: the process realizes a plan that the specification describes; left to an exporter) |

Rules:

- When a simulation continues from another, its `INITIAL_SYSTEM` is the same SimulatedSystem object as the previous run's `FINAL_SYSTEM`, not a copy, and the previous run is its openBIS parent.
- Parents are used for data dependency instead of a typed property because the upstream computations are of several types, and a typed OBJECT property accepts only one exact type.
- The physical model of an upstream calculation is not copied to an analysis. It is reached through the parents.
- `REPRESENTED_MATERIAL` is unrestricted (`object_code=None`) because `MATERIAL` and `SAMPLE` have subtypes, which a typed reference would not accept.

### Notes on specific types

- **SinglePointCalculation** has no `FINAL_SYSTEM`, because it has one configuration. Its results refer to that configuration.
- **NudgedElasticBand** lists the two end configurations and the intermediate configurations in `SIMULATED_SYSTEM`. It does not use `INITIAL_SYSTEM` or `FINAL_SYSTEM`, because both end configurations are inputs.
- **MolecularDynamicsResults**: averages are over the time steps of the run. Whether an equilibration period was excluded is not recorded, so the time series should be attached as a file.
- **EquationOfStateFit**: its parents are the simulations at the individual volumes, one per energy-volume point. The energy-volume data are attached as a file. `DESCRIBED_SYSTEM` of the results is the reference structure whose volume was scaled. For energies from static calculations, the results are static-lattice values at zero temperature, without zero-point or thermal vibrations.
- **Bulk modulus**: isotropic straining is not sufficient in general. For an anisotropic crystal, equal strains give unequal normal stresses, and the curvature of an isotropically scaled cell can exceed the hydrostatic bulk modulus. For cubic symmetry, isotropic scaling keeps the correct cell shape, but internal coordinates must still be relaxed. Otherwise the value is the curvature along the constrained deformation path (see `EOS_STRAIN_AXES` and the relaxation degrees of freedom of the parent simulations).
- **Total magnetic moment** is defined only for collinear spin-polarized calculations. For noncollinear calculations the total moment is a vector, and its magnitude must not be stored in `TOTAL_MAGNETIC_MOMENT`.
- **Electronic energies**: the three total energies coincide when no smearing is used. In VASP all energies are relative to the isolated atoms in the reference configuration of the PAW datasets, so only differences between calculations with the same datasets are meaningful.
- **Final pressure**: with a tensile-positive stress tensor sigma, it is P = -tr(sigma)/3. Codes differ in the sign of the stress they print, so check the convention of the source.

## Code reference

| v1 code | VASP | LAMMPS |
|-|-|-|
| `PSEUDOPOTENTIALS` | POTCAR | |
| `PLANE_WAVE_CUTOFF` | ENCUT | |
| `KPOINT_MESH_TYPE` | KPOINTS mode, KGAMMA | |
| `KPOINT_SPACING` | KSPACING; N_i = max(1, ceil(2 pi \|b_i\| / KSPACING)), with b_i the reciprocal lattice vectors without the factor 2 pi | |
| `SYMMETRY_USAGE` | ISYM: `CRYSTAL_SYMMETRY` = 1, 2, or 3; `TIME_REVERSAL_ONLY` = 0; `NONE` = -1 | |
| `OCCUPATION_SCHEME` | ISMEAR: `GAUSSIAN` = 0; `FERMI_DIRAC` = -1; `METHFESSEL_PAXTON` > 0 (the value is the order); `TETRAHEDRON` = -4; `TETRAHEDRON_BLOECHL` = -5; `FIXED` = -2 | |
| `SMEARING_WIDTH` | SIGMA | |
| `METHFESSEL_PAXTON_ORDER` | positive value of ISMEAR | |
| `N_BANDS` | NBANDS | |
| `ELECTRONIC_ALGORITHM` | ALGO: `BLOCKED_DAVIDSON` = Normal; `RMM_DIIS` = VeryFast; `BLOCKED_DAVIDSON_THEN_RMM_DIIS` = Fast; `ALL_BAND_CONJUGATE_GRADIENT` = All; `EXACT_DIAGONALIZATION` = Exact | |
| `SCF_ENERGY_CONVERGENCE` | EDIFF (VASP also requires the change of the band-structure energy to be below it) | |
| `MAX_SCF_ITERATIONS` | NELM | |
| `GEOMETRY_OPTIMIZATION_ALGORITHM` | IBRION: `QUASI_NEWTON_RMM_DIIS` = 1; `CONJUGATE_GRADIENT` = 2; `DAMPED_MOLECULAR_DYNAMICS` = 3 | |
| `FORCE_CONVERGENCE` | absolute value of a negative EDIFFG | minimize ftol |
| `FORCE_CONVERGENCE_NORM` | `MAX_ATOM_NORM` (negative EDIFFG) | min_modify norm: `MAX_ATOM_NORM` = max; `MAX_COMPONENT` = inf; `GLOBAL_VECTOR_NORM` = two (default) |
| `IONIC_ENERGY_CONVERGENCE` | positive EDIFFG | |
| `IONIC_RELATIVE_ENERGY_CONVERGENCE` | | minimize etol |
| `MAX_IONIC_STEPS` | NSW | minimize maxiter |
| `OPTIMIZATION_STOP_REASON` | `ENERGY_CRITERION_MET` = positive EDIFFG reached; `FORCE_CRITERION_MET` = negative EDIFFG reached; `MAX_STEPS_REACHED` = NSW reached | stopping criterion: `ENERGY_CRITERION_MET` = energy tolerance; `FORCE_CRITERION_MET` = force tolerance; `MAX_STEPS_REACHED` = max iterations; `MAX_FORCE_EVALUATIONS_REACHED` = max force evaluations; `LINE_SEARCH_FAILED` = linesearch alpha is zero, trust region too small |
| `VELOCITY_INITIALIZATION_TEMPERATURE` | | velocity create |
| `TARGET_TEMPERATURE_START`, `TARGET_TEMPERATURE_END` | | fix nvt/npt Tstart, Tstop |
| `TARGET_PRESSURE_START`, `TARGET_PRESSURE_END` | | fix npt Pstart, Pstop |
| `TIME_STEP` | POTIM (in fs, divide by 1000) | timestep (ps in metal units) |
| `N_TIME_STEPS` | NSW | |
| `THERMOSTAT_TIME_CONSTANT` | | fix langevin damp |
| `THERMODYNAMIC_ENSEMBLE` = `SEMI_GRAND_CANONICAL` | | for example fix atom/swap with NVT or NPT |
| `MAX_FORCE_COMPONENT` | | thermo fmax |
| `FORCE_VECTOR_NORM`, `AVERAGE_FORCE_VECTOR_NORM` | | thermo fnorm |
| `FINAL_POTENTIAL_ENERGY` | | thermo pe |
| `FINAL_PRESSURE` | OUTCAR line "external pressure", in kbar (1 GPa = 10 kbar) | |
| `TOTAL_FREE_ENERGY` | free energy TOTEN | |
| `TOTAL_ENERGY_WITHOUT_ENTROPY` | energy without entropy | |
| `TOTAL_ENERGY_ZERO_SMEARING` | energy(sigma->0) | |
| `FERMI_ENERGY` | E-fermi | |

## v0 to v1 migration rules

Each rule gives the v0 source, the v1 target, the condition, and what to do when the condition cannot be checked. Code comments in `datamodel/v1` refer to these rule numbers.

**R1. Job type.** `PYIRON_JOB.VASP:v0` and `PYIRON_JOB.LAMMPS:v0` become the v1 type given by `ATOMISTIC_CALC_TYPE:v0`:

| `ATOMISTIC_CALC_TYPE` | v1 type |
|-|-|
| `ATOM_CALC_SC` | `SINGLE_POINT_CALCULATION` |
| `ATOM_CALC_STRUC_OPT` | `GEOMETRY_OPTIMIZATION` |
| `ATOM_CALC_MD` | `MOLECULAR_DYNAMICS` |
| `ATOM_CALC_MC` | `MONTE_CARLO_SIMULATION` |
| `ATOM_CALC_NEB` | `NUDGED_ELASTIC_BAND` |
| not set | `SIMULATION` |

`PYIRON_JOB.MURNAGHAN:v0` becomes `EQUATION_OF_STATE_FIT`. Its result values go to an `EQUATION_OF_STATE_FIT_RESULTS` object.

**R2. K-point mesh type.** `ATOM_KPOINT_TYPE:v0` mixes how the mesh was generated (`KPOINTS_KSPACING`) with how it is placed. A mesh generated from KSPACING can be Gamma-centered or Monkhorst-Pack (VASP: KGAMMA). Derive `KPOINT_MESH_TYPE` from the v0 type together with `ATOM_KPT_GAMMA_CENT:v0` or the raw KPOINTS and INCAR files. Leave it unset if the centering cannot be determined.

**R3. K-point subdivisions.** `ATOMISTIC_N_KPT_X/Y/Z:v0` map to `KPOINT_MESH_B1/B2/B3`. v0 used x/y/z wording, so first check that these were the mesh subdivisions along the reciprocal lattice vectors.

**R4. Force threshold.** `ATOM_F_TOL_IN_EV_A:v0` was shared by VASP and LAMMPS jobs without stating the norm. Migrate the value to `FORCE_CONVERGENCE` together with `FORCE_CONVERGENCE_NORM`: `MAX_ATOM_NORM` for VASP; for LAMMPS, take the norm from the job's min_modify settings (default `GLOBAL_VECTOR_NORM`). Leave the norm unset if the settings are not known.

**R5. Ionic energy threshold.** `ATOM_E_TOL_ION_IN_EV:v0` is labelled eV but was also used for LAMMPS, whose etol is relative. Values from VASP jobs go to `IONIC_ENERGY_CONVERGENCE`. Values from LAMMPS jobs go to `IONIC_RELATIVE_ENERGY_CONVERGENCE`, after checking what the exporter stored. Never convert between the two.

**R6. MD targets.**

- `ATOM_MD_INIT_TEMP_IN_K:v0`: pyiron's `LammpsControl.calc_md` uses `initial_temperature` to initialize velocities. When it is None and a target temperature is given, it defaults to twice the first target temperature. Migrate to `VELOCITY_INITIALIZATION_TEMPERATURE` after checking the exporter of each record.
- `ATOM_MD_TARG_TEMP_IN_K:v0` is a generic target, not a ramp end point. For a constant target, set both `TARGET_TEMPERATURE_START` and `TARGET_TEMPERATURE_END`. If the job used a ramp, take both values from the job input.
- `ATOM_MD_INIT_PRESS_IN_GPA:v0` may be a barostat start target or a measured initial pressure. Migrate it to `TARGET_PRESSURE_START` only if the exporter shows it was Pstart. Keep a measured value separately.
- `ATOM_TARG_PRESS_IN_GPA:v0`: as for the target temperature, a constant target sets both `TARGET_PRESSURE_START` and `TARGET_PRESSURE_END`.
- `ATOM_MD_LANGEVIN:v0`: true means `THERMOSTAT` = `LANGEVIN`. False says nothing about the thermostat and must not be migrated as "no thermostat".

**R7. Minimization algorithms.** Both `GEOMETRY_OPTIMIZATION_ALGORITHM` and `ELECTRONIC_ALGORITHM` come from `MINIMIZATION_ALGO:v0`, so the target depends on the v0 property, not on the term alone. Values of `ATOM_IONIC_MIN_ALGO:v0` go to `GEOMETRY_OPTIMIZATION_ALGORITHM`. Values of `ATOM_ELEC_MIN_ALGO:v0` go to `ELECTRONIC_ALGORITHM`. `MIN_ALGO_RMM_DIIS` in `ATOM_IONIC_MIN_ALGO` maps to `QUASI_NEWTON_RMM_DIIS`. Report any value that has no target in its vocabulary; do not guess one.

**R8. Maximum force.** `ATOM_FORCE_MAX_IN_EV_A:v0` is labelled "maximum force component". It maps to `MAX_FORCE_COMPONENT` only if the exporter stored the largest Cartesian component. pyiron's `force_max` is the largest per-atom force norm (`np.linalg.norm(forces, axis=-1).max(axis=-1)`), which belongs to `MAX_FORCE_NORM`. Check the exporter per record.

**R9. Bravais lattice.** `BRAVAIS_LATTICE:v0` maps to a pair of `LATTICE_TYPE` and `LATTICE_CENTERING`:

| v0 term | `LATTICE_TYPE` | `LATTICE_CENTERING` |
|-|-|-|
| `TRICLINIC` | `TRICLINIC` | `PRIMITIVE` |
| `SIMPLE_MONOCLINIC` | `MONOCLINIC` | `PRIMITIVE` |
| `BASE_MONOCLINIC` | `MONOCLINIC` | `SIDE_CENTERED` |
| `SIMPLE_ORTHORMB` | `ORTHORHOMBIC` | `PRIMITIVE` |
| `BASE_ORTHORMB` | `ORTHORHOMBIC` | `SIDE_CENTERED` |
| `BODY_ORTHORMB` | `ORTHORHOMBIC` | `BODY_CENTERED` |
| `FACE_ORTHORMB` | `ORTHORHOMBIC` | `FACE_CENTERED` |
| `SIMPLE_TETRA` | `TETRAGONAL` | `PRIMITIVE` |
| `BODY_CENTER_TETRA` | `TETRAGONAL` | `BODY_CENTERED` |
| `HEXAGONAL` | `HEXAGONAL` | `PRIMITIVE` |
| `RHOMBOHEDRAL` | `HEXAGONAL` | `RHOMBOHEDRAL` |
| `SIMPLE_CUBIC` | `CUBIC` | `PRIMITIVE` |
| `BODY_CENTER_CUBIC` | `CUBIC` | `BODY_CENTERED` |
| `FACE_CENTER_CUBIC` | `CUBIC` | `FACE_CENTERED` |
| `HEX_CLOSE_PACK` | `HEXAGONAL` | `PRIMITIVE` |

`HEX_CLOSE_PACK` is a structure, not a Bravais lattice. For an elemental hcp structure, also set `STRUKTURBERICHT_DESIGNATION` to A3.

**R10. Total magnetic moment.** `ATOM_FIN_TOTMGMO_IN_MUB:v0` stored VARCHAR and also covered noncollinear jobs (`ATOM_NON_COLL_MAG`). Migrate to `TOTAL_MAGNETIC_MOMENT` only the values from collinear jobs that parse as a single number. Keep vector or other text values separately.

**R11. Final energies.** `ATOM_FIN_TOT_ENG_IN_EV:v0` and `ATOM_FIN_POT_ENG_IN_EV:v0` were shared by the VASP and LAMMPS job types. For LAMMPS, the potential energy is `FINAL_POTENTIAL_ENERGY` for every calculation type, and the total energy is `FINAL_TOTAL_ENERGY` of `MOLECULAR_DYNAMICS_RESULTS`. For VASP, pyiron (`vasp/base.py`, `_vasp_generic_energy_free_affected`) checks HDF version 0.1.0 (also assumed when the version is absent) for a mismatch between `output/generic/energy_pot` and the final SCF free energies. Check the HDF version, the stored energy fields, and the raw OUTCAR per job before choosing the v1 energy property.

**R12. Final volume and periodicity.** `ATOM_FIN_VOL_IN_A3:v0` becomes `CELL_VOLUME` of the SimulatedSystem referenced by `FINAL_SYSTEM`. `PERIODIC_BOUNDARY_X/Y/Z:v0` become `PERIODIC_A/B/C` of the SimulatedSystem. x/y/z and a/b/c only coincide for orthogonal cells aligned with the axes, so check the cell first.

**R13. Cell vectors.** `SIM_CELL_VECTORS:v0` stores text. Parse a numeric 3x3 matrix and check the row ordering and units before writing `LATTICE_VECTORS`.

**R14. Space group.** `SPACE_GROUP:v0` stores vocabulary terms. Extract the Hermann-Mauguin symbol from the term label for `SPACE_GROUP_SYMBOL`.

**R15. EOS fit order.** pyiron's Murnaghan uses `fit_order` as the polynomial degree for polynomial fits. The analytic fits (birch, birchmurnaghan, murnaghan, pouriertarantola, vinet) ignore the input order and reset `fit_order` to zero. Migrate `MURN_FIT_EQN_ORDER:v0` to `EQUATION_OF_STATE_ORDER` only for `EOS_POLYNOMIAL` fits.

**R16. Relaxation degrees of freedom.** v0 had three booleans: `ATOM_POS_RELAX`, `ATOM_CELL_SHP_RELAX`, `ATOM_CELL_VOL_RELAX`. They become one multivalued `RELAXATION_DEGREES_OF_FREEDOM`, following ASMO RelaxationDOF. A v0 value of true maps to `ATOMIC_POSITIONS`, `CELL_SHAPE`, or `CELL_VOLUME`.

**R17. Pseudopotential functional compatibility.** `PSEUDOPOT_FUNC:v0` (vocabulary `PSEUDOPOT_FUNCTIONAL`) maps to `FUNCTIONAL_COMPATIBILITY`: `PSEUDOPOT_LDA` to `LDA`, `PSEUDOPOT_GGA` to `GGA`, `PSEUDOPOT_HYBRID` to `HYBRID_GGA`. It says which functionals the pseudopotential is meant to be used with, not which functional generated it.

**R18. Not migrated.**

| v0 field | Reason |
|-|-|
| `LATTICE_C_OVER_A` | can be computed from `CELL_LENGTH_C` and `CELL_LENGTH_A` |
| `SIM_CELL_LENGTHS_IN_A`, `SIM_CELL_ANGLES_IN_DEG` | text duplicates of `CELL_LENGTH_*` and `CELL_ANGLE_*`; parse into those if the numeric fields are empty |
| `CRYSTAL_ORIENTATION` | not part of the v1 system model yet |
| `ATOM_SHORT_RNG_ORD` | not part of the v1 system model yet |
| `ATOM_SAMPLE_TEMP_IN_K` | not part of the v1 system model yet |
| `ATOMISTIC_KPT_FULL` | the explicit k-point list is attached as a file |
| `CO_RESPONSIBLE_PERSON` | `RESPONSIBLE_PERSON` is multivalued in v1 |
| `PSEUDOPOT_AE` (term of `PSEUDOPOT_TYPE`) | an all-electron calculation uses no pseudopotential |
| `WORKFLOW_REFERENCE` | no v1 workflow definition type yet |
