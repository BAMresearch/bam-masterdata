from bam_masterdata.metadata.definitions import PropertyTypeDef

AnnotationsState = PropertyTypeDef(
    code='$ANNOTATIONS_STATE',
    description='Annotations State',
    data_type='XML',
    property_label='Annotations State',
)


Barcode = PropertyTypeDef(
    code='$BARCODE',
    description='Custom Barcode',
    data_type='VARCHAR',
    property_label='Custom Barcode',
)


DefaultCollectionView = PropertyTypeDef(
    code='$DEFAULT_COLLECTION_VIEW',
    description='Default view for experiments of the type collection',
    data_type='CONTROLLEDVOCABULARY',
    property_label='Default collection view',
)


DefaultObjectType = PropertyTypeDef(
    code='$DEFAULT_OBJECT_TYPE',
    description='Enter the code of the object type for which the collection is used',
    data_type='VARCHAR',
    property_label='Default object type',
)


Document = PropertyTypeDef(
    code='$DOCUMENT',
    description='Document',
    data_type='MULTILINE_VARCHAR',
    property_label='Document',
)


ElnSettings = PropertyTypeDef(
    code='$ELN_SETTINGS',
    description='ELN Settings',
    data_type='VARCHAR',
    property_label='ELN Settings',
)


HistoryId = PropertyTypeDef(
    code='$HISTORY_ID',
    description='History ID',
    data_type='VARCHAR',
    property_label='History ID',
)


Name = PropertyTypeDef(
    code='$NAME',
    description='Name',
    data_type='VARCHAR',
    property_label='Name',
)


AdditionalInformation = PropertyTypeDef(
    code='$ORDER.ADDITIONAL_INFORMATION',
    description='Additional Information',
    data_type='VARCHAR',
    property_label='Additional Information',
)


BillTo = PropertyTypeDef(
    code='$ORDER.BILL_TO',
    description='Bill To',
    data_type='VARCHAR',
    property_label='Bill To',
)


ContactFax = PropertyTypeDef(
    code='$ORDER.CONTACT_FAX',
    description='Fax',
    data_type='VARCHAR',
    property_label='Fax',
)


ContactPhone = PropertyTypeDef(
    code='$ORDER.CONTACT_PHONE',
    description='Phone',
    data_type='VARCHAR',
    property_label='Phone',
)


OrderState = PropertyTypeDef(
    code='$ORDER.ORDER_STATE',
    description='Order State',
    data_type='VARCHAR',
    property_label='Order State',
)


ShipAddress = PropertyTypeDef(
    code='$ORDER.SHIP_ADDRESS',
    description='Ship Address',
    data_type='VARCHAR',
    property_label='Ship Address',
)


ShipTo = PropertyTypeDef(
    code='$ORDER.SHIP_TO',
    description='Ship To',
    data_type='VARCHAR',
    property_label='Ship To',
)


OrderStatus = PropertyTypeDef(
    code='$ORDERING.ORDER_STATUS',
    description='Order Status',
    data_type='CONTROLLEDVOCABULARY',
    property_label='Order Status',
)


CatalogNum = PropertyTypeDef(
    code='$PRODUCT.CATALOG_NUM',
    description='Catalog Number',
    data_type='VARCHAR',
    property_label='Catalog Number',
)


Currency = PropertyTypeDef(
    code='$PRODUCT.CURRENCY',
    description='Currency',
    data_type='CONTROLLEDVOCABULARY',
    property_label='Currency',
)


PricePerUnit = PropertyTypeDef(
    code='$PRODUCT.PRICE_PER_UNIT',
    description='Estimated Price',
    data_type='REAL',
    property_label='Estimated Price',
)


Description = PropertyTypeDef(
    code='$PUBLICATION.DESCRIPTION',
    description='Description',
    data_type='VARCHAR',
    property_label='Description',
)


Identifier = PropertyTypeDef(
    code='$PUBLICATION.IDENTIFIER',
    description='Digital Object Identifier',
    data_type='VARCHAR',
    property_label='DOI',
)


OpenbisRelatedIdentifiers = PropertyTypeDef(
    code='$PUBLICATION.OPENBIS_RELATED_IDENTIFIERS',
    description='openBIS Related Identifiers',
    data_type='VARCHAR',
    property_label='openBIS Related Identifiers',
)


Organization = PropertyTypeDef(
    code='$PUBLICATION.ORGANIZATION',
    description='Organization',
    data_type='VARCHAR',
    property_label='Organization',
)


Type = PropertyTypeDef(
    code='$PUBLICATION.TYPE',
    description='Type',
    data_type='VARCHAR',
    property_label='Type',
)


Url = PropertyTypeDef(
    code='$PUBLICATION.URL',
    description='URL',
    data_type='HYPERLINK',
    property_label='URL',
)


CustomData = PropertyTypeDef(
    code='$SEARCH_QUERY.CUSTOM_DATA',
    description='Additional data in custom format',
    data_type='XML',
    property_label='Custom data',
)


FetchOptions = PropertyTypeDef(
    code='$SEARCH_QUERY.FETCH_OPTIONS',
    description='V3 API fetch options',
    data_type='XML',
    property_label='Fetch options',
)


SearchCriteria = PropertyTypeDef(
    code='$SEARCH_QUERY.SEARCH_CRITERIA',
    description='V3 API search criteria',
    data_type='XML',
    property_label='Search criteria',
)


ShowInProjectOverview = PropertyTypeDef(
    code='$SHOW_IN_PROJECT_OVERVIEW',
    description='Show in project overview page',
    data_type='BOOLEAN',
    property_label='Show in project overview',
)


BoxNum = PropertyTypeDef(
    code='$STORAGE.BOX_NUM',
    description='Allowed number of Boxes in a rack',
    data_type='INTEGER',
    property_label='Number of Boxes',
)


BoxSpaceWarning = PropertyTypeDef(
    code='$STORAGE.BOX_SPACE_WARNING',
    description='Number between 0 and 99, represents a percentage',
    data_type='INTEGER',
    property_label='Box Space Warning',
)


ColumnNum = PropertyTypeDef(
    code='$STORAGE.COLUMN_NUM',
    description='Number of Columns',
    data_type='INTEGER',
    property_label='Number of Columns',
)


RowNum = PropertyTypeDef(
    code='$STORAGE.ROW_NUM',
    description='Number of Rows',
    data_type='INTEGER',
    property_label='Number of Rows',
)


StorageSpaceWarning = PropertyTypeDef(
    code='$STORAGE.STORAGE_SPACE_WARNING',
    description='Number between 0 and 99, represents a percentage',
    data_type='INTEGER',
    property_label='Rack Space Warning',
)


StorageValidationLevel = PropertyTypeDef(
    code='$STORAGE.STORAGE_VALIDATION_LEVEL',
    description='Validation level',
    data_type='CONTROLLEDVOCABULARY',
    property_label='Validation level',
)


StorageBoxName = PropertyTypeDef(
    code='$STORAGE_POSITION.STORAGE_BOX_NAME',
    description='Box Name',
    data_type='VARCHAR',
    property_label='Storage Box Name',
)


StorageBoxPosition = PropertyTypeDef(
    code='$STORAGE_POSITION.STORAGE_BOX_POSITION',
    description='Box Position',
    data_type='VARCHAR',
    property_label='Storage Box Position',
)


StorageBoxSize = PropertyTypeDef(
    code='$STORAGE_POSITION.STORAGE_BOX_SIZE',
    description='Box Size',
    data_type='CONTROLLEDVOCABULARY',
    property_label='Storage Box Size',
)


StorageCode = PropertyTypeDef(
    code='$STORAGE_POSITION.STORAGE_CODE',
    description='Storage Code',
    data_type='VARCHAR',
    property_label='Storage Code',
)


StorageRackColumn = PropertyTypeDef(
    code='$STORAGE_POSITION.STORAGE_RACK_COLUMN',
    description='Number of Columns',
    data_type='INTEGER',
    property_label='Storage Rack Column',
)


StorageRackRow = PropertyTypeDef(
    code='$STORAGE_POSITION.STORAGE_RACK_ROW',
    description='Number of Rows',
    data_type='INTEGER',
    property_label='Storage Rack Row',
)


StorageUser = PropertyTypeDef(
    code='$STORAGE_POSITION.STORAGE_USER',
    description='Storage User Id',
    data_type='VARCHAR',
    property_label='Storage User Id',
)


CompanyAddressLine1 = PropertyTypeDef(
    code='$SUPPLIER.COMPANY_ADDRESS_LINE_1',
    description='Company address',
    data_type='VARCHAR',
    property_label='Company address',
)


CompanyAddressLine2 = PropertyTypeDef(
    code='$SUPPLIER.COMPANY_ADDRESS_LINE_2',
    description='Company address, line 2',
    data_type='VARCHAR',
    property_label='Company address, line 2',
)


CompanyEmail = PropertyTypeDef(
    code='$SUPPLIER.COMPANY_EMAIL',
    description='Company email',
    data_type='VARCHAR',
    property_label='Company email',
)


CompanyFax = PropertyTypeDef(
    code='$SUPPLIER.COMPANY_FAX',
    description='Company fax',
    data_type='VARCHAR',
    property_label='Company fax',
)


CompanyLanguage = PropertyTypeDef(
    code='$SUPPLIER.COMPANY_LANGUAGE',
    description='Company language',
    data_type='CONTROLLEDVOCABULARY',
    property_label='Company language',
)


CompanyPhone = PropertyTypeDef(
    code='$SUPPLIER.COMPANY_PHONE',
    description='Company phone',
    data_type='VARCHAR',
    property_label='Company phone',
)


CustomerNumber = PropertyTypeDef(
    code='$SUPPLIER.CUSTOMER_NUMBER',
    description='Customer number',
    data_type='VARCHAR',
    property_label='Customer number',
)


ColorEncodedAnnotation = PropertyTypeDef(
    code='$WELL.COLOR_ENCODED_ANNOTATION',
    description='Color Annotation for plate wells',
    data_type='CONTROLLEDVOCABULARY',
    property_label='Color Annotation',
)


Xmlcomments = PropertyTypeDef(
    code='$XMLCOMMENTS',
    description='Comments log',
    data_type='XML',
    property_label='Comments',
)


Alias = PropertyTypeDef(
    code='ALIAS',
    description='e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname//z.B. Abkürzung oder Spitzname',
    data_type='VARCHAR',
    property_label='Alternative Name',
)


AllowDropboxImport = PropertyTypeDef(
    code='ALLOW_DROPBOX_IMPORT',
    description='Checks if Dropbox import is available for the experiment',
    data_type='BOOLEAN',
    property_label='ALLOW_DROPBOX_IMPORT',
)


Amount = PropertyTypeDef(
    code='AMOUNT',
    description='C',
    data_type='REAL',
    property_label='AMOUNT',
)


AmountUnit = PropertyTypeDef(
    code='AMOUNT_UNIT',
    description='Amount unit of the object',
    data_type='CONTROLLEDVOCABULARY',
    property_label='AMOUNT_UNIT',
)


QuantityOfItems = PropertyTypeDef(
    code='ANNOTATION.REQUEST.QUANTITY_OF_ITEMS',
    description='Quantity of Items',
    data_type='INTEGER',
    property_label='Quantity of Items',
)


Comments = PropertyTypeDef(
    code='ANNOTATION.SYSTEM.COMMENTS',
    description='Comments',
    data_type='VARCHAR',
    property_label='Comments',
)


BamFieldOfActivity = PropertyTypeDef(
    code='BAM_FIELD_OF_ACTIVITY',
    description='Field of Activity Testing',
    data_type='CONTROLLEDVOCABULARY',
    property_label='Field of Activity',
)


BamFloor = PropertyTypeDef(
    code='BAM_FLOOR',
    description='BAM Floor//BAM Etage',
    data_type='CONTROLLEDVOCABULARY',
    property_label='BAM_FLOOR',
)


BamFocusArea = PropertyTypeDef(
    code='BAM_FOCUS_AREA',
    description='Bam Focus Area Testing',
    data_type='MULTILINE_VARCHAR',
    property_label='Bam Focus Area',
)


BamFocusAreaV2 = PropertyTypeDef(
    code='BAM_FOCUS_AREA_V2',
    description='BAM Focus Area//BAM Themenfeld',
    data_type='CONTROLLEDVOCABULARY',
    property_label='BAM Focus Area',
)


BamHouse = PropertyTypeDef(
    code='BAM_HOUSE',
    description='BAM House//BAM Gebäude/Haus',
    data_type='CONTROLLEDVOCABULARY',
    property_label='BAM_HOUSE',
)


BamLocation = PropertyTypeDef(
    code='BAM_LOCATION',
    description='BAM Location//BAM Standort/Liegenschaft',
    data_type='CONTROLLEDVOCABULARY',
    property_label='BAM_LOCATION',
)


BamLocationComplete = PropertyTypeDef(
    code='BAM_LOCATION_COMPLETE',
    description='Complete location (up to room level)//Komplette Ortsangabe (bis Raumlevel)',
    data_type='CONTROLLEDVOCABULARY',
    property_label='BAM_LOCATION_COMPLETE',
)


BamRoom = PropertyTypeDef(
    code='BAM_ROOM',
    description='BAM Room//BAM Raum',
    data_type='CONTROLLEDVOCABULARY',
    property_label='BAM_ROOM',
)


BarcodeExternal = PropertyTypeDef(
    code='BARCODE_EXTERNAL',
    description='External Barcode (non-openBIS)//Externer Barcode (nicht von openBIS vergeben)',
    data_type='VARCHAR',
    property_label='External Barcode',
)


BaDynTest = PropertyTypeDef(
    code='BA_DYN_TEST',
    description='Testing Dynamic Scripts fetching',
    data_type='CONTROLLEDVOCABULARY',
    property_label='BAM_DYN',
)


Building = PropertyTypeDef(
    code='BUILDING',
    description='BUILDING (LOCATION) AT BAM',
    data_type='CONTROLLEDVOCABULARY',
    property_label='BUILDING',
)


CasNumber = PropertyTypeDef(
    code='CAS_NUMBER',
    description='CAS Registry Number (corresponds to field "CAS-No." in the Hazardous Materials Inventory (GSM) of BAM)//CAS-Nummer (entspricht Feld "CAS-Nr." aus dem Gefahrstoffmanagement (GSM) der BAM)',
    data_type='VARCHAR',
    property_label='CAS Registry Number',
)


Concentration = PropertyTypeDef(
    code='CONCENTRATION',
    description='Concentration [%] (corresponds to field "Concentration %" in the Hazardous Materials Inventory (GSM) of BAM)//Konzentration [%] (entspricht Feld "Konzentration %" aus dem Gefahrstoffmanagement (GSM) der BAM)',
    data_type='REAL',
    property_label='Concentration',
)


DateBottling = PropertyTypeDef(
    code='DATE_BOTTLING',
    description='Date of Bottling//Abfülldatum',
    data_type='DATE',
    property_label='Bottling Date',
)


DateExpiration = PropertyTypeDef(
    code='DATE_EXPIRATION',
    description='Expiration Date//Verfallsdatum',
    data_type='DATE',
    property_label='Expiration Date',
)


DateOpening = PropertyTypeDef(
    code='DATE_OPENING',
    description='Opening Data//Öffnungsdatum',
    data_type='DATE',
    property_label='Opening Date',
)


ExperimentalDescription = PropertyTypeDef(
    code='DEFAULT_EXPERIMENT.EXPERIMENTAL_DESCRIPTION',
    description='Description of the experiment',
    data_type='MULTILINE_VARCHAR',
    property_label='Description',
)


ExperimentalGoals = PropertyTypeDef(
    code='DEFAULT_EXPERIMENT.EXPERIMENTAL_GOALS',
    description='Goals of the experiment',
    data_type='MULTILINE_VARCHAR',
    property_label='Goals',
)


ExperimentalResults = PropertyTypeDef(
    code='DEFAULT_EXPERIMENT.EXPERIMENTAL_RESULTS',
    description='Summary of  experimental results',
    data_type='MULTILINE_VARCHAR',
    property_label='Results',
)


Grant = PropertyTypeDef(
    code='DEFAULT_EXPERIMENT.GRANT',
    description='Grant',
    data_type='VARCHAR',
    property_label='Grant',
)


DensityGramPerCubicCm = PropertyTypeDef(
    code='DENSITY_GRAM_PER_CUBIC_CM',
    description='Density [g/cm³]//Dichte [g/cm³]',
    data_type='REAL',
    property_label='Density',
)


Description = PropertyTypeDef(
    code='DESCRIPTION',
    description='A Description',
    data_type='VARCHAR',
    property_label='Description',
)


EndDate = PropertyTypeDef(
    code='END_DATE',
    description='End date',
    data_type='TIMESTAMP',
    property_label='End date',
)


ExperimentalDescription = PropertyTypeDef(
    code='EXPERIMENTAL_STEP.EXPERIMENTAL_DESCRIPTION',
    description='Description of the experiment',
    data_type='MULTILINE_VARCHAR',
    property_label='Experimental description',
)


ExperimentalGoals = PropertyTypeDef(
    code='EXPERIMENTAL_STEP.EXPERIMENTAL_GOALS',
    description='Goals of the experiment',
    data_type='MULTILINE_VARCHAR',
    property_label='Experimental goals',
)


ExperimentalResults = PropertyTypeDef(
    code='EXPERIMENTAL_STEP.EXPERIMENTAL_RESULTS',
    description='Summary of  experimental results',
    data_type='MULTILINE_VARCHAR',
    property_label='Experimental results',
)


Spreadsheet = PropertyTypeDef(
    code='EXPERIMENTAL_STEP.SPREADSHEET',
    description='Multi purpose Spreatsheet',
    data_type='XML',
    property_label='Spreadsheet',
)


FinishedFlag = PropertyTypeDef(
    code='FINISHED_FLAG',
    description='Marks the experiment as finished',
    data_type='BOOLEAN',
    property_label='Experiment completed',
)


ForWhat = PropertyTypeDef(
    code='FOR_WHAT',
    description='For what',
    data_type='MULTILINE_VARCHAR',
    property_label='For what',
)


FreqCheck = PropertyTypeDef(
    code='FREQ_CHECK',
    description='Time required to check in Days//Überprüfungsintervall in Tagen',
    data_type='INTEGER',
    property_label='Frequency of check',
)


Materials = PropertyTypeDef(
    code='GENERAL_PROTOCOL.MATERIALS',
    description='Machines (and relative set up)',
    data_type='MULTILINE_VARCHAR',
    property_label='Materials',
)


ProtocolEvaluation = PropertyTypeDef(
    code='GENERAL_PROTOCOL.PROTOCOL_EVALUATION',
    description='Parameters and observations to meet the minimal efficiency of the protocol',
    data_type='MULTILINE_VARCHAR',
    property_label='Protocol evaluation',
)


ProtocolType = PropertyTypeDef(
    code='GENERAL_PROTOCOL.PROTOCOL_TYPE',
    description='Category the protocol belongs to',
    data_type='MULTILINE_VARCHAR',
    property_label='Protocol type',
)


Spreadsheet = PropertyTypeDef(
    code='GENERAL_PROTOCOL.SPREADSHEET',
    description='Multi purpose Spreatsheet',
    data_type='XML',
    property_label='Spreadsheet',
)


TimeRequirement = PropertyTypeDef(
    code='GENERAL_PROTOCOL.TIME_REQUIREMENT',
    description='Time required to complete a protocol',
    data_type='MULTILINE_VARCHAR',
    property_label='Time requirement',
)


HazardousSubstance = PropertyTypeDef(
    code='HAZARDOUS_SUBSTANCE',
    description='Is the chemical a  hazardous substance according to the Hazardous Substances Ordinance (GefStoffV)?//Handelt es sich bei der Chemikalie um einen Gefahrenstoff nach der Gefahrenstoffverordnung (GefStoffV)?',
    data_type='BOOLEAN',
    property_label='Hazardous Substance',
)


Housec = PropertyTypeDef(
    code='HOUSEC',
    description='HOUSE AT BAM',
    data_type='CONTROLLEDVOCABULARY',
    property_label='HOUSE',
)


IupacName = PropertyTypeDef(
    code='IUPAC_NAME',
    description='IUPAC Name//IUPAC-Name',
    data_type='VARCHAR',
    property_label='IUPAC Name',
)


LastCheck = PropertyTypeDef(
    code='LAST_CHECK',
    description='Date of the last check//Datum der letzten Überprüfung',
    data_type='DATE',
    property_label='Date of last check',
)


Level = PropertyTypeDef(
    code='LEVEL',
    description='FLOOR / LEVEL INSIDE THE HOUSES AT BAM',
    data_type='CONTROLLEDVOCABULARY',
    property_label='LEVEL',
)


LotNumber = PropertyTypeDef(
    code='LOT_NUMBER',
    description='Lot/Batch Number//Chargennummer',
    data_type='VARCHAR',
    property_label='Lot/Batch Number',
)


Manufacturer = PropertyTypeDef(
    code='MANUFACTURER',
    description='Manufacturer (corresponds to field "Supplier" in the Hazardous Materials Inventory (GSM) of BAM)//Hersteller (entspricht Feld "Hersteller" aus dem Gefahrstoffmanagement (GSM) der BAM)',
    data_type='VARCHAR',
    property_label='Manufacturer',
)


MassMolar = PropertyTypeDef(
    code='MASS_MOLAR',
    description='Molar Mass [g/mol]//Molare Masse [g/mol]',
    data_type='REAL',
    property_label='Molar Mass',
)


Notes = PropertyTypeDef(
    code='NOTES',
    description='Notes',
    data_type='MULTILINE_VARCHAR',
    property_label='Notes',
)


PricePaid = PropertyTypeDef(
    code='ORDER.PRICE_PAID',
    description='Price Paid',
    data_type='REAL',
    property_label='Price Paid',
)


Percentage = PropertyTypeDef(
    code='PERCENTAGE',
    description='PERCENTAGE',
    data_type='REAL',
    property_label='PERCENTAGE',
)


PositiveNumber = PropertyTypeDef(
    code='POSITIVE_NUMBER',
    description='POSITIVE_NUMBER',
    data_type='REAL',
    property_label='POSITIVE_NUMBER',
)


Procedure = PropertyTypeDef(
    code='PROCEDURE',
    description='Step-by-step procedure',
    data_type='MULTILINE_VARCHAR',
    property_label='Procedure',
)


Category = PropertyTypeDef(
    code='PRODUCT.CATEGORY',
    description='Category',
    data_type='VARCHAR',
    property_label='Category',
)


Company = PropertyTypeDef(
    code='PRODUCT.COMPANY',
    description='Company',
    data_type='VARCHAR',
    property_label='Company',
)


Description = PropertyTypeDef(
    code='PRODUCT.DESCRIPTION',
    description='Description',
    data_type='MULTILINE_VARCHAR',
    property_label='Description',
)


HazardStatement = PropertyTypeDef(
    code='PRODUCT.HAZARD_STATEMENT',
    description='Hazard Statement',
    data_type='VARCHAR',
    property_label='Hazard Statement',
)


ProductSecondaryNames = PropertyTypeDef(
    code='PRODUCT.PRODUCT_SECONDARY_NAMES',
    description='Product Secondary Names',
    data_type='VARCHAR',
    property_label='Product Secondary Names',
)


SizeOfItem = PropertyTypeDef(
    code='PRODUCT.SIZE_OF_ITEM',
    description='Size of Item',
    data_type='VARCHAR',
    property_label='Size of Item',
)


Prop1 = PropertyTypeDef(
    code='PROP1',
    description='PROP1',
    data_type='REAL',
    property_label='PROP1',
)


Prop2 = PropertyTypeDef(
    code='PROP2',
    description='PROP2',
    data_type='REAL',
    property_label='PROP2',
)


Prop3 = PropertyTypeDef(
    code='PROP3',
    description='PROP3',
    data_type='REAL',
    property_label='PROP3',
)


Publication = PropertyTypeDef(
    code='PUBLICATION',
    description='Own publication where this entity is referenced',
    data_type='MULTILINE_VARCHAR',
    property_label='Publication',
)


RandomNumber = PropertyTypeDef(
    code='RANDOM_NUMBER',
    description='RANDOM NUMBER',
    data_type='INTEGER',
    property_label='NUMBER',
)


RectangleArea = PropertyTypeDef(
    code='RECTANGLE_AREA',
    description='Rectangle area [m²]//Fläche des Rechtecks [m²]',
    data_type='REAL',
    property_label='Rectangle area [m²]',
)


RectangleAreaInQm = PropertyTypeDef(
    code='RECTANGLE_AREA_IN_QM',
    description='Rectangle area [m²]//Fläche des Rechtecks [m²]',
    data_type='REAL',
    property_label='Rectangle area [m²]',
)


RectangleLength = PropertyTypeDef(
    code='RECTANGLE_LENGTH',
    description='Rectangle length [m]//Länge des Rechtecks [m]',
    data_type='REAL',
    property_label='Rectangle length [m]',
)


RectangleLengthInM = PropertyTypeDef(
    code='RECTANGLE_LENGTH_IN_M',
    description='Rectangle length [m]//Länge des Rechtecks [m]',
    data_type='REAL',
    property_label='Rectangle length [m]',
)


RectangleWidth = PropertyTypeDef(
    code='RECTANGLE_WIDTH',
    description='Rectangle width [m]//Breite des Rechtecks [m]',
    data_type='REAL',
    property_label='Rectangle width [m]',
)


RectangleWidthInM = PropertyTypeDef(
    code='RECTANGLE_WIDTH_IN_M',
    description='Rectangle width [m]//Breite des Rechtecks [m]',
    data_type='REAL',
    property_label='Rectangle width [m]',
)


Reference = PropertyTypeDef(
    code='REFERENCE',
    description='Useful refences',
    data_type='MULTILINE_VARCHAR',
    property_label='References',
)


Buyer = PropertyTypeDef(
    code='REQUEST.BUYER',
    description='Buyer',
    data_type='VARCHAR',
    property_label='Buyer',
)


Department = PropertyTypeDef(
    code='REQUEST.DEPARTMENT',
    description='Department',
    data_type='VARCHAR',
    property_label='Department',
)


Project = PropertyTypeDef(
    code='REQUEST.PROJECT',
    description='Project',
    data_type='VARCHAR',
    property_label='Project',
)


ResponsiblePerson = PropertyTypeDef(
    code='RESPONSIBLE_PERSON',
    description='Responsible Person: "Last name, first name"//Verantwortliche Person: "Name, Vorname"',
    data_type='VARCHAR',
    property_label='Responsible Person',
)


Roomc = PropertyTypeDef(
    code='ROOMC',
    description='LOCATION AT BAM',
    data_type='CONTROLLEDVOCABULARY',
    property_label='LOCATION',
)


RoomNumberC = PropertyTypeDef(
    code='ROOM_NUMBER_C',
    description='ROOM INSIDE THE HOUSES AT BAM',
    data_type='CONTROLLEDVOCABULARY',
    property_label='ROOM',
)


StartDate = PropertyTypeDef(
    code='START_DATE',
    description='Start date',
    data_type='TIMESTAMP',
    property_label='Start date',
)


StateCheck = PropertyTypeDef(
    code='STATE_CHECK',
    description='TRUE if onject needs to be checked//WAHR wenn das Objekt überprüft werden muss',
    data_type='BOOLEAN',
    property_label='Status of check',
)


SubstanceEmpty = PropertyTypeDef(
    code='SUBSTANCE_EMPTY',
    description='Is the substance used up?//Ist die Substanz aufgebraucht?',
    data_type='BOOLEAN',
    property_label='Empty',
)


Supplier = PropertyTypeDef(
    code='SUPPLIER',
    description='Supplier//Lieferant',
    data_type='VARCHAR',
    property_label='Supplier',
)


AdditionalInformation = PropertyTypeDef(
    code='SUPPLIER.ADDITIONAL_INFORMATION',
    description='Additional Information',
    data_type='VARCHAR',
    property_label='Additional Information',
)


CompanyContactEmail = PropertyTypeDef(
    code='SUPPLIER.COMPANY_CONTACT_EMAIL',
    description='Company contact email',
    data_type='VARCHAR',
    property_label='Company contact email',
)


CompanyContactName = PropertyTypeDef(
    code='SUPPLIER.COMPANY_CONTACT_NAME',
    description='Company contact name',
    data_type='VARCHAR',
    property_label='Company contact name',
)


PreferredOrderMethod = PropertyTypeDef(
    code='SUPPLIER.PREFERRED_ORDER_METHOD',
    description='Preferred order method',
    data_type='CONTROLLEDVOCABULARY',
    property_label='Preferred order method',
)


Url = PropertyTypeDef(
    code='SUPPLIER.URL',
    description='URL',
    data_type='HYPERLINK',
    property_label='URL',
)


TestVocab = PropertyTypeDef(
    code='TEST_VOCAB',
    description='Test_Vocab',
    data_type='CONTROLLEDVOCABULARY',
    property_label='Test_Vocab',
)
