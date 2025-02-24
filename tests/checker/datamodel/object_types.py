from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.entities import ObjectType


class Action(ObjectType):
    defs = ObjectTypeDef(
        code="ACTION",
        description="""This Object allows to store information on an action by a user.//Dieses Objekt erlaubt eine Nutzer-Aktion zu beschreiben.""",
        generated_code_prefix="ACT",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="MULTILINE_VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="Device ID",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="HYPERLINK",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )


class AuxiliaryMaterial(ObjectType):
    defs = ObjectTypeDef(
        code="AUXILIARY_MATERIAL",
        description="""Auxiliary Material//Hilfsstoff""",
        generated_code_prefix="AUX_MAT",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="INTEGER",
        property_label="Alternative Name",
        description="""e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="REAL",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )
