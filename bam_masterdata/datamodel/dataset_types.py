from bam_masterdata.metadata.definitions import DatasetTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.entities import DatasetType


class ElnPreview(DatasetType):
    defs = DatasetTypeDef(
        code="ELN_PREVIEW",
        description="""""",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class RawData(DatasetType):
    defs = DatasetTypeDef(
        code="RAW_DATA",
        description="""""",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class ProcessedData(DatasetType):
    defs = DatasetTypeDef(
        code="PROCESSED_DATA",
        description="""""",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class AnalyzedData(DatasetType):
    defs = DatasetTypeDef(
        code="ANALYZED_DATA",
        description="""""",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class Attachment(DatasetType):
    defs = DatasetTypeDef(
        code="ATTACHMENT",
        description="""""",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class OtherData(DatasetType):
    defs = DatasetTypeDef(
        code="OTHER_DATA",
        description="""""",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class SourceCode(DatasetType):
    defs = DatasetTypeDef(
        code="SOURCE_CODE",
        description="""""",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class AnalysisNotebook(DatasetType):
    defs = DatasetTypeDef(
        code="ANALYSIS_NOTEBOOK",
        description="""""",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
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


class PublicationData(DatasetType):
    defs = DatasetTypeDef(
        code="PUBLICATION_DATA",
        description="""""",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class Document(DatasetType):
    defs = DatasetTypeDef(
        code="DOCUMENT",
        description="""Document//Dokument""",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    document_type = PropertyTypeAssignment(
        code="DOCUMENT_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DOCUMENT_TYPE",
        property_label="Document type",
        description="""Document Type//Dokumenten Typ""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative Name",
        description="""e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    author = PropertyTypeAssignment(
        code="AUTHOR",
        data_type="VARCHAR",
        property_label="Author(s)",
        description="""Author(s)//Autor(en)""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    version = PropertyTypeAssignment(
        code="VERSION",
        data_type="VARCHAR",
        property_label="Version",
        description="""Version""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class TestFile(DatasetType):
    defs = DatasetTypeDef(
        code="TEST_FILE",
        description="""Test File//Test-Datei""",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    document_type = PropertyTypeAssignment(
        code="DOCUMENT_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DOCUMENT_TYPE",
        property_label="Document type",
        description="""Document Type//Dokumenten Typ""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative Name",
        description="""e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    author = PropertyTypeAssignment(
        code="AUTHOR",
        data_type="VARCHAR",
        property_label="Author(s)",
        description="""Author(s)//Autor(en)""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    version = PropertyTypeAssignment(
        code="VERSION",
        data_type="VARCHAR",
        property_label="Version",
        description="""Version""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class LogFile(DatasetType):
    defs = DatasetTypeDef(
        code="LOG_FILE",
        description="""A log file//Eine Log-Datei""",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class MeasurementProtocolFile(DatasetType):
    defs = DatasetTypeDef(
        code="MEASUREMENT_PROTOCOL_FILE",
        description="""A measurement protocol file that was used with a measurement software (proprietary or otherwise)//Eine Messprotokolldatei die mit einer (propritären oder anderen) Mess-Software verwendet wurde""",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    measurement_protocol_file_software_name = PropertyTypeAssignment(
        code="MEASUREMENT_PROTOCOL_FILE.SOFTWARE_NAME",
        data_type="VARCHAR",
        property_label="Software Name",
        description="""Name of the Software that was used to process this measurement protocol file//Name der Software die verwendet wurde, um diese Messprotokolldatei zu verarbeiteten""",
        mandatory=False,
        show_in_edit_views=False,
        section="Software",
    )

    measurement_protocol_file_software_version = PropertyTypeAssignment(
        code="MEASUREMENT_PROTOCOL_FILE.SOFTWARE_VERSION",
        data_type="VARCHAR",
        property_label="Software Version",
        description="""Version of the Software that was used to process this measurement protocol file//Version der Software die verwendet wurde, um diese Messprotokolldatei zu verarbeiteten""",
        mandatory=False,
        show_in_edit_views=False,
        section="Software",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class Norm(DatasetType):
    defs = DatasetTypeDef(
        code="NORM",
        description="""Technical Norm//Technische Norm""",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    date_publication = PropertyTypeAssignment(
        code="DATE_PUBLICATION",
        data_type="DATE",
        property_label="Date of publication",
        description="""Date of publication//Publikationsdatum""",
        mandatory=False,
        show_in_edit_views=False,
        section="Norm Details",
    )

    norm_analyzed_matrix = PropertyTypeAssignment(
        code="NORM_ANALYZED_MATRIX",
        data_type="VARCHAR",
        property_label="Analyzed matrix",
        description="""Analyzed matrix//Analysierte Matrix""",
        mandatory=False,
        show_in_edit_views=False,
        section="Norm Details",
    )

    norm_title = PropertyTypeAssignment(
        code="NORM_TITLE",
        data_type="VARCHAR",
        property_label="Title",
        description="""Title of the norm//Titel der Norm""",
        mandatory=True,
        show_in_edit_views=False,
        section="Norm Details",
    )

    version = PropertyTypeAssignment(
        code="VERSION",
        data_type="VARCHAR",
        property_label="Version",
        description="""Version""",
        mandatory=False,
        show_in_edit_views=False,
        section="Norm Details",
    )

    norm_url = PropertyTypeAssignment(
        code="NORM_URL",
        data_type="HYPERLINK",
        property_label="Source URL",
        description="""Source URL of Norm//Quell URL der Norm""",
        mandatory=False,
        show_in_edit_views=False,
        section="Norm Details",
    )

    last_check = PropertyTypeAssignment(
        code="LAST_CHECK",
        data_type="DATE",
        property_label="Date of last check",
        description="""Date of the last check//Datum der letzten Überprüfung""",
        mandatory=True,
        show_in_edit_views=False,
        section="Automation",
    )

    check_interval = PropertyTypeAssignment(
        code="CHECK_INTERVAL",
        data_type="INTEGER",
        property_label="Check interval [days]",
        description="""Time interval for checks in days//Überprüfungsintervall in Tagen""",
        mandatory=True,
        show_in_edit_views=False,
        section="Automation",
    )

    state_check = PropertyTypeAssignment(
        code="STATE_CHECK",
        data_type="BOOLEAN",
        property_label="Needs to be checked?",
        description="""TRUE if task needs to be done//WAHR wenn die Aufgabe getan werden muss""",
        mandatory=False,
        show_in_edit_views=False,
        section="Automation",
    )

    responsible_person = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Responsible person",
        description="""Responsible person//Verantwortliche Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="Automation",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class CompEnv(DatasetType):
    defs = DatasetTypeDef(
        code="COMP_ENV",
        description="""Computational environment file//Rechenumgebung Datei""",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    env_tool = PropertyTypeAssignment(
        code="ENV_TOOL",
        data_type="VARCHAR",
        property_label="Environment Tool Used",
        description="""E.g., conda//Z.B., conda""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class MatModel(DatasetType):
    defs = DatasetTypeDef(
        code="MAT_MODEL",
        description="""Material model file//Materialmodell Datei""",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    author = PropertyTypeAssignment(
        code="AUTHOR",
        data_type="VARCHAR",
        property_label="Author(s)",
        description="""Author(s)//Autor(en)""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    mat_scale = PropertyTypeAssignment(
        code="MAT_SCALE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="MAT_SCALE",
        property_label="Material Scale",
        description="""Material scale//Material Skala""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    file_format = PropertyTypeAssignment(
        code="FILE_FORMAT",
        data_type="VARCHAR",
        property_label="File format",
        description="""File format//Dateiformat""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    reference = PropertyTypeAssignment(
        code="REFERENCE",
        data_type="MULTILINE_VARCHAR",
        property_label="References",
        description="""Useful refences""",
        mandatory=False,
        show_in_edit_views=False,
        section="External Documetation",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class PyironJob(DatasetType):
    defs = DatasetTypeDef(
        code="PYIRON_JOB",
        description="""HDF5 file with pyiron job information//HDF5 Datei mit pyiron Job Informationen""",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    production_date = PropertyTypeAssignment(
        code="PRODUCTION_DATE",
        data_type="DATE",
        property_label="Production Date",
        description="""Production Date//Herstellungsdatum""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    file_format = PropertyTypeAssignment(
        code="FILE_FORMAT",
        data_type="VARCHAR",
        property_label="File format",
        description="""File format//Dateiformat""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    pyiron_hdf5_version = PropertyTypeAssignment(
        code="PYIRON_HDF5_VERSION",
        data_type="VARCHAR",
        property_label="pyiron HDF5 Version",
        description="""pyiron HDF5 format version//pyiron HDF5 Format Version""",
        mandatory=False,
        show_in_edit_views=False,
        section="Pyiron Information",
    )

    reference = PropertyTypeAssignment(
        code="REFERENCE",
        data_type="MULTILINE_VARCHAR",
        property_label="References",
        description="""Useful refences""",
        mandatory=False,
        show_in_edit_views=False,
        section="External Documetation",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class SourceCodeWorkflow(DatasetType):
    defs = DatasetTypeDef(
        code="SOURCE_CODE_WORKFLOW",
        description="""Source Code for Workflow//Quellcode für Workflow""",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    compilation_req = PropertyTypeAssignment(
        code="COMPILATION_REQ",
        data_type="BOOLEAN",
        property_label="Compilation Required?",
        description="""Is compilation required?//Ist eine Kompilierung erforderlich?""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    compiler = PropertyTypeAssignment(
        code="COMPILER",
        data_type="MULTILINE_VARCHAR",
        property_label="Compiler",
        description="""Compiler info//Compiler-Informationen""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    source_code_language = PropertyTypeAssignment(
        code="SOURCE_CODE_LANGUAGE",
        data_type="VARCHAR",
        property_label="Programming Language(s) Used",
        description="""Programming Language(s) used//Verwendete Programmiersprache(n)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class Figure(DatasetType):
    defs = DatasetTypeDef(
        code="FIGURE",
        description="""Figure//Bild""",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    col_blind_access = PropertyTypeAssignment(
        code="COL_BLIND_ACCESS",
        data_type="BOOLEAN",
        property_label="Colour-blind Accessibilty",
        description="""Colour-blind Accessibilty//Farbenblindheit Barrierefreiheit""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    author = PropertyTypeAssignment(
        code="AUTHOR",
        data_type="VARCHAR",
        property_label="Author(s)",
        description="""Author(s)//Autor(en)""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    production_date = PropertyTypeAssignment(
        code="PRODUCTION_DATE",
        data_type="DATE",
        property_label="Production Date",
        description="""Production Date//Herstellungsdatum""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    license = PropertyTypeAssignment(
        code="LICENSE",
        data_type="VARCHAR",
        property_label="License",
        description="""License//Lizenz""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    image_horizontal_resolution = PropertyTypeAssignment(
        code="IMAGE_HORIZONTAL_RESOLUTION",
        data_type="INTEGER",
        property_label="Horizontal resolution [pixel]",
        description="""Horizontal resolution of the image [pixel]//Horizonzale Auflösung des Bildes [Pixel]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    image_vertical_resolution = PropertyTypeAssignment(
        code="IMAGE_VERTICAL_RESOLUTION",
        data_type="INTEGER",
        property_label="Vertical resolution [pixel]",
        description="""Vertical resolution of the image [pixel]////Vertikale Auflösung des Bildes [Pixel]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    fig_dpi = PropertyTypeAssignment(
        code="FIG_DPI",
        data_type="INTEGER",
        property_label="Dots Per Inch (DPI)",
        description="""Dots per inch (DPI)//Punkte pro Zoll""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    file_format = PropertyTypeAssignment(
        code="FILE_FORMAT",
        data_type="VARCHAR",
        property_label="File format",
        description="""File format//Dateiformat""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class MatSimStructure(DatasetType):
    defs = DatasetTypeDef(
        code="MAT_SIM_STRUCTURE",
        description="""Simulation Structure//Simulationstruktur""",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    mat_scale = PropertyTypeAssignment(
        code="MAT_SCALE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="MAT_SCALE",
        property_label="Material Scale",
        description="""Material scale//Material Skala""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    multi_mat_scale = PropertyTypeAssignment(
        code="MULTI_MAT_SCALE",
        data_type="VARCHAR",
        property_label="Material Scales if Multiple",
        description="""Material scales if multiple (refer to property `Material Scale` for terminology)//Materialskala, falls mehrere vorhanden sind (siehe „MaterialScale“-Eigenschaft zur Terminologie)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    sw_compatibility = PropertyTypeAssignment(
        code="SW_COMPATIBILITY",
        data_type="VARCHAR",
        property_label="Software Compatibility",
        description="""Software which can use this file//Software, die diese Datei verwenden kann""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    file_format = PropertyTypeAssignment(
        code="FILE_FORMAT",
        data_type="VARCHAR",
        property_label="File format",
        description="""File format//Dateiformat""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class Pseudopot(MatModel):
    defs = DatasetTypeDef(
        code="MAT_MODEL.PSEUDOPOT",
        description="""Material model file for a pseudopotential//Materialmodell Datei für Pseudopotential""",
    )


class IntPot(MatModel):
    defs = DatasetTypeDef(
        code="MAT_MODEL.INT_POT",
        description="""Material model file for an interatomic potential//Materialmodell Datei für Interatomarer Potential""",
    )


class Plot(Figure):
    defs = DatasetTypeDef(
        code="FIGURE.PLOT",
        description="""Plot//Plot""",
    )

    plot_x_label = PropertyTypeAssignment(
        code="PLOT_X_LABEL",
        data_type="VARCHAR",
        property_label="Label of X-Axis",
        description="""Label of X-axis//X-Achsenbeschriftung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Content Information",
    )

    plot_y_label = PropertyTypeAssignment(
        code="PLOT_Y_LABEL",
        data_type="VARCHAR",
        property_label="Label of Y-Axis",
        description="""Label of Y-axis//Y-Achsenbeschriftung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Content Information",
    )

    plot_z_label = PropertyTypeAssignment(
        code="PLOT_Z_LABEL",
        data_type="VARCHAR",
        property_label="Label of Z-Axis",
        description="""Label of Z-axis//Z-Achsenbeschriftung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Content Information",
    )

    plot_x_range = PropertyTypeAssignment(
        code="PLOT_X_RANGE",
        data_type="REAL",
        property_label="Range of X-Axis",
        description="""Range of X-axis//Bereich der X-Achse""",
        mandatory=False,
        show_in_edit_views=False,
        section="Content Information",
    )

    plot_y_range = PropertyTypeAssignment(
        code="PLOT_Y_RANGE",
        data_type="REAL",
        property_label="Range of Y-Axis",
        description="""Range of Y-axis//Bereich der Y-Achse""",
        mandatory=False,
        show_in_edit_views=False,
        section="Content Information",
    )

    plot_z_range = PropertyTypeAssignment(
        code="PLOT_Z_RANGE",
        data_type="REAL",
        property_label="Range of Z-Axis",
        description="""Range of Z-axis//Bereich der Z-Achse""",
        mandatory=False,
        show_in_edit_views=False,
        section="Content Information",
    )

    plot_x_units = PropertyTypeAssignment(
        code="PLOT_X_UNITS",
        data_type="VARCHAR",
        property_label="Units of X-Axis",
        description="""Units of X-axis//X-Achse Einheiten""",
        mandatory=False,
        show_in_edit_views=False,
        section="Content Information",
    )

    plot_y_units = PropertyTypeAssignment(
        code="PLOT_Y_UNITS",
        data_type="VARCHAR",
        property_label="Units of Y-Axis",
        description="""Units of Y-axis//Y-Achse Einheiten""",
        mandatory=False,
        show_in_edit_views=False,
        section="Content Information",
    )

    plot_z_units = PropertyTypeAssignment(
        code="PLOT_Z_UNITS",
        data_type="VARCHAR",
        property_label="Units of Z-Axis",
        description="""Units of Z-axis//Z-Achse Einheiten""",
        mandatory=False,
        show_in_edit_views=False,
        section="Content Information",
    )

    plot_legend = PropertyTypeAssignment(
        code="PLOT_LEGEND",
        data_type="MULTILINE_VARCHAR",
        property_label="Plot Legend",
        description="""Plot legend//Legende des Plots""",
        mandatory=False,
        show_in_edit_views=False,
        section="Content Information",
    )


class Schematic(Figure):
    defs = DatasetTypeDef(
        code="FIGURE.SCHEMATIC",
        description="""Schematic//Schema-Bild""",
    )


class SimVis(Figure):
    defs = DatasetTypeDef(
        code="FIGURE.SIM_VIS",
        description="""Simulation Visualization//Visualisierung der Simulation""",
    )

    sim_vis_cbar = PropertyTypeAssignment(
        code="SIM_VIS_CBAR",
        data_type="BOOLEAN",
        property_label="Colour Bar?",
        description="""Colour bar?//Farbskala""",
        mandatory=False,
        show_in_edit_views=False,
        section="Content Information",
    )

    sim_vis_cbar_max = PropertyTypeAssignment(
        code="SIM_VIS_CBAR_MAX",
        data_type="REAL",
        property_label="Colour Bar Max. Range",
        description="""Colour bar max. range//Farbskala max. Bereich""",
        mandatory=False,
        show_in_edit_views=False,
        section="Content Information",
    )

    sim_vis_cbar_min = PropertyTypeAssignment(
        code="SIM_VIS_CBAR_MIN",
        data_type="REAL",
        property_label="Colour bar Min. Range",
        description="""Colour bar min. range//Farbskala min. Bereich""",
        mandatory=False,
        show_in_edit_views=False,
        section="Content Information",
    )

    sim_vis_cbar_prop = PropertyTypeAssignment(
        code="SIM_VIS_CBAR_PROP",
        data_type="VARCHAR",
        property_label="Colour Bar Property",
        description="""Property visualized by colour bar//Eigenschaft visualisiert durch Farbskala""",
        mandatory=False,
        show_in_edit_views=False,
        section="Content Information",
    )

    sim_vis_cbar_units = PropertyTypeAssignment(
        code="SIM_VIS_CBAR_UNITS",
        data_type="VARCHAR",
        property_label="Colour Bar Units",
        description="""Colour bar units//Farbskaleneinheiten""",
        mandatory=False,
        show_in_edit_views=False,
        section="Content Information",
    )

    sim_vis_coord = PropertyTypeAssignment(
        code="SIM_VIS_COORD",
        data_type="BOOLEAN",
        property_label="Coordinate Tripod?",
        description="""Coordinate tripod//Koordinatensystem""",
        mandatory=False,
        show_in_edit_views=False,
        section="Content Information",
    )

    sim_vis_coord_x = PropertyTypeAssignment(
        code="SIM_VIS_COORD_X",
        data_type="VARCHAR",
        property_label="Coordinate Index X",
        description="""Coordinate index X//Koordinatenindex X""",
        mandatory=False,
        show_in_edit_views=False,
        section="Content Information",
    )

    sim_vis_coord_y = PropertyTypeAssignment(
        code="SIM_VIS_COORD_Y",
        data_type="VARCHAR",
        property_label="Coordinate Index Y",
        description="""Coordinate index Y//Koordinatenindex Y""",
        mandatory=False,
        show_in_edit_views=False,
        section="Content Information",
    )

    sim_vis_coord_z = PropertyTypeAssignment(
        code="SIM_VIS_COORD_Z",
        data_type="VARCHAR",
        property_label="Coordinate Index Z",
        description="""Coordinate index Z//Koordinatenindex Z""",
        mandatory=False,
        show_in_edit_views=False,
        section="Content Information",
    )

    sim_vis_scbar = PropertyTypeAssignment(
        code="SIM_VIS_SCBAR",
        data_type="BOOLEAN",
        property_label="Scale Bar?",
        description="""Scale bar?//Maßstabsbalken""",
        mandatory=False,
        show_in_edit_views=False,
        section="Content Information",
    )

    sim_vis_scbar_units = PropertyTypeAssignment(
        code="SIM_VIS_SCBAR_UNITS",
        data_type="VARCHAR",
        property_label="Scale Units",
        description="""Scale units//Maßeinheiten""",
        mandatory=False,
        show_in_edit_views=False,
        section="Content Information",
    )
