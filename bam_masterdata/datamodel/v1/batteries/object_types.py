# AUTO-GENERATED CLASS HIERARCHY — DO NOT EDIT
#
# ChemicalStock
#
# ElectrodeMaterial
#
# ElectrodeSheet
#
# ElectrolyteStock
#
# SeparatorStock
#
# ElectrodeSample
#
# ElectrolyteSample
#
# SeparatorSample
#
# CoinCell
#
# END AUTO-GENERATED CLASS HIERARCHY

"""Battery definitions for the observed HZB archive concepts."""

from bam_masterdata.datamodel.v1.entities import Chemical, Device, Material, Sample
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.provenance import SOURCE_RECORD

from . import properties as p


class ChemicalStock(Chemical):
    defs = ObjectTypeDef(
        code="CHEMICAL_STOCK",
        description="A ChemicalStock is a purchased chemical item held as a source for laboratory preparation.",
        generated_code_prefix="BAT",
    )
    source_record = SOURCE_RECORD
    record_datetime = p.RECORD_DATETIME
    lab_id = p.LAB_ID.model_copy(update={"mandatory": True})
    product_number = p.PRODUCT_NUMBER
    shipping_datetime = p.SHIPPING_DATETIME
    opening_datetime = p.OPENING_DATETIME
    product_weight = p.PRODUCT_WEIGHT
    product_volume = p.PRODUCT_VOLUME


class ElectrodeMaterial(Material):
    defs = ObjectTypeDef(
        code="ELECTRODE_MATERIAL",
        description="An ElectrodeMaterial is a prepared material intended for incorporation into an electrode.",
        generated_code_prefix="BAT",
    )
    source_record = SOURCE_RECORD
    record_datetime = p.RECORD_DATETIME


class ElectrodeSheet(Material):
    defs = ObjectTypeDef(
        code="ELECTRODE_SHEET",
        description="An ElectrodeSheet is a sheet or stock of electrode material from which electrode samples can be prepared.",
        generated_code_prefix="BAT",
    )
    source_record = SOURCE_RECORD
    record_datetime = p.RECORD_DATETIME
    thickness = p.THICKNESS
    mass = p.MASS
    length = p.LENGTH
    width = p.WIDTH
    diameter = p.DIAMETER
    area = p.AREA
    shape = p.SHAPE
    casting_procedure = p.CASTING_PROCEDURE


class ElectrolyteStock(Material):
    defs = ObjectTypeDef(
        code="ELECTROLYTE_STOCK",
        description="An ElectrolyteStock is a prepared electrolyte solution held as a source for electrolyte samples.",
        generated_code_prefix="BAT",
    )
    source_record = SOURCE_RECORD
    record_datetime = p.RECORD_DATETIME
    volume = p.VOLUME
    mass = p.MASS


class SeparatorStock(Material):
    defs = ObjectTypeDef(
        code="SEPARATOR_STOCK",
        description="A SeparatorStock is separator material held as a source for separator samples.",
        generated_code_prefix="BAT",
    )
    source_record = SOURCE_RECORD
    record_datetime = p.RECORD_DATETIME
    thickness = p.THICKNESS
    mass = p.MASS
    length = p.LENGTH
    width = p.WIDTH
    diameter = p.DIAMETER
    area = p.AREA
    shape = p.SHAPE
    product_number = p.PRODUCT_NUMBER
    shipping_datetime = p.SHIPPING_DATETIME
    opening_datetime = p.OPENING_DATETIME


class ElectrodeSample(Sample):
    defs = ObjectTypeDef(
        code="ELECTRODE_SAMPLE",
        description="An ElectrodeSample is a discrete electrode prepared for use in a cell.",
        generated_code_prefix="BAT",
    )
    source_record = SOURCE_RECORD
    record_datetime = p.RECORD_DATETIME
    thickness = p.THICKNESS
    mass = p.MASS
    length = p.LENGTH
    width = p.WIDTH
    diameter = p.DIAMETER
    area = p.AREA
    shape = p.SHAPE
    electrode_sheet = PropertyTypeAssignment(
        code="ELECTRODE_SHEET",
        data_type="OBJECT",
        object_code="ELECTRODE_SHEET",
        property_label="Electrode sheet",
        description="Referenced battery component in the indicated role.",
        mandatory=False,
        section="Battery relationships",
    )


class ElectrolyteSample(Sample):
    defs = ObjectTypeDef(
        code="ELECTROLYTE_SAMPLE",
        description="An ElectrolyteSample is a discrete portion of an electrolyte stock.",
        generated_code_prefix="BAT",
    )
    source_record = SOURCE_RECORD
    record_datetime = p.RECORD_DATETIME
    volume = p.VOLUME
    mass = p.MASS
    electrolyte_stock = PropertyTypeAssignment(
        code="ELECTROLYTE_STOCK",
        data_type="OBJECT",
        object_code="ELECTROLYTE_STOCK",
        property_label="Electrolyte stock",
        description="Referenced battery component in the indicated role.",
        mandatory=False,
        section="Battery relationships",
    )


class SeparatorSample(Sample):
    defs = ObjectTypeDef(
        code="SEPARATOR_SAMPLE",
        description="A SeparatorSample is a discrete separator prepared for use in a cell.",
        generated_code_prefix="BAT",
    )
    source_record = SOURCE_RECORD
    record_datetime = p.RECORD_DATETIME
    thickness = p.THICKNESS
    mass = p.MASS
    length = p.LENGTH
    width = p.WIDTH
    diameter = p.DIAMETER
    area = p.AREA
    shape = p.SHAPE
    separator_stock = PropertyTypeAssignment(
        code="SEPARATOR_STOCK",
        data_type="OBJECT",
        object_code="SEPARATOR_STOCK",
        property_label="Separator stock",
        description="Referenced battery component in the indicated role.",
        mandatory=False,
        section="Battery relationships",
    )


class CoinCell(Device):
    defs = ObjectTypeDef(
        code="COIN_CELL",
        description="A CoinCell is an assembled electrochemical cell identified and handled as a discrete device.",
        generated_code_prefix="BAT",
    )
    source_record = SOURCE_RECORD
    record_datetime = p.RECORD_DATETIME
    lab_id = p.LAB_ID.model_copy(update={"mandatory": True})
    case_id = p.CASE_ID
    case_crimp = p.CASE_CRIMP
    working_electrode = PropertyTypeAssignment(
        code="WORKING_ELECTRODE",
        data_type="OBJECT",
        object_code="ELECTRODE_SAMPLE",
        property_label="Working electrode",
        description="Referenced battery component in the indicated role.",
        mandatory=False,
        section="Battery relationships",
    )
    counter_electrode = PropertyTypeAssignment(
        code="COUNTER_ELECTRODE",
        data_type="OBJECT",
        object_code="ELECTRODE_SAMPLE",
        property_label="Counter electrode",
        description="Referenced battery component in the indicated role.",
        mandatory=False,
        section="Battery relationships",
    )
    separator = PropertyTypeAssignment(
        code="SEPARATOR",
        data_type="OBJECT",
        object_code="SEPARATOR_SAMPLE",
        property_label="Separator",
        description="Referenced battery component in the indicated role.",
        mandatory=False,
        section="Battery relationships",
    )
    electrolyte = PropertyTypeAssignment(
        code="ELECTROLYTE",
        data_type="OBJECT",
        object_code="ELECTROLYTE_SAMPLE",
        property_label="Electrolyte",
        description="Referenced battery component in the indicated role.",
        mandatory=False,
        section="Battery relationships",
    )
