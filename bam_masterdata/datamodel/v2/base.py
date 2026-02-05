from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.entities import ObjectType

# A list of deprecated ObjectType codes that should not be used in new data entries. This can be used to
# maintain backward compatibility while signaling to users that certain types are no longer recommended for use.
deprecated_or_unused = ["RAW_MATERIAL.STEEL", "RAW_MATERIAL.ALUMINIUM"]


class BaseEntity(ObjectType):
    defs = ObjectTypeDef(
        code="BASE_ENTITY",
        description="""
        A BaseEntity is an entity that encompasses both material and immaterial
        existents, serving as the foundational type from which all domain-specific
        entities are derived.
        """,
        iri="https://bam.de/masterdata/BaseEntity",
        references=["http://purl.obolibrary.org/obo/BFO_0000001"],
        generated_code_prefix="BASE_ENTIT",
        aliases=[],
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        section="General Information",
    )

    def normalize(self):
        pass


class Activity(BaseEntity):
    defs = ObjectTypeDef(
        code="ACTIVITY",
        description="""
        An Activity is something that occurs over a period of time and acts upon or with
        entities; it may include consuming, processing, transforming, modifying,
        relocating, using, or generating entities.
        """,
        iri="https://bam.de/masterdata/Activity",
        references=[
            "http://purl.obolibrary.org/obo/BFO_0000015",
            "https://www.w3.org/TR/prov-o/#Activity",
        ],
        generated_code_prefix="ACTIV",
        aliases=[],
        previous_versions=["EXPERIMENTAL_STEP"],
    )


class Analysis(Activity):
    defs = ObjectTypeDef(
        code="ANALYSIS",
        description="""
        An Analysis is an activity that interprets existing data to derive new data, such
        as properties, patterns, or parameters
        """,
        iri="https://bam.de/masterdata/Analysis",
        generated_code_prefix="ANALI",
        aliases=[],
        previous_versions=[],
    )


class Calibration(Activity):
    defs = ObjectTypeDef(
        code="CALIBRATION",
        description="""
        A Calibration is an activity that establishes or adjusts the mapping between
        measurement outputs and reference standards.
        """,
        iri="https://bam.de/masterdata/Calibration",
        generated_code_prefix="CALIB",
        aliases=[],
        previous_versions=[],
    )


class Measurement(Activity):
    defs = ObjectTypeDef(
        code="MEASUREMENT",
        description="""
        A Measurement is an activity that uses an experimental device to produce quantitative
        or qualitative data about the properties of a material.
        """,
        iri="https://bam.de/masterdata/Measurement",
        generated_code_prefix="MEASU",
        aliases=[],
        previous_versions=[],
    )


class Processing(Activity):
    defs = ObjectTypeDef(
        code="PROCESSING",
        description="""
        A Processing is an activity that alters the structure, composition, or form of a
        material.
        """,
        iri="https://bam.de/masterdata/Processing",
        generated_code_prefix="PROCE",
        aliases=[],
        previous_versions=[],
    )


class Simulation(Activity):
    defs = ObjectTypeDef(
        code="SIMULATION",
        description="""
        A Simulation is an activity that uses computational models to replicate or
        predict the behavior of a material.
        """,
        iri="https://bam.de/masterdata/Simulation",
        generated_code_prefix="SIMUL",
        aliases=[],
        previous_versions=[],
    )


class Synthesis(Activity):
    defs = ObjectTypeDef(
        code="SYNTHESIS",
        description="""
        A Synthesis is an activity that creates or assembles materials through chemical or
        physical means.
        """,
        iri="https://bam.de/masterdata/Synthesis",
        generated_code_prefix="SYNTH",
        aliases=[],
        previous_versions=[],
    )


class Test(Activity):
    defs = ObjectTypeDef(
        code="TEST",
        description="""
        A Test is an activity that subjects materials to specific conditions to evaluate
        their performance, reliability, or compliance with certain standards.
        """,
        iri="https://bam.de/masterdata/Test",
        generated_code_prefix="TEST",
        aliases=[],
        previous_versions=[],
    )


class Entity(BaseEntity):
    defs = ObjectTypeDef(
        code="ENTITY",
        description="""
        An Entity is a physical, digital, conceptual, or other kind of thing with some fixed
        aspects; entities may be real or imaginary.
        """,
        iri="https://bam.de/masterdata/Entity",
        references=[
            "http://purl.obolibrary.org/obo/BFO_0000002",
            "https://www.w3.org/TR/prov-o/#Entity",
        ],
        generated_code_prefix="ENTIT",
        aliases=[],
        previous_versions=[],
    )


class InformationObject(Entity):
    defs = ObjectTypeDef(
        code="INFORMATION_OBJECT",
        description="""
        An InformationObject is an (information content) entity that represents, describes,
        or encodes knowledge about systems, instruments, or activities. It may be produced
        by processes or used as input for interpretation, automation, or modelling.
        """,
        iri="https://bam.de/masterdata/InformationObject",
        references=[
            "http://purl.obolibrary.org/obo/IAO_0000030",
        ],
        generated_code_prefix="INFOR_OBJEC",
        aliases=[],
        previous_versions=[],
    )


class MaterialEntity(Entity):
    defs = ObjectTypeDef(
        code="MATERIAL_ENTITY",
        description="""
        A MaterialEntity is an (independent continuant) entity that has some portion of matter as a
        proper or improper continuant part, and persists through time while possibly gaining
        or losing parts.
        """,
        iri="https://bam.de/masterdata/MaterialEntity",
        references=[
            "http://purl.obolibrary.org/obo/BFO_0000040",
        ],
        generated_code_prefix="MATER_ENTIT",
        aliases=[],
        previous_versions=[],
    )


class Material(MaterialEntity):
    defs = ObjectTypeDef(
        code="MATERIAL",
        description="""
        A Material is a material entity that is composed of a physical substance or mixture of
        substances that is characterized by its chemical composition, structure, and properties.
        """,
        iri="https://bam.de/masterdata/Material",
        references=[],
        generated_code_prefix="MATER",
        aliases=[],
        previous_versions=[],
    )


class Instrument(MaterialEntity):
    defs = ObjectTypeDef(
        code="INSTRUMENT",
        description="""
        An Instrument is a material entity that is designed or used to support an activity by
        measuring, modifying, or interacting with other entities such as systems and organisms.
        """,
        iri="https://bam.de/masterdata/Instrument",
        references=[
            "http://purl.obolibrary.org/obo/OBI_0000968",
        ],
        generated_code_prefix="INSTR",
        aliases=[],
        previous_versions=[],
    )


class Sample(MaterialEntity):
    defs = ObjectTypeDef(
        code="SAMPLE",
        description="""
        A Sample is a material entity that is collected for potential use as an input upon
        which measurements or observations are performed.
        """,
        iri="https://bam.de/masterdata/Sample",
        references=[
            "http://purl.obolibrary.org/obo/OBI_0100051",
        ],
        generated_code_prefix="SAMPL",
        aliases=[],
        previous_versions=[],
    )


class Organism(MaterialEntity):
    defs = ObjectTypeDef(
        code="ORGANISM",
        description="""
        An Organism is a material entity that is an individual living system, such as animal,
        plant, bacteria or virus, that is capable of replicating or reproducing, growth
        and maintenance in the right environment. An organism may be unicellular or made up,
        like humans, of many billions of cells divided into specialized tissues and organs.
        """,
        iri="https://bam.de/masterdata/Organism",
        references=[
            "http://purl.obolibrary.org/obo/OBI_0100026",
        ],
        generated_code_prefix="ORGAN",
        aliases=[],
        previous_versions=[],
    )
