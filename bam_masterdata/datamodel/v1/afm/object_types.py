# AUTO-GENERATED CLASS HIERARCHY — DO NOT EDIT
#
# AFMTipBox
#
# AFMTip
#
# END AUTO-GENERATED CLASS HIERARCHY

from bam_masterdata.datamodel.v1.entities import PhysicalObject
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment

# TIP_CLASS is assigned to both AFMTipBox and AFMTip and must share identical global metadata.
_TIP_CLASS_LABEL = "Tip class"
_TIP_CLASS_DESCRIPTION = (
    "Compact, human-readable classification code of an AFM probe according to its mechanical and "
    "geometrical properties, in the form Kc_Tip_phys(_Material), for example F_S09_N_Si."
)


class AFMTipBox(PhysicalObject):
    defs = ObjectTypeDef(
        code="AFM_TIP_BOX",
        description="Physical box or package supplied by the manufacturer, containing one or more "
        "AFM probes (also called tips, cantilevers or chips).",
        description_de="Physische Box bzw. Verpackung des Herstellers mit einer oder mehreren "
        "AFM-Sonden (auch Spitzen, Cantilever oder Chips genannt).",
        generated_code_prefix="ATB",
    )

    # General

    responsible_persons = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON",
        property_label="Responsible person",
        description="Responsible persons.",
        mandatory=True,
        multivalued=True,
        section="General",
        prev_versions=["RESPONSIBLE_PERSON:v0"],
    )

    manufacturer_info = PropertyTypeAssignment(
        code="MANUFACTURER_INFO",
        data_type="VARCHAR",
        property_label="Manufacturer info",
        description="Manufacturer information on the AFM tips in the box.",
        mandatory=True,
        section="General",
    )

    tip_class = PropertyTypeAssignment(
        code="TIP_CLASS",
        data_type="VARCHAR",
        property_label=_TIP_CLASS_LABEL,
        description=_TIP_CLASS_DESCRIPTION,
        mandatory=True,
        section="General",
    )

    premounted_type = PropertyTypeAssignment(
        code="PREMOUNTED_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="PREMOUNTED_TYPE",
        property_label="Premounted / AFM-specific",
        description="AFM tip compatibility class.",
        mandatory=True,
        section="General",
    )

    # Geometry

    base_shape = PropertyTypeAssignment(
        code="BASE_SHAPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BASE_SHAPE",
        property_label="Base shape",
        description="Cantilever base geometry.",
        mandatory=True,
        section="Geometry",
    )

    tip_shape = PropertyTypeAssignment(
        code="TIP_SHAPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TIP_SHAPE",
        property_label="Tip shape",
        description="AFM tip geometry.",
        mandatory=True,
        section="Geometry",
    )

    base_material = PropertyTypeAssignment(
        code="BASE_MATERIAL",
        data_type="VARCHAR",
        property_label="Base material",
        description="Material of the probe base (cantilever or support chip).",
        mandatory=False,
        section="Geometry",
    )

    tip_material = PropertyTypeAssignment(
        code="TIP_MATERIAL",
        data_type="VARCHAR",
        property_label="Tip material",
        description="Material of the AFM tip.",
        mandatory=False,
        section="Geometry",
    )

    tip_coating = PropertyTypeAssignment(
        code="TIP_COATING",
        data_type="VARCHAR",
        property_label="Tip coating",
        description="Coating of the AFM tip.",
        mandatory=False,
        section="Geometry",
    )

    detector_coating = PropertyTypeAssignment(
        code="DETECTOR_COATING",
        data_type="VARCHAR",
        property_label="Detector coating",
        description="Reflective coating on the back of the cantilever, used for optical "
        "beam-deflection detection.",
        mandatory=False,
        section="Geometry",
    )

    # Dimensions

    cantilever_thickness = PropertyTypeAssignment(
        code="CANTILEVER_THICKNESS",
        data_type="REAL",
        property_label="Thickness",
        description="Thickness of the cantilever.",
        units="um",
        mandatory=True,
        section="Dimensions",
    )

    cantilever_thickness_error = PropertyTypeAssignment(
        code="CANTILEVER_THICKNESS_ERROR",
        data_type="REAL",
        property_label="Thickness error",
        description="Error of the cantilever thickness.",
        units="um",
        mandatory=False,
        section="Dimensions",
    )

    cantilever_length = PropertyTypeAssignment(
        code="CANTILEVER_LENGTH",
        data_type="REAL",
        property_label="Length",
        description="Length of the cantilever.",
        units="um",
        mandatory=True,
        section="Dimensions",
    )

    cantilever_length_error = PropertyTypeAssignment(
        code="CANTILEVER_LENGTH_ERROR",
        data_type="REAL",
        property_label="Length error",
        description="Error of the cantilever length.",
        units="um",
        mandatory=False,
        section="Dimensions",
    )

    cantilever_width = PropertyTypeAssignment(
        code="CANTILEVER_WIDTH",
        data_type="REAL",
        property_label="Width",
        description="Width of the cantilever.",
        units="um",
        mandatory=False,
        section="Dimensions",
    )

    cantilever_width_error = PropertyTypeAssignment(
        code="CANTILEVER_WIDTH_ERROR",
        data_type="REAL",
        property_label="Width error",
        description="Error of the cantilever width.",
        units="um",
        mandatory=False,
        section="Dimensions",
    )

    # Mechanical

    spring_constant_low = PropertyTypeAssignment(
        code="SPRING_CONSTANT_LOW",
        data_type="REAL",
        property_label="Spring constant low",
        description="Lower value of the spring constant.",
        units="N/m",
        mandatory=True,
        section="Mechanical",
    )

    spring_constant_high = PropertyTypeAssignment(
        code="SPRING_CONSTANT_HIGH",
        data_type="REAL",
        property_label="Spring constant high",
        description="Upper value of the spring constant.",
        units="N/m",
        mandatory=True,
        section="Mechanical",
    )

    resonance_frequency_low = PropertyTypeAssignment(
        code="RESONANCE_FREQUENCY_LOW",
        data_type="REAL",
        property_label="Resonance frequency low",
        description="Lower value of the resonance frequency.",
        units="kHz",
        mandatory=True,
        section="Mechanical",
    )

    resonance_frequency_high = PropertyTypeAssignment(
        code="RESONANCE_FREQUENCY_HIGH",
        data_type="REAL",
        property_label="Resonance frequency high",
        description="Upper value of the resonance frequency.",
        units="kHz",
        mandatory=True,
        section="Mechanical",
    )

    # Sharp probes

    tip_height_low = PropertyTypeAssignment(
        code="TIP_HEIGHT_LOW",
        data_type="REAL",
        property_label="Tip height low",
        description="Lower value of the tip height of sharp probes.",
        units="um",
        mandatory=False,
        section="Sharp Probes",
    )

    tip_height_high = PropertyTypeAssignment(
        code="TIP_HEIGHT_HIGH",
        data_type="REAL",
        property_label="Tip height high",
        description="Upper value of the tip height of sharp probes.",
        units="um",
        mandatory=False,
        section="Sharp Probes",
    )

    tip_radius_low = PropertyTypeAssignment(
        code="TIP_RADIUS_LOW",
        data_type="REAL",
        property_label="Tip radius low",
        description="Lower value of the tip radius of sharp probes.",
        units="nm",
        mandatory=False,
        section="Sharp Probes",
    )

    tip_radius_high = PropertyTypeAssignment(
        code="TIP_RADIUS_HIGH",
        data_type="REAL",
        property_label="Tip radius high",
        description="Upper value of the tip radius of sharp probes.",
        units="nm",
        mandatory=False,
        section="Sharp Probes",
    )

    # Colloidal probes

    particle_diameter = PropertyTypeAssignment(
        code="PARTICLE_DIAMETER",
        data_type="REAL",
        property_label="Particle diameter",
        description="Particle diameter of colloidal probes.",
        units="um",
        mandatory=False,
        section="Colloidal Probes",
    )

    particle_diameter_tolerance = PropertyTypeAssignment(
        code="PARTICLE_DIAMETER_TOLERANCE",
        data_type="REAL",
        property_label="Particle diameter tolerance",
        description="Tolerance of the particle diameter of colloidal probes.",
        units="um",
        mandatory=False,
        section="Colloidal Probes",
    )

    particle_material = PropertyTypeAssignment(
        code="PARTICLE_MATERIAL",
        data_type="VARCHAR",
        property_label="Particle material",
        description="Particle material of colloidal probes.",
        mandatory=False,
        section="Colloidal Probes",
    )

    # Inventory

    lab = PropertyTypeAssignment(
        code="LAB",
        data_type="VARCHAR",
        property_label="Lab",
        description="Lab where the AFM tip box is kept.",
        mandatory=True,
        section="Inventory",
    )

    storage_compartment = PropertyTypeAssignment(
        code="STORAGE_COMPARTMENT",
        data_type="VARCHAR",
        property_label="Storage compartment",
        description="Storage compartment of the AFM tip box.",
        mandatory=True,
        section="Inventory",
    )

    number_of_tips = PropertyTypeAssignment(
        code="NUMBER_OF_TIPS",
        data_type="INTEGER",
        property_label="Number of tips",
        description="Number of AFM tips in the box.",
        mandatory=True,
        section="Inventory",
    )


class AFMTip(PhysicalObject):
    defs = ObjectTypeDef(
        code="AFM_TIP",
        description="Individual AFM tip originating from an AFM tip box, tracked individually "
        "throughout its lifecycle.",
        description_de="Einzelne AFM-Spitze aus einer AFM-Spitzenbox, die über ihren gesamten "
        "Lebenszyklus einzeln verfolgt wird.",
        generated_code_prefix="ATT",
    )

    tip_box = PropertyTypeAssignment(
        code="TIP_BOX",
        data_type="OBJECT",
        object_code="AFM_TIP_BOX",
        property_label="Parent AFM Tip Box",
        description="AFM tip box this tip originates from.",
        mandatory=True,
        section="General",
    )

    tip_number = PropertyTypeAssignment(
        code="TIP_NUMBER",
        data_type="INTEGER",
        property_label="Tip number",
        description="Number of the tip within its AFM tip box.",
        mandatory=True,
        section="General",
    )

    cantilever_variant = PropertyTypeAssignment(
        code="CANTILEVER_VARIANT",
        data_type="VARCHAR",
        property_label="Cantilever variant",
        description="Cantilever variant of the tip, for chips with several cantilevers "
        "(for example A, B or C).",
        mandatory=False,
        section="General",
    )

    # Own TIP_CLASS so that a modified tip can differ from its original box specification.
    tip_class = PropertyTypeAssignment(
        code="TIP_CLASS",
        data_type="VARCHAR",
        property_label=_TIP_CLASS_LABEL,
        description=_TIP_CLASS_DESCRIPTION,
        mandatory=True,
        section="General",
    )

    # Lifecycle

    afm_tip_status = PropertyTypeAssignment(
        code="AFM_TIP_STATUS",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="AFM_TIP_STATUS",
        property_label="Status",
        description="Lifecycle status of the AFM tip.",
        mandatory=True,
        section="Lifecycle",
    )

    archive_location = PropertyTypeAssignment(
        code="ARCHIVE_LOCATION",
        data_type="VARCHAR",
        property_label="Archive location",
        description="Archive location of the AFM tip.",
        mandatory=False,
        section="Lifecycle",
    )
