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
