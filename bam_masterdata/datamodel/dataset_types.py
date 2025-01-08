from bam_masterdata.metadata.definitions import DataSetTypeDef
from bam_masterdata.metadata.entities import DatasetType


class ElnPreview(DatasetType):
    defs = DataSetTypeDef(
        code="ELN_PREVIEW",
        description="""""",
    )


class RawData(DatasetType):
    defs = DataSetTypeDef(
        code="RAW_DATA",
        description="""""",
    )


class ProcessedData(DatasetType):
    defs = DataSetTypeDef(
        code="PROCESSED_DATA",
        description="""""",
    )


class AnalyzedData(DatasetType):
    defs = DataSetTypeDef(
        code="ANALYZED_DATA",
        description="""""",
    )


class Attachment(DatasetType):
    defs = DataSetTypeDef(
        code="ATTACHMENT",
        description="""""",
    )


class OtherData(DatasetType):
    defs = DataSetTypeDef(
        code="OTHER_DATA",
        description="""""",
    )


class SourceCode(DatasetType):
    defs = DataSetTypeDef(
        code="SOURCE_CODE",
        description="""""",
    )


class AnalysisNotebook(DatasetType):
    defs = DataSetTypeDef(
        code="ANALYSIS_NOTEBOOK",
        description="""""",
    )


class PublicationData(DatasetType):
    defs = DataSetTypeDef(
        code="PUBLICATION_DATA",
        description="""""",
    )


class Document(DatasetType):
    defs = DataSetTypeDef(
        code="DOCUMENT",
        description="""Document//Dokument""",
    )


class TestFile(DatasetType):
    defs = DataSetTypeDef(
        code="TEST_FILE",
        description="""Test File//Test-Datei""",
    )


class LogFile(DatasetType):
    defs = DataSetTypeDef(
        code="LOG_FILE",
        description="""A log file//Eine Log-Datei""",
    )


class MeasurementProtocolFile(DatasetType):
    defs = DataSetTypeDef(
        code="MEASUREMENT_PROTOCOL_FILE",
        description="""A measurement protocol file that was used with a measurement software (proprietary or otherwise)//Eine Messprotokolldatei die mit einer (propritären oder anderen) Mess-Software verwendet wurde""",
    )


class Norm(DatasetType):
    defs = DataSetTypeDef(
        code="NORM",
        description="""Technical Norm//Technische Norm""",
    )


class CompEnv(DatasetType):
    defs = DataSetTypeDef(
        code="COMP_ENV",
        description="""Computational environment file//Rechenumgebung Datei""",
    )


class MatModel(DatasetType):
    defs = DataSetTypeDef(
        code="MAT_MODEL",
        description="""Material model file//Materialmodell Datei""",
    )


class PyironJob(DatasetType):
    defs = DataSetTypeDef(
        code="PYIRON_JOB",
        description="""HDF5 file with pyiron job information//HDF5 Datei mit pyiron Job Informationen""",
    )


class SourceCodeWorkflow(DatasetType):
    defs = DataSetTypeDef(
        code="SOURCE_CODE_WORKFLOW",
        description="""Source Code for Workflow//Quellcode für Workflow""",
    )


class Figure(DatasetType):
    defs = DataSetTypeDef(
        code="FIGURE",
        description="""Figure//Bild""",
    )


class MatSimStructure(DatasetType):
    defs = DataSetTypeDef(
        code="MAT_SIM_STRUCTURE",
        description="""Simulation Structure//Simulationstruktur""",
    )


class Pseudopot(MatModel):
    defs = DataSetTypeDef(
        code="MAT_MODEL.PSEUDOPOT",
        description="""Material model file for a pseudopotential//Materialmodell Datei für Pseudopotential""",
    )


class IntPot(MatModel):
    defs = DataSetTypeDef(
        code="MAT_MODEL.INT_POT",
        description="""Material model file for an interatomic potential//Materialmodell Datei für Interatomarer Potential""",
    )


class Plot(Figure):
    defs = DataSetTypeDef(
        code="FIGURE.PLOT",
        description="""Plot//Plot""",
    )


class Schematic(Figure):
    defs = DataSetTypeDef(
        code="FIGURE.SCHEMATIC",
        description="""Schematic//Schema-Bild""",
    )


class SimVis(Figure):
    defs = DataSetTypeDef(
        code="FIGURE.SIM_VIS",
        description="""Simulation Visualization//Visualisierung der Simulation""",
    )
