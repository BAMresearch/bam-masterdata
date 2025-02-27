from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.entities import ObjectType


class Action(ObjectType):
    defs = ObjectTypeDef(
        code="ACTION",
        description="""This Object allows to store information on an action by a user.//Dieses Objekt erlaubt eine Nutzer-Aktion zu beschreiben.""",
        generated_code_prefix="ACT",
    )

    acting_person = PropertyTypeAssignment(
        code="ACTING_PERSON",
        data_type="OBJECT",
        property_label="Acting Person",
        description="""Acting Person//Handelnde Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="Action Data",
    )

    action_date = PropertyTypeAssignment(
        code="ACTION_DATE",
        data_type="DATE",
        property_label="Monitoring Date",
        description="""Action Date//Datum der Handlung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Action Data",
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

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="Device ID",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )
