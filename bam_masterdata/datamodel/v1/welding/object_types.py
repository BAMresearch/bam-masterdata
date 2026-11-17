from bam_masterdata.datamodel.v1.entities import Material
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment


class WeldingWire(Material):
    defs = ObjectTypeDef(
        code="WELDING_WIRE",
        description="A WeldingWire is a Sample ...",
        generated_code_prefix="WELD_WIRE",
        prev_versions=["CONSUMABLE.WELDING.WIRE_SOLID:v0"],
    )

    diameter_mm = PropertyTypeAssignment(
        code="DIAMETER_MM",
        data_type="REAL",
        property_label="Diameter",
        units="mm",
        description="""Diameter""",
        mandatory=True,
        section="Wire Information",
        prev_versions=["WELDING_WIRE.DIAMETER:v0"],
    )

    weight_kg = PropertyTypeAssignment(
        code="WEIGHT_KG",
        data_type="REAL",
        property_label="Weight",
        units="kg",
        description="""Weight""",
        mandatory=True,
        section="Wire Information",
        prev_versions=["WELDING_WIRE.WEIGHT:v0"],
    )

    iso_specname = PropertyTypeAssignment(
        code="ISO_SPECNAME",
        data_type="VARCHAR",
        property_label="ISO specification",
        description="""ISO specification""",
        mandatory=False,
        section="Wire Information",
        prev_versions=["WELDING_WIRE.ISO_SPECNAME:v0"],
    )

    iso_standard = PropertyTypeAssignment(
        code="ISO_STANDARD",
        data_type="VARCHAR",
        property_label="ISO standard",
        description="""ISO standard""",
        mandatory=False,
        section="Wire Information",
        prev_versions=["WELDING_WIRE.ISO_STANDARD:v0"],
    )

    aws_specname = PropertyTypeAssignment(
        code="AWS_SPECNAME",
        data_type="VARCHAR",
        property_label="AWS specification",
        description="""AWS specification""",
        mandatory=False,
        section="Wire Information",
        prev_versions=["WELDING_WIRE.AWS_SPECNAME:v0"],
    )

    aws_standard = PropertyTypeAssignment(
        code="AWS_STANDARD",
        data_type="VARCHAR",
        property_label="AWS standard",
        description="""AWS standard providing the specification""",
        mandatory=False,
        section="Wire Information",
        prev_versions=["WELDING_WIRE.AWS_STANDARD:v0"],
    )

    # New properties suggested in Miro:
    #   LOT_NUMBER (VARCHAR)
    #   MATERIAL (OBJECT, WeldingWireAllow)
    #   WIRE_TYPE (CONTROLLEDVOCABULARY) --> maybe MATERIAL_TYPE?
