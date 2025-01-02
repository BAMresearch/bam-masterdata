from pydantic import BaseModel

from bam_masterdata.metadata.definitions import DatasetTypeDef


class ElnPreview(BaseModel):
    defs = DatasetTypeDef(
        code='ELN_PREVIEW',
        description="",
    )


class RawData(BaseModel):
    defs = DatasetTypeDef(
        code='RAW_DATA',
        description="Data not processed",
    )


class ProcessedData(BaseModel):
    defs = DatasetTypeDef(
        code='PROCESSED_DATA',
        description="",
    )


class AnalyzedData(BaseModel):
    defs = DatasetTypeDef(
        code='ANALYZED_DATA',
        description="",
    )


class Attachment(BaseModel):
    defs = DatasetTypeDef(
        code='ATTACHMENT',
        description="",
    )


class OtherData(BaseModel):
    defs = DatasetTypeDef(
        code='OTHER_DATA',
        description="",
    )


class SourceCode(BaseModel):
    defs = DatasetTypeDef(
        code='SOURCE_CODE',
        description="",
    )


class AnalysisNotebook(BaseModel):
    defs = DatasetTypeDef(
        code='ANALYSIS_NOTEBOOK',
        description="",
    )


class PublicationData(BaseModel):
    defs = DatasetTypeDef(
        code='PUBLICATION_DATA',
        description="",
    )

