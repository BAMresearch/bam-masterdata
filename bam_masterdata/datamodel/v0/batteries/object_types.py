"""Battery definitions for the observed HZB archive concepts."""

from bam_masterdata.datamodel.v0.object_types import Chemical, MaterialV1, Sample
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.provenance import SOURCE_RECORD

from . import properties as p


class ChemicalStock(Chemical):
    defs = ObjectTypeDef(
        code="CHEMICAL.STOCK",
        description="A ChemicalStock is a purchased chemical item held as a source for laboratory preparation.",
        generated_code_prefix="BAT",
    )
    source_record = SOURCE_RECORD
    record_datetime = p.RECORD_DATETIME
    lab_id = p.LAB_ID.model_copy(update={"mandatory": True})
    manufacturer = Chemical.manufacturer.model_copy(update={"mandatory": False})
    hazardous_substance = Chemical.hazardous_substance.model_copy(
        update={"mandatory": False}
    )
    bam_oe = Chemical.bam_oe.model_copy(update={"mandatory": False})
    bam_location_complete = Chemical.bam_location_complete.model_copy(
        update={"mandatory": False}
    )
    product_number = p.PRODUCT_NUMBER
    shipping_datetime = p.SHIPPING_DATETIME
    opening_datetime = p.OPENING_DATETIME
    product_weight = p.PRODUCT_WEIGHT
    product_volume = p.PRODUCT_VOLUME
    chemical_formula_descriptive = PropertyTypeAssignment(
        code="CHEMICAL_FORMULA_DESCRIPTIVE",
        data_type="VARCHAR",
        property_label="Chemical formula descriptive",
        description="Chemical identity supplied by the external archive.",
        mandatory=False,
        section="Chemical identity",
    )
    inchi = PropertyTypeAssignment(
        code="INCHI",
        data_type="VARCHAR",
        property_label="Inchi",
        description="Chemical identity supplied by the external archive.",
        mandatory=False,
        section="Chemical identity",
    )
    inchi_key = PropertyTypeAssignment(
        code="INCHI_KEY",
        data_type="VARCHAR",
        property_label="Inchi key",
        description="Chemical identity supplied by the external archive.",
        mandatory=False,
        section="Chemical identity",
    )
    smiles = PropertyTypeAssignment(
        code="SMILES",
        data_type="VARCHAR",
        property_label="Smiles",
        description="Chemical identity supplied by the external archive.",
        mandatory=False,
        section="Chemical identity",
    )
    pubchem_cid = PropertyTypeAssignment(
        code="PUBCHEM_CID",
        data_type="INTEGER",
        property_label="Pubchem cid",
        description="Chemical identity supplied by the external archive.",
        mandatory=False,
        section="Chemical identity",
    )
    pubchem_link = PropertyTypeAssignment(
        code="PUBCHEM_LINK",
        data_type="HYPERLINK",
        property_label="Pubchem link",
        description="Chemical identity supplied by the external archive.",
        mandatory=False,
        section="Chemical identity",
    )


class ElectrodeMaterial(MaterialV1):
    defs = ObjectTypeDef(
        code="MATERIAL_V1.ELECTRODE_MATERIAL",
        description="An ElectrodeMaterial is a prepared material intended for incorporation into an electrode.",
        generated_code_prefix="BAT",
    )
    source_record = SOURCE_RECORD
    record_datetime = p.RECORD_DATETIME
    lab_id = p.LAB_ID.model_copy(update={"mandatory": True})


class ElectrodeSheet(MaterialV1):
    defs = ObjectTypeDef(
        code="MATERIAL_V1.ELECTRODE_SHEET",
        description="An ElectrodeSheet is a sheet or stock of electrode material from which electrode samples can be prepared.",
        generated_code_prefix="BAT",
    )
    source_record = SOURCE_RECORD
    record_datetime = p.RECORD_DATETIME
    lab_id = p.LAB_ID.model_copy(update={"mandatory": True})
    thickness = p.THICKNESS
    mass = p.MASS
    length = p.LENGTH
    width = p.WIDTH
    diameter = p.DIAMETER
    area = p.AREA
    shape = p.SHAPE
    casting_procedure = p.CASTING_PROCEDURE


class ElectrolyteStock(MaterialV1):
    defs = ObjectTypeDef(
        code="MATERIAL_V1.ELECTROLYTE_STOCK",
        description="An ElectrolyteStock is a prepared electrolyte solution held as a source for electrolyte samples.",
        generated_code_prefix="BAT",
    )
    source_record = SOURCE_RECORD
    record_datetime = p.RECORD_DATETIME
    lab_id = p.LAB_ID.model_copy(update={"mandatory": True})
    volume = p.VOLUME
    mass = p.MASS


class SeparatorStock(MaterialV1):
    defs = ObjectTypeDef(
        code="MATERIAL_V1.SEPARATOR_STOCK",
        description="A SeparatorStock is separator material held as a source for separator samples.",
        generated_code_prefix="BAT",
    )
    source_record = SOURCE_RECORD
    record_datetime = p.RECORD_DATETIME
    lab_id = p.LAB_ID.model_copy(update={"mandatory": True})
    thickness = p.THICKNESS
    mass = p.MASS
    length = p.LENGTH
    width = p.WIDTH
    diameter = p.DIAMETER
    area = p.AREA
    shape = p.SHAPE
    supplier = Chemical.supplier
    lot_number = Chemical.lot_number
    product_number = p.PRODUCT_NUMBER
    shipping_datetime = p.SHIPPING_DATETIME
    opening_datetime = p.OPENING_DATETIME


class ElectrodeSample(Sample):
    defs = ObjectTypeDef(
        code="SAMPLE.ELECTRODE",
        description="An ElectrodeSample is a discrete electrode prepared for use in a cell.",
        generated_code_prefix="BAT",
    )
    source_record = SOURCE_RECORD
    record_datetime = p.RECORD_DATETIME
    lab_id = p.LAB_ID.model_copy(update={"mandatory": True})
    bam_oe = Sample.bam_oe.model_copy(update={"mandatory": False})
    thickness = p.THICKNESS
    mass = p.MASS
    length = p.LENGTH
    width = p.WIDTH
    diameter = p.DIAMETER
    area = p.AREA
    shape = p.SHAPE
    electrode_sheet = PropertyTypeAssignment(
        code="BATTERY_ELECTRODE_SHEET",
        data_type="OBJECT",
        object_code="MATERIAL_V1.ELECTRODE_SHEET",
        property_label="Electrode sheet",
        description="Referenced battery component in the indicated role.",
        mandatory=False,
        section="Battery relationships",
    )


class ElectrolyteSample(Sample):
    defs = ObjectTypeDef(
        code="SAMPLE.ELECTROLYTE",
        description="An ElectrolyteSample is a discrete portion of an electrolyte stock.",
        generated_code_prefix="BAT",
    )
    source_record = SOURCE_RECORD
    record_datetime = p.RECORD_DATETIME
    lab_id = p.LAB_ID.model_copy(update={"mandatory": True})
    bam_oe = Sample.bam_oe.model_copy(update={"mandatory": False})
    volume = p.VOLUME
    mass = p.MASS
    electrolyte_stock = PropertyTypeAssignment(
        code="BATTERY_ELECTROLYTE_STOCK",
        data_type="OBJECT",
        object_code="MATERIAL_V1.ELECTROLYTE_STOCK",
        property_label="Electrolyte stock",
        description="Referenced battery component in the indicated role.",
        mandatory=False,
        section="Battery relationships",
    )


class SeparatorSample(Sample):
    defs = ObjectTypeDef(
        code="SAMPLE.SEPARATOR",
        description="A SeparatorSample is a discrete separator prepared for use in a cell.",
        generated_code_prefix="BAT",
    )
    source_record = SOURCE_RECORD
    record_datetime = p.RECORD_DATETIME
    lab_id = p.LAB_ID.model_copy(update={"mandatory": True})
    bam_oe = Sample.bam_oe.model_copy(update={"mandatory": False})
    thickness = p.THICKNESS
    mass = p.MASS
    length = p.LENGTH
    width = p.WIDTH
    diameter = p.DIAMETER
    area = p.AREA
    shape = p.SHAPE
    separator_stock = PropertyTypeAssignment(
        code="BATTERY_SEPARATOR_STOCK",
        data_type="OBJECT",
        object_code="MATERIAL_V1.SEPARATOR_STOCK",
        property_label="Separator stock",
        description="Referenced battery component in the indicated role.",
        mandatory=False,
        section="Battery relationships",
    )


class CoinCell(Sample):
    defs = ObjectTypeDef(
        code="SAMPLE.COIN_CELL",
        description="A CoinCell is an assembled electrochemical cell identified and handled as a discrete device.",
        generated_code_prefix="BAT",
    )
    source_record = SOURCE_RECORD
    record_datetime = p.RECORD_DATETIME
    lab_id = p.LAB_ID.model_copy(update={"mandatory": True})
    bam_oe = Sample.bam_oe.model_copy(update={"mandatory": False})
    case_id = p.CASE_ID
    case_crimp = p.CASE_CRIMP
    working_electrode = PropertyTypeAssignment(
        code="BATTERY_WORKING_ELECTRODE",
        data_type="OBJECT",
        object_code="SAMPLE.ELECTRODE",
        property_label="Working electrode",
        description="Referenced battery component in the indicated role.",
        mandatory=False,
        section="Battery relationships",
    )
    counter_electrode = PropertyTypeAssignment(
        code="BATTERY_COUNTER_ELECTRODE",
        data_type="OBJECT",
        object_code="SAMPLE.ELECTRODE",
        property_label="Counter electrode",
        description="Referenced battery component in the indicated role.",
        mandatory=False,
        section="Battery relationships",
    )
    separator = PropertyTypeAssignment(
        code="BATTERY_SEPARATOR",
        data_type="OBJECT",
        object_code="SAMPLE.SEPARATOR",
        property_label="Separator",
        description="Referenced battery component in the indicated role.",
        mandatory=False,
        section="Battery relationships",
    )
    electrolyte = PropertyTypeAssignment(
        code="BATTERY_ELECTROLYTE",
        data_type="OBJECT",
        object_code="SAMPLE.ELECTROLYTE",
        property_label="Electrolyte",
        description="Referenced battery component in the indicated role.",
        mandatory=False,
        section="Battery relationships",
    )
