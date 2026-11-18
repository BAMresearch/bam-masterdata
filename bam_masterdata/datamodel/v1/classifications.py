from bam_masterdata.datamodel.v1.entities import Classification
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment


class DangerousGood(Classification):
    defs = ObjectTypeDef(
        code="DANGEROUS_GOOD",
        description="A DangerousGood is a classification representing the hazardous characteristic assigned "
        "to a material entity according to applicable dangerous goods standards.",
        generated_code_prefix="DANG_GOOD",
    )

    un_number = PropertyTypeAssignment(
        code="UN_NUMBER",
        data_type="???",
        property_label="UN Number",
        description="...",
        mandatory=False,
        section="Hazardous Details",
    )

    hazard_class = PropertyTypeAssignment(
        code="HAZARD_CLASS",
        data_type="???",
        property_label="Hazard class",
        description="...",
        mandatory=False,
        section="Hazardous Details",
    )

    packing_group = PropertyTypeAssignment(
        code="PACKING_GROUP",
        data_type="???",
        property_label="Packing group",
        description="...",
        mandatory=False,
        section="Hazardous Details",
    )

    # LINK_TO_DGG_DATABASE maps to EXTERNAL_REFERENCES (in Root)
