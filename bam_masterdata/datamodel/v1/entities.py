from bam_masterdata.datamodel.v1.base_objects import Entity
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment


class Context(Entity):
    defs = ObjectTypeDef(
        code="CONTEXT",
        description="A Context is an entity that represents information about "
        "entities or activities and provides descriptive, configurational, or classificatory context.",
        generated_code_prefix="CONTX",
        iri=["http://purl.obolibrary.org/obo/IAO_0000030"],
    )


class Software(Context):
    defs = ObjectTypeDef(
        code="SOFTWARE",
        description="A Software is a context that specifies a computer program or library, in a given version, which "
        "can be executed to carry out a computational activity.",
        generated_code_prefix="SOFTW",
        iri=["http://purl.obolibrary.org/obo/IAO_0000010"],
        prev_versions=["SOFTWARE_CODE:v0"],
    )

    version = PropertyTypeAssignment(
        code="VERSION",
        data_type="VARCHAR",
        property_label="Version",
        description="Version identifier of the entity, such as a release number or a date.",
        mandatory=False,
        section="Software Details",
        prev_versions=["VERSION:v0"],
    )

    license = PropertyTypeAssignment(
        code="LICENSE",
        data_type="VARCHAR",
        property_label="License",
        description="License under which the entity is distributed.",
        mandatory=False,
        section="Software Details",
        prev_versions=["LICENSE:v0"],
    )

    link = PropertyTypeAssignment(
        code="LINK",
        data_type="HYPERLINK",
        property_label="Link",
        description="Link to the repository or publication relevant for the software.",
        mandatory=False,
        section="Software Details",
        prev_versions=["SOURCE_LINK:v0"],
    )

    # Properties from v0 that need to be migrated to v1 (from SOFTWARE_CODE:v0):
    # SOFTWARE_NAME
    # REFERENCE


class ParameterSet(Context):
    defs = ObjectTypeDef(
        code="PARAMETER_SET",
        description="A ParameterSet is a context that specifies a set of parameters, which can be used to configure "
        "an activity or an entity.",
        generated_code_prefix="PARAM_SET",
        prev_versions=["PARAMETER_SET:v0"],
    )

    generic_parameters = PropertyTypeAssignment(
        code="GENERIC_PARAMETERS",
        data_type="JSON",
        property_label="Generic Parameters",
        description="A JSON object containing generic parameters.",
        mandatory=False,
        section="Parameter Set Details",
    )

    # Properties from v0 that need to be migrated to v1 (from PARAMETER_SET:v0):
    # PARAMETER_SET.SPREADSHEET


class Classification(Context):
    defs = ObjectTypeDef(
        code="CLASSIFICATION",
        description="A Classification is a context that specifies a category, or label which can be "
        "used to classify entities or activities.",
        generated_code_prefix="CLASSIF",
    )


class Document(Context):
    defs = ObjectTypeDef(
        code="DOCUMENT",
        description="A Document is a context that specifies a document, which can be used to provide "
        "information about entities or activities.",
        generated_code_prefix="DOCUM",
        prev_versions=["DOCUMENT:v0"],
    )

    document_type = PropertyTypeAssignment(
        code="DOCUMENT_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DOCUMENT_TYPE",
        property_label="Document Type",
        description="Type of the document, such as a publication, a report, or a protocol.",
        mandatory=False,
        section="Document Details",
        prev_versions=["DOCUMENT_TYPE:v0"],
    )

    version = PropertyTypeAssignment(
        code="VERSION",
        data_type="VARCHAR",
        property_label="Version",
        description="Version identifier of the entity, such as a release number or a date.",
        mandatory=False,
        section="Document Details",
        prev_versions=["VERSION:v0"],
    )

    authors = PropertyTypeAssignment(
        code="AUTHOR",
        data_type="VARCHAR",
        property_label="Authors",
        description="Author of the entity.",
        mandatory=False,
        section="Document Details",
        # multivalued=True,  # ! no multivalued VARCHAR (check openBIS 7 property type)
        prev_versions=["AUTHOR:v0"],
    )


class InventoryInformation(Context):
    defs = ObjectTypeDef(
        code="INVENTORY_INFORMATION",
        description="An InventoryInformation is context that represents information about the storage, supply, "
        "availability, identification, or inventory state of an entity.",
        generated_code_prefix="INV_INFO",
    )

    manufacturer = PropertyTypeAssignment(
        code="MANUFACTURER",
        data_type="VARCHAR",
        property_label="Manufacturer",
        description="Organization that manufactured the item.",
        mandatory=False,
        section="Supply Information",
        prev_versions=["MANUFACTURER:v0"],
    )

    supplier = PropertyTypeAssignment(
        code="SUPPLIER",
        data_type="VARCHAR",
        property_label="Supplier",
        description="Organization that supplied the item.",
        mandatory=False,
        section="Supply Information",
        prev_versions=["SUPPLIER:v0"],
    )

    lot_number = PropertyTypeAssignment(
        code="LOT_NUMBER",
        data_type="VARCHAR",
        property_label="Lot number",
        description="Manufacturer or supplier batch/lot identifier.",
        mandatory=False,
        section="Supply Information",
        prev_versions=["LOT_NUMBER:v0"],
    )

    location = PropertyTypeAssignment(
        code="LOCATION",
        data_type="OBJECT",
        object_code="LOCATION",
        property_label="Location",
        description="Current physical location of the inventory item.",
        mandatory=False,
        section="Inventory Details",
    )

    responsible_persons = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON",
        property_label="Responsible person",
        description="Persons responsible for the inventory item.",
        mandatory=False,
        multivalued=True,
        section="Inventory Details",
        prev_versions=["RESPONSIBLE_PERSON:v0"],
    )

    date_bottling = PropertyTypeAssignment(
        code="DATE_BOTTLING",
        data_type="DATE",
        property_label="Bottling date",
        description="Date on which the material was bottled.",
        mandatory=False,
        section="Inventory Details",
        prev_versions=["DATE_BOTTLING:v0"],
    )

    date_opening = PropertyTypeAssignment(
        code="DATE_OPENING",
        data_type="DATE",
        property_label="Opening date",
        description="Date on which the container was first opened.",
        mandatory=False,
        section="Inventory Details",
        prev_versions=["DATE_OPENING:v0"],
    )

    date_expiration = PropertyTypeAssignment(
        code="DATE_EXPIRATION",
        data_type="DATE",
        property_label="Expiration date",
        description="Date after which the material should not be used.",
        mandatory=False,
        section="Inventory Details",
        prev_versions=["DATE_EXPIRATION:v0"],
    )

    is_empty = PropertyTypeAssignment(
        code="IS_EMPTY",
        data_type="BOOLEAN",
        property_label="Is empty",
        description="Whether the inventory item has been depleted.",
        mandatory=False,
        section="Inventory Details",
        prev_versions=["SUBSTANCE_EMPTY:v0"],
    )


class Location(Entity):
    defs = ObjectTypeDef(
        code="LOCATION",
        description="A Location is an entity that specifies a physical or spatial place, which can be used to "
        "describe where an entity is located or where an activity takes place.",
        generated_code_prefix="LOCAT",
        iri=["http://purl.obolibrary.org/obo/BFO_0000030"],
    )

    coordinates = PropertyTypeAssignment(
        code="COORDINATES",
        data_type="JSON",
        property_label="Coordinates",
        description="Coordinates of the location, defined by latitude and longitude.",
        mandatory=False,
        section="Location Details",
    )


class MaterialEntity(Entity):
    defs = ObjectTypeDef(
        code="MATERIAL_ENTITY",
        description="A MaterialEntity is an entity that has some portion of matter as a proper or improper "
        "continuant part, and persists through time while possibly gaining or losing parts.",
        generated_code_prefix="MAT_ENT",
        iri=["http://purl.obolibrary.org/obo/BFO_0000040"],
    )


class Organism(MaterialEntity):
    defs = ObjectTypeDef(
        code="ORGANISM",
        description="An Organism is a material entity that is a living system, capable of growth, reproduction, "
        "and response to stimuli.",
        generated_code_prefix="ORGANI",
        prev_versions=["ORGANISM:v0"],
    )


class Animal(Organism):
    defs = ObjectTypeDef(
        code="ANIMAL",
        description="An Animal is an organism that is a member of the kingdom Animalia, characterized by "
        "multicellularity, heterotrophy, and motility.",
        generated_code_prefix="ANIMAL",
    )


class Person(Animal):
    defs = ObjectTypeDef(
        code="PERSON",
        description="A Person is an animal that is a member of the species Homo sapiens.",
        generated_code_prefix="PERSON",
        prev_versions=["PERSON:v0"],
    )

    given_name = PropertyTypeAssignment(
        code="GIVEN_NAME",
        data_type="VARCHAR",
        property_label="Given Name",
        description="The given name of the person.",
        mandatory=True,
        section="Personal Details",
        prev_versions=["GIVEN_NAME:v0"],
    )

    family_name = PropertyTypeAssignment(
        code="FAMILY_NAME",
        data_type="VARCHAR",
        property_label="Family Name",
        description="The family name of the person.",
        mandatory=True,
        section="Personal Details",
        prev_versions=["FAMILY_NAME:v0"],
    )

    affiliation = PropertyTypeAssignment(
        code="AFFILIATION",
        data_type="VARCHAR",
        property_label="Affiliation",
        description="The affiliation of the person.",
        mandatory=True,
        section="Personal Details",
        prev_versions=["AFFILIATION:v0"],
    )

    email = PropertyTypeAssignment(
        code="EMAIL",
        data_type="VARCHAR",
        property_label="Email",
        description="The email address of the person.",
        mandatory=False,
        section="Personal Details",
        prev_versions=["EMAIL:v0"],
    )

    telephone = PropertyTypeAssignment(
        code="TELEPHONE",
        data_type="VARCHAR",
        property_label="Telephone",
        description="The telephone number of the person.",
        mandatory=False,
        section="Personal Details",
        prev_versions=["TELEPHONE:v0"],
    )

    address = PropertyTypeAssignment(
        code="ADDRESS",
        data_type="MULTILINE_VARCHAR",
        property_label="Address",
        description="The postal address of the person.",
        mandatory=False,
        section="Personal Details",
        prev_versions=["ADDRESS:v0"],
    )

    orcid = PropertyTypeAssignment(
        code="ORCID",
        data_type="VARCHAR",
        property_label="ORCID",
        description="The ORCID identifier of the person.",
        mandatory=False,
        section="Personal Details",
    )

    person_role = PropertyTypeAssignment(
        code="PERSON_ROLE",
        data_type="VARCHAR",
        property_label="Role",
        description="The role of the person in the context of a project or activity.",
        mandatory=False,
        section="Personal Details",
    )


class BAMPerson(Person):
    defs = ObjectTypeDef(
        code="BAM_PERSON",
        description="A BAMPerson is a person that is affiliated with the Bundesanstalt für Materialforschung und -prüfung (BAM).",
        generated_code_prefix="BAM_PERSON",
    )

    bam_oe = PropertyTypeAssignment(
        code="BAM_OE",
        data_type="VARCHAR",
        property_label="BAM Organizational Unit",
        description="The organizational unit of the person within BAM.",
        mandatory=False,
        section="Personal Details",
    )

    bam_username = PropertyTypeAssignment(
        code="BAM_USERNAME",
        data_type="VARCHAR",
        property_label="BAM Username",
        description="The username of the person within BAM's IT systems.",
        mandatory=False,
        section="Personal Details",
    )

    bam_data_store_status = PropertyTypeAssignment(
        code="BAM_DATA_STORE_STATUS",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_DATA_STORE_STATUS",
        property_label="BAM Data Store Status",
        description="The status of the person's data in BAM's data store, such as active or inactive.",
        mandatory=False,
        section="Personal Details",
    )


class Device(MaterialEntity):
    defs = ObjectTypeDef(
        code="DEVICE",
        description="A Device is a material entity that is designed and/or used to perform a technical function.",
        generated_code_prefix="DEVIC",
        iri=["https://w3id.org/pmd/co/PMD_0000602"],
    )

    manufacturer = PropertyTypeAssignment(
        code="MANUFACTURER",
        data_type="VARCHAR",
        property_label="Manufacturer",
        description="Organization that manufactured the device.",
        mandatory=False,
        section="Device Details",
        prev_versions=["MANUFACTURER:v0"],
    )

    supplier = PropertyTypeAssignment(
        code="SUPPLIER",
        data_type="VARCHAR",
        property_label="Supplier",
        description="Organization that supplied the device.",
        mandatory=False,
        section="Device Details",
        prev_versions=["SUPPLIER:v0"],
    )

    device_model_name = PropertyTypeAssignment(
        code="DEVICE_MODEL_NAME",
        data_type="VARCHAR",
        property_label="Device model",
        description="Manufacturer's model designation of the device.",
        mandatory=False,
        section="Device Details",
        prev_versions=["DEVICE_MODEL_NAME:v0"],
    )

    serial_number = PropertyTypeAssignment(
        code="SERIAL_NUMBER",
        data_type="VARCHAR",
        property_label="Serial number",
        description="Manufacturer-assigned serial number of the device.",
        mandatory=False,
        section="Device Details",
        prev_versions=["SERIAL_NUMBER:v0"],
    )

    mac_address = PropertyTypeAssignment(
        code="MAC_ADDRESS",
        data_type="VARCHAR",
        property_label="MAC address",
        description="Network interface MAC address of the device.",
        mandatory=False,
        section="Device Details",
        prev_versions=["MAC_ADDRESS:v0"],
    )

    location = PropertyTypeAssignment(
        code="LOCATION",
        data_type="OBJECT",
        object_code="LOCATION",
        property_label="Location",
        description="Current physical location of the device.",
        mandatory=False,
        section="Inventory Details",
    )

    responsible_persons = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON",
        property_label="Responsible persons",
        description="Persons responsible for the device.",
        mandatory=False,
        multivalued=True,
        section="Inventory Details",
        prev_versions=["RESPONSIBLE_PERSON:v0"],
    )

    device_status = PropertyTypeAssignment(
        code="DEVICE_STATUS",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DEVICE_STATUS",
        property_label="Device status",
        description="Current operational or availability status of the device.",
        mandatory=False,
        section="Inventory Details",
        prev_versions=["INSTRUMENT_STATUS:v0"],
    )

    # Properties from v0 that need to be migrated to v1 (from DEVICE:v0):
    # DFG_DEVICE_CODE
    # INVENTORY_NO
    # INVENTORY_NO_ADD


class Sample(MaterialEntity):
    defs = ObjectTypeDef(
        code="SAMPLE",
        description="A Sample is a material entity that is identified and treated as a discrete unit as input "
        "and/or output in the context of a scientific activity.",
        generated_code_prefix="SAMP",
        prev_versions=["AUXILIARY_MATERIAL:v0", "SAMPLE:v0"],
    )

    sample_id = PropertyTypeAssignment(
        code="SAMPLE_ID",
        data_type="VARCHAR",
        property_label="Sample ID",
        description="The identifier of the sample.",
        mandatory=True,
        section="Sample Details",
        prev_versions=["SAMPLE_ID:v0"],
    )

    location = PropertyTypeAssignment(
        code="LOCATION",
        data_type="OBJECT",
        object_code="LOCATION",
        property_label="Location",
        description="Current physical location of the inventory item.",
        mandatory=False,
        section="Sample Details",
    )

    responsible_persons = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON",
        property_label="Responsible Persons",
        description="The persons responsible for the sample.",
        mandatory=False,
        section="Sample Details",
        multivalued=True,
    )

    # Properties from v0 that need to be migrated to v1 (from SAMPLE:v0):
    # SAMPLE_ID_NUMBER
    # MANUFACTURER
    # BARCODE_EXTERNAL
    # SUPPLIER
    # PHYSICAL_STATE

    # Properties from v0 that need to be migrated to v1 (from AUXILIARY_MATERIAL:v0):
    # MANUFACTURER
    # SUPPLIER
    # AUXILIARY_MATERIAL_TYPE


class BAMSample(Sample):
    defs = ObjectTypeDef(
        code="BAM_SAMPLE",
        description="A BAMSample is a sample that is used or produced in the context of BAM's activities.",
        generated_code_prefix="BAM_SAMP",
    )

    bam_oe = PropertyTypeAssignment(
        code="BAM_OE",
        data_type="VARCHAR",
        property_label="BAM Organizational Unit",
        description="The organizational unit of BAM that is responsible for the sample.",
        mandatory=False,
        section="Sample Details",
    )

    responsible_persons = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="BAM_PERSON",
        property_label="BAM Responsible Persons",
        description="The BAM persons responsible for the sample.",
        mandatory=False,
        section="Sample Details",
        multivalued=True,
    )


class Material(MaterialEntity):
    defs = ObjectTypeDef(
        code="MATERIAL",
        description="A Material is a material entity that is composed of a physical substance or "
        "mixture of substances and that is characterized primarily by its composition, structure, "
        "and resulting properties for use, production, study, or processing in a scientific, technical, "
        "or industrial context.",
        generated_code_prefix="MATER",
        iri=["https://w3id.org/pmd/co/PMD_0000000"],
        prev_versions=["MATERIAL_V1:v0", "RAW_MATERIAL_CODE:v0"],
    )

    material_id = PropertyTypeAssignment(
        code="MATERIAL_ID",
        data_type="VARCHAR",
        property_label="Material ID",
        description="The identifier of the material.",
        mandatory=True,
        section="Material Details",
    )

    material_type = PropertyTypeAssignment(
        code="MATERIAL_TYPE",
        data_type="VARCHAR",
        property_label="Material Type",
        description="The type of the material, such as a chemical, a polymer, or a metal.",
        mandatory=False,
        section="Material Details",
    )

    material_composition = PropertyTypeAssignment(
        code="MATERIAL_COMPOSITION",
        data_type="JSON",
        property_label="Material Composition",
        description="The composition of the material, defined by its constituent substances and their proportions.",
        mandatory=False,
        section="Material Details",
    )

    # Properties from v0 that need to be migrated to v1 (from MATERIAL_V1:v0):
    # MAT_BONDING_TYPE
    # MAT_STRUCTURE
    # CHEM_SPECIES_BY_WT_IN_PCT
    # CHEM_SPECIES_BY_COMP_IN_PCT

    # Properties from v0 that need to be migrated to v1 (from RAW_MATERIAL_CODE:v0):
    # MATERIAL_NUMBER
    # MATERIAL_GROUP
    # CHARACTERISTICS


class Chemical(MaterialEntity):
    defs = ObjectTypeDef(
        code="CHEMICAL",
        description="A Chemical is a material entity that is composed of one or more chemical substances "
        "and is identified, used, produced, studied, or managed primarily according to its chemical "
        "composition or chemical identity.",
        generated_code_prefix="CHEM",
        iri=["http://purl.obolibrary.org/obo/CHEBI_24431"],
        prev_versions=["CHEMICAL:v0"],
    )

    chemical_formula_descriptive = PropertyTypeAssignment(
        code="CHEMICAL_FORMULA_DESCRIPTIVE",
        data_type="VARCHAR",
        property_label="Descriptive formula",
        description="Human-readable representation of the chemical composition.",
        mandatory=False,
        section="Chemical Identity",
    )

    chemical_formula_reduced = PropertyTypeAssignment(
        code="CHEMICAL_FORMULA_REDUCED",
        data_type="VARCHAR",
        property_label="Reduced formula",
        description="Chemical formula with reduced stoichiometric proportions.",
        mandatory=False,
        section="Chemical Identity",
    )

    chemical_formula_iupac = PropertyTypeAssignment(
        code="CHEMICAL_FORMULA_IUPAC",
        data_type="VARCHAR",
        property_label="IUPAC formula",
        description="Chemical formula following IUPAC conventions.",
        mandatory=False,
        section="Chemical Identity",
        prev_versions=["IUPAC_NAME:v0"],
    )

    chemical_formula_hill = PropertyTypeAssignment(
        code="CHEMICAL_FORMULA_HILL",
        data_type="VARCHAR",
        property_label="Hill formula",
        description="Chemical formula using Hill notation.",
        mandatory=False,
        section="Chemical Identity",
    )

    chemical_formula_anonymous = PropertyTypeAssignment(
        code="CHEMICAL_FORMULA_ANONYMOUS",
        data_type="VARCHAR",
        property_label="Anonymous formula",
        description="Formula describing stoichiometry without chemical element identities.",
        mandatory=False,
        section="Chemical Identity",
    )

    cas_number = PropertyTypeAssignment(
        code="CAS_NUMBER",
        data_type="VARCHAR",
        property_label="CAS number",
        description="Chemical Abstracts Service registry number.",
        mandatory=False,
        section="Chemical Identifiers",
        prev_versions=["CAS_NUMBER:v0"],
    )

    inchi = PropertyTypeAssignment(
        code="INCHI",
        data_type="VARCHAR",
        property_label="InChI",
        description="International Chemical Identifier.",
        mandatory=False,
        section="Chemical Identifiers",
    )

    inchi_key = PropertyTypeAssignment(
        code="INCHI_KEY",
        data_type="VARCHAR",
        property_label="InChIKey",
        description="Hashed representation of an InChI identifier.",
        mandatory=False,
        section="Chemical Identifiers",
    )

    smiles = PropertyTypeAssignment(
        code="SMILES",
        data_type="VARCHAR",
        property_label="SMILES",
        description="SMILES representation of the chemical structure.",
        mandatory=False,
        section="Chemical Identifiers",
    )

    canonical_smiles = PropertyTypeAssignment(
        code="CANONICAL_SMILES",
        data_type="VARCHAR",
        property_label="Canonical SMILES",
        description="Canonicalized SMILES representation of the chemical structure.",
        mandatory=False,
        section="Chemical Identifiers",
    )

    pubchem_cid = PropertyTypeAssignment(
        code="PUBCHEM_CID",
        data_type="INTEGER",
        property_label="PubChem CID",
        description="PubChem compound identifier.",
        mandatory=False,
        section="Chemical Identifiers",
    )

    pubchem_link = PropertyTypeAssignment(
        code="PUBCHEM_LINK",
        data_type="HYPERLINK",
        property_label="PubChem link",
        description="Link to the corresponding PubChem compound entry.",
        mandatory=False,
        section="Chemical Identifiers",
    )

    molar_mass = PropertyTypeAssignment(
        code="MOLAR_MASS",
        data_type="REAL",
        units="g/mol",
        property_label="Molar mass",
        description="Molar mass of the chemical species.",
        mandatory=False,
        section="Chemical Properties",
        prev_versions=["MASS_MOLAR:v0"],
    )

    # Properties from v0 that need to be migrated to v1 (from CHEMICAL:v0):
    # DENSITY_GRAM_PER_CUBIC_CM
    # CONCENTRATION
    # PRODUCT_CATEGORY
    # BARCODE_EXTERNAL
