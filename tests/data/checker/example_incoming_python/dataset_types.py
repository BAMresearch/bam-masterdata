from bam_masterdata.metadata.definitions import DatasetTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.entities import DatasetType


class AnalysisNotebook(DatasetType):
    defs = DatasetTypeDef(
        code="ANALYSIS_NOTEBOOK",
        description="""""",
    )

    history_id = PropertyTypeAssignment(
        code="$HISTORY_ID",
        data_type="VARCHAR",
        property_label="History ID",
        description="""History ID""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class AnalyzedData(DatasetType):
    defs = DatasetTypeDef(
        code="ANALYZED_DATA",
        description="""""",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes//Notizen""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )
