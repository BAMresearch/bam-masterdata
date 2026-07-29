from bam_masterdata.metadata.definitions import VocabularyTerm, VocabularyTypeDef
from bam_masterdata.metadata.entities import VocabularyType


class IonizationType(VocabularyType):
    defs = VocabularyTypeDef(
        code="IONIZATION_TYPE",
        description="""Ionization Type//Ionenquelle""",
    )

    esi = VocabularyTerm(
        code="ESI",
        label="ESI",
        description="""Electrospray Ionization//Electrospray Ionisierung""",
    )

    ei = VocabularyTerm(
        code="EI",
        label="EI",
        description="""Electron Impact Ionization//Elektronenstossionisierung""",
    )

    ci = VocabularyTerm(
        code="CI",
        label="CI",
        description="""Chemical Ionization//Chemische Ionisierung""",
    )

    apci = VocabularyTerm(
        code="APCI",
        label="APCI",
        description="""Athmospheric Pressure Chemical Ionization//Athmosphärendruck Chemische Ionisierung""",
    )


class ChromatographyType(VocabularyType):
    defs = VocabularyTypeDef(
        code="CHROMATOGRAPHY_TYPE",
        description="""Separator Type//Trennverfahren""",
    )

    lc = VocabularyTerm(
        code="LC",
        label="LC",
        description="""Liquid Chromatography//Flüssigchromatographie""",
    )

    hplc = VocabularyTerm(
        code="HPLC",
        label="HPLC",
        description="""High-Performance Liquid Chromatography//Hochleistungsflüssigchromatographie""",
    )

    uplc = VocabularyTerm(
        code="UPLC",
        label="UPLC",
        description="""Ultra-High-Performance Liquid Chromatography//Ultrahochleistungsflüssigchromatographie""",
    )

    gc = VocabularyTerm(
        code="GC",
        label="GC",
        description="""Gas Chromatography//Gaschromatographie""",
    )

    sfc = VocabularyTerm(
        code="SFC",
        label="SFC",
        description="""Supercritical Fluid Chromatography//Überkritische Fluidchromatographie""",
    )

    ic = VocabularyTerm(
        code="IC",
        label="IC",
        description="""Ion Chromatography//Ionenchromatographie""",
    )

    none = VocabularyTerm(
        code="NONE",
        label="none",
        description="""Without Chromatography//Keine Chromatography""",
    )


class DetectorType(VocabularyType):
    defs = VocabularyTypeDef(
        code="DETECTOR_TYPE",
        description="""Detector Type//Analysator""",
    )

    fid = VocabularyTerm(
        code="FID",
        label="FID",
        description="""Flame Ionization Detector//Flammenionisationsdetektor""",
    )

    ecd = VocabularyTerm(
        code="ECD",
        label="ECD",
        description="""Electron Capture Detector//Elektroneneinfangdetektor""",
    )

    ms_ms = VocabularyTerm(
        code="MSMS",
        label="MS/MS",
        description="""Tandem Mass Spectrometer//Tandem-Massenspektrometer""",
    )

    dad = VocabularyTerm(
        code="DAD",
        label="DAD",
        description="""Diode Array Detector//Diodenarraydetektor""",
    )

    uv = VocabularyTerm(
        code="UV",
        label="UV",
        description="""Ultraviolet Absorbance Detector//UV-Absorptionsdetektor""",
    )

    qtof = VocabularyTerm(
        code="QTOF",
        label="QTOF",
        description="""Quadrupole Time-of-Flight Mass Spectrometer//Quadrupol-Flugzeit-Massenspektrometer""",
    )

    q = VocabularyTerm(
        code="Q",
        label="Quadrupol",
        description="""Quadrupol//Quadrupol""",
    )

    qqq = VocabularyTerm(
        code="QQQ",
        label="Triple Quad",
        description="""Triple Quad//Triple Quad""",
    )

    qtof_alt = VocabularyTerm(
        code="QTOF",
        label="Quadrupol-Time Of Flight",
        description="""Quadrupol-Time Of Flight//Quadrupol-Time Of Flight""",
    )

    tof = VocabularyTerm(
        code="TOF",
        label="Time Of Flight",
        description="""Time Of Flight//Time Of Flight""",
    )

    fld = VocabularyTerm(
        code="FLD",
        label="FLD",
        description="""Fluorescence Detector//Fluoreszenzdetektor""",
    )


class MsAcquisitionMode(VocabularyType):
    defs = VocabularyTypeDef(
        code="MS_ACQUISITION_MODE",
        description="""Acquisition mode//Aufnahmemodus""",
    )

    fullscan = VocabularyTerm(
        code="FULL_SCAN",
        label="Full Scan",
        description="""Full Scan//Full Scan""",
    )

    ida = VocabularyTerm(
        code="IDA",
        label="IDA",
        description="""Information dependent acquisition//Informationsabhängige Aufnahme""",
    )

    swath = VocabularyTerm(
        code="SWATH",
        label="SWATH",
        description="""SWATH//SWATH""",
    )

    mrm = VocabularyTerm(
        code="MRM",
        label="MRM",
        description="""Multiple Reaction Monitoring//Multiple Reaction Monitoring""",
    )

    sim = VocabularyTerm(
        code="SIM",
        label="SIM",
        description="""Single Ion Monitoring//Single Ion Monitoring""",
    )


class MsIonPolarity(VocabularyType):
    defs = VocabularyTypeDef(
        code="MS_ION_POLARITY",
        description="""Ion polarity//Ionenpolarität""",
    )

    positive = VocabularyTerm(
        code="POSITIVE",
        label="Positive",
        description="""Positive Ion//Positive Ionen""",
    )

    negative = VocabularyTerm(
        code="NEGATIVE",
        label="Negative",
        description="""Negative Ion//Negative Ionen""",
    )

    positive_negative = VocabularyTerm(
        code="POSITIVENEGATIVE",
        label="Positive/Negative",
        description="""Positive and Negative Ions//Positive und Negative Ionen""",
    )


class MassSpecType(VocabularyType):
    defs = VocabularyTypeDef(
        code="MASS_SPEC_TYPE",
        description="""Mass Spec Type//Typ des Massenspektrometers""",
    )

    icp = VocabularyTerm(
        code="ICP",
        label="ICP",
        description="""ICP//ICP""",
    )

    maldi = VocabularyTerm(
        code="MALDI",
        label="MALDI",
        description="""MALDI//MALDI""",
    )

    q = VocabularyTerm(
        code="Q",
        label="Quadrupol",
        description="""Quadrupol//Quadrupol""",
    )

    qqq = VocabularyTerm(
        code="QQQ",
        label="Triple Quad",
        description="""Triple Quad//Triple Quad""",
    )

    qtof = VocabularyTerm(
        code="QTOF",
        label="Quadrupol-Time Of Flight",
        description="""Quadrupol-Time Of Flight//Quadrupol-Time Of Flight""",
    )

    tof = VocabularyTerm(
        code="TOF",
        label="Time Of Flight",
        description="""Time Of Flight//Time Of Flight""",
    )

    trap = VocabularyTerm(
        code="TRAP",
        label="Orbitrap",
        description="""Orbitrap//Orbitrap""",
    )
