"""Assignments reused within this version's battery definitions."""

from bam_masterdata.metadata.definitions import PropertyTypeAssignment

LAB_ID = PropertyTypeAssignment(
    code="LAB_ID",
    data_type="VARCHAR",
    property_label="Lab id",
    description="Source laboratory identifier",
    mandatory=False,
    section="Battery details",
)
RECORD_DATETIME = PropertyTypeAssignment(
    code="RECORD_DATETIME",
    data_type="TIMESTAMP",
    property_label="Record datetime",
    description="Datetime recorded for this entry; not necessarily preparation or assembly time",
    mandatory=False,
    section="Battery details",
)
PRODUCT_NUMBER = PropertyTypeAssignment(
    code="PRODUCT_NUMBER",
    data_type="VARCHAR",
    property_label="Product number",
    description="Supplier product identifier",
    mandatory=False,
    section="Battery details",
)
SHIPPING_DATETIME = PropertyTypeAssignment(
    code="SHIPPING_DATETIME",
    data_type="TIMESTAMP",
    property_label="Shipping datetime",
    description="Product shipping timestamp",
    mandatory=False,
    section="Battery details",
)
OPENING_DATETIME = PropertyTypeAssignment(
    code="OPENING_DATETIME",
    data_type="TIMESTAMP",
    property_label="Opening datetime",
    description="Product opening timestamp",
    mandatory=False,
    section="Battery details",
)
PRODUCT_WEIGHT = PropertyTypeAssignment(
    code="PRODUCT_WEIGHT_G",
    data_type="REAL",
    property_label="Product weight",
    description="Product mass",
    mandatory=False,
    section="Battery details",
    units="g",
)
PRODUCT_VOLUME = PropertyTypeAssignment(
    code="PRODUCT_VOLUME_ML",
    data_type="REAL",
    property_label="Product volume",
    description="Product volume",
    mandatory=False,
    section="Battery details",
    units="mL",
)
CASTING_PROCEDURE = PropertyTypeAssignment(
    code="CASTING_PROCEDURE",
    data_type="VARCHAR",
    property_label="Casting procedure",
    description="Source casting procedure",
    mandatory=False,
    section="Battery details",
)
CASE_ID = PropertyTypeAssignment(
    code="CASE_ID",
    data_type="VARCHAR",
    property_label="Case id",
    description="Source cell case identifier",
    mandatory=False,
    section="Battery details",
)
CASE_CRIMP = PropertyTypeAssignment(
    code="CASE_CRIMP",
    data_type="VARCHAR",
    property_label="Case crimp",
    description="Source case crimp method",
    mandatory=False,
    section="Battery details",
)
THICKNESS = PropertyTypeAssignment(
    code="THICKNESS_UM",
    data_type="REAL",
    property_label="Thickness",
    description="Thickness of the material or sample",
    mandatory=False,
    section="Battery details",
    units="um",
)
MASS = PropertyTypeAssignment(
    code="MASS_G",
    data_type="REAL",
    property_label="Mass",
    description="Mass of the material or sample",
    mandatory=False,
    section="Battery details",
    units="g",
)
LENGTH = PropertyTypeAssignment(
    code="LENGTH_MM",
    data_type="REAL",
    property_label="Length",
    description="Length of the material or sample",
    mandatory=False,
    section="Battery details",
    units="mm",
)
WIDTH = PropertyTypeAssignment(
    code="WIDTH_MM",
    data_type="REAL",
    property_label="Width",
    description="Width of the material or sample",
    mandatory=False,
    section="Battery details",
    units="mm",
)
DIAMETER = PropertyTypeAssignment(
    code="DIAMETER_MM",
    data_type="REAL",
    property_label="Diameter",
    description="Diameter of the material or sample",
    mandatory=False,
    section="Battery details",
    units="mm",
)
AREA = PropertyTypeAssignment(
    code="AREA_CM2",
    data_type="REAL",
    property_label="Area",
    description="Area of the material or sample",
    mandatory=False,
    section="Battery details",
    units="cm^2",
)
VOLUME = PropertyTypeAssignment(
    code="VOLUME_ML",
    data_type="REAL",
    property_label="Volume",
    description="Volume of the material or sample",
    mandatory=False,
    section="Battery details",
    units="mL",
)
SHAPE = PropertyTypeAssignment(
    code="BATTERY_PLANAR_SHAPE",
    data_type="CONTROLLEDVOCABULARY",
    vocabulary_code="BATTERY_PLANAR_SHAPE",
    property_label="Planar shape",
    description="Shape of the planar sample or sheet.",
    mandatory=False,
    section="Battery details",
)
