from bam_masterdata.datamodel.object_types import Sample
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.entities import ObjectType

# Object types of the Digital Reference Material Document (DRMD) datamodel.
#
# The structure follows drmd.xsd v1.0.0 (namespace urn:drmd:schema) and its supporting
# schemas DCC v3.3.0 and D-SI v2.2.1. Elements that occur once are modelled as
# properties; elements that repeat are modelled as object types. Repeating elements are
# linked to the object that contains them as openBIS parents ("component -> container"),
# for example: SAMPLE.REFERENCE_MATERIAL -> DRMD, DRMD_QUANTITY -> DRMD_RESULT ->
# DRMD_PROPERTY_SET -> DRMD. The full mapping to XPath, the cardinalities of the two
# document types (reference material certificate and product information sheet) and the
# corresponding Schematron rules are documented in README.md in this folder.
#
# XML details that only describe how an element sits in the document (its position in a
# list, @id, @refId and @refType) are grouped in the section "Document Structure"; a
# generator can fill or create them automatically.
#
# Property types that already exist in the BAM datamodel are reused with their existing
# definition ($NAME, DESCRIPTION, ALIAS, VERSION, UUID, DATE_EXPIRATION, EMAIL,
# TELEPHONE, HOMEPAGE, REFERENCE, RESPONSIBLE_PERSON, NOTES, $XMLCOMMENTS).


# Ontology mapping (BFO/IAO transition): IAO:0000310 (document)
class Drmd(ObjectType):
    defs = ObjectTypeDef(
        code="DRMD",
        description="""Digital Reference Material Document (DRMD): machine-readable RM certificate or product information sheet according to ISO 33401:2024//Digitales Referenzmaterialdokument (DRMD): maschinenlesbares RM-Zertifikat oder Produktinformationsblatt nach ISO 33401:2024""",
        generated_code_prefix="DRMD",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        section="General Information",
    )

    drmd_schema_version = PropertyTypeAssignment(
        code="DRMD_SCHEMA_VERSION",
        data_type="VARCHAR",
        property_label="DRMD schema version",
        description="""Version of the DRMD specification the document follows, written as major.minor.patch, e.g. 1.0.0 (@schemaVersion)//Version der DRMD-Spezifikation, der das Dokument folgt, im Format Major.Minor.Patch, z. B. 1.0.0 (@schemaVersion)""",
        mandatory=True,
        section="General Information",
    )

    drmd_language = PropertyTypeAssignment(
        code="DRMD_LANGUAGE",
        data_type="VARCHAR",
        property_label="Language",
        description="""Language code according to ISO 639-1 (two lower-case letters, e.g. en or de)//Sprachcode nach ISO 639-1 (zwei Kleinbuchstaben, z. B. en oder de)""",
        mandatory=False,
        section="General Information",
    )

    drmd_document_title = PropertyTypeAssignment(
        code="DRMD_DOCUMENT_TITLE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DRMD_DOCUMENT_TITLE",
        property_label="Title of the document",
        description="""Type of the document: reference material certificate or product information sheet (drmd:titleOfTheDocument, ISO 33401:2024, 5.2.2)//Art des Dokuments: Referenzmaterialzertifikat oder Produktinformationsblatt (drmd:titleOfTheDocument, ISO 33401:2024, 5.2.2)""",
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
        description="""Form in which the period of validity is stated: until revoked, period after dispatch or fixed end date (drmd:validity, ISO 33401:2024, 5.2.8)//Form der Gültigkeitsangabe: bis auf Widerruf, Zeitraum ab Versand oder festes Enddatum (drmd:validity, ISO 33401:2024, 5.2.8)""",
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
        description="""Date on which the unit was dispatched (drmd:timeAfterDispatch/drmd:dispatchDate)//Datum, an dem die Einheit versandt wurde (drmd:timeAfterDispatch/drmd:dispatchDate)""",
        mandatory=False,
        section="Validity",
    )

    drmd_period = PropertyTypeAssignment(
        code="DRMD_PERIOD",
        data_type="VARCHAR",
        property_label="Period",
        description="""Duration in ISO 8601 format, e.g. P2Y or P3Y2M//Zeitdauer im Format ISO 8601, z. B. P2Y oder P3Y2M""",
        mandatory=False,
        section="Validity",
    )

    drmd_producer = PropertyTypeAssignment(
        code="DRMD_PRODUCER",
        data_type="OBJECT",
        object_code="DRMD_PRODUCER",
        property_label="Reference material producer",
        description="""Organisation responsible for the reference material and for the document (drmd:referenceMaterialProducer, ISO 33401:2024, 5.2.5)//Für das Referenzmaterial und das Dokument verantwortliche Organisation (drmd:referenceMaterialProducer, ISO 33401:2024, 5.2.5)""",
        mandatory=True,
        section="Reference Material Producer",
    )

    drmd_intended_use = PropertyTypeAssignment(
        code="DRMD_INTENDED_USE",
        data_type="MULTILINE_VARCHAR",
        property_label="Intended use",
        description="""Intended use of the material and, where relevant, uses for which it is not suitable (drmd:intendedUse, ISO 33401:2024, 5.2.6)//Bestimmungsgemäße Verwendung des Materials und gegebenenfalls ungeeignete Verwendungen (drmd:intendedUse, ISO 33401:2024, 5.2.6)""",
        mandatory=True,
        section="Statements",
    )

    drmd_commutability = PropertyTypeAssignment(
        code="DRMD_COMMUTABILITY",
        data_type="MULTILINE_VARCHAR",
        property_label="Commutability",
        description="""Statement on commutability; if it was not assessed, say so (drmd:commutability, ISO 33401:2024, 5.2.9)//Aussage zur Kommutabilität; falls sie nicht bewertet wurde, ist dies anzugeben (drmd:commutability, ISO 33401:2024, 5.2.9)""",
        mandatory=False,
        section="Statements",
    )

    drmd_storage_information = PropertyTypeAssignment(
        code="DRMD_STORAGE_INFORMATION",
        data_type="MULTILINE_VARCHAR",
        property_label="Storage information",
        description="""Storage conditions needed to keep the material stable and its property values valid (drmd:storageInformation, ISO 33401:2024, 5.2.10)//Lagerbedingungen, die für die Stabilität des Materials und die Gültigkeit der Eigenschaftswerte erforderlich sind (drmd:storageInformation, ISO 33401:2024, 5.2.10)""",
        mandatory=True,
        section="Statements",
    )

    drmd_handling_instructions = PropertyTypeAssignment(
        code="DRMD_HANDLING_INSTRUCTIONS",
        data_type="MULTILINE_VARCHAR",
        property_label="Instructions for handling and use",
        description="""Instructions for handling and use of the material, e.g. preparation and cleaning (drmd:instructionsForHandlingAndUse, ISO 33401:2024, 5.2.11)//Anweisungen zur Handhabung und Verwendung des Materials, z. B. Vorbereitung und Reinigung (drmd:instructionsForHandlingAndUse, ISO 33401:2024, 5.2.11)""",
        mandatory=True,
        section="Statements",
    )

    drmd_metrological_traceability = PropertyTypeAssignment(
        code="DRMD_METROLOGICAL_TRACEABILITY",
        data_type="MULTILINE_VARCHAR",
        property_label="Metrological traceability",
        description="""Statement of metrological traceability naming the measurand and the reference to which the values are traceable; mandatory for certificates (drmd:metrologicalTraceability, ISO 33401:2024, 5.3.4)//Aussage zur metrologischen Rückführung mit Messgröße und Referenz, auf die die Werte rückgeführt sind; Pflicht für Zertifikate (drmd:metrologicalTraceability, ISO 33401:2024, 5.3.4)""",
        mandatory=False,
        section="Statements",
    )

    drmd_health_and_safety = PropertyTypeAssignment(
        code="DRMD_HEALTH_AND_SAFETY",
        data_type="MULTILINE_VARCHAR",
        property_label="Health and safety information",
        description="""Hazards of the material and the protective measures to take (drmd:healthAndSafetyInformation, ISO 33401:2024, 5.4.3)//Gefahren des Materials und zu ergreifende Schutzmaßnahmen (drmd:healthAndSafetyInformation, ISO 33401:2024, 5.4.3)""",
        mandatory=False,
        section="Statements",
    )

    drmd_subcontractors = PropertyTypeAssignment(
        code="DRMD_SUBCONTRACTORS",
        data_type="MULTILINE_VARCHAR",
        property_label="Subcontractors",
        description="""Subcontracted activities and contributing laboratories (drmd:subcontractors, ISO 33401:2024, 5.4.4)//Vergebene Tätigkeiten und beteiligte Laboratorien (drmd:subcontractors, ISO 33401:2024, 5.4.4)""",
        mandatory=False,
        section="Statements",
    )

    drmd_legal_notice = PropertyTypeAssignment(
        code="DRMD_LEGAL_NOTICE",
        data_type="MULTILINE_VARCHAR",
        property_label="Legal notice",
        description="""Legal notices such as disclaimers or limitations of liability (drmd:legalNotice, ISO 33401:2024, 5.4.6)//Rechtliche Hinweise wie Haftungsausschlüsse oder Haftungsbeschränkungen (drmd:legalNotice, ISO 33401:2024, 5.4.6)""",
        mandatory=False,
        section="Statements",
    )

    drmd_certification_report = PropertyTypeAssignment(
        code="DRMD_CERTIFICATION_REPORT",
        data_type="MULTILINE_VARCHAR",
        property_label="Reference to certification report",
        description="""Reference to the certification report or to a report on characterisation, homogeneity and stability (drmd:referenceToCertificationReport, ISO 33401:2024, 5.4.7)//Verweis auf den Zertifizierungsbericht oder einen Bericht zu Charakterisierung, Homogenität und Stabilität (drmd:referenceToCertificationReport, ISO 33401:2024, 5.4.7)""",
        mandatory=False,
        section="Statements",
    )

    drmd_comment = PropertyTypeAssignment(
        code="DRMD_COMMENT",
        data_type="MULTILINE_VARCHAR",
        property_label="Document comment",
        description="""Plain-text comment on the document as a whole that is published in the DRMD; internal notes belong in NOTES (drmd:comment)//Kommentar zum gesamten Dokument im Klartext, der im DRMD veröffentlicht wird; interne Notizen gehören in NOTES (drmd:comment)""",
        mandatory=False,
        section="Document Comment",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        section="Comments",
    )


# Ontology mapping (BFO/IAO transition): OBI:0000245 (organization)
class DrmdProducer(ObjectType):
    defs = ObjectTypeDef(
        code="DRMD_PRODUCER",
        description="""Reference material producer of a DRMD: name, contact details, postal address and electronic trust capabilities (drmd:referenceMaterialProducer)//Referenzmaterialhersteller eines DRMD: Name, Kontaktdaten, Anschrift und elektronische Vertrauensdienste (drmd:referenceMaterialProducer)""",
        generated_code_prefix="DRMD_PROD",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        section="General Information",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative Name",
        description="""e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname""",
        mandatory=False,
        section="General Information",
    )

    drmd_contact_name = PropertyTypeAssignment(
        code="DRMD_CONTACT_NAME",
        data_type="VARCHAR",
        property_label="Contact name",
        description="""Name of the contact point, e.g. a department or a sales team (dcc:contact/dcc:name)//Name der Kontaktstelle, z. B. einer Abteilung oder des Vertriebs (dcc:contact/dcc:name)""",
        mandatory=True,
        section="Contact Information",
    )

    email = PropertyTypeAssignment(
        code="EMAIL",
        data_type="VARCHAR",
        property_label="Email address",
        description="""Email address//E-Mail-Adresse""",
        mandatory=False,
        section="Contact Information",
    )

    telephone = PropertyTypeAssignment(
        code="TELEPHONE",
        data_type="VARCHAR",
        property_label="Telephone number",
        description="""Telephone number//Telefonnummer""",
        mandatory=False,
        section="Contact Information",
    )

    drmd_fax = PropertyTypeAssignment(
        code="DRMD_FAX",
        data_type="VARCHAR",
        property_label="Fax number",
        description="""Fax number (dcc:fax)//Faxnummer (dcc:fax)""",
        mandatory=False,
        section="Contact Information",
    )

    homepage = PropertyTypeAssignment(
        code="HOMEPAGE",
        data_type="HYPERLINK",
        property_label="Homepage",
        description="""Homepage//Homepage""",
        mandatory=False,
        section="Contact Information",
    )

    drmd_street = PropertyTypeAssignment(
        code="DRMD_STREET",
        data_type="VARCHAR",
        property_label="Street",
        description="""Street name (dcc:street)//Straßenname (dcc:street)""",
        mandatory=False,
        section="Postal Address",
    )

    drmd_street_no = PropertyTypeAssignment(
        code="DRMD_STREET_NO",
        data_type="VARCHAR",
        property_label="Street number",
        description="""House number (dcc:streetNo)//Hausnummer (dcc:streetNo)""",
        mandatory=False,
        section="Postal Address",
    )

    drmd_post_code = PropertyTypeAssignment(
        code="DRMD_POST_CODE",
        data_type="VARCHAR",
        property_label="Postal code",
        description="""Postal code (dcc:postCode)//Postleitzahl (dcc:postCode)""",
        mandatory=False,
        section="Postal Address",
    )

    drmd_city = PropertyTypeAssignment(
        code="DRMD_CITY",
        data_type="VARCHAR",
        property_label="City",
        description="""City (dcc:city)//Ort (dcc:city)""",
        mandatory=False,
        section="Postal Address",
    )

    drmd_state = PropertyTypeAssignment(
        code="DRMD_STATE",
        data_type="VARCHAR",
        property_label="State or region",
        description="""Federal state, province or region (dcc:state)//Bundesland, Provinz oder Region (dcc:state)""",
        mandatory=False,
        section="Postal Address",
    )

    drmd_country_code = PropertyTypeAssignment(
        code="DRMD_COUNTRY_CODE",
        data_type="VARCHAR",
        property_label="Country code",
        description="""Country code according to ISO 3166-1 alpha-2 (two upper-case letters, e.g. DE) (dcc:countryCode)//Ländercode nach ISO 3166-1 Alpha-2 (zwei Großbuchstaben, z. B. DE) (dcc:countryCode)""",
        mandatory=False,
        section="Postal Address",
    )

    drmd_post_office_box = PropertyTypeAssignment(
        code="DRMD_POST_OFFICE_BOX",
        data_type="VARCHAR",
        property_label="Post office box",
        description="""Post office box (dcc:postOfficeBox)//Postfach (dcc:postOfficeBox)""",
        mandatory=False,
        section="Postal Address",
    )

    drmd_address_further = PropertyTypeAssignment(
        code="DRMD_ADDRESS_FURTHER",
        data_type="MULTILINE_VARCHAR",
        property_label="Further address information",
        description="""Further address details, e.g. building or room (dcc:further)//Weitere Adressangaben, z. B. Gebäude oder Raum (dcc:further)""",
        mandatory=False,
        section="Postal Address",
    )

    drmd_latitude = PropertyTypeAssignment(
        code="DRMD_LATITUDE",
        data_type="REAL",
        property_label="Latitude",
        units="degree",
        description="""Geographic latitude in the WGS84 system, in decimal degrees (dcc:positionCoordinates)//Geografische Breite im System WGS84, in Dezimalgrad (dcc:positionCoordinates)""",
        mandatory=False,
        section="Postal Address",
    )

    drmd_longitude = PropertyTypeAssignment(
        code="DRMD_LONGITUDE",
        data_type="REAL",
        property_label="Longitude",
        units="degree",
        description="""Geographic longitude in the WGS84 system, in decimal degrees (dcc:positionCoordinates)//Geografische Länge im System WGS84, in Dezimalgrad (dcc:positionCoordinates)""",
        mandatory=False,
        section="Postal Address",
    )

    drmd_electronic_seal = PropertyTypeAssignment(
        code="DRMD_ELECTRONIC_SEAL",
        data_type="BOOLEAN",
        property_label="Electronic seal",
        description="""Whether an electronic seal of the organisation is applied (cryptElectronicSeal)//Ob ein elektronisches Siegel der Organisation angebracht wird (cryptElectronicSeal)""",
        mandatory=False,
        section="Electronic Trust",
    )

    drmd_electronic_signature = PropertyTypeAssignment(
        code="DRMD_ELECTRONIC_SIGNATURE",
        data_type="BOOLEAN",
        property_label="Electronic signature",
        description="""Whether personal electronic signatures are applied (cryptElectronicSignature)//Ob persönliche elektronische Signaturen angebracht werden (cryptElectronicSignature)""",
        mandatory=False,
        section="Electronic Trust",
    )

    drmd_electronic_timestamp = PropertyTypeAssignment(
        code="DRMD_ELECTRONIC_TIMESTAMP",
        data_type="BOOLEAN",
        property_label="Electronic time stamp",
        description="""Whether a trusted electronic time stamp is applied (cryptElectronicTimeStamp)//Ob ein vertrauenswürdiger elektronischer Zeitstempel angebracht wird (cryptElectronicTimeStamp)""",
        mandatory=False,
        section="Electronic Trust",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        section="Comments",
    )


# Ontology mapping (BFO/IAO transition): BFO:0000023 (role) borne by a person
class DrmdRespPerson(ObjectType):
    defs = ObjectTypeDef(
        code="DRMD_RESP_PERSON",
        description="""Person responsible for a DRMD, e.g. the approving officer, with name and function (drmd:respPersons/dcc:respPerson)//Für ein DRMD verantwortliche Person, z. B. die freigebende Person, mit Name und Funktion (drmd:respPersons/dcc:respPerson)""",
        generated_code_prefix="DRMD_RESP",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        section="General Information",
    )

    responsible_person = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Responsible person",
        description="""Responsible person//Verantwortliche Person""",
        mandatory=False,
        section="General Information",
    )

    drmd_role = PropertyTypeAssignment(
        code="DRMD_ROLE",
        data_type="VARCHAR",
        property_label="Function",
        description="""Function or role of the person, e.g. head of division; may name the responsible organisational unit (dcc:role, ISO 33401:2024, 5.3.5)//Funktion oder Rolle der Person, z. B. Abteilungsleitung; kann die verantwortliche Organisationseinheit nennen (dcc:role, ISO 33401:2024, 5.3.5)""",
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

    drmd_main_signer = PropertyTypeAssignment(
        code="DRMD_MAIN_SIGNER",
        data_type="BOOLEAN",
        property_label="Main signer",
        description="""Marks the person who signs the document (dcc:mainSigner)//Kennzeichnet die Person, die das Dokument unterzeichnet (dcc:mainSigner)""",
        mandatory=False,
        section="General Information",
    )

    email = PropertyTypeAssignment(
        code="EMAIL",
        data_type="VARCHAR",
        property_label="Email address",
        description="""Email address//E-Mail-Adresse""",
        mandatory=False,
        section="Contact Information",
    )

    telephone = PropertyTypeAssignment(
        code="TELEPHONE",
        data_type="VARCHAR",
        property_label="Telephone number",
        description="""Telephone number//Telefonnummer""",
        mandatory=False,
        section="Contact Information",
    )

    drmd_fax = PropertyTypeAssignment(
        code="DRMD_FAX",
        data_type="VARCHAR",
        property_label="Fax number",
        description="""Fax number (dcc:fax)//Faxnummer (dcc:fax)""",
        mandatory=False,
        section="Contact Information",
    )

    homepage = PropertyTypeAssignment(
        code="HOMEPAGE",
        data_type="HYPERLINK",
        property_label="Homepage",
        description="""Homepage//Homepage""",
        mandatory=False,
        section="Contact Information",
    )

    drmd_street = PropertyTypeAssignment(
        code="DRMD_STREET",
        data_type="VARCHAR",
        property_label="Street",
        description="""Street name (dcc:street)//Straßenname (dcc:street)""",
        mandatory=False,
        section="Postal Address",
    )

    drmd_street_no = PropertyTypeAssignment(
        code="DRMD_STREET_NO",
        data_type="VARCHAR",
        property_label="Street number",
        description="""House number (dcc:streetNo)//Hausnummer (dcc:streetNo)""",
        mandatory=False,
        section="Postal Address",
    )

    drmd_post_code = PropertyTypeAssignment(
        code="DRMD_POST_CODE",
        data_type="VARCHAR",
        property_label="Postal code",
        description="""Postal code (dcc:postCode)//Postleitzahl (dcc:postCode)""",
        mandatory=False,
        section="Postal Address",
    )

    drmd_city = PropertyTypeAssignment(
        code="DRMD_CITY",
        data_type="VARCHAR",
        property_label="City",
        description="""City (dcc:city)//Ort (dcc:city)""",
        mandatory=False,
        section="Postal Address",
    )

    drmd_state = PropertyTypeAssignment(
        code="DRMD_STATE",
        data_type="VARCHAR",
        property_label="State or region",
        description="""Federal state, province or region (dcc:state)//Bundesland, Provinz oder Region (dcc:state)""",
        mandatory=False,
        section="Postal Address",
    )

    drmd_country_code = PropertyTypeAssignment(
        code="DRMD_COUNTRY_CODE",
        data_type="VARCHAR",
        property_label="Country code",
        description="""Country code according to ISO 3166-1 alpha-2 (two upper-case letters, e.g. DE) (dcc:countryCode)//Ländercode nach ISO 3166-1 Alpha-2 (zwei Großbuchstaben, z. B. DE) (dcc:countryCode)""",
        mandatory=False,
        section="Postal Address",
    )

    drmd_post_office_box = PropertyTypeAssignment(
        code="DRMD_POST_OFFICE_BOX",
        data_type="VARCHAR",
        property_label="Post office box",
        description="""Post office box (dcc:postOfficeBox)//Postfach (dcc:postOfficeBox)""",
        mandatory=False,
        section="Postal Address",
    )

    drmd_address_further = PropertyTypeAssignment(
        code="DRMD_ADDRESS_FURTHER",
        data_type="MULTILINE_VARCHAR",
        property_label="Further address information",
        description="""Further address details, e.g. building or room (dcc:further)//Weitere Adressangaben, z. B. Gebäude oder Raum (dcc:further)""",
        mandatory=False,
        section="Postal Address",
    )

    drmd_latitude = PropertyTypeAssignment(
        code="DRMD_LATITUDE",
        data_type="REAL",
        property_label="Latitude",
        units="degree",
        description="""Geographic latitude in the WGS84 system, in decimal degrees (dcc:positionCoordinates)//Geografische Breite im System WGS84, in Dezimalgrad (dcc:positionCoordinates)""",
        mandatory=False,
        section="Postal Address",
    )

    drmd_longitude = PropertyTypeAssignment(
        code="DRMD_LONGITUDE",
        data_type="REAL",
        property_label="Longitude",
        units="degree",
        description="""Geographic longitude in the WGS84 system, in decimal degrees (dcc:positionCoordinates)//Geografische Länge im System WGS84, in Dezimalgrad (dcc:positionCoordinates)""",
        mandatory=False,
        section="Postal Address",
    )

    drmd_electronic_seal = PropertyTypeAssignment(
        code="DRMD_ELECTRONIC_SEAL",
        data_type="BOOLEAN",
        property_label="Electronic seal",
        description="""Whether an electronic seal of the organisation is applied (cryptElectronicSeal)//Ob ein elektronisches Siegel der Organisation angebracht wird (cryptElectronicSeal)""",
        mandatory=False,
        section="Electronic Trust",
    )

    drmd_electronic_signature = PropertyTypeAssignment(
        code="DRMD_ELECTRONIC_SIGNATURE",
        data_type="BOOLEAN",
        property_label="Electronic signature",
        description="""Whether personal electronic signatures are applied (cryptElectronicSignature)//Ob persönliche elektronische Signaturen angebracht werden (cryptElectronicSignature)""",
        mandatory=False,
        section="Electronic Trust",
    )

    drmd_electronic_timestamp = PropertyTypeAssignment(
        code="DRMD_ELECTRONIC_TIMESTAMP",
        data_type="BOOLEAN",
        property_label="Electronic time stamp",
        description="""Whether a trusted electronic time stamp is applied (cryptElectronicTimeStamp)//Ob ein vertrauenswürdiger elektronischer Zeitstempel angebracht wird (cryptElectronicTimeStamp)""",
        mandatory=False,
        section="Electronic Trust",
    )

    drmd_position = PropertyTypeAssignment(
        code="DRMD_POSITION",
        data_type="INTEGER",
        property_label="Position",
        description="""Position of the element within its list in the DRMD document (1 = first)//Position des Elements in seiner Liste im DRMD-Dokument (1 = erstes)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_xml_id = PropertyTypeAssignment(
        code="DRMD_XML_ID",
        data_type="VARCHAR",
        property_label="XML ID",
        description="""Identifier of the element within the DRMD document, the target of @refId; leave empty to have it generated (@id, xs:ID)//Kennung des Elements innerhalb des DRMD-Dokuments, Ziel von @refId; leer lassen, damit sie erzeugt wird (@id, xs:ID)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_xml_ref_id = PropertyTypeAssignment(
        code="DRMD_XML_REF_ID",
        data_type="VARCHAR",
        property_label="XML references",
        description="""Whitespace-separated XML IDs of other elements of the same document that this element refers to (@refId, xs:IDREFS)//Durch Leerzeichen getrennte XML-IDs anderer Elemente desselben Dokuments, auf die sich dieses Element bezieht (@refId, xs:IDREFS)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_dcc_ref_type = PropertyTypeAssignment(
        code="DRMD_DCC_REF_TYPE",
        data_type="VARCHAR",
        property_label="DCC reference type",
        description="""Whitespace-separated reference type tokens of an element with a DCC type, e.g. a quantity, procedure or responsible person (@refType, dcc:refTypesType)//Durch Leerzeichen getrennte Referenztypen eines Elements mit DCC-Typ, z. B. einer Größe, eines Verfahrens oder einer verantwortlichen Person (@refType, dcc:refTypesType)""",
        mandatory=False,
        section="Document Structure",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        section="Comments",
    )


# Ontology mapping (BFO/IAO transition): IAO:0020000 (identifier)
class DrmdIdentifier(ObjectType):
    defs = ObjectTypeDef(
        code="DRMD_IDENTIFIER",
        description="""Identifier of a DRMD document, organisation, material or property, given as scheme and value (drmd:identifierType)//Kennung eines DRMD-Dokuments, einer Organisation, eines Materials oder einer Eigenschaft, angegeben als System und Wert (drmd:identifierType)""",
        generated_code_prefix="DRMD_ID",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        section="General Information",
    )

    drmd_scheme = PropertyTypeAssignment(
        code="DRMD_SCHEME",
        data_type="VARCHAR",
        property_label="Scheme",
        description="""Naming system, registry, standard or taxonomy the value belongs to, e.g. DOI, ROR, CAS, ProductCode, Batch or UNS (drmd:scheme, drmd:reference)//Bezeichnungssystem, Register, Norm oder Taxonomie, zu der der Wert gehört, z. B. DOI, ROR, CAS, ProductCode, Batch oder UNS (drmd:scheme, drmd:reference)""",
        mandatory=True,
        section="General Information",
    )

    drmd_identifier_value = PropertyTypeAssignment(
        code="DRMD_IDENTIFIER_VALUE",
        data_type="VARCHAR",
        property_label="Identifier value",
        description="""Identifier exactly as issued within its scheme; for a material, exactly as printed on the label (drmd:value)//Kennung genau wie im jeweiligen System vergeben; bei einem Material genau wie auf dem Etikett gedruckt (drmd:value)""",
        mandatory=True,
        section="General Information",
    )

    drmd_link = PropertyTypeAssignment(
        code="DRMD_LINK",
        data_type="HYPERLINK",
        property_label="Link",
        description="""Persistent URL where the identifier or class can be looked up (drmd:link)//Persistente URL, unter der die Kennung oder Klasse nachgeschlagen werden kann (drmd:link)""",
        mandatory=False,
        section="General Information",
    )

    drmd_position = PropertyTypeAssignment(
        code="DRMD_POSITION",
        data_type="INTEGER",
        property_label="Position",
        description="""Position of the element within its list in the DRMD document (1 = first)//Position des Elements in seiner Liste im DRMD-Dokument (1 = erstes)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_xml_id = PropertyTypeAssignment(
        code="DRMD_XML_ID",
        data_type="VARCHAR",
        property_label="XML ID",
        description="""Identifier of the element within the DRMD document, the target of @refId; leave empty to have it generated (@id, xs:ID)//Kennung des Elements innerhalb des DRMD-Dokuments, Ziel von @refId; leer lassen, damit sie erzeugt wird (@id, xs:ID)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_xml_ref_id = PropertyTypeAssignment(
        code="DRMD_XML_REF_ID",
        data_type="VARCHAR",
        property_label="XML references",
        description="""Whitespace-separated XML IDs of other elements of the same document that this element refers to (@refId, xs:IDREFS)//Durch Leerzeichen getrennte XML-IDs anderer Elemente desselben Dokuments, auf die sich dieses Element bezieht (@refId, xs:IDREFS)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_ref_type = PropertyTypeAssignment(
        code="DRMD_REF_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DRMD_REF_TYPE",
        property_label="Reference type",
        description="""Reference type of an element with a DRMD type: basic_certificateIdentification or basic_measuredValue (@refType, drmd:refTypesType)//Referenztyp eines Elements mit DRMD-Typ: basic_certificateIdentification oder basic_measuredValue (@refType, drmd:refTypesType)""",
        mandatory=False,
        section="Document Structure",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        section="Comments",
    )


# Ontology mapping (BFO/IAO transition): BFO:0000040 (material entity)
class ReferenceMaterial(Sample):
    defs = ObjectTypeDef(
        code="SAMPLE.REFERENCE_MATERIAL",
        description="""Reference material (RM or CRM) described by a DRMD document, typically one batch; name and description are given in $NAME and DESCRIPTION (drmd:material)//Referenzmaterial (RM oder ZRM), das in einem DRMD-Dokument beschrieben wird, typischerweise eine Charge; Name und Beschreibung stehen in $NAME und DESCRIPTION (drmd:material)""",
        generated_code_prefix="SAM.RM",
    )

    drmd_position = PropertyTypeAssignment(
        code="DRMD_POSITION",
        data_type="INTEGER",
        property_label="Position",
        description="""Position of the element within its list in the DRMD document (1 = first)//Position des Elements in seiner Liste im DRMD-Dokument (1 = erstes)""",
        mandatory=False,
        section="Document Structure",
    )


# Ontology mapping (BFO/IAO transition): IAO:0000030 (information content entity), classification
class DrmdMaterialClass(ObjectType):
    defs = ObjectTypeDef(
        code="DRMD_MATERIAL_CLASS",
        description="""Classification of a reference material according to a standard, taxonomy or catalogue scheme (drmd:materialClass)//Klassifizierung eines Referenzmaterials nach einer Norm, Taxonomie oder einem Katalogsystem (drmd:materialClass)""",
        generated_code_prefix="DRMD_MCL",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        section="General Information",
    )

    drmd_scheme = PropertyTypeAssignment(
        code="DRMD_SCHEME",
        data_type="VARCHAR",
        property_label="Scheme",
        description="""Naming system, registry, standard or taxonomy the value belongs to, e.g. DOI, ROR, CAS, ProductCode, Batch or UNS (drmd:scheme, drmd:reference)//Bezeichnungssystem, Register, Norm oder Taxonomie, zu der der Wert gehört, z. B. DOI, ROR, CAS, ProductCode, Batch oder UNS (drmd:scheme, drmd:reference)""",
        mandatory=True,
        section="General Information",
    )

    drmd_class_id = PropertyTypeAssignment(
        code="DRMD_CLASS_ID",
        data_type="VARCHAR",
        property_label="Class ID",
        description="""Class code or name within the classification scheme, e.g. A03190 or A2 Fine Test Dust (drmd:classID)//Klassencode oder Klassenname innerhalb des Klassifikationssystems, z. B. A03190 oder A2 Fine Test Dust (drmd:classID)""",
        mandatory=True,
        section="General Information",
    )

    drmd_link = PropertyTypeAssignment(
        code="DRMD_LINK",
        data_type="HYPERLINK",
        property_label="Link",
        description="""Persistent URL where the identifier or class can be looked up (drmd:link)//Persistente URL, unter der die Kennung oder Klasse nachgeschlagen werden kann (drmd:link)""",
        mandatory=False,
        section="General Information",
    )

    drmd_position = PropertyTypeAssignment(
        code="DRMD_POSITION",
        data_type="INTEGER",
        property_label="Position",
        description="""Position of the element within its list in the DRMD document (1 = first)//Position des Elements in seiner Liste im DRMD-Dokument (1 = erstes)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_xml_id = PropertyTypeAssignment(
        code="DRMD_XML_ID",
        data_type="VARCHAR",
        property_label="XML ID",
        description="""Identifier of the element within the DRMD document, the target of @refId; leave empty to have it generated (@id, xs:ID)//Kennung des Elements innerhalb des DRMD-Dokuments, Ziel von @refId; leer lassen, damit sie erzeugt wird (@id, xs:ID)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_xml_ref_id = PropertyTypeAssignment(
        code="DRMD_XML_REF_ID",
        data_type="VARCHAR",
        property_label="XML references",
        description="""Whitespace-separated XML IDs of other elements of the same document that this element refers to (@refId, xs:IDREFS)//Durch Leerzeichen getrennte XML-IDs anderer Elemente desselben Dokuments, auf die sich dieses Element bezieht (@refId, xs:IDREFS)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_ref_type = PropertyTypeAssignment(
        code="DRMD_REF_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DRMD_REF_TYPE",
        property_label="Reference type",
        description="""Reference type of an element with a DRMD type: basic_certificateIdentification or basic_measuredValue (@refType, drmd:refTypesType)//Referenztyp eines Elements mit DRMD-Typ: basic_certificateIdentification oder basic_measuredValue (@refType, drmd:refTypesType)""",
        mandatory=False,
        section="Document Structure",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        section="Comments",
    )


# Ontology mapping (BFO/IAO transition): IAO:0000100 (data set)
class DrmdPropertySet(ObjectType):
    defs = ObjectTypeDef(
        code="DRMD_PROPERTY_SET",
        description="""Block of property values of a DRMD, certified or informative, with procedures, results and metadata (drmd:propertiesList/drmd:properties)//Block von Eigenschaftswerten eines DRMD, zertifiziert oder informativ, mit Verfahren, Ergebnissen und Metadaten (drmd:propertiesList/drmd:properties)""",
        generated_code_prefix="DRMD_PSET",
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
        description="""True if the values of this block are certified; not permitted in a product information sheet (@isCertified, ISO 33401:2024, 5.3.3)//Wahr, wenn die Werte dieses Blocks zertifiziert sind; in einem Produktinformationsblatt nicht zulässig (@isCertified, ISO 33401:2024, 5.3.3)""",
        mandatory=False,
        section="General Information",
    )

    drmd_position = PropertyTypeAssignment(
        code="DRMD_POSITION",
        data_type="INTEGER",
        property_label="Position",
        description="""Position of the element within its list in the DRMD document (1 = first)//Position des Elements in seiner Liste im DRMD-Dokument (1 = erstes)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_xml_id = PropertyTypeAssignment(
        code="DRMD_XML_ID",
        data_type="VARCHAR",
        property_label="XML ID",
        description="""Identifier of the element within the DRMD document, the target of @refId; leave empty to have it generated (@id, xs:ID)//Kennung des Elements innerhalb des DRMD-Dokuments, Ziel von @refId; leer lassen, damit sie erzeugt wird (@id, xs:ID)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_xml_ref_id = PropertyTypeAssignment(
        code="DRMD_XML_REF_ID",
        data_type="VARCHAR",
        property_label="XML references",
        description="""Whitespace-separated XML IDs of other elements of the same document that this element refers to (@refId, xs:IDREFS)//Durch Leerzeichen getrennte XML-IDs anderer Elemente desselben Dokuments, auf die sich dieses Element bezieht (@refId, xs:IDREFS)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_ref_type = PropertyTypeAssignment(
        code="DRMD_REF_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DRMD_REF_TYPE",
        property_label="Reference type",
        description="""Reference type of an element with a DRMD type: basic_certificateIdentification or basic_measuredValue (@refType, drmd:refTypesType)//Referenztyp eines Elements mit DRMD-Typ: basic_certificateIdentification oder basic_measuredValue (@refType, drmd:refTypesType)""",
        mandatory=False,
        section="Document Structure",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        section="Comments",
    )


# Ontology mapping (BFO/IAO transition): IAO:0000109 (measurement datum)
class DrmdResult(ObjectType):
    defs = ObjectTypeDef(
        code="DRMD_RESULT",
        description="""Result within a block of property values, typically one value or one table (drmd:results/drmd:result)//Ergebnis innerhalb eines Blocks von Eigenschaftswerten, typischerweise ein Wert oder eine Tabelle (drmd:results/drmd:result)""",
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
        description="""True if the result data is a list of quantities (drmd:list), e.g. a composition table; a result with several quantities is always a list//Wahr, wenn die Ergebnisdaten eine Liste von Größen sind (drmd:list), z. B. eine Zusammensetzungstabelle; ein Ergebnis mit mehreren Größen ist immer eine Liste""",
        mandatory=False,
        section="General Information",
    )

    drmd_position = PropertyTypeAssignment(
        code="DRMD_POSITION",
        data_type="INTEGER",
        property_label="Position",
        description="""Position of the element within its list in the DRMD document (1 = first)//Position des Elements in seiner Liste im DRMD-Dokument (1 = erstes)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_xml_id = PropertyTypeAssignment(
        code="DRMD_XML_ID",
        data_type="VARCHAR",
        property_label="XML ID",
        description="""Identifier of the element within the DRMD document, the target of @refId; leave empty to have it generated (@id, xs:ID)//Kennung des Elements innerhalb des DRMD-Dokuments, Ziel von @refId; leer lassen, damit sie erzeugt wird (@id, xs:ID)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_xml_ref_id = PropertyTypeAssignment(
        code="DRMD_XML_REF_ID",
        data_type="VARCHAR",
        property_label="XML references",
        description="""Whitespace-separated XML IDs of other elements of the same document that this element refers to (@refId, xs:IDREFS)//Durch Leerzeichen getrennte XML-IDs anderer Elemente desselben Dokuments, auf die sich dieses Element bezieht (@refId, xs:IDREFS)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_ref_type = PropertyTypeAssignment(
        code="DRMD_REF_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DRMD_REF_TYPE",
        property_label="Reference type",
        description="""Reference type of an element with a DRMD type: basic_certificateIdentification or basic_measuredValue (@refType, drmd:refTypesType)//Referenztyp eines Elements mit DRMD-Typ: basic_certificateIdentification oder basic_measuredValue (@refType, drmd:refTypesType)""",
        mandatory=False,
        section="Document Structure",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        section="Comments",
    )


# Ontology mapping (BFO/IAO transition): IAO:0000032 (scalar measurement datum)
class DrmdQuantity(ObjectType):
    defs = ObjectTypeDef(
        code="DRMD_QUANTITY",
        description="""Quantity of a DRMD with value, D-SI unit, quantity kind and measurement uncertainty (drmd:quantityType, dcc:primitiveQuantityType)//Größe eines DRMD mit Wert, D-SI-Einheit, Größenart und Messunsicherheit (drmd:quantityType, dcc:primitiveQuantityType)""",
        generated_code_prefix="DRMD_QTY",
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
        description="""Encoding of the value: si:real, si:hybrid, si:constant, si:realListXMLList, dcc:noQuantity or dcc:charsXMLList//Kodierung des Werts: si:real, si:hybrid, si:constant, si:realListXMLList, dcc:noQuantity oder dcc:charsXMLList""",
        mandatory=True,
        section="General Information",
    )

    drmd_quantity_role = PropertyTypeAssignment(
        code="DRMD_QUANTITY_ROLE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DRMD_QUANTITY_ROLE",
        property_label="Quantity role",
        description="""Place of the quantity in the document; required for quantities linked to a reference material (minimum sample size or item quantity)//Stelle der Größe im Dokument; erforderlich für Größen, die mit einem Referenzmaterial verknüpft sind (Mindestprobenmenge oder Größe der Einheit)""",
        mandatory=False,
        section="General Information",
    )

    drmd_si_label = PropertyTypeAssignment(
        code="DRMD_SI_LABEL",
        data_type="VARCHAR",
        property_label="SI label",
        description="""Short label of the value (si:label)//Kurzbezeichnung des Werts (si:label)""",
        mandatory=False,
        section="SI Value",
    )

    drmd_quantity_kind = PropertyTypeAssignment(
        code="DRMD_QUANTITY_KIND",
        data_type="VARCHAR",
        property_label="Quantity kind (QUDT)",
        description="""Kind of quantity as QUDT quantity kind local name, e.g. MassFraction, Mass or Density; it states what was measured (si:quantityTypeQUDT)//Größenart als lokaler Name einer QUDT-Größenart, z. B. MassFraction, Mass oder Density; sie gibt an, was gemessen wurde (si:quantityTypeQUDT)""",
        mandatory=False,
        section="SI Value",
    )

    drmd_si_value = PropertyTypeAssignment(
        code="DRMD_SI_VALUE",
        data_type="REAL",
        property_label="Value",
        description="""Numeric value in the unit given in DRMD_SI_UNIT (si:value)//Zahlenwert in der unter DRMD_SI_UNIT angegebenen Einheit (si:value)""",
        mandatory=False,
        section="SI Value",
    )

    drmd_si_unit = PropertyTypeAssignment(
        code="DRMD_SI_UNIT",
        data_type="VARCHAR",
        property_label="Unit (D-SI)",
        description="""Unit written in D-SI syntax, e.g. \\gram or \\milli\\gram\\kilo\\gram\\tothe{-1} (si:unit)//Einheit in D-SI-Syntax, z. B. \\gram oder \\milli\\gram\\kilo\\gram\\tothe{-1} (si:unit)""",
        mandatory=False,
        section="SI Value",
    )

    drmd_significant_digit = PropertyTypeAssignment(
        code="DRMD_SIGNIFICANT_DIGIT",
        data_type="INTEGER",
        property_label="Significant digit",
        description="""Power of ten of the last significant digit of the value according to ISO 80000, e.g. -2 for 6.42 (si:significantDigit)//Zehnerpotenz der letzten signifikanten Stelle des Werts nach ISO 80000, z. B. -2 für 6,42 (si:significantDigit)""",
        mandatory=False,
        section="SI Value",
    )

    drmd_si_date_time = PropertyTypeAssignment(
        code="DRMD_SI_DATE_TIME",
        data_type="TIMESTAMP",
        property_label="Date and time",
        description="""Date and time the value refers to (si:dateTime)//Datum und Uhrzeit, auf die sich der Wert bezieht (si:dateTime)""",
        mandatory=False,
        section="SI Value",
    )

    drmd_uncertainty_type = PropertyTypeAssignment(
        code="DRMD_UNCERTAINTY_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DRMD_UNCERTAINTY_TYPE",
        property_label="Uncertainty type",
        description="""Form of the measurement uncertainty: standardMU, expandedMU or coverageIntervalMU (si:measurementUncertaintyUnivariate)//Form der Messunsicherheit: standardMU, expandedMU oder coverageIntervalMU (si:measurementUncertaintyUnivariate)""",
        mandatory=False,
        section="Measurement Uncertainty",
    )

    drmd_standard_uncertainty = PropertyTypeAssignment(
        code="DRMD_STANDARD_UNCERTAINTY",
        data_type="REAL",
        property_label="Standard uncertainty",
        description="""Standard uncertainty in the unit of the value (si:valueStandardMU)//Standardunsicherheit in der Einheit des Werts (si:valueStandardMU)""",
        mandatory=False,
        section="Measurement Uncertainty",
    )

    drmd_expanded_uncertainty = PropertyTypeAssignment(
        code="DRMD_EXPANDED_UNCERTAINTY",
        data_type="REAL",
        property_label="Expanded uncertainty",
        description="""Expanded uncertainty in the unit of the value (si:valueExpandedMU)//Erweiterte Unsicherheit in der Einheit des Werts (si:valueExpandedMU)""",
        mandatory=False,
        section="Measurement Uncertainty",
    )

    drmd_coverage_factor = PropertyTypeAssignment(
        code="DRMD_COVERAGE_FACTOR",
        data_type="REAL",
        property_label="Coverage factor",
        description="""Coverage factor k, greater than or equal to 1 (si:coverageFactor)//Erweiterungsfaktor k, größer oder gleich 1 (si:coverageFactor)""",
        mandatory=False,
        section="Measurement Uncertainty",
    )

    drmd_coverage_probability = PropertyTypeAssignment(
        code="DRMD_COVERAGE_PROBABILITY",
        data_type="REAL",
        property_label="Coverage probability",
        description="""Coverage probability between 0 and 1, e.g. 0.95 (si:coverageProbability)//Überdeckungswahrscheinlichkeit zwischen 0 und 1, z. B. 0,95 (si:coverageProbability)""",
        mandatory=False,
        section="Measurement Uncertainty",
    )

    drmd_interval_min = PropertyTypeAssignment(
        code="DRMD_INTERVAL_MIN",
        data_type="REAL",
        property_label="Coverage interval minimum",
        description="""Lower limit of the coverage interval in the unit of the value (si:intervalMin)//Untere Grenze des Überdeckungsintervalls in der Einheit des Werts (si:intervalMin)""",
        mandatory=False,
        section="Measurement Uncertainty",
    )

    drmd_interval_max = PropertyTypeAssignment(
        code="DRMD_INTERVAL_MAX",
        data_type="REAL",
        property_label="Coverage interval maximum",
        description="""Upper limit of the coverage interval in the unit of the value (si:intervalMax)//Obere Grenze des Überdeckungsintervalls in der Einheit des Werts (si:intervalMax)""",
        mandatory=False,
        section="Measurement Uncertainty",
    )

    drmd_distribution = PropertyTypeAssignment(
        code="DRMD_DISTRIBUTION",
        data_type="VARCHAR",
        property_label="Distribution",
        description="""Probability distribution assumed for the value, e.g. normal or rectangular (si:distribution)//Angenommene Wahrscheinlichkeitsverteilung des Werts, z. B. normal oder rechteckig (si:distribution)""",
        mandatory=False,
        section="Measurement Uncertainty",
    )

    drmd_no_quantity_text = PropertyTypeAssignment(
        code="DRMD_NO_QUANTITY_TEXT",
        data_type="MULTILINE_VARCHAR",
        property_label="Non-numeric value",
        description="""Statement given instead of a numeric value, e.g. why no value was determined (dcc:noQuantity)//Angabe anstelle eines Zahlenwerts, z. B. warum kein Wert bestimmt wurde (dcc:noQuantity)""",
        mandatory=False,
        section="Non Numeric Value",
    )

    drmd_chars_list = PropertyTypeAssignment(
        code="DRMD_CHARS_LIST",
        data_type="VARCHAR",
        property_label="Token list",
        description="""Whitespace-separated list of tokens such as codes or categories (dcc:charsXMLList)//Durch Leerzeichen getrennte Liste von Zeichenketten wie Codes oder Kategorien (dcc:charsXMLList)""",
        mandatory=False,
        section="Non Numeric Value",
    )

    drmd_position = PropertyTypeAssignment(
        code="DRMD_POSITION",
        data_type="INTEGER",
        property_label="Position",
        description="""Position of the element within its list in the DRMD document (1 = first)//Position des Elements in seiner Liste im DRMD-Dokument (1 = erstes)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_xml_id = PropertyTypeAssignment(
        code="DRMD_XML_ID",
        data_type="VARCHAR",
        property_label="XML ID",
        description="""Identifier of the element within the DRMD document, the target of @refId; leave empty to have it generated (@id, xs:ID)//Kennung des Elements innerhalb des DRMD-Dokuments, Ziel von @refId; leer lassen, damit sie erzeugt wird (@id, xs:ID)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_xml_ref_id = PropertyTypeAssignment(
        code="DRMD_XML_REF_ID",
        data_type="VARCHAR",
        property_label="XML references",
        description="""Whitespace-separated XML IDs of other elements of the same document that this element refers to (@refId, xs:IDREFS)//Durch Leerzeichen getrennte XML-IDs anderer Elemente desselben Dokuments, auf die sich dieses Element bezieht (@refId, xs:IDREFS)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_dcc_ref_type = PropertyTypeAssignment(
        code="DRMD_DCC_REF_TYPE",
        data_type="VARCHAR",
        property_label="DCC reference type",
        description="""Whitespace-separated reference type tokens of an element with a DCC type, e.g. a quantity, procedure or responsible person (@refType, dcc:refTypesType)//Durch Leerzeichen getrennte Referenztypen eines Elements mit DCC-Typ, z. B. einer Größe, eines Verfahrens oder einer verantwortlichen Person (@refType, dcc:refTypesType)""",
        mandatory=False,
        section="Document Structure",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        section="Comments",
    )


# Ontology mapping (BFO/IAO transition): IAO:0000104 (plan specification)
class DrmdProcedure(ObjectType):
    defs = ObjectTypeDef(
        code="DRMD_PROCEDURE",
        description="""Measurement procedure used to establish property values or for which the material is intended (drmd:procedures/dcc:usedMethod)//Messverfahren, mit dem Eigenschaftswerte ermittelt wurden oder für das das Material bestimmt ist (drmd:procedures/dcc:usedMethod)""",
        generated_code_prefix="DRMD_PROC",
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
        description="""Standards or other normative documents, one per line, e.g. ISO 11885 (dcc:norm)//Normen oder andere normative Dokumente, eines je Zeile, z. B. ISO 11885 (dcc:norm)""",
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
        description="""URLs with further information, one per line (dcc:link)//URLs mit weiteren Informationen, eine je Zeile (dcc:link)""",
        mandatory=False,
        section="General Information",
    )

    drmd_position = PropertyTypeAssignment(
        code="DRMD_POSITION",
        data_type="INTEGER",
        property_label="Position",
        description="""Position of the element within its list in the DRMD document (1 = first)//Position des Elements in seiner Liste im DRMD-Dokument (1 = erstes)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_xml_id = PropertyTypeAssignment(
        code="DRMD_XML_ID",
        data_type="VARCHAR",
        property_label="XML ID",
        description="""Identifier of the element within the DRMD document, the target of @refId; leave empty to have it generated (@id, xs:ID)//Kennung des Elements innerhalb des DRMD-Dokuments, Ziel von @refId; leer lassen, damit sie erzeugt wird (@id, xs:ID)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_xml_ref_id = PropertyTypeAssignment(
        code="DRMD_XML_REF_ID",
        data_type="VARCHAR",
        property_label="XML references",
        description="""Whitespace-separated XML IDs of other elements of the same document that this element refers to (@refId, xs:IDREFS)//Durch Leerzeichen getrennte XML-IDs anderer Elemente desselben Dokuments, auf die sich dieses Element bezieht (@refId, xs:IDREFS)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_dcc_ref_type = PropertyTypeAssignment(
        code="DRMD_DCC_REF_TYPE",
        data_type="VARCHAR",
        property_label="DCC reference type",
        description="""Whitespace-separated reference type tokens of an element with a DCC type, e.g. a quantity, procedure or responsible person (@refType, dcc:refTypesType)//Durch Leerzeichen getrennte Referenztypen eines Elements mit DCC-Typ, z. B. einer Größe, eines Verfahrens oder einer verantwortlichen Person (@refType, dcc:refTypesType)""",
        mandatory=False,
        section="Document Structure",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        section="Comments",
    )


# Ontology mapping (BFO/IAO transition): IAO:0000030 (information content entity)
class DrmdMetadata(ObjectType):
    defs = ObjectTypeDef(
        code="DRMD_METADATA",
        description="""Measurement metadata of a block of property values, e.g. traceability or the definition of a non-SI unit (drmd:measurementMetaData/dcc:metaData)//Messmetadaten eines Blocks von Eigenschaftswerten, z. B. Rückführung oder Definition einer Nicht-SI-Einheit (drmd:measurementMetaData/dcc:metaData)""",
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
        description="""Convention that was applied, e.g. for rounding or reporting (dcc:convention)//Angewandte Konvention, z. B. für Rundung oder Angabe (dcc:convention)""",
        mandatory=False,
        section="Measurement Metadata",
    )

    drmd_traceable = PropertyTypeAssignment(
        code="DRMD_TRACEABLE",
        data_type="BOOLEAN",
        property_label="Traceable",
        description="""Whether the values are metrologically traceable (dcc:traceable)//Ob die Werte metrologisch rückgeführt sind (dcc:traceable)""",
        mandatory=False,
        section="Measurement Metadata",
    )

    drmd_norms = PropertyTypeAssignment(
        code="DRMD_NORMS",
        data_type="MULTILINE_VARCHAR",
        property_label="Normative documents",
        description="""Standards or other normative documents, one per line, e.g. ISO 11885 (dcc:norm)//Normen oder andere normative Dokumente, eines je Zeile, z. B. ISO 11885 (dcc:norm)""",
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
        description="""URLs with further information, one per line (dcc:link)//URLs mit weiteren Informationen, eine je Zeile (dcc:link)""",
        mandatory=False,
        section="Measurement Metadata",
    )

    drmd_declaration = PropertyTypeAssignment(
        code="DRMD_DECLARATION",
        data_type="MULTILINE_VARCHAR",
        property_label="Declaration",
        description="""Declaration text of the metadata statement (dcc:declaration)//Erklärungstext der Metadatenaussage (dcc:declaration)""",
        mandatory=False,
        section="Measurement Metadata",
    )

    drmd_valid = PropertyTypeAssignment(
        code="DRMD_VALID",
        data_type="BOOLEAN",
        property_label="Valid",
        description="""Validity flag of the metadata statement (dcc:valid)//Gültigkeitskennzeichen der Metadatenaussage (dcc:valid)""",
        mandatory=False,
        section="Measurement Metadata",
    )

    drmd_metadata_date = PropertyTypeAssignment(
        code="DRMD_METADATA_DATE",
        data_type="DATE",
        property_label="Date",
        description="""Date of the metadata statement (dcc:date)//Datum der Metadatenaussage (dcc:date)""",
        mandatory=False,
        section="Measurement Metadata",
    )

    drmd_period = PropertyTypeAssignment(
        code="DRMD_PERIOD",
        data_type="VARCHAR",
        property_label="Period",
        description="""Duration in ISO 8601 format, e.g. P2Y or P3Y2M//Zeitdauer im Format ISO 8601, z. B. P2Y oder P3Y2M""",
        mandatory=False,
        section="Measurement Metadata",
    )

    drmd_conformity = PropertyTypeAssignment(
        code="DRMD_CONFORMITY",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DRMD_CONFORMITY",
        property_label="Conformity",
        description="""Conformity status of the metadata statement (dcc:conformity)//Konformitätsstatus der Metadatenaussage (dcc:conformity)""",
        mandatory=False,
        section="Measurement Metadata",
    )

    drmd_non_si_unit = PropertyTypeAssignment(
        code="DRMD_NON_SI_UNIT",
        data_type="VARCHAR",
        property_label="Non-SI unit",
        description="""Non-SI unit defined by this metadata, as used in a si:hybrid sibling value (dcc:nonSIUnit)//Nicht-SI-Einheit, die durch diese Metadaten definiert wird, wie in einem si:hybrid-Geschwisterwert verwendet (dcc:nonSIUnit)""",
        mandatory=False,
        section="Measurement Metadata",
    )

    drmd_non_si_definition = PropertyTypeAssignment(
        code="DRMD_NON_SI_DEFINITION",
        data_type="MULTILINE_VARCHAR",
        property_label="Definition of the non-SI unit",
        description="""Definition of the non-SI unit (dcc:nonSIDefinition)//Definition der Nicht-SI-Einheit (dcc:nonSIDefinition)""",
        mandatory=False,
        section="Measurement Metadata",
    )

    drmd_position = PropertyTypeAssignment(
        code="DRMD_POSITION",
        data_type="INTEGER",
        property_label="Position",
        description="""Position of the element within its list in the DRMD document (1 = first)//Position des Elements in seiner Liste im DRMD-Dokument (1 = erstes)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_xml_id = PropertyTypeAssignment(
        code="DRMD_XML_ID",
        data_type="VARCHAR",
        property_label="XML ID",
        description="""Identifier of the element within the DRMD document, the target of @refId; leave empty to have it generated (@id, xs:ID)//Kennung des Elements innerhalb des DRMD-Dokuments, Ziel von @refId; leer lassen, damit sie erzeugt wird (@id, xs:ID)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_xml_ref_id = PropertyTypeAssignment(
        code="DRMD_XML_REF_ID",
        data_type="VARCHAR",
        property_label="XML references",
        description="""Whitespace-separated XML IDs of other elements of the same document that this element refers to (@refId, xs:IDREFS)//Durch Leerzeichen getrennte XML-IDs anderer Elemente desselben Dokuments, auf die sich dieses Element bezieht (@refId, xs:IDREFS)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_dcc_ref_type = PropertyTypeAssignment(
        code="DRMD_DCC_REF_TYPE",
        data_type="VARCHAR",
        property_label="DCC reference type",
        description="""Whitespace-separated reference type tokens of an element with a DCC type, e.g. a quantity, procedure or responsible person (@refType, dcc:refTypesType)//Durch Leerzeichen getrennte Referenztypen eines Elements mit DCC-Typ, z. B. einer Größe, eines Verfahrens oder einer verantwortlichen Person (@refType, dcc:refTypesType)""",
        mandatory=False,
        section="Document Structure",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        section="Comments",
    )


# Ontology mapping (BFO/IAO transition): IAO:0000300 (textual entity)
class DrmdStatement(ObjectType):
    defs = ObjectTypeDef(
        code="DRMD_STATEMENT",
        description="""Additional statement on the handling and use of the material that has no dedicated element (drmd:statements/drmd:statement)//Zusätzliche Aussage zur Handhabung und Verwendung des Materials ohne eigenes Element (drmd:statements/drmd:statement)""",
        generated_code_prefix="DRMD_STMT",
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
        description="""Text of the statement (dcc:content)//Text der Aussage (dcc:content)""",
        mandatory=False,
        section="General Information",
    )

    drmd_formula_latex = PropertyTypeAssignment(
        code="DRMD_FORMULA_LATEX",
        data_type="MULTILINE_VARCHAR",
        property_label="Formula (LaTeX)",
        description="""Formula belonging to the statement, in LaTeX notation (dcc:formula/dcc:latex)//Formel zur Aussage in LaTeX-Notation (dcc:formula/dcc:latex)""",
        mandatory=False,
        section="General Information",
    )

    drmd_position = PropertyTypeAssignment(
        code="DRMD_POSITION",
        data_type="INTEGER",
        property_label="Position",
        description="""Position of the element within its list in the DRMD document (1 = first)//Position des Elements in seiner Liste im DRMD-Dokument (1 = erstes)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_xml_id = PropertyTypeAssignment(
        code="DRMD_XML_ID",
        data_type="VARCHAR",
        property_label="XML ID",
        description="""Identifier of the element within the DRMD document, the target of @refId; leave empty to have it generated (@id, xs:ID)//Kennung des Elements innerhalb des DRMD-Dokuments, Ziel von @refId; leer lassen, damit sie erzeugt wird (@id, xs:ID)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_xml_ref_id = PropertyTypeAssignment(
        code="DRMD_XML_REF_ID",
        data_type="VARCHAR",
        property_label="XML references",
        description="""Whitespace-separated XML IDs of other elements of the same document that this element refers to (@refId, xs:IDREFS)//Durch Leerzeichen getrennte XML-IDs anderer Elemente desselben Dokuments, auf die sich dieses Element bezieht (@refId, xs:IDREFS)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_dcc_ref_type = PropertyTypeAssignment(
        code="DRMD_DCC_REF_TYPE",
        data_type="VARCHAR",
        property_label="DCC reference type",
        description="""Whitespace-separated reference type tokens of an element with a DCC type, e.g. a quantity, procedure or responsible person (@refType, dcc:refTypesType)//Durch Leerzeichen getrennte Referenztypen eines Elements mit DCC-Typ, z. B. einer Größe, eines Verfahrens oder einer verantwortlichen Person (@refType, dcc:refTypesType)""",
        mandatory=False,
        section="Document Structure",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        section="Comments",
    )


# Ontology mapping (BFO/IAO transition): IAO:0000030 (information content entity), digital file
class DrmdFile(ObjectType):
    defs = ObjectTypeDef(
        code="DRMD_FILE",
        description="""File embedded in a DRMD; the file itself is attached to this object as dataset. With a target property it belongs to that text of the linked object (dcc:file), without one it is the document embedded in the DRMD (drmd:document) or the description data of a contact (dcc:descriptionData)//In ein DRMD eingebettete Datei; die Datei selbst ist als Datensatz an dieses Objekt angehängt. Mit Zieleigenschaft gehört sie zu diesem Text des verknüpften Objekts (dcc:file), ohne Zieleigenschaft ist sie das im DRMD eingebettete Dokument (drmd:document) oder die Beschreibungsdaten eines Kontakts (dcc:descriptionData)""",
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
        description="""File name written to the DRMD; its extension should match the media type, e.g. EXA-1a-certificate.pdf (dcc:fileName)//In das DRMD geschriebener Dateiname; die Endung sollte zum Medientyp passen, z. B. EXA-1a-certificate.pdf (dcc:fileName)""",
        mandatory=True,
        section="General Information",
    )

    drmd_mime_type = PropertyTypeAssignment(
        code="DRMD_MIME_TYPE",
        data_type="VARCHAR",
        property_label="Media type",
        description="""Registered media (MIME) type of the file, e.g. application/pdf (dcc:mimeType)//Registrierter Medientyp (MIME-Typ) der Datei, z. B. application/pdf (dcc:mimeType)""",
        mandatory=True,
        section="General Information",
    )

    drmd_target_property = PropertyTypeAssignment(
        code="DRMD_TARGET_PROPERTY",
        data_type="VARCHAR",
        property_label="Target property",
        description="""Code of the text property of the linked object that this translation or file belongs to, e.g. $NAME, DESCRIPTION or DRMD_HEALTH_AND_SAFETY//Code der Texteigenschaft des verknüpften Objekts, zu der diese Übersetzung oder Datei gehört, z. B. $NAME, DESCRIPTION oder DRMD_HEALTH_AND_SAFETY""",
        mandatory=False,
        section="General Information",
    )

    drmd_position = PropertyTypeAssignment(
        code="DRMD_POSITION",
        data_type="INTEGER",
        property_label="Position",
        description="""Position of the element within its list in the DRMD document (1 = first)//Position des Elements in seiner Liste im DRMD-Dokument (1 = erstes)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_xml_id = PropertyTypeAssignment(
        code="DRMD_XML_ID",
        data_type="VARCHAR",
        property_label="XML ID",
        description="""Identifier of the element within the DRMD document, the target of @refId; leave empty to have it generated (@id, xs:ID)//Kennung des Elements innerhalb des DRMD-Dokuments, Ziel von @refId; leer lassen, damit sie erzeugt wird (@id, xs:ID)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_xml_ref_id = PropertyTypeAssignment(
        code="DRMD_XML_REF_ID",
        data_type="VARCHAR",
        property_label="XML references",
        description="""Whitespace-separated XML IDs of other elements of the same document that this element refers to (@refId, xs:IDREFS)//Durch Leerzeichen getrennte XML-IDs anderer Elemente desselben Dokuments, auf die sich dieses Element bezieht (@refId, xs:IDREFS)""",
        mandatory=False,
        section="Document Structure",
    )

    drmd_dcc_ref_type = PropertyTypeAssignment(
        code="DRMD_DCC_REF_TYPE",
        data_type="VARCHAR",
        property_label="DCC reference type",
        description="""Whitespace-separated reference type tokens of an element with a DCC type, e.g. a quantity, procedure or responsible person (@refType, dcc:refTypesType)//Durch Leerzeichen getrennte Referenztypen eines Elements mit DCC-Typ, z. B. einer Größe, eines Verfahrens oder einer verantwortlichen Person (@refType, dcc:refTypesType)""",
        mandatory=False,
        section="Document Structure",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        section="Comments",
    )


# Ontology mapping (BFO/IAO transition): IAO:0000300 (textual entity)
class DrmdTranslation(ObjectType):
    defs = ObjectTypeDef(
        code="DRMD_TRANSLATION",
        description="""Translation of a text property of a DRMD object into another language (dcc:content with @lang)//Übersetzung einer Texteigenschaft eines DRMD-Objekts in eine andere Sprache (dcc:content mit @lang)""",
        generated_code_prefix="DRMD_TRL",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        section="General Information",
    )

    drmd_language = PropertyTypeAssignment(
        code="DRMD_LANGUAGE",
        data_type="VARCHAR",
        property_label="Language",
        description="""Language code according to ISO 639-1 (two lower-case letters, e.g. en or de)//Sprachcode nach ISO 639-1 (zwei Kleinbuchstaben, z. B. en oder de)""",
        mandatory=True,
        section="General Information",
    )

    drmd_target_property = PropertyTypeAssignment(
        code="DRMD_TARGET_PROPERTY",
        data_type="VARCHAR",
        property_label="Target property",
        description="""Code of the text property of the linked object that this translation or file belongs to, e.g. $NAME, DESCRIPTION or DRMD_HEALTH_AND_SAFETY//Code der Texteigenschaft des verknüpften Objekts, zu der diese Übersetzung oder Datei gehört, z. B. $NAME, DESCRIPTION oder DRMD_HEALTH_AND_SAFETY""",
        mandatory=True,
        section="General Information",
    )

    drmd_translated_text = PropertyTypeAssignment(
        code="DRMD_TRANSLATED_TEXT",
        data_type="MULTILINE_VARCHAR",
        property_label="Translated text",
        description="""Text in the language given in DRMD_LANGUAGE (dcc:content with @lang)//Text in der unter DRMD_LANGUAGE angegebenen Sprache (dcc:content mit @lang)""",
        mandatory=True,
        section="General Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        section="Comments",
    )
