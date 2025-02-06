from bam_masterdata.metadata.definitions import PropertyTypeDef

PropA = PropertyTypeDef(
    code="PROPA",
    description="""repeated property""",
    data_type="VARCHAR",
    property_label="A1",
)


PropB = PropertyTypeDef(
    code="PROPB",
    description="""non-repeated property""",
    data_type="VARCHAR",
    property_label="B",
)

PropA = PropertyTypeDef(
    code="PROPA",
    description="""repeated property""",
    data_type="VARCHAR",
    property_label="A2",
)
