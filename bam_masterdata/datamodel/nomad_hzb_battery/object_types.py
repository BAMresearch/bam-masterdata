from bam_masterdata.datamodel.v1.entities import Sample
from bam_masterdata.metadata.definitions import (
    ObjectTypeDef,
    PropertyTypeAssignment,
)


class CoinCell(Sample):
    defs = ObjectTypeDef(
        code="COIN_CELL",
        description="Coin cell battery sample",
        generated_code_prefix="CCELL",
    )

    # NOMAD m_def:
    # nomad_battery_space.schema_packages.
    # hzb_bs_assembly_package.CoinCellBattery
    # TODO: Integrate external schema references into ObjectTypeDef
    # to support generic mappings between external data models.
    external_def = {
        "NOMAD": "nomad_battery_space.schema_packages.hzb_bs_assembly_package.CoinCellBattery",
    }

    assembly_datetime = PropertyTypeAssignment(
        code="ASSEMBLY_DATETIME",
        data_type="TIMESTAMP",
        property_label="Assembly datetime",
        description="Date and time of the battery assembly.",
        mandatory=False,
        section="Battery Assembly",
    )

    case_id = PropertyTypeAssignment(
        code="CASE_ID",
        data_type="VARCHAR",
        property_label="Case ID",
        description="Identifier of the coin cell case.",
        mandatory=False,
        section="Battery Assembly",
    )

    case_crimp = PropertyTypeAssignment(
        code="CASE_CRIMP",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CASE_CRIMP",
        property_label="Case crimping method",
        description="Method used to crimp the coin cell case.",
        mandatory=False,
        section="Battery Assembly",
    )

    aggregated_elements = PropertyTypeAssignment(
        code="AGGREGATED_ELEMENTS",
        data_type="MULTILINE_VARCHAR",
        property_label="Aggregated elements",
        description="Chemical elements present in the coin cell.",
        mandatory=False,
        section="Battery Assembly",
    )
