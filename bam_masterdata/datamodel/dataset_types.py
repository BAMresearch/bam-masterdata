from pydantic import BaseModel

from bam_masterdata.metadata.definitions import DataSetTypeDef


class ElnPreview(BaseModel):
    defs = DataSetTypeDef(
        code='ELN_PREVIEW',
        description='',
    )


class RawData(BaseModel):
    defs = DataSetTypeDef(
        code='RAW_DATA',
        description='Data not processed',
    )


class ProcessedData(BaseModel):
    defs = DataSetTypeDef(
        code='PROCESSED_DATA',
        description='',
    )


class AnalyzedData(BaseModel):
    defs = DataSetTypeDef(
        code='ANALYZED_DATA',
        description='',
    )


class Attachment(BaseModel):
    defs = DataSetTypeDef(
        code='ATTACHMENT',
        description='',
    )


class OtherData(BaseModel):
    defs = DataSetTypeDef(
        code='OTHER_DATA',
        description='',
    )


class SourceCode(BaseModel):
    defs = DataSetTypeDef(
        code='SOURCE_CODE',
        description='',
    )


class AnalysisNotebook(BaseModel):
    defs = DataSetTypeDef(
        code='ANALYSIS_NOTEBOOK',
        description='',
    )


class PublicationData(BaseModel):
    defs = DataSetTypeDef(
        code='PUBLICATION_DATA',
        description='',
    )
