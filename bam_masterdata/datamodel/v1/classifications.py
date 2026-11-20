# AUTO-GENERATED CLASS HIERARCHY — DO NOT EDIT
#
# Classification*
# └── DangerousGood
#
# END AUTO-GENERATED CLASS HIERARCHY

from bam_masterdata.datamodel.v1.entities import Classification
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment


class DangerousGood(Classification):
    defs = ObjectTypeDef(
        code="DANGEROUS_GOOD",
        description="A DangerousGood is a classification that specifies the dangerous-goods transport "
        "designation assigned to a material entity.",
        generated_code_prefix="DANG_GOOD",
    )

    un_number = PropertyTypeAssignment(
        code="UN_NUMBER",
        data_type="VARCHAR",
        property_label="UN number",
        description="UN identifier associated with the dangerous-goods classification.",
        mandatory=False,
        section="Dangerous Goods Classification",
    )

    hazard_class = PropertyTypeAssignment(
        code="HAZARD_CLASS",
        data_type="VARCHAR",
        property_label="Hazard class",
        description="Transport hazard class or division associated with the dangerous-goods classification.",
        mandatory=False,
        section="Dangerous Goods Classification",
    )

    packing_group = PropertyTypeAssignment(
        code="PACKING_GROUP",
        data_type="VARCHAR",
        property_label="Packing group",
        description="Packing group assigned under the applicable dangerous-goods classification, where applicable.",
        mandatory=False,
        section="Dangerous Goods Classification",
    )

    # LINK_TO_DGG_DATABASE maps to EXTERNAL_REFERENCES (in Root)
