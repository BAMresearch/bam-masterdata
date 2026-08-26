from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.entities import ObjectType


class Entry(ObjectType):
    defs = ObjectTypeDef(
        code="ENTRY",
        description="""""",
        generated_code_prefix="ENTRY",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        section="General Information",
    )

    show_in_project_overview = PropertyTypeAssignment(
        code="$SHOW_IN_PROJECT_OVERVIEW",
        data_type="BOOLEAN",
        property_label="Show in project overview",
        description="""Show in project overview page""",
        mandatory=False,
        section="General Information",
    )

    document = PropertyTypeAssignment(
        code="$DOCUMENT",
        data_type="MULTILINE_VARCHAR",
        property_label="Document",
        description="""Document""",
        mandatory=False,
        section="General Information",
    )


class SubEntry(Entry):
    defs = ObjectTypeDef(
        code="ENTRY.SUBENTRY",
        description="""""",
        generated_code_prefix="ENTRY.SUB",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative Name",
        description="""e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname""",
        mandatory=False,
        section="General Information",
    )

    test_sync_prop = PropertyTypeAssignment(
        code="TEST_SYNC_PROP",
        data_type="VARCHAR",
        property_label="Testing the sync cli in bam-masterdata",
        description="""changing now the description!""",
        mandatory=False,
        section="General NEW SECTION CHANGE",
    )
