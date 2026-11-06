from bam_masterdata.datamodel.v0.object_types import Person, Sample
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.entities import ObjectType


class Drmd(ObjectType):
    defs = ObjectTypeDef(
        code="DRMD",
        description="""Digital Reference Material Document (DRMD): machine-readable reference material certificate or product information sheet according to ISO 33401:2024""",
        generated_code_prefix="DRMD",
        iri=[
            "http://purl.obolibrary.org/obo/IAO_0000310",
            "https://www.iso.org/standard/84222.html",
        ],
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        section="General Information",
    )

    language = PropertyTypeAssignment(
        code="LANGUAGE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="LANGUAGE",
        property_label="Language",
        description="""Language of the texts of the document, written as ISO 639-1 code on each text element (@lang)""",
        mandatory=False,
        section="General Information",
    )

    drmd_document_title = PropertyTypeAssignment(
        code="DRMD_DOCUMENT_TITLE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DRMD_DOCUMENT_TITLE",
        property_label="Title of the document",
        description="""Type of the document: reference material certificate or product information sheet (drmd:titleOfTheDocument, ISO 33401:2024, 5.2.2)""",
        mandatory=True,
        section="Core Data",
    )

    uuid = PropertyTypeAssignment(
        code="UUID",
        data_type="VARCHAR",
        property_label="UUID",
        description="""A Universally Unique IDentifier (UUID/GUID) according to RFC 4122//Ein Universally Unique IDentifier (UUID/GUID) nach RFC 4122""",
        mandatory=True,
        section="Core Data",
    )

    version = PropertyTypeAssignment(
        code="VERSION",
        data_type="VARCHAR",
        property_label="Version",
        description="""Version""",
        mandatory=True,
        section="Core Data",
    )

    drmd_validity_type = PropertyTypeAssignment(
        code="DRMD_VALIDITY_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DRMD_VALIDITY_TYPE",
        property_label="Validity type",
        description="""Form in which the period of validity is stated: until revoked, period after dispatch or fixed end date (drmd:validity, ISO 33401:2024, 5.2.8)""",
        mandatory=True,
        section="Validity",
    )

    date_expiration = PropertyTypeAssignment(
        code="DATE_EXPIRATION",
        data_type="DATE",
        property_label="Expiration Date",
        description="""Expiration Date//Verfallsdatum""",
        mandatory=False,
        section="Validity",
    )

    drmd_dispatch_date = PropertyTypeAssignment(
        code="DRMD_DISPATCH_DATE",
        data_type="DATE",
        property_label="Dispatch date",
        description="""Date on which the unit was dispatched (drmd:timeAfterDispatch/drmd:dispatchDate)""",
        mandatory=False,
        section="Validity",
    )

    drmd_period = PropertyTypeAssignment(
        code="DRMD_PERIOD",
        data_type="VARCHAR",
        property_label="Period",
        description="""Duration in ISO 8601 format, e.g. P2Y or P3Y2M""",
        mandatory=False,
        section="Validity",
    )

    drmd_producer = PropertyTypeAssignment(
        code="DRMD_PRODUCER",
        data_type="OBJECT",
        object_code="PERSON.DRMD_PRODUCER",
        property_label="Reference material producer",
        description="""Producer responsible for the reference material and for the document (drmd:referenceMaterialProducer, ISO 33401:2024, 5.2.5)""",
        mandatory=True,
        section="Reference Material Producer",
    )

    drmd_intended_use = PropertyTypeAssignment(
        code="DRMD_INTENDED_USE",
        data_type="MULTILINE_VARCHAR",
        property_label="Intended use",
        description="""Intended use of the material and, where relevant, uses for which it is not suitable (drmd:intendedUse, ISO 33401:2024, 5.2.6)""",
        mandatory=True,
        section="Statements",
    )

    drmd_commutability = PropertyTypeAssignment(
        code="DRMD_COMMUTABILITY",
        data_type="MULTILINE_VARCHAR",
        property_label="Commutability",
        description="""Statement on commutability; if it was not assessed, say so (drmd:commutability, ISO 33401:2024, 5.2.9)""",
        mandatory=False,
        section="Statements",
    )

    drmd_storage_information = PropertyTypeAssignment(
        code="DRMD_STORAGE_INFORMATION",
        data_type="MULTILINE_VARCHAR",
        property_label="Storage information",
        description="""Storage conditions needed to keep the material stable and its property values valid (drmd:storageInformation, ISO 33401:2024, 5.2.10)""",
        mandatory=True,
        section="Statements",
    )

    drmd_handling_instructions = PropertyTypeAssignment(
        code="DRMD_HANDLING_INSTRUCTIONS",
        data_type="MULTILINE_VARCHAR",
        property_label="Instructions for handling and use",
        description="""Instructions for handling and use of the material, e.g. preparation and cleaning (drmd:instructionsForHandlingAndUse, ISO 33401:2024, 5.2.11)""",
        mandatory=True,
        section="Statements",
    )

    drmd_metrological_traceability = PropertyTypeAssignment(
        code="DRMD_METROLOGICAL_TRACEABILITY",
        data_type="MULTILINE_VARCHAR",
        property_label="Metrological traceability",
        description="""Statement of metrological traceability naming the measurand and the reference to which the values are traceable; mandatory for certificates (drmd:metrologicalTraceability, ISO 33401:2024, 5.3.4)""",
        mandatory=False,
        section="Statements",
    )

    drmd_health_and_safety = PropertyTypeAssignment(
        code="DRMD_HEALTH_AND_SAFETY",
        data_type="MULTILINE_VARCHAR",
        property_label="Health and safety information",
        description="""Hazards of the material and the protective measures to take (drmd:healthAndSafetyInformation, ISO 33401:2024, 5.4.3)""",
        mandatory=False,
        section="Statements",
    )

    drmd_subcontractors = PropertyTypeAssignment(
        code="DRMD_SUBCONTRACTORS",
        data_type="MULTILINE_VARCHAR",
        property_label="Subcontractors",
        description="""Subcontracted activities and contributing laboratories (drmd:subcontractors, ISO 33401:2024, 5.4.4)""",
        mandatory=False,
        section="Statements",
    )

    drmd_legal_notice = PropertyTypeAssignment(
        code="DRMD_LEGAL_NOTICE",
        data_type="MULTILINE_VARCHAR",
        property_label="Legal notice",
        description="""Legal notices such as disclaimers or limitations of liability (drmd:legalNotice, ISO 33401:2024, 5.4.6)""",
        mandatory=False,
        section="Statements",
    )

    drmd_certification_report = PropertyTypeAssignment(
        code="DRMD_CERTIFICATION_REPORT",
        data_type="MULTILINE_VARCHAR",
        property_label="Reference to certification report",
        description="""Reference to the certification report or to a report on characterisation, homogeneity and stability, e.g. a citation with DOI or URL (drmd:referenceToCertificationReport, ISO 33401:2024, 5.4.7)""",
        mandatory=False,
        section="Statements",
    )

    drmd_comment = PropertyTypeAssignment(
        code="DRMD_COMMENT",
        data_type="MULTILINE_VARCHAR",
        property_label="Document comment",
        description="""Comment on the document as a whole that is published in the DRMD (drmd:comment)""",
        mandatory=False,
        section="Document Comment",
    )


class DrmdProducer(Person):
    defs = ObjectTypeDef(
        code="PERSON.DRMD_PRODUCER",
        description="""Reference material producer as stated in a DRMD: the producer organisation in AFFILIATION, its contact point (a department or a person) in $NAME, and the contact details and postal address of that contact point (drmd:referenceMaterialProducer)""",
        generated_code_prefix="PERS.DRMD_PROD",
    )

    # The contact point can be a department, so the family name is optional here
    family_name = PropertyTypeAssignment(
        code="FAMILY_NAME",
        data_type="VARCHAR",
        property_label="Family name",
        description="""Family name//Nachname""",
        mandatory=False,
        section="General Information",
    )

    homepage = PropertyTypeAssignment(
        code="HOMEPAGE",
        data_type="HYPERLINK",
        property_label="Homepage",
        description="""Homepage//Homepage""",
        mandatory=False,
        section="Contact Information",
    )

    # A DRMD states the postal address of the producer in separate parts (dcc:location)
    street = PropertyTypeAssignment(
        code="STREET",
        data_type="VARCHAR",
        property_label="Street",
        description="""Street name of a postal address""",
        mandatory=False,
        section="Postal Address",
    )

    street_number = PropertyTypeAssignment(
        code="STREET_NUMBER",
        data_type="VARCHAR",
        property_label="Street number",
        description="""House number of a postal address""",
        mandatory=False,
        section="Postal Address",
    )

    postal_code = PropertyTypeAssignment(
        code="POSTAL_CODE",
        data_type="VARCHAR",
        property_label="Postal code",
        description="""Postal code of a postal address""",
        mandatory=False,
        section="Postal Address",
    )

    city = PropertyTypeAssignment(
        code="CITY",
        data_type="VARCHAR",
        property_label="City",
        description="""City of a postal address""",
        mandatory=False,
        section="Postal Address",
    )

    country_code = PropertyTypeAssignment(
        code="COUNTRY_CODE",
        data_type="VARCHAR",
        property_label="Country code",
        description="""Country code according to ISO 3166-1 alpha-2, e.g. DE""",
        mandatory=False,
        section="Postal Address",
    )


class DrmdResponsiblePerson(Person):
    defs = ObjectTypeDef(
        code="PERSON.DRMD_RESPONSIBLE_PERSON",
        description="""Person responsible for a DRMD, e.g. the officer who approves the document, with name and role (drmd:respPersons/dcc:respPerson, ISO 33401:2024, 5.3.5)""",
        generated_code_prefix="PERS.DRMD_RESP",
    )

    role = PropertyTypeAssignment(
        code="ROLE",
        data_type="VARCHAR",
        property_label="Role",
        description="""Role or function of the person, e.g. head of division; it may name the responsible organisational unit""",
        mandatory=False,
        section="General Information",
    )

    drmd_main_signer = PropertyTypeAssignment(
        code="DRMD_MAIN_SIGNER",
        data_type="BOOLEAN",
        property_label="Main signer",
        description="""Marks the person who signs the document (dcc:mainSigner)""",
        mandatory=False,
        section="General Information",
    )


class DrmdIdentifier(ObjectType):
    defs = ObjectTypeDef(
        code="DRMD_IDENTIFIER",
        description="""Identifier given as scheme and value, e.g. a DOI, ROR, CAS number, product code or batch number; it is a parent of the document, producer, reference material or quantity it identifies (drmd:identifierType)""",
        generated_code_prefix="DRMD_ID",
        iri=["http://purl.obolibrary.org/obo/IAO_0020000"],
    )

    drmd_scheme = PropertyTypeAssignment(
        code="DRMD_SCHEME",
        data_type="VARCHAR",
        property_label="Scheme",
        description="""Naming system, registry, standard or taxonomy the value belongs to, e.g. DOI, ROR, CAS, ProductCode, Batch or UNS (drmd:scheme, drmd:reference)""",
        mandatory=True,
        section="General Information",
    )

    drmd_identifier_value = PropertyTypeAssignment(
        code="DRMD_IDENTIFIER_VALUE",
        data_type="VARCHAR",
        property_label="Identifier value",
        description="""Identifier or class exactly as issued within its scheme; for a material, exactly as printed on the label (drmd:value, drmd:classID)""",
        mandatory=True,
        section="General Information",
    )

    drmd_link = PropertyTypeAssignment(
        code="DRMD_LINK",
        data_type="HYPERLINK",
        property_label="Link",
        description="""Persistent URL where the identifier or class can be looked up (drmd:link)""",
        mandatory=False,
        section="General Information",
    )


class DrmdMaterialClass(DrmdIdentifier):
    defs = ObjectTypeDef(
        code="DRMD_IDENTIFIER.MATERIAL_CLASS",
        description="""Classification of a reference material in a standard, taxonomy or catalogue: DRMD_SCHEME names the classification and DRMD_IDENTIFIER_VALUE holds the class, e.g. A03190 (drmd:materialClass)""",
        generated_code_prefix="DRMD_MCL",
    )


class ReferenceMaterial(Sample):
    defs = ObjectTypeDef(
        code="SAMPLE.REFERENCE_MATERIAL",
        description="""Reference material (RM or CRM) described by a DRMD document, typically one batch; name and description are given in $NAME and DESCRIPTION (drmd:material)""",
        generated_code_prefix="SAM.RM",
        iri=["http://purl.obolibrary.org/obo/BFO_0000040"],
    )


class DrmdPropertySet(ObjectType):
    defs = ObjectTypeDef(
        code="DRMD_PROPERTY_SET",
        description="""Block of property values of a DRMD, certified or informative, with procedures, results and metadata (drmd:propertiesList/drmd:properties)""",
        generated_code_prefix="DRMD_PSET",
        iri=["http://purl.obolibrary.org/obo/IAO_0000100"],
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        section="General Information",
    )

    drmd_is_certified = PropertyTypeAssignment(
        code="DRMD_IS_CERTIFIED",
        data_type="BOOLEAN",
        property_label="Certified values",
        description="""True if the values of this block are certified; not permitted in a product information sheet (@isCertified, ISO 33401:2024, 5.3.3)""",
        mandatory=False,
        section="General Information",
    )


class DrmdResult(ObjectType):
    defs = ObjectTypeDef(
        code="DRMD_RESULT",
        description="""Result within a block of property values, typically one value or one table (drmd:results/drmd:result)""",
        generated_code_prefix="DRMD_RES",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        section="General Information",
    )

    drmd_data_as_list = PropertyTypeAssignment(
        code="DRMD_DATA_AS_LIST",
        data_type="BOOLEAN",
        property_label="Data given as list",
        description="""True if the result data is a list of quantities (drmd:list), e.g. a composition table; a result with several quantities is always a list""",
        mandatory=False,
        section="General Information",
    )


class DrmdQuantity(ObjectType):
    defs = ObjectTypeDef(
        code="DRMD_QUANTITY",
        description="""Quantity of a DRMD with value, D-SI unit, quantity kind and measurement uncertainty (drmd:quantityType, dcc:primitiveQuantityType)""",
        generated_code_prefix="DRMD_QTY",
        iri=["http://purl.obolibrary.org/obo/IAO_0000109"],
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        section="General Information",
    )

    drmd_value_type = PropertyTypeAssignment(
        code="DRMD_VALUE_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DRMD_VALUE_TYPE",
        property_label="Value type",
        description="""Form in which the value is given: real, hybrid, constant, real list, no quantity or character list""",
        mandatory=True,
        section="General Information",
    )

    drmd_quantity_role = PropertyTypeAssignment(
        code="DRMD_QUANTITY_ROLE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DRMD_QUANTITY_ROLE",
        property_label="Quantity role",
        description="""Place of the quantity in the document; required for quantities linked to a reference material (minimum sample size or item quantity)""",
        mandatory=False,
        section="General Information",
    )

    drmd_si_label = PropertyTypeAssignment(
        code="DRMD_SI_LABEL",
        data_type="VARCHAR",
        property_label="SI label",
        description="""Short label of the value (si:label)""",
        mandatory=False,
        section="SI Value",
    )

    drmd_quantity_kind = PropertyTypeAssignment(
        code="DRMD_QUANTITY_KIND",
        data_type="VARCHAR",
        property_label="Quantity kind (QUDT)",
        description="""Kind of quantity as QUDT quantity kind local name, e.g. MassFraction, Mass or Density; it states what was measured (si:quantityTypeQUDT)""",
        mandatory=False,
        section="SI Value",
        iri=["http://qudt.org/schema/qudt/QuantityKind"],
    )

    drmd_si_value = PropertyTypeAssignment(
        code="DRMD_SI_VALUE",
        data_type="REAL",
        property_label="Value",
        description="""Numeric value in the unit given in DRMD_SI_UNIT (si:value)""",
        mandatory=False,
        section="SI Value",
    )

    drmd_si_unit = PropertyTypeAssignment(
        code="DRMD_SI_UNIT",
        data_type="VARCHAR",
        property_label="Unit (D-SI)",
        description="""Unit written in D-SI syntax, e.g. \\gram or \\milli\\gram\\kilo\\gram\\tothe{-1} (si:unit)""",
        mandatory=False,
        section="SI Value",
    )

    drmd_significant_digit = PropertyTypeAssignment(
        code="DRMD_SIGNIFICANT_DIGIT",
        data_type="INTEGER",
        property_label="Significant digit",
        description="""Power of ten of the last significant digit of the value according to ISO 80000, e.g. -2 for 6.42 (si:significantDigit)""",
        mandatory=False,
        section="SI Value",
    )

    drmd_si_date_time = PropertyTypeAssignment(
        code="DRMD_SI_DATE_TIME",
        data_type="TIMESTAMP",
        property_label="Date and time",
        description="""Date and time the value refers to (si:dateTime)""",
        mandatory=False,
        section="SI Value",
    )

    drmd_uncertainty_type = PropertyTypeAssignment(
        code="DRMD_UNCERTAINTY_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DRMD_UNCERTAINTY_TYPE",
        property_label="Uncertainty type",
        description="""Form of the measurement uncertainty: standard uncertainty, expanded uncertainty or coverage interval (si:measurementUncertaintyUnivariate)""",
        mandatory=False,
        section="Measurement Uncertainty",
    )

    drmd_standard_uncertainty = PropertyTypeAssignment(
        code="DRMD_STANDARD_UNCERTAINTY",
        data_type="REAL",
        property_label="Standard uncertainty",
        description="""Standard uncertainty in the unit of the value (si:valueStandardMU)""",
        mandatory=False,
        section="Measurement Uncertainty",
    )

    drmd_expanded_uncertainty = PropertyTypeAssignment(
        code="DRMD_EXPANDED_UNCERTAINTY",
        data_type="REAL",
        property_label="Expanded uncertainty",
        description="""Expanded uncertainty in the unit of the value (si:valueExpandedMU)""",
        mandatory=False,
        section="Measurement Uncertainty",
    )

    drmd_coverage_factor = PropertyTypeAssignment(
        code="DRMD_COVERAGE_FACTOR",
        data_type="REAL",
        property_label="Coverage factor",
        description="""Coverage factor k, greater than or equal to 1 (si:coverageFactor)""",
        mandatory=False,
        section="Measurement Uncertainty",
    )

    drmd_coverage_probability = PropertyTypeAssignment(
        code="DRMD_COVERAGE_PROBABILITY",
        data_type="REAL",
        property_label="Coverage probability",
        description="""Coverage probability between 0 and 1, e.g. 0.95 (si:coverageProbability)""",
        mandatory=False,
        section="Measurement Uncertainty",
    )

    drmd_interval_min = PropertyTypeAssignment(
        code="DRMD_INTERVAL_MIN",
        data_type="REAL",
        property_label="Coverage interval minimum",
        description="""Lower limit of the coverage interval in the unit of the value (si:intervalMin)""",
        mandatory=False,
        section="Measurement Uncertainty",
    )

    drmd_interval_max = PropertyTypeAssignment(
        code="DRMD_INTERVAL_MAX",
        data_type="REAL",
        property_label="Coverage interval maximum",
        description="""Upper limit of the coverage interval in the unit of the value (si:intervalMax)""",
        mandatory=False,
        section="Measurement Uncertainty",
    )

    drmd_distribution = PropertyTypeAssignment(
        code="DRMD_DISTRIBUTION",
        data_type="VARCHAR",
        property_label="Distribution",
        description="""Probability distribution assumed for the value, e.g. normal or rectangular (si:distribution)""",
        mandatory=False,
        section="Measurement Uncertainty",
    )

    drmd_no_quantity_text = PropertyTypeAssignment(
        code="DRMD_NO_QUANTITY_TEXT",
        data_type="MULTILINE_VARCHAR",
        property_label="Non-numeric value",
        description="""Statement given instead of a numeric value, e.g. why no value was determined (dcc:noQuantity)""",
        mandatory=False,
        section="Non Numeric Value",
    )

    drmd_chars_list = PropertyTypeAssignment(
        code="DRMD_CHARS_LIST",
        data_type="VARCHAR",
        property_label="Token list",
        description="""Whitespace-separated list of tokens such as codes or categories (dcc:charsXMLList)""",
        mandatory=False,
        section="Non Numeric Value",
    )


class DrmdProcedure(ObjectType):
    defs = ObjectTypeDef(
        code="DRMD_PROCEDURE",
        description="""Measurement procedure used to establish property values or for which the material is intended (drmd:procedures/dcc:usedMethod)""",
        generated_code_prefix="DRMD_PROC",
        iri=["http://purl.obolibrary.org/obo/OBI_0000272"],
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        section="General Information",
    )

    drmd_norms = PropertyTypeAssignment(
        code="DRMD_NORMS",
        data_type="MULTILINE_VARCHAR",
        property_label="Normative documents",
        description="""Standards or other normative documents, one per line, e.g. ISO 11885 (dcc:norm)""",
        mandatory=False,
        section="General Information",
    )

    reference = PropertyTypeAssignment(
        code="REFERENCE",
        data_type="MULTILINE_VARCHAR",
        property_label="References",
        description="""Useful refences""",
        mandatory=False,
        section="General Information",
    )

    drmd_links = PropertyTypeAssignment(
        code="DRMD_LINKS",
        data_type="MULTILINE_VARCHAR",
        property_label="Links",
        description="""URLs with further information, one per line (dcc:link)""",
        mandatory=False,
        section="General Information",
    )


class DrmdMetadata(ObjectType):
    defs = ObjectTypeDef(
        code="DRMD_METADATA",
        description="""Measurement metadata of a block of property values, e.g. traceability or the definition of a non-SI unit (drmd:measurementMetaData/dcc:metaData)""",
        generated_code_prefix="DRMD_META",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        section="General Information",
    )

    drmd_convention = PropertyTypeAssignment(
        code="DRMD_CONVENTION",
        data_type="VARCHAR",
        property_label="Convention",
        description="""Convention that was applied, e.g. for rounding or reporting (dcc:convention)""",
        mandatory=False,
        section="Measurement Metadata",
    )

    drmd_traceable = PropertyTypeAssignment(
        code="DRMD_TRACEABLE",
        data_type="BOOLEAN",
        property_label="Traceable",
        description="""Whether the values are metrologically traceable (dcc:traceable)""",
        mandatory=False,
        section="Measurement Metadata",
    )

    drmd_norms = PropertyTypeAssignment(
        code="DRMD_NORMS",
        data_type="MULTILINE_VARCHAR",
        property_label="Normative documents",
        description="""Standards or other normative documents, one per line, e.g. ISO 11885 (dcc:norm)""",
        mandatory=False,
        section="Measurement Metadata",
    )

    reference = PropertyTypeAssignment(
        code="REFERENCE",
        data_type="MULTILINE_VARCHAR",
        property_label="References",
        description="""Useful refences""",
        mandatory=False,
        section="Measurement Metadata",
    )

    drmd_links = PropertyTypeAssignment(
        code="DRMD_LINKS",
        data_type="MULTILINE_VARCHAR",
        property_label="Links",
        description="""URLs with further information, one per line (dcc:link)""",
        mandatory=False,
        section="Measurement Metadata",
    )

    drmd_declaration = PropertyTypeAssignment(
        code="DRMD_DECLARATION",
        data_type="MULTILINE_VARCHAR",
        property_label="Declaration",
        description="""Declaration text of the metadata statement (dcc:declaration)""",
        mandatory=False,
        section="Measurement Metadata",
    )

    drmd_valid = PropertyTypeAssignment(
        code="DRMD_VALID",
        data_type="BOOLEAN",
        property_label="Valid",
        description="""Validity flag of the metadata statement (dcc:valid)""",
        mandatory=False,
        section="Measurement Metadata",
    )

    drmd_metadata_date = PropertyTypeAssignment(
        code="DRMD_METADATA_DATE",
        data_type="DATE",
        property_label="Date",
        description="""Date of the metadata statement (dcc:date)""",
        mandatory=False,
        section="Measurement Metadata",
    )

    drmd_period = PropertyTypeAssignment(
        code="DRMD_PERIOD",
        data_type="VARCHAR",
        property_label="Period",
        description="""Duration in ISO 8601 format, e.g. P2Y or P3Y2M""",
        mandatory=False,
        section="Measurement Metadata",
    )

    drmd_conformity = PropertyTypeAssignment(
        code="DRMD_CONFORMITY",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DRMD_CONFORMITY",
        property_label="Conformity",
        description="""Conformity status of the metadata statement (dcc:conformity)""",
        mandatory=False,
        section="Measurement Metadata",
    )

    drmd_non_si_unit = PropertyTypeAssignment(
        code="DRMD_NON_SI_UNIT",
        data_type="VARCHAR",
        property_label="Non-SI unit",
        description="""Non-SI unit defined by this metadata, as used in a si:hybrid sibling value (dcc:nonSIUnit)""",
        mandatory=False,
        section="Measurement Metadata",
    )

    drmd_non_si_definition = PropertyTypeAssignment(
        code="DRMD_NON_SI_DEFINITION",
        data_type="MULTILINE_VARCHAR",
        property_label="Definition of the non-SI unit",
        description="""Definition of the non-SI unit (dcc:nonSIDefinition)""",
        mandatory=False,
        section="Measurement Metadata",
    )


class DrmdStatement(ObjectType):
    defs = ObjectTypeDef(
        code="DRMD_STATEMENT",
        description="""Additional statement on the handling and use of the material that has no dedicated element (drmd:statements/drmd:statement)""",
        generated_code_prefix="DRMD_STMT",
        iri=["http://purl.obolibrary.org/obo/IAO_0000300"],
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        section="General Information",
    )

    drmd_statement_text = PropertyTypeAssignment(
        code="DRMD_STATEMENT_TEXT",
        data_type="MULTILINE_VARCHAR",
        property_label="Statement text",
        description="""Text of the statement (dcc:content)""",
        mandatory=False,
        section="General Information",
    )

    drmd_formula_latex = PropertyTypeAssignment(
        code="DRMD_FORMULA_LATEX",
        data_type="MULTILINE_VARCHAR",
        property_label="Formula (LaTeX)",
        description="""Formula belonging to the statement, in LaTeX notation (dcc:formula/dcc:latex)""",
        mandatory=False,
        section="General Information",
    )


class DrmdFile(ObjectType):
    defs = ObjectTypeDef(
        code="DRMD_FILE",
        description="""File embedded in a DRMD; the file itself is attached to this object as dataset. As a parent of the document it is an embedded document such as the PDF rendition (drmd:document), as a parent of a statement it belongs to that statement (dcc:file)""",
        generated_code_prefix="DRMD_FILE",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        section="General Information",
    )

    drmd_file_name = PropertyTypeAssignment(
        code="DRMD_FILE_NAME",
        data_type="VARCHAR",
        property_label="File name",
        description="""File name written to the DRMD; its extension should match the media type, e.g. EXA-1a-certificate.pdf (dcc:fileName)""",
        mandatory=True,
        section="General Information",
    )

    drmd_mime_type = PropertyTypeAssignment(
        code="DRMD_MIME_TYPE",
        data_type="VARCHAR",
        property_label="Media type",
        description="""Registered media (MIME) type of the file, e.g. application/pdf (dcc:mimeType)""",
        mandatory=True,
        section="General Information",
    )
