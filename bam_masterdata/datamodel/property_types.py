from bam_masterdata.metadata.definitions import PropertyTypeDef

AnnotationsState = PropertyTypeDef(
    code="$ANNOTATIONS_STATE",
    description="""Annotations State""",
    data_type="XML",
    property_label="Annotations State",
)


Barcode = PropertyTypeDef(
    code="$BARCODE",
    description="""Custom Barcode""",
    data_type="VARCHAR",
    property_label="Custom Barcode",
)


DefaultCollectionView = PropertyTypeDef(
    code="$DEFAULT_COLLECTION_VIEW",
    description="""Default view for experiments of the type collection""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="$DEFAULT_COLLECTION_VIEWS",
    property_label="Default collection view",
)


DefaultObjectType = PropertyTypeDef(
    code="$DEFAULT_OBJECT_TYPE",
    description="""Enter the code of the object type for which the collection is used""",
    data_type="VARCHAR",
    property_label="Default object type",
)


Document = PropertyTypeDef(
    code="$DOCUMENT",
    description="""Document""",
    data_type="MULTILINE_VARCHAR",
    property_label="Document",
)


ElnSettings = PropertyTypeDef(
    code="$ELN_SETTINGS",
    description="""ELN Settings""",
    data_type="VARCHAR",
    property_label="ELN Settings",
)


HistoryId = PropertyTypeDef(
    code="$HISTORY_ID",
    description="""History ID""",
    data_type="VARCHAR",
    property_label="History ID",
)


Name = PropertyTypeDef(
    code="$NAME",
    description="""Name""",
    data_type="VARCHAR",
    property_label="Name",
)


ShowInProjectOverview = PropertyTypeDef(
    code="$SHOW_IN_PROJECT_OVERVIEW",
    description="""Show in project overview page""",
    data_type="BOOLEAN",
    property_label="Show in project overview",
)


Xmlcomments = PropertyTypeDef(
    code="$XMLCOMMENTS",
    description="""Comments log""",
    data_type="XML",
    property_label="Comments",
)


Abstract = PropertyTypeDef(
    code="ABSTRACT",
    description="""Abstract//Kurzzusammenfassung""",
    data_type="MULTILINE_VARCHAR",
    property_label="Abstract",
)


AccreditatedCalibrationLab = PropertyTypeDef(
    code="ACCREDITATED_CALIBRATION_LAB",
    description="""Accredited Calibration Laboratory//Akkreditiertes Kalibrierlabor""",
    data_type="BOOLEAN",
    property_label="Accredited Calibration Laboratory",
)


AccuracyClassVde0410 = PropertyTypeDef(
    code="ACCURACY_CLASS_VDE0410",
    description="""Accuracy Class according to VDE 0410//Genauigkeitsklasse anch VDE 0410""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="ACCURACY_CLASS_VDE0410",
    property_label="Accuracy Class according to VDE 0410",
)


Acronym = PropertyTypeDef(
    code="ACRONYM",
    description="""Acronym//Akronym""",
    data_type="VARCHAR",
    property_label="Acronym",
)


ActingPerson = PropertyTypeDef(
    code="ACTING_PERSON",
    description="""Acting Person//Handelnde Person""",
    data_type="OBJECT",
    object_code="PERSON.BAM",
    property_label="Acting Person",
)


ActionDate = PropertyTypeDef(
    code="ACTION_DATE",
    description="""Action Date//Datum der Handlung""",
    data_type="DATE",
    property_label="Monitoring Date",
)


ActionEnd = PropertyTypeDef(
    code="ACTION_END",
    description="""End time//Ende""",
    data_type="TIMESTAMP",
    property_label="End time",
)


ActionStart = PropertyTypeDef(
    code="ACTION_START",
    description="""Start time//Beginn""",
    data_type="TIMESTAMP",
    property_label="Start time",
)


Address = PropertyTypeDef(
    code="ADDRESS",
    description="""Postal address//Anschrift""",
    data_type="MULTILINE_VARCHAR",
    property_label="Postal address",
)


AdChannelDescription = PropertyTypeDef(
    code="AD_CHANNEL_DESCRIPTION",
    description="""Description of AD-channel data//Beschreibung der AD-Kanal Signale""",
    data_type="MULTILINE_VARCHAR",
    property_label="Description of AD-channel data",
)


Affiliation = PropertyTypeDef(
    code="AFFILIATION",
    description="""Institute or company//Institut oder Unternehmen""",
    data_type="VARCHAR",
    property_label="Institute or company",
)


AirRelHumidityInPercent = PropertyTypeDef(
    code="AIR_REL_HUMIDITY_IN_PERCENT",
    description="""Relative Air Humidity in %//Relative Luftfeuchte in %""",
    data_type="REAL",
    property_label="Relative Air Humidity [%]",
)


AirTemperatureInCelsius = PropertyTypeDef(
    code="AIR_TEMPERATURE_IN_CELSIUS",
    description="""Air Temperature in °C//Lufttemperatur in °C""",
    data_type="REAL",
    property_label="Air Temperature [°C]",
)


Alias = PropertyTypeDef(
    code="ALIAS",
    description="""e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname""",
    data_type="VARCHAR",
    property_label="Alternative Name",
)


AluTreatmentFirst = PropertyTypeDef(
    code="ALU_TREATMENT_FIRST",
    description="""First Treatment//Erste Behandlung""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="RAW_MAT_TREATMENT_ALU",
    property_label="First Treatment",
)


AluTreatmentFourth = PropertyTypeDef(
    code="ALU_TREATMENT_FOURTH",
    description="""Fourth Treatment//Vierte Behandlung""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="RAW_MAT_TREATMENT_ALU",
    property_label="Fourth Treatment",
)


AluTreatmentSecond = PropertyTypeDef(
    code="ALU_TREATMENT_SECOND",
    description="""Second Treatment//Zweite Behandlung""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="RAW_MAT_TREATMENT_ALU",
    property_label="Second Treatment",
)


AluTreatmentThird = PropertyTypeDef(
    code="ALU_TREATMENT_THIRD",
    description="""Third Treatment//Dritte Behandlung""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="RAW_MAT_TREATMENT_ALU",
    property_label="Third Treatment",
)


AnalogOutputVoltageMax = PropertyTypeDef(
    code="ANALOG_OUTPUT_VOLTAGE_MAX",
    description="""Analog Output Maximum Voltage [V]//Maximale Spannung am Analogen Ausgang [V]""",
    data_type="REAL",
    property_label="Analog Output Maximum Voltage [V]",
)


AnalogOutputVoltageMin = PropertyTypeDef(
    code="ANALOG_OUTPUT_VOLTAGE_MIN",
    description="""Analog Output Minimum Voltage [V]//Minimale Spannung am Analogen Ausgang [V]""",
    data_type="REAL",
    property_label="Analog Output Minimum Voltage [V]",
)


ArbitrarySubframeHeightInPixel = PropertyTypeDef(
    code="ARBITRARY_SUBFRAME_HEIGHT_IN_PIXEL",
    description="""Height of arbitrary subframe in pixel//Höhe des arbiträren Subframes in Pixel""",
    data_type="INTEGER",
    property_label="Height of arbitrary subframe [pix]",
)


ArbitrarySubframeStartHeightInPixel = PropertyTypeDef(
    code="ARBITRARY_SUBFRAME_START_HEIGHT_IN_PIXEL",
    description="""Start height of arbitrary subframe in pixel//Starthöhe des arbiträren Subframes in Pixel""",
    data_type="INTEGER",
    property_label="Start height of arbitrary subframe [pix]",
)


ArbitrarySubframeStartWidthInPixel = PropertyTypeDef(
    code="ARBITRARY_SUBFRAME_START_WIDTH_IN_PIXEL",
    description="""Start Width of arbitrary subframe in pixel//Startbreite des arbiträren Subframes in Pixel""",
    data_type="INTEGER",
    property_label="Start Width of arbitrary subframe [pix]",
)


ArbitrarySubframeWidthInPixel = PropertyTypeDef(
    code="ARBITRARY_SUBFRAME_WIDTH_IN_PIXEL",
    description="""Width of arbitrary subframe in pixel//Breite des arbiträren Subframes in Pixel""",
    data_type="INTEGER",
    property_label="Width of arbitrary subframe [pix]",
)


Arrest = PropertyTypeDef(
    code="ARREST",
    description="""Crack Arrest during Step//Rissarrest während des Versuchschrittes""",
    data_type="BOOLEAN",
    property_label="Crack Arrest during Step",
)


AssociatedProject = PropertyTypeDef(
    code="ASSOCIATED_PROJECT",
    description="""Associated project//Assoziiertes Projekt""",
    data_type="OBJECT",
    object_code="PROJECT",
    property_label="Associated project",
)


AtomisticCalcType = PropertyTypeDef(
    code="ATOMISTIC_CALC_TYPE",
    description="""Type of atomistic calculation//Art der atomistischen Berechnung""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="ATOMISTIC_CALC_TYPE",
    property_label="Atomistic Calculation Type",
)


AtomisticIonicSteps = PropertyTypeDef(
    code="ATOMISTIC_IONIC_STEPS",
    description="""Number of ionic steps//Anzahl der Ionischen Schritten""",
    data_type="INTEGER",
    property_label="N Ionic Steps",
)


AtomisticKptFull = PropertyTypeDef(
    code="ATOMISTIC_KPT_FULL",
    description="""Full list of K-points//Vollständige Liste der K-Punkte""",
    data_type="MULTILINE_VARCHAR",
    property_label="Full list of K-points",
)


AtomisticKptSpacinIn1A = PropertyTypeDef(
    code="ATOMISTIC_KPT_SPACIN_IN_1_A",
    description="""K-spacing value [1/Å]//K-Abstandswert""",
    data_type="REAL",
    property_label="K-spacing [1/Å]",
)


AtomisticNKptX = PropertyTypeDef(
    code="ATOMISTIC_N_KPT_X",
    description="""Number of K-points in x-direction//Anzahl der K-Punkte in x-Richtung""",
    data_type="INTEGER",
    property_label="Number of K-points in x-direction",
)


AtomisticNKptY = PropertyTypeDef(
    code="ATOMISTIC_N_KPT_Y",
    description="""Number of K-points in y-direction//Anzahl der K-Punkte in y-Richtung""",
    data_type="INTEGER",
    property_label="Number of K-points in y-direction",
)


AtomisticNKptZ = PropertyTypeDef(
    code="ATOMISTIC_N_KPT_Z",
    description="""Number of K-points in z-direction//Anzahl der K-Punkte in z-Richtung""",
    data_type="INTEGER",
    property_label="Number of K-points in z-direction",
)


AtomAvgFnormInEvA = PropertyTypeDef(
    code="ATOM_AVG_FNORM_IN_EV_A",
    description="""Average Force norm over time steps [eV/Å]//Durchschnittskraftnorm [eV/Å]""",
    data_type="REAL",
    property_label="Average Force Norm [eV/Å]",
)


AtomAvgPotEngInEv = PropertyTypeDef(
    code="ATOM_AVG_POT_ENG_IN_EV",
    description="""Average Potential Energy over time steps (eV)//Durchschnittliche potenzielle Energie [eV]""",
    data_type="REAL",
    property_label="Average Potential Energy [eV]",
)


AtomAvgPressInGpa = PropertyTypeDef(
    code="ATOM_AVG_PRESS_IN_GPA",
    description="""Average pressure over time steps [GPa]//Durchschnittsdruck [GPa]""",
    data_type="REAL",
    property_label="Average Pressure [GPa]",
)


AtomAvgTotEngInEv = PropertyTypeDef(
    code="ATOM_AVG_TOT_ENG_IN_EV",
    description="""Average Total Energy over time steps [eV]//Durchschnittsgesamtenergie [eV]""",
    data_type="REAL",
    property_label="Average Total Energy [eV]",
)


AtomAvgVolInA3 = PropertyTypeDef(
    code="ATOM_AVG_VOL_IN_A3",
    description="""Average Volume over time steps [Å^3]//Durchschnittliches Volumen [Å^3]""",
    data_type="REAL",
    property_label="Average Volume [Å^3]",
)


AtomCellShpRelax = PropertyTypeDef(
    code="ATOM_CELL_SHP_RELAX",
    description="""Degrees of freedom - Cell shape relaxation//Freiheitsgrade - Zellformrelaxation""",
    data_type="BOOLEAN",
    property_label="Cell Shape Relaxation",
)


AtomCellVolRelax = PropertyTypeDef(
    code="ATOM_CELL_VOL_RELAX",
    description="""Degrees of freedom - Cell volume relaxation//Freiheitsgrade - Zellvolumenrelaxation""",
    data_type="BOOLEAN",
    property_label="Cell Volume Relaxation",
)


AtomChgdensReuse = PropertyTypeDef(
    code="ATOM_CHGDENS_REUSE",
    description="""Are the initial charge densities from a previous calculation?//Stammen die Anfangsladungsdichten aus einer früheren Berechnung?""",
    data_type="BOOLEAN",
    property_label="Charge density from a previous run?",
)


AtomElecMinAlgo = PropertyTypeDef(
    code="ATOM_ELEC_MIN_ALGO",
    description="""Minimization algorithm for electronic steps//Minimalisierungsalgorithmus zur elektronischen Schritten""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="MINIMIZATION_ALGO",
    property_label="Minimization Algorithm for Electronic Steps",
)


AtomElETolInEv = PropertyTypeDef(
    code="ATOM_EL_E_TOL_IN_EV",
    description="""Energy tolerance for electronic minimization [eV]//Energietoleranz zur elektronische Minimierung [eV]""",
    data_type="REAL",
    property_label="Electronic Energy Tolerance [eV]",
)


AtomEquilKModInGpa = PropertyTypeDef(
    code="ATOM_EQUIL_K_MOD_IN_GPA",
    description="""Equilibrium bulk modulus [GPa]//Kompressionsmodul im  Gleichgewicht [GPa]""",
    data_type="REAL",
    property_label="Equilibrium Bulk Modulus [GPa]",
)


AtomEquilTotengInEv = PropertyTypeDef(
    code="ATOM_EQUIL_TOTENG_IN_EV",
    description="""Equilibrium total energy [eV]//Gesamtenergie im Gleichgewicht [eV]""",
    data_type="REAL",
    property_label="Equilibrium Total Energy [eV]",
)


AtomEquilVolInA3 = PropertyTypeDef(
    code="ATOM_EQUIL_VOL_IN_A3",
    description="""Equilibrium volume [Å^3]//Volumen im Gleichgewicht [Å^3]""",
    data_type="REAL",
    property_label="Equilibrium Volume [Å^3]",
)


AtomECutoffInEv = PropertyTypeDef(
    code="ATOM_E_CUTOFF_IN_EV",
    description="""Energy cutoff for wavefunctions [eV]//Energiegrenzwert für Wellenfunktionen [eV]""",
    data_type="REAL",
    property_label="Energy Cutoff [eV]",
)


AtomETolIonInEv = PropertyTypeDef(
    code="ATOM_E_TOL_ION_IN_EV",
    description="""Energy tolerance for ionic minimization [eV]//Energietoleranz zur ionische Minimierung [eV]""",
    data_type="REAL",
    property_label="Ionic Energy Tolerance [eV]",
)


AtomFinFnormInEvA = PropertyTypeDef(
    code="ATOM_FIN_FNORM_IN_EV_A",
    description="""Final Force norm [eV/Å]//Letztes Kraftnorm [eV/Å]""",
    data_type="REAL",
    property_label="Final Force Norm [eV/Å]",
)


AtomFinPotEngInEv = PropertyTypeDef(
    code="ATOM_FIN_POT_ENG_IN_EV",
    description="""Final Potential Energy [eV]//Letzte potenzielle Energie [eV]""",
    data_type="REAL",
    property_label="Final Potential Energy [eV]",
)


AtomFinPressInGpa = PropertyTypeDef(
    code="ATOM_FIN_PRESS_IN_GPA",
    description="""Final pressure [GPa]//Letzter Druck [GPa]""",
    data_type="REAL",
    property_label="Final Pressure [GPa]",
)


AtomFinTotmgmoInMub = PropertyTypeDef(
    code="ATOM_FIN_TOTMGMO_IN_MUB",
    description="""Final total magnetic moment [μ_B]//Leztztes magnetisches Gesamtmoment [μ_B]""",
    data_type="VARCHAR",
    property_label="Final Total Magnetic Moment [μ_B]",
)


AtomFinTotEngInEv = PropertyTypeDef(
    code="ATOM_FIN_TOT_ENG_IN_EV",
    description="""Final Total Energy [eV]//Letzte Gesamtenergie [eV]""",
    data_type="REAL",
    property_label="Final Total Energy [eV]",
)


AtomFinVolInA3 = PropertyTypeDef(
    code="ATOM_FIN_VOL_IN_A3",
    description="""Final Volume [Å^3]//Letztes Volumen [Å^3]""",
    data_type="REAL",
    property_label="Final Volume [Å^3]",
)


AtomForceMaxInEvA = PropertyTypeDef(
    code="ATOM_FORCE_MAX_IN_EV_A",
    description="""Final maximum force component [eV/Å]//Letzte maximale Kraftkomponente [eV/Å]""",
    data_type="REAL",
    property_label="Final Maximum Force Component [eV/Å]",
)


AtomFTolInEvA = PropertyTypeDef(
    code="ATOM_F_TOL_IN_EV_A",
    description="""Force tolerance for minimization [eV/Å]//Krafttoleranz für Minimierung [eV/Å]""",
    data_type="REAL",
    property_label="Ionic Force Tolerance [eV/Å]",
)


AtomIonicMinAlgo = PropertyTypeDef(
    code="ATOM_IONIC_MIN_ALGO",
    description="""Minimization algorithm for ionic steps//Minimalisierungsalgorithmus zur ionischen Schritten""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="MINIMIZATION_ALGO",
    property_label="Minimization Algorithm for Ionic Steps",
)


AtomIonicSteps = PropertyTypeDef(
    code="ATOM_IONIC_STEPS",
    description="""Number of ionic steps//Anzahl der Ionischen Schritten""",
    data_type="INTEGER",
    property_label="N Ionic Steps",
)


AtomKpointType = PropertyTypeDef(
    code="ATOM_KPOINT_TYPE",
    description="""K-points specification type//K-Punkte-Spezifikation Typ""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="ATOM_KPOINT_TYPE",
    property_label="K-points Specification Type",
)


AtomKptGammaCent = PropertyTypeDef(
    code="ATOM_KPT_GAMMA_CENT",
    description="""Are the K-points centered around the gamma point?//Sind die k-Punkte um den Gamma-Punkt zentriert?""",
    data_type="BOOLEAN",
    property_label="Gamma-centered?",
)


AtomMdAvgTempInK = PropertyTypeDef(
    code="ATOM_MD_AVG_TEMP_IN_K",
    description="""Average temperature over time steps [K]//Durchschnittstemperatur [K]""",
    data_type="REAL",
    property_label="Average Temperature [K]",
)


AtomMdEnsemble = PropertyTypeDef(
    code="ATOM_MD_ENSEMBLE",
    description="""Statistical ensemble set in the simulation//Statistisches Ensemble in der Simulation""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="THERMODYN_ENSEMBLE",
    property_label="Statistical Ensemble",
)


AtomMdInitPressInGpa = PropertyTypeDef(
    code="ATOM_MD_INIT_PRESS_IN_GPA",
    description="""Initial pressure [GPa]//Anfangsdruck [GPa]""",
    data_type="REAL",
    property_label="Initial Pressure [GPa]",
)


AtomMdInitTempInK = PropertyTypeDef(
    code="ATOM_MD_INIT_TEMP_IN_K",
    description="""Initial temperature [K]//Anfangstemperatur [K]""",
    data_type="REAL",
    property_label="Initial Temperature [K]",
)


AtomMdLangevin = PropertyTypeDef(
    code="ATOM_MD_LANGEVIN",
    description="""Use of Langevin dynamics//Verwendung der Langevin-Dynamik""",
    data_type="BOOLEAN",
    property_label="Langevin Dynamics",
)


AtomMdTargTempInK = PropertyTypeDef(
    code="ATOM_MD_TARG_TEMP_IN_K",
    description="""Target temperature [K]//Zieltemperatur [K]""",
    data_type="REAL",
    property_label="Target Temperature [K]",
)


AtomMdTimeStpInPs = PropertyTypeDef(
    code="ATOM_MD_TIME_STP_IN_PS",
    description="""Time step size [ps]//Zeitschrittweite [ps]""",
    data_type="REAL",
    property_label="Time Step Size [ps]",
)


AtomNonCollMag = PropertyTypeDef(
    code="ATOM_NON_COLL_MAG",
    description="""Are the magnetic moments non-collinear?//Sind die magnetischen Momente nicht kollinear?""",
    data_type="BOOLEAN",
    property_label="Non-collinear Magnetism?",
)


AtomPosRelax = PropertyTypeDef(
    code="ATOM_POS_RELAX",
    description="""Degrees of freedom - Atomic position relaxation//Freiheitsgrade - Atomare Positionsrelaxation""",
    data_type="BOOLEAN",
    property_label="Atomic Position Relaxation",
)


AtomPotentialStyle = PropertyTypeDef(
    code="ATOM_POTENTIAL_STYLE",
    description="""Interatomic Potential Style//Interatomarer Potential Stil""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="ATOM_POTENTIAL_STYLE",
    property_label="Interatomic Potential Style",
)


AtomSampleTempInK = PropertyTypeDef(
    code="ATOM_SAMPLE_TEMP_IN_K",
    description="""Current temperature of sample [K]//Aktuelle Temperatur der Probe [K]""",
    data_type="REAL",
    property_label="Sample Temperature [K]",
)


AtomShortRngOrd = PropertyTypeDef(
    code="ATOM_SHORT_RNG_ORD",
    description="""Chains, rings, tetrahedra etc.//Ketten, Ringe, Tetraeder usw.""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="SHORT_RNG_ORD",
    property_label="Short-range Ordering",
)


AtomSigmaInEv = PropertyTypeDef(
    code="ATOM_SIGMA_IN_EV",
    description="""Sigma value [eV]//Sigma-Wert [eV]""",
    data_type="REAL",
    property_label="Sigma Value [eV]",
)


AtomSimTimePsInPs = PropertyTypeDef(
    code="ATOM_SIM_TIME_PS_IN_PS",
    description="""Simulated timespan [ps]// Simulierte Zeitspanne [ps]""",
    data_type="REAL",
    property_label="Simulation Time [ps]",
)


AtomSpinPolarized = PropertyTypeDef(
    code="ATOM_SPIN_POLARIZED",
    description="""Is the calculation spin-polarized?//Ist die Berechnung spinpolarisiert?""",
    data_type="BOOLEAN",
    property_label="Calculation Spin-polarized?",
)


AtomTargPressInGpa = PropertyTypeDef(
    code="ATOM_TARG_PRESS_IN_GPA",
    description="""Target pressure [GPa]//Ziel-Druck [GPa]""",
    data_type="REAL",
    property_label="Target Pressure [GPa]",
)


AtomWavefuncReuse = PropertyTypeDef(
    code="ATOM_WAVEFUNC_REUSE",
    description="""Are the initial wavefunctions from a previous calculation?//Stammen die Anfangswellenfunktionen aus einer früheren Berechnung?""",
    data_type="BOOLEAN",
    property_label="Wavefunctions from a previous run?",
)


AtomXcFunctional = PropertyTypeDef(
    code="ATOM_XC_FUNCTIONAL",
    description="""Exchange-correlation functional//Austausch-Korrelations-Funktional""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="ATOM_XC_FUNCTIONAL",
    property_label="XC functional",
)


AtomXcUCorrection = PropertyTypeDef(
    code="ATOM_XC_U_CORRECTION",
    description="""Are U corrections included?//Sind U-Korrekturen enthalten?""",
    data_type="BOOLEAN",
    property_label="U Correction?",
)


Author = PropertyTypeDef(
    code="AUTHOR",
    description="""Author(s)//Autor(en)""",
    data_type="VARCHAR",
    property_label="Author(s)",
)


AuxiliaryMaterialType = PropertyTypeDef(
    code="AUXILIARY_MATERIAL_TYPE",
    description="""Auxiliary Material Type//Hilfsstofftyp""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="AUXILIARY_MATERIAL_TYPE",
    property_label="Auxiliary Material Type",
)


BamDataStoreUserStatus = PropertyTypeDef(
    code="BAM_DATA_STORE_USER_STATUS",
    description="""BAM Data Store user//BAM Data Store-Nutzer*in""",
    data_type="BOOLEAN",
    property_label="BAM Data Store user",
)


BamFieldOfActivity = PropertyTypeDef(
    code="BAM_FIELD_OF_ACTIVITY",
    description="""BAM Field of Activity//BAM Aktivitätsfeld""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="BAM_FIELD_OF_ACTIVITY",
    property_label="BAM Field of Activity",
)


BamFloor = PropertyTypeDef(
    code="BAM_FLOOR",
    description="""BAM Floor//BAM Etage""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="BAM_FLOOR",
    property_label="BAM Floor",
)


BamFocusArea = PropertyTypeDef(
    code="BAM_FOCUS_AREA",
    description="""BAM Focus Area//BAM Themenfeld""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="BAM_FOCUS_AREA",
    property_label="BAM Focus Area",
)


BamHouse = PropertyTypeDef(
    code="BAM_HOUSE",
    description="""BAM House//BAM Haus""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="BAM_HOUSE",
    property_label="BAM House",
)


BamLocation = PropertyTypeDef(
    code="BAM_LOCATION",
    description="""BAM Location//BAM Liegenschaft""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="BAM_LOCATION",
    property_label="BAM Location",
)


BamLocationComplete = PropertyTypeDef(
    code="BAM_LOCATION_COMPLETE",
    description="""Complete BAM location (up to room level)//Komplette BAM-Ortsangabe (bis Raumlevel)""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="BAM_LOCATION_COMPLETE",
    property_label="Complete BAM Location",
)


BamOe = PropertyTypeDef(
    code="BAM_OE",
    description="""BAM Organizational Entity//BAM Organisationseinheit (OE)""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="BAM_OE",
    property_label="BAM Organizational Entity",
)


BamPartner = PropertyTypeDef(
    code="BAM_PARTNER",
    description="""BAM Partner(s)//BAM Partner""",
    data_type="VARCHAR",
    property_label="BAM Partner",
)


BamRoom = PropertyTypeDef(
    code="BAM_ROOM",
    description="""BAM Room//BAM Raum""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="BAM_ROOM",
    property_label="BAM Room",
)


BamUsername = PropertyTypeDef(
    code="BAM_USERNAME",
    description="""BAM username//BAM Benutzername""",
    data_type="VARCHAR",
    property_label="BAM username",
)


BamUserprofile = PropertyTypeDef(
    code="BAM_USERPROFILE",
    description="""BAM user profile link//BAM Link zum Benutzerprofil""",
    data_type="HYPERLINK",
    property_label="BAM user profile link",
)


Bandwidth = PropertyTypeDef(
    code="BANDWIDTH",
    description="""Bandwidth [Hz]//Bandbreite [Hz]""",
    data_type="REAL",
    property_label="Bandwidth [Hz]",
)


BarcodeExternal = PropertyTypeDef(
    code="BARCODE_EXTERNAL",
    description="""External barcode (if availabe)//Externer Barcode (falls vorhanden)""",
    data_type="VARCHAR",
    property_label="External Barcode",
)


BatchNumber = PropertyTypeDef(
    code="BATCH_NUMBER",
    description="""Batch number//Chargennummer""",
    data_type="VARCHAR",
    property_label="Batch number",
)


BravaisLattice = PropertyTypeDef(
    code="BRAVAIS_LATTICE",
    description="""Bravais lattice//Bravais-Gitter""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="BRAVAIS_LATTICE",
    property_label="Bravais Lattice",
)


CalibrationCertificateNumber = PropertyTypeDef(
    code="CALIBRATION_CERTIFICATE_NUMBER",
    description="""Calibration Certificate Number//Kalibrierschein-Nummer""",
    data_type="VARCHAR",
    property_label="Calibration Certificate Number",
)


CalibrationDate = PropertyTypeDef(
    code="CALIBRATION_DATE",
    description="""Date of calibration//Datum der Kalibrierung""",
    data_type="DATE",
    property_label="Calibration date",
)


CalibrationInterval = PropertyTypeDef(
    code="CALIBRATION_INTERVAL",
    description="""Calibration Interval [Months]//Kalibrierintervall [Monate]""",
    data_type="INTEGER",
    property_label="Calibration Interval [Months]",
)


CalibrationLabAccreditationNumber = PropertyTypeDef(
    code="CALIBRATION_LAB_ACCREDITATION_NUMBER",
    description="""Calibration Laboratory Accreditation Number//Akkreditierungszeichen des Kalibrierlabors""",
    data_type="VARCHAR",
    property_label="Calibration Laboratory Accreditation Number",
)


CalibrationProvider = PropertyTypeDef(
    code="CALIBRATION_PROVIDER",
    description="""Calibration provider//Kalibrierdienstleister""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="CALIBRATION_PROVIDER",
    property_label="Calibration provider",
)


CameraDistanceInMillimeter = PropertyTypeDef(
    code="CAMERA_DISTANCE_IN_MILLIMETER",
    description="""Distance camera -> sample in mm//Abstand Kamera zu Sample in mm""",
    data_type="REAL",
    property_label="Distance camera -> sample [mm]",
)


CameraShutterMode = PropertyTypeDef(
    code="CAMERA_SHUTTER_MODE",
    description="""The shutter mode used for video recording//Belichtungsprinzip des Bildsensors""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="CAMERA_SHUTTER_MODE",
    property_label="Shutter mode",
)


CasNumber = PropertyTypeDef(
    code="CAS_NUMBER",
    description="""CAS Registry Number (corresponds to field `CAS-No.` in the Hazardous Materials Inventory (GSM) of BAM)//CAS-Nummer (entspricht Feld `CAS-Nr.` aus dem Gefahrstoffmanagement (GSM) der BAM)""",
    data_type="VARCHAR",
    property_label="CAS Registry Number",
)


CellTemperatureInCelsius = PropertyTypeDef(
    code="CELL_TEMPERATURE_IN_CELSIUS",
    description="""Measurement cell temperature in °C // Temperatur der Messzelle in °C""",
    data_type="REAL",
    property_label="Cell Temperature [°C]",
)


Characteristics = PropertyTypeDef(
    code="CHARACTERISTICS",
    description="""Characteristics//Merkmale""",
    data_type="VARCHAR",
    property_label="Characteristics",
)


CheckInterval = PropertyTypeDef(
    code="CHECK_INTERVAL",
    description="""Time interval for checks in days//Überprüfungsintervall in Tagen""",
    data_type="INTEGER",
    property_label="Check interval [days]",
)


ChemSpeciesAddressed = PropertyTypeDef(
    code="CHEM_SPECIES_ADDRESSED",
    description="""Chemical species addressed//Angesprochene chemische Arten""",
    data_type="VARCHAR",
    property_label="Chemical Species Addressed",
)


ChemSpeciesByCompInPct = PropertyTypeDef(
    code="CHEM_SPECIES_BY_COMP_IN_PCT",
    description="""Chemical species involved by composition [%]//Inbegriffene chemische Spezies nach Zusammensetzung [%]""",
    data_type="VARCHAR",
    property_label="Chemical species involved by composition [%]",
)


ChemSpeciesByNAtoms = PropertyTypeDef(
    code="CHEM_SPECIES_BY_N_ATOMS",
    description="""Chemical species involved by number of atoms//Chemische Spezies nach Anzahl der Atome""",
    data_type="VARCHAR",
    property_label="Chemical Species (number of atoms)",
)


ChemSpeciesByWtInPct = PropertyTypeDef(
    code="CHEM_SPECIES_BY_WT_IN_PCT",
    description="""Chemical species involved by weight [%]//Inbegriffene chemische Spezies nach Gewicht [%]""",
    data_type="VARCHAR",
    property_label="Chemical Species by weight [%]",
)


ColBlindAccess = PropertyTypeDef(
    code="COL_BLIND_ACCESS",
    description="""Colour-blind Accessibilty//Farbenblindheit Barrierefreiheit""",
    data_type="BOOLEAN",
    property_label="Colour-blind Accessibilty",
)


CompilationReq = PropertyTypeDef(
    code="COMPILATION_REQ",
    description="""Is compilation required?//Ist eine Kompilierung erforderlich?""",
    data_type="BOOLEAN",
    property_label="Compilation Required?",
)


Compiler = PropertyTypeDef(
    code="COMPILER",
    description="""Compiler info//Compiler-Informationen""",
    data_type="MULTILINE_VARCHAR",
    property_label="Compiler",
)


Concentration = PropertyTypeDef(
    code="CONCENTRATION",
    description="""Concentration [%] (corresponds to field `Concentration %` in the Hazardous Materials Inventory (GSM) of BAM)//Konzentration [%] (entspricht Feld `Konzentration %` aus dem Gefahrstoffmanagement (GSM) der BAM)""",
    data_type="REAL",
    property_label="Concentration",
)


ConceptualDictionary = PropertyTypeDef(
    code="CONCEPTUAL_DICTIONARY",
    description="""Conceptual dictionary associated with pyiron job//Begriffswörterbuch zu pyiron job""",
    data_type="MULTILINE_VARCHAR",
    property_label="Conceptual Dictionary",
)


CondaChannels = PropertyTypeDef(
    code="CONDA_CHANNELS",
    description="""Conda channels used//Verwendete Conda-Kanäle""",
    data_type="MULTILINE_VARCHAR",
    property_label="Conda Channels",
)


CondaPip = PropertyTypeDef(
    code="CONDA_PIP",
    description="""Is pip used to install packages?//Wird pip zur Installation von Packages verwendet?""",
    data_type="BOOLEAN",
    property_label="Pip Usage?",
)


ConductivityInMs = PropertyTypeDef(
    code="CONDUCTIVITY_IN_MS",
    description="""Conductivity in mili Siemens (mS)//Leitfähigkeit in Millisiemens (mS)""",
    data_type="REAL",
    property_label="Conductivity",
)


CoResponsiblePerson = PropertyTypeDef(
    code="CO_RESPONSIBLE_PERSON",
    description="""Co-responsible person//Weitere verantwortliche Person""",
    data_type="OBJECT",
    object_code="PERSON.BAM",
    property_label="Co-responsible person",
)


CpuNodesConfig = PropertyTypeDef(
    code="CPU_NODES_CONFIG",
    description="""CPU node configuration//Konfiguration der CPU-Knoten""",
    data_type="MULTILINE_VARCHAR",
    property_label="CPU Node Configuration",
)


CrystalOrientation = PropertyTypeDef(
    code="CRYSTAL_ORIENTATION",
    description="""Miller indices//Millersche Indizes""",
    data_type="VARCHAR",
    property_label="Crystallographic Orientation",
)


CylinderType = PropertyTypeDef(
    code="CYLINDER_TYPE",
    description="""Hydraulic Cylinder Type Code as specified by Manufacturer//Typenbezeichnung des Herstellers für den Hydraulikzylinder""",
    data_type="VARCHAR",
    property_label="Hydraulic Cylinder Type",
)


DateBottling = PropertyTypeDef(
    code="DATE_BOTTLING",
    description="""Date of Bottling//Abfülldatum""",
    data_type="DATE",
    property_label="Bottling Date",
)


DateExpiration = PropertyTypeDef(
    code="DATE_EXPIRATION",
    description="""Expiration Date//Verfallsdatum""",
    data_type="DATE",
    property_label="Expiration Date",
)


DateOpening = PropertyTypeDef(
    code="DATE_OPENING",
    description="""Opening Data//Öffnungsdatum""",
    data_type="DATE",
    property_label="Opening Date",
)


DatePublication = PropertyTypeDef(
    code="DATE_PUBLICATION",
    description="""Date of publication//Publikationsdatum""",
    data_type="DATE",
    property_label="Date of publication",
)


DcpdAmplificationFactor = PropertyTypeDef(
    code="DCPD_AMPLIFICATION_FACTOR",
    description="""Amplification Factor//Verstärkungsfaktor""",
    data_type="REAL",
    property_label="Amplification Factor",
)


DcpdCurrent = PropertyTypeDef(
    code="DCPD_CURRENT",
    description="""DCPD Current [A]//DCPD Stromstärke [A]""",
    data_type="REAL",
    property_label="Current [A]",
)


DcpdInitialCracklength = PropertyTypeDef(
    code="DCPD_INITIAL_CRACKLENGTH",
    description="""Initial Cracklength (measured optically) [mm]// Initiale Risslänge (optisch vermessen) [mm]""",
    data_type="REAL",
    property_label="Initial Cracklength (measured optically) [mm]",
)


DcpdInitialPotentialDrop = PropertyTypeDef(
    code="DCPD_INITIAL_POTENTIAL_DROP",
    description="""Initial Potential Drop (amplified) [V]//Initiale Potentialabfall (verstärkt) [V]""",
    data_type="REAL",
    property_label="Initial Potential Drop (amplified) [V]",
)


DcpdInitialTemp = PropertyTypeDef(
    code="DCPD_INITIAL_TEMP",
    description="""Initial Temperature [°C]//Anfangstemperatur [°C]""",
    data_type="REAL",
    property_label="Initial Temperature [°C]",
)


DcpdLinearisedPotential = PropertyTypeDef(
    code="DCPD_LINEARISED_POTENTIAL",
    description="""Output Signal Proportional to Cracklength//Ausgangssignal proportional zur Risslänge""",
    data_type="BOOLEAN",
    property_label="Output Signal Proportional to Cracklength",
)


DcpdPotDropCal = PropertyTypeDef(
    code="DCPD_POT_DROP_CAL",
    description="""Potential Drop Calibration//Kalibrierung des Potentialabfalls""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="DCPD_POT_CAL",
    property_label="Potential Drop Calibration",
)


DcpdProportionalPotential = PropertyTypeDef(
    code="DCPD_PROPORTIONAL_POTENTIAL",
    description="""Output Signal proportional to Potential Drop//Ausgangssignal proportional zum Potentialabfall""",
    data_type="BOOLEAN",
    property_label="Output Signal proportional to Potential Drop",
)


DcpdTempCoeff = PropertyTypeDef(
    code="DCPD_TEMP_COEFF",
    description="""Temperature Coefficient of Resistivity [°C^-1]//Temperaturkoeffizient der Resistivität [°C^-1]""",
    data_type="REAL",
    property_label="Temperature Coefficient of Resistivity [°C^-1]",
)


DcpdTempComp = PropertyTypeDef(
    code="DCPD_TEMP_COMP",
    description="""Temperature Compensation//Temperaturkompensation""",
    data_type="BOOLEAN",
    property_label="Temperature Compensation",
)


DcpdYzeroFitted = PropertyTypeDef(
    code="DCPD_YZERO_FITTED",
    description="""Y0 in Johnson Formula fitted for Notch Geometry [mm]//Y0 in Johnson Formel angepasst an die Kerbgeometrie [mm]""",
    data_type="REAL",
    property_label="Y0 in Johnson Formula fitted for Notch Geometry [mm]",
)


DefectDescription = PropertyTypeDef(
    code="DEFECT_DESCRIPTION",
    description="""Defect Description//Beschreibung der Defekte""",
    data_type="MULTILINE_VARCHAR",
    property_label="Defect description",
)


DeltakExponent = PropertyTypeDef(
    code="DELTAK_EXPONENT",
    description="""Exponent for Delta K increase or decrease [mm^-1]//Exponent für Lastabsenkung oder -erhöhung [mm^-1]""",
    data_type="REAL",
    property_label="Exponent for Delta K increase or decrease [mm^-1]",
)


DeltaA = PropertyTypeDef(
    code="DELTA_A",
    description="""Crack Extension [mm]//Risserweiterung [mm]""",
    data_type="REAL",
    property_label="Crack Extension [mm]",
)


DeltaN = PropertyTypeDef(
    code="DELTA_N",
    description="""Elapsed Cycles in Step//Im Versuchsschritt gefahrene Zyklen""",
    data_type="INTEGER",
    property_label="Elapsed Cycles in Step",
)


DensityGramPerCubicCm = PropertyTypeDef(
    code="DENSITY_GRAM_PER_CUBIC_CM",
    description="""Density [g/cm³]//Dichte [g/cm³]""",
    data_type="REAL",
    property_label="Density",
)


Description = PropertyTypeDef(
    code="DESCRIPTION",
    description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
    data_type="MULTILINE_VARCHAR",
    property_label="Description",
)


DetectionRangeMaxInNm = PropertyTypeDef(
    code="DETECTION_RANGE_MAX_IN_NM",
    description="""Maximal detectable wavelength [nm]//Maximale detektierbare Wellenlänge [nm]""",
    data_type="REAL",
    property_label="Detection Range Max [nm]",
)


DetectionRangeMinInNm = PropertyTypeDef(
    code="DETECTION_RANGE_MIN_IN_NM",
    description="""Minimal detectable wavelength [nm]//Minimale detektierbare Wellenlänge [nm]""",
    data_type="REAL",
    property_label="Detection Range Min [nm]",
)


DeviceModelName = PropertyTypeDef(
    code="DEVICE_MODEL_NAME",
    description="""Manufacturer model name//Modellname bzw. Gerätebezeichnung seitens des Herstellers""",
    data_type="VARCHAR",
    property_label="Model Name",
)


DfgDeviceCode = PropertyTypeDef(
    code="DFG_DEVICE_CODE",
    description="""DFG Device Code//DFG Gerätegruppenschlüssel (GGS)""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="DFG_DEVICE_CODE",
    property_label="DFG Device Code",
)


DocumentType = PropertyTypeDef(
    code="DOCUMENT_TYPE",
    description="""Document Type//Dokumenten Typ""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="DOCUMENT_TYPE",
    property_label="Document type",
)


Donor = PropertyTypeDef(
    code="DONOR",
    description="""Name of the donor organism of which the genetic information is used for generating a GMO//Name des Spenderorganismus, dessen genetische Information für die Erzeugung eines GVO verwendet wird""",
    data_type="OBJECT",
    object_code="ORGANISM",
    property_label="Donor Organism",
)


DonorRiskGroup = PropertyTypeDef(
    code="DONOR_RISK_GROUP",
    description="""Organism Risk Group Assignment//Risikogruppenzuordnung des Organismus""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="ORGANISM_RISK_GROUP",
    property_label="Donor Organism Risk Group",
)


DurationInSeconds = PropertyTypeDef(
    code="DURATION_IN_SECONDS",
    description="""The duration of the sample treatment in seconds//Die Dauer der Probenbehandlung in Sekunden""",
    data_type="REAL",
    property_label="Duration [s]",
)


ElectronicSmearing = PropertyTypeDef(
    code="ELECTRONIC_SMEARING",
    description="""Partial occupancies//Teilbesetzungen""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="ELECTRONIC_SMEARING",
    property_label="Partial Occupancies",
)


Email = PropertyTypeDef(
    code="EMAIL",
    description="""Email address//E-Mail-Adresse""",
    data_type="VARCHAR",
    property_label="Email address",
)


EndDate = PropertyTypeDef(
    code="END_DATE",
    description="""End date//Enddatum""",
    data_type="TIMESTAMP",
    property_label="End date",
)


EnvTool = PropertyTypeDef(
    code="ENV_TOOL",
    description="""E.g., conda//Z.B., conda""",
    data_type="VARCHAR",
    property_label="Environment Tool Used",
)


Ethernet = PropertyTypeDef(
    code="ETHERNET",
    description="""Ethernet Interface//Ethernet Schnittstelle""",
    data_type="BOOLEAN",
    property_label="Ethernet Interface",
)


ExposureTimeInSeconds = PropertyTypeDef(
    code="EXPOSURE_TIME_IN_SECONDS",
    description="""Exposure time in seconds//Belichtungszeit in Sekunden""",
    data_type="REAL",
    property_label="Exposure time [s]",
)


FamilyName = PropertyTypeDef(
    code="FAMILY_NAME",
    description="""Family name//Nachname""",
    data_type="VARCHAR",
    property_label="Family name",
)


FcgCyclicR = PropertyTypeDef(
    code="FCG_CYCLIC_R",
    description="""Cyclic R-Curve Determination//Ermittlung der zyklischen R-Kurve""",
    data_type="BOOLEAN",
    property_label="Cyclic R-Curve",
)


FcgNominalR = PropertyTypeDef(
    code="FCG_NOMINAL_R",
    description="""Test Nominal R-Ratio//Nominelles R-Verhältnis des Tests""",
    data_type="REAL",
    property_label="Test Nominal R-Ratio",
)


FcgParis = PropertyTypeDef(
    code="FCG_PARIS",
    description="""PARIS Regime Parameters Determination//Ermittlung der PARIS-Parameter""",
    data_type="BOOLEAN",
    property_label="PARIS Parameters Determination",
)


FcgResultCyclicrA = PropertyTypeDef(
    code="FCG_RESULT_CYCLICR_A",
    description="""Cyclic R-Curve Parameter A//Zyklische R-Kurve Parameter A""",
    data_type="REAL",
    property_label="Cyclic R-Curve Parameter A",
)


FcgResultCyclicrB = PropertyTypeDef(
    code="FCG_RESULT_CYCLICR_B",
    description="""Cyclic R-Curve Parameter b//Zyklische R-Kurve Parameter b""",
    data_type="REAL",
    property_label="Cyclic R-Curve Parameter b",
)


FcgResultParisC = PropertyTypeDef(
    code="FCG_RESULT_PARIS_C",
    description="""PARIS Parameter C//PARIS Parameter C""",
    data_type="REAL",
    property_label="PARIS Parameter C",
)


FcgResultParisM = PropertyTypeDef(
    code="FCG_RESULT_PARIS_M",
    description="""PARIS Parameter m//PARIS Parameter m""",
    data_type="REAL",
    property_label="PARIS Parameter m",
)


FcgResultThrshld = PropertyTypeDef(
    code="FCG_RESULT_THRSHLD",
    description="""Threshold Stress Intensity Factor Range//Schwellenwert gegen Ermüdungsrissausbreitung""",
    data_type="REAL",
    property_label="Threshold Stress intensity Factor Range",
)


FcgStepPrecrack = PropertyTypeDef(
    code="FCG_STEP_PRECRACK",
    description="""Precracking Step//Precracking-Schritt""",
    data_type="BOOLEAN",
    property_label="Precracking Step",
)


FcgStepType = PropertyTypeDef(
    code="FCG_STEP_TYPE",
    description="""Step Type//Versuchsschritt-Typ""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="FCG_STEP_TYPE",
    property_label="Step Type",
)


FcgThrshld = PropertyTypeDef(
    code="FCG_THRSHLD",
    description="""Threshold Stress Intensity Factor Range Determination//Ermittlung des Schwellenwertes gegen Ermüdungsrissausbreitung""",
    data_type="BOOLEAN",
    property_label="Threshold Determination",
)


FemFitEq = PropertyTypeDef(
    code="FEM_FIT_EQ",
    description="""Equation of FEM Fit a = f(U)//Gleichung für FEM Fit a = f(U)""",
    data_type="VARCHAR",
    property_label="Equation of FEM Fit a = f(U)",
)


FigDpi = PropertyTypeDef(
    code="FIG_DPI",
    description="""Dots per inch (DPI)//Punkte pro Zoll""",
    data_type="INTEGER",
    property_label="Dots Per Inch (DPI)",
)


FileFormat = PropertyTypeDef(
    code="FILE_FORMAT",
    description="""File format//Dateiformat""",
    data_type="VARCHAR",
    property_label="File format",
)


FileSystemConfig = PropertyTypeDef(
    code="FILE_SYSTEM_CONFIG",
    description="""File system configuration//Konfiguration des Dateisystems""",
    data_type="MULTILINE_VARCHAR",
    property_label="File System Configuration",
)


FinalCracklength = PropertyTypeDef(
    code="FINAL_CRACKLENGTH",
    description="""Final Cracklength [mm]//Finale Risslänge [mm]""",
    data_type="REAL",
    property_label="Final Cracklength [mm]",
)


FinalCycles = PropertyTypeDef(
    code="FINAL_CYCLES",
    description="""Final Cycle Count//Finale Zyklenzahl""",
    data_type="REAL",
    property_label="Final Cycle Count",
)


FinalDeltaf = PropertyTypeDef(
    code="FINAL_DELTAF",
    description="""Final Delta F [kN]//Finales Delta F [kN]""",
    data_type="REAL",
    property_label="Final Delta F [kN]",
)


FinalDeltak = PropertyTypeDef(
    code="FINAL_DELTAK",
    description="""Final Delta K [MPa*m^0,5]//Finales Delta K [MPa*m^0,5]""",
    data_type="REAL",
    property_label="Final Delta K [MPa*m^0,5]",
)


FinalFamp = PropertyTypeDef(
    code="FINAL_FAMP",
    description="""Final F_amp [kN]//Finales F_amp [kN]""",
    data_type="REAL",
    property_label="Final F_amp [kN]",
)


FinalFmax = PropertyTypeDef(
    code="FINAL_FMAX",
    description="""Final F_max [kN]//Finales F_max [kN]""",
    data_type="REAL",
    property_label="Final F_max [kN]",
)


FinalFmean = PropertyTypeDef(
    code="FINAL_FMEAN",
    description="""Final F_mean [kN]//Finales F_mean [kN]""",
    data_type="REAL",
    property_label="Final F_mean [kN]",
)


FinalFmin = PropertyTypeDef(
    code="FINAL_FMIN",
    description="""Final F_min [kN]//Finales F_min [kN]""",
    data_type="REAL",
    property_label="Final F_min [kN]",
)


FinalGeomfun = PropertyTypeDef(
    code="FINAL_GEOMFUN",
    description="""Final Stress Intensity Factor Geometry Function//Finale Geometriefunktion des Spannungsintensitätsfaktors""",
    data_type="REAL",
    property_label="Final Stress Intensity Factor Geometry Function",
)


FinalRRatio = PropertyTypeDef(
    code="FINAL_R_RATIO",
    description="""Final R-Ratio//Finales R-Verhältnis""",
    data_type="REAL",
    property_label="Final R-Ratio",
)


FinalSsyRatio = PropertyTypeDef(
    code="FINAL_SSY_RATIO",
    description="""Ratio of Ligament Length to critical Ligament Length//Verhältnis von Ligamentlänge zu kritischer Ligamentlänge""",
    data_type="REAL",
    property_label="Ratio of Ligament Length to critical Ligament Length",
)


FinishedFlag = PropertyTypeDef(
    code="FINISHED_FLAG",
    description="""Marks the experiment as finished//Markiert das Experiment als abgeschlossen""",
    data_type="BOOLEAN",
    property_label="Experiment completed",
)


FirmwareVersion = PropertyTypeDef(
    code="FIRMWARE_VERSION",
    description="""The currently installed firmware version//Die aktuell installierte Firmware-Version""",
    data_type="VARCHAR",
    property_label="Current firmware version",
)


FlashLampShape = PropertyTypeDef(
    code="FLASH_LAMP_SHAPE",
    description="""Lamp shape//Lampenform""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="FLASH_LAMP_SHAPE",
    property_label="Lamp shape",
)


ForceTransducerType = PropertyTypeDef(
    code="FORCE_TRANSDUCER_TYPE",
    description="""Force Transducer Type Code as specified by Manufacturer//Typenbezeichnung des Herstellers für die Kraftmesseinrichtung""",
    data_type="VARCHAR",
    property_label="Force Transducer Type",
)


ForWhat = PropertyTypeDef(
    code="FOR_WHAT",
    description="""For what""",
    data_type="MULTILINE_VARCHAR",
    property_label="For what",
)


FramerateInHertz = PropertyTypeDef(
    code="FRAMERATE_IN_HERTZ",
    description="""Framerate in Hz//Bildwiederholrate in Hz""",
    data_type="REAL",
    property_label="Framerate [Hz]",
)


FrameCount = PropertyTypeDef(
    code="FRAME_COUNT",
    description="""Number of frames//Anzahl von Aufnahmen""",
    data_type="INTEGER",
    property_label="Number of frames",
)


FundingGrantNo = PropertyTypeDef(
    code="FUNDING_GRANT_NO",
    description="""Grant Number//Förderkennzeichen""",
    data_type="VARCHAR",
    property_label="Grant Number",
)


GasPressureBar = PropertyTypeDef(
    code="GAS_PRESSURE_BAR",
    description="""Gas pressure (in bar)// Gasdruck der Flasche (in bar)""",
    data_type="REAL",
    property_label="Gas pressure [bar]",
)


GasVolume = PropertyTypeDef(
    code="GAS_VOLUME",
    description="""Gas volume in liter//Gasvolumen in liter""",
    data_type="REAL",
    property_label="Gas Volume [liter]",
)


GeneticMaterial = PropertyTypeDef(
    code="GENETIC_MATERIAL",
    description="""Name of the transferred genetic material (e.g. gene name)//Name der übertragenen Nukleinsäure (z.B. Genname)""",
    data_type="MULTILINE_VARCHAR",
    property_label="Transferred genetic material",
)


GeneticMaterialJustification = PropertyTypeDef(
    code="GENETIC_MATERIAL_JUSTIFICATION",
    description="""Justification of the risk assessment: A keyword is to be given, e.g: Toxin gene, oncogene, uncharacterised DNA fragment, defined gene, cDNA, genomic DNA, viral genome, replication defects of infectious viruses, etc.//Begründung der Risikobewertung: Es ist ein Stichwort anzugeben, z.B: Toxin-Gen, Onkogen, uncharakterisiertes DNA-Fragment, definiertes Gen, cDNA, genomische DNA, virales Genom, Replikationsdefekte infektiöser Viren usw.""",
    data_type="MULTILINE_VARCHAR",
    property_label="Risk justification",
)


GeneticMaterialRiskPotential = PropertyTypeDef(
    code="GENETIC_MATERIAL_RISK_POTENTIAL",
    description="""Risk potential of transferred genetic material: Dangerous? Yes-No//Risikobewertung des übertragenen genetischen Materials: Gefährlich? Ja-Nein""",
    data_type="BOOLEAN",
    property_label="Risk potential of transf. material",
)


GentechBiosafetyOfficer = PropertyTypeDef(
    code="GENTECH_BIOSAFETY_OFFICER",
    description="""BAM Biosafety Officer according to GenTSV//BAM Beauftragte für biologische Sicherheit nach GenTSV""",
    data_type="OBJECT",
    object_code="PERSON.BAM",
    property_label="Genetic Engineering Facility Biosafety Officer",
)


GentechFacility = PropertyTypeDef(
    code="GENTECH_FACILITY",
    description="""BAM genetic engineering facility//BAM gentechnische Anlage""",
    data_type="OBJECT",
    object_code="BAM_GENTECH_FACILITY",
    property_label="BAM genetic engineering installation",
)


GentechProjectLead = PropertyTypeDef(
    code="GENTECH_PROJECT_LEAD",
    description="""BAM Project Leader according to GenTSV//BAM Project Leiter nach GenTSV""",
    data_type="OBJECT",
    object_code="PERSON.BAM",
    property_label="Genetic Engineering Facility Project Leader",
)


GentechSafetyLevel = PropertyTypeDef(
    code="GENTECH_SAFETY_LEVEL",
    description="""BAM genetic engineering facility//BAM gentechnische Anlage""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="GENTECH_SAFETY_LEVEL",
    property_label="Genetic Engineering Facility Safety Level",
)


GivenName = PropertyTypeDef(
    code="GIVEN_NAME",
    description="""Given name//Nachname""",
    data_type="VARCHAR",
    property_label="Given name",
)


GmoDisposalDate = PropertyTypeDef(
    code="GMO_DISPOSAL_DATE",
    description="""Genetically modified organism disposed of at//Genetisch veränderter Organismus entsorgt am""",
    data_type="DATE",
    property_label="Disposal date",
)


GmoDonor = PropertyTypeDef(
    code="GMO_DONOR",
    description="""Donor organism of which the genetic information is used for generating a GMO//Spenderorganismus, dessen genetische Information für die Erzeugung eines GVO verwendet wird""",
    data_type="OBJECT",
    object_code="SAMPLE.GMO_DONOR",
    property_label="Donor Organism",
)


GmoProductionDate = PropertyTypeDef(
    code="GMO_PRODUCTION_DATE",
    description="""Genetically modified organism produced on//Genetisch veränderter Organismus erzeugt am""",
    data_type="DATE",
    property_label="Production date",
)


GmoRecipient = PropertyTypeDef(
    code="GMO_RECIPIENT",
    description="""Recipient organism in which the genetic information is used for generating a GMO//Empfängerorganismus, in dem die genetische Information für die Erzeugung eines GVO verwendet wird""",
    data_type="OBJECT",
    object_code="SAMPLE.GMO_RECIPIENT",
    property_label="Recipient Organism",
)


GmoRiskGroup = PropertyTypeDef(
    code="GMO_RISK_GROUP",
    description="""Organism Risk Group Assignment of GMO according own Risk Assessment//Risikogruppenzuordnung des GVO anhand eigener Risikobewertung""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="ORGANISM_RISK_GROUP",
    property_label="GMO Risk Group",
)


Gpib = PropertyTypeDef(
    code="GPIB",
    description="""GPIB Interface//GPIB Schnittstelle""",
    data_type="BOOLEAN",
    property_label="GPIB Interface",
)


GpuNodesConfig = PropertyTypeDef(
    code="GPU_NODES_CONFIG",
    description="""GPU node configuration//Konfiguration der GPU-Knoten""",
    data_type="MULTILINE_VARCHAR",
    property_label="GPU Node Configuration",
)


HardwareTriggerInput = PropertyTypeDef(
    code="HARDWARE_TRIGGER_INPUT",
    description="""Utilized hardware trigger input//Genutzter Input für Hardware-Trigger""",
    data_type="VARCHAR",
    property_label="Utilized hardware trigger input",
)


HazardousSubstance = PropertyTypeDef(
    code="HAZARDOUS_SUBSTANCE",
    description="""Is the chemical a  hazardous substance according to the Hazardous Substances Ordinance (GefStoffV)?//Handelt es sich bei der Chemikalie um einen Gefahrenstoff nach der Gefahrenstoffverordnung (GefStoffV)?""",
    data_type="BOOLEAN",
    property_label="Hazardous Substance",
)


HeatingAreaDesc = PropertyTypeDef(
    code="HEATING_AREA_DESC",
    description="""Area of effect of the heating//Effektive Erwärmungsfläche""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="HEATING_AREA_DESC",
    property_label="Area of effect of the heating",
)


HeatingDurationInSeconds = PropertyTypeDef(
    code="HEATING_DURATION_IN_SECONDS",
    description="""Duration of the heating in s//Dauer der Erwärmung in s""",
    data_type="REAL",
    property_label="Duration of the heating [s]",
)


HeatingFrequencyInHertz = PropertyTypeDef(
    code="HEATING_FREQUENCY_IN_HERTZ",
    description="""Frequency of the heating in Hz//Frequenz der Erwärmung in Hz""",
    data_type="REAL",
    property_label="Frequency of the heating [Hz]",
)


HeatingHeightInMillimeter = PropertyTypeDef(
    code="HEATING_HEIGHT_IN_MILLIMETER",
    description="""Height of the heating area in mm//Höhe der erwärmten Fläche in mm""",
    data_type="REAL",
    property_label="Height of the heating area [mm]",
)


HeatingPrinciple = PropertyTypeDef(
    code="HEATING_PRINCIPLE",
    description="""Heating Principle//Prinzip der Erwärmung""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="HEATING_PRINCIPLE",
    property_label="Heating Principle",
)


HeatingTemperatureInCelsius = PropertyTypeDef(
    code="HEATING_TEMPERATURE_IN_CELSIUS",
    description="""Temperature of the heating element in °C//Eingestellte Temperatur der Erwärmung in °C""",
    data_type="REAL",
    property_label="Temperature of the heating element [°C]",
)


HeatingWidthInMillimeter = PropertyTypeDef(
    code="HEATING_WIDTH_IN_MILLIMETER",
    description="""Width of the heating area in mm//Breite der erwärmten Fläche in mm""",
    data_type="REAL",
    property_label="Width of the heating area [mm]",
)


HeatSourceDistanceInMillimeter = PropertyTypeDef(
    code="HEAT_SOURCE_DISTANCE_IN_MILLIMETER",
    description="""Distance heat source -> sample in mm//Abstand Wärmequelle zu Sample in mm""",
    data_type="REAL",
    property_label="Distance heat source -> sample [mm]",
)


HeatSourceOrientation = PropertyTypeDef(
    code="HEAT_SOURCE_ORIENTATION",
    description="""Orientation of the heat source w.r.t. the camera//Ausrichtung der Wärmequelle zur Kamera""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="THERMOGRAPHIC_SETUP_HS_ORIENT",
    property_label="Orientation of the heat source w.r.t. the camera",
)


Homepage = PropertyTypeDef(
    code="HOMEPAGE",
    description="""Homepage//Homepage""",
    data_type="HYPERLINK",
    property_label="Homepage",
)


HpcExtEmailAddress = PropertyTypeDef(
    code="HPC_EXT_EMAIL_ADDRESS",
    description="""Email address/point of contact for the external HPC//Email adresse/Kontaktstelle des externen HPC""",
    data_type="VARCHAR",
    property_label="Email Address/Contact for External HPC",
)


HpcExtPhysAddress = PropertyTypeDef(
    code="HPC_EXT_PHYS_ADDRESS",
    description="""Physical address of external HPC//Adresse des externen HPC""",
    data_type="VARCHAR",
    property_label="Physical Address of External HPC",
)


HpcJobId = PropertyTypeDef(
    code="HPC_JOB_ID",
    description="""Job ID in the HPC queue//Job-ID in der HPC-Warteschlange""",
    data_type="VARCHAR",
    property_label="HPC Job ID",
)


HpcJobQueue = PropertyTypeDef(
    code="HPC_JOB_QUEUE",
    description="""HPC queue used//Verwendete HPC-Warteschlange""",
    data_type="VARCHAR",
    property_label="HPC Job Queue",
)


IdEakte = PropertyTypeDef(
    code="ID_EAKTE",
    description="""Identifier used in E-Akte//E-Akte Nummer""",
    data_type="VARCHAR",
    property_label="ID E-Akte",
)


ImageHorizontalResolution = PropertyTypeDef(
    code="IMAGE_HORIZONTAL_RESOLUTION",
    description="""Horizontal resolution of the image [pixel]//Horizonzale Auflösung des Bildes [Pixel]""",
    data_type="INTEGER",
    property_label="Horizontal resolution [pixel]",
)


ImageSensorFramerate = PropertyTypeDef(
    code="IMAGE_SENSOR_FRAMERATE",
    description="""Highest framerate at indicated maximum resolution//Höchste erreichbare Bildrate bei voller Auflösung""",
    data_type="REAL",
    property_label="Framerate (at max. resolution)",
)


ImageSensorName = PropertyTypeDef(
    code="IMAGE_SENSOR_NAME",
    description="""Name of the image sensor model//Modellbezeichnung des Bildsensors""",
    data_type="VARCHAR",
    property_label="Sensor",
)


ImageSensorResolutionHorizontal = PropertyTypeDef(
    code="IMAGE_SENSOR_RESOLUTION_HORIZONTAL",
    description="""Horizontal camera resolution in pixel//Horizontale Auflösung des Sensors""",
    data_type="INTEGER",
    property_label="Horizontal sensor resolution [pixel]",
)


ImageSensorResolutionVertical = PropertyTypeDef(
    code="IMAGE_SENSOR_RESOLUTION_VERTICAL",
    description="""Vertical camera resolution in pixel//Vertikale Sensorauflösung in pixel""",
    data_type="INTEGER",
    property_label="Vertical camera resolution [pixel]",
)


ImageSensorSize = PropertyTypeDef(
    code="IMAGE_SENSOR_SIZE",
    description="""Size of the image sensor//Größenangabe des Bildsensors""",
    data_type="VARCHAR",
    property_label="Sensor size",
)


ImageSeriesCount = PropertyTypeDef(
    code="IMAGE_SERIES_COUNT",
    description="""Number of images recorded//Anzahl der aufgenommenen Bilder""",
    data_type="INTEGER",
    property_label="Number of images recorded",
)


ImageVerticalResolution = PropertyTypeDef(
    code="IMAGE_VERTICAL_RESOLUTION",
    description="""Vertical resolution of the image [pixel]////Vertikale Auflösung des Bildes [Pixel]""",
    data_type="INTEGER",
    property_label="Vertical resolution [pixel]",
)


IncrementDadn = PropertyTypeDef(
    code="INCREMENT_DADN",
    description="""Increment for da/dN calculation [mm]//Inkrement für die Rissfortschrittsratenbestimmung [mm]""",
    data_type="REAL",
    property_label="Increment for da/dN calculation [mm]",
)


InitialCracklength = PropertyTypeDef(
    code="INITIAL_CRACKLENGTH",
    description="""Initial Cracklength [mm]//Initiale Risslänge [mm]""",
    data_type="REAL",
    property_label="Initial Cracklength [mm]",
)


InitialCycles = PropertyTypeDef(
    code="INITIAL_CYCLES",
    description="""Initial Cycle Count//Initiale Zyklenzahl""",
    data_type="INTEGER",
    property_label="Initial Cycle Count",
)


InitialDeltaf = PropertyTypeDef(
    code="INITIAL_DELTAF",
    description="""Initial Delta F [kN]//Initiales Delta F [kN]""",
    data_type="REAL",
    property_label="Initial Delta F [kN]",
)


InitialDeltak = PropertyTypeDef(
    code="INITIAL_DELTAK",
    description="""Initial Delta K [MPa*m^0,5]//Initiales Delta K [MPa*m^0,5]""",
    data_type="REAL",
    property_label="Initial Delta K [MPa*m^0,5]",
)


InitialFamp = PropertyTypeDef(
    code="INITIAL_FAMP",
    description="""Initial F_amp [kN]//Initiales F_amp [kN]""",
    data_type="REAL",
    property_label="Initial F_amp [kN]",
)


InitialFmax = PropertyTypeDef(
    code="INITIAL_FMAX",
    description="""Initial F_max [kN]//Initiales F_max [kN]""",
    data_type="REAL",
    property_label="Initial F_max [kN]",
)


InitialFmean = PropertyTypeDef(
    code="INITIAL_FMEAN",
    description="""Initial F_mean [kN]//Initiales F_mean [kN]""",
    data_type="REAL",
    property_label="Initial F_mean [kN]",
)


InitialFmin = PropertyTypeDef(
    code="INITIAL_FMIN",
    description="""Initial F_min [kN]//Initiales F_min [kN]""",
    data_type="REAL",
    property_label="Initial F_min [kN]",
)


InitialGeomfun = PropertyTypeDef(
    code="INITIAL_GEOMFUN",
    description="""Initial Stress Intensity Factor Geometry Function//Initiale Geometriefunktion des Spannungsintensitätsfaktors""",
    data_type="REAL",
    property_label="Initial Stress Intensity Factor Geometry Function",
)


InitialKamp = PropertyTypeDef(
    code="INITIAL_KAMP",
    description="""Initial K_amp [MPa*m^0,5]//Initiales K_amp [MPa*m^0,5]""",
    data_type="REAL",
    property_label="Initial K_amp [MPa*m^0,5]",
)


InitialKmax = PropertyTypeDef(
    code="INITIAL_KMAX",
    description="""Initial K_max [MPa*m^0,5]//Initiales K_max [MPa*m^0,5]""",
    data_type="REAL",
    property_label="Initial K_max [MPa*m^0,5]",
)


InitialKmean = PropertyTypeDef(
    code="INITIAL_KMEAN",
    description="""Initial K_mean [MPa*m^0,5]//Initiales K_mean [MPa*m^0,5]""",
    data_type="REAL",
    property_label="Initial K_mean [MPa*m^0,5]",
)


InitialKmin = PropertyTypeDef(
    code="INITIAL_KMIN",
    description="""Initial K_min [MPa*m^0,5]//Initiales K_min [MPa*m^0,5]""",
    data_type="REAL",
    property_label="Initial K_min [MPa*m^0,5]",
)


InitialRRatio = PropertyTypeDef(
    code="INITIAL_R_RATIO",
    description="""Initial R-Ratio//Initiales R-Verhältnis""",
    data_type="REAL",
    property_label="Initial R-Ratio",
)


InitialSsyRatio = PropertyTypeDef(
    code="INITIAL_SSY_RATIO",
    description="""Ratio of Ligament Length to critical Ligament Length//Verhältnis von Ligamentlänge zu kritischer Ligamentlänge""",
    data_type="REAL",
    property_label="Ratio of Ligament Length to critical Ligament Length",
)


# ! Missing `object_code`
Instrument = PropertyTypeDef(
    code="INSTRUMENT",
    description="""Testing machine or measurement device//Prüfmaschine oder Messgerät""",
    data_type="OBJECT",
    property_label="Testing Machine or Measurement Device",
)


InstrumentStatus = PropertyTypeDef(
    code="INSTRUMENT_STATUS",
    description="""Instrument status//Instrumentenstatus""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="INSTRUMENT_STATUS",
    property_label="Instrument Status",
)


IntegrationTimeInMicrosecond = PropertyTypeDef(
    code="INTEGRATION_TIME_IN_MICROSECOND",
    description="""Integration time in µs//Integrationszeit in µs""",
    data_type="REAL",
    property_label="Integration time [µs]",
)


InventoryNo = PropertyTypeDef(
    code="INVENTORY_NO",
    description="""PARFIS inventory number (8-digit)//PARFIS Inventarnummer (8-stellig)""",
    data_type="INTEGER",
    property_label="Inventory Number",
)


InventoryNoAdd = PropertyTypeDef(
    code="INVENTORY_NO_ADD",
    description="""PARFIS inventory number (8-digit)//PARFIS Inventarnummer (8-stellig)""",
    data_type="INTEGER",
    property_label="Inventory Number Addition",
)


IupacName = PropertyTypeDef(
    code="IUPAC_NAME",
    description="""IUPAC Name//IUPAC-Name""",
    data_type="VARCHAR",
    property_label="IUPAC Name",
)


JupyterHeaders = PropertyTypeDef(
    code="JUPYTER_HEADERS",
    description="""Headers used in the notebook//Im Notebook verwendete Headers""",
    data_type="MULTILINE_VARCHAR",
    property_label="Headers Used (Programming)",
)


JupyterModules = PropertyTypeDef(
    code="JUPYTER_MODULES",
    description="""Modules used in the notebook//Im Notebook verwendete Module""",
    data_type="MULTILINE_VARCHAR",
    property_label="Modules Used",
)


LaserBeamDiameterInMm = PropertyTypeDef(
    code="LASER_BEAM_DIAMETER_IN_MM",
    description="""Output laser beam diameter in mm//Durchmesser des Ausgangslaserstrahls in mm""",
    data_type="REAL",
    property_label="Beam Diameter [mm]",
)


LaserClass = PropertyTypeDef(
    code="LASER_CLASS",
    description="""Laser class rating according to DIN EN 60825-1//Laserklasse nach DIN EN 60825-1""",
    data_type="VARCHAR",
    property_label="Laser class",
)


LaserM2 = PropertyTypeDef(
    code="LASER_M2",
    description="""M² (parameter which relates the beam divergence of a laser beam to the minimum focussed spot size that can be achieved)//M² (Beugungsmaßzahl, welche beschreibt, wie gut ein Laserstrahl bei einer gegebenen Divergenz fokussiert werden kann)""",
    data_type="REAL",
    property_label="M²",
)


LaserPulseEnergyNormalInMj = PropertyTypeDef(
    code="LASER_PULSE_ENERGY_NORMAL_IN_MJ",
    description="""Nominal pulse energy in mJ//Nominale Pulsenergie in mJ""",
    data_type="REAL",
    property_label="Nominal Pulse Energy [mJ]",
)


LaserRepetitionRateInHz = PropertyTypeDef(
    code="LASER_REPETITION_RATE_IN_HZ",
    description="""Maximum repetition rate (-1 for CW) in Hz//Maximale Wiederholrate (-1 für CW) in Hz""",
    data_type="REAL",
    property_label="Repetition Rate [Hz]",
)


LaserType = PropertyTypeDef(
    code="LASER_TYPE",
    description="""Type of the laser//Lasertyp""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="LASER_TYPE",
    property_label="Laser Type",
)


LaserWavelength = PropertyTypeDef(
    code="LASER_WAVELENGTH",
    description="""Wavelength of emitted laser light//Wellenlänge des Laserlichts""",
    data_type="VARCHAR",
    property_label="Laser wavelength [nm]",
)


LaserWavelengthInNm = PropertyTypeDef(
    code="LASER_WAVELENGTH_IN_NM",
    description="""List all allowed wavelengths following the XML schema given//Auflistung aller zulässigen Wellenlängen gemäß dem angegebenen XML-Schema""",
    data_type="XML",
    property_label="Operating Wavelength(s) [nm]",
)


LastCalibration = PropertyTypeDef(
    code="LAST_CALIBRATION",
    description="""Last Calibration//Letzte Kalibrierung""",
    data_type="DATE",
    property_label="Last Calibration",
)


LastCheck = PropertyTypeDef(
    code="LAST_CHECK",
    description="""Date of the last check//Datum der letzten Überprüfung""",
    data_type="DATE",
    property_label="Date of last check",
)


LastSystemcheck = PropertyTypeDef(
    code="LAST_SYSTEMCHECK",
    description="""Date of the last system check//Datum des letzten Systemchecks""",
    data_type="DATE",
    property_label="Last System Check",
)


LatticeAngalphaInDeg = PropertyTypeDef(
    code="LATTICE_ANGALPHA_IN_DEG",
    description="""Lattice angle (alpha) [Degrees]//Gitterwinkel (alpha) [Grad]""",
    data_type="REAL",
    property_label="Lattice Angle (alpha) [Degrees]",
)


LatticeAngbetaInDeg = PropertyTypeDef(
    code="LATTICE_ANGBETA_IN_DEG",
    description="""Lattice angle (beta) [Degrees]//Gitterwinkel (beta) [Grad]""",
    data_type="REAL",
    property_label="Lattice Angle (beta) [Degrees]",
)


LatticeAnggammaInDeg = PropertyTypeDef(
    code="LATTICE_ANGGAMMA_IN_DEG",
    description="""Lattice angle (gamma) [Degrees]//Gitterwinkel (gamma) [Grad]""",
    data_type="REAL",
    property_label="Lattice Angle (gamma) [Degrees]",
)


LatticeCOverA = PropertyTypeDef(
    code="LATTICE_C_OVER_A",
    description="""Lattice parameter (c over a)//Gitterparameter (c über a)""",
    data_type="REAL",
    property_label="Lattice Parameter (c over a)",
)


LatticeParamAInA = PropertyTypeDef(
    code="LATTICE_PARAM_A_IN_A",
    description="""Lattice parameter (a) [Å]//Gitterparameter (a) [Å]""",
    data_type="REAL",
    property_label="Lattice Parameter (a) [Å]",
)


LatticeParamBInA = PropertyTypeDef(
    code="LATTICE_PARAM_B_IN_A",
    description="""Lattice parameter (b) [Å]//Gitterparameter (b) [Å]""",
    data_type="REAL",
    property_label="Lattice Parameter (b) [Å]",
)


LatticeParamCInA = PropertyTypeDef(
    code="LATTICE_PARAM_C_IN_A",
    description="""Lattice parameter (c) [Å]//Gitterparameter (c) [Å]""",
    data_type="REAL",
    property_label="Lattice Parameter (c) [Å]",
)


LatticeVolumeInA3 = PropertyTypeDef(
    code="LATTICE_VOLUME_IN_A3",
    description="""Lattice volume [Å^3]//Volumen des Gitters [Å^3]""",
    data_type="REAL",
    property_label="Lattice Volume [Å^3]",
)


LensApertureMax = PropertyTypeDef(
    code="LENS_APERTURE_MAX",
    description="""Maximum Aperture [f/]//Maximale Blendenöffnung [f/]""",
    data_type="REAL",
    property_label="Maximum Aperture [f/]",
)


LensApertureMin = PropertyTypeDef(
    code="LENS_APERTURE_MIN",
    description="""Minimum Aperture [f/]//Minimale Blendenzahl [f/]""",
    data_type="REAL",
    property_label="Minimum Aperture [f/]",
)


LensConfocal = PropertyTypeDef(
    code="LENS_CONFOCAL",
    description="""Confocal optics//Konfokale Linse""",
    data_type="BOOLEAN",
    property_label="Confocal",
)


LensFocallength = PropertyTypeDef(
    code="LENS_FOCALLENGTH",
    description="""Focal length of optical lens [mm]//Brennweite der Kameralinse [mm]""",
    data_type="REAL",
    property_label="Focal length [mm]",
)


LensMountType = PropertyTypeDef(
    code="LENS_MOUNT_TYPE",
    description="""The lens mount of a camera or lens//Art des Objektivanschluss""",
    data_type="VARCHAR",
    property_label="Lens mount",
)


License = PropertyTypeDef(
    code="LICENSE",
    description="""License//Lizenz""",
    data_type="VARCHAR",
    property_label="License",
)


LinkEakte = PropertyTypeDef(
    code="LINK_EAKTE",
    description="""Link to E-Akte//Link zum Dokument in der E-Akte""",
    data_type="HYPERLINK",
    property_label="Link E-Akte",
)


LoadFrameOrientation = PropertyTypeDef(
    code="LOAD_FRAME_ORIENTATION",
    description="""Load Frame Orientation//Orientierung des Lastrahmens""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="LOAD_FRAME_ORIENTATION",
    property_label="Load Frame Orientation",
)


LoadFrameType = PropertyTypeDef(
    code="LOAD_FRAME_TYPE",
    description="""Load Frame Type Code as specified by Manufacturer//Typenbezeichnung des Herstellers für den Lastrahmen""",
    data_type="VARCHAR",
    property_label="Load Frame Type Code as specified by Manufacturer",
)


LocationAddress = PropertyTypeDef(
    code="LOCATION_ADDRESS",
    description="""Location address//Adresse des Messortes""",
    data_type="VARCHAR",
    property_label="Location address",
)


LocationLatitudeInDegrees = PropertyTypeDef(
    code="LOCATION_LATITUDE_IN_DEGREES",
    description="""Location latitude in °//Breitengrad des Messortes in °""",
    data_type="REAL",
    property_label="Location latitude [°]",
)


LocationLongitudeInDegrees = PropertyTypeDef(
    code="LOCATION_LONGITUDE_IN_DEGREES",
    description="""Location longitude in °//Längengrad des Messortes in °""",
    data_type="REAL",
    property_label="Location longitude [°]",
)


LotNumber = PropertyTypeDef(
    code="LOT_NUMBER",
    description="""Lot/Batch Number//Chargennummer""",
    data_type="VARCHAR",
    property_label="Lot/Batch Number",
)


Manufacturer = PropertyTypeDef(
    code="MANUFACTURER",
    description="""Manufacturer//Hersteller""",
    data_type="VARCHAR",
    property_label="Manufacturer",
)


MassMolar = PropertyTypeDef(
    code="MASS_MOLAR",
    description="""Molar Mass [g/mol]//Molare Masse [g/mol]""",
    data_type="REAL",
    property_label="Molar Mass",
)


MassSpecType = PropertyTypeDef(
    code="MASS_SPEC_TYPE",
    description="""Mass Spectrometer Type//Massenspektrometer-Typ""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="MASS_SPEC_TYPE",
    property_label="MS Type",
)


Material = PropertyTypeDef(
    code="MATERIAL",
    description="""Material//Material""",
    data_type="VARCHAR",
    property_label="Material",
)


MaterialGroup = PropertyTypeDef(
    code="MATERIAL_GROUP",
    description="""Material group (e.g. steel group)//Materialgruppe (z.B. Stahlgruppe)""",
    data_type="VARCHAR",
    property_label="Material group",
)


MaterialNumber = PropertyTypeDef(
    code="MATERIAL_NUMBER",
    description="""Material number//Werkstoffnummer""",
    data_type="VARCHAR",
    property_label="Material number",
)


MatBondingType = PropertyTypeDef(
    code="MAT_BONDING_TYPE",
    description="""Material bonding type//Material Atombindungstyp""",
    data_type="VARCHAR",
    property_label="Material Bonding Type",
)


MatCode = PropertyTypeDef(
    code="MAT_CODE",
    description="""Material Number//Werkstoffnummer""",
    data_type="OBJECT",
    object_code="RAW_MATERIAL_CODE",
    property_label="Material Number",
)


MatScale = PropertyTypeDef(
    code="MAT_SCALE",
    description="""Material scale//Material Skala""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="MAT_SCALE",
    property_label="Material Scale",
)


MatStructure = PropertyTypeDef(
    code="MAT_STRUCTURE",
    description="""Material Structure//Materialstruktur""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="MAT_STRUCTURE",
    property_label="Material Structure",
)


Maxrange = PropertyTypeDef(
    code="MAXRANGE",
    description="""Maximum Range [V]//Größter Messbereich [V]""",
    data_type="REAL",
    property_label="Maximum Range [V]",
)


MaxrangeResolution = PropertyTypeDef(
    code="MAXRANGE_RESOLUTION",
    description="""Resolution at maximum Range [nV]//Auflösung im größten Messbereich [nV]""",
    data_type="REAL",
    property_label="Resolution at maximum Range [nV]",
)


MaxCommonModeVoltage = PropertyTypeDef(
    code="MAX_COMMON_MODE_VOLTAGE",
    description="""Maximum Common Mode Voltage [V]//Maximale Gleichtaktspannung [V]""",
    data_type="REAL",
    property_label="Maximum Common Mode Voltage [V]",
)


MaxDynamicForce = PropertyTypeDef(
    code="MAX_DYNAMIC_FORCE",
    description="""Maximum Dynamic Force in kN//Maximale dynamische Kraft [kN[""",
    data_type="REAL",
    property_label="Maximum Dynamic Force [kN]",
)


MaxExcitationVoltage = PropertyTypeDef(
    code="MAX_EXCITATION_VOLTAGE",
    description="""Maximum Excitation Voltage [V]//Maximale Speisespannung [V]""",
    data_type="REAL",
    property_label="Maximum Excitation Voltage [V]",
)


MaxIters = PropertyTypeDef(
    code="MAX_ITERS",
    description="""Maximum number of iterations//Maximale Anzahl von Iterationen""",
    data_type="INTEGER",
    property_label="Maximum Iterations",
)


MaxLoadDynamicPrimary = PropertyTypeDef(
    code="MAX_LOAD_DYNAMIC_PRIMARY",
    description="""Maximum dynamic load of primary load type//Maximale dynamische Last der primären Belastungsart""",
    data_type="REAL",
    property_label="Maximum Dynamic Load (Primary) [kN/kNm]",
)


MaxLoadDynamicSecondary = PropertyTypeDef(
    code="MAX_LOAD_DYNAMIC_SECONDARY",
    description="""Maximum dynamic load of secondary load type//Maximale dynamische Last der sekundären Belastungsart""",
    data_type="REAL",
    property_label="Maximum Dynamic Load (Secondary) [kN/kNm]",
)


MaxLoadStaticPrimary = PropertyTypeDef(
    code="MAX_LOAD_STATIC_PRIMARY",
    description="""Maximum static load of primary load type//Maximale statische Last der primären Belastungsart""",
    data_type="REAL",
    property_label="Maximum Static Load (Primary) [kN/kNm]",
)


MaxLoadStaticSecondary = PropertyTypeDef(
    code="MAX_LOAD_STATIC_SECONDARY",
    description="""Maximum static load of secondary load type (in case of combined load-type)//Maximale statische Last der sekundären Belastungsart (falls kombinierte Antriebsart)""",
    data_type="REAL",
    property_label="Maximum Static Load (Secondary) [kN/kNm]",
)


MaxOutputCurrent = PropertyTypeDef(
    code="MAX_OUTPUT_CURRENT",
    description="""Maximum Output Current [A]//Maximaler Ausgangsstrom [A]""",
    data_type="REAL",
    property_label="Maximum Output Current [A]",
)


MaxOutputVoltage = PropertyTypeDef(
    code="MAX_OUTPUT_VOLTAGE",
    description="""Maximum Output Voltage [V]//Maximale Ausgangsspannung [V]""",
    data_type="REAL",
    property_label="Maximum Output Voltage [V]",
)


MaxPressure = PropertyTypeDef(
    code="MAX_PRESSURE",
    description="""Maximum Operating Pressure [bar]//Maximaler Betriebsdruck [bar]""",
    data_type="REAL",
    property_label="Maximum Operating Pressure [bar]",
)


MaxPulseEnergyInJoule = PropertyTypeDef(
    code="MAX_PULSE_ENERGY_IN_JOULE",
    description="""Maximum pulse energy in J//Maximale Pulsenergie in J""",
    data_type="REAL",
    property_label="Maximum pulse energy [J]",
)


MaxSpaceHor = PropertyTypeDef(
    code="MAX_SPACE_HOR",
    description="""Maximum horizontal space between Columns [mm]//Maximaler horizontaler Bauraum zwischen den Säulen [mm]""",
    data_type="REAL",
    property_label="Maximum horizontal space between Columns [mm]",
)


MaxSpaceVert = PropertyTypeDef(
    code="MAX_SPACE_VERT",
    description="""Maximum vertical space for Specimens and Grips [mm]//Maximaler vertikaler Bauraum für Proben und Probenhalter [mm]""",
    data_type="REAL",
    property_label="Maximum vertical space for Specimens and Grips [mm]",
)


MaxStaticForce = PropertyTypeDef(
    code="MAX_STATIC_FORCE",
    description="""Maximum Static Force in kN//Maximale statische Kraft [kN]""",
    data_type="REAL",
    property_label="Maximum Static Force [kN]",
)


MaxStroke = PropertyTypeDef(
    code="MAX_STROKE",
    description="""Maximum Stroke//Maximaler Maschinenweg""",
    data_type="REAL",
    property_label="Maximum Stroke [mm]",
)


MeasurementDate = PropertyTypeDef(
    code="MEASUREMENT_DATE",
    description="""Measurement Date//Messdatum""",
    data_type="DATE",
    property_label="Measurement Date",
)


MeasurementId = PropertyTypeDef(
    code="MEASUREMENT_ID",
    description="""Div. internal measurement ID//FB-interne Messdatennummer""",
    data_type="INTEGER",
    property_label="Measurement ID",
)


MicFcgFracsurfCracklengthCycles = PropertyTypeDef(
    code="MIC_FCG_FRACSURF_CRACKLENGTH_CYCLES",
    description="""Cycle Count corresponding with Cracklength measured on Fracture Surface//Mit der auf der Bruchfläche gemessenen Länge korrespondierende Zyklenzahl""",
    data_type="INTEGER",
    property_label="Cycle Count corresponding with Cracklength measured on Fracture Surface",
)


MicFcgFracsurfCracklengthType = PropertyTypeDef(
    code="MIC_FCG_FRACSURF_CRACKLENGTH_TYPE",
    description="""Type of Cracklength measured on Fracture Surface//Art der auf der Bruchfläche gemessenen Risslänge""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="MICROSCOPY_FCG_CRACKLENGTH_TYPE",
    property_label="Type of Cracklength measured on Fracture Surface",
)


MicFcgFracsurfCracklengthValue = PropertyTypeDef(
    code="MIC_FCG_FRACSURF_CRACKLENGTH_VALUE",
    description="""Value of Cracklength measured on Fracture Surface [mm]//Wert der auf der Bruchfläche gemessenen Risslänge [mm]""",
    data_type="REAL",
    property_label="Value of Cracklength measured on Fracture Surface [mm]",
)


Minrange = PropertyTypeDef(
    code="MINRANGE",
    description="""Minimum Range [V]//Kleinster Messbereich [V]""",
    data_type="REAL",
    property_label="Minimum Range [V]",
)


MinrangeResolution = PropertyTypeDef(
    code="MINRANGE_RESOLUTION",
    description="""Resolution at minimum Range [nV]//Auflösung im kleinsten Messbereich [nV]""",
    data_type="REAL",
    property_label="Resolution at minimum Range [nV]",
)


MinExcitationVoltage = PropertyTypeDef(
    code="MIN_EXCITATION_VOLTAGE",
    description="""Minimum Excitation Voltage [V]//Minimale Speisespannung [V]""",
    data_type="REAL",
    property_label="Minimum Excitation Voltage [V]",
)


MiscHydCompType = PropertyTypeDef(
    code="MISC_HYD_COMP_TYPE",
    description="""Type Code as specified by Manufacturer//Typenbezeichnung des Herstellers""",
    data_type="VARCHAR",
    property_label="Type Code as specified by Manufacturer",
)


MonitoringDate = PropertyTypeDef(
    code="MONITORING_DATE",
    description="""Monitoring date//Datum der Überprüfung""",
    data_type="DATE",
    property_label="Monitoring date",
)


MonitoringValue = PropertyTypeDef(
    code="MONITORING_VALUE",
    description="""Monitoring value or status//Messwert oder Status""",
    data_type="VARCHAR",
    property_label="Monitoring value",
)


MsHyphenationMethod = PropertyTypeDef(
    code="MS_HYPHENATION_METHOD",
    description="""Hyphenation (DI, LC, GC, CE)//Probeninjektion (DI, LC, GC, CE)""",
    data_type="VARCHAR",
    property_label="Hyphenation method",
)


MsIonizationMode = PropertyTypeDef(
    code="MS_IONIZATION_MODE",
    description="""Ionization mode (pos/neg)//Ionisierung (pos/neg)""",
    data_type="VARCHAR",
    property_label="Ionization mode",
)


MultiMatScale = PropertyTypeDef(
    code="MULTI_MAT_SCALE",
    description="""Material scales if multiple (refer to property `Material Scale` for terminology)//Materialskala, falls mehrere vorhanden sind (siehe „MaterialScale“-Eigenschaft zur Terminologie)""",
    data_type="VARCHAR",
    property_label="Material Scales if Multiple",
)


MurnEqnOfState = PropertyTypeDef(
    code="MURN_EQN_OF_STATE",
    description="""Equation of state used for fit//Für das Fitting verwendete Zustandsgleichung""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="MURN_EQN_OF_STATE",
    property_label="Equation of State",
)


MurnFitEqnOrder = PropertyTypeDef(
    code="MURN_FIT_EQN_ORDER",
    description="""Fit order (if polynomial)//Grad des Polynoms""",
    data_type="INTEGER",
    property_label="Fit Order (if Polynomial)",
)


MurnNDataPoints = PropertyTypeDef(
    code="MURN_N_DATA_POINTS",
    description="""Number of data points//Anzahl der Datenpunkte""",
    data_type="INTEGER",
    property_label="Number of Data Points",
)


MurnStrainvolRange = PropertyTypeDef(
    code="MURN_STRAINVOL_RANGE",
    description="""Volume range (fractional)//Volumenbereich (fraktioniert)""",
    data_type="REAL",
    property_label="Volume Range (Fractional)",
)


MurnStrainAxes = PropertyTypeDef(
    code="MURN_STRAIN_AXES",
    description="""Axes along which cell is strained//Achsen, entlang derer die Zelle belastet wird""",
    data_type="VARCHAR",
    property_label="Strain Axes",
)


Ncores = PropertyTypeDef(
    code="NCORES",
    description="""Number of cores used//Anzahl der Kerne""",
    data_type="INTEGER",
    property_label="Number of Cores",
)


Ngpus = PropertyTypeDef(
    code="NGPUS",
    description="""Number of GPUs used//Anzahl der GPUs""",
    data_type="INTEGER",
    property_label="Number of GPUs",
)


NormAnalyzedMatrix = PropertyTypeDef(
    code="NORM_ANALYZED_MATRIX",
    description="""Analyzed matrix//Analysierte Matrix""",
    data_type="VARCHAR",
    property_label="Analyzed matrix",
)


NormTitle = PropertyTypeDef(
    code="NORM_TITLE",
    description="""Title of the norm//Titel der Norm""",
    data_type="VARCHAR",
    property_label="Title",
)


NormUrl = PropertyTypeDef(
    code="NORM_URL",
    description="""Source URL of Norm//Quell URL der Norm""",
    data_type="HYPERLINK",
    property_label="Source URL",
)


Notes = PropertyTypeDef(
    code="NOTES",
    description="""Notes//Notizen""",
    data_type="MULTILINE_VARCHAR",
    property_label="Notes",
)


Nthreads = PropertyTypeDef(
    code="NTHREADS",
    description="""Number of Threads used//Anzahl der Threads""",
    data_type="INTEGER",
    property_label="Number of Threads",
)


NucPerformed = PropertyTypeDef(
    code="NUC_PERFORMED",
    description="""NUC-performed//NUC-durchgeführt""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="NUC_PERFORMED",
    property_label="NUC-performed",
)


NumberConsecutiveAcquisitons = PropertyTypeDef(
    code="NUMBER_CONSECUTIVE_ACQUISITONS",
    description="""Number of consecutive acquisitions//Anzahl der konsekutiven Aufnahmen""",
    data_type="INTEGER",
    property_label="Number of consecutive acquisitions",
)


NumberOfAnalogOutputs = PropertyTypeDef(
    code="NUMBER_OF_ANALOG_OUTPUTS",
    description="""Number of Analog Outputs//Anzahl Analoger Ausgänge""",
    data_type="INTEGER",
    property_label="Number of Analog Outputs",
)


NumberOfChannels = PropertyTypeDef(
    code="NUMBER_OF_CHANNELS",
    description="""Number of Channels//Anzahl der Kanäle""",
    data_type="INTEGER",
    property_label="Number of Channels",
)


NumberOfInputs = PropertyTypeDef(
    code="NUMBER_OF_INPUTS",
    description="""Number of Inputs//Anzahl der Eingänge""",
    data_type="INTEGER",
    property_label="Number of Inputs",
)


NumberOfOutputs = PropertyTypeDef(
    code="NUMBER_OF_OUTPUTS",
    description="""Number of Outputs//Anzahl der Ausgänge""",
    data_type="INTEGER",
    property_label="Number of Outputs",
)


NumberPretriggerFrames = PropertyTypeDef(
    code="NUMBER_PRETRIGGER_FRAMES",
    description="""Number of recorded pretrigger frames//Anzahl der Pretrigger Frames""",
    data_type="INTEGER",
    property_label="Number of recorded pretrigger frames",
)


NumberRecordedFrames = PropertyTypeDef(
    code="NUMBER_RECORDED_FRAMES",
    description="""Number of recorded frames//Anzahl der aufgenommenen Frames""",
    data_type="INTEGER",
    property_label="Number of recorded frames",
)


NAtomsTotal = PropertyTypeDef(
    code="N_ATOMS_TOTAL",
    description="""Total number of atoms in sample//Gesamtzahl der Atome in der Probe""",
    data_type="INTEGER",
    property_label="Total Number of Atoms",
)


OperatingSystem = PropertyTypeDef(
    code="OPERATING_SYSTEM",
    description="""Operating System (OS)//Betriebssystem""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="OPERATING_SYSTEM",
    property_label="Operating System",
)


OrganismFamily = PropertyTypeDef(
    code="ORGANISM_FAMILY",
    description="""Organism family assignment according Central Commision for Biological Safety//Organismen Familienzuordnung anhand ZKBS""",
    data_type="VARCHAR",
    property_label="Organism Family Assignment",
)


OrganismFootnote = PropertyTypeDef(
    code="ORGANISM_FOOTNOTE",
    description="""Central commission for biological safety Footnotes//Zentral Komission für Biologische Sicherheit ZKBS Fußnote""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="ORGANISM_FOOTNOTE_ZKBS",
    property_label="ZKBS Footnote",
)


OrganismGroup = PropertyTypeDef(
    code="ORGANISM_GROUP",
    description="""Organism group assignment according to the central comission of biological safety or category in the BAM-Biomicrosearch//Organismen Gruppenzuordnung anhand ZKBS bzw. die Kategorie in der BAM-Microsearch Datenbank database//Organismen Gruppenzuordnung anhand ZKBS bzw. die Kategorie in der BAM-Microsearch Datenbank""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="ORGANISM_GROUP",
    property_label="Organism Group Assignment",
)


OrganismRiskGroup = PropertyTypeDef(
    code="ORGANISM_RISK_GROUP",
    description="""Organism Risk Group Assignment//Risikogruppenzuordnung des Organismus""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="ORGANISM_RISK_GROUP",
    property_label="Organism Risk Group Assignement",
)


OrganismZkbsStatement = PropertyTypeDef(
    code="ORGANISM_ZKBS_STATEMENT",
    description="""Central Commission for Biological Safety  Statement//Zentral Komission für Biologische Sicherheit ZKBS-Stellungnahme""",
    data_type="HYPERLINK",
    property_label="Central Commission for Biological Safety  Statement",
)


ParfisProjectNo = PropertyTypeDef(
    code="PARFIS_PROJECT_NO",
    description="""PARFIS Project Number: `VhXXXX`//PARFIS Vorhabennummer: `VhXXXX`""",
    data_type="VARCHAR",
    property_label="PARFIS Project Number",
)


PeriodicBoundaryX = PropertyTypeDef(
    code="PERIODIC_BOUNDARY_X",
    description="""Simulation periodicity in X-direction//Periodizität der Simulation in X-Richtung""",
    data_type="BOOLEAN",
    property_label="Simulation Periodicity in X-Direction",
)


PeriodicBoundaryY = PropertyTypeDef(
    code="PERIODIC_BOUNDARY_Y",
    description="""Simulation periodicity in Y-direction//Periodizität der Simulation in Y-Richtung""",
    data_type="BOOLEAN",
    property_label="Simulation Periodicity in Y-Direction",
)


PeriodicBoundaryZ = PropertyTypeDef(
    code="PERIODIC_BOUNDARY_Z",
    description="""Simulation periodicity in Z-direction//Periodizität der Simulation in Z-Richtung""",
    data_type="BOOLEAN",
    property_label="Simulation Periodicity in Z-Direction",
)


PersonAlias = PropertyTypeDef(
    code="PERSON_ALIAS",
    description="""Name abbreviation of a person//Laborkürzel einer Person""",
    data_type="VARCHAR",
    property_label="Person alias",
)


PersonStatus = PropertyTypeDef(
    code="PERSON_STATUS",
    description="""Person status//Anwesenheitsstatus einer Person""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="PERSON_STATUS",
    property_label="Person status",
)


PhysicalState = PropertyTypeDef(
    code="PHYSICAL_STATE",
    description="""Physical state of a material // Physikalischer Zustand eines Materials""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="PHYSICAL_STATE",
    property_label="Physical State",
)


PlasmidBacterialAntibioticResistance = PropertyTypeDef(
    code="PLASMID_BACTERIAL_ANTIBIOTIC_RESISTANCE",
    description="""Bacterial antibiotic resistance//Bakterielle Antibiotikaresistenz zur Selektion""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="PLASMID_BACTERIAL_ANTIBIOTIC_RESISTANCE",
    property_label="Bacterial Antibiotic Resistance",
)


PlasmidMarker = PropertyTypeDef(
    code="PLASMID_MARKER",
    description="""Marker to select the strain/cell line after transformation/transfection//Marker zur Selektion d. Stamm/Zelllinie nach der Transformation/Transfektion""",
    data_type="VARCHAR",
    property_label="Plasmid marker",
)


PlasmidOri = PropertyTypeDef(
    code="PLASMID_ORI",
    description="""Bacterial Origin of Replication (plasmid copy number)//Bakterieller Replikationsursprung""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="PLASMID_ORI",
    property_label="Origin of Replication",
)


PlasmidOtherMarker = PropertyTypeDef(
    code="PLASMID_OTHER_MARKER",
    description="""Other marker useful for selection//Andere nützliche Marker zur Selektion""",
    data_type="VARCHAR",
    property_label="Plasmid other marker",
)


PlotLegend = PropertyTypeDef(
    code="PLOT_LEGEND",
    description="""Plot legend//Legende des Plots""",
    data_type="MULTILINE_VARCHAR",
    property_label="Plot Legend",
)


PlotXLabel = PropertyTypeDef(
    code="PLOT_X_LABEL",
    description="""Label of X-axis//X-Achsenbeschriftung""",
    data_type="VARCHAR",
    property_label="Label of X-Axis",
)


PlotXRange = PropertyTypeDef(
    code="PLOT_X_RANGE",
    description="""Range of X-axis//Bereich der X-Achse""",
    data_type="REAL",
    property_label="Range of X-Axis",
)


PlotXUnits = PropertyTypeDef(
    code="PLOT_X_UNITS",
    description="""Units of X-axis//X-Achse Einheiten""",
    data_type="VARCHAR",
    property_label="Units of X-Axis",
)


PlotYLabel = PropertyTypeDef(
    code="PLOT_Y_LABEL",
    description="""Label of Y-axis//Y-Achsenbeschriftung""",
    data_type="VARCHAR",
    property_label="Label of Y-Axis",
)


PlotYRange = PropertyTypeDef(
    code="PLOT_Y_RANGE",
    description="""Range of Y-axis//Bereich der Y-Achse""",
    data_type="REAL",
    property_label="Range of Y-Axis",
)


PlotYUnits = PropertyTypeDef(
    code="PLOT_Y_UNITS",
    description="""Units of Y-axis//Y-Achse Einheiten""",
    data_type="VARCHAR",
    property_label="Units of Y-Axis",
)


PlotZLabel = PropertyTypeDef(
    code="PLOT_Z_LABEL",
    description="""Label of Z-axis//Z-Achsenbeschriftung""",
    data_type="VARCHAR",
    property_label="Label of Z-Axis",
)


PlotZRange = PropertyTypeDef(
    code="PLOT_Z_RANGE",
    description="""Range of Z-axis//Bereich der Z-Achse""",
    data_type="REAL",
    property_label="Range of Z-Axis",
)


PlotZUnits = PropertyTypeDef(
    code="PLOT_Z_UNITS",
    description="""Units of Z-axis//Z-Achse Einheiten""",
    data_type="VARCHAR",
    property_label="Units of Z-Axis",
)


PositionerAxisCount = PropertyTypeDef(
    code="POSITIONER_AXIS_COUNT",
    description="""The number of controllable axis of the positioner (a value of 0 indicates static positioner)//""",
    data_type="INTEGER",
    property_label="Number of axis",
)


PositionerPayloadMax = PropertyTypeDef(
    code="POSITIONER_PAYLOAD_MAX",
    description="""The maximum payload to be handled by the positioner//Maximal zulässige Traglast""",
    data_type="REAL",
    property_label="Maximum payload [kg]",
)


PositionerType = PropertyTypeDef(
    code="POSITIONER_TYPE",
    description="""Positioner type//Art des Positionierers""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="POSITIONER_TYPE",
    property_label="Positioner type",
)


PowerInWatt = PropertyTypeDef(
    code="POWER_IN_WATT",
    description="""Power setting of the heating element in W//Eingestellte Erwärmungsleistung Leistung in W""",
    data_type="REAL",
    property_label="Power setting of the heating element [W]",
)


PrecisionMass = PropertyTypeDef(
    code="PRECISION_MASS",
    description="""Precision of the scale/measurement  (in UNIT_MASS)//Messgenauigkeit Waage/Messung  (in UNIT_MASS)""",
    data_type="REAL",
    property_label="Measurement precision//Messgenauigkeit",
)


Procedure = PropertyTypeDef(
    code="PROCEDURE",
    description="""Step-by-step procedure""",
    data_type="MULTILINE_VARCHAR",
    property_label="Procedure",
)


ProductionDate = PropertyTypeDef(
    code="PRODUCTION_DATE",
    description="""Production Date//Herstellungsdatum""",
    data_type="DATE",
    property_label="Production Date",
)


ProductCategory = PropertyTypeDef(
    code="PRODUCT_CATEGORY",
    description="""Product Category (corresponds to field `Product Category` in the Hazardous Materials Inventory (GSM) of BAM)//Produktkategorie (entspricht Feld `Verwendungstypen/Produktkategorie` aus dem Gefahrstoffmanagement (GSM) der BAM))""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="CHEMICAL_PRODUCT_CATEGORY",
    property_label="Product Category",
)


ProjectLeader = PropertyTypeDef(
    code="PROJECT_LEADER",
    description="""Project Leader: `Last name, first name`//Projektleitung: `Name, Vorname`""",
    data_type="VARCHAR",
    property_label="Project Leader",
)


ProjectLeaderBam = PropertyTypeDef(
    code="PROJECT_LEADER_BAM",
    description="""Project Leader at BAM//Projektleitung an der BAM""",
    data_type="OBJECT",
    object_code="PERSON.BAM",
    property_label="Project Leader",
)


ProjectStatus = PropertyTypeDef(
    code="PROJECT_STATUS",
    description="""Project Status//Projektstatus""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="PROJECT_STATUS",
    property_label="Project Status",
)


Propagation = PropertyTypeDef(
    code="PROPAGATION",
    description="""Crack Propagation during Step//Risserweiterung während des Versuchschrittes""",
    data_type="BOOLEAN",
    property_label="Crack Propagation during Step",
)


PseudopotFunc = PropertyTypeDef(
    code="PSEUDOPOT_FUNC",
    description="""Functional compatibility//Funktional-Kompatibilität""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="PSEUDOPOT_FUNCTIONAL",
    property_label="Functional Compatibility",
)


PseudopotSemicore = PropertyTypeDef(
    code="PSEUDOPOT_SEMICORE",
    description="""Semicore shells considered as valence//Halbkernschalen, die als Valenz betrachtet werden""",
    data_type="VARCHAR",
    property_label="Semicore Shells Considered as Valence",
)


PseudopotType = PropertyTypeDef(
    code="PSEUDOPOT_TYPE",
    description="""Type of pseudopotenial//Art des Pseudopotenials""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="PSEUDOPOT_TYPE",
    property_label="Type of Pseudopotenial",
)


Publication = PropertyTypeDef(
    code="PUBLICATION",
    description="""Own publication where this entity is referenced//Eigene Publikation, in dem dieses Experiment beschrieben wird""",
    data_type="MULTILINE_VARCHAR",
    property_label="Publication",
)


PulseEnergyInJoule = PropertyTypeDef(
    code="PULSE_ENERGY_IN_JOULE",
    description="""Pulse energy setting of the heating element in J //Eingetragene Erwärmungsenergie in J""",
    data_type="REAL",
    property_label="Pulse energy setting of the heating element [J]",
)


PurityInPercentage = PropertyTypeDef(
    code="PURITY_IN_PERCENTAGE",
    description="""Purity of the substance [ %]// Reinheit der Substanz""",
    data_type="REAL",
    property_label="Purity",
)


PyironHdf5Version = PropertyTypeDef(
    code="PYIRON_HDF5_VERSION",
    description="""pyiron HDF5 format version//pyiron HDF5 Format Version""",
    data_type="VARCHAR",
    property_label="pyiron HDF5 Version",
)


QueuingSystem = PropertyTypeDef(
    code="QUEUING_SYSTEM",
    description="""Queuing System used by HPC//Warteschlangensystem des HPCs""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="QUEUING_SYSTEM",
    property_label="Queuing System",
)


RatedFlow = PropertyTypeDef(
    code="RATED_FLOW",
    description="""Rated flow [l/min]//Nenndurchfluss [l/min]""",
    data_type="REAL",
    property_label="Rated Flow [l/min]",
)


RatedPower = PropertyTypeDef(
    code="RATED_POWER",
    description="""Rated power [kW]//Nennleistung [kW]""",
    data_type="REAL",
    property_label="Rated Power [kW]",
)


RawmatMechpropSupplierBreakelongation5Max = PropertyTypeDef(
    code="RAWMAT_MECHPROP_SUPPLIER_BREAKELONGATION_5_MAX",
    description="""Maximum Elongation at Break A5  [%]//Höchstwert Bruchdehnung A5 [%]""",
    data_type="REAL",
    property_label="Maximum Elongation at Break A5 [%]",
)


RawmatMechpropSupplierBreakelongation5Min = PropertyTypeDef(
    code="RAWMAT_MECHPROP_SUPPLIER_BREAKELONGATION_5_MIN",
    description="""Minimum Elongation at Break A5 [%]//Mindestwert Bruchdehnung A5 [%]""",
    data_type="REAL",
    property_label="Minimum Elongation at Break A5 [%]",
)


RawmatMechpropSupplierBreakelongation10Max = PropertyTypeDef(
    code="RAWMAT_MECHPROP_SUPPLIER_BREAKELONGATION_10_MAX",
    description="""Maximum Elongation at Break A10 [%]//Höchstwert Bruchdehnung A10 [%]""",
    data_type="REAL",
    property_label="Maximum Elongation at Break A10 [%]",
)


RawmatMechpropSupplierBreakelongation10Min = PropertyTypeDef(
    code="RAWMAT_MECHPROP_SUPPLIER_BREAKELONGATION_10_MIN",
    description="""Minimum Elongation at Break A10 [%]//Mindestwert Bruchdehnung A10 [%]""",
    data_type="REAL",
    property_label="Minimum Elongation at Break A10 [%]",
)


RawmatMechpropSupplierLoweryieldstrengthMax = PropertyTypeDef(
    code="RAWMAT_MECHPROP_SUPPLIER_LOWERYIELDSTRENGTH_MAX",
    description="""Maximum Lower Yield Strength R_el [MPa] //Höchstwert Untere Streckgrenze R_el [MPa]""",
    data_type="REAL",
    property_label="Maximum Lower Yield Strength R_el [MPa]",
)


RawmatMechpropSupplierLoweryieldstrengthMin = PropertyTypeDef(
    code="RAWMAT_MECHPROP_SUPPLIER_LOWERYIELDSTRENGTH_MIN",
    description="""Minimum Lower Yield Strength R_el [MPa] //Mindestwert Untere Streckgrenze R_el [MPa]""",
    data_type="REAL",
    property_label="Minimum Lower Yield Strength R_el [MPa]",
)


RawmatMechpropSupplierUniformelongationMax = PropertyTypeDef(
    code="RAWMAT_MECHPROP_SUPPLIER_UNIFORMELONGATION_MAX",
    description="""Maximum Uniform Elongation A_g [%]//Höchstwert Gleichmaßdehnung A_g [%]""",
    data_type="REAL",
    property_label="Maximum Uniform Elongation A_g [%]",
)


RawmatMechpropSupplierUniformelongationMin = PropertyTypeDef(
    code="RAWMAT_MECHPROP_SUPPLIER_UNIFORMELONGATION_MIN",
    description="""Minimum Uniform Elongation A_g [%]//Mindestwert Gleichmaßdehnung A_g [%]""",
    data_type="REAL",
    property_label="Minimum Uniform Elongation A_g [%]",
)


RawmatMechpropSupplierUpperyieldstrengthMax = PropertyTypeDef(
    code="RAWMAT_MECHPROP_SUPPLIER_UPPERYIELDSTRENGTH_MAX",
    description="""Maximum Upper Yield Strength R_eh [MPa] //Höchsttwert Obere Streckgrenze R_eh [MPa]""",
    data_type="REAL",
    property_label="Maximum Upper Yield Strength R_eh [MPa]",
)


RawmatMechpropSupplierUpperyieldstrengthMin = PropertyTypeDef(
    code="RAWMAT_MECHPROP_SUPPLIER_UPPERYIELDSTRENGTH_MIN",
    description="""Minimum Upper Yield Strength R_eh [MPa] //Mindestwert Obere Streckgrenze R_eh [MPa]""",
    data_type="REAL",
    property_label="Minimum Upper Yield Strength R_eh [MPa]",
)


RawmatMechpropSupplierUtsMax = PropertyTypeDef(
    code="RAWMAT_MECHPROP_SUPPLIER_UTS_MAX",
    description="""Maximum Ultimate Tensile Strength R_m [MPa]//Höchstwert Zugfestigkeit R_m [MPa]""",
    data_type="REAL",
    property_label="Maximum Ultimate Tensile Strength R_m [MPa]",
)


RawmatMechpropSupplierUtsMin = PropertyTypeDef(
    code="RAWMAT_MECHPROP_SUPPLIER_UTS_MIN",
    description="""Minimum Ultimate Tensile Strength R_m [MPa]//Mindestwert Zugfestigkeit R_m [MPa]""",
    data_type="REAL",
    property_label="Minimum Ultimate Tensile Strength R_m [MPa]",
)


RawmatMechpropSupplierYieldlimitMax = PropertyTypeDef(
    code="RAWMAT_MECHPROP_SUPPLIER_YIELDLIMIT_MAX",
    description="""Maximum Yield Limit R_p0,2 [MPa] //Höchstwert Dehngrenze R_p0,2 [MPa]""",
    data_type="REAL",
    property_label="Maximum Yield Limit R_p0,2 [MPa]",
)


RawmatMechpropSupplierYieldlimitMin = PropertyTypeDef(
    code="RAWMAT_MECHPROP_SUPPLIER_YIELDLIMIT_MIN",
    description="""Minimum Yield Limit R_p0,2 [MPa] //Mindestwert Dehngrenze R_p0,2 [MPa]""",
    data_type="REAL",
    property_label="Minimum Yield Limit R_p0,2 [MPa]",
)


RawmatMechpropSupplierYoungsmodulus = PropertyTypeDef(
    code="RAWMAT_MECHPROP_SUPPLIER_YOUNGSMODULUS",
    description="""Young`s Modulus [MPa]//Elastizitätsmodul [MPa]""",
    data_type="REAL",
    property_label="Young's Modulus [MPa]",
)


RawmatMechPropSupplierDensity = PropertyTypeDef(
    code="RAWMAT_MECH_PROP_SUPPLIER_DENSITY",
    description="""Density [kg/m^3]//Dichte [kg/m^3]""",
    data_type="REAL",
    property_label="Density [kg/m^3]",
)


RawMatAmountInStock = PropertyTypeDef(
    code="RAW_MAT_AMOUNT_IN_STOCK",
    description="""Amount in Stock [Pieces]//Anzahl auf Lager [Stück]""",
    data_type="INTEGER",
    property_label="Amount in Stock [Pieces]",
)


RawMatBatchNumber = PropertyTypeDef(
    code="RAW_MAT_BATCH_NUMBER",
    description="""Raw Material Batch Number//Chargennummer des Rohmaterials""",
    data_type="VARCHAR",
    property_label="Raw Material Batch Number",
)


RawMatComponentDescription = PropertyTypeDef(
    code="RAW_MAT_COMPONENT_DESCRIPTION",
    description="""Description of Component//Beschreibung der Komponente""",
    data_type="VARCHAR",
    property_label="Description of Component",
)


RawMatDiameter = PropertyTypeDef(
    code="RAW_MAT_DIAMETER",
    description="""Raw Material (outer) Diameter [mm]//(Außen-)durchmesser des Halbzeugs [mm]""",
    data_type="REAL",
    property_label="Raw Material (outer) Diameter [mm]",
)


RawMatForm = PropertyTypeDef(
    code="RAW_MAT_FORM",
    description="""Raw Material Form//Halbzeugart""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="RAW_MAT_FORM",
    property_label="Raw Material Form",
)


RawMatLength = PropertyTypeDef(
    code="RAW_MAT_LENGTH",
    description="""Length of Raw Material [mm]//Halbzeuglänge [mm]""",
    data_type="REAL",
    property_label="Length of Raw Material [mm]",
)


RawMatThickness = PropertyTypeDef(
    code="RAW_MAT_THICKNESS",
    description="""Thickness of Raw Material [mm]//Halbzeugdicke [mm]""",
    data_type="REAL",
    property_label="(Wall) Thickness of Raw Material [mm]",
)


RawMatWidth = PropertyTypeDef(
    code="RAW_MAT_WIDTH",
    description="""Width of Raw Material [mm]//Halbzeugbreite [mm]""",
    data_type="REAL",
    property_label="Width of Raw Material [mm]",
)


RazorDepth = PropertyTypeDef(
    code="RAZOR_DEPTH",
    description="""Notch Depth Increase according to Gauge [µm]//Kerbvertiefenzunahme nach Messuhr [µm]""",
    data_type="REAL",
    property_label="Notch Depth Increase according to Gauge [µm]",
)


RazorStrokecount = PropertyTypeDef(
    code="RAZOR_STROKECOUNT",
    description="""Stroke Count//Anzahl der Klingenhuebe""",
    data_type="REAL",
    property_label="Stroke Count",
)


RazorStrokelength = PropertyTypeDef(
    code="RAZOR_STROKELENGTH",
    description="""Stroke Length [mm]//Klingenhub [mm]""",
    data_type="REAL",
    property_label="Stroke Length [mm]",
)


RazorStrokespeed = PropertyTypeDef(
    code="RAZOR_STROKESPEED",
    description="""Stroke Speed [mm/s]//Hubgeschwindigkeit [mm/s]""",
    data_type="REAL",
    property_label="Stroke Speed [mm/s]",
)


Recipient = PropertyTypeDef(
    code="RECIPIENT",
    description="""Name of the recipient organism in which the genetic information is used to generate a GMO//Name des Empfängerorganismus, in dem die genetische Information für die Erzeugung eines GVO verwendet wird""",
    data_type="OBJECT",
    object_code="ORGANISM",
    property_label="Recipient Organism",
)


RecipientRiskGroup = PropertyTypeDef(
    code="RECIPIENT_RISK_GROUP",
    description="""Organism Risk Group Assignment//Risikogruppenzuordnung des Organismus""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="ORGANISM_RISK_GROUP",
    property_label="Recipient Organism Risk Group Assignment",
)


Reference = PropertyTypeDef(
    code="REFERENCE",
    description="""Useful refences//Nützliche Referenzen""",
    data_type="MULTILINE_VARCHAR",
    property_label="References",
)


ResearchBamProjectId = PropertyTypeDef(
    code="RESEARCH_BAM_PROJECT_ID",
    description="""ReSEARCH BAM ID//ReSEARCH BAM ID""",
    data_type="VARCHAR",
    property_label="ReSEARCH BAM ID",
)


ResponsiblePerson = PropertyTypeDef(
    code="RESPONSIBLE_PERSON",
    description="""Responsible person//Verantwortliche Person""",
    data_type="OBJECT",
    object_code="PERSON.BAM",
    property_label="Responsible person",
)


RobotAxisCount = PropertyTypeDef(
    code="ROBOT_AXIS_COUNT",
    description="""The number of a axis on the robot//Anzahl der Roboterachsen""",
    data_type="INTEGER",
    property_label="Number of robot axis",
)


RobotControllerAxisCount = PropertyTypeDef(
    code="ROBOT_CONTROLLER_AXIS_COUNT",
    description="""The number of robot axis the controller can operate//Anzahl der Roboterachsen die von der Steuerung angesteuert werden können""",
    data_type="INTEGER",
    property_label="Number of robot axis",
)


RobotControllerAxisCountExternal = PropertyTypeDef(
    code="ROBOT_CONTROLLER_AXIS_COUNT_EXTERNAL",
    description="""The number of external axis the controller can operate//Anzahl der zusätzlichen externen Achsen die von der Steuerung angesteuert werden können""",
    data_type="INTEGER",
    property_label="Number of external axis",
)


RobotPayloadMax = PropertyTypeDef(
    code="ROBOT_PAYLOAD_MAX",
    description="""The maximum allowable payload of the robot//Die maximal zulässig Traglast des Roboters""",
    data_type="INTEGER",
    property_label="Robot maximum payload [kg]",
)


RobotType = PropertyTypeDef(
    code="ROBOT_TYPE",
    description="""Type of Robot//Roboterart""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="ROBOT_TYPE",
    property_label="Type of Robot",
)


RobotWorkingRange = PropertyTypeDef(
    code="ROBOT_WORKING_RANGE",
    description="""The maximum specified working range of the robot (in mm)//Größe des maximal angegegebenen Arbeitsbereiches (in mm)""",
    data_type="REAL",
    property_label="Maximum working range [mm]",
)


Rs232 = PropertyTypeDef(
    code="RS232",
    description="""RS232 Interface//RS232 Schnittstelle""",
    data_type="BOOLEAN",
    property_label="RS232 Interface",
)


RtdAccuracyClass = PropertyTypeDef(
    code="RTD_ACCURACY_CLASS",
    description="""RTD Accuracy Class//Widerstandsthermometer Genauigkeitsklasse""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="RTD_ACCURACY_CLASS",
    property_label="RTD Accuracy Class",
)


RtdCableLength = PropertyTypeDef(
    code="RTD_CABLE_LENGTH",
    description="""RTD Cable Length [mm]//Widerstandsthermometer Kabellänge [mm]""",
    data_type="REAL",
    property_label="RTD Cable Length [mm]",
)


RtdConnection = PropertyTypeDef(
    code="RTD_CONNECTION",
    description="""RTD Connection//Widerstandsthermometer Anschlussart""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="RTD_CONNECTION_TYPE",
    property_label="RTD Connection",
)


RtdCoverTubeDiameter = PropertyTypeDef(
    code="RTD_COVER_TUBE_DIAMETER",
    description="""RTD Cover Tube Diameter [mm]//Widerstandsthermometer Schutzhülsendurchmesser [mm]""",
    data_type="REAL",
    property_label="RTD Cover Tube Diameter [mm]",
)


RtdCoverTubeLength = PropertyTypeDef(
    code="RTD_COVER_TUBE_LENGTH",
    description="""RTD Cover Tube Length [mm]//Widerstandsthermometer Schutzhülsenlänge [mm]""",
    data_type="REAL",
    property_label="RTD Cover Tube Length [mm]",
)


RtdInsulationMaterial = PropertyTypeDef(
    code="RTD_INSULATION_MATERIAL",
    description="""RTD Insulation Material//Widerstandsthermometer Isolationsmaterial""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="RTD_INSULATION_MATERIAL",
    property_label="RTD Insulation Material",
)


RtdMaxTemp = PropertyTypeDef(
    code="RTD_MAX_TEMP",
    description="""Maximum Operating Temperature [°C]//Maximale Betriebstemperatur [°C]""",
    data_type="REAL",
    property_label="Maximum Operating Temperature [°C]",
)


RtdMinTemp = PropertyTypeDef(
    code="RTD_MIN_TEMP",
    description="""Minimum Operating Temperature [°C]//Minimale Betriebstemperatur [°C]""",
    data_type="REAL",
    property_label="Minimum Operating Temperature [°C]",
)


RtdType = PropertyTypeDef(
    code="RTD_TYPE",
    description="""RTD Type//Widerstandsthermometer Typ""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="RTD_TYPE",
    property_label="RTD Type",
)


SampleAnalyte = PropertyTypeDef(
    code="SAMPLE_ANALYTE",
    description="""Name/ID of sought-after substance//Name/Kürzel der gesuchten Substanz""",
    data_type="VARCHAR",
    property_label="Analyte",
)


SampleConsumed = PropertyTypeDef(
    code="SAMPLE_CONSUMED",
    description="""Leftover sample or material//Restliche(s) Probe oder Material""",
    data_type="BOOLEAN",
    property_label="Leftover sample",
)


SampleHolderMaterial = PropertyTypeDef(
    code="SAMPLE_HOLDER_MATERIAL",
    description="""Material of the sample holder//Material des Probenbehälters""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="SAMPLE_HOLDER_MATERIAL",
    property_label="Holder Material",
)


SampleHolderThicknessInMm = PropertyTypeDef(
    code="SAMPLE_HOLDER_THICKNESS_IN_MM",
    description="""Sample Container Wall Thickness in mm//Wandstärke des Probenbehälters in mm""",
    data_type="REAL",
    property_label="Thickness effective [mm]",
)


SampleId = PropertyTypeDef(
    code="SAMPLE_ID",
    description="""Sample ID//Identifikationsnummer""",
    data_type="VARCHAR",
    property_label="Sample ID",
)


SampleIdNumber = PropertyTypeDef(
    code="SAMPLE_ID_NUMBER",
    description="""Sample number//Probennummer""",
    data_type="INTEGER",
    property_label="Sample Number",
)


SampleLocation = PropertyTypeDef(
    code="SAMPLE_LOCATION",
    description="""Location of retained samples (if any?)//Standort von Rückstellproben (wenn existent?)""",
    data_type="VARCHAR",
    property_label="Retained samples",
)


SampleMatrix = PropertyTypeDef(
    code="SAMPLE_MATRIX",
    description="""Extra Informaton about samples//Zusätzliche Information zu den Proben""",
    data_type="MULTILINE_VARCHAR",
    property_label="Sample matrix",
)


SampleName = PropertyTypeDef(
    code="SAMPLE_NAME",
    description="""What is the label on the Sample//Probenbezeichnung""",
    data_type="VARCHAR",
    property_label="Sample name",
)


SampleProvider = PropertyTypeDef(
    code="SAMPLE_PROVIDER",
    description="""Who is the provider of the Sample?//Wer hat die Probe erzeugt/geliefert?""",
    data_type="VARCHAR",
    property_label="Sample source",
)


SampleReceived = PropertyTypeDef(
    code="SAMPLE_RECEIVED",
    description="""Date when samples arrived//Eingangsdatum der Proben""",
    data_type="TIMESTAMP",
    property_label="Date of receipt",
)


SampleTreatment = PropertyTypeDef(
    code="SAMPLE_TREATMENT",
    description="""Sample treatment//Oberflächenzustand des Sample""",
    data_type="MULTILINE_VARCHAR",
    property_label="Sample treatment",
)


ScanLineCount = PropertyTypeDef(
    code="SCAN_LINE_COUNT",
    description="""Number of individual scan lines recorded//Anzahl der aufgenommenen Scanlinien""",
    data_type="INTEGER",
    property_label="Scan line count",
)


ScanLineResolution = PropertyTypeDef(
    code="SCAN_LINE_RESOLUTION",
    description="""Number of pixels recorded for each scan line//Anzahl der Messpunkt einer Scanlinie""",
    data_type="INTEGER",
    property_label="Scan line resolution [pixel]",
)


SerialNumber = PropertyTypeDef(
    code="SERIAL_NUMBER",
    description="""Serial Number//Seriennummer""",
    data_type="VARCHAR",
    property_label="Serial Number",
)


SetupConfiguration = PropertyTypeDef(
    code="SETUP_CONFIGURATION",
    description="""Setup configuration//Messanordnung""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="THERMOGRAPHIC_SETUP_CONFIG",
    property_label="Setup configuration",
)


SftwCompatibility = PropertyTypeDef(
    code="SFTW_COMPATIBILITY",
    description="""Software which can use this file//Software, die diese Datei verwenden kann""",
    data_type="VARCHAR",
    property_label="Software Compatibility",
)


SimCellAnglesInDeg = PropertyTypeDef(
    code="SIM_CELL_ANGLES_IN_DEG",
    description="""Simulation cell angles [Degrees]//Winkel der Simulationszelle [Grad]""",
    data_type="VARCHAR",
    property_label="Simulation Cell Angles [Degrees]",
)


SimCellLengthsInA = PropertyTypeDef(
    code="SIM_CELL_LENGTHS_IN_A",
    description="""Simulation cell lengths [Å]//Längen der Simulationszelle [Å]""",
    data_type="VARCHAR",
    property_label="Simulation Cell Lengths [Å]",
)


SimCellVectors = PropertyTypeDef(
    code="SIM_CELL_VECTORS",
    description="""Simulation cell vectors//Vektoren der Simulationszelle""",
    data_type="VARCHAR",
    property_label="Simulation Cell Vectors",
)


SimCellVolumeInA3 = PropertyTypeDef(
    code="SIM_CELL_VOLUME_IN_A3",
    description="""Simulation cell volume [Å^3]//Volumen der Simulationszelle [Å^3]""",
    data_type="REAL",
    property_label="Simulation Cell Volume [Å^3]",
)


SimCoretimeInHours = PropertyTypeDef(
    code="SIM_CORETIME_IN_HOURS",
    description="""Total core hours used [hr]//Gesamtkernstundenzeit des Jobs [Stunden]""",
    data_type="REAL",
    property_label="Total Job Core Time [hr]",
)


SimJobFinished = PropertyTypeDef(
    code="SIM_JOB_FINISHED",
    description="""Finished = True, Aborted or incomplete = False//Beendet = Wahr, Abgebrochen oder unvollständig = Falsch""",
    data_type="BOOLEAN",
    property_label="Is the job finished?",
)


SimVisCbar = PropertyTypeDef(
    code="SIM_VIS_CBAR",
    description="""Colour bar?//Farbskala""",
    data_type="BOOLEAN",
    property_label="Colour Bar?",
)


SimVisCbarMax = PropertyTypeDef(
    code="SIM_VIS_CBAR_MAX",
    description="""Colour bar max. range//Farbskala max. Bereich""",
    data_type="REAL",
    property_label="Colour Bar Max. Range",
)


SimVisCbarMin = PropertyTypeDef(
    code="SIM_VIS_CBAR_MIN",
    description="""Colour bar min. range//Farbskala min. Bereich""",
    data_type="REAL",
    property_label="Colour bar Min. Range",
)


SimVisCbarProp = PropertyTypeDef(
    code="SIM_VIS_CBAR_PROP",
    description="""Property visualized by colour bar//Eigenschaft visualisiert durch Farbskala""",
    data_type="VARCHAR",
    property_label="Colour Bar Property",
)


SimVisCbarUnits = PropertyTypeDef(
    code="SIM_VIS_CBAR_UNITS",
    description="""Colour bar units//Farbskaleneinheiten""",
    data_type="VARCHAR",
    property_label="Colour Bar Units",
)


SimVisCoord = PropertyTypeDef(
    code="SIM_VIS_COORD",
    description="""Coordinate tripod//Koordinatensystem""",
    data_type="BOOLEAN",
    property_label="Coordinate Tripod?",
)


SimVisCoordX = PropertyTypeDef(
    code="SIM_VIS_COORD_X",
    description="""Coordinate index X//Koordinatenindex X""",
    data_type="VARCHAR",
    property_label="Coordinate Index X",
)


SimVisCoordY = PropertyTypeDef(
    code="SIM_VIS_COORD_Y",
    description="""Coordinate index Y//Koordinatenindex Y""",
    data_type="VARCHAR",
    property_label="Coordinate Index Y",
)


SimVisCoordZ = PropertyTypeDef(
    code="SIM_VIS_COORD_Z",
    description="""Coordinate index Z//Koordinatenindex Z""",
    data_type="VARCHAR",
    property_label="Coordinate Index Z",
)


SimVisScbar = PropertyTypeDef(
    code="SIM_VIS_SCBAR",
    description="""Scale bar?//Maßstabsbalken""",
    data_type="BOOLEAN",
    property_label="Scale Bar?",
)


SimVisScbarUnits = PropertyTypeDef(
    code="SIM_VIS_SCBAR_UNITS",
    description="""Scale units//Maßeinheiten""",
    data_type="VARCHAR",
    property_label="Scale Units",
)


SimWalltimeInHours = PropertyTypeDef(
    code="SIM_WALLTIME_IN_HOURS",
    description="""Total job run time [hr]//Gesamtlaufzeit des Jobs [Stunden]""",
    data_type="REAL",
    property_label="Job Run Time (Walltime) [hr]",
)


SizeEffectiveMm = PropertyTypeDef(
    code="SIZE_EFFECTIVE_MM",
    description="""Instrument specific relevant size in mm//Instrumentspezifische relevante Größe in mm""",
    data_type="REAL",
    property_label="Effective Dimension [mm]",
)


SizeHeightInMillimeter = PropertyTypeDef(
    code="SIZE_HEIGHT_IN_MILLIMETER",
    description="""Height in mm//Höhe in mm""",
    data_type="REAL",
    property_label="Height [mm]",
)


SizeThicknessInMillimeter = PropertyTypeDef(
    code="SIZE_THICKNESS_IN_MILLIMETER",
    description="""Thickness in mm//Dicke in mm""",
    data_type="REAL",
    property_label="Thickness [mm]",
)


SizeWidthInMillimeter = PropertyTypeDef(
    code="SIZE_WIDTH_IN_MILLIMETER",
    description="""Width in mm//Breite in mm""",
    data_type="REAL",
    property_label="Width [mm]",
)


SoftwareName = PropertyTypeDef(
    code="SOFTWARE_NAME",
    description="""Software name//Software-Name""",
    data_type="VARCHAR",
    property_label="Software Name",
)


SourceCodeLanguage = PropertyTypeDef(
    code="SOURCE_CODE_LANGUAGE",
    description="""Programming Language(s) used//Verwendete Programmiersprache(n)""",
    data_type="VARCHAR",
    property_label="Programming Language(s) Used",
)


SourceLink = PropertyTypeDef(
    code="SOURCE_LINK",
    description="""Source/Download//Quelle/Herunterladen""",
    data_type="MULTILINE_VARCHAR",
    property_label="Source for download",
)


SpaceGroup = PropertyTypeDef(
    code="SPACE_GROUP",
    description="""Space group//Raumgruppe""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="SPACE_GROUP",
    property_label="Space Group",
)


SpectrometerType = PropertyTypeDef(
    code="SPECTROMETER_TYPE",
    description="""Type of spectrometer//Spektrometertyp""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="OPTICAL_SPECTROMETER_TYPE",
    property_label="Spectrometer Type",
)


SpecFcgNotchlengthMiddle = PropertyTypeDef(
    code="SPEC_FCG_NOTCHLENGTH_MIDDLE",
    description="""Specimen Notch Length a_n [mm] (Middle, Chevron Notch only)//Kerbtiefe a_n [mm] (Mitte, nur Chevron-Kerbe)""",
    data_type="REAL",
    property_label="Notch Length a_n [mm] (Middle, Chevron Notch only)",
)


SpecFcgNotchlengthSide1 = PropertyTypeDef(
    code="SPEC_FCG_NOTCHLENGTH_SIDE1",
    description="""Specimen Notch Length a_n [mm] (Side 1)//Kerbtiefe a_n [mm] (Seite 1)""",
    data_type="REAL",
    property_label="Notch Length a_n [mm] (Side 1)",
)


SpecFcgNotchlengthSide2 = PropertyTypeDef(
    code="SPEC_FCG_NOTCHLENGTH_SIDE2",
    description="""Specimen Notch Length a_n [mm] (Side 2)//Kerbtiefe a_n [mm] (Seite 2)""",
    data_type="REAL",
    property_label="Notch Length a_n [mm] (Side 2)",
)


SpecFcgNotchtype = PropertyTypeDef(
    code="SPEC_FCG_NOTCHTYPE",
    description="""Notch Type//Kerbtyp""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="NOTCH_TYPE_FCG",
    property_label="Notch Type",
)


SpecFcgThickness = PropertyTypeDef(
    code="SPEC_FCG_THICKNESS",
    description="""Specimen Thickness B [mm]//Probendicke B [mm]""",
    data_type="REAL",
    property_label="Thickness B [mm]",
)


SpecFcgType = PropertyTypeDef(
    code="SPEC_FCG_TYPE",
    description="""Fatigue Crack Growth Specimen Type//Ermüdungsrisswachstums-Probentyp""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="SPECIMEN_TYPE_FCG_TEST",
    property_label="Fatigue Crack Growth Specimen Type",
)


SpecFcgWidthSide1 = PropertyTypeDef(
    code="SPEC_FCG_WIDTH_SIDE1",
    description="""Specimen Width W [mm] (Side 1)//Probenbreite W [mm] (Seite 1)""",
    data_type="REAL",
    property_label="Width W [mm] (Side 1)",
)


SpecFcgWidthSide2 = PropertyTypeDef(
    code="SPEC_FCG_WIDTH_SIDE2",
    description="""Specimen Width W [mm] (Side 2)//Probenbreite W [mm] (Seite 2)""",
    data_type="REAL",
    property_label="Width W [mm] (Side 2)",
)


SpecStatus = PropertyTypeDef(
    code="SPEC_STATUS",
    description="""Specimen Status//Probenstatus""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="SPECIMEN_STATUS",
    property_label="Specimen Status",
)


StartDate = PropertyTypeDef(
    code="START_DATE",
    description="""Start date//Startdatum""",
    data_type="TIMESTAMP",
    property_label="Start date",
)


StateCheck = PropertyTypeDef(
    code="STATE_CHECK",
    description="""TRUE if task needs to be done//WAHR wenn die Aufgabe getan werden muss""",
    data_type="BOOLEAN",
    property_label="Needs to be checked?",
)


SteelTreatmentFirst = PropertyTypeDef(
    code="STEEL_TREATMENT_FIRST",
    description="""First Treatment//Erste Behandlung""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="RAW_MAT_TREATMENT_STEEL",
    property_label="First Treatment",
)


SteelTreatmentFourth = PropertyTypeDef(
    code="STEEL_TREATMENT_FOURTH",
    description="""Fourth Treatment//Vierte Behandlung""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="RAW_MAT_TREATMENT_STEEL",
    property_label="Fourth Treatment",
)


SteelTreatmentSecond = PropertyTypeDef(
    code="STEEL_TREATMENT_SECOND",
    description="""Second Treatment//Zweite Behandlung""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="RAW_MAT_TREATMENT_STEEL",
    property_label="Second Treatment",
)


SteelTreatmentThird = PropertyTypeDef(
    code="STEEL_TREATMENT_THIRD",
    description="""Third Treatment//Dritte Behandlung""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="RAW_MAT_TREATMENT_STEEL",
    property_label="Third Treatment",
)


StepNo = PropertyTypeDef(
    code="STEP_NO",
    description="""Step Number//Schrittnummer""",
    data_type="INTEGER",
    property_label="Step No.",
)


Subframe = PropertyTypeDef(
    code="SUBFRAME",
    description="""Subframe setting//Einstellung Subframe""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="SUBFRAME_TYPE",
    property_label="Subframe type",
)


SubstanceEmpty = PropertyTypeDef(
    code="SUBSTANCE_EMPTY",
    description="""Is the substance used up?//Ist die Substanz aufgebraucht?""",
    data_type="BOOLEAN",
    property_label="Empty",
)


SunIrradianceInWattPerMeterSquared = PropertyTypeDef(
    code="SUN_IRRADIANCE_IN_WATT_PER_METER_SQUARED",
    description="""Sun irradiance in W/m^2//Sonneneinstrahlung in W/m^2""",
    data_type="REAL",
    property_label="Sun irradiance [W/m^2]",
)


Supplier = PropertyTypeDef(
    code="SUPPLIER",
    description="""Supplier//Lieferant""",
    data_type="VARCHAR",
    property_label="Supplier",
)


SwCompatibility = PropertyTypeDef(
    code="SW_COMPATIBILITY",
    description="""Software which can use this file//Software, die diese Datei verwenden kann""",
    data_type="VARCHAR",
    property_label="Software Compatibility",
)


TcCableLength = PropertyTypeDef(
    code="TC_CABLE_LENGTH",
    description="""Cable Length [mm]//Kabellänge [mm]""",
    data_type="REAL",
    property_label="Cable Length [mm]",
)


TcConnector = PropertyTypeDef(
    code="TC_CONNECTOR",
    description="""Connector//Stecker""",
    data_type="BOOLEAN",
    property_label="Connector",
)


TcDiameter = PropertyTypeDef(
    code="TC_DIAMETER",
    description="""Diameter [mm]//Durchmesser [mm]""",
    data_type="REAL",
    property_label="Diameter [mm]",
)


TcMaxTemp = PropertyTypeDef(
    code="TC_MAX_TEMP",
    description="""Maximum Operating Temperature [°C]//Maximale Betriebstemperatur [°C]""",
    data_type="REAL",
    property_label="Maximum Operating Temperature [°C]",
)


TcMinTemp = PropertyTypeDef(
    code="TC_MIN_TEMP",
    description="""Minimum Operating Temperature [°C]//Minimale Betriebstemperatur [°C]""",
    data_type="REAL",
    property_label="Minimum Operating Temperature [°C]",
)


TcType = PropertyTypeDef(
    code="TC_TYPE",
    description="""Thermocouple Type//Thermoelement Typ""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="THERMOCOUPLE_TYPE",
    property_label="Thermocouple Type",
)


TechnikumMaterialAmount = PropertyTypeDef(
    code="TECHNIKUM_MATERIAL_AMOUNT",
    description="""Mass or amount of material (potentially measured in non-SI units)//Materialmenge (ggf. in nicht SI-konformen Einheiten)""",
    data_type="VARCHAR",
    property_label="Material amount",
)


TechnikumMaterialUsage = PropertyTypeDef(
    code="TECHNIKUM_MATERIAL_USAGE",
    description="""Potential material usage//Möglicher Verwendungszweck des Materials""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="MATERIAL_USAGE_TECHNIKUM",
    property_label="Material usage",
)


TechnikumSubstanceConcentration = PropertyTypeDef(
    code="TECHNIKUM_SUBSTANCE_CONCENTRATION",
    description="""Concentration (in mg/kg) of sought-after substance//Konzentration(in mg/kg) des zu bestimmenden Stoffes""",
    data_type="REAL",
    property_label="Analyte concentration [mg/kg]",
)


Telephone = PropertyTypeDef(
    code="TELEPHONE",
    description="""Telephone number//Telefonnummer""",
    data_type="VARCHAR",
    property_label="Telephone number",
)


TemporalHeatingStructure = PropertyTypeDef(
    code="TEMPORAL_HEATING_STRUCTURE",
    description="""Temporal Structure of the heating//Zeitliche Struktur der Erwärmung""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="TEMPORAL_HEATING_STRUCTURE",
    property_label="Temporal Structure of the heating",
)


TempMaxCelsius = PropertyTypeDef(
    code="TEMP_MAX_CELSIUS",
    description="""Maximum Temperature [°C]//Maximaltemperatur [°C]""",
    data_type="REAL",
    property_label="Temperature Maximum [°C]",
)


TempMinCelsius = PropertyTypeDef(
    code="TEMP_MIN_CELSIUS",
    description="""Minimum Temperature [°C]//Minimaltemperatur [°C]""",
    data_type="REAL",
    property_label="Temperature Minimum [°C]",
)


TestingMachineDriveType = PropertyTypeDef(
    code="TESTING_MACHINE_DRIVE_TYPE",
    description="""Drive Type//Antriebsart""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="TESTING_MACHINE_DRIVE_TYPE",
    property_label="Drive Type",
)


TestingMachineLoadType = PropertyTypeDef(
    code="TESTING_MACHINE_LOAD_TYPE",
    description="""Load type//Belastungsart""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="TESTING_MACHINE_LOAD_TYPE",
    property_label="Load Type",
)


TestObjHeight = PropertyTypeDef(
    code="TEST_OBJ_HEIGHT",
    description="""Test Object Height [mm]//Höhe des Prüfkörpers [mm]""",
    data_type="INTEGER",
    property_label="Test Object Height [mm]",
)


TestObjLength = PropertyTypeDef(
    code="TEST_OBJ_LENGTH",
    description="""Test Object Length [mm]//Länge des Prüfkörpers [mm]""",
    data_type="INTEGER",
    property_label="Test Object Length [mm]",
)


TestObjMaterial = PropertyTypeDef(
    code="TEST_OBJ_MATERIAL",
    description="""Building Material//Werkstoff""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="BUILDING_MATERIAL_TYPE",
    property_label="Building Material",
)


TestObjStatus = PropertyTypeDef(
    code="TEST_OBJ_STATUS",
    description="""Test Object Status//Prüfkörperstatus""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="TEST_OBJECT_STATUS",
    property_label="Test Object Status",
)


TestObjWidth = PropertyTypeDef(
    code="TEST_OBJ_WIDTH",
    description="""Test Object Width [mm]//Breite des Prüfkörpers [mm]""",
    data_type="INTEGER",
    property_label="Test Object Width [mm]",
)


TestSetupType = PropertyTypeDef(
    code="TEST_SETUP_TYPE",
    description="""Test Setup Type//Test Setup Typ""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="TEST_SETUP_TYPE",
    property_label="Test Setup Type",
)


TestType = PropertyTypeDef(
    code="TEST_TYPE",
    description="""Test Type//Art des Versuchs""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="TEST_PROGRAM_TYPE",
    property_label="Test Type",
)


ThicknessInMillimeter = PropertyTypeDef(
    code="THICKNESS_IN_MILLIMETER",
    description="""Thickness of the spacer in mm//Dicke des Abstandsringes in mm""",
    data_type="REAL",
    property_label="Thickness [mm]",
)


TrainedPerson = PropertyTypeDef(
    code="TRAINED_PERSON",
    description="""Trained Person//Eingewiesene Person""",
    data_type="OBJECT",
    object_code="PERSON.BAM",
    property_label="Trained Person",
)


UnitMass = PropertyTypeDef(
    code="UNIT_MASS",
    description="""Mass unit//Masseeinheit""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="UNIT_MASS",
    property_label="Mass unit//Masseeinheit",
)


Usb = PropertyTypeDef(
    code="USB",
    description="""USB Interface//USB Schnittstelle""",
    data_type="BOOLEAN",
    property_label="USB Interface",
)


UsedCalibrationRangeMaxInCelsius = PropertyTypeDef(
    code="USED_CALIBRATION_RANGE_MAX_IN_CELSIUS",
    description="""Upper limit of utilized calibration range in °C//Oberes Limit des genutzten Kalibrierbereichs in °C""",
    data_type="REAL",
    property_label="Upper limit of utilized calibration range [°C]",
)


UsedCalibrationRangeMinInCelsius = PropertyTypeDef(
    code="USED_CALIBRATION_RANGE_MIN_IN_CELSIUS",
    description="""Lower limit of utilized calibration range in °C//Unteres Limit des genutzten Kalibrierbereichs in °C""",
    data_type="REAL",
    property_label="Lower limit of utilized calibration range [°C]",
)


Uuid = PropertyTypeDef(
    code="UUID",
    description="""A Universally Unique IDentifier (UUID/GUID) according to RFC 4122//Ein Universally Unique IDentifier (UUID/GUID) nach RFC 4122""",
    data_type="VARCHAR",
    property_label="UUID",
)


ValveModelId = PropertyTypeDef(
    code="VALVE_MODEL_ID",
    description="""Valve Model Code as specified by Manufacturer//Modellbezeichnung des Herstellers für das Servoventil""",
    data_type="VARCHAR",
    property_label="Model",
)


ValveTypeId = PropertyTypeDef(
    code="VALVE_TYPE_ID",
    description="""Valve Type Code as specified by Manufacturer//Typenbezeichnung des Herstellers für das Servoventil""",
    data_type="VARCHAR",
    property_label="Type",
)


Vector = PropertyTypeDef(
    code="VECTOR",
    description="""A plasmid used as a biological carrier to introduce nucleic acid segments into a new cell//Ein Plasmid, das als biologischer Träger verwendet wird, um Nukleinsäuresegmente in eine neue Zelle einzubringen""",
    data_type="OBJECT",
    object_code="SAMPLE.PLASMID",
    property_label="Vector name",
)


Version = PropertyTypeDef(
    code="VERSION",
    description="""Version""",
    data_type="VARCHAR",
    property_label="Version",
)


VideoCodec = PropertyTypeDef(
    code="VIDEO_CODEC",
    description="""Video codec used during recording (if applicable)//Videocodec (sofern kodiert)""",
    data_type="VARCHAR",
    property_label="Video codec used during recording",
)


VideoDynamicFramerate = PropertyTypeDef(
    code="VIDEO_DYNAMIC_FRAMERATE",
    description="""Flag to indicate that the video frame rate varies over time//Gibt an, dass die Bildrate des Videos nicht konstant ist""",
    data_type="BOOLEAN",
    property_label="Dynamic video frame rate",
)


VideoFramePerSeconds = PropertyTypeDef(
    code="VIDEO_FRAME_PER_SECONDS",
    description="""Average video framerate [frames per second]//Mittlere Bildrate (in Bilder pro Sekunde)""",
    data_type="INTEGER",
    property_label="Average video framerate [frames per second]",
)


VolumeMaxInMl = PropertyTypeDef(
    code="VOLUME_MAX_IN_ML",
    description="""Maximum volume in mililiter/Maximales Volumen in Milliliter""",
    data_type="REAL",
    property_label="Maximum volume",
)


VolumeMinInMl = PropertyTypeDef(
    code="VOLUME_MIN_IN_ML",
    description="""Minimum volume in mililiter//Mindestvolumen in Milliliter""",
    data_type="REAL",
    property_label="Minimum volume",
)


VolumePercentArgon = PropertyTypeDef(
    code="VOLUME_PERCENT_ARGON",
    description="""Volume percent of Argon//Volumenanteil von Argon""",
    data_type="REAL",
    property_label="Ar",
)


VolumePercentCarbonDioxide = PropertyTypeDef(
    code="VOLUME_PERCENT_CARBON_DIOXIDE",
    description="""Volume percent of CO2//Volumenanteil von CO2""",
    data_type="REAL",
    property_label="CO2",
)


VolumePercentHelium = PropertyTypeDef(
    code="VOLUME_PERCENT_HELIUM",
    description="""Volume percent of Helium//Volumenanteil von Helium""",
    data_type="REAL",
    property_label="He",
)


VolumePercentHydrogen = PropertyTypeDef(
    code="VOLUME_PERCENT_HYDROGEN",
    description="""Volume percent of hydrogen//Volumenanteil von Wasserstoff""",
    data_type="REAL",
    property_label="H2",
)


VolumePercentNitrogen = PropertyTypeDef(
    code="VOLUME_PERCENT_NITROGEN",
    description="""Volume percent of Nitrogen//Volumenanteil von Stickstoff""",
    data_type="REAL",
    property_label="N2",
)


VolumePercentOxygen = PropertyTypeDef(
    code="VOLUME_PERCENT_OXYGEN",
    description="""Volume percent of Oxygen//Volumenanteil von Sauerstoff""",
    data_type="REAL",
    property_label="O2",
)


WeatherCondition = PropertyTypeDef(
    code="WEATHER_CONDITION",
    description="""Weather//Wetter""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="WEATHER_CONDITION",
    property_label="Weather",
)


WeightMax = PropertyTypeDef(
    code="WEIGHT_MAX",
    description="""Maximum weight (in UNIT_MASS)//Maximales Gewicht (in UNIT_MASS)""",
    data_type="REAL",
    property_label="Maximum weight",
)


WeightMin = PropertyTypeDef(
    code="WEIGHT_MIN",
    description="""Minimum weight (in UNIT_MASS)//Minimales Gewicht (in UNIT_MASS)""",
    data_type="REAL",
    property_label="Minimum weight",
)


WindDirection = PropertyTypeDef(
    code="WIND_DIRECTION",
    description="""Wind direction//Windrichtung""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="WIND_DIRECTION",
    property_label="Wind direction",
)


WindSpeedInMeterPerSecond = PropertyTypeDef(
    code="WIND_SPEED_IN_METER_PER_SECOND",
    description="""Wind speed in m/s//Windgeschwindigkeit in m/s""",
    data_type="REAL",
    property_label="Wind speed [m/s]",
)


WorkflowManager = PropertyTypeDef(
    code="WORKFLOW_MANAGER",
    description="""Workflow manager//Workflow-Manager""",
    data_type="VARCHAR",
    property_label="Workflow Manager",
)


AdditionalInformation = PropertyTypeDef(
    code="$ORDER.ADDITIONAL_INFORMATION",
    description="""Additional Information""",
    data_type="VARCHAR",
    property_label="Additional Information",
)


BillTo = PropertyTypeDef(
    code="$ORDER.BILL_TO",
    description="""Bill To""",
    data_type="VARCHAR",
    property_label="Bill To",
)


ContactFax = PropertyTypeDef(
    code="$ORDER.CONTACT_FAX",
    description="""Fax""",
    data_type="VARCHAR",
    property_label="Fax",
)


ContactPhone = PropertyTypeDef(
    code="$ORDER.CONTACT_PHONE",
    description="""Phone""",
    data_type="VARCHAR",
    property_label="Phone",
)


OrderState = PropertyTypeDef(
    code="$ORDER.ORDER_STATE",
    description="""Order State""",
    data_type="VARCHAR",
    property_label="Order State",
)


ShipAddress = PropertyTypeDef(
    code="$ORDER.SHIP_ADDRESS",
    description="""Ship Address""",
    data_type="VARCHAR",
    property_label="Ship Address",
)


ShipTo = PropertyTypeDef(
    code="$ORDER.SHIP_TO",
    description="""Ship To""",
    data_type="VARCHAR",
    property_label="Ship To",
)


OrderStatus = PropertyTypeDef(
    code="$ORDERING.ORDER_STATUS",
    description="""Order Status""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="$ORDER.ORDER_STATUS",
    property_label="Order Status",
)


CatalogNum = PropertyTypeDef(
    code="$PRODUCT.CATALOG_NUM",
    description="""Catalog Number""",
    data_type="VARCHAR",
    property_label="Catalog Number",
)


Currency = PropertyTypeDef(
    code="$PRODUCT.CURRENCY",
    description="""Currency""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="$PRODUCT.CURRENCY",
    property_label="Currency",
)


PricePerUnit = PropertyTypeDef(
    code="$PRODUCT.PRICE_PER_UNIT",
    description="""Estimated Price""",
    data_type="REAL",
    property_label="Estimated Price",
)


Description = PropertyTypeDef(
    code="$PUBLICATION.DESCRIPTION",
    description="""Description""",
    data_type="VARCHAR",
    property_label="Description",
)


Identifier = PropertyTypeDef(
    code="$PUBLICATION.IDENTIFIER",
    description="""Identifier""",
    data_type="VARCHAR",
    property_label="Identifier",
)


OpenbisRelatedIdentifiers = PropertyTypeDef(
    code="$PUBLICATION.OPENBIS_RELATED_IDENTIFIERS",
    description="""openBIS Related Identifiers""",
    data_type="VARCHAR",
    property_label="openBIS Related Identifiers",
)


Organization = PropertyTypeDef(
    code="$PUBLICATION.ORGANIZATION",
    description="""Organization""",
    data_type="VARCHAR",
    property_label="Organization",
)


Type = PropertyTypeDef(
    code="$PUBLICATION.TYPE",
    description="""Type""",
    data_type="VARCHAR",
    property_label="Type",
)


Url = PropertyTypeDef(
    code="$PUBLICATION.URL",
    description="""URL""",
    data_type="HYPERLINK",
    property_label="URL",
)


CustomData = PropertyTypeDef(
    code="$SEARCH_QUERY.CUSTOM_DATA",
    description="""Additional data in custom format""",
    data_type="XML",
    property_label="Custom data",
)


FetchOptions = PropertyTypeDef(
    code="$SEARCH_QUERY.FETCH_OPTIONS",
    description="""V3 API fetch options""",
    data_type="XML",
    property_label="Fetch options",
)


SearchCriteria = PropertyTypeDef(
    code="$SEARCH_QUERY.SEARCH_CRITERIA",
    description="""V3 API search criteria""",
    data_type="XML",
    property_label="Search criteria",
)


BoxNum = PropertyTypeDef(
    code="$STORAGE.BOX_NUM",
    description="""Allowed number of Boxes in a rack""",
    data_type="INTEGER",
    property_label="Number of Boxes",
)


BoxSpaceWarning = PropertyTypeDef(
    code="$STORAGE.BOX_SPACE_WARNING",
    description="""Number between 0 and 99, represents a percentage""",
    data_type="INTEGER",
    property_label="Box Space Warning",
)


ColumnNum = PropertyTypeDef(
    code="$STORAGE.COLUMN_NUM",
    description="""Number of Columns""",
    data_type="INTEGER",
    property_label="Number of Columns",
)


RowNum = PropertyTypeDef(
    code="$STORAGE.ROW_NUM",
    description="""Number of Rows""",
    data_type="INTEGER",
    property_label="Number of Rows",
)


StorageSpaceWarning = PropertyTypeDef(
    code="$STORAGE.STORAGE_SPACE_WARNING",
    description="""Number between 0 and 99, represents a percentage""",
    data_type="INTEGER",
    property_label="Rack Space Warning",
)


StorageValidationLevel = PropertyTypeDef(
    code="$STORAGE.STORAGE_VALIDATION_LEVEL",
    description="""Validation level""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="$STORAGE.STORAGE_VALIDATION_LEVEL",
    property_label="Validation level",
)


StorageBoxName = PropertyTypeDef(
    code="$STORAGE_POSITION.STORAGE_BOX_NAME",
    description="""Box Name""",
    data_type="VARCHAR",
    property_label="Storage Box Name",
)


StorageBoxPosition = PropertyTypeDef(
    code="$STORAGE_POSITION.STORAGE_BOX_POSITION",
    description="""Box Position""",
    data_type="VARCHAR",
    property_label="Storage Box Position",
)


StorageBoxSize = PropertyTypeDef(
    code="$STORAGE_POSITION.STORAGE_BOX_SIZE",
    description="""Box Size""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="$STORAGE_POSITION.STORAGE_BOX_SIZE",
    property_label="Storage Box Size",
)


StorageCode = PropertyTypeDef(
    code="$STORAGE_POSITION.STORAGE_CODE",
    description="""Storage Code""",
    data_type="VARCHAR",
    property_label="Storage Code",
)


StorageRackColumn = PropertyTypeDef(
    code="$STORAGE_POSITION.STORAGE_RACK_COLUMN",
    description="""Number of Columns""",
    data_type="INTEGER",
    property_label="Storage Rack Column",
)


StorageRackRow = PropertyTypeDef(
    code="$STORAGE_POSITION.STORAGE_RACK_ROW",
    description="""Number of Rows""",
    data_type="INTEGER",
    property_label="Storage Rack Row",
)


StorageUser = PropertyTypeDef(
    code="$STORAGE_POSITION.STORAGE_USER",
    description="""Storage User Id""",
    data_type="VARCHAR",
    property_label="Storage User Id",
)


CompanyAddressLine1 = PropertyTypeDef(
    code="$SUPPLIER.COMPANY_ADDRESS_LINE_1",
    description="""Company address""",
    data_type="VARCHAR",
    property_label="Company address",
)


CompanyAddressLine2 = PropertyTypeDef(
    code="$SUPPLIER.COMPANY_ADDRESS_LINE_2",
    description="""Company address, line 2""",
    data_type="VARCHAR",
    property_label="Company address, line 2",
)


CompanyEmail = PropertyTypeDef(
    code="$SUPPLIER.COMPANY_EMAIL",
    description="""Company email""",
    data_type="VARCHAR",
    property_label="Company email",
)


CompanyFax = PropertyTypeDef(
    code="$SUPPLIER.COMPANY_FAX",
    description="""Company fax""",
    data_type="VARCHAR",
    property_label="Company fax",
)


CompanyLanguage = PropertyTypeDef(
    code="$SUPPLIER.COMPANY_LANGUAGE",
    description="""Company language""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="$SUPPLIER.LANGUAGE",
    property_label="Company language",
)


CompanyPhone = PropertyTypeDef(
    code="$SUPPLIER.COMPANY_PHONE",
    description="""Company phone""",
    data_type="VARCHAR",
    property_label="Company phone",
)


CustomerNumber = PropertyTypeDef(
    code="$SUPPLIER.CUSTOMER_NUMBER",
    description="""Customer number""",
    data_type="VARCHAR",
    property_label="Customer number",
)


ColorEncodedAnnotation = PropertyTypeDef(
    code="$WELL.COLOR_ENCODED_ANNOTATION",
    description="""Color Annotation for plate wells""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="$WELL.COLOR_ENCODED_ANNOTATIONS",
    property_label="Color Annotation",
)


CompatibleRotors = PropertyTypeDef(
    code="CENTRIFUGE.COMPATIBLE_ROTORS",
    description="""Compatible Rotors with this Centrifuge//Kompatible Rotatoren mit dieser Zentrifuge""",
    data_type="VARCHAR",
    property_label="Compatible Rotors",
)


DateLastDguvChecking = PropertyTypeDef(
    code="CENTRIFUGE.DATE_LAST_DGUV_CHECKING",
    description="""Date of last checks according to DGUV Paragraph 3 Rule 100-500//Datum der letzten sicherheitstechnischen Überprüfung gemäß DGUV Paragraph 3 Regel 100-500""",
    data_type="DATE",
    property_label="Date of last DGUV check",
)


IsTemperatureControlled = PropertyTypeDef(
    code="CENTRIFUGE.IS_TEMPERATURE_CONTROLLED",
    description="""Centrifuge Temperature can be set//Zentrifuge ist temperierbar""",
    data_type="BOOLEAN",
    property_label="Temperature can be set",
)


MaximumSpeedRcf = PropertyTypeDef(
    code="CENTRIFUGE.MAXIMUM_SPEED_RCF",
    description="""Maximum Centrifugation Speed (depending on rotor) [rcf]//Maximale Zentrifugationsgeschwindigkeit (rotorabhängig) [rcf]""",
    data_type="INTEGER",
    property_label="Maximum Centrifugation Speed (depending on rotor) [rcf]",
)


MaximumSpeedRpm = PropertyTypeDef(
    code="CENTRIFUGE.MAXIMUM_SPEED_RPM",
    description="""Maximum Centrifugation Speed (depending on rotor) [rpm]//Maximale Zentrifugationsgeschwindigkeit (rotorabhängig) [rpm]""",
    data_type="INTEGER",
    property_label="Maximum Centrifugation Speed (depending on rotor) [rpm]",
)


MaximumTemperature = PropertyTypeDef(
    code="CENTRIFUGE.MAXIMUM_TEMPERATURE",
    description="""Maximum Centrifuge Temperature [°C]//Maximale Zentrifugen-Temperatur [°C]""",
    data_type="INTEGER",
    property_label="Maximum Temperature [°C]",
)


MinimumTemperature = PropertyTypeDef(
    code="CENTRIFUGE.MINIMUM_TEMPERATURE",
    description="""Minimum Centrifuge Temperature [°C]//Minimale Zentrifugen-Temperatur [°C]""",
    data_type="INTEGER",
    property_label="Minimum Temperature [°C]",
)


RequiresDguvChecking = PropertyTypeDef(
    code="CENTRIFUGE.REQUIRES_DGUV_CHECKING",
    description="""Requires checks according to DGUV Paragraph 3 Rule 100-500//Sicherheitstechnische Überprüfung gemäß DGUV Paragraph 3 Regel 100-500 vorgeschrieben""",
    data_type="BOOLEAN",
    property_label="Requires DGUV check",
)


CompatibleVials = PropertyTypeDef(
    code="CENTRIFUGE_ROTOR.COMPATIBLE_VIALS",
    description="""Compatible vials (possibly with adapters)//Kompatible Gefäße (ggf. mit Adapter)""",
    data_type="VARCHAR",
    property_label="Compatible vials (possibly with adapters)",
)


MaximumCapacityVials = PropertyTypeDef(
    code="CENTRIFUGE_ROTOR.MAXIMUM_CAPACITY_VIALS",
    description="""Maximum Rotor Capacity (number of vials)//Maximale Rotor-Kapazität (Anzahl an Gefäßen)""",
    data_type="INTEGER",
    property_label="Maximum Capacity (Number of Vials)",
)


MaximumCapacityVolume = PropertyTypeDef(
    code="CENTRIFUGE_ROTOR.MAXIMUM_CAPACITY_VOLUME",
    description="""Maximum Rotor Capacity (volume) [mL]//Maximale Rotor-Kapazität (Volumen) [mL]""",
    data_type="INTEGER",
    property_label="Maximum Capacity (Volume) [mL]",
)


MaximumSpeedRcf = PropertyTypeDef(
    code="CENTRIFUGE_ROTOR.MAXIMUM_SPEED_RCF",
    description="""Maximum Rotor Speed [rcf]//Maximale Rotor-Geschwindigkeit [rcf]""",
    data_type="INTEGER",
    property_label="Maximum Speed [rcf]",
)


MaximumSpeedRpm = PropertyTypeDef(
    code="CENTRIFUGE_ROTOR.MAXIMUM_SPEED_RPM",
    description="""Maximum Rotor Speed [rpm]//Maximale Rotor-Geschwindigkeit [rpm]""",
    data_type="INTEGER",
    property_label="Maximum Speed [rpm]",
)


ExperimentalDescription = PropertyTypeDef(
    code="DEFAULT_EXPERIMENT.EXPERIMENTAL_DESCRIPTION",
    description="""Description of the experiment""",
    data_type="MULTILINE_VARCHAR",
    property_label="Description",
)


ExperimentalGoals = PropertyTypeDef(
    code="DEFAULT_EXPERIMENT.EXPERIMENTAL_GOALS",
    description="""Goals of the experiment""",
    data_type="MULTILINE_VARCHAR",
    property_label="Goals",
)


ExperimentalResults = PropertyTypeDef(
    code="DEFAULT_EXPERIMENT.EXPERIMENTAL_RESULTS",
    description="""Summary of  experimental results""",
    data_type="MULTILINE_VARCHAR",
    property_label="Results",
)


Grant = PropertyTypeDef(
    code="DEFAULT_EXPERIMENT.GRANT",
    description="""Grant""",
    data_type="VARCHAR",
    property_label="Grant",
)


Analysismodel = PropertyTypeDef(
    code="DLS.ANALYSISMODEL",
    description="""Analysis Model//Analysemodell""",
    data_type="VARCHAR",
    property_label="Analysis Model",
)


Attenuator = PropertyTypeDef(
    code="DLS.ATTENUATOR",
    description="""Attenuator for DLS Measurement//Abschwächung für DLS Messung""",
    data_type="INTEGER",
    property_label="Attenuator",
)


Celldescription = PropertyTypeDef(
    code="DLS.CELLDESCRIPTION",
    description="""DLS Cell Description//DLS Messküvette""",
    data_type="VARCHAR",
    property_label="Cell Description",
)


Cond = PropertyTypeDef(
    code="DLS.COND",
    description="""Conductivity [mS/cm]//Leitfähigkeit [mS/cm]""",
    data_type="REAL",
    property_label="Conductivity [mS/cm]",
)


Cumulantsfiterror = PropertyTypeDef(
    code="DLS.CUMULANTSFITERROR",
    description="""Cumulants Fit Error//Fehler des Kummulanten-Fits""",
    data_type="REAL",
    property_label="Cumulants Fit Error",
)


Dispersant = PropertyTypeDef(
    code="DLS.DISPERSANT",
    description="""Dispersant for DLS Measurement//Dispersant für DLS Messung""",
    data_type="VARCHAR",
    property_label="Dispersant",
)


Fkamodel = PropertyTypeDef(
    code="DLS.FKAMODEL",
    description="""Fka Model//Fka Modell""",
    data_type="VARCHAR",
    property_label="Fka Model",
)


Intercept = PropertyTypeDef(
    code="DLS.INTERCEPT",
    description="""Measured Intercept//Achsenabschnitt""",
    data_type="REAL",
    property_label="Measured Intercept",
)


Material = PropertyTypeDef(
    code="DLS.MATERIAL",
    description="""Material Name for DLS Measurement//Materialname für DLS Messung""",
    data_type="VARCHAR",
    property_label="Material Name",
)


Multimodalfiterror = PropertyTypeDef(
    code="DLS.MULTIMODALFITERROR",
    description="""Multimodal Fit Error//Fehler des multimodalen Fits""",
    data_type="REAL",
    property_label="Multimodal Fit Error",
)


Pdi = PropertyTypeDef(
    code="DLS.PDI",
    description="""Polydispersity Index//Polydispersitätsindex""",
    data_type="REAL",
    property_label="PDI",
)


Pk1Int = PropertyTypeDef(
    code="DLS.PK1INT",
    description="""Peak 1 (Intensity) [nm]//Peak 1 (Intensität) [nm]""",
    data_type="REAL",
    property_label="Peak 1 (Intensity) [nm]",
)


Pk1Intpd = PropertyTypeDef(
    code="DLS.PK1INTPD",
    description="""Peak 1 Polydispersity (Intensity)//Peak 1 Polydispersität (Intensität)""",
    data_type="REAL",
    property_label="Peak 1 Polydispersity (Intensity)",
)


Pk1Intwidth = PropertyTypeDef(
    code="DLS.PK1INTWIDTH",
    description="""Peak 1 Width (Intensity) [nm]//Peak 1 Breite (Intensität) [nm]""",
    data_type="REAL",
    property_label="Peak 1 Width (Intensity) [nm]",
)


Pk1Num = PropertyTypeDef(
    code="DLS.PK1NUM",
    description="""Peak 1 (Number) [nm]//Peak 1 (Anzahl) [nm]""",
    data_type="REAL",
    property_label="Peak 1 (Number) [nm]",
)


Pk1Numpd = PropertyTypeDef(
    code="DLS.PK1NUMPD",
    description="""Peak 1 Polydispersity (Number)//Peak 1 Polydispersität (Anzahl)""",
    data_type="REAL",
    property_label="Peak 1 Polydispersity (Number)",
)


Pk1Numwidth = PropertyTypeDef(
    code="DLS.PK1NUMWIDTH",
    description="""Peak 1 Width (Number) [nm]//Peak 1 Breite (Anzahl) [nm]""",
    data_type="REAL",
    property_label="Peak 1 Width (Number) [nm]",
)


Pk1Vol = PropertyTypeDef(
    code="DLS.PK1VOL",
    description="""Peak 1 (Volume) [nm]//Peak 1 (Volumen) [nm]""",
    data_type="REAL",
    property_label="Peak 1 (Volume) [nm]",
)


Pk1Volpd = PropertyTypeDef(
    code="DLS.PK1VOLPD",
    description="""Peak 1 Polydispersity (Volume)//Peak 1 Polydispersität (Volumen)""",
    data_type="REAL",
    property_label="Peak 1 Polydispersity (Volume)",
)


Pk1Volwidth = PropertyTypeDef(
    code="DLS.PK1VOLWIDTH",
    description="""Peak 1 Width (Volume) [nm]//Peak 1 Breite (Volumen) [nm]""",
    data_type="REAL",
    property_label="Peak 1 Width (Volume) [nm]",
)


Pk1Zeta = PropertyTypeDef(
    code="DLS.PK1ZETA",
    description="""Peak 1 (Zetapotential) [mV]//Peak 1 (Zetapotential) [mV]""",
    data_type="REAL",
    property_label="Peak 1 (Zeta) [mV]",
)


Pk1Zetawidth = PropertyTypeDef(
    code="DLS.PK1ZETAWIDTH",
    description="""Peak 1 Width (Zetapotential) [mV]//Peak 1 Breite (Zetapotential) [mV]""",
    data_type="REAL",
    property_label="Peak 1 Width (Zeta) [mV]",
)


Pk2Int = PropertyTypeDef(
    code="DLS.PK2INT",
    description="""Peak 2 (Intensity) [nm]//Peak 2 (Intensität) [nm]""",
    data_type="REAL",
    property_label="Peak 2 (Intensity) [nm]",
)


Pk2Intpd = PropertyTypeDef(
    code="DLS.PK2INTPD",
    description="""Peak 2 Polydispersity (Intensity)//Peak 2 Polydispersität (Intensität)""",
    data_type="REAL",
    property_label="Peak 2 Polydispersity (Intensity)",
)


Pk2Intwidth = PropertyTypeDef(
    code="DLS.PK2INTWIDTH",
    description="""Peak 2 Width (Intensity) [nm]//Peak 2 Breite (Intensität) [nm]""",
    data_type="REAL",
    property_label="Peak 2 Width (Intensity) [nm]",
)


Pk2Num = PropertyTypeDef(
    code="DLS.PK2NUM",
    description="""Peak 2 (Number) [nm]//Peak 2 (Anzahl) [nm]""",
    data_type="REAL",
    property_label="Peak 2 (Number) [nm]",
)


Pk2Numpd = PropertyTypeDef(
    code="DLS.PK2NUMPD",
    description="""Peak 2 Polydispersity (Number)//Peak 2 Polydispersität (Anzahl)""",
    data_type="REAL",
    property_label="Peak 2 Polydispersity (Number)",
)


Pk2Numwidth = PropertyTypeDef(
    code="DLS.PK2NUMWIDTH",
    description="""Peak 2 Width (Number) [nm]//Peak 2 Breite (Anzahl) [nm]""",
    data_type="REAL",
    property_label="Peak 2 Width (Number) [nm]",
)


Pk2Vol = PropertyTypeDef(
    code="DLS.PK2VOL",
    description="""Peak 2 (Volume) [nm]//Peak 2 (Volumen) [nm]""",
    data_type="REAL",
    property_label="Peak 2 (Volume) [nm]",
)


Pk2Volpd = PropertyTypeDef(
    code="DLS.PK2VOLPD",
    description="""Peak 2 Polydispersity (Volume)//Peak 2 Polydispersität (Volumen)""",
    data_type="REAL",
    property_label="Peak 2 Polydispersity (Volume)",
)


Pk2Volwidth = PropertyTypeDef(
    code="DLS.PK2VOLWIDTH",
    description="""Peak 2 Width (Volume) [nm]//Peak 2 Breite (Volumen) [nm]""",
    data_type="REAL",
    property_label="Peak 2 Width (Volume) [nm]",
)


Pk2Zeta = PropertyTypeDef(
    code="DLS.PK2ZETA",
    description="""Peak 2 (Zetapotential) [mV]//Peak 2 (Zetapotential) [mV]""",
    data_type="REAL",
    property_label="Peak 2 (Zeta) [mV]",
)


Pk2Zetawidth = PropertyTypeDef(
    code="DLS.PK2ZETAWIDTH",
    description="""Peak 2 Width (Zetapotential) [mV]//Peak 2 Breite (Zetapotential) [mV]""",
    data_type="REAL",
    property_label="Peak 2 Width (Zeta) [mV]",
)


Pk3Int = PropertyTypeDef(
    code="DLS.PK3INT",
    description="""Peak 3 (Intensity) [nm]//Peak 3 (Intensität) [nm]""",
    data_type="REAL",
    property_label="Peak 3 (Intensity) [nm]",
)


Pk3Intpd = PropertyTypeDef(
    code="DLS.PK3INTPD",
    description="""Peak 3 Polydispersity (Intensity)//Peak 3 Polydispersität (Intensität)""",
    data_type="REAL",
    property_label="Peak 3 Polydispersity (Intensity)",
)


Pk3Intwidth = PropertyTypeDef(
    code="DLS.PK3INTWIDTH",
    description="""Peak 3 Width (Intensity) [nm]//Peak 3 Breite (Intensität) [nm]""",
    data_type="REAL",
    property_label="Peak 3 Width (Intensity) [nm]",
)


Pk3Num = PropertyTypeDef(
    code="DLS.PK3NUM",
    description="""Peak 3 (Number) [nm]//Peak 3 (Anzahl) [nm]""",
    data_type="REAL",
    property_label="Peak 3 (Number) [nm]",
)


Pk3Numpd = PropertyTypeDef(
    code="DLS.PK3NUMPD",
    description="""Peak 3 Polydispersity (Number)//Peak 3 Polydispersität (Anzahl)""",
    data_type="REAL",
    property_label="Peak 3 Polydispersity (Number)",
)


Pk3Numwidth = PropertyTypeDef(
    code="DLS.PK3NUMWIDTH",
    description="""Peak 3 Width (Number) [nm]//Peak 3 Breite (Anzahl) [nm]""",
    data_type="REAL",
    property_label="Peak 3 Width (Number) [nm]",
)


Pk3Vol = PropertyTypeDef(
    code="DLS.PK3VOL",
    description="""Peak 3 (Volume) [nm]//Peak 3 (Volumen) [nm]""",
    data_type="REAL",
    property_label="Peak 3 (Volume) [nm]",
)


Pk3Volpd = PropertyTypeDef(
    code="DLS.PK3VOLPD",
    description="""Peak 3 Polydispersity (Volume)//Peak 3 Polydispersität (Volumen)""",
    data_type="REAL",
    property_label="Peak 3 Polydispersity (Volume)",
)


Pk3Volwidth = PropertyTypeDef(
    code="DLS.PK3VOLWIDTH",
    description="""Peak 3 Width (Volume) [nm]//Peak 3 Breite (Volumen) [nm]""",
    data_type="REAL",
    property_label="Peak 3 Width (Volume) [nm]",
)


Pk3Zeta = PropertyTypeDef(
    code="DLS.PK3ZETA",
    description="""Peak 3 (Zetapotential) [mV]//Peak 3 (Zetapotential) [mV]""",
    data_type="REAL",
    property_label="Peak 3 (Zeta) [mV]",
)


Pk3Zetawidth = PropertyTypeDef(
    code="DLS.PK3ZETAWIDTH",
    description="""Peak 3 Width (Zetapotential) [mV]//Peak 3 Breite (Zetapotential) [mV]""",
    data_type="REAL",
    property_label="Peak 3 Width (Zeta) [mV]",
)


Sizemerit = PropertyTypeDef(
    code="DLS.SIZEMERIT",
    description="""Size Merit//Güte""",
    data_type="REAL",
    property_label="Size Merit",
)


Temperature = PropertyTypeDef(
    code="DLS.TEMPERATURE",
    description="""Temperature [°C]//Temperatur [°C]""",
    data_type="REAL",
    property_label="Temperature [°C]",
)


Volt = PropertyTypeDef(
    code="DLS.VOLT",
    description="""Measured Voltage [V]//Gemessene Spannung [V]""",
    data_type="REAL",
    property_label="Measured Voltage [V]",
)


Zavg = PropertyTypeDef(
    code="DLS.ZAVG",
    description="""Z-Average//Z-Durchschnitt""",
    data_type="REAL",
    property_label="Z-Average",
)


Zeta = PropertyTypeDef(
    code="DLS.ZETA",
    description="""Zeta Potential [mV]//Zeta Potential [mV]""",
    data_type="REAL",
    property_label="Zeta Potential [mV]",
)


ExperimentalDescription = PropertyTypeDef(
    code="EXPERIMENTAL_STEP.EXPERIMENTAL_DESCRIPTION",
    description="""Description of the experiment//Beschreibung des Experiments""",
    data_type="MULTILINE_VARCHAR",
    property_label="Experimental description",
)


ExperimentalGoals = PropertyTypeDef(
    code="EXPERIMENTAL_STEP.EXPERIMENTAL_GOALS",
    description="""Goals of the experiment//Ziele des Experiments""",
    data_type="MULTILINE_VARCHAR",
    property_label="Experimental goals",
)


ExperimentalResults = PropertyTypeDef(
    code="EXPERIMENTAL_STEP.EXPERIMENTAL_RESULTS",
    description="""Summary of experimental results//Zusammenfassung der Ergebnisse des Experiments""",
    data_type="MULTILINE_VARCHAR",
    property_label="Experimental results",
)


Spreadsheet = PropertyTypeDef(
    code="EXPERIMENTAL_STEP.SPREADSHEET",
    description="""Multi-purpose Spreadsheet//Spreadsheet zur freien Verwendung""",
    data_type="XML",
    property_label="Spreadsheet",
)


WeldmentType = PropertyTypeDef(
    code="EXPERIMENTAL_STEP.WELDMENT_TYPE",
    description="""Type of weldment made//Art der Schweißverbindung""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="WELDING.WELD_TYPE",
    property_label="Type of weld",
)


Accessory = PropertyTypeDef(
    code="FTIR.ACCESSORY",
    description="""FTIR Accessory//FTIR Zubehör""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="FTIR_ACCESSORIES",
    property_label="Accessory",
)


EndWavenumber = PropertyTypeDef(
    code="FTIR.END_WAVENUMBER",
    description="""End Wavenumber [1/cm]//End-Wellenzahl [1/cm]""",
    data_type="REAL",
    property_label="End Wavenumber [1/cm]",
)


Instrument = PropertyTypeDef(
    code="FTIR.INSTRUMENT",
    description="""FT-IR Instrument//FT-IR Instrument""",
    data_type="VARCHAR",
    property_label="Instrument",
)


IsFlushed = PropertyTypeDef(
    code="FTIR.IS_FLUSHED",
    description="""Flushed with Nitrogen//Gespült mit Sickstoff""",
    data_type="BOOLEAN",
    property_label="Flushed with Nitrogen",
)


Resolution = PropertyTypeDef(
    code="FTIR.RESOLUTION",
    description="""Resolution [1/cm]//Auflösung [1/cm]""",
    data_type="INTEGER",
    property_label="Resolution [1/cm]",
)


Scans = PropertyTypeDef(
    code="FTIR.SCANS",
    description="""Number of FTIR Scans//Anzahl FTIR Scans""",
    data_type="INTEGER",
    property_label="Number of Scans",
)


StartWavenumber = PropertyTypeDef(
    code="FTIR.START_WAVENUMBER",
    description="""Start Wavenumber [1/cm]//Start-Wellenzahl [1/cm]""",
    data_type="REAL",
    property_label="Start Wavenumber [1/cm]",
)


Materials = PropertyTypeDef(
    code="GENERAL_PROTOCOL.MATERIALS",
    description="""Machines (and relative set up)""",
    data_type="MULTILINE_VARCHAR",
    property_label="Materials",
)


ProtocolEvaluation = PropertyTypeDef(
    code="GENERAL_PROTOCOL.PROTOCOL_EVALUATION",
    description="""Parameters and observations to meet the minimal efficiency of the protocol""",
    data_type="MULTILINE_VARCHAR",
    property_label="Protocol evaluation",
)


ProtocolType = PropertyTypeDef(
    code="GENERAL_PROTOCOL.PROTOCOL_TYPE",
    description="""Category the protocol belongs to""",
    data_type="MULTILINE_VARCHAR",
    property_label="Protocol type",
)


Spreadsheet = PropertyTypeDef(
    code="GENERAL_PROTOCOL.SPREADSHEET",
    description="""Multi purpose Spreatsheet""",
    data_type="XML",
    property_label="Spreadsheet",
)


TimeRequirement = PropertyTypeDef(
    code="GENERAL_PROTOCOL.TIME_REQUIREMENT",
    description="""Time required to complete a protocol""",
    data_type="MULTILINE_VARCHAR",
    property_label="Time requirement",
)


TriggerSetting = PropertyTypeDef(
    code="IR_CAMERA.TRIGGER_SETTING",
    description="""Trigger setting//Einstellung Kameratrigger""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="IR_CAMERA.TRIGGER_SETTING",
    property_label="Trigger setting",
)


SoftwareName = PropertyTypeDef(
    code="MEASUREMENT_PROTOCOL_FILE.SOFTWARE_NAME",
    description="""Name of the Software that was used to process this measurement protocol file//Name der Software die verwendet wurde, um diese Messprotokolldatei zu verarbeiteten""",
    data_type="VARCHAR",
    property_label="Software Name",
)


SoftwareVersion = PropertyTypeDef(
    code="MEASUREMENT_PROTOCOL_FILE.SOFTWARE_VERSION",
    description="""Version of the Software that was used to process this measurement protocol file//Version der Software die verwendet wurde, um diese Messprotokolldatei zu verarbeiteten""",
    data_type="VARCHAR",
    property_label="Software Version",
)


Material = PropertyTypeDef(
    code="NDT.MATERIAL",
    description="""NDT Material//NDT Material""",
    data_type="VARCHAR",
    property_label="Material",
)


MaterialNumber = PropertyTypeDef(
    code="NDT.MATERIAL_NUMBER",
    description="""NDT Material number//NDT Werkstoffnummer""",
    data_type="VARCHAR",
    property_label="Material number",
)


AcquisitionTime = PropertyTypeDef(
    code="NMR.ACQUISITION_TIME",
    description="""Acquisition Time [s]//Akquisitionszeit [s]""",
    data_type="REAL",
    property_label="Acquisition Time [s]",
)


EndChemicalShift = PropertyTypeDef(
    code="NMR.END_CHEMICAL_SHIFT",
    description="""End Chemical Shift [ppm]//Ende Chemische Verschiebung [ppm]""",
    data_type="REAL",
    property_label="End Chemical Shift [ppm]",
)


Experiment = PropertyTypeDef(
    code="NMR.EXPERIMENT",
    description="""NMR Experiment//NMR Experiment""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="NMR_EXPERIMENT_TYPES",
    property_label="Experiment",
)


Frequency = PropertyTypeDef(
    code="NMR.FREQUENCY",
    description="""NMR Frequency [MHz]//NMR Frequenz [MHz]""",
    data_type="REAL",
    property_label="Frequency [MHz]",
)


Instrument = PropertyTypeDef(
    code="NMR.INSTRUMENT",
    description="""NMR Instrument//NMR Instrument""",
    data_type="VARCHAR",
    property_label="Instrument",
)


InterpulseDelay = PropertyTypeDef(
    code="NMR.INTERPULSE_DELAY",
    description="""Interpulse Delay [s]//Wartezeit zwischen Pulsen [s]""",
    data_type="REAL",
    property_label="Interpulse Delay [s]",
)


IsQnmr = PropertyTypeDef(
    code="NMR.IS_QNMR",
    description="""Quantitative NMR//Quantitatives NMR""",
    data_type="BOOLEAN",
    property_label="Quantitative NMR",
)


NucleusDirect = PropertyTypeDef(
    code="NMR.NUCLEUS_DIRECT",
    description="""Nucleus (direct)//Kern (direct)""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="NMR_NUCLEI",
    property_label="Nucleus (direct)",
)


NucleusIndirect = PropertyTypeDef(
    code="NMR.NUCLEUS_INDIRECT",
    description="""Nucleus (indirect, 2D only)//Kern (indirekt, nur 2D)""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="NMR_NUCLEI",
    property_label="Nucleus (indirect, 2D only)",
)


PulseAngle = PropertyTypeDef(
    code="NMR.PULSE_ANGLE",
    description="""Pulse Angle [degree]//Pulswinkel [degree]""",
    data_type="REAL",
    property_label="Pulse Angle [degree]",
)


Scans = PropertyTypeDef(
    code="NMR.SCANS",
    description="""Number of NMR Scans//Anzahl NMR Scans""",
    data_type="INTEGER",
    property_label="Number of Scans",
)


Solvent = PropertyTypeDef(
    code="NMR.SOLVENT",
    description="""NMR Solvent//NMR Lösungsmittel""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="NMR_SOLVENTS",
    property_label="Solvent",
)


StartChemicalShift = PropertyTypeDef(
    code="NMR.START_CHEMICAL_SHIFT",
    description="""Start Chemical Shift [ppm]//Start Chemische Verschiebung [ppm]""",
    data_type="REAL",
    property_label="Start Chemical Shift [ppm]",
)


PricePaid = PropertyTypeDef(
    code="ORDER.PRICE_PAID",
    description="""Price Paid""",
    data_type="REAL",
    property_label="Price Paid",
)


Spreadsheet = PropertyTypeDef(
    code="PARAMETER_SET.SPREADSHEET",
    description="""Table of parameters//Parameter-Tabelle""",
    data_type="XML",
    property_label="Parameter Table",
)


Category = PropertyTypeDef(
    code="PRODUCT.CATEGORY",
    description="""Category""",
    data_type="VARCHAR",
    property_label="Category",
)


Company = PropertyTypeDef(
    code="PRODUCT.COMPANY",
    description="""Company""",
    data_type="VARCHAR",
    property_label="Company",
)


Description = PropertyTypeDef(
    code="PRODUCT.DESCRIPTION",
    description="""Description""",
    data_type="MULTILINE_VARCHAR",
    property_label="Description",
)


HazardStatement = PropertyTypeDef(
    code="PRODUCT.HAZARD_STATEMENT",
    description="""Hazard Statement""",
    data_type="VARCHAR",
    property_label="Hazard Statement",
)


ProductSecondaryNames = PropertyTypeDef(
    code="PRODUCT.PRODUCT_SECONDARY_NAMES",
    description="""Product Secondary Names""",
    data_type="VARCHAR",
    property_label="Product Secondary Names",
)


SizeOfItem = PropertyTypeDef(
    code="PRODUCT.SIZE_OF_ITEM",
    description="""Size of Item""",
    data_type="VARCHAR",
    property_label="Size of Item",
)


Buyer = PropertyTypeDef(
    code="REQUEST.BUYER",
    description="""Buyer""",
    data_type="VARCHAR",
    property_label="Buyer",
)


Department = PropertyTypeDef(
    code="REQUEST.DEPARTMENT",
    description="""Department""",
    data_type="VARCHAR",
    property_label="Department",
)


Project = PropertyTypeDef(
    code="REQUEST.PROJECT",
    description="""Project""",
    data_type="VARCHAR",
    property_label="Project",
)


Accelerationvoltage = PropertyTypeDef(
    code="SEM.ACCELERATIONVOLTAGE",
    description="""Acceleration Voltage [keV]//Beschleunigungsspannung [keV]""",
    data_type="VARCHAR",
    property_label="Acceleration Voltage [keV]",
)


Detector = PropertyTypeDef(
    code="SEM.DETECTOR",
    description="""Detector//Detektor""",
    data_type="VARCHAR",
    property_label="Detector",
)


Imagesizex = PropertyTypeDef(
    code="SEM.IMAGESIZEX",
    description="""Image Size X//Bildgröße X""",
    data_type="VARCHAR",
    property_label="Image Size X",
)


Imagesizey = PropertyTypeDef(
    code="SEM.IMAGESIZEY",
    description="""Image Size Y//Bildgröße Y""",
    data_type="VARCHAR",
    property_label="Image Size Y",
)


Instrument = PropertyTypeDef(
    code="SEM.INSTRUMENT",
    description="""SEM Instrument//SEM Instrument""",
    data_type="VARCHAR",
    property_label="Instrument",
)


Magnification = PropertyTypeDef(
    code="SEM.MAGNIFICATION",
    description="""Magnificaiton//Vergrößerung""",
    data_type="VARCHAR",
    property_label="Magnification",
)


Operatingmode = PropertyTypeDef(
    code="SEM.OPERATINGMODE",
    description="""Operating Mode//Aufnahmemodus""",
    data_type="VARCHAR",
    property_label="Operating Mode",
)


Pixelsizex = PropertyTypeDef(
    code="SEM.PIXELSIZEX",
    description="""Pixel Size X//Pixelgröße X""",
    data_type="VARCHAR",
    property_label="Pixel Size X",
)


Pixelsizey = PropertyTypeDef(
    code="SEM.PIXELSIZEY",
    description="""Pixel Size Y//Pixelgrße Y""",
    data_type="VARCHAR",
    property_label="Pixel Size Y",
)


Projectormode = PropertyTypeDef(
    code="SEM.PROJECTORMODE",
    description="""Projector Mode//Projektionsmodus""",
    data_type="VARCHAR",
    property_label="Projector Mode",
)


Workingdistance = PropertyTypeDef(
    code="SEM.WORKINGDISTANCE",
    description="""Working Distance [mm]//Arbeitsabstand [mm]""",
    data_type="VARCHAR",
    property_label="Working Distance [mm]",
)


AdditionalInformation = PropertyTypeDef(
    code="SUPPLIER.ADDITIONAL_INFORMATION",
    description="""Additional Information""",
    data_type="VARCHAR",
    property_label="Additional Information",
)


CompanyContactEmail = PropertyTypeDef(
    code="SUPPLIER.COMPANY_CONTACT_EMAIL",
    description="""Company contact email""",
    data_type="VARCHAR",
    property_label="Company contact email",
)


CompanyContactName = PropertyTypeDef(
    code="SUPPLIER.COMPANY_CONTACT_NAME",
    description="""Company contact name""",
    data_type="VARCHAR",
    property_label="Company contact name",
)


PreferredOrderMethod = PropertyTypeDef(
    code="SUPPLIER.PREFERRED_ORDER_METHOD",
    description="""Preferred order method""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="$SUPPLIER.PREFERRED_ORDER_METHOD",
    property_label="Preferred order method",
)


Url = PropertyTypeDef(
    code="SUPPLIER.URL",
    description="""URL""",
    data_type="HYPERLINK",
    property_label="URL",
)


Accelerationvoltage = PropertyTypeDef(
    code="TEM.ACCELERATIONVOLTAGE",
    description="""Acceleration Voltage [keV]//Beschleunigungsspannung [keV]""",
    data_type="VARCHAR",
    property_label="Acceleration Voltage  [keV]",
)


C2ApertureName = PropertyTypeDef(
    code="TEM.C2_APERTURE_NAME",
    description="""C2 Aperture//C2 Apertur""",
    data_type="VARCHAR",
    property_label="C2 Aperture",
)


Cameralength = PropertyTypeDef(
    code="TEM.CAMERALENGTH",
    description="""Camera Length//Kamera-Länge""",
    data_type="VARCHAR",
    property_label="Camera Length",
)


Detector = PropertyTypeDef(
    code="TEM.DETECTOR",
    description="""Detector//Detektor""",
    data_type="VARCHAR",
    property_label="Detector",
)


GunLensSetting = PropertyTypeDef(
    code="TEM.GUN_LENS_SETTING",
    description="""Gun Lens Setting//Einstellung der Elektronenquellenlinse""",
    data_type="VARCHAR",
    property_label="Gun Lens Setting",
)


Imagesizex = PropertyTypeDef(
    code="TEM.IMAGESIZEX",
    description="""Image Size X//Bildgröße X""",
    data_type="VARCHAR",
    property_label="Image Size X",
)


Imagesizey = PropertyTypeDef(
    code="TEM.IMAGESIZEY",
    description="""Image Size Y//Bildgröße Y""",
    data_type="VARCHAR",
    property_label="Image Size Y",
)


Instrument = PropertyTypeDef(
    code="TEM.INSTRUMENT",
    description="""TEM Instrument//TEM Instrument""",
    data_type="VARCHAR",
    property_label="Instrument",
)


Magnification = PropertyTypeDef(
    code="TEM.MAGNIFICATION",
    description="""Magnification//Vergrößerung""",
    data_type="VARCHAR",
    property_label="Magnification",
)


ObjApertureName = PropertyTypeDef(
    code="TEM.OBJ_APERTURE_NAME",
    description="""Objective Aperture//Objektiv Apertur""",
    data_type="VARCHAR",
    property_label="Objective Aperture",
)


Operatingmode = PropertyTypeDef(
    code="TEM.OPERATINGMODE",
    description="""Operating Mode//Aufnahmemodus""",
    data_type="VARCHAR",
    property_label="Operating Mode",
)


Pixelsizex = PropertyTypeDef(
    code="TEM.PIXELSIZEX",
    description="""Pixel Size X//Pixelgröße X""",
    data_type="VARCHAR",
    property_label="Pixel Size X",
)


Pixelsizey = PropertyTypeDef(
    code="TEM.PIXELSIZEY",
    description="""Pixel Size Y//Pixelgrße Y""",
    data_type="VARCHAR",
    property_label="Pixel Size Y",
)


Projectormode = PropertyTypeDef(
    code="TEM.PROJECTORMODE",
    description="""Projector Mode//Projektionsmodus""",
    data_type="VARCHAR",
    property_label="Projector Mode",
)


SaedAperturediameter = PropertyTypeDef(
    code="TEM.SAED_APERTUREDIAMETER",
    description="""SAED Aperture Diameter//SAED Apertur Durchmesser""",
    data_type="VARCHAR",
    property_label="SAED Aperture Diameter",
)


SaedApertureposx = PropertyTypeDef(
    code="TEM.SAED_APERTUREPOSX",
    description="""SAED Aperture Pos X//SAED Apertur Position X""",
    data_type="VARCHAR",
    property_label="SAED Aperture Pos X",
)


SaedApertureposy = PropertyTypeDef(
    code="TEM.SAED_APERTUREPOSY",
    description="""SAED Aperture Pos Y//SAED Apertur Position Y""",
    data_type="VARCHAR",
    property_label="SAED Aperture PosY",
)


SpotIndex = PropertyTypeDef(
    code="TEM.SPOT_INDEX",
    description="""Spot Index//Spot Index""",
    data_type="VARCHAR",
    property_label="Spot Index",
)


ArcCurrentContinuous = PropertyTypeDef(
    code="WELDING.ARC_CURRENT_CONTINUOUS",
    description="""Maximum continuous arc current at 100% duty cycle//Maximaler Schweißstrom bei 100% Einschaltdauer""",
    data_type="REAL",
    property_label="Maximum continuous arc current [A]",
)


ArcCurrentMax = PropertyTypeDef(
    code="WELDING.ARC_CURRENT_MAX",
    description="""Maximum arc current//Maximaler Schweißstrom""",
    data_type="REAL",
    property_label="Arc current maximum [A]",
)


ArcCurrentMin = PropertyTypeDef(
    code="WELDING.ARC_CURRENT_MIN",
    description="""Minimum arc current//Minimaler Schweißstrom""",
    data_type="REAL",
    property_label="Arc current minimum [A]",
)


TorchType = PropertyTypeDef(
    code="WELDING.TORCH_TYPE",
    description="""type of welding torch//Art des Schweißbrenners""",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="WELDING.GMAW_TORCH_TYPE",
    property_label="Type",
)


AwsSpecname = PropertyTypeDef(
    code="WELDING_WIRE.AWS_SPECNAME",
    description="""AWS specification of the wire//AWS Klassifizierung des Zusatzwerkstoffs""",
    data_type="VARCHAR",
    property_label="AWS specification",
)


AwsStandard = PropertyTypeDef(
    code="WELDING_WIRE.AWS_STANDARD",
    description="""AWS standard providing the specification//AWS Standard mit Angabe zur Klassifizierung""",
    data_type="VARCHAR",
    property_label="AWS standard",
)


Diameter = PropertyTypeDef(
    code="WELDING_WIRE.DIAMETER",
    description="""Diameter in mm//Durchmesser in mm""",
    data_type="REAL",
    property_label="Diameter [mm]",
)


IsoSpecname = PropertyTypeDef(
    code="WELDING_WIRE.ISO_SPECNAME",
    description="""ISO specification of the wire//ISO Klassifizierung des Zusatzwerkstoffs""",
    data_type="VARCHAR",
    property_label="ISO specification",
)


IsoStandard = PropertyTypeDef(
    code="WELDING_WIRE.ISO_STANDARD",
    description="""ISO standard providing the specification//ISO Norm o.ä. mit Angabe zur Klassifizierung""",
    data_type="VARCHAR",
    property_label="ISO standard",
)


Weight = PropertyTypeDef(
    code="WELDING_WIRE.WEIGHT",
    description="""Weight of the wire package as delivered//Gesamtgewicht des Drahtes bei Lieferung""",
    data_type="REAL",
    property_label="Weight [kg]",
)


QuantityOfItems = PropertyTypeDef(
    code="ANNOTATION.REQUEST.QUANTITY_OF_ITEMS",
    description="""Quantity of Items""",
    data_type="INTEGER",
    property_label="Quantity of Items",
)


Comments = PropertyTypeDef(
    code="ANNOTATION.SYSTEM.COMMENTS",
    description="""Comments""",
    data_type="VARCHAR",
    property_label="Comments",
)


ArcCurrent = PropertyTypeDef(
    code="EXPERIMENTAL_STEP.WELDMENT.ARC_CURRENT",
    description="""Welding arc current//Schweißstrom""",
    data_type="REAL",
    property_label="Arc current [A]",
)


ArcProcess = PropertyTypeDef(
    code="EXPERIMENTAL_STEP.WELDMENT.ARC_PROCESS",
    description="""Name of the selected arc welding process//Name des Lichtbogenschweißprozesses""",
    data_type="VARCHAR",
    property_label="Arc welding process",
)


ArcVoltage = PropertyTypeDef(
    code="EXPERIMENTAL_STEP.WELDMENT.ARC_VOLTAGE",
    description="""Welding arc voltage//Lichtbogenspannung""",
    data_type="REAL",
    property_label="Arc voltage [V]",
)


CurrentTransformer = PropertyTypeDef(
    code="EXPERIMENTAL_STEP.WELDMENT.CURRENT_TRANSFORMER",
    description="""Current transformer HAS 50-S//Stromwandler HAS 50-S""",
    data_type="REAL",
    property_label="Current transformer HAS 50-S [mV/A]",
)


GroovePreparation = PropertyTypeDef(
    code="EXPERIMENTAL_STEP.WELDMENT.GROOVE_PREPARATION",
    description="""Groove or Joint preparation description//Beschreibung der Nahtvorbereitung""",
    data_type="VARCHAR",
    property_label="Groove preparation",
)


LaserFocus = PropertyTypeDef(
    code="EXPERIMENTAL_STEP.WELDMENT.LASER_FOCUS",
    description="""Laser focus position//Laser Fokuslage""",
    data_type="REAL",
    property_label="Laser focus [mm]",
)


LaserPower = PropertyTypeDef(
    code="EXPERIMENTAL_STEP.WELDMENT.LASER_POWER",
    description="""Laser power//Laserleistung""",
    data_type="REAL",
    property_label="Laser power [kW]",
)


LaserWireOffset = PropertyTypeDef(
    code="EXPERIMENTAL_STEP.WELDMENT.LASER_WIRE_OFFSET",
    description="""Distance from laser spot to wire feed//Abstand zwischen Laser und Draht""",
    data_type="REAL",
    property_label="Laser distance to wire [mm]",
)


MagnetCapacitance = PropertyTypeDef(
    code="EXPERIMENTAL_STEP.WELDMENT.MAGNET_CAPACITANCE",
    description="""Capacitance//Kapazität""",
    data_type="REAL",
    property_label="Capacitance C [µF]",
)


MagnetFrequency = PropertyTypeDef(
    code="EXPERIMENTAL_STEP.WELDMENT.MAGNET_FREQUENCY",
    description="""Frequency//Frequenz""",
    data_type="REAL",
    property_label="Frequency F [Hz]",
)


MagnetI1 = PropertyTypeDef(
    code="EXPERIMENTAL_STEP.WELDMENT.MAGNET_I_1",
    description="""Magnet I_1 value//Magnet I_1 Wert""",
    data_type="REAL",
    property_label="I_1 [A]",
)


MagnetU1 = PropertyTypeDef(
    code="EXPERIMENTAL_STEP.WELDMENT.MAGNET_U_1",
    description="""Magnet U_1 value//Magnet U_1 Wert""",
    data_type="REAL",
    property_label="U_1 [mV]",
)


ShieldingGasFlow = PropertyTypeDef(
    code="EXPERIMENTAL_STEP.WELDMENT.SHIELDING_GAS_FLOW",
    description="""Shielding gas flowrate//Schutzgasflussgeschwindigkeit""",
    data_type="REAL",
    property_label="Shielding gas flowrate [l/min]",
)


WeldTravelSpeed = PropertyTypeDef(
    code="EXPERIMENTAL_STEP.WELDMENT.WELD_TRAVEL_SPEED",
    description="""Welding travel speed//Schweißgeschwindigkeit""",
    data_type="REAL",
    property_label="Welding travel speed [cm/min]",
)


WireFeedRate = PropertyTypeDef(
    code="EXPERIMENTAL_STEP.WELDMENT.WIRE_FEED_RATE",
    description="""Welding wire feed rate//Drahtvorschubrate""",
    data_type="REAL",
    property_label="Wire feed rate [m/min]",
)


WireStickoutLength = PropertyTypeDef(
    code="EXPERIMENTAL_STEP.WELDMENT.WIRE_STICKOUT_LENGTH",
    description="""Length of the wire stickout//Stickoutlänge des Schweißdrahtes""",
    data_type="REAL",
    property_label="Wire stickout [mm]",
)


WorkpieceThickness = PropertyTypeDef(
    code="EXPERIMENTAL_STEP.WELDMENT.WORKPIECE_THICKNESS",
    description="""Workpiece thickness//Bauteildicke""",
    data_type="REAL",
    property_label="Thickness of the workpiece [mm]",
)


LineResolution = PropertyTypeDef(
    code="INSTRUMENT.LASER_SCANNER.LINE_RESOLUTION",
    description="""Maximum resolution per laser line//Maximale Anzahl Messpunkte per Linienmessung""",
    data_type="INTEGER",
    property_label="Maximum line resolution [pixel]",
)


XMax = PropertyTypeDef(
    code="INSTRUMENT.LASER_SCANNER.X_MAX",
    description="""Maximum measuring distance in z-Direction//Maximaler Messabstand in z-Richtung""",
    data_type="REAL",
    property_label="Maximum x measuring range [mm]",
)


XMin = PropertyTypeDef(
    code="INSTRUMENT.LASER_SCANNER.X_MIN",
    description="""Minimal measuring distance in z-Direction//Minimaler Messabstand in z-Richtung""",
    data_type="REAL",
    property_label="Minimum x measuring range [mm]",
)


ZMax = PropertyTypeDef(
    code="INSTRUMENT.LASER_SCANNER.Z_MAX",
    description="""Maximum measuring distance in z-Direction//Maximaler Messabstand in z-Richtung""",
    data_type="REAL",
    property_label="Maximum z distance [mm]",
)


ZMin = PropertyTypeDef(
    code="INSTRUMENT.LASER_SCANNER.Z_MIN",
    description="""Minimal measuring distance in z-Direction//Minimaler Messabstand in z-Richtung""",
    data_type="REAL",
    property_label="Minimum z distance [mm]",
)
