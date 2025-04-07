from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.entities import ObjectType


class SearchQuery(ObjectType):
    defs = ObjectTypeDef(
        code="SEARCH_QUERY",
        description="""""",
        generated_code_prefix="SEARCH_QUERY.",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    search_query_search_criteria = PropertyTypeAssignment(
        code="$SEARCH_QUERY.SEARCH_CRITERIA",
        data_type="XML",
        property_label="Search criteria",
        description="""V3 API search criteria""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    search_query_fetch_options = PropertyTypeAssignment(
        code="$SEARCH_QUERY.FETCH_OPTIONS",
        data_type="XML",
        property_label="Fetch options",
        description="""V3 API fetch options""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    search_query_custom_data = PropertyTypeAssignment(
        code="$SEARCH_QUERY.CUSTOM_DATA",
        data_type="XML",
        property_label="Custom data",
        description="""Additional data in custom format""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )


class GeneralElnSettings(ObjectType):
    defs = ObjectTypeDef(
        code="GENERAL_ELN_SETTINGS",
        description="""""",
        generated_code_prefix="S",
    )

    eln_settings = PropertyTypeAssignment(
        code="$ELN_SETTINGS",
        data_type="VARCHAR",
        property_label="ELN Settings",
        description="""ELN Settings""",
        mandatory=False,
        show_in_edit_views=False,
        section="Settings",
    )


class Entry(ObjectType):
    defs = ObjectTypeDef(
        code="ENTRY",
        description="""""",
        generated_code_prefix="ENTRY",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    show_in_project_overview = PropertyTypeAssignment(
        code="$SHOW_IN_PROJECT_OVERVIEW",
        data_type="BOOLEAN",
        property_label="Show in project overview",
        description="""Show in project overview page""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    document = PropertyTypeAssignment(
        code="$DOCUMENT",
        data_type="MULTILINE_VARCHAR",
        property_label="Document",
        description="""Document""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class GeneralProtocol(ObjectType):
    defs = ObjectTypeDef(
        code="GENERAL_PROTOCOL",
        description="""""",
        generated_code_prefix="GEN",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    for_what = PropertyTypeAssignment(
        code="FOR_WHAT",
        data_type="MULTILINE_VARCHAR",
        property_label="For what",
        description="""For what""",
        mandatory=False,
        show_in_edit_views=False,
        section="Details",
    )

    general_protocol_protocol_type = PropertyTypeAssignment(
        code="GENERAL_PROTOCOL.PROTOCOL_TYPE",
        data_type="MULTILINE_VARCHAR",
        property_label="Protocol type",
        description="""Category the protocol belongs to""",
        mandatory=False,
        show_in_edit_views=False,
        section="Details",
    )

    general_protocol_materials = PropertyTypeAssignment(
        code="GENERAL_PROTOCOL.MATERIALS",
        data_type="MULTILINE_VARCHAR",
        property_label="Materials",
        description="""Machines (and relative set up)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Details",
    )

    general_protocol_time_requirement = PropertyTypeAssignment(
        code="GENERAL_PROTOCOL.TIME_REQUIREMENT",
        data_type="MULTILINE_VARCHAR",
        property_label="Time requirement",
        description="""Time required to complete a protocol""",
        mandatory=False,
        show_in_edit_views=False,
        section="Details",
    )

    procedure = PropertyTypeAssignment(
        code="PROCEDURE",
        data_type="MULTILINE_VARCHAR",
        property_label="Procedure",
        description="""Step-by-step procedure""",
        mandatory=False,
        show_in_edit_views=False,
        section="Details",
    )

    general_protocol_protocol_evaluation = PropertyTypeAssignment(
        code="GENERAL_PROTOCOL.PROTOCOL_EVALUATION",
        data_type="MULTILINE_VARCHAR",
        property_label="Protocol evaluation",
        description="""Parameters and observations to meet the minimal efficiency of the protocol""",
        mandatory=False,
        show_in_edit_views=False,
        section="Details",
    )

    general_protocol_spreadsheet = PropertyTypeAssignment(
        code="GENERAL_PROTOCOL.SPREADSHEET",
        data_type="XML",
        property_label="Spreadsheet",
        description="""Multi purpose Spreatsheet""",
        mandatory=False,
        show_in_edit_views=False,
        section="Details",
    )

    reference = PropertyTypeAssignment(
        code="REFERENCE",
        data_type="MULTILINE_VARCHAR",
        property_label="References",
        description="""Useful refences""",
        mandatory=False,
        show_in_edit_views=False,
        section="References",
    )

    publication = PropertyTypeAssignment(
        code="PUBLICATION",
        data_type="MULTILINE_VARCHAR",
        property_label="Publication",
        description="""Own publication where this entity is referenced""",
        mandatory=False,
        show_in_edit_views=False,
        section="References",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class ExperimentalStep(ObjectType):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP",
        description="""Experimental Step (generic)//Experimenteller Schritt (allgemein)""",
        generated_code_prefix="EXP",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    show_in_project_overview = PropertyTypeAssignment(
        code="$SHOW_IN_PROJECT_OVERVIEW",
        data_type="BOOLEAN",
        property_label="Show in project overview",
        description="""Show in project overview page""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    finished_flag = PropertyTypeAssignment(
        code="FINISHED_FLAG",
        data_type="BOOLEAN",
        property_label="Experiment completed",
        description="""Marks the experiment as finished//Markiert das Experiment als abgeschlossen""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    start_date = PropertyTypeAssignment(
        code="START_DATE",
        data_type="TIMESTAMP",
        property_label="Start date",
        description="""Start date//Startdatum""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    end_date = PropertyTypeAssignment(
        code="END_DATE",
        data_type="TIMESTAMP",
        property_label="End date",
        description="""End date//Enddatum""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    experimental_step_experimental_goals = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.EXPERIMENTAL_GOALS",
        data_type="MULTILINE_VARCHAR",
        property_label="Experimental goals",
        description="""Goals of the experiment//Ziele des Experiments""",
        mandatory=False,
        show_in_edit_views=False,
        section="Experimental Details",
    )

    experimental_step_experimental_description = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.EXPERIMENTAL_DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Experimental description",
        description="""Description of the experiment//Beschreibung des Experiments""",
        mandatory=False,
        show_in_edit_views=False,
        section="Experimental Details",
    )

    experimental_step_experimental_results = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.EXPERIMENTAL_RESULTS",
        data_type="MULTILINE_VARCHAR",
        property_label="Experimental results",
        description="""Summary of experimental results//Zusammenfassung der Ergebnisse des Experiments""",
        mandatory=False,
        show_in_edit_views=False,
        section="Experimental Details",
    )

    experimental_step_spreadsheet = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.SPREADSHEET",
        data_type="XML",
        property_label="Spreadsheet",
        description="""Multi-purpose Spreadsheet//Spreadsheet zur freien Verwendung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Experimental Details",
    )

    reference = PropertyTypeAssignment(
        code="REFERENCE",
        data_type="MULTILINE_VARCHAR",
        property_label="References",
        description="""Useful refences""",
        mandatory=False,
        show_in_edit_views=False,
        section="References",
    )

    publication = PropertyTypeAssignment(
        code="PUBLICATION",
        data_type="MULTILINE_VARCHAR",
        property_label="Publication",
        description="""Own publication where this entity is referenced""",
        mandatory=False,
        show_in_edit_views=False,
        section="References",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class Storage(ObjectType):
    defs = ObjectTypeDef(
        code="STORAGE",
        description="""""",
        generated_code_prefix="S",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    storage_row_num = PropertyTypeAssignment(
        code="$STORAGE.ROW_NUM",
        data_type="INTEGER",
        property_label="Number of Rows",
        description="""Number of Rows""",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    storage_column_num = PropertyTypeAssignment(
        code="$STORAGE.COLUMN_NUM",
        data_type="INTEGER",
        property_label="Number of Columns",
        description="""Number of Columns""",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    storage_box_num = PropertyTypeAssignment(
        code="$STORAGE.BOX_NUM",
        data_type="INTEGER",
        property_label="Number of Boxes",
        description="""Allowed number of Boxes in a rack""",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    storage_storage_space_warning = PropertyTypeAssignment(
        code="$STORAGE.STORAGE_SPACE_WARNING",
        data_type="INTEGER",
        property_label="Rack Space Warning",
        description="""Number between 0 and 99, represents a percentage""",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    storage_box_space_warning = PropertyTypeAssignment(
        code="$STORAGE.BOX_SPACE_WARNING",
        data_type="INTEGER",
        property_label="Box Space Warning",
        description="""Number between 0 and 99, represents a percentage""",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    storage_storage_validation_level = PropertyTypeAssignment(
        code="$STORAGE.STORAGE_VALIDATION_LEVEL",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="$STORAGE.STORAGE_VALIDATION_LEVEL",
        property_label="Validation level",
        description="""Validation level""",
        mandatory=True,
        show_in_edit_views=False,
        section="General info",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class StoragePosition(ObjectType):
    defs = ObjectTypeDef(
        code="STORAGE_POSITION",
        description="""""",
        generated_code_prefix="STO",
    )

    storage_position_storage_code = PropertyTypeAssignment(
        code="$STORAGE_POSITION.STORAGE_CODE",
        data_type="VARCHAR",
        property_label="Storage Code",
        description="""Storage Code""",
        mandatory=False,
        show_in_edit_views=False,
        section="Physical Storage",
    )

    storage_position_storage_rack_row = PropertyTypeAssignment(
        code="$STORAGE_POSITION.STORAGE_RACK_ROW",
        data_type="INTEGER",
        property_label="Storage Rack Row",
        description="""Number of Rows""",
        mandatory=False,
        show_in_edit_views=False,
        section="Physical Storage",
    )

    storage_position_storage_rack_column = PropertyTypeAssignment(
        code="$STORAGE_POSITION.STORAGE_RACK_COLUMN",
        data_type="INTEGER",
        property_label="Storage Rack Column",
        description="""Number of Columns""",
        mandatory=False,
        show_in_edit_views=False,
        section="Physical Storage",
    )

    storage_position_storage_box_name = PropertyTypeAssignment(
        code="$STORAGE_POSITION.STORAGE_BOX_NAME",
        data_type="VARCHAR",
        property_label="Storage Box Name",
        description="""Box Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="Physical Storage",
    )

    storage_position_storage_box_size = PropertyTypeAssignment(
        code="$STORAGE_POSITION.STORAGE_BOX_SIZE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="$STORAGE_POSITION.STORAGE_BOX_SIZE",
        property_label="Storage Box Size",
        description="""Box Size""",
        mandatory=False,
        show_in_edit_views=False,
        section="Physical Storage",
    )

    storage_position_storage_box_position = PropertyTypeAssignment(
        code="$STORAGE_POSITION.STORAGE_BOX_POSITION",
        data_type="VARCHAR",
        property_label="Storage Box Position",
        description="""Box Position""",
        mandatory=False,
        show_in_edit_views=False,
        section="Physical Storage",
    )

    storage_position_storage_user = PropertyTypeAssignment(
        code="$STORAGE_POSITION.STORAGE_USER",
        data_type="VARCHAR",
        property_label="Storage User Id",
        description="""Storage User Id""",
        mandatory=False,
        show_in_edit_views=False,
        section="Physical Storage",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class Supplier(ObjectType):
    defs = ObjectTypeDef(
        code="SUPPLIER",
        description="""""",
        generated_code_prefix="SUP",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    supplier_company_address_line_1 = PropertyTypeAssignment(
        code="$SUPPLIER.COMPANY_ADDRESS_LINE_1",
        data_type="VARCHAR",
        property_label="Company address",
        description="""Company address""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    supplier_company_address_line_2 = PropertyTypeAssignment(
        code="$SUPPLIER.COMPANY_ADDRESS_LINE_2",
        data_type="VARCHAR",
        property_label="Company address, line 2",
        description="""Company address, line 2""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    supplier_company_fax = PropertyTypeAssignment(
        code="$SUPPLIER.COMPANY_FAX",
        data_type="VARCHAR",
        property_label="Company fax",
        description="""Company fax""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    supplier_company_phone = PropertyTypeAssignment(
        code="$SUPPLIER.COMPANY_PHONE",
        data_type="VARCHAR",
        property_label="Company phone",
        description="""Company phone""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    supplier_company_email = PropertyTypeAssignment(
        code="$SUPPLIER.COMPANY_EMAIL",
        data_type="VARCHAR",
        property_label="Company email",
        description="""Company email""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    supplier_company_language = PropertyTypeAssignment(
        code="$SUPPLIER.COMPANY_LANGUAGE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="$SUPPLIER.LANGUAGE",
        property_label="Company language",
        description="""Company language""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    supplier_customer_number = PropertyTypeAssignment(
        code="$SUPPLIER.CUSTOMER_NUMBER",
        data_type="VARCHAR",
        property_label="Customer number",
        description="""Customer number""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    supplier_company_contact_name = PropertyTypeAssignment(
        code="SUPPLIER.COMPANY_CONTACT_NAME",
        data_type="VARCHAR",
        property_label="Company contact name",
        description="""Company contact name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    supplier_company_contact_email = PropertyTypeAssignment(
        code="SUPPLIER.COMPANY_CONTACT_EMAIL",
        data_type="VARCHAR",
        property_label="Company contact email",
        description="""Company contact email""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    supplier_preferred_order_method = PropertyTypeAssignment(
        code="SUPPLIER.PREFERRED_ORDER_METHOD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="$SUPPLIER.PREFERRED_ORDER_METHOD",
        property_label="Preferred order method",
        description="""Preferred order method""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    supplier_url = PropertyTypeAssignment(
        code="SUPPLIER.URL",
        data_type="HYPERLINK",
        property_label="URL",
        description="""URL""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    supplier_additional_information = PropertyTypeAssignment(
        code="SUPPLIER.ADDITIONAL_INFORMATION",
        data_type="VARCHAR",
        property_label="Additional Information",
        description="""Additional Information""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class Product(ObjectType):
    defs = ObjectTypeDef(
        code="PRODUCT",
        description="""""",
        generated_code_prefix="PRO",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    product_product_secondary_names = PropertyTypeAssignment(
        code="PRODUCT.PRODUCT_SECONDARY_NAMES",
        data_type="VARCHAR",
        property_label="Product Secondary Names",
        description="""Product Secondary Names""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    product_description = PropertyTypeAssignment(
        code="PRODUCT.DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Description""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    product_company = PropertyTypeAssignment(
        code="PRODUCT.COMPANY",
        data_type="VARCHAR",
        property_label="Company",
        description="""Company""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    product_catalog_num = PropertyTypeAssignment(
        code="$PRODUCT.CATALOG_NUM",
        data_type="VARCHAR",
        property_label="Catalog Number",
        description="""Catalog Number""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    product_category = PropertyTypeAssignment(
        code="PRODUCT.CATEGORY",
        data_type="VARCHAR",
        property_label="Category",
        description="""Category""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    product_hazard_statement = PropertyTypeAssignment(
        code="PRODUCT.HAZARD_STATEMENT",
        data_type="VARCHAR",
        property_label="Hazard Statement",
        description="""Hazard Statement""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    product_price_per_unit = PropertyTypeAssignment(
        code="$PRODUCT.PRICE_PER_UNIT",
        data_type="REAL",
        property_label="Estimated Price",
        description="""Estimated Price""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    product_currency = PropertyTypeAssignment(
        code="$PRODUCT.CURRENCY",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="$PRODUCT.CURRENCY",
        property_label="Currency",
        description="""Currency""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    product_size_of_item = PropertyTypeAssignment(
        code="PRODUCT.SIZE_OF_ITEM",
        data_type="VARCHAR",
        property_label="Size of Item",
        description="""Size of Item""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class Request(ObjectType):
    defs = ObjectTypeDef(
        code="REQUEST",
        description="""""",
        generated_code_prefix="REQ",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    ordering_order_status = PropertyTypeAssignment(
        code="$ORDERING.ORDER_STATUS",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="$ORDER.ORDER_STATUS",
        property_label="Order Status",
        description="""Order Status""",
        mandatory=True,
        show_in_edit_views=False,
        section="General",
    )

    request_project = PropertyTypeAssignment(
        code="REQUEST.PROJECT",
        data_type="VARCHAR",
        property_label="Project",
        description="""Project""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    request_department = PropertyTypeAssignment(
        code="REQUEST.DEPARTMENT",
        data_type="VARCHAR",
        property_label="Department",
        description="""Department""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    request_buyer = PropertyTypeAssignment(
        code="REQUEST.BUYER",
        data_type="VARCHAR",
        property_label="Buyer",
        description="""Buyer""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class Order(ObjectType):
    defs = ObjectTypeDef(
        code="ORDER",
        description="""""",
        generated_code_prefix="ORD",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    order_ship_to = PropertyTypeAssignment(
        code="$ORDER.SHIP_TO",
        data_type="VARCHAR",
        property_label="Ship To",
        description="""Ship To""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    order_bill_to = PropertyTypeAssignment(
        code="$ORDER.BILL_TO",
        data_type="VARCHAR",
        property_label="Bill To",
        description="""Bill To""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    order_ship_address = PropertyTypeAssignment(
        code="$ORDER.SHIP_ADDRESS",
        data_type="VARCHAR",
        property_label="Ship Address",
        description="""Ship Address""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    order_contact_phone = PropertyTypeAssignment(
        code="$ORDER.CONTACT_PHONE",
        data_type="VARCHAR",
        property_label="Phone",
        description="""Phone""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    order_contact_fax = PropertyTypeAssignment(
        code="$ORDER.CONTACT_FAX",
        data_type="VARCHAR",
        property_label="Fax",
        description="""Fax""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    ordering_order_status = PropertyTypeAssignment(
        code="$ORDERING.ORDER_STATUS",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="$ORDER.ORDER_STATUS",
        property_label="Order Status",
        description="""Order Status""",
        mandatory=True,
        show_in_edit_views=False,
        section="General",
    )

    order_price_paid = PropertyTypeAssignment(
        code="ORDER.PRICE_PAID",
        data_type="REAL",
        property_label="Price Paid",
        description="""Price Paid""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    order_additional_information = PropertyTypeAssignment(
        code="$ORDER.ADDITIONAL_INFORMATION",
        data_type="VARCHAR",
        property_label="Additional Information",
        description="""Additional Information""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    order_order_state = PropertyTypeAssignment(
        code="$ORDER.ORDER_STATE",
        data_type="VARCHAR",
        property_label="Order State",
        description="""Order State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class Publication(ObjectType):
    defs = ObjectTypeDef(
        code="PUBLICATION",
        description="""""",
        generated_code_prefix="PUB",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General",
    )

    publication_organization = PropertyTypeAssignment(
        code="$PUBLICATION.ORGANIZATION",
        data_type="VARCHAR",
        property_label="Organization",
        description="""Organization""",
        mandatory=True,
        show_in_edit_views=False,
        section="General",
    )

    publication_type = PropertyTypeAssignment(
        code="$PUBLICATION.TYPE",
        data_type="VARCHAR",
        property_label="Type",
        description="""Type""",
        mandatory=True,
        show_in_edit_views=False,
        section="General",
    )

    publication_identifier = PropertyTypeAssignment(
        code="$PUBLICATION.IDENTIFIER",
        data_type="VARCHAR",
        property_label="Identifier",
        description="""Identifier""",
        mandatory=True,
        show_in_edit_views=False,
        section="General",
    )

    publication_url = PropertyTypeAssignment(
        code="$PUBLICATION.URL",
        data_type="HYPERLINK",
        property_label="URL",
        description="""URL""",
        mandatory=True,
        show_in_edit_views=False,
        section="General",
    )

    publication_description = PropertyTypeAssignment(
        code="$PUBLICATION.DESCRIPTION",
        data_type="VARCHAR",
        property_label="Description",
        description="""Description""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    publication_openbis_related_identifiers = PropertyTypeAssignment(
        code="$PUBLICATION.OPENBIS_RELATED_IDENTIFIERS",
        data_type="VARCHAR",
        property_label="openBIS Related Identifiers",
        description="""openBIS Related Identifiers""",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class Calibration(ObjectType):
    defs = ObjectTypeDef(
        code="CALIBRATION",
        description="""Calibration//Kalibrierung""",
        generated_code_prefix="CAL",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    instrument = PropertyTypeAssignment(
        code="INSTRUMENT",
        data_type="OBJECT",
        object_code="(ALL)",
        property_label="Testing Machine or Measurement Device",
        description="""Testing machine or measurement device//Prüfmaschine oder Messgerät""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    calibration_date = PropertyTypeAssignment(
        code="CALIBRATION_DATE",
        data_type="DATE",
        property_label="Calibration date",
        description="""Date of calibration//Datum der Kalibrierung""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    calibration_provider = PropertyTypeAssignment(
        code="CALIBRATION_PROVIDER",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CALIBRATION_PROVIDER",
        property_label="Calibration provider",
        description="""Calibration provider//Kalibrierdienstleister""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    calibration_certificate_number = PropertyTypeAssignment(
        code="CALIBRATION_CERTIFICATE_NUMBER",
        data_type="VARCHAR",
        property_label="Calibration Certificate Number",
        description="""Calibration Certificate Number//Kalibrierschein-Nummer""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    accreditated_calibration_lab = PropertyTypeAssignment(
        code="ACCREDITATED_CALIBRATION_LAB",
        data_type="BOOLEAN",
        property_label="Accredited Calibration Laboratory",
        description="""Accredited Calibration Laboratory//Akkreditiertes Kalibrierlabor""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    calibration_lab_accreditation_number = PropertyTypeAssignment(
        code="CALIBRATION_LAB_ACCREDITATION_NUMBER",
        data_type="VARCHAR",
        property_label="Calibration Laboratory Accreditation Number",
        description="""Calibration Laboratory Accreditation Number//Akkreditierungszeichen des Kalibrierlabors""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class AuxiliaryMaterial(ObjectType):
    defs = ObjectTypeDef(
        code="AUXILIARY_MATERIAL",
        description="""Auxiliary Material//Hilfsstoff""",
        generated_code_prefix="AUX_MAT",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative Name",
        description="""e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    manufacturer = PropertyTypeAssignment(
        code="MANUFACTURER",
        data_type="VARCHAR",
        property_label="Manufacturer",
        description="""Manufacturer//Hersteller""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    supplier = PropertyTypeAssignment(
        code="SUPPLIER",
        data_type="VARCHAR",
        property_label="Supplier",
        description="""Supplier//Lieferant""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    auxiliary_material_type = PropertyTypeAssignment(
        code="AUXILIARY_MATERIAL_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="AUXILIARY_MATERIAL_TYPE",
        property_label="Auxiliary Material Type",
        description="""Auxiliary Material Type//Hilfsstofftyp""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class Instrument(ObjectType):
    defs = ObjectTypeDef(
        code="INSTRUMENT",
        description="""Measuring Instrument//Messgerät""",
        generated_code_prefix="INS",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative Name",
        description="""e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    device_model_name = PropertyTypeAssignment(
        code="DEVICE_MODEL_NAME",
        data_type="VARCHAR",
        property_label="Model Name",
        description="""Manufacturer model name//Modellname bzw. Gerätebezeichnung seitens des Herstellers""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    manufacturer = PropertyTypeAssignment(
        code="MANUFACTURER",
        data_type="VARCHAR",
        property_label="Manufacturer",
        description="""Manufacturer//Hersteller""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    supplier = PropertyTypeAssignment(
        code="SUPPLIER",
        data_type="VARCHAR",
        property_label="Supplier",
        description="""Supplier//Lieferant""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    serial_number = PropertyTypeAssignment(
        code="SERIAL_NUMBER",
        data_type="VARCHAR",
        property_label="Serial Number",
        description="""Serial Number//Seriennummer""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    dfg_device_code = PropertyTypeAssignment(
        code="DFG_DEVICE_CODE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DFG_DEVICE_CODE",
        property_label="DFG Device Code",
        description="""DFG Device Code//DFG Gerätegruppenschlüssel (GGS)""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    inventory_no = PropertyTypeAssignment(
        code="INVENTORY_NO",
        data_type="INTEGER",
        property_label="Inventory Number",
        description="""PARFIS inventory number (8-digit)//PARFIS Inventarnummer (8-stellig)""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    inventory_no_add = PropertyTypeAssignment(
        code="INVENTORY_NO_ADD",
        data_type="INTEGER",
        property_label="Inventory Number Addition",
        description="""PARFIS inventory number (8-digit)//PARFIS Inventarnummer (8-stellig)""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_oe = PropertyTypeAssignment(
        code="BAM_OE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_OE",
        property_label="BAM Organizational Entity",
        description="""BAM Organizational Entity//BAM Organisationseinheit (OE)""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    responsible_person = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Responsible person",
        description="""Responsible person//Verantwortliche Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    co_responsible_person = PropertyTypeAssignment(
        code="CO_RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Co-responsible person",
        description="""Co-responsible person//Weitere verantwortliche Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_room = PropertyTypeAssignment(
        code="BAM_ROOM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_ROOM",
        property_label="BAM Room",
        description="""BAM Room//BAM Raum""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_floor = PropertyTypeAssignment(
        code="BAM_FLOOR",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_FLOOR",
        property_label="BAM Floor",
        description="""BAM Floor//BAM Etage""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_location = PropertyTypeAssignment(
        code="BAM_LOCATION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_LOCATION",
        property_label="BAM Location",
        description="""BAM Location//BAM Liegenschaft""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_house = PropertyTypeAssignment(
        code="BAM_HOUSE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_HOUSE",
        property_label="BAM House",
        description="""BAM House//BAM Haus""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_location_complete = PropertyTypeAssignment(
        code="BAM_LOCATION_COMPLETE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_LOCATION_COMPLETE",
        property_label="Complete BAM Location",
        description="""Complete BAM location (up to room level)//Komplette BAM-Ortsangabe (bis Raumlevel)""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    instrument_status = PropertyTypeAssignment(
        code="INSTRUMENT_STATUS",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="INSTRUMENT_STATUS",
        property_label="Instrument Status",
        description="""Instrument status//Instrumentenstatus""",
        mandatory=False,
        show_in_edit_views=False,
        section="Status",
    )

    last_calibration = PropertyTypeAssignment(
        code="LAST_CALIBRATION",
        data_type="DATE",
        property_label="Last Calibration",
        description="""Last Calibration//Letzte Kalibrierung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Status",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class TestingMachine(ObjectType):
    defs = ObjectTypeDef(
        code="TESTING_MACHINE",
        description="""Machine for performing mechanical tests on specimens or components//Maschine zur Durchführung von mechanischen Prüfungen an Probekörpern oder Bauteilen""",
        generated_code_prefix="INS.TMACH",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative Name",
        description="""e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    manufacturer = PropertyTypeAssignment(
        code="MANUFACTURER",
        data_type="VARCHAR",
        property_label="Manufacturer",
        description="""Manufacturer//Hersteller""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    supplier = PropertyTypeAssignment(
        code="SUPPLIER",
        data_type="VARCHAR",
        property_label="Supplier",
        description="""Supplier//Lieferant""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    serial_number = PropertyTypeAssignment(
        code="SERIAL_NUMBER",
        data_type="VARCHAR",
        property_label="Serial Number",
        description="""Serial Number//Seriennummer""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    dfg_device_code = PropertyTypeAssignment(
        code="DFG_DEVICE_CODE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DFG_DEVICE_CODE",
        property_label="DFG Device Code",
        description="""DFG Device Code//DFG Gerätegruppenschlüssel (GGS)""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    inventory_no = PropertyTypeAssignment(
        code="INVENTORY_NO",
        data_type="INTEGER",
        property_label="Inventory Number",
        description="""PARFIS inventory number (8-digit)//PARFIS Inventarnummer (8-stellig)""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    inventory_no_add = PropertyTypeAssignment(
        code="INVENTORY_NO_ADD",
        data_type="INTEGER",
        property_label="Inventory Number Addition",
        description="""PARFIS inventory number (8-digit)//PARFIS Inventarnummer (8-stellig)""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_oe = PropertyTypeAssignment(
        code="BAM_OE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_OE",
        property_label="BAM Organizational Entity",
        description="""BAM Organizational Entity//BAM Organisationseinheit (OE)""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    responsible_person = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Responsible person",
        description="""Responsible person//Verantwortliche Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    co_responsible_person = PropertyTypeAssignment(
        code="CO_RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Co-responsible person",
        description="""Co-responsible person//Weitere verantwortliche Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_room = PropertyTypeAssignment(
        code="BAM_ROOM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_ROOM",
        property_label="BAM Room",
        description="""BAM Room//BAM Raum""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_floor = PropertyTypeAssignment(
        code="BAM_FLOOR",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_FLOOR",
        property_label="BAM Floor",
        description="""BAM Floor//BAM Etage""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_house = PropertyTypeAssignment(
        code="BAM_HOUSE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_HOUSE",
        property_label="BAM House",
        description="""BAM House//BAM Haus""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_location = PropertyTypeAssignment(
        code="BAM_LOCATION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_LOCATION",
        property_label="BAM Location",
        description="""BAM Location//BAM Liegenschaft""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_location_complete = PropertyTypeAssignment(
        code="BAM_LOCATION_COMPLETE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_LOCATION_COMPLETE",
        property_label="Complete BAM Location",
        description="""Complete BAM location (up to room level)//Komplette BAM-Ortsangabe (bis Raumlevel)""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    testing_machine_drive_type = PropertyTypeAssignment(
        code="TESTING_MACHINE_DRIVE_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TESTING_MACHINE_DRIVE_TYPE",
        property_label="Drive Type",
        description="""Drive Type//Antriebsart""",
        mandatory=True,
        show_in_edit_views=False,
        section="Machine Details",
    )

    testing_machine_load_type = PropertyTypeAssignment(
        code="TESTING_MACHINE_LOAD_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TESTING_MACHINE_LOAD_TYPE",
        property_label="Load Type",
        description="""Load type//Belastungsart""",
        mandatory=True,
        show_in_edit_views=False,
        section="Machine Details",
    )

    max_load_static_primary = PropertyTypeAssignment(
        code="MAX_LOAD_STATIC_PRIMARY",
        data_type="REAL",
        property_label="Maximum Static Load (Primary) [kN/kNm]",
        description="""Maximum static load of primary load type//Maximale statische Last der primären Belastungsart""",
        mandatory=True,
        show_in_edit_views=False,
        section="Machine Details",
    )

    max_load_dynamic_primary = PropertyTypeAssignment(
        code="MAX_LOAD_DYNAMIC_PRIMARY",
        data_type="REAL",
        property_label="Maximum Dynamic Load (Primary) [kN/kNm]",
        description="""Maximum dynamic load of primary load type//Maximale dynamische Last der primären Belastungsart""",
        mandatory=True,
        show_in_edit_views=False,
        section="Machine Details",
    )

    max_load_static_secondary = PropertyTypeAssignment(
        code="MAX_LOAD_STATIC_SECONDARY",
        data_type="REAL",
        property_label="Maximum Static Load (Secondary) [kN/kNm]",
        description="""Maximum static load of secondary load type (in case of combined load-type)//Maximale statische Last der sekundären Belastungsart (falls kombinierte Antriebsart)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Machine Details",
    )

    max_load_dynamic_secondary = PropertyTypeAssignment(
        code="MAX_LOAD_DYNAMIC_SECONDARY",
        data_type="REAL",
        property_label="Maximum Dynamic Load (Secondary) [kN/kNm]",
        description="""Maximum dynamic load of secondary load type//Maximale dynamische Last der sekundären Belastungsart""",
        mandatory=False,
        show_in_edit_views=False,
        section="Machine Details",
    )

    max_stroke = PropertyTypeAssignment(
        code="MAX_STROKE",
        data_type="REAL",
        property_label="Maximum Stroke [mm]",
        description="""Maximum Stroke//Maximaler Maschinenweg""",
        mandatory=False,
        show_in_edit_views=False,
        section="Machine Details",
    )

    instrument_status = PropertyTypeAssignment(
        code="INSTRUMENT_STATUS",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="INSTRUMENT_STATUS",
        property_label="Instrument Status",
        description="""Instrument status//Instrumentenstatus""",
        mandatory=False,
        show_in_edit_views=False,
        section="Status",
    )

    last_calibration = PropertyTypeAssignment(
        code="LAST_CALIBRATION",
        data_type="DATE",
        property_label="Last Calibration",
        description="""Last Calibration//Letzte Kalibrierung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Status",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class Document(ObjectType):
    defs = ObjectTypeDef(
        code="DOCUMENT",
        description="""Document//Dokument""",
        generated_code_prefix="DOC",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    document_type = PropertyTypeAssignment(
        code="DOCUMENT_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DOCUMENT_TYPE",
        property_label="Document type",
        description="""Document Type//Dokumenten Typ""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative Name",
        description="""e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    author = PropertyTypeAssignment(
        code="AUTHOR",
        data_type="VARCHAR",
        property_label="Author(s)",
        description="""Author(s)//Autor(en)""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    version = PropertyTypeAssignment(
        code="VERSION",
        data_type="VARCHAR",
        property_label="Version",
        description="""Version""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class GasBottle(ObjectType):
    defs = ObjectTypeDef(
        code="GAS_BOTTLE",
        description="""Gas bottle containing a specific gas mixture//Gasflasche gefüllt mit spezifischem Gasgemisch""",
        generated_code_prefix="GAS_BTL",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    supplier = PropertyTypeAssignment(
        code="SUPPLIER",
        data_type="VARCHAR",
        property_label="Supplier",
        description="""Supplier//Lieferant""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    gas_volume = PropertyTypeAssignment(
        code="GAS_VOLUME",
        data_type="REAL",
        property_label="Gas Volume [liter]",
        description="""Gas volume in liter//Gasvolumen in liter""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    gas_pressure_bar = PropertyTypeAssignment(
        code="GAS_PRESSURE_BAR",
        data_type="REAL",
        property_label="Gas pressure [bar]",
        description="""Gas pressure (in bar)// Gasdruck der Flasche (in bar)""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    volume_percent_argon = PropertyTypeAssignment(
        code="VOLUME_PERCENT_ARGON",
        data_type="REAL",
        property_label="Ar",
        description="""Volume percent of Argon//Volumenanteil von Argon""",
        mandatory=False,
        show_in_edit_views=False,
        section="Gas Mixture",
    )

    volume_percent_carbon_dioxide = PropertyTypeAssignment(
        code="VOLUME_PERCENT_CARBON_DIOXIDE",
        data_type="REAL",
        property_label="CO2",
        description="""Volume percent of CO2//Volumenanteil von CO2""",
        mandatory=False,
        show_in_edit_views=False,
        section="Gas Mixture",
    )

    volume_percent_oxygen = PropertyTypeAssignment(
        code="VOLUME_PERCENT_OXYGEN",
        data_type="REAL",
        property_label="O2",
        description="""Volume percent of Oxygen//Volumenanteil von Sauerstoff""",
        mandatory=False,
        show_in_edit_views=False,
        section="Gas Mixture",
    )

    volume_percent_helium = PropertyTypeAssignment(
        code="VOLUME_PERCENT_HELIUM",
        data_type="REAL",
        property_label="He",
        description="""Volume percent of Helium//Volumenanteil von Helium""",
        mandatory=False,
        show_in_edit_views=False,
        section="Gas Mixture",
    )

    volume_percent_hydrogen = PropertyTypeAssignment(
        code="VOLUME_PERCENT_HYDROGEN",
        data_type="REAL",
        property_label="H2",
        description="""Volume percent of hydrogen//Volumenanteil von Wasserstoff""",
        mandatory=False,
        show_in_edit_views=False,
        section="Gas Mixture",
    )

    volume_percent_nitrogen = PropertyTypeAssignment(
        code="VOLUME_PERCENT_NITROGEN",
        data_type="REAL",
        property_label="N2",
        description="""Volume percent of Nitrogen//Volumenanteil von Stickstoff""",
        mandatory=False,
        show_in_edit_views=False,
        section="Gas Mixture",
    )

    inventory_no = PropertyTypeAssignment(
        code="INVENTORY_NO",
        data_type="INTEGER",
        property_label="Inventory Number",
        description="""PARFIS inventory number (8-digit)//PARFIS Inventarnummer (8-stellig)""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    inventory_no_add = PropertyTypeAssignment(
        code="INVENTORY_NO_ADD",
        data_type="INTEGER",
        property_label="Inventory Number Addition",
        description="""PARFIS inventory number (8-digit)//PARFIS Inventarnummer (8-stellig)""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_oe = PropertyTypeAssignment(
        code="BAM_OE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_OE",
        property_label="BAM Organizational Entity",
        description="""BAM Organizational Entity//BAM Organisationseinheit (OE)""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    responsible_person = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Responsible person",
        description="""Responsible person//Verantwortliche Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    co_responsible_person = PropertyTypeAssignment(
        code="CO_RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Co-responsible person",
        description="""Co-responsible person//Weitere verantwortliche Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_room = PropertyTypeAssignment(
        code="BAM_ROOM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_ROOM",
        property_label="BAM Room",
        description="""BAM Room//BAM Raum""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_floor = PropertyTypeAssignment(
        code="BAM_FLOOR",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_FLOOR",
        property_label="BAM Floor",
        description="""BAM Floor//BAM Etage""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_house = PropertyTypeAssignment(
        code="BAM_HOUSE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_HOUSE",
        property_label="BAM House",
        description="""BAM House//BAM Haus""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_location = PropertyTypeAssignment(
        code="BAM_LOCATION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_LOCATION",
        property_label="BAM Location",
        description="""BAM Location//BAM Liegenschaft""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_location_complete = PropertyTypeAssignment(
        code="BAM_LOCATION_COMPLETE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_LOCATION_COMPLETE",
        property_label="Complete BAM Location",
        description="""Complete BAM location (up to room level)//Komplette BAM-Ortsangabe (bis Raumlevel)""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    last_systemcheck = PropertyTypeAssignment(
        code="LAST_SYSTEMCHECK",
        data_type="DATE",
        property_label="Last System Check",
        description="""Date of the last system check//Datum des letzten Systemchecks""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class TestObject(ObjectType):
    defs = ObjectTypeDef(
        code="TEST_OBJECT",
        description="""Test Object//Prüfobjekt""",
        generated_code_prefix="TEST_OBJ",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative Name",
        description="""e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    production_date = PropertyTypeAssignment(
        code="PRODUCTION_DATE",
        data_type="DATE",
        property_label="Production Date",
        description="""Production Date//Herstellungsdatum""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    test_obj_status = PropertyTypeAssignment(
        code="TEST_OBJ_STATUS",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TEST_OBJECT_STATUS",
        property_label="Test Object Status",
        description="""Test Object Status//Prüfkörperstatus""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    bam_oe = PropertyTypeAssignment(
        code="BAM_OE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_OE",
        property_label="BAM Organizational Entity",
        description="""BAM Organizational Entity//BAM Organisationseinheit (OE)""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    responsible_person = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Responsible person",
        description="""Responsible person//Verantwortliche Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_room = PropertyTypeAssignment(
        code="BAM_ROOM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_ROOM",
        property_label="BAM Room",
        description="""BAM Room//BAM Raum""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_floor = PropertyTypeAssignment(
        code="BAM_FLOOR",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_FLOOR",
        property_label="BAM Floor",
        description="""BAM Floor//BAM Etage""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_house = PropertyTypeAssignment(
        code="BAM_HOUSE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_HOUSE",
        property_label="BAM House",
        description="""BAM House//BAM Haus""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_location = PropertyTypeAssignment(
        code="BAM_LOCATION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_LOCATION",
        property_label="BAM Location",
        description="""BAM Location//BAM Liegenschaft""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_location_complete = PropertyTypeAssignment(
        code="BAM_LOCATION_COMPLETE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_LOCATION_COMPLETE",
        property_label="Complete BAM Location",
        description="""Complete BAM location (up to room level)//Komplette BAM-Ortsangabe (bis Raumlevel)""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    test_obj_material = PropertyTypeAssignment(
        code="TEST_OBJ_MATERIAL",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BUILDING_MATERIAL_TYPE",
        property_label="Building Material",
        description="""Building Material//Werkstoff""",
        mandatory=True,
        show_in_edit_views=False,
        section="Specific Information",
    )

    test_obj_length = PropertyTypeAssignment(
        code="TEST_OBJ_LENGTH",
        data_type="INTEGER",
        property_label="Test Object Length [mm]",
        description="""Test Object Length [mm]//Länge des Prüfkörpers [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Specific Information",
    )

    test_obj_width = PropertyTypeAssignment(
        code="TEST_OBJ_WIDTH",
        data_type="INTEGER",
        property_label="Test Object Width [mm]",
        description="""Test Object Width [mm]//Breite des Prüfkörpers [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Specific Information",
    )

    test_obj_height = PropertyTypeAssignment(
        code="TEST_OBJ_HEIGHT",
        data_type="INTEGER",
        property_label="Test Object Height [mm]",
        description="""Test Object Height [mm]//Höhe des Prüfkörpers [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Specific Information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class Project(ObjectType):
    defs = ObjectTypeDef(
        code="PROJECT",
        description="""Project//Projekt""",
        generated_code_prefix="PROJ",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    acronym = PropertyTypeAssignment(
        code="ACRONYM",
        data_type="VARCHAR",
        property_label="Acronym",
        description="""Acronym//Akronym""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    abstract = PropertyTypeAssignment(
        code="ABSTRACT",
        data_type="MULTILINE_VARCHAR",
        property_label="Abstract",
        description="""Abstract//Kurzzusammenfassung""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    homepage = PropertyTypeAssignment(
        code="HOMEPAGE",
        data_type="HYPERLINK",
        property_label="Homepage",
        description="""Homepage//Homepage""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    project_status = PropertyTypeAssignment(
        code="PROJECT_STATUS",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="PROJECT_STATUS",
        property_label="Project Status",
        description="""Project Status//Projektstatus""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    start_date = PropertyTypeAssignment(
        code="START_DATE",
        data_type="TIMESTAMP",
        property_label="Start date",
        description="""Start date//Startdatum""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    end_date = PropertyTypeAssignment(
        code="END_DATE",
        data_type="TIMESTAMP",
        property_label="End date",
        description="""End date//Enddatum""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    project_leader = PropertyTypeAssignment(
        code="PROJECT_LEADER",
        data_type="VARCHAR",
        property_label="Project Leader",
        description="""Project Leader: `Last name, first name`//Projektleitung: `Name, Vorname`""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    project_leader_bam = PropertyTypeAssignment(
        code="PROJECT_LEADER_BAM",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Project Leader",
        description="""Project Leader at BAM//Projektleitung an der BAM""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_oe = PropertyTypeAssignment(
        code="BAM_OE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_OE",
        property_label="BAM Organizational Entity",
        description="""BAM Organizational Entity//BAM Organisationseinheit (OE)""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_focus_area = PropertyTypeAssignment(
        code="BAM_FOCUS_AREA",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_FOCUS_AREA",
        property_label="BAM Focus Area",
        description="""BAM Focus Area//BAM Themenfeld""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_field_of_activity = PropertyTypeAssignment(
        code="BAM_FIELD_OF_ACTIVITY",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_FIELD_OF_ACTIVITY",
        property_label="BAM Field of Activity",
        description="""BAM Field of Activity//BAM Aktivitätsfeld""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_partner = PropertyTypeAssignment(
        code="BAM_PARTNER",
        data_type="VARCHAR",
        property_label="BAM Partner",
        description="""BAM Partner(s)//BAM Partner""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    parfis_project_no = PropertyTypeAssignment(
        code="PARFIS_PROJECT_NO",
        data_type="VARCHAR",
        property_label="PARFIS Project Number",
        description="""PARFIS Project Number: `VhXXXX`//PARFIS Vorhabennummer: `VhXXXX`""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    research_bam_project_id = PropertyTypeAssignment(
        code="RESEARCH_BAM_PROJECT_ID",
        data_type="VARCHAR",
        property_label="ReSEARCH BAM ID",
        description="""ReSEARCH BAM ID//ReSEARCH BAM ID""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    funding_grant_no = PropertyTypeAssignment(
        code="FUNDING_GRANT_NO",
        data_type="VARCHAR",
        property_label="Grant Number",
        description="""Grant Number//Förderkennzeichen""",
        mandatory=False,
        show_in_edit_views=False,
        section="Funding Information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class Person(ObjectType):
    defs = ObjectTypeDef(
        code="PERSON",
        description="""A natural person//Eine natürliche Person""",
        generated_code_prefix="PERS",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    family_name = PropertyTypeAssignment(
        code="FAMILY_NAME",
        data_type="VARCHAR",
        property_label="Family name",
        description="""Family name//Nachname""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    given_name = PropertyTypeAssignment(
        code="GIVEN_NAME",
        data_type="VARCHAR",
        property_label="Given name",
        description="""Given name//Nachname""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative Name",
        description="""e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    affiliation = PropertyTypeAssignment(
        code="AFFILIATION",
        data_type="VARCHAR",
        property_label="Institute or company",
        description="""Institute or company//Institut oder Unternehmen""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    email = PropertyTypeAssignment(
        code="EMAIL",
        data_type="VARCHAR",
        property_label="Email address",
        description="""Email address//E-Mail-Adresse""",
        mandatory=False,
        show_in_edit_views=False,
        section="Contact Information",
    )

    telephone = PropertyTypeAssignment(
        code="TELEPHONE",
        data_type="VARCHAR",
        property_label="Telephone number",
        description="""Telephone number//Telefonnummer""",
        mandatory=False,
        show_in_edit_views=False,
        section="Contact Information",
    )

    address = PropertyTypeAssignment(
        code="ADDRESS",
        data_type="MULTILINE_VARCHAR",
        property_label="Postal address",
        description="""Postal address//Anschrift""",
        mandatory=False,
        show_in_edit_views=False,
        section="Contact Information",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class Control(ObjectType):
    defs = ObjectTypeDef(
        code="CONTROL",
        description="""This Object allows to store a control point value for a device//Dieses Objekt erlaubt einen Kontrollpunkt Messwert für ein Gerät zu erstellen""",
        generated_code_prefix="CTRL",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    monitoring_date = PropertyTypeAssignment(
        code="MONITORING_DATE",
        data_type="DATE",
        property_label="Monitoring date",
        description="""Monitoring date//Datum der Überprüfung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Control Data",
    )

    monitoring_value = PropertyTypeAssignment(
        code="MONITORING_VALUE",
        data_type="VARCHAR",
        property_label="Monitoring value",
        description="""Monitoring value or status//Messwert oder Status""",
        mandatory=False,
        show_in_edit_views=False,
        section="Control Data",
    )

    acting_person = PropertyTypeAssignment(
        code="ACTING_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Acting Person",
        description="""Acting Person//Handelnde Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="Control Data",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class Task(ObjectType):
    defs = ObjectTypeDef(
        code="TASK",
        description="""This object allows to define a scheduled action//Mit diesem Objekt kann eine geplante Aktion definiert werden""",
        generated_code_prefix="TASK",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="Task Details",
    )

    responsible_person = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Responsible person",
        description="""Responsible person//Verantwortliche Person""",
        mandatory=True,
        show_in_edit_views=False,
        section="Automation",
    )

    co_responsible_person = PropertyTypeAssignment(
        code="CO_RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Co-responsible person",
        description="""Co-responsible person//Weitere verantwortliche Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="Automation",
    )

    last_check = PropertyTypeAssignment(
        code="LAST_CHECK",
        data_type="DATE",
        property_label="Date of last check",
        description="""Date of the last check//Datum der letzten Überprüfung""",
        mandatory=True,
        show_in_edit_views=False,
        section="Automation",
    )

    check_interval = PropertyTypeAssignment(
        code="CHECK_INTERVAL",
        data_type="INTEGER",
        property_label="Check interval [days]",
        description="""Time interval for checks in days//Überprüfungsintervall in Tagen""",
        mandatory=True,
        show_in_edit_views=False,
        section="Automation",
    )

    state_check = PropertyTypeAssignment(
        code="STATE_CHECK",
        data_type="BOOLEAN",
        property_label="Needs to be checked?",
        description="""TRUE if task needs to be done//WAHR wenn die Aufgabe getan werden muss""",
        mandatory=False,
        show_in_edit_views=False,
        section="Automation",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class SpecificPersonInfo(ObjectType):
    defs = ObjectTypeDef(
        code="SPECIFIC_PERSON_INFO",
        description="""Additional employee information//Zusätzliche Mitarbeiterinformationen""",
        generated_code_prefix="SPI",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General information",
    )

    responsible_person = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Responsible person",
        description="""Responsible person//Verantwortliche Person""",
        mandatory=True,
        show_in_edit_views=False,
        section="Employee Information",
    )

    person_alias = PropertyTypeAssignment(
        code="PERSON_ALIAS",
        data_type="VARCHAR",
        property_label="Person alias",
        description="""Name abbreviation of a person//Laborkürzel einer Person""",
        mandatory=True,
        show_in_edit_views=False,
        section="Employee Information",
    )

    person_status = PropertyTypeAssignment(
        code="PERSON_STATUS",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="PERSON_STATUS",
        property_label="Person status",
        description="""Person status//Anwesenheitsstatus einer Person""",
        mandatory=True,
        show_in_edit_views=False,
        section="Employee Information",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class Sop(ObjectType):
    defs = ObjectTypeDef(
        code="SOP",
        description="""Standard Operating Procedure (SOP)//Standardarbeitsanweisung (STAA)""",
        generated_code_prefix="SOP",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    id_eakte = PropertyTypeAssignment(
        code="ID_EAKTE",
        data_type="VARCHAR",
        property_label="ID E-Akte",
        description="""Identifier used in E-Akte//E-Akte Nummer""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    link_eakte = PropertyTypeAssignment(
        code="LINK_EAKTE",
        data_type="HYPERLINK",
        property_label="Link E-Akte",
        description="""Link to E-Akte//Link zum Dokument in der E-Akte""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_oe = PropertyTypeAssignment(
        code="BAM_OE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_OE",
        property_label="BAM Organizational Entity",
        description="""BAM Organizational Entity//BAM Organisationseinheit (OE)""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    responsible_person = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Responsible person",
        description="""Responsible person//Verantwortliche Person""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    co_responsible_person = PropertyTypeAssignment(
        code="CO_RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Co-responsible person",
        description="""Co-responsible person//Weitere verantwortliche Person""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    author = PropertyTypeAssignment(
        code="AUTHOR",
        data_type="VARCHAR",
        property_label="Author(s)",
        description="""Author(s)//Autor(en)""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    version = PropertyTypeAssignment(
        code="VERSION",
        data_type="VARCHAR",
        property_label="Version",
        description="""Version""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    last_check = PropertyTypeAssignment(
        code="LAST_CHECK",
        data_type="DATE",
        property_label="Date of last check",
        description="""Date of the last check//Datum der letzten Überprüfung""",
        mandatory=True,
        show_in_edit_views=False,
        section="Automation",
    )

    check_interval = PropertyTypeAssignment(
        code="CHECK_INTERVAL",
        data_type="INTEGER",
        property_label="Check interval [days]",
        description="""Time interval for checks in days//Überprüfungsintervall in Tagen""",
        mandatory=True,
        show_in_edit_views=False,
        section="Automation",
    )

    state_check = PropertyTypeAssignment(
        code="STATE_CHECK",
        data_type="BOOLEAN",
        property_label="Needs to be checked?",
        description="""TRUE if task needs to be done//WAHR wenn die Aufgabe getan werden muss""",
        mandatory=False,
        show_in_edit_views=False,
        section="Automation",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class Sample(ObjectType):
    defs = ObjectTypeDef(
        code="SAMPLE",
        description="""Generic sample/sample material//Generische Probe/Probenmaterial""",
        generated_code_prefix="SAM",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative Name",
        description="""e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    sample_id_number = PropertyTypeAssignment(
        code="SAMPLE_ID_NUMBER",
        data_type="INTEGER",
        property_label="Sample Number",
        description="""Sample number//Probennummer""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    manufacturer = PropertyTypeAssignment(
        code="MANUFACTURER",
        data_type="VARCHAR",
        property_label="Manufacturer",
        description="""Manufacturer//Hersteller""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    barcode_external = PropertyTypeAssignment(
        code="BARCODE_EXTERNAL",
        data_type="VARCHAR",
        property_label="External Barcode",
        description="""External barcode (if availabe)//Externer Barcode (falls vorhanden)""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    supplier = PropertyTypeAssignment(
        code="SUPPLIER",
        data_type="VARCHAR",
        property_label="Supplier",
        description="""Supplier//Lieferant""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    physical_state = PropertyTypeAssignment(
        code="PHYSICAL_STATE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="PHYSICAL_STATE",
        property_label="Physical State",
        description="""Physical state of a material // Physikalischer Zustand eines Materials""",
        mandatory=False,
        show_in_edit_views=False,
        section="Properties",
    )

    bam_oe = PropertyTypeAssignment(
        code="BAM_OE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_OE",
        property_label="BAM Organizational Entity",
        description="""BAM Organizational Entity//BAM Organisationseinheit (OE)""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    responsible_person = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Responsible person",
        description="""Responsible person//Verantwortliche Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    co_responsible_person = PropertyTypeAssignment(
        code="CO_RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Co-responsible person",
        description="""Co-responsible person//Weitere verantwortliche Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_room = PropertyTypeAssignment(
        code="BAM_ROOM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_ROOM",
        property_label="BAM Room",
        description="""BAM Room//BAM Raum""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_floor = PropertyTypeAssignment(
        code="BAM_FLOOR",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_FLOOR",
        property_label="BAM Floor",
        description="""BAM Floor//BAM Etage""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_house = PropertyTypeAssignment(
        code="BAM_HOUSE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_HOUSE",
        property_label="BAM House",
        description="""BAM House//BAM Haus""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_location = PropertyTypeAssignment(
        code="BAM_LOCATION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_LOCATION",
        property_label="BAM Location",
        description="""BAM Location//BAM Liegenschaft""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_location_complete = PropertyTypeAssignment(
        code="BAM_LOCATION_COMPLETE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_LOCATION_COMPLETE",
        property_label="Complete BAM Location",
        description="""Complete BAM location (up to room level)//Komplette BAM-Ortsangabe (bis Raumlevel)""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class Chemical(ObjectType):
    defs = ObjectTypeDef(
        code="CHEMICAL",
        description="""Chemical Substance//Chemische Substanz""",
        generated_code_prefix="CHEM",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative Name",
        description="""e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    iupac_name = PropertyTypeAssignment(
        code="IUPAC_NAME",
        data_type="VARCHAR",
        property_label="IUPAC Name",
        description="""IUPAC Name//IUPAC-Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    cas_number = PropertyTypeAssignment(
        code="CAS_NUMBER",
        data_type="VARCHAR",
        property_label="CAS Registry Number",
        description="""CAS Registry Number (corresponds to field `CAS-No.` in the Hazardous Materials Inventory (GSM) of BAM)//CAS-Nummer (entspricht Feld `CAS-Nr.` aus dem Gefahrstoffmanagement (GSM) der BAM)""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    manufacturer = PropertyTypeAssignment(
        code="MANUFACTURER",
        data_type="VARCHAR",
        property_label="Manufacturer",
        description="""Manufacturer//Hersteller""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    supplier = PropertyTypeAssignment(
        code="SUPPLIER",
        data_type="VARCHAR",
        property_label="Supplier",
        description="""Supplier//Lieferant""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    lot_number = PropertyTypeAssignment(
        code="LOT_NUMBER",
        data_type="VARCHAR",
        property_label="Lot/Batch Number",
        description="""Lot/Batch Number//Chargennummer""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    barcode_external = PropertyTypeAssignment(
        code="BARCODE_EXTERNAL",
        data_type="VARCHAR",
        property_label="External Barcode",
        description="""External barcode (if availabe)//Externer Barcode (falls vorhanden)""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    product_category = PropertyTypeAssignment(
        code="PRODUCT_CATEGORY",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CHEMICAL_PRODUCT_CATEGORY",
        property_label="Product Category",
        description="""Product Category (corresponds to field `Product Category` in the Hazardous Materials Inventory (GSM) of BAM)//Produktkategorie (entspricht Feld `Verwendungstypen/Produktkategorie` aus dem Gefahrstoffmanagement (GSM) der BAM))""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    hazardous_substance = PropertyTypeAssignment(
        code="HAZARDOUS_SUBSTANCE",
        data_type="BOOLEAN",
        property_label="Hazardous Substance",
        description="""Is the chemical a  hazardous substance according to the Hazardous Substances Ordinance (GefStoffV)?//Handelt es sich bei der Chemikalie um einen Gefahrenstoff nach der Gefahrenstoffverordnung (GefStoffV)?""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    bam_oe = PropertyTypeAssignment(
        code="BAM_OE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_OE",
        property_label="BAM Organizational Entity",
        description="""BAM Organizational Entity//BAM Organisationseinheit (OE)""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_room = PropertyTypeAssignment(
        code="BAM_ROOM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_ROOM",
        property_label="BAM Room",
        description="""BAM Room//BAM Raum""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_floor = PropertyTypeAssignment(
        code="BAM_FLOOR",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_FLOOR",
        property_label="BAM Floor",
        description="""BAM Floor//BAM Etage""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_house = PropertyTypeAssignment(
        code="BAM_HOUSE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_HOUSE",
        property_label="BAM House",
        description="""BAM House//BAM Haus""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_location = PropertyTypeAssignment(
        code="BAM_LOCATION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_LOCATION",
        property_label="BAM Location",
        description="""BAM Location//BAM Liegenschaft""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_location_complete = PropertyTypeAssignment(
        code="BAM_LOCATION_COMPLETE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_LOCATION_COMPLETE",
        property_label="Complete BAM Location",
        description="""Complete BAM location (up to room level)//Komplette BAM-Ortsangabe (bis Raumlevel)""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    responsible_person = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Responsible person",
        description="""Responsible person//Verantwortliche Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    mass_molar = PropertyTypeAssignment(
        code="MASS_MOLAR",
        data_type="REAL",
        property_label="Molar Mass",
        description="""Molar Mass [g/mol]//Molare Masse [g/mol]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Chemical Properties",
    )

    density_gram_per_cubic_cm = PropertyTypeAssignment(
        code="DENSITY_GRAM_PER_CUBIC_CM",
        data_type="REAL",
        property_label="Density",
        description="""Density [g/cm³]//Dichte [g/cm³]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Chemical Properties",
    )

    concentration = PropertyTypeAssignment(
        code="CONCENTRATION",
        data_type="REAL",
        property_label="Concentration",
        description="""Concentration [%] (corresponds to field `Concentration %` in the Hazardous Materials Inventory (GSM) of BAM)//Konzentration [%] (entspricht Feld `Konzentration %` aus dem Gefahrstoffmanagement (GSM) der BAM)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Chemical Properties",
    )

    date_bottling = PropertyTypeAssignment(
        code="DATE_BOTTLING",
        data_type="DATE",
        property_label="Bottling Date",
        description="""Date of Bottling//Abfülldatum""",
        mandatory=False,
        show_in_edit_views=False,
        section="Handling",
    )

    date_opening = PropertyTypeAssignment(
        code="DATE_OPENING",
        data_type="DATE",
        property_label="Opening Date",
        description="""Opening Data//Öffnungsdatum""",
        mandatory=False,
        show_in_edit_views=False,
        section="Handling",
    )

    date_expiration = PropertyTypeAssignment(
        code="DATE_EXPIRATION",
        data_type="DATE",
        property_label="Expiration Date",
        description="""Expiration Date//Verfallsdatum""",
        mandatory=False,
        show_in_edit_views=False,
        section="Handling",
    )

    substance_empty = PropertyTypeAssignment(
        code="SUBSTANCE_EMPTY",
        data_type="BOOLEAN",
        property_label="Empty",
        description="""Is the substance used up?//Ist die Substanz aufgebraucht?""",
        mandatory=False,
        show_in_edit_views=False,
        section="Handling",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class Organism(ObjectType):
    defs = ObjectTypeDef(
        code="ORGANISM",
        description="""Organism with Risk Group Assignment//Organismus mit Risikogruppe Zuweisung""",
        generated_code_prefix="ORGA",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative Name",
        description="""e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    supplier = PropertyTypeAssignment(
        code="SUPPLIER",
        data_type="VARCHAR",
        property_label="Supplier",
        description="""Supplier//Lieferant""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    organism_risk_group = PropertyTypeAssignment(
        code="ORGANISM_RISK_GROUP",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="ORGANISM_RISK_GROUP",
        property_label="Organism Risk Group Assignement",
        description="""Organism Risk Group Assignment//Risikogruppenzuordnung des Organismus""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    organism_group = PropertyTypeAssignment(
        code="ORGANISM_GROUP",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="ORGANISM_GROUP",
        property_label="Organism Group Assignment",
        description="""Organism group assignment according to the central comission of biological safety or category in the BAM-Biomicrosearch//Organismen Gruppenzuordnung anhand ZKBS bzw. die Kategorie in der BAM-Microsearch Datenbank database//Organismen Gruppenzuordnung anhand ZKBS bzw. die Kategorie in der BAM-Microsearch Datenbank""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    organism_family = PropertyTypeAssignment(
        code="ORGANISM_FAMILY",
        data_type="VARCHAR",
        property_label="Organism Family Assignment",
        description="""Organism family assignment according Central Commision for Biological Safety//Organismen Familienzuordnung anhand ZKBS""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    organism_footnote = PropertyTypeAssignment(
        code="ORGANISM_FOOTNOTE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="ORGANISM_FOOTNOTE_ZKBS",
        property_label="ZKBS Footnote",
        description="""Central commission for biological safety Footnotes//Zentral Komission für Biologische Sicherheit ZKBS Fußnote""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    organism_zkbs_statement = PropertyTypeAssignment(
        code="ORGANISM_ZKBS_STATEMENT",
        data_type="HYPERLINK",
        property_label="Central Commission for Biological Safety  Statement",
        description="""Central Commission for Biological Safety  Statement//Zentral Komission für Biologische Sicherheit ZKBS-Stellungnahme""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class BamGentechFacility(ObjectType):
    defs = ObjectTypeDef(
        code="BAM_GENTECH_FACILITY",
        description="""BAM genetic engineering facility//BAM gentechnische Anlage""",
        generated_code_prefix="BAM.GENT_FAC",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative Name",
        description="""e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    gentech_safety_level = PropertyTypeAssignment(
        code="GENTECH_SAFETY_LEVEL",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="GENTECH_SAFETY_LEVEL",
        property_label="Genetic Engineering Facility Safety Level",
        description="""BAM genetic engineering facility//BAM gentechnische Anlage""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    gentech_project_lead = PropertyTypeAssignment(
        code="GENTECH_PROJECT_LEAD",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Genetic Engineering Facility Project Leader",
        description="""BAM Project Leader according to GenTSV//BAM Project Leiter nach GenTSV""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    gentech_biosafety_officer = PropertyTypeAssignment(
        code="GENTECH_BIOSAFETY_OFFICER",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Genetic Engineering Facility Biosafety Officer",
        description="""BAM Biosafety Officer according to GenTSV//BAM Beauftragte für biologische Sicherheit nach GenTSV""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_oe = PropertyTypeAssignment(
        code="BAM_OE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_OE",
        property_label="BAM Organizational Entity",
        description="""BAM Organizational Entity//BAM Organisationseinheit (OE)""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_room = PropertyTypeAssignment(
        code="BAM_ROOM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_ROOM",
        property_label="BAM Room",
        description="""BAM Room//BAM Raum""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_floor = PropertyTypeAssignment(
        code="BAM_FLOOR",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_FLOOR",
        property_label="BAM Floor",
        description="""BAM Floor//BAM Etage""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_house = PropertyTypeAssignment(
        code="BAM_HOUSE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_HOUSE",
        property_label="BAM House",
        description="""BAM House//BAM Haus""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_location = PropertyTypeAssignment(
        code="BAM_LOCATION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_LOCATION",
        property_label="BAM Location",
        description="""BAM Location//BAM Liegenschaft""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_location_complete = PropertyTypeAssignment(
        code="BAM_LOCATION_COMPLETE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_LOCATION_COMPLETE",
        property_label="Complete BAM Location",
        description="""Complete BAM location (up to room level)//Komplette BAM-Ortsangabe (bis Raumlevel)""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class GlassWare(ObjectType):
    defs = ObjectTypeDef(
        code="GLASS_WARE",
        description="""Any type of glass ware //Jede Art von Glaswaren""",
        generated_code_prefix="GLAS_WAR",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    manufacturer = PropertyTypeAssignment(
        code="MANUFACTURER",
        data_type="VARCHAR",
        property_label="Manufacturer",
        description="""Manufacturer//Hersteller""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    supplier = PropertyTypeAssignment(
        code="SUPPLIER",
        data_type="VARCHAR",
        property_label="Supplier",
        description="""Supplier//Lieferant""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    lot_number = PropertyTypeAssignment(
        code="LOT_NUMBER",
        data_type="VARCHAR",
        property_label="Lot/Batch Number",
        description="""Lot/Batch Number//Chargennummer""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    barcode_external = PropertyTypeAssignment(
        code="BARCODE_EXTERNAL",
        data_type="VARCHAR",
        property_label="External Barcode",
        description="""External barcode (if availabe)//Externer Barcode (falls vorhanden)""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    volume_min_in_ml = PropertyTypeAssignment(
        code="VOLUME_MIN_IN_ML",
        data_type="REAL",
        property_label="Minimum volume",
        description="""Minimum volume in mililiter//Mindestvolumen in Milliliter""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    volume_max_in_ml = PropertyTypeAssignment(
        code="VOLUME_MAX_IN_ML",
        data_type="REAL",
        property_label="Maximum volume",
        description="""Maximum volume in mililiter/Maximales Volumen in Milliliter""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    bam_oe = PropertyTypeAssignment(
        code="BAM_OE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_OE",
        property_label="BAM Organizational Entity",
        description="""BAM Organizational Entity//BAM Organisationseinheit (OE)""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_room = PropertyTypeAssignment(
        code="BAM_ROOM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_ROOM",
        property_label="BAM Room",
        description="""BAM Room//BAM Raum""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_floor = PropertyTypeAssignment(
        code="BAM_FLOOR",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_FLOOR",
        property_label="BAM Floor",
        description="""BAM Floor//BAM Etage""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_house = PropertyTypeAssignment(
        code="BAM_HOUSE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_HOUSE",
        property_label="BAM House",
        description="""BAM House//BAM Haus""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_location = PropertyTypeAssignment(
        code="BAM_LOCATION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_LOCATION",
        property_label="BAM Location",
        description="""BAM Location//BAM Liegenschaft""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_location_complete = PropertyTypeAssignment(
        code="BAM_LOCATION_COMPLETE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_LOCATION_COMPLETE",
        property_label="Complete BAM Location",
        description="""Complete BAM location (up to room level)//Komplette BAM-Ortsangabe (bis Raumlevel)""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class StorageConnector(ObjectType):
    defs = ObjectTypeDef(
        code="STORAGE_CONNECTOR",
        description="""Connects a storage position to another object//Verbindet eine Storage position mit einem anderen Objekt""",
        generated_code_prefix="STO_CON",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class Action(ObjectType):
    defs = ObjectTypeDef(
        code="ACTION",
        description="""This Object allows to store information on an action by a user.//Dieses Objekt erlaubt eine Nutzer-Aktion zu beschreiben.""",
        generated_code_prefix="ACT",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="Device ID",
    )

    action_date = PropertyTypeAssignment(
        code="ACTION_DATE",
        data_type="DATE",
        property_label="Monitoring Date",
        description="""Action Date//Datum der Handlung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Action Data",
    )

    acting_person = PropertyTypeAssignment(
        code="ACTING_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Acting Person",
        description="""Acting Person//Handelnde Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="Action Data",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class RawMaterialCode(ObjectType):
    defs = ObjectTypeDef(
        code="RAW_MATERIAL_CODE",
        description="""Material Number and name according to VDEh//Werkstoffnummern und Namen nach VDEh""",
        generated_code_prefix="RAW_MAT_CODE",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative Name",
        description="""e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    material_number = PropertyTypeAssignment(
        code="MATERIAL_NUMBER",
        data_type="VARCHAR",
        property_label="Material number",
        description="""Material number//Werkstoffnummer""",
        mandatory=True,
        show_in_edit_views=False,
        section="Material Information",
    )

    material_group = PropertyTypeAssignment(
        code="MATERIAL_GROUP",
        data_type="VARCHAR",
        property_label="Material group",
        description="""Material group (e.g. steel group)//Materialgruppe (z.B. Stahlgruppe)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Material Information",
    )

    characteristics = PropertyTypeAssignment(
        code="CHARACTERISTICS",
        data_type="VARCHAR",
        property_label="Characteristics",
        description="""Characteristics//Merkmale""",
        mandatory=False,
        show_in_edit_views=False,
        section="Material Information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class ParameterSet(ObjectType):
    defs = ObjectTypeDef(
        code="PARAMETER_SET",
        description="""IR-camera acquisition parameters//Aufnahmeeinstellung IR-Kamera""",
        generated_code_prefix="PAR_SET",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    parameter_set_spreadsheet = PropertyTypeAssignment(
        code="PARAMETER_SET.SPREADSHEET",
        data_type="XML",
        property_label="Parameter Table",
        description="""Table of parameters//Parameter-Tabelle""",
        mandatory=False,
        show_in_edit_views=False,
        section="Parameters",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class EnvironmentalConditions(ObjectType):
    defs = ObjectTypeDef(
        code="ENVIRONMENTAL_CONDITIONS",
        description="""Environmental conditions//Umgebungsbedingungen""",
        generated_code_prefix="ENV_COND",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    air_temperature_in_celsius = PropertyTypeAssignment(
        code="AIR_TEMPERATURE_IN_CELSIUS",
        data_type="REAL",
        property_label="Air Temperature [°C]",
        description="""Air Temperature in °C//Lufttemperatur in °C""",
        mandatory=True,
        show_in_edit_views=False,
        section="Atmospheric Conditions",
    )

    air_rel_humidity_in_percent = PropertyTypeAssignment(
        code="AIR_REL_HUMIDITY_IN_PERCENT",
        data_type="REAL",
        property_label="Relative Air Humidity [%]",
        description="""Relative Air Humidity in %//Relative Luftfeuchte in %""",
        mandatory=True,
        show_in_edit_views=False,
        section="Atmospheric Conditions",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class SampleNdt(ObjectType):
    defs = ObjectTypeDef(
        code="SAMPLE_NDT",
        description="""Sample used to validate Nondestructive Testing (NDT)-methods//Sample zur Validierung von Zerstörungsfreier Prüfverfahren""",
        generated_code_prefix="SAM_NDT",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=True,
        show_in_edit_views=False,
        section="Properties",
    )

    ndt_material = PropertyTypeAssignment(
        code="NDT.MATERIAL",
        data_type="VARCHAR",
        property_label="Material",
        description="""NDT Material//NDT Material""",
        mandatory=True,
        show_in_edit_views=False,
        section="Properties",
    )

    ndt_material_number = PropertyTypeAssignment(
        code="NDT.MATERIAL_NUMBER",
        data_type="VARCHAR",
        property_label="Material number",
        description="""NDT Material number//NDT Werkstoffnummer""",
        mandatory=False,
        show_in_edit_views=False,
        section="NDT Material number",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class SampleHolder(ObjectType):
    defs = ObjectTypeDef(
        code="SAMPLE_HOLDER",
        description="""Container holding the sample during measurement//Behälter für die Probe während der Messung""",
        generated_code_prefix="SAM_HOL_",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative Name",
        description="""e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    manufacturer = PropertyTypeAssignment(
        code="MANUFACTURER",
        data_type="VARCHAR",
        property_label="Manufacturer",
        description="""Manufacturer//Hersteller""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    sample_holder_material = PropertyTypeAssignment(
        code="SAMPLE_HOLDER_MATERIAL",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="SAMPLE_HOLDER_MATERIAL",
        property_label="Holder Material",
        description="""Material of the sample holder//Material des Probenbehälters""",
        mandatory=True,
        show_in_edit_views=False,
        section="Physical Properties",
    )

    sample_holder_thickness_in_mm = PropertyTypeAssignment(
        code="SAMPLE_HOLDER_THICKNESS_IN_MM",
        data_type="REAL",
        property_label="Thickness effective [mm]",
        description="""Sample Container Wall Thickness in mm//Wandstärke des Probenbehälters in mm""",
        mandatory=True,
        show_in_edit_views=False,
        section="Physical Properties",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class SamplePretreatment(ObjectType):
    defs = ObjectTypeDef(
        code="SAMPLE_PRETREATMENT",
        description="""Treatment of sample before measurement//Behandlung der Probe vor der Messung""",
        generated_code_prefix="SAM_PRE_",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    duration_in_seconds = PropertyTypeAssignment(
        code="DURATION_IN_SECONDS",
        data_type="REAL",
        property_label="Duration [s]",
        description="""The duration of the sample treatment in seconds//Die Dauer der Probenbehandlung in Sekunden""",
        mandatory=True,
        show_in_edit_views=False,
        section="Properties",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class InstrumentAccessory(ObjectType):
    defs = ObjectTypeDef(
        code="INSTRUMENT_ACCESSORY",
        description="""Instrument accessories//Instrumentzubehör""",
        generated_code_prefix="INS_ACC_",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    size_effective_mm = PropertyTypeAssignment(
        code="SIZE_EFFECTIVE_MM",
        data_type="REAL",
        property_label="Effective Dimension [mm]",
        description="""Instrument specific relevant size in mm//Instrumentspezifische relevante Größe in mm""",
        mandatory=False,
        show_in_edit_views=False,
        section="Properties",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class ComputationalAnalysis(ObjectType):
    defs = ObjectTypeDef(
        code="COMPUTATIONAL_ANALYSIS",
        description="""Computational analysis//Computergestützte Analyse""",
        generated_code_prefix="COMP_ANA",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    source_code_language = PropertyTypeAssignment(
        code="SOURCE_CODE_LANGUAGE",
        data_type="VARCHAR",
        property_label="Programming Language(s) Used",
        description="""Programming Language(s) used//Verwendete Programmiersprache(n)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class CondaEnvironment(ObjectType):
    defs = ObjectTypeDef(
        code="CONDA_ENVIRONMENT",
        description="""Conda environment//Conda-Umgebung""",
        generated_code_prefix="CON_ENV",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    conda_channels = PropertyTypeAssignment(
        code="CONDA_CHANNELS",
        data_type="MULTILINE_VARCHAR",
        property_label="Conda Channels",
        description="""Conda channels used//Verwendete Conda-Kanäle""",
        mandatory=True,
        show_in_edit_views=False,
        section="Technical Information",
    )

    conda_pip = PropertyTypeAssignment(
        code="CONDA_PIP",
        data_type="BOOLEAN",
        property_label="Pip Usage?",
        description="""Is pip used to install packages?//Wird pip zur Installation von Packages verwendet?""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class Hpc(ObjectType):
    defs = ObjectTypeDef(
        code="HPC",
        description="""High Performance Compute cluster//Hochleistungs-Rechnencluster""",
        generated_code_prefix="HPC",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative Name",
        description="""e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    hpc_ext_phys_address = PropertyTypeAssignment(
        code="HPC_EXT_PHYS_ADDRESS",
        data_type="VARCHAR",
        property_label="Physical Address of External HPC",
        description="""Physical address of external HPC//Adresse des externen HPC""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    hpc_ext_email_address = PropertyTypeAssignment(
        code="HPC_EXT_EMAIL_ADDRESS",
        data_type="VARCHAR",
        property_label="Email Address/Contact for External HPC",
        description="""Email address/point of contact for the external HPC//Email adresse/Kontaktstelle des externen HPC""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    operating_system = PropertyTypeAssignment(
        code="OPERATING_SYSTEM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="OPERATING_SYSTEM",
        property_label="Operating System",
        description="""Operating System (OS)//Betriebssystem""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    queuing_system = PropertyTypeAssignment(
        code="QUEUING_SYSTEM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="QUEUING_SYSTEM",
        property_label="Queuing System",
        description="""Queuing System used by HPC//Warteschlangensystem des HPCs""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    cpu_nodes_config = PropertyTypeAssignment(
        code="CPU_NODES_CONFIG",
        data_type="MULTILINE_VARCHAR",
        property_label="CPU Node Configuration",
        description="""CPU node configuration//Konfiguration der CPU-Knoten""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    gpu_nodes_config = PropertyTypeAssignment(
        code="GPU_NODES_CONFIG",
        data_type="MULTILINE_VARCHAR",
        property_label="GPU Node Configuration",
        description="""GPU node configuration//Konfiguration der GPU-Knoten""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    file_system_config = PropertyTypeAssignment(
        code="FILE_SYSTEM_CONFIG",
        data_type="MULTILINE_VARCHAR",
        property_label="File System Configuration",
        description="""File system configuration//Konfiguration des Dateisystems""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    reference = PropertyTypeAssignment(
        code="REFERENCE",
        data_type="MULTILINE_VARCHAR",
        property_label="References",
        description="""Useful refences""",
        mandatory=False,
        show_in_edit_views=False,
        section="External Documentation",
    )

    responsible_person = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Responsible person",
        description="""Responsible person//Verantwortliche Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    co_responsible_person = PropertyTypeAssignment(
        code="CO_RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Co-responsible person",
        description="""Co-responsible person//Weitere verantwortliche Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class InteratomicPotential(ObjectType):
    defs = ObjectTypeDef(
        code="INTERATOMIC_POTENTIAL",
        description="""Interatomic Potential//Interatomarer Potential""",
        generated_code_prefix="INT_POT",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    chem_species_addressed = PropertyTypeAssignment(
        code="CHEM_SPECIES_ADDRESSED",
        data_type="VARCHAR",
        property_label="Chemical Species Addressed",
        description="""Chemical species addressed//Angesprochene chemische Arten""",
        mandatory=False,
        show_in_edit_views=False,
        section="Material Information",
    )

    atom_potential_style = PropertyTypeAssignment(
        code="ATOM_POTENTIAL_STYLE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="ATOM_POTENTIAL_STYLE",
        property_label="Interatomic Potential Style",
        description="""Interatomic Potential Style//Interatomarer Potential Stil""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    source_link = PropertyTypeAssignment(
        code="SOURCE_LINK",
        data_type="MULTILINE_VARCHAR",
        property_label="Source for download",
        description="""Source/Download//Quelle/Herunterladen""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    sftw_compatibility = PropertyTypeAssignment(
        code="SFTW_COMPATIBILITY",
        data_type="VARCHAR",
        property_label="Software Compatibility",
        description="""Software which can use this file//Software, die diese Datei verwenden kann""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    reference = PropertyTypeAssignment(
        code="REFERENCE",
        data_type="MULTILINE_VARCHAR",
        property_label="References",
        description="""Useful refences""",
        mandatory=False,
        show_in_edit_views=False,
        section="External Documentation",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class JupyterNotebook(ObjectType):
    defs = ObjectTypeDef(
        code="JUPYTER_NOTEBOOK",
        description="""Jupyter Notebook//Jupyter-Notebook""",
        generated_code_prefix="JUP_NTB",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    source_code_language = PropertyTypeAssignment(
        code="SOURCE_CODE_LANGUAGE",
        data_type="VARCHAR",
        property_label="Programming Language(s) Used",
        description="""Programming Language(s) used//Verwendete Programmiersprache(n)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    jupyter_modules = PropertyTypeAssignment(
        code="JUPYTER_MODULES",
        data_type="MULTILINE_VARCHAR",
        property_label="Modules Used",
        description="""Modules used in the notebook//Im Notebook verwendete Module""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    jupyter_headers = PropertyTypeAssignment(
        code="JUPYTER_HEADERS",
        data_type="MULTILINE_VARCHAR",
        property_label="Headers Used (Programming)",
        description="""Headers used in the notebook//Im Notebook verwendete Headers""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class Pseudopotential(ObjectType):
    defs = ObjectTypeDef(
        code="PSEUDOPOTENTIAL",
        description="""Pseudoptential for electronic structure simulations//Pseudoptential für Elektronische-Struktur Simulationen""",
        generated_code_prefix="PSE",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    version = PropertyTypeAssignment(
        code="VERSION",
        data_type="VARCHAR",
        property_label="Version",
        description="""Version""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    license = PropertyTypeAssignment(
        code="LICENSE",
        data_type="VARCHAR",
        property_label="License",
        description="""License//Lizenz""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    chem_species_addressed = PropertyTypeAssignment(
        code="CHEM_SPECIES_ADDRESSED",
        data_type="VARCHAR",
        property_label="Chemical Species Addressed",
        description="""Chemical species addressed//Angesprochene chemische Arten""",
        mandatory=False,
        show_in_edit_views=False,
        section="Material Information",
    )

    pseudopot_func = PropertyTypeAssignment(
        code="PSEUDOPOT_FUNC",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="PSEUDOPOT_FUNCTIONAL",
        property_label="Functional Compatibility",
        description="""Functional compatibility//Funktional-Kompatibilität""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    pseudopot_type = PropertyTypeAssignment(
        code="PSEUDOPOT_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="PSEUDOPOT_TYPE",
        property_label="Type of Pseudopotenial",
        description="""Type of pseudopotenial//Art des Pseudopotenials""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    sw_compatibility = PropertyTypeAssignment(
        code="SW_COMPATIBILITY",
        data_type="VARCHAR",
        property_label="Software Compatibility",
        description="""Software which can use this file//Software, die diese Datei verwenden kann""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    pseudopot_semicore = PropertyTypeAssignment(
        code="PSEUDOPOT_SEMICORE",
        data_type="VARCHAR",
        property_label="Semicore Shells Considered as Valence",
        description="""Semicore shells considered as valence//Halbkernschalen, die als Valenz betrachtet werden""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    reference = PropertyTypeAssignment(
        code="REFERENCE",
        data_type="MULTILINE_VARCHAR",
        property_label="References",
        description="""Useful refences""",
        mandatory=False,
        show_in_edit_views=False,
        section="External Documetation",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class PyironJob(ObjectType):
    defs = ObjectTypeDef(
        code="PYIRON_JOB",
        description="""Generic pyiron job//Allgemeines pyiron Job""",
        generated_code_prefix="PYI_JOB",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    bam_username = PropertyTypeAssignment(
        code="BAM_USERNAME",
        data_type="VARCHAR",
        property_label="BAM username",
        description="""BAM username//BAM Benutzername""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    workflow_manager = PropertyTypeAssignment(
        code="WORKFLOW_MANAGER",
        data_type="VARCHAR",
        property_label="Workflow Manager",
        description="""Workflow manager//Workflow-Manager""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    sim_job_finished = PropertyTypeAssignment(
        code="SIM_JOB_FINISHED",
        data_type="BOOLEAN",
        property_label="Is the job finished?",
        description="""Finished = True, Aborted or incomplete = False//Beendet = Wahr, Abgebrochen oder unvollständig = Falsch""",
        mandatory=False,
        show_in_edit_views=False,
        section="Pyiron Information",
    )

    start_date = PropertyTypeAssignment(
        code="START_DATE",
        data_type="TIMESTAMP",
        property_label="Start date",
        description="""Start date//Startdatum""",
        mandatory=False,
        show_in_edit_views=False,
        section="Pyiron Information",
    )

    sim_walltime_in_hours = PropertyTypeAssignment(
        code="SIM_WALLTIME_IN_HOURS",
        data_type="REAL",
        property_label="Job Run Time (Walltime) [hr]",
        description="""Total job run time [hr]//Gesamtlaufzeit des Jobs [Stunden]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Pyiron Information",
    )

    sim_coretime_in_hours = PropertyTypeAssignment(
        code="SIM_CORETIME_IN_HOURS",
        data_type="REAL",
        property_label="Total Job Core Time [hr]",
        description="""Total core hours used [hr]//Gesamtkernstundenzeit des Jobs [Stunden]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Pyiron Information",
    )

    ncores = PropertyTypeAssignment(
        code="NCORES",
        data_type="INTEGER",
        property_label="Number of Cores",
        description="""Number of cores used//Anzahl der Kerne""",
        mandatory=False,
        show_in_edit_views=False,
        section="Pyiron Information",
    )

    ngpus = PropertyTypeAssignment(
        code="NGPUS",
        data_type="INTEGER",
        property_label="Number of GPUs",
        description="""Number of GPUs used//Anzahl der GPUs""",
        mandatory=False,
        show_in_edit_views=False,
        section="Pyiron Information",
    )

    nthreads = PropertyTypeAssignment(
        code="NTHREADS",
        data_type="INTEGER",
        property_label="Number of Threads",
        description="""Number of Threads used//Anzahl der Threads""",
        mandatory=False,
        show_in_edit_views=False,
        section="Pyiron Information",
    )

    hpc_job_queue = PropertyTypeAssignment(
        code="HPC_JOB_QUEUE",
        data_type="VARCHAR",
        property_label="HPC Job Queue",
        description="""HPC queue used//Verwendete HPC-Warteschlange""",
        mandatory=False,
        show_in_edit_views=False,
        section="Pyiron Information",
    )

    hpc_job_id = PropertyTypeAssignment(
        code="HPC_JOB_ID",
        data_type="VARCHAR",
        property_label="HPC Job ID",
        description="""Job ID in the HPC queue//Job-ID in der HPC-Warteschlange""",
        mandatory=False,
        show_in_edit_views=False,
        section="Pyiron Information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    conceptual_dictionary = PropertyTypeAssignment(
        code="CONCEPTUAL_DICTIONARY",
        data_type="MULTILINE_VARCHAR",
        property_label="Conceptual Dictionary",
        description="""Conceptual dictionary associated with pyiron job//Begriffswörterbuch zu pyiron job""",
        mandatory=False,
        show_in_edit_views=False,
        section="Annotations",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class SoftwareCode(ObjectType):
    defs = ObjectTypeDef(
        code="SOFTWARE_CODE",
        description="""(Computational) software code reference//(Computational) software code reference""",
        generated_code_prefix="SW_CODE",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    version = PropertyTypeAssignment(
        code="VERSION",
        data_type="VARCHAR",
        property_label="Version",
        description="""Version""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    license = PropertyTypeAssignment(
        code="LICENSE",
        data_type="VARCHAR",
        property_label="License",
        description="""License//Lizenz""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    source_link = PropertyTypeAssignment(
        code="SOURCE_LINK",
        data_type="MULTILINE_VARCHAR",
        property_label="Source for download",
        description="""Source/Download//Quelle/Herunterladen""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    software_name = PropertyTypeAssignment(
        code="SOFTWARE_NAME",
        data_type="VARCHAR",
        property_label="Software Name",
        description="""Software name//Software-Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="Technical Information",
    )

    reference = PropertyTypeAssignment(
        code="REFERENCE",
        data_type="MULTILINE_VARCHAR",
        property_label="References",
        description="""Useful refences""",
        mandatory=False,
        show_in_edit_views=False,
        section="External Documentation",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class WorkflowReference(ObjectType):
    defs = ObjectTypeDef(
        code="WORKFLOW_REFERENCE",
        description="""Workflow reference//Workflowreferenz""",
        generated_code_prefix="WOR_REF",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    reference = PropertyTypeAssignment(
        code="REFERENCE",
        data_type="MULTILINE_VARCHAR",
        property_label="References",
        description="""Useful refences""",
        mandatory=False,
        show_in_edit_views=False,
        section="External Documetation",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class MaterialV1(ObjectType):
    defs = ObjectTypeDef(
        code="MATERIAL_V1",
        description="""Material definition for BAM (v1)//Materialdefinition für BAM (v1)""",
        generated_code_prefix="MAT_V1",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    mat_bonding_type = PropertyTypeAssignment(
        code="MAT_BONDING_TYPE",
        data_type="VARCHAR",
        property_label="Material Bonding Type",
        description="""Material bonding type//Material Atombindungstyp""",
        mandatory=False,
        show_in_edit_views=False,
        section="Material Information",
    )

    mat_structure = PropertyTypeAssignment(
        code="MAT_STRUCTURE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="MAT_STRUCTURE",
        property_label="Material Structure",
        description="""Material Structure//Materialstruktur""",
        mandatory=False,
        show_in_edit_views=False,
        section="Material Information",
    )

    chem_species_by_wt_in_pct = PropertyTypeAssignment(
        code="CHEM_SPECIES_BY_WT_IN_PCT",
        data_type="VARCHAR",
        property_label="Chemical Species by weight [%]",
        description="""Chemical species involved by weight [%]//Inbegriffene chemische Spezies nach Gewicht [%]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Material Information",
    )

    chem_species_by_comp_in_pct = PropertyTypeAssignment(
        code="CHEM_SPECIES_BY_COMP_IN_PCT",
        data_type="VARCHAR",
        property_label="Chemical species involved by composition [%]",
        description="""Chemical species involved by composition [%]//Inbegriffene chemische Spezies nach Zusammensetzung [%]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Material Information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class MatSimStructure(ObjectType):
    defs = ObjectTypeDef(
        code="MAT_SIM_STRUCTURE",
        description="""Material simulation structure // Material-Simulationsstruktur""",
        generated_code_prefix="MAT_SIM_STR",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    workflow_manager = PropertyTypeAssignment(
        code="WORKFLOW_MANAGER",
        data_type="VARCHAR",
        property_label="Workflow Manager",
        description="""Workflow manager//Workflow-Manager""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )

    crystal_orientation = PropertyTypeAssignment(
        code="CRYSTAL_ORIENTATION",
        data_type="VARCHAR",
        property_label="Crystallographic Orientation",
        description="""Miller indices//Millersche Indizes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Material Information",
    )

    sim_cell_lengths_in_a = PropertyTypeAssignment(
        code="SIM_CELL_LENGTHS_IN_A",
        data_type="VARCHAR",
        property_label="Simulation Cell Lengths [Å]",
        description="""Simulation cell lengths [Å]//Längen der Simulationszelle [Å]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Simulation Information",
    )

    sim_cell_vectors = PropertyTypeAssignment(
        code="SIM_CELL_VECTORS",
        data_type="VARCHAR",
        property_label="Simulation Cell Vectors",
        description="""Simulation cell vectors//Vektoren der Simulationszelle""",
        mandatory=False,
        show_in_edit_views=False,
        section="Simulation Information",
    )

    sim_cell_angles_in_deg = PropertyTypeAssignment(
        code="SIM_CELL_ANGLES_IN_DEG",
        data_type="VARCHAR",
        property_label="Simulation Cell Angles [Degrees]",
        description="""Simulation cell angles [Degrees]//Winkel der Simulationszelle [Grad]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Simulation Information",
    )

    sim_cell_volume_in_a3 = PropertyTypeAssignment(
        code="SIM_CELL_VOLUME_IN_A3",
        data_type="REAL",
        property_label="Simulation Cell Volume [Å^3]",
        description="""Simulation cell volume [Å^3]//Volumen der Simulationszelle [Å^3]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Simulation Information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    conceptual_dictionary = PropertyTypeAssignment(
        code="CONCEPTUAL_DICTIONARY",
        data_type="MULTILINE_VARCHAR",
        property_label="Conceptual Dictionary",
        description="""Conceptual dictionary associated with pyiron job//Begriffswörterbuch zu pyiron job""",
        mandatory=False,
        show_in_edit_views=False,
        section="Annotations",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class Dcpd(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.DCPD",
        description="""Direct Current Potential Drop (DCPD) Method//DC-Spannungsabfall (DCPD)-Methode""",
        generated_code_prefix="EXP.DCPD",
    )

    dcpd_pot_drop_cal = PropertyTypeAssignment(
        code="DCPD_POT_DROP_CAL",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DCPD_POT_CAL",
        property_label="Potential Drop Calibration",
        description="""Potential Drop Calibration//Kalibrierung des Potentialabfalls""",
        mandatory=False,
        show_in_edit_views=False,
        section="Setup",
    )

    dcpd_current = PropertyTypeAssignment(
        code="DCPD_CURRENT",
        data_type="REAL",
        property_label="Current [A]",
        description="""DCPD Current [A]//DCPD Stromstärke [A]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Setup",
    )

    dcpd_initial_cracklength = PropertyTypeAssignment(
        code="DCPD_INITIAL_CRACKLENGTH",
        data_type="REAL",
        property_label="Initial Cracklength (measured optically) [mm]",
        description="""Initial Cracklength (measured optically) [mm]// Initiale Risslänge (optisch vermessen) [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Setup",
    )

    dcpd_yzero_fitted = PropertyTypeAssignment(
        code="DCPD_YZERO_FITTED",
        data_type="REAL",
        property_label="Y0 in Johnson Formula fitted for Notch Geometry [mm]",
        description="""Y0 in Johnson Formula fitted for Notch Geometry [mm]//Y0 in Johnson Formel angepasst an die Kerbgeometrie [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Setup",
    )

    fem_fit_eq = PropertyTypeAssignment(
        code="FEM_FIT_EQ",
        data_type="VARCHAR",
        property_label="Equation of FEM Fit a = f(U)",
        description="""Equation of FEM Fit a = f(U)//Gleichung für FEM Fit a = f(U)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Setup",
    )

    dcpd_proportional_potential = PropertyTypeAssignment(
        code="DCPD_PROPORTIONAL_POTENTIAL",
        data_type="BOOLEAN",
        property_label="Output Signal proportional to Potential Drop",
        description="""Output Signal proportional to Potential Drop//Ausgangssignal proportional zum Potentialabfall""",
        mandatory=False,
        show_in_edit_views=False,
        section="Direct Amplification of Corrected Potential Drop",
    )

    dcpd_initial_potential_drop = PropertyTypeAssignment(
        code="DCPD_INITIAL_POTENTIAL_DROP",
        data_type="REAL",
        property_label="Initial Potential Drop (amplified) [V]",
        description="""Initial Potential Drop (amplified) [V]//Initiale Potentialabfall (verstärkt) [V]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Direct Amplification of Corrected Potential Drop",
    )

    dcpd_amplification_factor = PropertyTypeAssignment(
        code="DCPD_AMPLIFICATION_FACTOR",
        data_type="REAL",
        property_label="Amplification Factor",
        description="""Amplification Factor//Verstärkungsfaktor""",
        mandatory=False,
        show_in_edit_views=False,
        section="Direct Amplification of Corrected Potential Drop",
    )

    dcpd_linearised_potential = PropertyTypeAssignment(
        code="DCPD_LINEARISED_POTENTIAL",
        data_type="BOOLEAN",
        property_label="Output Signal Proportional to Cracklength",
        description="""Output Signal Proportional to Cracklength//Ausgangssignal proportional zur Risslänge""",
        mandatory=False,
        show_in_edit_views=False,
        section="Output Potential Proportional to Cracklength",
    )

    dcpd_temp_comp = PropertyTypeAssignment(
        code="DCPD_TEMP_COMP",
        data_type="BOOLEAN",
        property_label="Temperature Compensation",
        description="""Temperature Compensation//Temperaturkompensation""",
        mandatory=False,
        show_in_edit_views=False,
        section="Temperature Compensation",
    )

    dcpd_initial_temp = PropertyTypeAssignment(
        code="DCPD_INITIAL_TEMP",
        data_type="REAL",
        property_label="Initial Temperature [°C]",
        description="""Initial Temperature [°C]//Anfangstemperatur [°C]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Temperature Compensation",
    )

    dcpd_temp_coeff = PropertyTypeAssignment(
        code="DCPD_TEMP_COEFF",
        data_type="REAL",
        property_label="Temperature Coefficient of Resistivity [°C^-1]",
        description="""Temperature Coefficient of Resistivity [°C^-1]//Temperaturkoeffizient der Resistivität [°C^-1]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Temperature Compensation",
    )


class FcgTest(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.FCG_TEST",
        description="""Fatigue Crack Growth Test//Rissfortschrittsversuch""",
        generated_code_prefix="EXP.FCG_TEST",
    )

    fcg_nominal_r = PropertyTypeAssignment(
        code="FCG_NOMINAL_R",
        data_type="REAL",
        property_label="Test Nominal R-Ratio",
        description="""Test Nominal R-Ratio//Nominelles R-Verhältnis des Tests""",
        mandatory=True,
        show_in_edit_views=False,
        section="Experimental Details FCG",
    )

    fcg_thrshld = PropertyTypeAssignment(
        code="FCG_THRSHLD",
        data_type="BOOLEAN",
        property_label="Threshold Determination",
        description="""Threshold Stress Intensity Factor Range Determination//Ermittlung des Schwellenwertes gegen Ermüdungsrissausbreitung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Experimental Details FCG",
    )

    fcg_paris = PropertyTypeAssignment(
        code="FCG_PARIS",
        data_type="BOOLEAN",
        property_label="PARIS Parameters Determination",
        description="""PARIS Regime Parameters Determination//Ermittlung der PARIS-Parameter""",
        mandatory=False,
        show_in_edit_views=False,
        section="Experimental Details FCG",
    )

    fcg_cyclic_r = PropertyTypeAssignment(
        code="FCG_CYCLIC_R",
        data_type="BOOLEAN",
        property_label="Cyclic R-Curve",
        description="""Cyclic R-Curve Determination//Ermittlung der zyklischen R-Kurve""",
        mandatory=False,
        show_in_edit_views=False,
        section="Experimental Details FCG",
    )

    fcg_result_thrshld = PropertyTypeAssignment(
        code="FCG_RESULT_THRSHLD",
        data_type="REAL",
        property_label="Threshold Stress intensity Factor Range",
        description="""Threshold Stress Intensity Factor Range//Schwellenwert gegen Ermüdungsrissausbreitung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Experimental Results",
    )

    fcg_result_paris_c = PropertyTypeAssignment(
        code="FCG_RESULT_PARIS_C",
        data_type="REAL",
        property_label="PARIS Parameter C",
        description="""PARIS Parameter C//PARIS Parameter C""",
        mandatory=False,
        show_in_edit_views=False,
        section="Experimental Results",
    )

    fcg_result_paris_m = PropertyTypeAssignment(
        code="FCG_RESULT_PARIS_M",
        data_type="REAL",
        property_label="PARIS Parameter m",
        description="""PARIS Parameter m//PARIS Parameter m""",
        mandatory=False,
        show_in_edit_views=False,
        section="Experimental Results",
    )

    fcg_result_cyclicr_a = PropertyTypeAssignment(
        code="FCG_RESULT_CYCLICR_A",
        data_type="REAL",
        property_label="Cyclic R-Curve Parameter A",
        description="""Cyclic R-Curve Parameter A//Zyklische R-Kurve Parameter A""",
        mandatory=False,
        show_in_edit_views=False,
        section="Experimental Results",
    )

    fcg_result_cyclicr_b = PropertyTypeAssignment(
        code="FCG_RESULT_CYCLICR_B",
        data_type="REAL",
        property_label="Cyclic R-Curve Parameter b",
        description="""Cyclic R-Curve Parameter b//Zyklische R-Kurve Parameter b""",
        mandatory=False,
        show_in_edit_views=False,
        section="Experimental Results",
    )


class RazorbladeNotching(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.RAZORBLADE_NOTCHING",
        description="""Razorblade Notching//Kerbeinbringung mittels Rasierklinge""",
        generated_code_prefix="EXP.FCG_RAZOR",
    )

    razor_strokelength = PropertyTypeAssignment(
        code="RAZOR_STROKELENGTH",
        data_type="REAL",
        property_label="Stroke Length [mm]",
        description="""Stroke Length [mm]//Klingenhub [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Process Parameters",
    )

    razor_strokespeed = PropertyTypeAssignment(
        code="RAZOR_STROKESPEED",
        data_type="REAL",
        property_label="Stroke Speed [mm/s]",
        description="""Stroke Speed [mm/s]//Hubgeschwindigkeit [mm/s]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Process Parameters",
    )

    razor_strokecount = PropertyTypeAssignment(
        code="RAZOR_STROKECOUNT",
        data_type="REAL",
        property_label="Stroke Count",
        description="""Stroke Count//Anzahl der Klingenhuebe""",
        mandatory=False,
        show_in_edit_views=False,
        section="Process Parameters",
    )

    razor_depth = PropertyTypeAssignment(
        code="RAZOR_DEPTH",
        data_type="REAL",
        property_label="Notch Depth Increase according to Gauge [µm]",
        description="""Notch Depth Increase according to Gauge [µm]//Kerbvertiefenzunahme nach Messuhr [µm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Results",
    )


class FcgStep(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.FCG_STEP",
        description="""Single Step of a Fatigue Crack Growth (FCG) Test//Einzelner Schritt eines Rissfortschritt-Tests""",
        generated_code_prefix="EXP.FCG_STEP",
    )

    step_no = PropertyTypeAssignment(
        code="STEP_NO",
        data_type="INTEGER",
        property_label="Step No.",
        description="""Step Number//Schrittnummer""",
        mandatory=True,
        show_in_edit_views=False,
        section="Step Information",
    )

    fcg_step_type = PropertyTypeAssignment(
        code="FCG_STEP_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="FCG_STEP_TYPE",
        property_label="Step Type",
        description="""Step Type//Versuchsschritt-Typ""",
        mandatory=False,
        show_in_edit_views=False,
        section="Step Information",
    )

    fcg_step_precrack = PropertyTypeAssignment(
        code="FCG_STEP_PRECRACK",
        data_type="BOOLEAN",
        property_label="Precracking Step",
        description="""Precracking Step//Precracking-Schritt""",
        mandatory=False,
        show_in_edit_views=False,
        section="Step Information",
    )

    initial_cycles = PropertyTypeAssignment(
        code="INITIAL_CYCLES",
        data_type="INTEGER",
        property_label="Initial Cycle Count",
        description="""Initial Cycle Count//Initiale Zyklenzahl""",
        mandatory=False,
        show_in_edit_views=False,
        section="Step Initial Parameters (Manual Input)",
    )

    initial_cracklength = PropertyTypeAssignment(
        code="INITIAL_CRACKLENGTH",
        data_type="REAL",
        property_label="Initial Cracklength [mm]",
        description="""Initial Cracklength [mm]//Initiale Risslänge [mm]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Step Initial Parameters (Manual Input)",
    )

    initial_r_ratio = PropertyTypeAssignment(
        code="INITIAL_R_RATIO",
        data_type="REAL",
        property_label="Initial R-Ratio",
        description="""Initial R-Ratio//Initiales R-Verhältnis""",
        mandatory=False,
        show_in_edit_views=False,
        section="Step Initial Parameters (Manual Input)",
    )

    initial_deltak = PropertyTypeAssignment(
        code="INITIAL_DELTAK",
        data_type="REAL",
        property_label="Initial Delta K [MPa*m^0,5]",
        description="""Initial Delta K [MPa*m^0,5]//Initiales Delta K [MPa*m^0,5]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Step Initial Parameters (Manual Input)",
    )

    deltak_exponent = PropertyTypeAssignment(
        code="DELTAK_EXPONENT",
        data_type="REAL",
        property_label="Exponent for Delta K increase or decrease [mm^-1]",
        description="""Exponent for Delta K increase or decrease [mm^-1]//Exponent für Lastabsenkung oder -erhöhung [mm^-1]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Step Initial Parameters (Manual Input)",
    )

    increment_dadn = PropertyTypeAssignment(
        code="INCREMENT_DADN",
        data_type="REAL",
        property_label="Increment for da/dN calculation [mm]",
        description="""Increment for da/dN calculation [mm]//Inkrement für die Rissfortschrittsratenbestimmung [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Step Initial Parameters (Manual Input)",
    )

    final_cycles = PropertyTypeAssignment(
        code="FINAL_CYCLES",
        data_type="REAL",
        property_label="Final Cycle Count",
        description="""Final Cycle Count//Finale Zyklenzahl""",
        mandatory=False,
        show_in_edit_views=False,
        section="Step Final Parameters (Manual Input)",
    )

    final_cracklength = PropertyTypeAssignment(
        code="FINAL_CRACKLENGTH",
        data_type="REAL",
        property_label="Final Cracklength [mm]",
        description="""Final Cracklength [mm]//Finale Risslänge [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Step Final Parameters (Manual Input)",
    )

    final_r_ratio = PropertyTypeAssignment(
        code="FINAL_R_RATIO",
        data_type="REAL",
        property_label="Final R-Ratio",
        description="""Final R-Ratio//Finales R-Verhältnis""",
        mandatory=False,
        show_in_edit_views=False,
        section="Step Final Parameters (Manual Input)",
    )

    final_deltak = PropertyTypeAssignment(
        code="FINAL_DELTAK",
        data_type="REAL",
        property_label="Final Delta K [MPa*m^0,5]",
        description="""Final Delta K [MPa*m^0,5]//Finales Delta K [MPa*m^0,5]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Step Final Parameters (Manual Input)",
    )

    propagation = PropertyTypeAssignment(
        code="PROPAGATION",
        data_type="BOOLEAN",
        property_label="Crack Propagation during Step",
        description="""Crack Propagation during Step//Risserweiterung während des Versuchschrittes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Propagation/Arrest",
    )

    arrest = PropertyTypeAssignment(
        code="ARREST",
        data_type="BOOLEAN",
        property_label="Crack Arrest during Step",
        description="""Crack Arrest during Step//Rissarrest während des Versuchschrittes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Propagation/Arrest",
    )

    initial_kmax = PropertyTypeAssignment(
        code="INITIAL_KMAX",
        data_type="REAL",
        property_label="Initial K_max [MPa*m^0,5]",
        description="""Initial K_max [MPa*m^0,5]//Initiales K_max [MPa*m^0,5]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Derived Parameters (Automatic Input)",
    )

    initial_kmin = PropertyTypeAssignment(
        code="INITIAL_KMIN",
        data_type="REAL",
        property_label="Initial K_min [MPa*m^0,5]",
        description="""Initial K_min [MPa*m^0,5]//Initiales K_min [MPa*m^0,5]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Derived Parameters (Automatic Input)",
    )

    initial_kamp = PropertyTypeAssignment(
        code="INITIAL_KAMP",
        data_type="REAL",
        property_label="Initial K_amp [MPa*m^0,5]",
        description="""Initial K_amp [MPa*m^0,5]//Initiales K_amp [MPa*m^0,5]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Derived Parameters (Automatic Input)",
    )

    initial_kmean = PropertyTypeAssignment(
        code="INITIAL_KMEAN",
        data_type="REAL",
        property_label="Initial K_mean [MPa*m^0,5]",
        description="""Initial K_mean [MPa*m^0,5]//Initiales K_mean [MPa*m^0,5]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Derived Parameters (Automatic Input)",
    )

    initial_geomfun = PropertyTypeAssignment(
        code="INITIAL_GEOMFUN",
        data_type="REAL",
        property_label="Initial Stress Intensity Factor Geometry Function",
        description="""Initial Stress Intensity Factor Geometry Function//Initiale Geometriefunktion des Spannungsintensitätsfaktors""",
        mandatory=False,
        show_in_edit_views=False,
        section="Derived Parameters (Automatic Input)",
    )

    initial_deltaf = PropertyTypeAssignment(
        code="INITIAL_DELTAF",
        data_type="REAL",
        property_label="Initial Delta F [kN]",
        description="""Initial Delta F [kN]//Initiales Delta F [kN]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Derived Parameters (Automatic Input)",
    )

    initial_fmax = PropertyTypeAssignment(
        code="INITIAL_FMAX",
        data_type="REAL",
        property_label="Initial F_max [kN]",
        description="""Initial F_max [kN]//Initiales F_max [kN]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Derived Parameters (Automatic Input)",
    )

    initial_fmin = PropertyTypeAssignment(
        code="INITIAL_FMIN",
        data_type="REAL",
        property_label="Initial F_min [kN]",
        description="""Initial F_min [kN]//Initiales F_min [kN]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Derived Parameters (Automatic Input)",
    )

    initial_famp = PropertyTypeAssignment(
        code="INITIAL_FAMP",
        data_type="REAL",
        property_label="Initial F_amp [kN]",
        description="""Initial F_amp [kN]//Initiales F_amp [kN]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Derived Parameters (Automatic Input)",
    )

    initial_fmean = PropertyTypeAssignment(
        code="INITIAL_FMEAN",
        data_type="REAL",
        property_label="Initial F_mean [kN]",
        description="""Initial F_mean [kN]//Initiales F_mean [kN]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Derived Parameters (Automatic Input)",
    )

    initial_ssy_ratio = PropertyTypeAssignment(
        code="INITIAL_SSY_RATIO",
        data_type="REAL",
        property_label="Ratio of Ligament Length to critical Ligament Length",
        description="""Ratio of Ligament Length to critical Ligament Length//Verhältnis von Ligamentlänge zu kritischer Ligamentlänge""",
        mandatory=False,
        show_in_edit_views=False,
        section="Derived Parameters (Automatic Input)",
    )

    delta_a = PropertyTypeAssignment(
        code="DELTA_A",
        data_type="REAL",
        property_label="Crack Extension [mm]",
        description="""Crack Extension [mm]//Risserweiterung [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Derived Parameters (Automatic Input)",
    )

    delta_n = PropertyTypeAssignment(
        code="DELTA_N",
        data_type="INTEGER",
        property_label="Elapsed Cycles in Step",
        description="""Elapsed Cycles in Step//Im Versuchsschritt gefahrene Zyklen""",
        mandatory=False,
        show_in_edit_views=False,
        section="Derived Parameters (Automatic Input)",
    )

    final_geomfun = PropertyTypeAssignment(
        code="FINAL_GEOMFUN",
        data_type="REAL",
        property_label="Final Stress Intensity Factor Geometry Function",
        description="""Final Stress Intensity Factor Geometry Function//Finale Geometriefunktion des Spannungsintensitätsfaktors""",
        mandatory=False,
        show_in_edit_views=False,
        section="Derived Parameters (Automatic Input)",
    )

    final_deltaf = PropertyTypeAssignment(
        code="FINAL_DELTAF",
        data_type="REAL",
        property_label="Final Delta F [kN]",
        description="""Final Delta F [kN]//Finales Delta F [kN]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Derived Parameters (Automatic Input)",
    )

    final_fmax = PropertyTypeAssignment(
        code="FINAL_FMAX",
        data_type="REAL",
        property_label="Final F_max [kN]",
        description="""Final F_max [kN]//Finales F_max [kN]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Derived Parameters (Automatic Input)",
    )

    final_fmin = PropertyTypeAssignment(
        code="FINAL_FMIN",
        data_type="REAL",
        property_label="Final F_min [kN]",
        description="""Final F_min [kN]//Finales F_min [kN]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Derived Parameters (Automatic Input)",
    )

    final_famp = PropertyTypeAssignment(
        code="FINAL_FAMP",
        data_type="REAL",
        property_label="Final F_amp [kN]",
        description="""Final F_amp [kN]//Finales F_amp [kN]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Derived Parameters (Automatic Input)",
    )

    final_fmean = PropertyTypeAssignment(
        code="FINAL_FMEAN",
        data_type="REAL",
        property_label="Final F_mean [kN]",
        description="""Final F_mean [kN]//Finales F_mean [kN]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Derived Parameters (Automatic Input)",
    )

    final_ssy_ratio = PropertyTypeAssignment(
        code="FINAL_SSY_RATIO",
        data_type="REAL",
        property_label="Ratio of Ligament Length to critical Ligament Length",
        description="""Ratio of Ligament Length to critical Ligament Length//Verhältnis von Ligamentlänge zu kritischer Ligamentlänge""",
        mandatory=False,
        show_in_edit_views=False,
        section="Derived Parameters (Automatic Input)",
    )


class ForceTransducer(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.FORCE_TRANSDUCER",
        description="""Force Transducer//Kraftmesseinrichtung""",
        generated_code_prefix="INS.FORCE_TRANSD",
    )

    force_transducer_type = PropertyTypeAssignment(
        code="FORCE_TRANSDUCER_TYPE",
        data_type="VARCHAR",
        property_label="Force Transducer Type",
        description="""Force Transducer Type Code as specified by Manufacturer//Typenbezeichnung des Herstellers für die Kraftmesseinrichtung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )

    max_static_force = PropertyTypeAssignment(
        code="MAX_STATIC_FORCE",
        data_type="REAL",
        property_label="Maximum Static Force [kN]",
        description="""Maximum Static Force in kN//Maximale statische Kraft [kN]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Technical Details",
    )

    max_dynamic_force = PropertyTypeAssignment(
        code="MAX_DYNAMIC_FORCE",
        data_type="REAL",
        property_label="Maximum Dynamic Force [kN]",
        description="""Maximum Dynamic Force in kN//Maximale dynamische Kraft [kN[""",
        mandatory=True,
        show_in_edit_views=False,
        section="Technical Details",
    )

    max_excitation_voltage = PropertyTypeAssignment(
        code="MAX_EXCITATION_VOLTAGE",
        data_type="REAL",
        property_label="Maximum Excitation Voltage [V]",
        description="""Maximum Excitation Voltage [V]//Maximale Speisespannung [V]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Technical Details",
    )

    calibration_interval = PropertyTypeAssignment(
        code="CALIBRATION_INTERVAL",
        data_type="INTEGER",
        property_label="Calibration Interval [Months]",
        description="""Calibration Interval [Months]//Kalibrierintervall [Monate]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Status",
    )


class MicroscopyFcgFractureSurfaceCracklength(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MICROSCOPY_FCG_FRACTURE_SURFACE_CRACKLENGTH",
        description="""Optical Measurement of Cracklength on the Fracture Surface of an FCG Specimen//Lichtmikroskopische Messung einer Risslänge auf der Bruchfläche einer Ermüdungsrissfortschrittsprobe""",
        generated_code_prefix="EXP.MIC_FCG_FRACSURF_CRACKLENGTH",
    )

    mic_fcg_fracsurf_cracklength_type = PropertyTypeAssignment(
        code="MIC_FCG_FRACSURF_CRACKLENGTH_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="MICROSCOPY_FCG_CRACKLENGTH_TYPE",
        property_label="Type of Cracklength measured on Fracture Surface",
        description="""Type of Cracklength measured on Fracture Surface//Art der auf der Bruchfläche gemessenen Risslänge""",
        mandatory=False,
        show_in_edit_views=False,
        section="Experimental Details",
    )

    mic_fcg_fracsurf_cracklength_value = PropertyTypeAssignment(
        code="MIC_FCG_FRACSURF_CRACKLENGTH_VALUE",
        data_type="REAL",
        property_label="Value of Cracklength measured on Fracture Surface [mm]",
        description="""Value of Cracklength measured on Fracture Surface [mm]//Wert der auf der Bruchfläche gemessenen Risslänge [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Experimental Details",
    )

    mic_fcg_fracsurf_cracklength_cycles = PropertyTypeAssignment(
        code="MIC_FCG_FRACSURF_CRACKLENGTH_CYCLES",
        data_type="INTEGER",
        property_label="Cycle Count corresponding with Cracklength measured on Fracture Surface",
        description="""Cycle Count corresponding with Cracklength measured on Fracture Surface//Mit der auf der Bruchfläche gemessenen Länge korrespondierende Zyklenzahl""",
        mandatory=False,
        show_in_edit_views=False,
        section="Experimental Details",
    )


class FcgEvaluation(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.FCG_EVALUATION",
        description="""Fatigue Crack Growth Data Evaluation//Rissfortschrittsversuch Datenauswertung""",
        generated_code_prefix="EXP.FCG_EVAL",
    )

    test_type = PropertyTypeAssignment(
        code="TEST_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TEST_PROGRAM_TYPE",
        property_label="Test Type",
        description="""Test Type//Art des Versuchs""",
        mandatory=False,
        show_in_edit_views=False,
        section="Experimental Details",
    )


# ! The parent class of Fcg is not defined (missing ObjectType)
class Fcg(ObjectType):
    defs = ObjectTypeDef(
        code="SPECIMEN.FCG",
        description="""Fatigue Crack Growth (FCG) Specimen//Ermüdungsrissfortschrittsprobe""",
        generated_code_prefix="SPEC.FCG",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    spec_status = PropertyTypeAssignment(
        code="SPEC_STATUS",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="SPECIMEN_STATUS",
        property_label="Specimen Status",
        description="""Specimen Status//Probenstatus""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    responsible_person = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Responsible person",
        description="""Responsible person//Verantwortliche Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    spec_fcg_type = PropertyTypeAssignment(
        code="SPEC_FCG_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="SPECIMEN_TYPE_FCG_TEST",
        property_label="Fatigue Crack Growth Specimen Type",
        description="""Fatigue Crack Growth Specimen Type//Ermüdungsrisswachstums-Probentyp""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Geometry (in accordance with ISO 12108)",
    )

    spec_fcg_width_side2 = PropertyTypeAssignment(
        code="SPEC_FCG_WIDTH_SIDE2",
        data_type="REAL",
        property_label="Width W [mm] (Side 2)",
        description="""Specimen Width W [mm] (Side 2)//Probenbreite W [mm] (Seite 2)""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Geometry (in accordance with ISO 12108)",
    )

    spec_fcg_width_side1 = PropertyTypeAssignment(
        code="SPEC_FCG_WIDTH_SIDE1",
        data_type="REAL",
        property_label="Width W [mm] (Side 1)",
        description="""Specimen Width W [mm] (Side 1)//Probenbreite W [mm] (Seite 1)""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Geometry (in accordance with ISO 12108)",
    )

    spec_fcg_thickness = PropertyTypeAssignment(
        code="SPEC_FCG_THICKNESS",
        data_type="REAL",
        property_label="Thickness B [mm]",
        description="""Specimen Thickness B [mm]//Probendicke B [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Geometry (in accordance with ISO 12108)",
    )

    spec_fcg_notchtype = PropertyTypeAssignment(
        code="SPEC_FCG_NOTCHTYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="NOTCH_TYPE_FCG",
        property_label="Notch Type",
        description="""Notch Type//Kerbtyp""",
        mandatory=True,
        show_in_edit_views=False,
        section="Notch Geometry",
    )

    spec_fcg_notchlength_side1 = PropertyTypeAssignment(
        code="SPEC_FCG_NOTCHLENGTH_SIDE1",
        data_type="REAL",
        property_label="Notch Length a_n [mm] (Side 1)",
        description="""Specimen Notch Length a_n [mm] (Side 1)//Kerbtiefe a_n [mm] (Seite 1)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Notch Geometry",
    )

    spec_fcg_notchlength_side2 = PropertyTypeAssignment(
        code="SPEC_FCG_NOTCHLENGTH_SIDE2",
        data_type="REAL",
        property_label="Notch Length a_n [mm] (Side 2)",
        description="""Specimen Notch Length a_n [mm] (Side 2)//Kerbtiefe a_n [mm] (Seite 2)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Notch Geometry",
    )

    spec_fcg_notchlength_middle = PropertyTypeAssignment(
        code="SPEC_FCG_NOTCHLENGTH_MIDDLE",
        data_type="REAL",
        property_label="Notch Length a_n [mm] (Middle, Chevron Notch only)",
        description="""Specimen Notch Length a_n [mm] (Middle, Chevron Notch only)//Kerbtiefe a_n [mm] (Mitte, nur Chevron-Kerbe)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Notch Geometry",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


# ! The parent class of Steel is not defined (missing ObjectType)
class Steel(ObjectType):
    defs = ObjectTypeDef(
        code="RAW_MATERIAL.STEEL",
        description="""Raw Material (Steel) as received from Supplier//Rohmaterial (Stahl) im Anlieferungszustand""",
        generated_code_prefix="RAW_MAT.STEEL",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative Name",
        description="""e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    mat_code = PropertyTypeAssignment(
        code="MAT_CODE",
        data_type="OBJECT",
        object_code="RAW_MATERIAL_CODE",
        property_label="Material Number",
        description="""Material Number//Werkstoffnummer""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    manufacturer = PropertyTypeAssignment(
        code="MANUFACTURER",
        data_type="VARCHAR",
        property_label="Manufacturer",
        description="""Manufacturer//Hersteller""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    supplier = PropertyTypeAssignment(
        code="SUPPLIER",
        data_type="VARCHAR",
        property_label="Supplier",
        description="""Supplier//Lieferant""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    raw_mat_batch_number = PropertyTypeAssignment(
        code="RAW_MAT_BATCH_NUMBER",
        data_type="VARCHAR",
        property_label="Raw Material Batch Number",
        description="""Raw Material Batch Number//Chargennummer des Rohmaterials""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    steel_treatment_first = PropertyTypeAssignment(
        code="STEEL_TREATMENT_FIRST",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="RAW_MAT_TREATMENT_STEEL",
        property_label="First Treatment",
        description="""First Treatment//Erste Behandlung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Delivery Condition",
    )

    steel_treatment_second = PropertyTypeAssignment(
        code="STEEL_TREATMENT_SECOND",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="RAW_MAT_TREATMENT_STEEL",
        property_label="Second Treatment",
        description="""Second Treatment//Zweite Behandlung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Delivery Condition",
    )

    steel_treatment_third = PropertyTypeAssignment(
        code="STEEL_TREATMENT_THIRD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="RAW_MAT_TREATMENT_STEEL",
        property_label="Third Treatment",
        description="""Third Treatment//Dritte Behandlung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Delivery Condition",
    )

    steel_treatment_fourth = PropertyTypeAssignment(
        code="STEEL_TREATMENT_FOURTH",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="RAW_MAT_TREATMENT_STEEL",
        property_label="Fourth Treatment",
        description="""Fourth Treatment//Vierte Behandlung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Delivery Condition",
    )

    raw_mat_form = PropertyTypeAssignment(
        code="RAW_MAT_FORM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="RAW_MAT_FORM",
        property_label="Raw Material Form",
        description="""Raw Material Form//Halbzeugart""",
        mandatory=False,
        show_in_edit_views=False,
        section="Geometry",
    )

    raw_mat_thickness = PropertyTypeAssignment(
        code="RAW_MAT_THICKNESS",
        data_type="REAL",
        property_label="(Wall) Thickness of Raw Material [mm]",
        description="""Thickness of Raw Material [mm]//Halbzeugdicke [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Geometry",
    )

    raw_mat_width = PropertyTypeAssignment(
        code="RAW_MAT_WIDTH",
        data_type="REAL",
        property_label="Width of Raw Material [mm]",
        description="""Width of Raw Material [mm]//Halbzeugbreite [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Geometry",
    )

    raw_mat_diameter = PropertyTypeAssignment(
        code="RAW_MAT_DIAMETER",
        data_type="REAL",
        property_label="Raw Material (outer) Diameter [mm]",
        description="""Raw Material (outer) Diameter [mm]//(Außen-)durchmesser des Halbzeugs [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Geometry",
    )

    raw_mat_length = PropertyTypeAssignment(
        code="RAW_MAT_LENGTH",
        data_type="REAL",
        property_label="Length of Raw Material [mm]",
        description="""Length of Raw Material [mm]//Halbzeuglänge [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Geometry",
    )

    raw_mat_component_description = PropertyTypeAssignment(
        code="RAW_MAT_COMPONENT_DESCRIPTION",
        data_type="VARCHAR",
        property_label="Description of Component",
        description="""Description of Component//Beschreibung der Komponente""",
        mandatory=False,
        show_in_edit_views=False,
        section="Geometry",
    )

    raw_mat_amount_in_stock = PropertyTypeAssignment(
        code="RAW_MAT_AMOUNT_IN_STOCK",
        data_type="INTEGER",
        property_label="Amount in Stock [Pieces]",
        description="""Amount in Stock [Pieces]//Anzahl auf Lager [Stück]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Stock",
    )

    rawmat_mech_prop_supplier_density = PropertyTypeAssignment(
        code="RAWMAT_MECH_PROP_SUPPLIER_DENSITY",
        data_type="REAL",
        property_label="Density [kg/m^3]",
        description="""Density [kg/m^3]//Dichte [kg/m^3]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_youngsmodulus = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_YOUNGSMODULUS",
        data_type="REAL",
        property_label="Young's Modulus [MPa]",
        description="""Young`s Modulus [MPa]//Elastizitätsmodul [MPa]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_upperyieldstrength_min = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_UPPERYIELDSTRENGTH_MIN",
        data_type="REAL",
        property_label="Minimum Upper Yield Strength R_eh [MPa]",
        description="""Minimum Upper Yield Strength R_eh [MPa] //Mindestwert Obere Streckgrenze R_eh [MPa]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_upperyieldstrength_max = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_UPPERYIELDSTRENGTH_MAX",
        data_type="REAL",
        property_label="Maximum Upper Yield Strength R_eh [MPa]",
        description="""Maximum Upper Yield Strength R_eh [MPa] //Höchsttwert Obere Streckgrenze R_eh [MPa]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_loweryieldstrength_min = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_LOWERYIELDSTRENGTH_MIN",
        data_type="REAL",
        property_label="Minimum Lower Yield Strength R_el [MPa]",
        description="""Minimum Lower Yield Strength R_el [MPa] //Mindestwert Untere Streckgrenze R_el [MPa]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_loweryieldstrength_max = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_LOWERYIELDSTRENGTH_MAX",
        data_type="REAL",
        property_label="Maximum Lower Yield Strength R_el [MPa]",
        description="""Maximum Lower Yield Strength R_el [MPa] //Höchstwert Untere Streckgrenze R_el [MPa]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_yieldlimit_min = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_YIELDLIMIT_MIN",
        data_type="REAL",
        property_label="Minimum Yield Limit R_p0,2 [MPa]",
        description="""Minimum Yield Limit R_p0,2 [MPa] //Mindestwert Dehngrenze R_p0,2 [MPa]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_yieldlimit_max = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_YIELDLIMIT_MAX",
        data_type="REAL",
        property_label="Maximum Yield Limit R_p0,2 [MPa]",
        description="""Maximum Yield Limit R_p0,2 [MPa] //Höchstwert Dehngrenze R_p0,2 [MPa]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_uts_min = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_UTS_MIN",
        data_type="REAL",
        property_label="Minimum Ultimate Tensile Strength R_m [MPa]",
        description="""Minimum Ultimate Tensile Strength R_m [MPa]//Mindestwert Zugfestigkeit R_m [MPa]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_uts_max = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_UTS_MAX",
        data_type="REAL",
        property_label="Maximum Ultimate Tensile Strength R_m [MPa]",
        description="""Maximum Ultimate Tensile Strength R_m [MPa]//Höchstwert Zugfestigkeit R_m [MPa]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_uniformelongation_min = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_UNIFORMELONGATION_MIN",
        data_type="REAL",
        property_label="Minimum Uniform Elongation A_g [%]",
        description="""Minimum Uniform Elongation A_g [%]//Mindestwert Gleichmaßdehnung A_g [%]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_uniformelongation_max = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_UNIFORMELONGATION_MAX",
        data_type="REAL",
        property_label="Maximum Uniform Elongation A_g [%]",
        description="""Maximum Uniform Elongation A_g [%]//Höchstwert Gleichmaßdehnung A_g [%]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_breakelongation_5_min = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_BREAKELONGATION_5_MIN",
        data_type="REAL",
        property_label="Minimum Elongation at Break A5 [%]",
        description="""Minimum Elongation at Break A5 [%]//Mindestwert Bruchdehnung A5 [%]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_breakelongation_5_max = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_BREAKELONGATION_5_MAX",
        data_type="REAL",
        property_label="Maximum Elongation at Break A5 [%]",
        description="""Maximum Elongation at Break A5  [%]//Höchstwert Bruchdehnung A5 [%]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_breakelongation_10_min = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_BREAKELONGATION_10_MIN",
        data_type="REAL",
        property_label="Minimum Elongation at Break A10 [%]",
        description="""Minimum Elongation at Break A10 [%]//Mindestwert Bruchdehnung A10 [%]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_breakelongation_10_max = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_BREAKELONGATION_10_MAX",
        data_type="REAL",
        property_label="Maximum Elongation at Break A10 [%]",
        description="""Maximum Elongation at Break A10 [%]//Höchstwert Bruchdehnung A10 [%]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


# ! The parent class of Aluminium is not defined (missing ObjectType)
class Aluminium(ObjectType):
    defs = ObjectTypeDef(
        code="RAW_MATERIAL.ALUMINIUM",
        description="""Raw Material (Aluminium Alloy) as received from Supplier//Rohmaterial (Aluminiumlegierung) im Anlieferungszustand""",
        generated_code_prefix="RAW_MAT.ALU",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative Name",
        description="""e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    mat_code = PropertyTypeAssignment(
        code="MAT_CODE",
        data_type="OBJECT",
        object_code="RAW_MATERIAL_CODE",
        property_label="Material Number",
        description="""Material Number//Werkstoffnummer""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    manufacturer = PropertyTypeAssignment(
        code="MANUFACTURER",
        data_type="VARCHAR",
        property_label="Manufacturer",
        description="""Manufacturer//Hersteller""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    supplier = PropertyTypeAssignment(
        code="SUPPLIER",
        data_type="VARCHAR",
        property_label="Supplier",
        description="""Supplier//Lieferant""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    raw_mat_batch_number = PropertyTypeAssignment(
        code="RAW_MAT_BATCH_NUMBER",
        data_type="VARCHAR",
        property_label="Raw Material Batch Number",
        description="""Raw Material Batch Number//Chargennummer des Rohmaterials""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    alu_treatment_first = PropertyTypeAssignment(
        code="ALU_TREATMENT_FIRST",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="RAW_MAT_TREATMENT_ALU",
        property_label="First Treatment",
        description="""First Treatment//Erste Behandlung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Delivery Condition",
    )

    alu_treatment_second = PropertyTypeAssignment(
        code="ALU_TREATMENT_SECOND",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="RAW_MAT_TREATMENT_ALU",
        property_label="Second Treatment",
        description="""Second Treatment//Zweite Behandlung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Delivery Condition",
    )

    alu_treatment_third = PropertyTypeAssignment(
        code="ALU_TREATMENT_THIRD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="RAW_MAT_TREATMENT_ALU",
        property_label="Third Treatment",
        description="""Third Treatment//Dritte Behandlung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Delivery Condition",
    )

    alu_treatment_fourth = PropertyTypeAssignment(
        code="ALU_TREATMENT_FOURTH",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="RAW_MAT_TREATMENT_ALU",
        property_label="Fourth Treatment",
        description="""Fourth Treatment//Vierte Behandlung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Delivery Condition",
    )

    raw_mat_form = PropertyTypeAssignment(
        code="RAW_MAT_FORM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="RAW_MAT_FORM",
        property_label="Raw Material Form",
        description="""Raw Material Form//Halbzeugart""",
        mandatory=False,
        show_in_edit_views=False,
        section="Geometry",
    )

    raw_mat_thickness = PropertyTypeAssignment(
        code="RAW_MAT_THICKNESS",
        data_type="REAL",
        property_label="(Wall) Thickness of Raw Material [mm]",
        description="""Thickness of Raw Material [mm]//Halbzeugdicke [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Geometry",
    )

    raw_mat_width = PropertyTypeAssignment(
        code="RAW_MAT_WIDTH",
        data_type="REAL",
        property_label="Width of Raw Material [mm]",
        description="""Width of Raw Material [mm]//Halbzeugbreite [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Geometry",
    )

    raw_mat_diameter = PropertyTypeAssignment(
        code="RAW_MAT_DIAMETER",
        data_type="REAL",
        property_label="Raw Material (outer) Diameter [mm]",
        description="""Raw Material (outer) Diameter [mm]//(Außen-)durchmesser des Halbzeugs [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Geometry",
    )

    raw_mat_length = PropertyTypeAssignment(
        code="RAW_MAT_LENGTH",
        data_type="REAL",
        property_label="Length of Raw Material [mm]",
        description="""Length of Raw Material [mm]//Halbzeuglänge [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Geometry",
    )

    raw_mat_component_description = PropertyTypeAssignment(
        code="RAW_MAT_COMPONENT_DESCRIPTION",
        data_type="VARCHAR",
        property_label="Description of Component",
        description="""Description of Component//Beschreibung der Komponente""",
        mandatory=False,
        show_in_edit_views=False,
        section="Geometry",
    )

    raw_mat_amount_in_stock = PropertyTypeAssignment(
        code="RAW_MAT_AMOUNT_IN_STOCK",
        data_type="INTEGER",
        property_label="Amount in Stock [Pieces]",
        description="""Amount in Stock [Pieces]//Anzahl auf Lager [Stück]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Stock",
    )

    rawmat_mech_prop_supplier_density = PropertyTypeAssignment(
        code="RAWMAT_MECH_PROP_SUPPLIER_DENSITY",
        data_type="REAL",
        property_label="Density [kg/m^3]",
        description="""Density [kg/m^3]//Dichte [kg/m^3]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_youngsmodulus = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_YOUNGSMODULUS",
        data_type="REAL",
        property_label="Young's Modulus [MPa]",
        description="""Young`s Modulus [MPa]//Elastizitätsmodul [MPa]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_upperyieldstrength_min = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_UPPERYIELDSTRENGTH_MIN",
        data_type="REAL",
        property_label="Minimum Upper Yield Strength R_eh [MPa]",
        description="""Minimum Upper Yield Strength R_eh [MPa] //Mindestwert Obere Streckgrenze R_eh [MPa]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_upperyieldstrength_max = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_UPPERYIELDSTRENGTH_MAX",
        data_type="REAL",
        property_label="Maximum Upper Yield Strength R_eh [MPa]",
        description="""Maximum Upper Yield Strength R_eh [MPa] //Höchsttwert Obere Streckgrenze R_eh [MPa]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_loweryieldstrength_min = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_LOWERYIELDSTRENGTH_MIN",
        data_type="REAL",
        property_label="Minimum Lower Yield Strength R_el [MPa]",
        description="""Minimum Lower Yield Strength R_el [MPa] //Mindestwert Untere Streckgrenze R_el [MPa]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_loweryieldstrength_max = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_LOWERYIELDSTRENGTH_MAX",
        data_type="REAL",
        property_label="Maximum Lower Yield Strength R_el [MPa]",
        description="""Maximum Lower Yield Strength R_el [MPa] //Höchstwert Untere Streckgrenze R_el [MPa]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_yieldlimit_min = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_YIELDLIMIT_MIN",
        data_type="REAL",
        property_label="Minimum Yield Limit R_p0,2 [MPa]",
        description="""Minimum Yield Limit R_p0,2 [MPa] //Mindestwert Dehngrenze R_p0,2 [MPa]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_yieldlimit_max = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_YIELDLIMIT_MAX",
        data_type="REAL",
        property_label="Maximum Yield Limit R_p0,2 [MPa]",
        description="""Maximum Yield Limit R_p0,2 [MPa] //Höchstwert Dehngrenze R_p0,2 [MPa]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_uts_min = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_UTS_MIN",
        data_type="REAL",
        property_label="Minimum Ultimate Tensile Strength R_m [MPa]",
        description="""Minimum Ultimate Tensile Strength R_m [MPa]//Mindestwert Zugfestigkeit R_m [MPa]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_uts_max = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_UTS_MAX",
        data_type="REAL",
        property_label="Maximum Ultimate Tensile Strength R_m [MPa]",
        description="""Maximum Ultimate Tensile Strength R_m [MPa]//Höchstwert Zugfestigkeit R_m [MPa]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_uniformelongation_min = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_UNIFORMELONGATION_MIN",
        data_type="REAL",
        property_label="Minimum Uniform Elongation A_g [%]",
        description="""Minimum Uniform Elongation A_g [%]//Mindestwert Gleichmaßdehnung A_g [%]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_uniformelongation_max = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_UNIFORMELONGATION_MAX",
        data_type="REAL",
        property_label="Maximum Uniform Elongation A_g [%]",
        description="""Maximum Uniform Elongation A_g [%]//Höchstwert Gleichmaßdehnung A_g [%]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_breakelongation_5_min = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_BREAKELONGATION_5_MIN",
        data_type="REAL",
        property_label="Minimum Elongation at Break A5 [%]",
        description="""Minimum Elongation at Break A5 [%]//Mindestwert Bruchdehnung A5 [%]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_breakelongation_5_max = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_BREAKELONGATION_5_MAX",
        data_type="REAL",
        property_label="Maximum Elongation at Break A5 [%]",
        description="""Maximum Elongation at Break A5  [%]//Höchstwert Bruchdehnung A5 [%]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_breakelongation_10_min = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_BREAKELONGATION_10_MIN",
        data_type="REAL",
        property_label="Minimum Elongation at Break A10 [%]",
        description="""Minimum Elongation at Break A10 [%]//Mindestwert Bruchdehnung A10 [%]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    rawmat_mechprop_supplier_breakelongation_10_max = PropertyTypeAssignment(
        code="RAWMAT_MECHPROP_SUPPLIER_BREAKELONGATION_10_MAX",
        data_type="REAL",
        property_label="Maximum Elongation at Break A10 [%]",
        description="""Maximum Elongation at Break A10 [%]//Höchstwert Bruchdehnung A10 [%]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Mechanical Properties at Room Temperature (as provided by Supplier)",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class HydraulicCylinder(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.HYDRAULIC_CYLINDER",
        description="""Hydraulic Cylinder//Hydraulikzylinder""",
        generated_code_prefix="INS.HYDR_CYL",
    )

    cylinder_type = PropertyTypeAssignment(
        code="CYLINDER_TYPE",
        data_type="VARCHAR",
        property_label="Hydraulic Cylinder Type",
        description="""Hydraulic Cylinder Type Code as specified by Manufacturer//Typenbezeichnung des Herstellers für den Hydraulikzylinder""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )

    max_static_force = PropertyTypeAssignment(
        code="MAX_STATIC_FORCE",
        data_type="REAL",
        property_label="Maximum Static Force [kN]",
        description="""Maximum Static Force in kN//Maximale statische Kraft [kN]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Technical Details",
    )

    max_dynamic_force = PropertyTypeAssignment(
        code="MAX_DYNAMIC_FORCE",
        data_type="REAL",
        property_label="Maximum Dynamic Force [kN]",
        description="""Maximum Dynamic Force in kN//Maximale dynamische Kraft [kN[""",
        mandatory=True,
        show_in_edit_views=False,
        section="Technical Details",
    )

    max_excitation_voltage = PropertyTypeAssignment(
        code="MAX_EXCITATION_VOLTAGE",
        data_type="REAL",
        property_label="Maximum Excitation Voltage [V]",
        description="""Maximum Excitation Voltage [V]//Maximale Speisespannung [V]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Technical Details",
    )

    calibration_interval = PropertyTypeAssignment(
        code="CALIBRATION_INTERVAL",
        data_type="INTEGER",
        property_label="Calibration Interval [Months]",
        description="""Calibration Interval [Months]//Kalibrierintervall [Monate]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Status",
    )


class HydraulicMisc(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.HYDRAULIC_MISC",
        description="""Miscellaneous Hydraulic Component""",
        generated_code_prefix="INS.HYDR_MISC",
    )

    misc_hyd_comp_type = PropertyTypeAssignment(
        code="MISC_HYD_COMP_TYPE",
        data_type="VARCHAR",
        property_label="Type Code as specified by Manufacturer",
        description="""Type Code as specified by Manufacturer//Typenbezeichnung des Herstellers""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )

    calibration_interval = PropertyTypeAssignment(
        code="CALIBRATION_INTERVAL",
        data_type="INTEGER",
        property_label="Calibration Interval [Months]",
        description="""Calibration Interval [Months]//Kalibrierintervall [Monate]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Status",
    )


class Servovalve(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.SERVOVALVE",
        description="""Servovalve for servohydraulic testing machines//Servoventil für servohydraulische Prüfmaschinen""",
        generated_code_prefix="INS.HYDR_SVALV",
    )

    valve_type_id = PropertyTypeAssignment(
        code="VALVE_TYPE_ID",
        data_type="VARCHAR",
        property_label="Type",
        description="""Valve Type Code as specified by Manufacturer//Typenbezeichnung des Herstellers für das Servoventil""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )

    valve_model_id = PropertyTypeAssignment(
        code="VALVE_MODEL_ID",
        data_type="VARCHAR",
        property_label="Model",
        description="""Valve Model Code as specified by Manufacturer//Modellbezeichnung des Herstellers für das Servoventil""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )

    rated_flow = PropertyTypeAssignment(
        code="RATED_FLOW",
        data_type="REAL",
        property_label="Rated Flow [l/min]",
        description="""Rated flow [l/min]//Nenndurchfluss [l/min]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Technical Details",
    )

    max_pressure = PropertyTypeAssignment(
        code="MAX_PRESSURE",
        data_type="REAL",
        property_label="Maximum Operating Pressure [bar]",
        description="""Maximum Operating Pressure [bar]//Maximaler Betriebsdruck [bar]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Technical Details",
    )

    rated_power = PropertyTypeAssignment(
        code="RATED_POWER",
        data_type="REAL",
        property_label="Rated Power [kW]",
        description="""Rated power [kW]//Nennleistung [kW]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Technical Details",
    )

    calibration_interval = PropertyTypeAssignment(
        code="CALIBRATION_INTERVAL",
        data_type="INTEGER",
        property_label="Calibration Interval [Months]",
        description="""Calibration Interval [Months]//Kalibrierintervall [Monate]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Status",
    )


class LoadFrame(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.LOAD_FRAME",
        description="""Load Frame of Testing Machine//Lastrahmen für Prüfmaschinen""",
        generated_code_prefix="INS.LOAD_FRAME",
    )

    load_frame_type = PropertyTypeAssignment(
        code="LOAD_FRAME_TYPE",
        data_type="VARCHAR",
        property_label="Load Frame Type Code as specified by Manufacturer",
        description="""Load Frame Type Code as specified by Manufacturer//Typenbezeichnung des Herstellers für den Lastrahmen""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )

    max_static_force = PropertyTypeAssignment(
        code="MAX_STATIC_FORCE",
        data_type="REAL",
        property_label="Maximum Static Force [kN]",
        description="""Maximum Static Force in kN//Maximale statische Kraft [kN]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )

    max_dynamic_force = PropertyTypeAssignment(
        code="MAX_DYNAMIC_FORCE",
        data_type="REAL",
        property_label="Maximum Dynamic Force [kN]",
        description="""Maximum Dynamic Force in kN//Maximale dynamische Kraft [kN[""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )

    load_frame_orientation = PropertyTypeAssignment(
        code="LOAD_FRAME_ORIENTATION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="LOAD_FRAME_ORIENTATION",
        property_label="Load Frame Orientation",
        description="""Load Frame Orientation//Orientierung des Lastrahmens""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )

    max_space_vert = PropertyTypeAssignment(
        code="MAX_SPACE_VERT",
        data_type="REAL",
        property_label="Maximum vertical space for Specimens and Grips [mm]",
        description="""Maximum vertical space for Specimens and Grips [mm]//Maximaler vertikaler Bauraum für Proben und Probenhalter [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )

    max_space_hor = PropertyTypeAssignment(
        code="MAX_SPACE_HOR",
        data_type="REAL",
        property_label="Maximum horizontal space between Columns [mm]",
        description="""Maximum horizontal space between Columns [mm]//Maximaler horizontaler Bauraum zwischen den Säulen [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )


class AlignmentFixture(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.ALIGNMENT_FIXTURE",
        description="""Alignment Fixture for Testing Machine//Ausrichtvorrichtung für Prüfmaschinen""",
        generated_code_prefix="INS.ALGN_FIX",
    )

    max_static_force = PropertyTypeAssignment(
        code="MAX_STATIC_FORCE",
        data_type="REAL",
        property_label="Maximum Static Force [kN]",
        description="""Maximum Static Force in kN//Maximale statische Kraft [kN]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )

    max_dynamic_force = PropertyTypeAssignment(
        code="MAX_DYNAMIC_FORCE",
        data_type="REAL",
        property_label="Maximum Dynamic Force [kN]",
        description="""Maximum Dynamic Force in kN//Maximale dynamische Kraft [kN[""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )


class Thermocouple(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.THERMOCOUPLE",
        description="""Thermocouple//Thermoelement""",
        generated_code_prefix="INS.TC",
    )

    tc_type = PropertyTypeAssignment(
        code="TC_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="THERMOCOUPLE_TYPE",
        property_label="Thermocouple Type",
        description="""Thermocouple Type//Thermoelement Typ""",
        mandatory=True,
        show_in_edit_views=False,
        section="Technical Details",
    )

    tc_min_temp = PropertyTypeAssignment(
        code="TC_MIN_TEMP",
        data_type="REAL",
        property_label="Minimum Operating Temperature [°C]",
        description="""Minimum Operating Temperature [°C]//Minimale Betriebstemperatur [°C]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )

    tc_max_temp = PropertyTypeAssignment(
        code="TC_MAX_TEMP",
        data_type="REAL",
        property_label="Maximum Operating Temperature [°C]",
        description="""Maximum Operating Temperature [°C]//Maximale Betriebstemperatur [°C]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )

    tc_diameter = PropertyTypeAssignment(
        code="TC_DIAMETER",
        data_type="REAL",
        property_label="Diameter [mm]",
        description="""Diameter [mm]//Durchmesser [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )

    tc_cable_length = PropertyTypeAssignment(
        code="TC_CABLE_LENGTH",
        data_type="REAL",
        property_label="Cable Length [mm]",
        description="""Cable Length [mm]//Kabellänge [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )

    tc_connector = PropertyTypeAssignment(
        code="TC_CONNECTOR",
        data_type="BOOLEAN",
        property_label="Connector",
        description="""Connector//Stecker""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )


class Rtd(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.RTD",
        description="""Resistance Temperature Detector (RTD)//Widerstandsthermometer""",
        generated_code_prefix="INS.RTD",
    )

    rtd_type = PropertyTypeAssignment(
        code="RTD_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="RTD_TYPE",
        property_label="RTD Type",
        description="""RTD Type//Widerstandsthermometer Typ""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )

    rtd_min_temp = PropertyTypeAssignment(
        code="RTD_MIN_TEMP",
        data_type="REAL",
        property_label="Minimum Operating Temperature [°C]",
        description="""Minimum Operating Temperature [°C]//Minimale Betriebstemperatur [°C]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )

    rtd_max_temp = PropertyTypeAssignment(
        code="RTD_MAX_TEMP",
        data_type="REAL",
        property_label="Maximum Operating Temperature [°C]",
        description="""Maximum Operating Temperature [°C]//Maximale Betriebstemperatur [°C]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )

    rtd_accuracy_class = PropertyTypeAssignment(
        code="RTD_ACCURACY_CLASS",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="RTD_ACCURACY_CLASS",
        property_label="RTD Accuracy Class",
        description="""RTD Accuracy Class//Widerstandsthermometer Genauigkeitsklasse""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )

    rtd_insulation_material = PropertyTypeAssignment(
        code="RTD_INSULATION_MATERIAL",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="RTD_INSULATION_MATERIAL",
        property_label="RTD Insulation Material",
        description="""RTD Insulation Material//Widerstandsthermometer Isolationsmaterial""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )

    rtd_cover_tube_diameter = PropertyTypeAssignment(
        code="RTD_COVER_TUBE_DIAMETER",
        data_type="REAL",
        property_label="RTD Cover Tube Diameter [mm]",
        description="""RTD Cover Tube Diameter [mm]//Widerstandsthermometer Schutzhülsendurchmesser [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )

    rtd_cover_tube_length = PropertyTypeAssignment(
        code="RTD_COVER_TUBE_LENGTH",
        data_type="REAL",
        property_label="RTD Cover Tube Length [mm]",
        description="""RTD Cover Tube Length [mm]//Widerstandsthermometer Schutzhülsenlänge [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )

    rtd_cable_length = PropertyTypeAssignment(
        code="RTD_CABLE_LENGTH",
        data_type="REAL",
        property_label="RTD Cable Length [mm]",
        description="""RTD Cable Length [mm]//Widerstandsthermometer Kabellänge [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )

    rtd_connection = PropertyTypeAssignment(
        code="RTD_CONNECTION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="RTD_CONNECTION_TYPE",
        property_label="RTD Connection",
        description="""RTD Connection//Widerstandsthermometer Anschlussart""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )


class Nanovoltmeter(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.NANOVOLTMETER",
        description="""Nanovoltmeter//Nanovoltmeter""",
        generated_code_prefix="INS.NANOVM",
    )

    number_of_channels = PropertyTypeAssignment(
        code="NUMBER_OF_CHANNELS",
        data_type="INTEGER",
        property_label="Number of Channels",
        description="""Number of Channels//Anzahl der Kanäle""",
        mandatory=False,
        show_in_edit_views=False,
        section="Inputs",
    )

    minrange = PropertyTypeAssignment(
        code="MINRANGE",
        data_type="REAL",
        property_label="Minimum Range [V]",
        description="""Minimum Range [V]//Kleinster Messbereich [V]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Inputs",
    )

    minrange_resolution = PropertyTypeAssignment(
        code="MINRANGE_RESOLUTION",
        data_type="REAL",
        property_label="Resolution at minimum Range [nV]",
        description="""Resolution at minimum Range [nV]//Auflösung im kleinsten Messbereich [nV]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Inputs",
    )

    maxrange = PropertyTypeAssignment(
        code="MAXRANGE",
        data_type="REAL",
        property_label="Maximum Range [V]",
        description="""Maximum Range [V]//Größter Messbereich [V]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Inputs",
    )

    maxrange_resolution = PropertyTypeAssignment(
        code="MAXRANGE_RESOLUTION",
        data_type="REAL",
        property_label="Resolution at maximum Range [nV]",
        description="""Resolution at maximum Range [nV]//Auflösung im größten Messbereich [nV]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Inputs",
    )

    number_of_analog_outputs = PropertyTypeAssignment(
        code="NUMBER_OF_ANALOG_OUTPUTS",
        data_type="INTEGER",
        property_label="Number of Analog Outputs",
        description="""Number of Analog Outputs//Anzahl Analoger Ausgänge""",
        mandatory=False,
        show_in_edit_views=False,
        section="Outputs",
    )

    analog_output_voltage_min = PropertyTypeAssignment(
        code="ANALOG_OUTPUT_VOLTAGE_MIN",
        data_type="REAL",
        property_label="Analog Output Minimum Voltage [V]",
        description="""Analog Output Minimum Voltage [V]//Minimale Spannung am Analogen Ausgang [V]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Outputs",
    )

    analog_output_voltage_max = PropertyTypeAssignment(
        code="ANALOG_OUTPUT_VOLTAGE_MAX",
        data_type="REAL",
        property_label="Analog Output Maximum Voltage [V]",
        description="""Analog Output Maximum Voltage [V]//Maximale Spannung am Analogen Ausgang [V]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Outputs",
    )

    gpib = PropertyTypeAssignment(
        code="GPIB",
        data_type="BOOLEAN",
        property_label="GPIB Interface",
        description="""GPIB Interface//GPIB Schnittstelle""",
        mandatory=False,
        show_in_edit_views=False,
        section="Command Interfaces",
    )

    rs232 = PropertyTypeAssignment(
        code="RS232",
        data_type="BOOLEAN",
        property_label="RS232 Interface",
        description="""RS232 Interface//RS232 Schnittstelle""",
        mandatory=False,
        show_in_edit_views=False,
        section="Command Interfaces",
    )

    ethernet = PropertyTypeAssignment(
        code="ETHERNET",
        data_type="BOOLEAN",
        property_label="Ethernet Interface",
        description="""Ethernet Interface//Ethernet Schnittstelle""",
        mandatory=False,
        show_in_edit_views=False,
        section="Command Interfaces",
    )

    usb = PropertyTypeAssignment(
        code="USB",
        data_type="BOOLEAN",
        property_label="USB Interface",
        description="""USB Interface//USB Schnittstelle""",
        mandatory=False,
        show_in_edit_views=False,
        section="Command Interfaces",
    )


class PowerSupply(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.POWER_SUPPLY",
        description="""Power Supply//Labornetzgerät""",
        generated_code_prefix="INS.POWR_SPPLY",
    )

    number_of_outputs = PropertyTypeAssignment(
        code="NUMBER_OF_OUTPUTS",
        data_type="INTEGER",
        property_label="Number of Outputs",
        description="""Number of Outputs//Anzahl der Ausgänge""",
        mandatory=False,
        show_in_edit_views=False,
        section="Outputs",
    )

    max_output_voltage = PropertyTypeAssignment(
        code="MAX_OUTPUT_VOLTAGE",
        data_type="REAL",
        property_label="Maximum Output Voltage [V]",
        description="""Maximum Output Voltage [V]//Maximale Ausgangsspannung [V]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Outputs",
    )

    max_output_current = PropertyTypeAssignment(
        code="MAX_OUTPUT_CURRENT",
        data_type="REAL",
        property_label="Maximum Output Current [A]",
        description="""Maximum Output Current [A]//Maximaler Ausgangsstrom [A]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Outputs",
    )

    gpib = PropertyTypeAssignment(
        code="GPIB",
        data_type="BOOLEAN",
        property_label="GPIB Interface",
        description="""GPIB Interface//GPIB Schnittstelle""",
        mandatory=False,
        show_in_edit_views=False,
        section="Command Interfaces",
    )

    rs232 = PropertyTypeAssignment(
        code="RS232",
        data_type="BOOLEAN",
        property_label="RS232 Interface",
        description="""RS232 Interface//RS232 Schnittstelle""",
        mandatory=False,
        show_in_edit_views=False,
        section="Command Interfaces",
    )

    ethernet = PropertyTypeAssignment(
        code="ETHERNET",
        data_type="BOOLEAN",
        property_label="Ethernet Interface",
        description="""Ethernet Interface//Ethernet Schnittstelle""",
        mandatory=False,
        show_in_edit_views=False,
        section="Command Interfaces",
    )

    usb = PropertyTypeAssignment(
        code="USB",
        data_type="BOOLEAN",
        property_label="USB Interface",
        description="""USB Interface//USB Schnittstelle""",
        mandatory=False,
        show_in_edit_views=False,
        section="Command Interfaces",
    )


# ! The parent class of Test is not defined (missing ObjectType)
class Test(ObjectType):
    defs = ObjectTypeDef(
        code="SETUP.TEST",
        description="""This Object type is used to correlate the components of a test setup with a time period//Dieser Objekttyp dient der Verknüpfung der Komponenten eines Testsetups mit einer Zeitspanne""",
        generated_code_prefix="SETUP.TESTING_MACHINE",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    show_in_project_overview = PropertyTypeAssignment(
        code="$SHOW_IN_PROJECT_OVERVIEW",
        data_type="BOOLEAN",
        property_label="Show in project overview",
        description="""Show in project overview page""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    test_setup_type = PropertyTypeAssignment(
        code="TEST_SETUP_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TEST_SETUP_TYPE",
        property_label="Test Setup Type",
        description="""Test Setup Type//Test Setup Typ""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    start_date = PropertyTypeAssignment(
        code="START_DATE",
        data_type="TIMESTAMP",
        property_label="Start date",
        description="""Start date//Startdatum""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    end_date = PropertyTypeAssignment(
        code="END_DATE",
        data_type="TIMESTAMP",
        property_label="End date",
        description="""End date//Enddatum""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class MeasuringAmplifier(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.MEASURING_AMPLIFIER",
        description="""Measuring Amplifier//Messverstärker""",
        generated_code_prefix="INS.MEAS_AMP",
    )

    bandwidth = PropertyTypeAssignment(
        code="BANDWIDTH",
        data_type="REAL",
        property_label="Bandwidth [Hz]",
        description="""Bandwidth [Hz]//Bandbreite [Hz]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )

    accuracy_class_vde0410 = PropertyTypeAssignment(
        code="ACCURACY_CLASS_VDE0410",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="ACCURACY_CLASS_VDE0410",
        property_label="Accuracy Class according to VDE 0410",
        description="""Accuracy Class according to VDE 0410//Genauigkeitsklasse anch VDE 0410""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )

    number_of_inputs = PropertyTypeAssignment(
        code="NUMBER_OF_INPUTS",
        data_type="INTEGER",
        property_label="Number of Inputs",
        description="""Number of Inputs//Anzahl der Eingänge""",
        mandatory=False,
        show_in_edit_views=False,
        section="Inputs",
    )

    min_excitation_voltage = PropertyTypeAssignment(
        code="MIN_EXCITATION_VOLTAGE",
        data_type="REAL",
        property_label="Minimum Excitation Voltage [V]",
        description="""Minimum Excitation Voltage [V]//Minimale Speisespannung [V]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Inputs",
    )

    max_excitation_voltage = PropertyTypeAssignment(
        code="MAX_EXCITATION_VOLTAGE",
        data_type="REAL",
        property_label="Maximum Excitation Voltage [V]",
        description="""Maximum Excitation Voltage [V]//Maximale Speisespannung [V]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Inputs",
    )

    max_common_mode_voltage = PropertyTypeAssignment(
        code="MAX_COMMON_MODE_VOLTAGE",
        data_type="REAL",
        property_label="Maximum Common Mode Voltage [V]",
        description="""Maximum Common Mode Voltage [V]//Maximale Gleichtaktspannung [V]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Inputs",
    )

    number_of_analog_outputs = PropertyTypeAssignment(
        code="NUMBER_OF_ANALOG_OUTPUTS",
        data_type="INTEGER",
        property_label="Number of Analog Outputs",
        description="""Number of Analog Outputs//Anzahl Analoger Ausgänge""",
        mandatory=False,
        show_in_edit_views=False,
        section="Outputs",
    )

    analog_output_voltage_min = PropertyTypeAssignment(
        code="ANALOG_OUTPUT_VOLTAGE_MIN",
        data_type="REAL",
        property_label="Analog Output Minimum Voltage [V]",
        description="""Analog Output Minimum Voltage [V]//Minimale Spannung am Analogen Ausgang [V]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Outputs",
    )

    analog_output_voltage_max = PropertyTypeAssignment(
        code="ANALOG_OUTPUT_VOLTAGE_MAX",
        data_type="REAL",
        property_label="Analog Output Maximum Voltage [V]",
        description="""Analog Output Maximum Voltage [V]//Maximale Spannung am Analogen Ausgang [V]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Outputs",
    )

    gpib = PropertyTypeAssignment(
        code="GPIB",
        data_type="BOOLEAN",
        property_label="GPIB Interface",
        description="""GPIB Interface//GPIB Schnittstelle""",
        mandatory=False,
        show_in_edit_views=False,
        section="Command Interfaces",
    )

    rs232 = PropertyTypeAssignment(
        code="RS232",
        data_type="BOOLEAN",
        property_label="RS232 Interface",
        description="""RS232 Interface//RS232 Schnittstelle""",
        mandatory=False,
        show_in_edit_views=False,
        section="Command Interfaces",
    )

    ethernet = PropertyTypeAssignment(
        code="ETHERNET",
        data_type="BOOLEAN",
        property_label="Ethernet Interface",
        description="""Ethernet Interface//Ethernet Schnittstelle""",
        mandatory=False,
        show_in_edit_views=False,
        section="Command Interfaces",
    )

    usb = PropertyTypeAssignment(
        code="USB",
        data_type="BOOLEAN",
        property_label="USB Interface",
        description="""USB Interface//USB Schnittstelle""",
        mandatory=False,
        show_in_edit_views=False,
        section="Command Interfaces",
    )

    calibration_interval = PropertyTypeAssignment(
        code="CALIBRATION_INTERVAL",
        data_type="INTEGER",
        property_label="Calibration Interval [Months]",
        description="""Calibration Interval [Months]//Kalibrierintervall [Monate]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Status",
    )


class ImageSeries(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.IMAGE_SERIES",
        description="""A series of one or more still image recordings//Eine Serie aus einer oder mehrerer Einzelbildaufnahmen""",
        generated_code_prefix="EXP.IMG_SRS",
    )

    uuid = PropertyTypeAssignment(
        code="UUID",
        data_type="VARCHAR",
        property_label="UUID",
        description="""A Universally Unique IDentifier (UUID/GUID) according to RFC 4122//Ein Universally Unique IDentifier (UUID/GUID) nach RFC 4122""",
        mandatory=False,
        show_in_edit_views=False,
        section="Identifiers",
    )

    image_horizontal_resolution = PropertyTypeAssignment(
        code="IMAGE_HORIZONTAL_RESOLUTION",
        data_type="INTEGER",
        property_label="Horizontal resolution [pixel]",
        description="""Horizontal resolution of the image [pixel]//Horizonzale Auflösung des Bildes [Pixel]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Image Series Information",
    )

    image_vertical_resolution = PropertyTypeAssignment(
        code="IMAGE_VERTICAL_RESOLUTION",
        data_type="INTEGER",
        property_label="Vertical resolution [pixel]",
        description="""Vertical resolution of the image [pixel]////Vertikale Auflösung des Bildes [Pixel]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Image Series Information",
    )

    image_series_count = PropertyTypeAssignment(
        code="IMAGE_SERIES_COUNT",
        data_type="INTEGER",
        property_label="Number of images recorded",
        description="""Number of images recorded//Anzahl der aufgenommenen Bilder""",
        mandatory=False,
        show_in_edit_views=False,
        section="Image Series Information",
    )


class ProfileScan(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.PROFILE_SCAN",
        description="""A series of 2D line sensor readings//Eine Reihe von 2D Profillinienaufnahmen""",
        generated_code_prefix="EXP.LINE_SCAN",
    )

    uuid = PropertyTypeAssignment(
        code="UUID",
        data_type="VARCHAR",
        property_label="UUID",
        description="""A Universally Unique IDentifier (UUID/GUID) according to RFC 4122//Ein Universally Unique IDentifier (UUID/GUID) nach RFC 4122""",
        mandatory=False,
        show_in_edit_views=False,
        section="Identifiers",
    )

    scan_line_count = PropertyTypeAssignment(
        code="SCAN_LINE_COUNT",
        data_type="INTEGER",
        property_label="Scan line count",
        description="""Number of individual scan lines recorded//Anzahl der aufgenommenen Scanlinien""",
        mandatory=False,
        show_in_edit_views=False,
        section="Scan Information",
    )

    scan_line_resolution = PropertyTypeAssignment(
        code="SCAN_LINE_RESOLUTION",
        data_type="INTEGER",
        property_label="Scan line resolution [pixel]",
        description="""Number of pixels recorded for each scan line//Anzahl der Messpunkt einer Scanlinie""",
        mandatory=False,
        show_in_edit_views=False,
        section="Scan Information",
    )


class VideoRecording(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.VIDEO_RECORDING",
        description="""An experimental step describing a video recording//Ein experimenteller Schritt zur Erzeugung einer Videoaufnahme""",
        generated_code_prefix="EXP.VID",
    )

    uuid = PropertyTypeAssignment(
        code="UUID",
        data_type="VARCHAR",
        property_label="UUID",
        description="""A Universally Unique IDentifier (UUID/GUID) according to RFC 4122//Ein Universally Unique IDentifier (UUID/GUID) nach RFC 4122""",
        mandatory=False,
        show_in_edit_views=False,
        section="Identifiers",
    )

    image_horizontal_resolution = PropertyTypeAssignment(
        code="IMAGE_HORIZONTAL_RESOLUTION",
        data_type="INTEGER",
        property_label="Horizontal resolution [pixel]",
        description="""Horizontal resolution of the image [pixel]//Horizonzale Auflösung des Bildes [Pixel]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Video Information",
    )

    image_vertical_resolution = PropertyTypeAssignment(
        code="IMAGE_VERTICAL_RESOLUTION",
        data_type="INTEGER",
        property_label="Vertical resolution [pixel]",
        description="""Vertical resolution of the image [pixel]////Vertikale Auflösung des Bildes [Pixel]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Video Information",
    )

    video_frame_per_seconds = PropertyTypeAssignment(
        code="VIDEO_FRAME_PER_SECONDS",
        data_type="INTEGER",
        property_label="Average video framerate [frames per second]",
        description="""Average video framerate [frames per second]//Mittlere Bildrate (in Bilder pro Sekunde)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Video Information",
    )

    video_codec = PropertyTypeAssignment(
        code="VIDEO_CODEC",
        data_type="VARCHAR",
        property_label="Video codec used during recording",
        description="""Video codec used during recording (if applicable)//Videocodec (sofern kodiert)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Video Information",
    )

    video_dynamic_framerate = PropertyTypeAssignment(
        code="VIDEO_DYNAMIC_FRAMERATE",
        data_type="BOOLEAN",
        property_label="Dynamic video frame rate",
        description="""Flag to indicate that the video frame rate varies over time//Gibt an, dass die Bildrate des Videos nicht konstant ist""",
        mandatory=False,
        show_in_edit_views=False,
        section="Video Information",
    )

    camera_shutter_mode = PropertyTypeAssignment(
        code="CAMERA_SHUTTER_MODE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="CAMERA_SHUTTER_MODE",
        property_label="Shutter mode",
        description="""The shutter mode used for video recording//Belichtungsprinzip des Bildsensors""",
        mandatory=False,
        show_in_edit_views=False,
        section="Video Information",
    )


class Weldment(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.WELDMENT",
        description="""An experimental step describing a welding experiment//Ein experimenteller Schritt der einen Schweißvorgang beschreibt""",
        generated_code_prefix="EXP.WLD",
    )

    uuid = PropertyTypeAssignment(
        code="UUID",
        data_type="VARCHAR",
        property_label="UUID",
        description="""A Universally Unique IDentifier (UUID/GUID) according to RFC 4122//Ein Universally Unique IDentifier (UUID/GUID) nach RFC 4122""",
        mandatory=False,
        show_in_edit_views=False,
        section="Identifiers",
    )

    experimental_step_weldment_type = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="WELDING.WELD_TYPE",
        property_label="Type of weld",
        description="""Type of weldment made//Art der Schweißverbindung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Weldment Information",
    )


# ! The parent class of Welding is not defined (missing ObjectType)
class Welding(ObjectType):
    defs = ObjectTypeDef(
        code="CONSUMABLE.WELDING",
        description="""Generic welding consumable//Generisches Verbrauchsmaterial für Schweißen""",
        generated_code_prefix="CONS.WLD",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative Name",
        description="""e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    manufacturer = PropertyTypeAssignment(
        code="MANUFACTURER",
        data_type="VARCHAR",
        property_label="Manufacturer",
        description="""Manufacturer//Hersteller""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    supplier = PropertyTypeAssignment(
        code="SUPPLIER",
        data_type="VARCHAR",
        property_label="Supplier",
        description="""Supplier//Lieferant""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    batch_number = PropertyTypeAssignment(
        code="BATCH_NUMBER",
        data_type="VARCHAR",
        property_label="Batch number",
        description="""Batch number//Chargennummer""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    inventory_no = PropertyTypeAssignment(
        code="INVENTORY_NO",
        data_type="INTEGER",
        property_label="Inventory Number",
        description="""PARFIS inventory number (8-digit)//PARFIS Inventarnummer (8-stellig)""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    inventory_no_add = PropertyTypeAssignment(
        code="INVENTORY_NO_ADD",
        data_type="INTEGER",
        property_label="Inventory Number Addition",
        description="""PARFIS inventory number (8-digit)//PARFIS Inventarnummer (8-stellig)""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_oe = PropertyTypeAssignment(
        code="BAM_OE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_OE",
        property_label="BAM Organizational Entity",
        description="""BAM Organizational Entity//BAM Organisationseinheit (OE)""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    responsible_person = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Responsible person",
        description="""Responsible person//Verantwortliche Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    co_responsible_person = PropertyTypeAssignment(
        code="CO_RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Co-responsible person",
        description="""Co-responsible person//Weitere verantwortliche Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    last_systemcheck = PropertyTypeAssignment(
        code="LAST_SYSTEMCHECK",
        data_type="DATE",
        property_label="Last System Check",
        description="""Date of the last system check//Datum des letzten Systemchecks""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


class Camera(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.CAMERA",
        description="""A generic camera  device for recording video or photos//Eine generische Kamera für Video- oder Fotoaufnahmen""",
        generated_code_prefix="INS.CAM",
    )

    image_sensor_name = PropertyTypeAssignment(
        code="IMAGE_SENSOR_NAME",
        data_type="VARCHAR",
        property_label="Sensor",
        description="""Name of the image sensor model//Modellbezeichnung des Bildsensors""",
        mandatory=False,
        show_in_edit_views=False,
        section="Camera Information",
    )

    image_sensor_size = PropertyTypeAssignment(
        code="IMAGE_SENSOR_SIZE",
        data_type="VARCHAR",
        property_label="Sensor size",
        description="""Size of the image sensor//Größenangabe des Bildsensors""",
        mandatory=False,
        show_in_edit_views=False,
        section="Camera Information",
    )

    image_sensor_resolution_horizontal = PropertyTypeAssignment(
        code="IMAGE_SENSOR_RESOLUTION_HORIZONTAL",
        data_type="INTEGER",
        property_label="Horizontal sensor resolution [pixel]",
        description="""Horizontal camera resolution in pixel//Horizontale Auflösung des Sensors""",
        mandatory=True,
        show_in_edit_views=False,
        section="Camera Information",
    )

    image_sensor_resolution_vertical = PropertyTypeAssignment(
        code="IMAGE_SENSOR_RESOLUTION_VERTICAL",
        data_type="INTEGER",
        property_label="Vertical camera resolution [pixel]",
        description="""Vertical camera resolution in pixel//Vertikale Sensorauflösung in pixel""",
        mandatory=True,
        show_in_edit_views=False,
        section="Camera Information",
    )

    image_sensor_framerate = PropertyTypeAssignment(
        code="IMAGE_SENSOR_FRAMERATE",
        data_type="REAL",
        property_label="Framerate (at max. resolution)",
        description="""Highest framerate at indicated maximum resolution//Höchste erreichbare Bildrate bei voller Auflösung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Camera Information",
    )

    lens_mount_type = PropertyTypeAssignment(
        code="LENS_MOUNT_TYPE",
        data_type="VARCHAR",
        property_label="Lens mount",
        description="""The lens mount of a camera or lens//Art des Objektivanschluss""",
        mandatory=False,
        show_in_edit_views=False,
        section="Camera Information",
    )

    firmware_version = PropertyTypeAssignment(
        code="FIRMWARE_VERSION",
        data_type="VARCHAR",
        property_label="Current firmware version",
        description="""The currently installed firmware version//Die aktuell installierte Firmware-Version""",
        mandatory=False,
        show_in_edit_views=False,
        section="Software Information",
    )

    last_systemcheck = PropertyTypeAssignment(
        code="LAST_SYSTEMCHECK",
        data_type="DATE",
        property_label="Last System Check",
        description="""Date of the last system check//Datum des letzten Systemchecks""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )


class LaserLineScanner(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.LASER_LINE_SCANNER",
        description="""A laser scanner used to measure 2D profiles along a laser line//Laserlinienscanner""",
        generated_code_prefix="INS.LAS_LINE_SCAN",
    )

    instrument_laser_scanner_z_min = PropertyTypeAssignment(
        code="INSTRUMENT.LASER_SCANNER.Z_MIN",
        data_type="REAL",
        property_label="Minimum z distance [mm]",
        description="""Minimal measuring distance in z-Direction//Minimaler Messabstand in z-Richtung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Laser Sensor Information",
    )

    instrument_laser_scanner_z_max = PropertyTypeAssignment(
        code="INSTRUMENT.LASER_SCANNER.Z_MAX",
        data_type="REAL",
        property_label="Maximum z distance [mm]",
        description="""Maximum measuring distance in z-Direction//Maximaler Messabstand in z-Richtung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Laser Sensor Information",
    )

    instrument_laser_scanner_x_min = PropertyTypeAssignment(
        code="INSTRUMENT.LASER_SCANNER.X_MIN",
        data_type="REAL",
        property_label="Minimum x measuring range [mm]",
        description="""Minimal measuring distance in z-Direction//Minimaler Messabstand in z-Richtung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Laser Sensor Information",
    )

    instrument_laser_scanner_x_max = PropertyTypeAssignment(
        code="INSTRUMENT.LASER_SCANNER.X_MAX",
        data_type="REAL",
        property_label="Maximum x measuring range [mm]",
        description="""Maximum measuring distance in z-Direction//Maximaler Messabstand in z-Richtung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Laser Sensor Information",
    )

    instrument_laser_scanner_line_resolution = PropertyTypeAssignment(
        code="INSTRUMENT.LASER_SCANNER.LINE_RESOLUTION",
        data_type="INTEGER",
        property_label="Maximum line resolution [pixel]",
        description="""Maximum resolution per laser line//Maximale Anzahl Messpunkte per Linienmessung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Laser Sensor Information",
    )

    laser_wavelength = PropertyTypeAssignment(
        code="LASER_WAVELENGTH",
        data_type="VARCHAR",
        property_label="Laser wavelength [nm]",
        description="""Wavelength of emitted laser light//Wellenlänge des Laserlichts""",
        mandatory=False,
        show_in_edit_views=False,
        section="Laser Sensor Information",
    )

    laser_class = PropertyTypeAssignment(
        code="LASER_CLASS",
        data_type="VARCHAR",
        property_label="Laser class",
        description="""Laser class rating according to DIN EN 60825-1//Laserklasse nach DIN EN 60825-1""",
        mandatory=False,
        show_in_edit_views=False,
        section="Laser Sensor Information",
    )

    firmware_version = PropertyTypeAssignment(
        code="FIRMWARE_VERSION",
        data_type="VARCHAR",
        property_label="Current firmware version",
        description="""The currently installed firmware version//Die aktuell installierte Firmware-Version""",
        mandatory=False,
        show_in_edit_views=False,
        section="Software Information",
    )

    last_systemcheck = PropertyTypeAssignment(
        code="LAST_SYSTEMCHECK",
        data_type="DATE",
        property_label="Last System Check",
        description="""Date of the last system check//Datum des letzten Systemchecks""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )


class WeldingEquipment(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.WELDING_EQUIPMENT",
        description="""Generic Welding Equipment//Unspezifisches Schweiß-Equipment""",
        generated_code_prefix="INS.WLD_EQP",
    )

    last_systemcheck = PropertyTypeAssignment(
        code="LAST_SYSTEMCHECK",
        data_type="DATE",
        property_label="Last System Check",
        description="""Date of the last system check//Datum des letzten Systemchecks""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )


class Centrifuge(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.CENTRIFUGE",
        description="""Centrifuge//Zentrifuge""",
        generated_code_prefix="INS.CEN",
    )

    centrifuge_maximum_speed_rpm = PropertyTypeAssignment(
        code="CENTRIFUGE.MAXIMUM_SPEED_RPM",
        data_type="INTEGER",
        property_label="Maximum Centrifugation Speed (depending on rotor) [rpm]",
        description="""Maximum Centrifugation Speed (depending on rotor) [rpm]//Maximale Zentrifugationsgeschwindigkeit (rotorabhängig) [rpm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Instrument Specification",
    )

    centrifuge_maximum_speed_rcf = PropertyTypeAssignment(
        code="CENTRIFUGE.MAXIMUM_SPEED_RCF",
        data_type="INTEGER",
        property_label="Maximum Centrifugation Speed (depending on rotor) [rcf]",
        description="""Maximum Centrifugation Speed (depending on rotor) [rcf]//Maximale Zentrifugationsgeschwindigkeit (rotorabhängig) [rcf]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Instrument Specification",
    )

    centrifuge_is_temperature_controlled = PropertyTypeAssignment(
        code="CENTRIFUGE.IS_TEMPERATURE_CONTROLLED",
        data_type="BOOLEAN",
        property_label="Temperature can be set",
        description="""Centrifuge Temperature can be set//Zentrifuge ist temperierbar""",
        mandatory=False,
        show_in_edit_views=False,
        section="Instrument Specification",
    )

    centrifuge_minimum_temperature = PropertyTypeAssignment(
        code="CENTRIFUGE.MINIMUM_TEMPERATURE",
        data_type="INTEGER",
        property_label="Minimum Temperature [°C]",
        description="""Minimum Centrifuge Temperature [°C]//Minimale Zentrifugen-Temperatur [°C]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Instrument Specification",
    )

    centrifuge_maximum_temperature = PropertyTypeAssignment(
        code="CENTRIFUGE.MAXIMUM_TEMPERATURE",
        data_type="INTEGER",
        property_label="Maximum Temperature [°C]",
        description="""Maximum Centrifuge Temperature [°C]//Maximale Zentrifugen-Temperatur [°C]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Instrument Specification",
    )

    centrifuge_compatible_rotors = PropertyTypeAssignment(
        code="CENTRIFUGE.COMPATIBLE_ROTORS",
        data_type="VARCHAR",
        property_label="Compatible Rotors",
        description="""Compatible Rotors with this Centrifuge//Kompatible Rotatoren mit dieser Zentrifuge""",
        mandatory=False,
        show_in_edit_views=False,
        section="Instrument Specification",
    )

    centrifuge_requires_dguv_checking = PropertyTypeAssignment(
        code="CENTRIFUGE.REQUIRES_DGUV_CHECKING",
        data_type="BOOLEAN",
        property_label="Requires DGUV check",
        description="""Requires checks according to DGUV Paragraph 3 Rule 100-500//Sicherheitstechnische Überprüfung gemäß DGUV Paragraph 3 Regel 100-500 vorgeschrieben""",
        mandatory=False,
        show_in_edit_views=False,
        section="Instrument Specification",
    )

    centrifuge_date_last_dguv_checking = PropertyTypeAssignment(
        code="CENTRIFUGE.DATE_LAST_DGUV_CHECKING",
        data_type="DATE",
        property_label="Date of last DGUV check",
        description="""Date of last checks according to DGUV Paragraph 3 Rule 100-500//Datum der letzten sicherheitstechnischen Überprüfung gemäß DGUV Paragraph 3 Regel 100-500""",
        mandatory=False,
        show_in_edit_views=False,
        section="Instrument Specification",
    )


class CentrifugeRotor(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.CENTRIFUGE_ROTOR",
        description="""Centrifuge Rotor//Zentrifugenrotor""",
        generated_code_prefix="INS.CEN_ROT",
    )

    centrifuge_rotor_maximum_speed_rpm = PropertyTypeAssignment(
        code="CENTRIFUGE_ROTOR.MAXIMUM_SPEED_RPM",
        data_type="INTEGER",
        property_label="Maximum Speed [rpm]",
        description="""Maximum Rotor Speed [rpm]//Maximale Rotor-Geschwindigkeit [rpm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Rotor Specification",
    )

    centrifuge_rotor_maximum_speed_rcf = PropertyTypeAssignment(
        code="CENTRIFUGE_ROTOR.MAXIMUM_SPEED_RCF",
        data_type="INTEGER",
        property_label="Maximum Speed [rcf]",
        description="""Maximum Rotor Speed [rcf]//Maximale Rotor-Geschwindigkeit [rcf]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Rotor Specification",
    )

    centrifuge_rotor_maximum_capacity_vials = PropertyTypeAssignment(
        code="CENTRIFUGE_ROTOR.MAXIMUM_CAPACITY_VIALS",
        data_type="INTEGER",
        property_label="Maximum Capacity (Number of Vials)",
        description="""Maximum Rotor Capacity (number of vials)//Maximale Rotor-Kapazität (Anzahl an Gefäßen)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Rotor Specification",
    )

    centrifuge_rotor_maximum_capacity_volume = PropertyTypeAssignment(
        code="CENTRIFUGE_ROTOR.MAXIMUM_CAPACITY_VOLUME",
        data_type="INTEGER",
        property_label="Maximum Capacity (Volume) [mL]",
        description="""Maximum Rotor Capacity (volume) [mL]//Maximale Rotor-Kapazität (Volumen) [mL]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Rotor Specification",
    )

    centrifuge_rotor_compatible_vials = PropertyTypeAssignment(
        code="CENTRIFUGE_ROTOR.COMPATIBLE_VIALS",
        data_type="VARCHAR",
        property_label="Compatible vials (possibly with adapters)",
        description="""Compatible vials (possibly with adapters)//Kompatible Gefäße (ggf. mit Adapter)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Rotor Specification",
    )


class Ftir(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.FTIR",
        description="""Fourier-Transfom Infrared Spectroscopy//Fourier-Transfom Infrarotspektroskopie""",
        generated_code_prefix="EXP.FTIR",
    )

    ftir_instrument = PropertyTypeAssignment(
        code="FTIR.INSTRUMENT",
        data_type="VARCHAR",
        property_label="Instrument",
        description="""FT-IR Instrument//FT-IR Instrument""",
        mandatory=False,
        show_in_edit_views=False,
        section="Meaurement Parameters",
    )

    ftir_start_wavenumber = PropertyTypeAssignment(
        code="FTIR.START_WAVENUMBER",
        data_type="REAL",
        property_label="Start Wavenumber [1/cm]",
        description="""Start Wavenumber [1/cm]//Start-Wellenzahl [1/cm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Meaurement Parameters",
    )

    ftir_end_wavenumber = PropertyTypeAssignment(
        code="FTIR.END_WAVENUMBER",
        data_type="REAL",
        property_label="End Wavenumber [1/cm]",
        description="""End Wavenumber [1/cm]//End-Wellenzahl [1/cm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Meaurement Parameters",
    )

    ftir_resolution = PropertyTypeAssignment(
        code="FTIR.RESOLUTION",
        data_type="INTEGER",
        property_label="Resolution [1/cm]",
        description="""Resolution [1/cm]//Auflösung [1/cm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Meaurement Parameters",
    )

    ftir_scans = PropertyTypeAssignment(
        code="FTIR.SCANS",
        data_type="INTEGER",
        property_label="Number of Scans",
        description="""Number of FTIR Scans//Anzahl FTIR Scans""",
        mandatory=False,
        show_in_edit_views=False,
        section="Meaurement Parameters",
    )

    ftir_accessory = PropertyTypeAssignment(
        code="FTIR.ACCESSORY",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="FTIR_ACCESSORIES",
        property_label="Accessory",
        description="""FTIR Accessory//FTIR Zubehör""",
        mandatory=False,
        show_in_edit_views=False,
        section="Meaurement Parameters",
    )

    ftir_is_flushed = PropertyTypeAssignment(
        code="FTIR.IS_FLUSHED",
        data_type="BOOLEAN",
        property_label="Flushed with Nitrogen",
        description="""Flushed with Nitrogen//Gespült mit Sickstoff""",
        mandatory=False,
        show_in_edit_views=False,
        section="Meaurement Parameters",
    )


class Sem(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.SEM",
        description="""Scanning Electron Microscopy//Rasterelektronenmikroskopie""",
        generated_code_prefix="EXP.SEM",
    )

    sem_instrument = PropertyTypeAssignment(
        code="SEM.INSTRUMENT",
        data_type="VARCHAR",
        property_label="Instrument",
        description="""SEM Instrument//SEM Instrument""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    sem_imagesizex = PropertyTypeAssignment(
        code="SEM.IMAGESIZEX",
        data_type="VARCHAR",
        property_label="Image Size X",
        description="""Image Size X//Bildgröße X""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    sem_imagesizey = PropertyTypeAssignment(
        code="SEM.IMAGESIZEY",
        data_type="VARCHAR",
        property_label="Image Size Y",
        description="""Image Size Y//Bildgröße Y""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    sem_operatingmode = PropertyTypeAssignment(
        code="SEM.OPERATINGMODE",
        data_type="VARCHAR",
        property_label="Operating Mode",
        description="""Operating Mode//Aufnahmemodus""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    sem_detector = PropertyTypeAssignment(
        code="SEM.DETECTOR",
        data_type="VARCHAR",
        property_label="Detector",
        description="""Detector//Detektor""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    sem_projectormode = PropertyTypeAssignment(
        code="SEM.PROJECTORMODE",
        data_type="VARCHAR",
        property_label="Projector Mode",
        description="""Projector Mode//Projektionsmodus""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    sem_pixelsizex = PropertyTypeAssignment(
        code="SEM.PIXELSIZEX",
        data_type="VARCHAR",
        property_label="Pixel Size X",
        description="""Pixel Size X//Pixelgröße X""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    sem_pixelsizey = PropertyTypeAssignment(
        code="SEM.PIXELSIZEY",
        data_type="VARCHAR",
        property_label="Pixel Size Y",
        description="""Pixel Size Y//Pixelgrße Y""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    sem_accelerationvoltage = PropertyTypeAssignment(
        code="SEM.ACCELERATIONVOLTAGE",
        data_type="VARCHAR",
        property_label="Acceleration Voltage [keV]",
        description="""Acceleration Voltage [keV]//Beschleunigungsspannung [keV]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    sem_magnification = PropertyTypeAssignment(
        code="SEM.MAGNIFICATION",
        data_type="VARCHAR",
        property_label="Magnification",
        description="""Magnificaiton//Vergrößerung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    sem_workingdistance = PropertyTypeAssignment(
        code="SEM.WORKINGDISTANCE",
        data_type="VARCHAR",
        property_label="Working Distance [mm]",
        description="""Working Distance [mm]//Arbeitsabstand [mm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )


class Nmr(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.NMR",
        description="""Nuclear Magnetic Resonance Spectroscopy//Kernspinresonanz-Spektroskopie""",
        generated_code_prefix="EXP.NMR",
    )

    nmr_instrument = PropertyTypeAssignment(
        code="NMR.INSTRUMENT",
        data_type="VARCHAR",
        property_label="Instrument",
        description="""NMR Instrument//NMR Instrument""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    nmr_nucleus_direct = PropertyTypeAssignment(
        code="NMR.NUCLEUS_DIRECT",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="NMR_NUCLEI",
        property_label="Nucleus (direct)",
        description="""Nucleus (direct)//Kern (direct)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    nmr_nucleus_indirect = PropertyTypeAssignment(
        code="NMR.NUCLEUS_INDIRECT",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="NMR_NUCLEI",
        property_label="Nucleus (indirect, 2D only)",
        description="""Nucleus (indirect, 2D only)//Kern (indirekt, nur 2D)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    nmr_solvent = PropertyTypeAssignment(
        code="NMR.SOLVENT",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="NMR_SOLVENTS",
        property_label="Solvent",
        description="""NMR Solvent//NMR Lösungsmittel""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    nmr_frequency = PropertyTypeAssignment(
        code="NMR.FREQUENCY",
        data_type="REAL",
        property_label="Frequency [MHz]",
        description="""NMR Frequency [MHz]//NMR Frequenz [MHz]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    nmr_experiment = PropertyTypeAssignment(
        code="NMR.EXPERIMENT",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="NMR_EXPERIMENT_TYPES",
        property_label="Experiment",
        description="""NMR Experiment//NMR Experiment""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    nmr_scans = PropertyTypeAssignment(
        code="NMR.SCANS",
        data_type="INTEGER",
        property_label="Number of Scans",
        description="""Number of NMR Scans//Anzahl NMR Scans""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    nmr_start_chemical_shift = PropertyTypeAssignment(
        code="NMR.START_CHEMICAL_SHIFT",
        data_type="REAL",
        property_label="Start Chemical Shift [ppm]",
        description="""Start Chemical Shift [ppm]//Start Chemische Verschiebung [ppm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    nmr_end_chemical_shift = PropertyTypeAssignment(
        code="NMR.END_CHEMICAL_SHIFT",
        data_type="REAL",
        property_label="End Chemical Shift [ppm]",
        description="""End Chemical Shift [ppm]//Ende Chemische Verschiebung [ppm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    nmr_is_qnmr = PropertyTypeAssignment(
        code="NMR.IS_QNMR",
        data_type="BOOLEAN",
        property_label="Quantitative NMR",
        description="""Quantitative NMR//Quantitatives NMR""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    nmr_pulse_angle = PropertyTypeAssignment(
        code="NMR.PULSE_ANGLE",
        data_type="REAL",
        property_label="Pulse Angle [degree]",
        description="""Pulse Angle [degree]//Pulswinkel [degree]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    nmr_interpulse_delay = PropertyTypeAssignment(
        code="NMR.INTERPULSE_DELAY",
        data_type="REAL",
        property_label="Interpulse Delay [s]",
        description="""Interpulse Delay [s]//Wartezeit zwischen Pulsen [s]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    nmr_acquisition_time = PropertyTypeAssignment(
        code="NMR.ACQUISITION_TIME",
        data_type="REAL",
        property_label="Acquisition Time [s]",
        description="""Acquisition Time [s]//Akquisitionszeit [s]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )


class Tem(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.TEM",
        description="""Transmission Electron Microscopy//Transmisisonselektronenmikroskopie""",
        generated_code_prefix="EXP.TEM",
    )

    tem_instrument = PropertyTypeAssignment(
        code="TEM.INSTRUMENT",
        data_type="VARCHAR",
        property_label="Instrument",
        description="""TEM Instrument//TEM Instrument""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    tem_imagesizex = PropertyTypeAssignment(
        code="TEM.IMAGESIZEX",
        data_type="VARCHAR",
        property_label="Image Size X",
        description="""Image Size X//Bildgröße X""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    tem_imagesizey = PropertyTypeAssignment(
        code="TEM.IMAGESIZEY",
        data_type="VARCHAR",
        property_label="Image Size Y",
        description="""Image Size Y//Bildgröße Y""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    tem_operatingmode = PropertyTypeAssignment(
        code="TEM.OPERATINGMODE",
        data_type="VARCHAR",
        property_label="Operating Mode",
        description="""Operating Mode//Aufnahmemodus""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    tem_detector = PropertyTypeAssignment(
        code="TEM.DETECTOR",
        data_type="VARCHAR",
        property_label="Detector",
        description="""Detector//Detektor""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    tem_projectormode = PropertyTypeAssignment(
        code="TEM.PROJECTORMODE",
        data_type="VARCHAR",
        property_label="Projector Mode",
        description="""Projector Mode//Projektionsmodus""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    tem_pixelsizex = PropertyTypeAssignment(
        code="TEM.PIXELSIZEX",
        data_type="VARCHAR",
        property_label="Pixel Size X",
        description="""Pixel Size X//Pixelgröße X""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    tem_pixelsizey = PropertyTypeAssignment(
        code="TEM.PIXELSIZEY",
        data_type="VARCHAR",
        property_label="Pixel Size Y",
        description="""Pixel Size Y//Pixelgrße Y""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    tem_accelerationvoltage = PropertyTypeAssignment(
        code="TEM.ACCELERATIONVOLTAGE",
        data_type="VARCHAR",
        property_label="Acceleration Voltage  [keV]",
        description="""Acceleration Voltage [keV]//Beschleunigungsspannung [keV]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    tem_magnification = PropertyTypeAssignment(
        code="TEM.MAGNIFICATION",
        data_type="VARCHAR",
        property_label="Magnification",
        description="""Magnification//Vergrößerung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    tem_cameralength = PropertyTypeAssignment(
        code="TEM.CAMERALENGTH",
        data_type="VARCHAR",
        property_label="Camera Length",
        description="""Camera Length//Kamera-Länge""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    tem_spot_index = PropertyTypeAssignment(
        code="TEM.SPOT_INDEX",
        data_type="VARCHAR",
        property_label="Spot Index",
        description="""Spot Index//Spot Index""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    tem_gun_lens_setting = PropertyTypeAssignment(
        code="TEM.GUN_LENS_SETTING",
        data_type="VARCHAR",
        property_label="Gun Lens Setting",
        description="""Gun Lens Setting//Einstellung der Elektronenquellenlinse""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    tem_c2_aperture_name = PropertyTypeAssignment(
        code="TEM.C2_APERTURE_NAME",
        data_type="VARCHAR",
        property_label="C2 Aperture",
        description="""C2 Aperture//C2 Apertur""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    tem_obj_aperture_name = PropertyTypeAssignment(
        code="TEM.OBJ_APERTURE_NAME",
        data_type="VARCHAR",
        property_label="Objective Aperture",
        description="""Objective Aperture//Objektiv Apertur""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    tem_saed_aperturediameter = PropertyTypeAssignment(
        code="TEM.SAED_APERTUREDIAMETER",
        data_type="VARCHAR",
        property_label="SAED Aperture Diameter",
        description="""SAED Aperture Diameter//SAED Apertur Durchmesser""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    tem_saed_apertureposx = PropertyTypeAssignment(
        code="TEM.SAED_APERTUREPOSX",
        data_type="VARCHAR",
        property_label="SAED Aperture Pos X",
        description="""SAED Aperture Pos X//SAED Apertur Position X""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    tem_saed_apertureposy = PropertyTypeAssignment(
        code="TEM.SAED_APERTUREPOSY",
        data_type="VARCHAR",
        property_label="SAED Aperture PosY",
        description="""SAED Aperture Pos Y//SAED Apertur Position Y""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )


class Dls(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.DLS",
        description="""Dynamic and electrophoretic light scattering//Dynamische und elektrophoretische Lichtstreuung""",
        generated_code_prefix="EXP.DLS",
    )

    dls_material = PropertyTypeAssignment(
        code="DLS.MATERIAL",
        data_type="VARCHAR",
        property_label="Material Name",
        description="""Material Name for DLS Measurement//Materialname für DLS Messung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    dls_dispersant = PropertyTypeAssignment(
        code="DLS.DISPERSANT",
        data_type="VARCHAR",
        property_label="Dispersant",
        description="""Dispersant for DLS Measurement//Dispersant für DLS Messung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    dls_temperature = PropertyTypeAssignment(
        code="DLS.TEMPERATURE",
        data_type="REAL",
        property_label="Temperature [°C]",
        description="""Temperature [°C]//Temperatur [°C]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    dls_celldescription = PropertyTypeAssignment(
        code="DLS.CELLDESCRIPTION",
        data_type="VARCHAR",
        property_label="Cell Description",
        description="""DLS Cell Description//DLS Messküvette""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    dls_attenuator = PropertyTypeAssignment(
        code="DLS.ATTENUATOR",
        data_type="INTEGER",
        property_label="Attenuator",
        description="""Attenuator for DLS Measurement//Abschwächung für DLS Messung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Parameters",
    )

    dls_zavg = PropertyTypeAssignment(
        code="DLS.ZAVG",
        data_type="REAL",
        property_label="Z-Average",
        description="""Z-Average//Z-Durchschnitt""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results",
    )

    dls_pdi = PropertyTypeAssignment(
        code="DLS.PDI",
        data_type="REAL",
        property_label="PDI",
        description="""Polydispersity Index//Polydispersitätsindex""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results",
    )

    dls_zeta = PropertyTypeAssignment(
        code="DLS.ZETA",
        data_type="REAL",
        property_label="Zeta Potential [mV]",
        description="""Zeta Potential [mV]//Zeta Potential [mV]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results",
    )

    dls_pk1int = PropertyTypeAssignment(
        code="DLS.PK1INT",
        data_type="REAL",
        property_label="Peak 1 (Intensity) [nm]",
        description="""Peak 1 (Intensity) [nm]//Peak 1 (Intensität) [nm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Intensity Distribution)",
    )

    dls_pk1intwidth = PropertyTypeAssignment(
        code="DLS.PK1INTWIDTH",
        data_type="REAL",
        property_label="Peak 1 Width (Intensity) [nm]",
        description="""Peak 1 Width (Intensity) [nm]//Peak 1 Breite (Intensität) [nm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Intensity Distribution)",
    )

    dls_pk1intpd = PropertyTypeAssignment(
        code="DLS.PK1INTPD",
        data_type="REAL",
        property_label="Peak 1 Polydispersity (Intensity)",
        description="""Peak 1 Polydispersity (Intensity)//Peak 1 Polydispersität (Intensität)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Intensity Distribution)",
    )

    dls_pk2int = PropertyTypeAssignment(
        code="DLS.PK2INT",
        data_type="REAL",
        property_label="Peak 2 (Intensity) [nm]",
        description="""Peak 2 (Intensity) [nm]//Peak 2 (Intensität) [nm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Intensity Distribution)",
    )

    dls_pk2intwidth = PropertyTypeAssignment(
        code="DLS.PK2INTWIDTH",
        data_type="REAL",
        property_label="Peak 2 Width (Intensity) [nm]",
        description="""Peak 2 Width (Intensity) [nm]//Peak 2 Breite (Intensität) [nm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Intensity Distribution)",
    )

    dls_pk2intpd = PropertyTypeAssignment(
        code="DLS.PK2INTPD",
        data_type="REAL",
        property_label="Peak 2 Polydispersity (Intensity)",
        description="""Peak 2 Polydispersity (Intensity)//Peak 2 Polydispersität (Intensität)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Intensity Distribution)",
    )

    dls_pk3int = PropertyTypeAssignment(
        code="DLS.PK3INT",
        data_type="REAL",
        property_label="Peak 3 (Intensity) [nm]",
        description="""Peak 3 (Intensity) [nm]//Peak 3 (Intensität) [nm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Intensity Distribution)",
    )

    dls_pk3intwidth = PropertyTypeAssignment(
        code="DLS.PK3INTWIDTH",
        data_type="REAL",
        property_label="Peak 3 Width (Intensity) [nm]",
        description="""Peak 3 Width (Intensity) [nm]//Peak 3 Breite (Intensität) [nm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Intensity Distribution)",
    )

    dls_pk3intpd = PropertyTypeAssignment(
        code="DLS.PK3INTPD",
        data_type="REAL",
        property_label="Peak 3 Polydispersity (Intensity)",
        description="""Peak 3 Polydispersity (Intensity)//Peak 3 Polydispersität (Intensität)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Intensity Distribution)",
    )

    dls_pk1vol = PropertyTypeAssignment(
        code="DLS.PK1VOL",
        data_type="REAL",
        property_label="Peak 1 (Volume) [nm]",
        description="""Peak 1 (Volume) [nm]//Peak 1 (Volumen) [nm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Volume Distribution)",
    )

    dls_pk1volwidth = PropertyTypeAssignment(
        code="DLS.PK1VOLWIDTH",
        data_type="REAL",
        property_label="Peak 1 Width (Volume) [nm]",
        description="""Peak 1 Width (Volume) [nm]//Peak 1 Breite (Volumen) [nm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Volume Distribution)",
    )

    dls_pk1volpd = PropertyTypeAssignment(
        code="DLS.PK1VOLPD",
        data_type="REAL",
        property_label="Peak 1 Polydispersity (Volume)",
        description="""Peak 1 Polydispersity (Volume)//Peak 1 Polydispersität (Volumen)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Volume Distribution)",
    )

    dls_pk2vol = PropertyTypeAssignment(
        code="DLS.PK2VOL",
        data_type="REAL",
        property_label="Peak 2 (Volume) [nm]",
        description="""Peak 2 (Volume) [nm]//Peak 2 (Volumen) [nm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Volume Distribution)",
    )

    dls_pk2volwidth = PropertyTypeAssignment(
        code="DLS.PK2VOLWIDTH",
        data_type="REAL",
        property_label="Peak 2 Width (Volume) [nm]",
        description="""Peak 2 Width (Volume) [nm]//Peak 2 Breite (Volumen) [nm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Volume Distribution)",
    )

    dls_pk2volpd = PropertyTypeAssignment(
        code="DLS.PK2VOLPD",
        data_type="REAL",
        property_label="Peak 2 Polydispersity (Volume)",
        description="""Peak 2 Polydispersity (Volume)//Peak 2 Polydispersität (Volumen)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Volume Distribution)",
    )

    dls_pk3vol = PropertyTypeAssignment(
        code="DLS.PK3VOL",
        data_type="REAL",
        property_label="Peak 3 (Volume) [nm]",
        description="""Peak 3 (Volume) [nm]//Peak 3 (Volumen) [nm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Volume Distribution)",
    )

    dls_pk3volwidth = PropertyTypeAssignment(
        code="DLS.PK3VOLWIDTH",
        data_type="REAL",
        property_label="Peak 3 Width (Volume) [nm]",
        description="""Peak 3 Width (Volume) [nm]//Peak 3 Breite (Volumen) [nm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Volume Distribution)",
    )

    dls_pk3volpd = PropertyTypeAssignment(
        code="DLS.PK3VOLPD",
        data_type="REAL",
        property_label="Peak 3 Polydispersity (Volume)",
        description="""Peak 3 Polydispersity (Volume)//Peak 3 Polydispersität (Volumen)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Volume Distribution)",
    )

    dls_pk1num = PropertyTypeAssignment(
        code="DLS.PK1NUM",
        data_type="REAL",
        property_label="Peak 1 (Number) [nm]",
        description="""Peak 1 (Number) [nm]//Peak 1 (Anzahl) [nm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Number Distribution)",
    )

    dls_pk1numwidth = PropertyTypeAssignment(
        code="DLS.PK1NUMWIDTH",
        data_type="REAL",
        property_label="Peak 1 Width (Number) [nm]",
        description="""Peak 1 Width (Number) [nm]//Peak 1 Breite (Anzahl) [nm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Number Distribution)",
    )

    dls_pk1numpd = PropertyTypeAssignment(
        code="DLS.PK1NUMPD",
        data_type="REAL",
        property_label="Peak 1 Polydispersity (Number)",
        description="""Peak 1 Polydispersity (Number)//Peak 1 Polydispersität (Anzahl)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Number Distribution)",
    )

    dls_pk2num = PropertyTypeAssignment(
        code="DLS.PK2NUM",
        data_type="REAL",
        property_label="Peak 2 (Number) [nm]",
        description="""Peak 2 (Number) [nm]//Peak 2 (Anzahl) [nm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Number Distribution)",
    )

    dls_pk2numwidth = PropertyTypeAssignment(
        code="DLS.PK2NUMWIDTH",
        data_type="REAL",
        property_label="Peak 2 Width (Number) [nm]",
        description="""Peak 2 Width (Number) [nm]//Peak 2 Breite (Anzahl) [nm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Number Distribution)",
    )

    dls_pk2numpd = PropertyTypeAssignment(
        code="DLS.PK2NUMPD",
        data_type="REAL",
        property_label="Peak 2 Polydispersity (Number)",
        description="""Peak 2 Polydispersity (Number)//Peak 2 Polydispersität (Anzahl)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Number Distribution)",
    )

    dls_pk3num = PropertyTypeAssignment(
        code="DLS.PK3NUM",
        data_type="REAL",
        property_label="Peak 3 (Number) [nm]",
        description="""Peak 3 (Number) [nm]//Peak 3 (Anzahl) [nm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Number Distribution)",
    )

    dls_pk3numwidth = PropertyTypeAssignment(
        code="DLS.PK3NUMWIDTH",
        data_type="REAL",
        property_label="Peak 3 Width (Number) [nm]",
        description="""Peak 3 Width (Number) [nm]//Peak 3 Breite (Anzahl) [nm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Number Distribution)",
    )

    dls_pk3numpd = PropertyTypeAssignment(
        code="DLS.PK3NUMPD",
        data_type="REAL",
        property_label="Peak 3 Polydispersity (Number)",
        description="""Peak 3 Polydispersity (Number)//Peak 3 Polydispersität (Anzahl)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Number Distribution)",
    )

    dls_pk1zeta = PropertyTypeAssignment(
        code="DLS.PK1ZETA",
        data_type="REAL",
        property_label="Peak 1 (Zeta) [mV]",
        description="""Peak 1 (Zetapotential) [mV]//Peak 1 (Zetapotential) [mV]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Zeta Potential)",
    )

    dls_pk1zetawidth = PropertyTypeAssignment(
        code="DLS.PK1ZETAWIDTH",
        data_type="REAL",
        property_label="Peak 1 Width (Zeta) [mV]",
        description="""Peak 1 Width (Zetapotential) [mV]//Peak 1 Breite (Zetapotential) [mV]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Zeta Potential)",
    )

    dls_pk2zeta = PropertyTypeAssignment(
        code="DLS.PK2ZETA",
        data_type="REAL",
        property_label="Peak 2 (Zeta) [mV]",
        description="""Peak 2 (Zetapotential) [mV]//Peak 2 (Zetapotential) [mV]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Zeta Potential)",
    )

    dls_pk2zetawidth = PropertyTypeAssignment(
        code="DLS.PK2ZETAWIDTH",
        data_type="REAL",
        property_label="Peak 2 Width (Zeta) [mV]",
        description="""Peak 2 Width (Zetapotential) [mV]//Peak 2 Breite (Zetapotential) [mV]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Zeta Potential)",
    )

    dls_pk3zeta = PropertyTypeAssignment(
        code="DLS.PK3ZETA",
        data_type="REAL",
        property_label="Peak 3 (Zeta) [mV]",
        description="""Peak 3 (Zetapotential) [mV]//Peak 3 (Zetapotential) [mV]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Zeta Potential)",
    )

    dls_pk3zetawidth = PropertyTypeAssignment(
        code="DLS.PK3ZETAWIDTH",
        data_type="REAL",
        property_label="Peak 3 Width (Zeta) [mV]",
        description="""Peak 3 Width (Zetapotential) [mV]//Peak 3 Breite (Zetapotential) [mV]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Results (Zeta Potential)",
    )

    dls_analysismodel = PropertyTypeAssignment(
        code="DLS.ANALYSISMODEL",
        data_type="VARCHAR",
        property_label="Analysis Model",
        description="""Analysis Model//Analysemodell""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Information",
    )

    dls_intercept = PropertyTypeAssignment(
        code="DLS.INTERCEPT",
        data_type="REAL",
        property_label="Measured Intercept",
        description="""Measured Intercept//Achsenabschnitt""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Information",
    )

    dls_sizemerit = PropertyTypeAssignment(
        code="DLS.SIZEMERIT",
        data_type="REAL",
        property_label="Size Merit",
        description="""Size Merit//Güte""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Information",
    )

    dls_cumulantsfiterror = PropertyTypeAssignment(
        code="DLS.CUMULANTSFITERROR",
        data_type="REAL",
        property_label="Cumulants Fit Error",
        description="""Cumulants Fit Error//Fehler des Kummulanten-Fits""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Information",
    )

    dls_multimodalfiterror = PropertyTypeAssignment(
        code="DLS.MULTIMODALFITERROR",
        data_type="REAL",
        property_label="Multimodal Fit Error",
        description="""Multimodal Fit Error//Fehler des multimodalen Fits""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Information",
    )

    dls_fkamodel = PropertyTypeAssignment(
        code="DLS.FKAMODEL",
        data_type="VARCHAR",
        property_label="Fka Model",
        description="""Fka Model//Fka Modell""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Information",
    )

    dls_volt = PropertyTypeAssignment(
        code="DLS.VOLT",
        data_type="REAL",
        property_label="Measured Voltage [V]",
        description="""Measured Voltage [V]//Gemessene Spannung [V]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Information",
    )

    dls_cond = PropertyTypeAssignment(
        code="DLS.COND",
        data_type="REAL",
        property_label="Conductivity [mS/cm]",
        description="""Conductivity [mS/cm]//Leitfähigkeit [mS/cm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Measurement Information",
    )


class MsBatch(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MS_BATCH",
        description="""MS sample batch with attached raw data//MS Proben-Batch mit verknüpften Rohdaten""",
        generated_code_prefix="EXP.MSB",
    )

    ms_ionization_mode = PropertyTypeAssignment(
        code="MS_IONIZATION_MODE",
        data_type="VARCHAR",
        property_label="Ionization mode",
        description="""Ionization mode (pos/neg)//Ionisierung (pos/neg)""",
        mandatory=False,
        show_in_edit_views=False,
        section="MS Information",
    )

    ms_hyphenation_method = PropertyTypeAssignment(
        code="MS_HYPHENATION_METHOD",
        data_type="VARCHAR",
        property_label="Hyphenation method",
        description="""Hyphenation (DI, LC, GC, CE)//Probeninjektion (DI, LC, GC, CE)""",
        mandatory=False,
        show_in_edit_views=False,
        section="MS Information",
    )


class Bam(Person):
    defs = ObjectTypeDef(
        code="PERSON.BAM",
        description="""A BAM employee (is generated automatically)//Ein*e BAM-Mitarbeiter*in (wird automatisch generiert)""",
        generated_code_prefix="S",
    )

    bam_oe = PropertyTypeAssignment(
        code="BAM_OE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_OE",
        property_label="BAM Organizational Entity",
        description="""BAM Organizational Entity//BAM Organisationseinheit (OE)""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_username = PropertyTypeAssignment(
        code="BAM_USERNAME",
        data_type="VARCHAR",
        property_label="BAM username",
        description="""BAM username//BAM Benutzername""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_userprofile = PropertyTypeAssignment(
        code="BAM_USERPROFILE",
        data_type="HYPERLINK",
        property_label="BAM user profile link",
        description="""BAM user profile link//BAM Link zum Benutzerprofil""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_data_store_user_status = PropertyTypeAssignment(
        code="BAM_DATA_STORE_USER_STATUS",
        data_type="BOOLEAN",
        property_label="BAM Data Store user",
        description="""BAM Data Store user//BAM Data Store-Nutzer*in""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )


# Freezer is defined several times in the model
class Freezer1(Control):
    defs = ObjectTypeDef(
        code="CONTROL.FREEZER",
        description="""This Object allows to store temperature data as a control point for a Freezer//Dieses Objekt erlaubt einen Kontrollpunkt für ein Kühlgerät zu erstellen""",
        generated_code_prefix="CTRL.FRE",
    )

    temp_min_celsius = PropertyTypeAssignment(
        code="TEMP_MIN_CELSIUS",
        data_type="REAL",
        property_label="Temperature Minimum [°C]",
        description="""Minimum Temperature [°C]//Minimaltemperatur [°C]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Control Data",
    )

    temp_max_celsius = PropertyTypeAssignment(
        code="TEMP_MAX_CELSIUS",
        data_type="REAL",
        property_label="Temperature Maximum [°C]",
        description="""Maximum Temperature [°C]//Maximaltemperatur [°C]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Control Data",
    )


# Freezer is defined several times in the model
class Freezer2(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.FREEZER",
        description="""Cooling Device//Kühlgerät""",
        generated_code_prefix="INS.FRE",
    )

    temp_min_celsius = PropertyTypeAssignment(
        code="TEMP_MIN_CELSIUS",
        data_type="REAL",
        property_label="Temperature Minimum [°C]",
        description="""Minimum Temperature [°C]//Minimaltemperatur [°C]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Freezer Details",
    )

    temp_max_celsius = PropertyTypeAssignment(
        code="TEMP_MAX_CELSIUS",
        data_type="REAL",
        property_label="Temperature Maximum [°C]",
        description="""Maximum Temperature [°C]//Maximaltemperatur [°C]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Freezer Details",
    )


class MassSpec(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.MASS_SPEC",
        description="""Mass Spectrometer//Massenspektrometer""",
        generated_code_prefix="INS.MS",
    )

    mass_spec_type = PropertyTypeAssignment(
        code="MASS_SPEC_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="MASS_SPEC_TYPE",
        property_label="MS Type",
        description="""Mass Spectrometer Type//Massenspektrometer-Typ""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )


class Scale(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.SCALE",
        description="""Scale//Waage""",
        generated_code_prefix="INS.SCA",
    )

    weight_min = PropertyTypeAssignment(
        code="WEIGHT_MIN",
        data_type="REAL",
        property_label="Minimum weight",
        description="""Minimum weight (in UNIT_MASS)//Minimales Gewicht (in UNIT_MASS)""",
        mandatory=True,
        show_in_edit_views=False,
        section="Technical Details",
    )

    weight_max = PropertyTypeAssignment(
        code="WEIGHT_MAX",
        data_type="REAL",
        property_label="Maximum weight",
        description="""Maximum weight (in UNIT_MASS)//Maximales Gewicht (in UNIT_MASS)""",
        mandatory=True,
        show_in_edit_views=False,
        section="Technical Details",
    )

    precision_mass = PropertyTypeAssignment(
        code="PRECISION_MASS",
        data_type="REAL",
        property_label="Measurement precision//Messgenauigkeit",
        description="""Precision of the scale/measurement  (in UNIT_MASS)//Messgenauigkeit Waage/Messung  (in UNIT_MASS)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Details",
    )

    unit_mass = PropertyTypeAssignment(
        code="UNIT_MASS",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="UNIT_MASS",
        property_label="Mass unit//Masseeinheit",
        description="""Mass unit//Masseeinheit""",
        mandatory=True,
        show_in_edit_views=False,
        section="Technical Details",
    )


class MsCenter(Project):
    defs = ObjectTypeDef(
        code="PROJECT.MS_CENTER",
        description="""Mass Spectrometry Center Project//MS-Zentrum Projekt""",
        generated_code_prefix="PROJ.MSC",
    )

    acting_person = PropertyTypeAssignment(
        code="ACTING_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Acting Person",
        description="""Acting Person//Handelnde Person""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    sample_provider = PropertyTypeAssignment(
        code="SAMPLE_PROVIDER",
        data_type="VARCHAR",
        property_label="Sample source",
        description="""Who is the provider of the Sample?//Wer hat die Probe erzeugt/geliefert?""",
        mandatory=True,
        show_in_edit_views=False,
        section="Sample Information",
    )

    sample_name = PropertyTypeAssignment(
        code="SAMPLE_NAME",
        data_type="VARCHAR",
        property_label="Sample name",
        description="""What is the label on the Sample//Probenbezeichnung""",
        mandatory=True,
        show_in_edit_views=False,
        section="Sample Information",
    )

    sample_received = PropertyTypeAssignment(
        code="SAMPLE_RECEIVED",
        data_type="TIMESTAMP",
        property_label="Date of receipt",
        description="""Date when samples arrived//Eingangsdatum der Proben""",
        mandatory=True,
        show_in_edit_views=False,
        section="Sample Information",
    )

    sample_location = PropertyTypeAssignment(
        code="SAMPLE_LOCATION",
        data_type="VARCHAR",
        property_label="Retained samples",
        description="""Location of retained samples (if any?)//Standort von Rückstellproben (wenn existent?)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Sample Information",
    )

    sample_consumed = PropertyTypeAssignment(
        code="SAMPLE_CONSUMED",
        data_type="BOOLEAN",
        property_label="Leftover sample",
        description="""Leftover sample or material//Restliche(s) Probe oder Material""",
        mandatory=True,
        show_in_edit_views=False,
        section="Sample Information",
    )

    sample_matrix = PropertyTypeAssignment(
        code="SAMPLE_MATRIX",
        data_type="MULTILINE_VARCHAR",
        property_label="Sample matrix",
        description="""Extra Informaton about samples//Zusätzliche Information zu den Proben""",
        mandatory=False,
        show_in_edit_views=False,
        section="Sample Information",
    )

    sample_analyte = PropertyTypeAssignment(
        code="SAMPLE_ANALYTE",
        data_type="VARCHAR",
        property_label="Analyte",
        description="""Name/ID of sought-after substance//Name/Kürzel der gesuchten Substanz""",
        mandatory=False,
        show_in_edit_views=False,
        section="Sample Information",
    )


class SpectrometerOptical(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.SPECTROMETER_OPTICAL",
        description="""Optical Spectrometer//Optisches Spektrometer""",
        generated_code_prefix="INS.SPEC_OPT",
    )

    detection_range_min_in_nm = PropertyTypeAssignment(
        code="DETECTION_RANGE_MIN_IN_NM",
        data_type="REAL",
        property_label="Detection Range Min [nm]",
        description="""Minimal detectable wavelength [nm]//Minimale detektierbare Wellenlänge [nm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Specifications",
    )

    detection_range_max_in_nm = PropertyTypeAssignment(
        code="DETECTION_RANGE_MAX_IN_NM",
        data_type="REAL",
        property_label="Detection Range Max [nm]",
        description="""Maximal detectable wavelength [nm]//Maximale detektierbare Wellenlänge [nm]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Specifications",
    )

    spectrometer_type = PropertyTypeAssignment(
        code="SPECTROMETER_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="OPTICAL_SPECTROMETER_TYPE",
        property_label="Spectrometer Type",
        description="""Type of spectrometer//Spektrometertyp""",
        mandatory=False,
        show_in_edit_views=False,
        section="Specifications",
    )


class LaserGeneral(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.LASER_GENERAL",
        description="""Generalized laser entry//Generischer Laser""",
        generated_code_prefix="INS.LAS_GEN",
    )

    laser_pulse_energy_normal_in_mj = PropertyTypeAssignment(
        code="LASER_PULSE_ENERGY_NORMAL_IN_MJ",
        data_type="REAL",
        property_label="Nominal Pulse Energy [mJ]",
        description="""Nominal pulse energy in mJ//Nominale Pulsenergie in mJ""",
        mandatory=False,
        show_in_edit_views=False,
        section="Laser Specifications",
    )

    laser_beam_diameter_in_mm = PropertyTypeAssignment(
        code="LASER_BEAM_DIAMETER_IN_MM",
        data_type="REAL",
        property_label="Beam Diameter [mm]",
        description="""Output laser beam diameter in mm//Durchmesser des Ausgangslaserstrahls in mm""",
        mandatory=False,
        show_in_edit_views=False,
        section="Laser Specifications",
    )

    laser_wavelength_in_nm = PropertyTypeAssignment(
        code="LASER_WAVELENGTH_IN_NM",
        data_type="XML",
        property_label="Operating Wavelength(s) [nm]",
        description="""List all allowed wavelengths following the XML schema given//Auflistung aller zulässigen Wellenlängen gemäß dem angegebenen XML-Schema""",
        mandatory=False,
        show_in_edit_views=False,
        section="Laser Specifications",
    )

    laser_repetition_rate_in_hz = PropertyTypeAssignment(
        code="LASER_REPETITION_RATE_IN_HZ",
        data_type="REAL",
        property_label="Repetition Rate [Hz]",
        description="""Maximum repetition rate (-1 for CW) in Hz//Maximale Wiederholrate (-1 für CW) in Hz""",
        mandatory=False,
        show_in_edit_views=False,
        section="Laser Specifications",
    )

    laser_m2 = PropertyTypeAssignment(
        code="LASER_M2",
        data_type="REAL",
        property_label="M²",
        description="""M² (parameter which relates the beam divergence of a laser beam to the minimum focussed spot size that can be achieved)//M² (Beugungsmaßzahl, welche beschreibt, wie gut ein Laserstrahl bei einer gegebenen Divergenz fokussiert werden kann)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Laser Specifications",
    )

    laser_type = PropertyTypeAssignment(
        code="LASER_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="LASER_TYPE",
        property_label="Laser Type",
        description="""Type of the laser//Lasertyp""",
        mandatory=False,
        show_in_edit_views=False,
        section="Laser Specifications",
    )


class Technikum(Sample):
    defs = ObjectTypeDef(
        code="SAMPLE.TECHNIKUM",
        description="""Sample/sample material received via the Technikum in Adlershof//Probe/Probenmaterial, welches/s im Technikum in Adlershof ankommt""",
        generated_code_prefix="SAM",
    )

    technikum_material_amount = PropertyTypeAssignment(
        code="TECHNIKUM_MATERIAL_AMOUNT",
        data_type="VARCHAR",
        property_label="Material amount",
        description="""Mass or amount of material (potentially measured in non-SI units)//Materialmenge (ggf. in nicht SI-konformen Einheiten)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Material Details",
    )

    technikum_substance_concentration = PropertyTypeAssignment(
        code="TECHNIKUM_SUBSTANCE_CONCENTRATION",
        data_type="REAL",
        property_label="Analyte concentration [mg/kg]",
        description="""Concentration (in mg/kg) of sought-after substance//Konzentration(in mg/kg) des zu bestimmenden Stoffes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Material Details",
    )

    technikum_material_usage = PropertyTypeAssignment(
        code="TECHNIKUM_MATERIAL_USAGE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="MATERIAL_USAGE_TECHNIKUM",
        property_label="Material usage",
        description="""Potential material usage//Möglicher Verwendungszweck des Materials""",
        mandatory=False,
        show_in_edit_views=False,
        section="Material Details",
    )


class GmoDonor(Sample):
    defs = ObjectTypeDef(
        code="SAMPLE.GMO_DONOR",
        description="""Name of the donor organism of which the genetic information is used to generate a GMO//Name des Spenderorganismus, dessen genetische Information für die Erzeugung eines GVO verwendet wird""",
        generated_code_prefix="SAM.GMO_DON",
    )

    donor = PropertyTypeAssignment(
        code="DONOR",
        data_type="OBJECT",
        object_code="ORGANISM",
        property_label="Donor Organism",
        description="""Name of the donor organism of which the genetic information is used for generating a GMO//Name des Spenderorganismus, dessen genetische Information für die Erzeugung eines GVO verwendet wird""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    donor_risk_group = PropertyTypeAssignment(
        code="DONOR_RISK_GROUP",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="ORGANISM_RISK_GROUP",
        property_label="Donor Organism Risk Group",
        description="""Organism Risk Group Assignment//Risikogruppenzuordnung des Organismus""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    gentech_facility = PropertyTypeAssignment(
        code="GENTECH_FACILITY",
        data_type="OBJECT",
        object_code="BAM_GENTECH_FACILITY",
        property_label="BAM genetic engineering installation",
        description="""BAM genetic engineering facility//BAM gentechnische Anlage""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )


class GmoRecipient(Sample):
    defs = ObjectTypeDef(
        code="SAMPLE.GMO_RECIPIENT",
        description="""Name of the recipient organism in which the genetic information is used to generate a GMO//Name des Empfängerorganismus, in dem die genetische Information für die Erzeugung eines GVO verwendet wird""",
        generated_code_prefix="SAM.GMO_REC",
    )

    recipient = PropertyTypeAssignment(
        code="RECIPIENT",
        data_type="OBJECT",
        object_code="ORGANISM",
        property_label="Recipient Organism",
        description="""Name of the recipient organism in which the genetic information is used to generate a GMO//Name des Empfängerorganismus, in dem die genetische Information für die Erzeugung eines GVO verwendet wird""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    recipient_risk_group = PropertyTypeAssignment(
        code="RECIPIENT_RISK_GROUP",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="ORGANISM_RISK_GROUP",
        property_label="Recipient Organism Risk Group Assignment",
        description="""Organism Risk Group Assignment//Risikogruppenzuordnung des Organismus""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    plasmid_bacterial_antibiotic_resistance = PropertyTypeAssignment(
        code="PLASMID_BACTERIAL_ANTIBIOTIC_RESISTANCE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="PLASMID_BACTERIAL_ANTIBIOTIC_RESISTANCE",
        property_label="Bacterial Antibiotic Resistance",
        description="""Bacterial antibiotic resistance//Bakterielle Antibiotikaresistenz zur Selektion""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    gentech_facility = PropertyTypeAssignment(
        code="GENTECH_FACILITY",
        data_type="OBJECT",
        object_code="BAM_GENTECH_FACILITY",
        property_label="BAM genetic engineering installation",
        description="""BAM genetic engineering facility//BAM gentechnische Anlage""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )


class Plasmid(Sample):
    defs = ObjectTypeDef(
        code="SAMPLE.PLASMID",
        description="""Ring-based nucleic acid construct used as a vector to transfer genetic material//Ringförmiges Nukleinsäurekonstrukt, das als Vektor für die Übertragung von genetischem Material verwendet wird""",
        generated_code_prefix="SAM.PLA",
    )

    plasmid_ori = PropertyTypeAssignment(
        code="PLASMID_ORI",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="PLASMID_ORI",
        property_label="Origin of Replication",
        description="""Bacterial Origin of Replication (plasmid copy number)//Bakterieller Replikationsursprung""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    plasmid_bacterial_antibiotic_resistance = PropertyTypeAssignment(
        code="PLASMID_BACTERIAL_ANTIBIOTIC_RESISTANCE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="PLASMID_BACTERIAL_ANTIBIOTIC_RESISTANCE",
        property_label="Bacterial Antibiotic Resistance",
        description="""Bacterial antibiotic resistance//Bakterielle Antibiotikaresistenz zur Selektion""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    plasmid_marker = PropertyTypeAssignment(
        code="PLASMID_MARKER",
        data_type="VARCHAR",
        property_label="Plasmid marker",
        description="""Marker to select the strain/cell line after transformation/transfection//Marker zur Selektion d. Stamm/Zelllinie nach der Transformation/Transfektion""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    plasmid_other_marker = PropertyTypeAssignment(
        code="PLASMID_OTHER_MARKER",
        data_type="VARCHAR",
        property_label="Plasmid other marker",
        description="""Other marker useful for selection//Andere nützliche Marker zur Selektion""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    gentech_facility = PropertyTypeAssignment(
        code="GENTECH_FACILITY",
        data_type="OBJECT",
        object_code="BAM_GENTECH_FACILITY",
        property_label="BAM genetic engineering installation",
        description="""BAM genetic engineering facility//BAM gentechnische Anlage""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )


class Gmo(Sample):
    defs = ObjectTypeDef(
        code="SAMPLE.GMO",
        description="""Genetically Modified Organism//Gentechnisch veränderter Organismus""",
        generated_code_prefix="SAM.GMO",
    )

    vector = PropertyTypeAssignment(
        code="VECTOR",
        data_type="OBJECT",
        object_code="SAMPLE.PLASMID",
        property_label="Vector name",
        description="""A plasmid used as a biological carrier to introduce nucleic acid segments into a new cell//Ein Plasmid, das als biologischer Träger verwendet wird, um Nukleinsäuresegmente in eine neue Zelle einzubringen""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    gmo_recipient = PropertyTypeAssignment(
        code="GMO_RECIPIENT",
        data_type="OBJECT",
        object_code="SAMPLE.GMO_RECIPIENT",
        property_label="Recipient Organism",
        description="""Recipient organism in which the genetic information is used for generating a GMO//Empfängerorganismus, in dem die genetische Information für die Erzeugung eines GVO verwendet wird""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    gmo_donor = PropertyTypeAssignment(
        code="GMO_DONOR",
        data_type="OBJECT",
        object_code="SAMPLE.GMO_DONOR",
        property_label="Donor Organism",
        description="""Donor organism of which the genetic information is used for generating a GMO//Spenderorganismus, dessen genetische Information für die Erzeugung eines GVO verwendet wird""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    gmo_production_date = PropertyTypeAssignment(
        code="GMO_PRODUCTION_DATE",
        data_type="DATE",
        property_label="Production date",
        description="""Genetically modified organism produced on//Genetisch veränderter Organismus erzeugt am""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    gmo_disposal_date = PropertyTypeAssignment(
        code="GMO_DISPOSAL_DATE",
        data_type="DATE",
        property_label="Disposal date",
        description="""Genetically modified organism disposed of at//Genetisch veränderter Organismus entsorgt am""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    genetic_material = PropertyTypeAssignment(
        code="GENETIC_MATERIAL",
        data_type="MULTILINE_VARCHAR",
        property_label="Transferred genetic material",
        description="""Name of the transferred genetic material (e.g. gene name)//Name der übertragenen Nukleinsäure (z.B. Genname)""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    gmo_risk_group = PropertyTypeAssignment(
        code="GMO_RISK_GROUP",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="ORGANISM_RISK_GROUP",
        property_label="GMO Risk Group",
        description="""Organism Risk Group Assignment of GMO according own Risk Assessment//Risikogruppenzuordnung des GVO anhand eigener Risikobewertung""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    genetic_material_risk_potential = PropertyTypeAssignment(
        code="GENETIC_MATERIAL_RISK_POTENTIAL",
        data_type="BOOLEAN",
        property_label="Risk potential of transf. material",
        description="""Risk potential of transferred genetic material: Dangerous? Yes-No//Risikobewertung des übertragenen genetischen Materials: Gefährlich? Ja-Nein""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    genetic_material_justification = PropertyTypeAssignment(
        code="GENETIC_MATERIAL_JUSTIFICATION",
        data_type="MULTILINE_VARCHAR",
        property_label="Risk justification",
        description="""Justification of the risk assessment: A keyword is to be given, e.g: Toxin gene, oncogene, uncharacterised DNA fragment, defined gene, cDNA, genomic DNA, viral genome, replication defects of infectious viruses, etc.//Begründung der Risikobewertung: Es ist ein Stichwort anzugeben, z.B: Toxin-Gen, Onkogen, uncharakterisiertes DNA-Fragment, definiertes Gen, cDNA, genomische DNA, virales Genom, Replikationsdefekte infektiöser Viren usw.""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    gentech_facility = PropertyTypeAssignment(
        code="GENTECH_FACILITY",
        data_type="OBJECT",
        object_code="BAM_GENTECH_FACILITY",
        property_label="BAM genetic engineering installation",
        description="""BAM genetic engineering facility//BAM gentechnische Anlage""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )


class RmEthanol(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.RM_ETHANOL",
        description="""Experimental Step to generate a reference material Ethanol//Experimenteller Schritt zur Generierung eines Referenzmaterials Ethanol""",
        generated_code_prefix="EXP.ETHANOL",
    )

    purity_in_percentage = PropertyTypeAssignment(
        code="PURITY_IN_PERCENTAGE",
        data_type="REAL",
        property_label="Purity",
        description="""Purity of the substance [ %]// Reinheit der Substanz""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    conductivity_in_ms = PropertyTypeAssignment(
        code="CONDUCTIVITY_IN_MS",
        data_type="REAL",
        property_label="Conductivity",
        description="""Conductivity in mili Siemens (mS)//Leitfähigkeit in Millisiemens (mS)""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )


class DeviceTraining(Action):
    defs = ObjectTypeDef(
        code="ACTION.DEVICE_TRAINING",
        description="""This Object allows to document a device instruction.//Dieses Objekt erlaubt eine Geräte-Unterweisung zu dokumentieren.""",
        generated_code_prefix="ACT.DEV_TRA",
    )

    trained_person = PropertyTypeAssignment(
        code="TRAINED_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Trained Person",
        description="""Trained Person//Eingewiesene Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="Action Data",
    )


class DeviceUsage(Action):
    defs = ObjectTypeDef(
        code="ACTION.DEVICE_USAGE",
        description="""This Object allows allows to create a device usage entry.//Dieses Objekt erlaubt einen Geräte-Nutzungseintrag zu erstellen.""",
        generated_code_prefix="ACT.DEV.USE",
    )

    action_start = PropertyTypeAssignment(
        code="ACTION_START",
        data_type="TIMESTAMP",
        property_label="Start time",
        description="""Start time//Beginn""",
        mandatory=False,
        show_in_edit_views=False,
        section="Action Data",
    )

    action_end = PropertyTypeAssignment(
        code="ACTION_END",
        data_type="TIMESTAMP",
        property_label="End time",
        description="""End time//Ende""",
        mandatory=False,
        show_in_edit_views=False,
        section="Action Data",
    )


class IrCameraAcquisition(ParameterSet):
    defs = ObjectTypeDef(
        code="PARAMETER_SET.IR_CAMERA_ACQUISITION",
        description="""IR-camera acquisition parameters//Aufnahmeeinstellung IR-Kamera""",
        generated_code_prefix="PAR_SET.IR_CAM_ACQ",
    )

    integration_time_in_microsecond = PropertyTypeAssignment(
        code="INTEGRATION_TIME_IN_MICROSECOND",
        data_type="REAL",
        property_label="Integration time [µs]",
        description="""Integration time in µs//Integrationszeit in µs""",
        mandatory=False,
        show_in_edit_views=False,
        section="Parameters",
    )

    framerate_in_hertz = PropertyTypeAssignment(
        code="FRAMERATE_IN_HERTZ",
        data_type="REAL",
        property_label="Framerate [Hz]",
        description="""Framerate in Hz//Bildwiederholrate in Hz""",
        mandatory=True,
        show_in_edit_views=False,
        section="Parameters",
    )

    number_recorded_frames = PropertyTypeAssignment(
        code="NUMBER_RECORDED_FRAMES",
        data_type="INTEGER",
        property_label="Number of recorded frames",
        description="""Number of recorded frames//Anzahl der aufgenommenen Frames""",
        mandatory=True,
        show_in_edit_views=False,
        section="Parameters",
    )

    number_pretrigger_frames = PropertyTypeAssignment(
        code="NUMBER_PRETRIGGER_FRAMES",
        data_type="INTEGER",
        property_label="Number of recorded pretrigger frames",
        description="""Number of recorded pretrigger frames//Anzahl der Pretrigger Frames""",
        mandatory=True,
        show_in_edit_views=False,
        section="Parameters",
    )

    subframe = PropertyTypeAssignment(
        code="SUBFRAME",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="SUBFRAME_TYPE",
        property_label="Subframe type",
        description="""Subframe setting//Einstellung Subframe""",
        mandatory=True,
        show_in_edit_views=False,
        section="Parameters",
    )

    arbitrary_subframe_height_in_pixel = PropertyTypeAssignment(
        code="ARBITRARY_SUBFRAME_HEIGHT_IN_PIXEL",
        data_type="INTEGER",
        property_label="Height of arbitrary subframe [pix]",
        description="""Height of arbitrary subframe in pixel//Höhe des arbiträren Subframes in Pixel""",
        mandatory=False,
        show_in_edit_views=False,
        section="Parameters",
    )

    arbitrary_subframe_width_in_pixel = PropertyTypeAssignment(
        code="ARBITRARY_SUBFRAME_WIDTH_IN_PIXEL",
        data_type="INTEGER",
        property_label="Width of arbitrary subframe [pix]",
        description="""Width of arbitrary subframe in pixel//Breite des arbiträren Subframes in Pixel""",
        mandatory=False,
        show_in_edit_views=False,
        section="Parameters",
    )

    arbitrary_subframe_start_height_in_pixel = PropertyTypeAssignment(
        code="ARBITRARY_SUBFRAME_START_HEIGHT_IN_PIXEL",
        data_type="INTEGER",
        property_label="Start height of arbitrary subframe [pix]",
        description="""Start height of arbitrary subframe in pixel//Starthöhe des arbiträren Subframes in Pixel""",
        mandatory=False,
        show_in_edit_views=False,
        section="Parameters",
    )

    arbitrary_subframe_start_width_in_pixel = PropertyTypeAssignment(
        code="ARBITRARY_SUBFRAME_START_WIDTH_IN_PIXEL",
        data_type="INTEGER",
        property_label="Start Width of arbitrary subframe [pix]",
        description="""Start Width of arbitrary subframe in pixel//Startbreite des arbiträren Subframes in Pixel""",
        mandatory=False,
        show_in_edit_views=False,
        section="Parameters",
    )

    ir_camera_trigger_setting = PropertyTypeAssignment(
        code="IR_CAMERA.TRIGGER_SETTING",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="IR_CAMERA.TRIGGER_SETTING",
        property_label="Trigger setting",
        description="""Trigger setting//Einstellung Kameratrigger""",
        mandatory=True,
        show_in_edit_views=False,
        section="Parameters",
    )

    number_consecutive_acquisitons = PropertyTypeAssignment(
        code="NUMBER_CONSECUTIVE_ACQUISITONS",
        data_type="INTEGER",
        property_label="Number of consecutive acquisitions",
        description="""Number of consecutive acquisitions//Anzahl der konsekutiven Aufnahmen""",
        mandatory=True,
        show_in_edit_views=False,
        section="Parameters",
    )

    hardware_trigger_input = PropertyTypeAssignment(
        code="HARDWARE_TRIGGER_INPUT",
        data_type="VARCHAR",
        property_label="Utilized hardware trigger input",
        description="""Utilized hardware trigger input//Genutzter Input für Hardware-Trigger""",
        mandatory=False,
        show_in_edit_views=False,
        section="Parameters",
    )

    ad_channel_description = PropertyTypeAssignment(
        code="AD_CHANNEL_DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description of AD-channel data",
        description="""Description of AD-channel data//Beschreibung der AD-Kanal Signale""",
        mandatory=False,
        show_in_edit_views=False,
        section="Parameters",
    )

    nuc_performed = PropertyTypeAssignment(
        code="NUC_PERFORMED",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="NUC_PERFORMED",
        property_label="NUC-performed",
        description="""NUC-performed//NUC-durchgeführt""",
        mandatory=True,
        show_in_edit_views=False,
        section="Parameters",
    )

    used_calibration_range_min_in_celsius = PropertyTypeAssignment(
        code="USED_CALIBRATION_RANGE_MIN_IN_CELSIUS",
        data_type="REAL",
        property_label="Lower limit of utilized calibration range [°C]",
        description="""Lower limit of utilized calibration range in °C//Unteres Limit des genutzten Kalibrierbereichs in °C""",
        mandatory=False,
        show_in_edit_views=False,
        section="Parameters",
    )

    used_calibration_range_max_in_celsius = PropertyTypeAssignment(
        code="USED_CALIBRATION_RANGE_MAX_IN_CELSIUS",
        data_type="REAL",
        property_label="Upper limit of utilized calibration range [°C]",
        description="""Upper limit of utilized calibration range in °C//Oberes Limit des genutzten Kalibrierbereichs in °C""",
        mandatory=False,
        show_in_edit_views=False,
        section="Parameters",
    )


class ThermographySetup(ParameterSet):
    defs = ObjectTypeDef(
        code="PARAMETER_SET.THERMOGRAPHY_SETUP",
        description="""Parameters describing the thermographic measurement setup//Parameter zur Beschreibung des Thermografie-Messaufbau""",
        generated_code_prefix="PAR_SET.THERM_SET",
    )

    camera_distance_in_millimeter = PropertyTypeAssignment(
        code="CAMERA_DISTANCE_IN_MILLIMETER",
        data_type="REAL",
        property_label="Distance camera -> sample [mm]",
        description="""Distance camera -> sample in mm//Abstand Kamera zu Sample in mm""",
        mandatory=True,
        show_in_edit_views=False,
        section="Parameters",
    )

    heat_source_distance_in_millimeter = PropertyTypeAssignment(
        code="HEAT_SOURCE_DISTANCE_IN_MILLIMETER",
        data_type="REAL",
        property_label="Distance heat source -> sample [mm]",
        description="""Distance heat source -> sample in mm//Abstand Wärmequelle zu Sample in mm""",
        mandatory=False,
        show_in_edit_views=False,
        section="Parameters",
    )

    sample_treatment = PropertyTypeAssignment(
        code="SAMPLE_TREATMENT",
        data_type="MULTILINE_VARCHAR",
        property_label="Sample treatment",
        description="""Sample treatment//Oberflächenzustand des Sample""",
        mandatory=False,
        show_in_edit_views=False,
        section="Parameters",
    )

    setup_configuration = PropertyTypeAssignment(
        code="SETUP_CONFIGURATION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="THERMOGRAPHIC_SETUP_CONFIG",
        property_label="Setup configuration",
        description="""Setup configuration//Messanordnung""",
        mandatory=True,
        show_in_edit_views=False,
        section="Parameters",
    )

    heat_source_orientation = PropertyTypeAssignment(
        code="HEAT_SOURCE_ORIENTATION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="THERMOGRAPHIC_SETUP_HS_ORIENT",
        property_label="Orientation of the heat source w.r.t. the camera",
        description="""Orientation of the heat source w.r.t. the camera//Ausrichtung der Wärmequelle zur Kamera""",
        mandatory=False,
        show_in_edit_views=False,
        section="Parameters",
    )


class ThermographyHeating(ParameterSet):
    defs = ObjectTypeDef(
        code="PARAMETER_SET.THERMOGRAPHY_HEATING",
        description="""Heating parameters for active thermography//Erwärmungsparameter für die aktive Thermografie""",
        generated_code_prefix="PAR_SET.THERM_HEAT",
    )

    temporal_heating_structure = PropertyTypeAssignment(
        code="TEMPORAL_HEATING_STRUCTURE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="TEMPORAL_HEATING_STRUCTURE",
        property_label="Temporal Structure of the heating",
        description="""Temporal Structure of the heating//Zeitliche Struktur der Erwärmung""",
        mandatory=True,
        show_in_edit_views=False,
        section="Parameters",
    )

    heating_principle = PropertyTypeAssignment(
        code="HEATING_PRINCIPLE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="HEATING_PRINCIPLE",
        property_label="Heating Principle",
        description="""Heating Principle//Prinzip der Erwärmung""",
        mandatory=True,
        show_in_edit_views=False,
        section="Parameters",
    )

    power_in_watt = PropertyTypeAssignment(
        code="POWER_IN_WATT",
        data_type="REAL",
        property_label="Power setting of the heating element [W]",
        description="""Power setting of the heating element in W//Eingestellte Erwärmungsleistung Leistung in W""",
        mandatory=False,
        show_in_edit_views=False,
        section="Parameters",
    )

    pulse_energy_in_joule = PropertyTypeAssignment(
        code="PULSE_ENERGY_IN_JOULE",
        data_type="REAL",
        property_label="Pulse energy setting of the heating element [J]",
        description="""Pulse energy setting of the heating element in J //Eingetragene Erwärmungsenergie in J""",
        mandatory=False,
        show_in_edit_views=False,
        section="Parameters",
    )

    heating_temperature_in_celsius = PropertyTypeAssignment(
        code="HEATING_TEMPERATURE_IN_CELSIUS",
        data_type="REAL",
        property_label="Temperature of the heating element [°C]",
        description="""Temperature of the heating element in °C//Eingestellte Temperatur der Erwärmung in °C""",
        mandatory=False,
        show_in_edit_views=False,
        section="Parameters",
    )

    heating_duration_in_seconds = PropertyTypeAssignment(
        code="HEATING_DURATION_IN_SECONDS",
        data_type="REAL",
        property_label="Duration of the heating [s]",
        description="""Duration of the heating in s//Dauer der Erwärmung in s""",
        mandatory=False,
        show_in_edit_views=False,
        section="Parameters",
    )

    heating_frequency_in_hertz = PropertyTypeAssignment(
        code="HEATING_FREQUENCY_IN_HERTZ",
        data_type="REAL",
        property_label="Frequency of the heating [Hz]",
        description="""Frequency of the heating in Hz//Frequenz der Erwärmung in Hz""",
        mandatory=False,
        show_in_edit_views=False,
        section="Parameters",
    )

    heating_area_desc = PropertyTypeAssignment(
        code="HEATING_AREA_DESC",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="HEATING_AREA_DESC",
        property_label="Area of effect of the heating",
        description="""Area of effect of the heating//Effektive Erwärmungsfläche""",
        mandatory=True,
        show_in_edit_views=False,
        section="Parameters",
    )

    heating_height_in_millimeter = PropertyTypeAssignment(
        code="HEATING_HEIGHT_IN_MILLIMETER",
        data_type="REAL",
        property_label="Height of the heating area [mm]",
        description="""Height of the heating area in mm//Höhe der erwärmten Fläche in mm""",
        mandatory=False,
        show_in_edit_views=False,
        section="Parameters",
    )

    heating_width_in_millimeter = PropertyTypeAssignment(
        code="HEATING_WIDTH_IN_MILLIMETER",
        data_type="REAL",
        property_label="Width of the heating area [mm]",
        description="""Width of the heating area in mm//Breite der erwärmten Fläche in mm""",
        mandatory=False,
        show_in_edit_views=False,
        section="Parameters",
    )


class BamLaboratory(EnvironmentalConditions):
    defs = ObjectTypeDef(
        code="ENVIRONMENTAL_CONDITIONS.BAM_LABORATORY",
        description="""Environmental conditions in a BAM Laboratory//Umgebungsbedingungen im Labor der BAM""",
        generated_code_prefix="ENV_COND.BAM_LAB",
    )

    bam_room = PropertyTypeAssignment(
        code="BAM_ROOM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_ROOM",
        property_label="BAM Room",
        description="""BAM Room//BAM Raum""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_floor = PropertyTypeAssignment(
        code="BAM_FLOOR",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_FLOOR",
        property_label="BAM Floor",
        description="""BAM Floor//BAM Etage""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_house = PropertyTypeAssignment(
        code="BAM_HOUSE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_HOUSE",
        property_label="BAM House",
        description="""BAM House//BAM Haus""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_location = PropertyTypeAssignment(
        code="BAM_LOCATION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_LOCATION",
        property_label="BAM Location",
        description="""BAM Location//BAM Liegenschaft""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_location_complete = PropertyTypeAssignment(
        code="BAM_LOCATION_COMPLETE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_LOCATION_COMPLETE",
        property_label="Complete BAM Location",
        description="""Complete BAM location (up to room level)//Komplette BAM-Ortsangabe (bis Raumlevel)""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )


class Outdoor(EnvironmentalConditions):
    defs = ObjectTypeDef(
        code="ENVIRONMENTAL_CONDITIONS.OUTDOOR",
        description="""Environmental conditions for outside measurements//Umgebungsbedingungen für Feldmessungen""",
        generated_code_prefix="ENV_COND.OUT",
    )

    wind_speed_in_meter_per_second = PropertyTypeAssignment(
        code="WIND_SPEED_IN_METER_PER_SECOND",
        data_type="REAL",
        property_label="Wind speed [m/s]",
        description="""Wind speed in m/s//Windgeschwindigkeit in m/s""",
        mandatory=False,
        show_in_edit_views=False,
        section="Atmospheric Conditions",
    )

    wind_direction = PropertyTypeAssignment(
        code="WIND_DIRECTION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="WIND_DIRECTION",
        property_label="Wind direction",
        description="""Wind direction//Windrichtung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Atmospheric Conditions",
    )

    sun_irradiance_in_watt_per_meter_squared = PropertyTypeAssignment(
        code="SUN_IRRADIANCE_IN_WATT_PER_METER_SQUARED",
        data_type="REAL",
        property_label="Sun irradiance [W/m^2]",
        description="""Sun irradiance in W/m^2//Sonneneinstrahlung in W/m^2""",
        mandatory=False,
        show_in_edit_views=False,
        section="Weather Conditions",
    )

    weather_condition = PropertyTypeAssignment(
        code="WEATHER_CONDITION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="WEATHER_CONDITION",
        property_label="Weather",
        description="""Weather//Wetter""",
        mandatory=False,
        show_in_edit_views=False,
        section="Weather Conditions",
    )

    location_latitude_in_degrees = PropertyTypeAssignment(
        code="LOCATION_LATITUDE_IN_DEGREES",
        data_type="REAL",
        property_label="Location latitude [°]",
        description="""Location latitude in °//Breitengrad des Messortes in °""",
        mandatory=False,
        show_in_edit_views=False,
        section="Location",
    )

    location_longitude_in_degrees = PropertyTypeAssignment(
        code="LOCATION_LONGITUDE_IN_DEGREES",
        data_type="REAL",
        property_label="Location longitude [°]",
        description="""Location longitude in °//Längengrad des Messortes in °""",
        mandatory=False,
        show_in_edit_views=False,
        section="Location",
    )

    location_address = PropertyTypeAssignment(
        code="LOCATION_ADDRESS",
        data_type="VARCHAR",
        property_label="Location address",
        description="""Location address//Adresse des Messortes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Location",
    )


class FlashLamp(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.FLASH_LAMP",
        description="""Flash lamp//Blitzlampe""",
        generated_code_prefix="INS.FLA_LAM",
    )

    max_pulse_energy_in_joule = PropertyTypeAssignment(
        code="MAX_PULSE_ENERGY_IN_JOULE",
        data_type="REAL",
        property_label="Maximum pulse energy [J]",
        description="""Maximum pulse energy in J//Maximale Pulsenergie in J""",
        mandatory=True,
        show_in_edit_views=False,
        section="Flash Lamp Specifics",
    )

    flash_lamp_shape = PropertyTypeAssignment(
        code="FLASH_LAMP_SHAPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="FLASH_LAMP_SHAPE",
        property_label="Lamp shape",
        description="""Lamp shape//Lampenform""",
        mandatory=True,
        show_in_edit_views=False,
        section="Flash Lamp Specifics",
    )


class ObjectiveSpacer(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.OBJECTIVE_SPACER",
        description="""Objective spacer//Abstandsring""",
        generated_code_prefix="INS.OBJ_SPA",
    )

    thickness_in_millimeter = PropertyTypeAssignment(
        code="THICKNESS_IN_MILLIMETER",
        data_type="REAL",
        property_label="Thickness [mm]",
        description="""Thickness of the spacer in mm//Dicke des Abstandsringes in mm""",
        mandatory=True,
        show_in_edit_views=False,
        section="Properties",
    )


class ThermographicMeasurement(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.THERMOGRAPHIC_MEASUREMENT",
        description="""Thermographic Measurement//Thermografiemessung""",
        generated_code_prefix="EXP_STEP.THE_MEA",
    )

    associated_project = PropertyTypeAssignment(
        code="ASSOCIATED_PROJECT",
        data_type="OBJECT",
        object_code="PROJECT",
        property_label="Associated project",
        description="""Associated project//Assoziiertes Projekt""",
        mandatory=False,
        show_in_edit_views=False,
        section="References",
    )


class Named(SampleNdt):
    defs = ObjectTypeDef(
        code="SAMPLE_NDT.NAMED",
        description="""Named sample used to validate NDT-methods//Benanntes Sample zur Validierung von ZfP-Verfahren""",
        generated_code_prefix="SAM_NDT_NAM",
    )

    sample_id = PropertyTypeAssignment(
        code="SAMPLE_ID",
        data_type="VARCHAR",
        property_label="Sample ID",
        description="""Sample ID//Identifikationsnummer""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    material = PropertyTypeAssignment(
        code="MATERIAL",
        data_type="VARCHAR",
        property_label="Material",
        description="""Material//Material""",
        mandatory=True,
        show_in_edit_views=False,
        section="Properties",
    )

    defect_description = PropertyTypeAssignment(
        code="DEFECT_DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Defect description",
        description="""Defect Description//Beschreibung der Defekte""",
        mandatory=True,
        show_in_edit_views=False,
        section="Properties",
    )

    size_height_in_millimeter = PropertyTypeAssignment(
        code="SIZE_HEIGHT_IN_MILLIMETER",
        data_type="REAL",
        property_label="Height [mm]",
        description="""Height in mm//Höhe in mm""",
        mandatory=True,
        show_in_edit_views=False,
        section="Properties",
    )

    size_width_in_millimeter = PropertyTypeAssignment(
        code="SIZE_WIDTH_IN_MILLIMETER",
        data_type="REAL",
        property_label="Width [mm]",
        description="""Width in mm//Breite in mm""",
        mandatory=True,
        show_in_edit_views=False,
        section="Properties",
    )

    size_thickness_in_millimeter = PropertyTypeAssignment(
        code="SIZE_THICKNESS_IN_MILLIMETER",
        data_type="REAL",
        property_label="Thickness [mm]",
        description="""Thickness in mm//Dicke in mm""",
        mandatory=True,
        show_in_edit_views=False,
        section="Properties",
    )

    associated_project = PropertyTypeAssignment(
        code="ASSOCIATED_PROJECT",
        data_type="OBJECT",
        object_code="PROJECT",
        property_label="Associated project",
        description="""Associated project//Assoziiertes Projekt""",
        mandatory=False,
        show_in_edit_views=False,
        section="Properties",
    )

    responsible_person = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Responsible person",
        description="""Responsible person//Verantwortliche Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    co_responsible_person = PropertyTypeAssignment(
        code="CO_RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Co-responsible person",
        description="""Co-responsible person//Weitere verantwortliche Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )


class SaxsMeasurement(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.SAXS_MEASUREMENT",
        description="""Metadata of a single Small-Angle Scattering (SAXS) measurement//Metadaten einer einzelnen Kleinwinkelstreuungmessung""",
        generated_code_prefix="EXP.SXSM_",
    )

    measurement_id = PropertyTypeAssignment(
        code="MEASUREMENT_ID",
        data_type="INTEGER",
        property_label="Measurement ID",
        description="""Div. internal measurement ID//FB-interne Messdatennummer""",
        mandatory=False,
        show_in_edit_views=False,
        section="Experiment Details",
    )

    measurement_date = PropertyTypeAssignment(
        code="MEASUREMENT_DATE",
        data_type="DATE",
        property_label="Measurement Date",
        description="""Measurement Date//Messdatum""",
        mandatory=True,
        show_in_edit_views=False,
        section="Experiment Details",
    )

    cell_temperature_in_celsius = PropertyTypeAssignment(
        code="CELL_TEMPERATURE_IN_CELSIUS",
        data_type="REAL",
        property_label="Cell Temperature [°C]",
        description="""Measurement cell temperature in °C // Temperatur der Messzelle in °C""",
        mandatory=True,
        show_in_edit_views=False,
        section="Experiment Details",
    )

    exposure_time_in_seconds = PropertyTypeAssignment(
        code="EXPOSURE_TIME_IN_SECONDS",
        data_type="REAL",
        property_label="Exposure time [s]",
        description="""Exposure time in seconds//Belichtungszeit in Sekunden""",
        mandatory=True,
        show_in_edit_views=False,
        section="Experiment Details",
    )

    frame_count = PropertyTypeAssignment(
        code="FRAME_COUNT",
        data_type="INTEGER",
        property_label="Number of frames",
        description="""Number of frames//Anzahl von Aufnahmen""",
        mandatory=True,
        show_in_edit_views=False,
        section="Experiment Details",
    )


class LocalWorkstation(Instrument):
    defs = ObjectTypeDef(
        code="INSTRUMENT.LOCAL_WORKSTATION",
        description="""BAM local workstation//BAM Arbeitsstation""",
        generated_code_prefix="INS.LOC_WOR",
    )

    operating_system = PropertyTypeAssignment(
        code="OPERATING_SYSTEM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="OPERATING_SYSTEM",
        property_label="Operating System",
        description="""Operating System (OS)//Betriebssystem""",
        mandatory=False,
        show_in_edit_views=False,
        section="Technical Information",
    )


class Lammps(PyironJob):
    defs = ObjectTypeDef(
        code="PYIRON_JOB.LAMMPS",
        description="""LAMMPS pyiron job//LAMMPS pyiron Job""",
        generated_code_prefix="PYI_JOB.LMP",
    )

    atomistic_calc_type = PropertyTypeAssignment(
        code="ATOMISTIC_CALC_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="ATOMISTIC_CALC_TYPE",
        property_label="Atomistic Calculation Type",
        description="""Type of atomistic calculation//Art der atomistischen Berechnung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    periodic_boundary_x = PropertyTypeAssignment(
        code="PERIODIC_BOUNDARY_X",
        data_type="BOOLEAN",
        property_label="Simulation Periodicity in X-Direction",
        description="""Simulation periodicity in X-direction//Periodizität der Simulation in X-Richtung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    periodic_boundary_y = PropertyTypeAssignment(
        code="PERIODIC_BOUNDARY_Y",
        data_type="BOOLEAN",
        property_label="Simulation Periodicity in Y-Direction",
        description="""Simulation periodicity in Y-direction//Periodizität der Simulation in Y-Richtung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    periodic_boundary_z = PropertyTypeAssignment(
        code="PERIODIC_BOUNDARY_Z",
        data_type="BOOLEAN",
        property_label="Simulation Periodicity in Z-Direction",
        description="""Simulation periodicity in Z-direction//Periodizität der Simulation in Z-Richtung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    atom_cell_vol_relax = PropertyTypeAssignment(
        code="ATOM_CELL_VOL_RELAX",
        data_type="BOOLEAN",
        property_label="Cell Volume Relaxation",
        description="""Degrees of freedom - Cell volume relaxation//Freiheitsgrade - Zellvolumenrelaxation""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    atom_cell_shp_relax = PropertyTypeAssignment(
        code="ATOM_CELL_SHP_RELAX",
        data_type="BOOLEAN",
        property_label="Cell Shape Relaxation",
        description="""Degrees of freedom - Cell shape relaxation//Freiheitsgrade - Zellformrelaxation""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    atom_pos_relax = PropertyTypeAssignment(
        code="ATOM_POS_RELAX",
        data_type="BOOLEAN",
        property_label="Atomic Position Relaxation",
        description="""Degrees of freedom - Atomic position relaxation//Freiheitsgrade - Atomare Positionsrelaxation""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    atom_md_ensemble = PropertyTypeAssignment(
        code="ATOM_MD_ENSEMBLE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="THERMODYN_ENSEMBLE",
        property_label="Statistical Ensemble",
        description="""Statistical ensemble set in the simulation//Statistisches Ensemble in der Simulation""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    atom_ionic_min_algo = PropertyTypeAssignment(
        code="ATOM_IONIC_MIN_ALGO",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="MINIMIZATION_ALGO",
        property_label="Minimization Algorithm for Ionic Steps",
        description="""Minimization algorithm for ionic steps//Minimalisierungsalgorithmus zur ionischen Schritten""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    atom_md_time_stp_in_ps = PropertyTypeAssignment(
        code="ATOM_MD_TIME_STP_IN_PS",
        data_type="REAL",
        property_label="Time Step Size [ps]",
        description="""Time step size [ps]//Zeitschrittweite [ps]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Input",
    )

    atom_sim_time_ps_in_ps = PropertyTypeAssignment(
        code="ATOM_SIM_TIME_PS_IN_PS",
        data_type="REAL",
        property_label="Simulation Time [ps]",
        description="""Simulated timespan [ps]// Simulierte Zeitspanne [ps]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Input",
    )

    atom_md_langevin = PropertyTypeAssignment(
        code="ATOM_MD_LANGEVIN",
        data_type="BOOLEAN",
        property_label="Langevin Dynamics",
        description="""Use of Langevin dynamics//Verwendung der Langevin-Dynamik""",
        mandatory=False,
        show_in_edit_views=False,
        section="Input",
    )

    max_iters = PropertyTypeAssignment(
        code="MAX_ITERS",
        data_type="INTEGER",
        property_label="Maximum Iterations",
        description="""Maximum number of iterations//Maximale Anzahl von Iterationen""",
        mandatory=False,
        show_in_edit_views=False,
        section="Input",
    )

    atom_e_tol_ion_in_ev = PropertyTypeAssignment(
        code="ATOM_E_TOL_ION_IN_EV",
        data_type="REAL",
        property_label="Ionic Energy Tolerance [eV]",
        description="""Energy tolerance for ionic minimization [eV]//Energietoleranz zur ionische Minimierung [eV]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Input",
    )

    atom_f_tol_in_ev_a = PropertyTypeAssignment(
        code="ATOM_F_TOL_IN_EV_A",
        data_type="REAL",
        property_label="Ionic Force Tolerance [eV/Å]",
        description="""Force tolerance for minimization [eV/Å]//Krafttoleranz für Minimierung [eV/Å]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Input",
    )

    atom_md_init_temp_in_k = PropertyTypeAssignment(
        code="ATOM_MD_INIT_TEMP_IN_K",
        data_type="REAL",
        property_label="Initial Temperature [K]",
        description="""Initial temperature [K]//Anfangstemperatur [K]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Input",
    )

    atom_md_init_press_in_gpa = PropertyTypeAssignment(
        code="ATOM_MD_INIT_PRESS_IN_GPA",
        data_type="REAL",
        property_label="Initial Pressure [GPa]",
        description="""Initial pressure [GPa]//Anfangsdruck [GPa]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Input",
    )

    atom_md_targ_temp_in_k = PropertyTypeAssignment(
        code="ATOM_MD_TARG_TEMP_IN_K",
        data_type="REAL",
        property_label="Target Temperature [K]",
        description="""Target temperature [K]//Zieltemperatur [K]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Input",
    )

    atom_targ_press_in_gpa = PropertyTypeAssignment(
        code="ATOM_TARG_PRESS_IN_GPA",
        data_type="REAL",
        property_label="Target Pressure [GPa]",
        description="""Target pressure [GPa]//Ziel-Druck [GPa]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Input",
    )

    atom_ionic_steps = PropertyTypeAssignment(
        code="ATOM_IONIC_STEPS",
        data_type="INTEGER",
        property_label="N Ionic Steps",
        description="""Number of ionic steps//Anzahl der Ionischen Schritten""",
        mandatory=False,
        show_in_edit_views=False,
        section="Output",
    )

    atom_md_avg_temp_in_k = PropertyTypeAssignment(
        code="ATOM_MD_AVG_TEMP_IN_K",
        data_type="REAL",
        property_label="Average Temperature [K]",
        description="""Average temperature over time steps [K]//Durchschnittstemperatur [K]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Output",
    )

    atom_avg_press_in_gpa = PropertyTypeAssignment(
        code="ATOM_AVG_PRESS_IN_GPA",
        data_type="REAL",
        property_label="Average Pressure [GPa]",
        description="""Average pressure over time steps [GPa]//Durchschnittsdruck [GPa]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Output",
    )

    atom_fin_tot_eng_in_ev = PropertyTypeAssignment(
        code="ATOM_FIN_TOT_ENG_IN_EV",
        data_type="REAL",
        property_label="Final Total Energy [eV]",
        description="""Final Total Energy [eV]//Letzte Gesamtenergie [eV]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Output",
    )

    atom_avg_tot_eng_in_ev = PropertyTypeAssignment(
        code="ATOM_AVG_TOT_ENG_IN_EV",
        data_type="REAL",
        property_label="Average Total Energy [eV]",
        description="""Average Total Energy over time steps [eV]//Durchschnittsgesamtenergie [eV]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Output",
    )

    atom_fin_vol_in_a3 = PropertyTypeAssignment(
        code="ATOM_FIN_VOL_IN_A3",
        data_type="REAL",
        property_label="Final Volume [Å^3]",
        description="""Final Volume [Å^3]//Letztes Volumen [Å^3]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Output",
    )

    atom_avg_vol_in_a3 = PropertyTypeAssignment(
        code="ATOM_AVG_VOL_IN_A3",
        data_type="REAL",
        property_label="Average Volume [Å^3]",
        description="""Average Volume over time steps [Å^3]//Durchschnittliches Volumen [Å^3]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Output",
    )

    atom_fin_pot_eng_in_ev = PropertyTypeAssignment(
        code="ATOM_FIN_POT_ENG_IN_EV",
        data_type="REAL",
        property_label="Final Potential Energy [eV]",
        description="""Final Potential Energy [eV]//Letzte potenzielle Energie [eV]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Output",
    )

    atom_avg_pot_eng_in_ev = PropertyTypeAssignment(
        code="ATOM_AVG_POT_ENG_IN_EV",
        data_type="REAL",
        property_label="Average Potential Energy [eV]",
        description="""Average Potential Energy over time steps (eV)//Durchschnittliche potenzielle Energie [eV]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Output",
    )

    atom_fin_fnorm_in_ev_a = PropertyTypeAssignment(
        code="ATOM_FIN_FNORM_IN_EV_A",
        data_type="REAL",
        property_label="Final Force Norm [eV/Å]",
        description="""Final Force norm [eV/Å]//Letztes Kraftnorm [eV/Å]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Output",
    )

    atom_avg_fnorm_in_ev_a = PropertyTypeAssignment(
        code="ATOM_AVG_FNORM_IN_EV_A",
        data_type="REAL",
        property_label="Average Force Norm [eV/Å]",
        description="""Average Force norm over time steps [eV/Å]//Durchschnittskraftnorm [eV/Å]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Output",
    )

    atom_force_max_in_ev_a = PropertyTypeAssignment(
        code="ATOM_FORCE_MAX_IN_EV_A",
        data_type="REAL",
        property_label="Final Maximum Force Component [eV/Å]",
        description="""Final maximum force component [eV/Å]//Letzte maximale Kraftkomponente [eV/Å]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Output",
    )


class Murnaghan(PyironJob):
    defs = ObjectTypeDef(
        code="PYIRON_JOB.MURNAGHAN",
        description="""Murnaghan pyiron job//Murnaghan pyiron Job""",
        generated_code_prefix="PYI_JOB.MRN",
    )

    murn_eqn_of_state = PropertyTypeAssignment(
        code="MURN_EQN_OF_STATE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="MURN_EQN_OF_STATE",
        property_label="Equation of State",
        description="""Equation of state used for fit//Für das Fitting verwendete Zustandsgleichung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    murn_fit_eqn_order = PropertyTypeAssignment(
        code="MURN_FIT_EQN_ORDER",
        data_type="INTEGER",
        property_label="Fit Order (if Polynomial)",
        description="""Fit order (if polynomial)//Grad des Polynoms""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    murn_strain_axes = PropertyTypeAssignment(
        code="MURN_STRAIN_AXES",
        data_type="VARCHAR",
        property_label="Strain Axes",
        description="""Axes along which cell is strained//Achsen, entlang derer die Zelle belastet wird""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    murn_n_data_points = PropertyTypeAssignment(
        code="MURN_N_DATA_POINTS",
        data_type="INTEGER",
        property_label="Number of Data Points",
        description="""Number of data points//Anzahl der Datenpunkte""",
        mandatory=False,
        show_in_edit_views=False,
        section="Input",
    )

    murn_strainvol_range = PropertyTypeAssignment(
        code="MURN_STRAINVOL_RANGE",
        data_type="REAL",
        property_label="Volume Range (Fractional)",
        description="""Volume range (fractional)//Volumenbereich (fraktioniert)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Input",
    )

    atom_equil_k_mod_in_gpa = PropertyTypeAssignment(
        code="ATOM_EQUIL_K_MOD_IN_GPA",
        data_type="REAL",
        property_label="Equilibrium Bulk Modulus [GPa]",
        description="""Equilibrium bulk modulus [GPa]//Kompressionsmodul im  Gleichgewicht [GPa]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Output",
    )

    atom_equil_toteng_in_ev = PropertyTypeAssignment(
        code="ATOM_EQUIL_TOTENG_IN_EV",
        data_type="REAL",
        property_label="Equilibrium Total Energy [eV]",
        description="""Equilibrium total energy [eV]//Gesamtenergie im Gleichgewicht [eV]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Output",
    )

    atom_equil_vol_in_a3 = PropertyTypeAssignment(
        code="ATOM_EQUIL_VOL_IN_A3",
        data_type="REAL",
        property_label="Equilibrium Volume [Å^3]",
        description="""Equilibrium volume [Å^3]//Volumen im Gleichgewicht [Å^3]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Output",
    )


class Vasp(PyironJob):
    defs = ObjectTypeDef(
        code="PYIRON_JOB.VASP",
        description="""VASP pyiron job//VASP pyiron Job""",
        generated_code_prefix="PYI_JOB.VASP",
    )

    atomistic_calc_type = PropertyTypeAssignment(
        code="ATOMISTIC_CALC_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="ATOMISTIC_CALC_TYPE",
        property_label="Atomistic Calculation Type",
        description="""Type of atomistic calculation//Art der atomistischen Berechnung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    atom_wavefunc_reuse = PropertyTypeAssignment(
        code="ATOM_WAVEFUNC_REUSE",
        data_type="BOOLEAN",
        property_label="Wavefunctions from a previous run?",
        description="""Are the initial wavefunctions from a previous calculation?//Stammen die Anfangswellenfunktionen aus einer früheren Berechnung?""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    atom_chgdens_reuse = PropertyTypeAssignment(
        code="ATOM_CHGDENS_REUSE",
        data_type="BOOLEAN",
        property_label="Charge density from a previous run?",
        description="""Are the initial charge densities from a previous calculation?//Stammen die Anfangsladungsdichten aus einer früheren Berechnung?""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    atom_cell_vol_relax = PropertyTypeAssignment(
        code="ATOM_CELL_VOL_RELAX",
        data_type="BOOLEAN",
        property_label="Cell Volume Relaxation",
        description="""Degrees of freedom - Cell volume relaxation//Freiheitsgrade - Zellvolumenrelaxation""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    atom_cell_shp_relax = PropertyTypeAssignment(
        code="ATOM_CELL_SHP_RELAX",
        data_type="BOOLEAN",
        property_label="Cell Shape Relaxation",
        description="""Degrees of freedom - Cell shape relaxation//Freiheitsgrade - Zellformrelaxation""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    atom_pos_relax = PropertyTypeAssignment(
        code="ATOM_POS_RELAX",
        data_type="BOOLEAN",
        property_label="Atomic Position Relaxation",
        description="""Degrees of freedom - Atomic position relaxation//Freiheitsgrade - Atomare Positionsrelaxation""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    atom_xc_functional = PropertyTypeAssignment(
        code="ATOM_XC_FUNCTIONAL",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="ATOM_XC_FUNCTIONAL",
        property_label="XC functional",
        description="""Exchange-correlation functional//Austausch-Korrelations-Funktional""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    atom_xc_u_correction = PropertyTypeAssignment(
        code="ATOM_XC_U_CORRECTION",
        data_type="BOOLEAN",
        property_label="U Correction?",
        description="""Are U corrections included?//Sind U-Korrekturen enthalten?""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    electronic_smearing = PropertyTypeAssignment(
        code="ELECTRONIC_SMEARING",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="ELECTRONIC_SMEARING",
        property_label="Partial Occupancies",
        description="""Partial occupancies//Teilbesetzungen""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    atom_ionic_min_algo = PropertyTypeAssignment(
        code="ATOM_IONIC_MIN_ALGO",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="MINIMIZATION_ALGO",
        property_label="Minimization Algorithm for Ionic Steps",
        description="""Minimization algorithm for ionic steps//Minimalisierungsalgorithmus zur ionischen Schritten""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    atom_elec_min_algo = PropertyTypeAssignment(
        code="ATOM_ELEC_MIN_ALGO",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="MINIMIZATION_ALGO",
        property_label="Minimization Algorithm for Electronic Steps",
        description="""Minimization algorithm for electronic steps//Minimalisierungsalgorithmus zur elektronischen Schritten""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    atom_spin_polarized = PropertyTypeAssignment(
        code="ATOM_SPIN_POLARIZED",
        data_type="BOOLEAN",
        property_label="Calculation Spin-polarized?",
        description="""Is the calculation spin-polarized?//Ist die Berechnung spinpolarisiert?""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    atom_non_coll_mag = PropertyTypeAssignment(
        code="ATOM_NON_COLL_MAG",
        data_type="BOOLEAN",
        property_label="Non-collinear Magnetism?",
        description="""Are the magnetic moments non-collinear?//Sind die magnetischen Momente nicht kollinear?""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    atom_kpoint_type = PropertyTypeAssignment(
        code="ATOM_KPOINT_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="ATOM_KPOINT_TYPE",
        property_label="K-points Specification Type",
        description="""K-points specification type//K-Punkte-Spezifikation Typ""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    atom_kpt_gamma_cent = PropertyTypeAssignment(
        code="ATOM_KPT_GAMMA_CENT",
        data_type="BOOLEAN",
        property_label="Gamma-centered?",
        description="""Are the K-points centered around the gamma point?//Sind die k-Punkte um den Gamma-Punkt zentriert?""",
        mandatory=False,
        show_in_edit_views=False,
        section="Method Specific",
    )

    atomistic_n_kpt_x = PropertyTypeAssignment(
        code="ATOMISTIC_N_KPT_X",
        data_type="INTEGER",
        property_label="Number of K-points in x-direction",
        description="""Number of K-points in x-direction//Anzahl der K-Punkte in x-Richtung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Input",
    )

    atomistic_n_kpt_y = PropertyTypeAssignment(
        code="ATOMISTIC_N_KPT_Y",
        data_type="INTEGER",
        property_label="Number of K-points in y-direction",
        description="""Number of K-points in y-direction//Anzahl der K-Punkte in y-Richtung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Input",
    )

    atomistic_n_kpt_z = PropertyTypeAssignment(
        code="ATOMISTIC_N_KPT_Z",
        data_type="INTEGER",
        property_label="Number of K-points in z-direction",
        description="""Number of K-points in z-direction//Anzahl der K-Punkte in z-Richtung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Input",
    )

    atomistic_kpt_spacin_in_1_a = PropertyTypeAssignment(
        code="ATOMISTIC_KPT_SPACIN_IN_1_A",
        data_type="REAL",
        property_label="K-spacing [1/Å]",
        description="""K-spacing value [1/Å]//K-Abstandswert""",
        mandatory=False,
        show_in_edit_views=False,
        section="Input",
    )

    atomistic_kpt_full = PropertyTypeAssignment(
        code="ATOMISTIC_KPT_FULL",
        data_type="MULTILINE_VARCHAR",
        property_label="Full list of K-points",
        description="""Full list of K-points//Vollständige Liste der K-Punkte""",
        mandatory=False,
        show_in_edit_views=False,
        section="Input",
    )

    atom_e_tol_ion_in_ev = PropertyTypeAssignment(
        code="ATOM_E_TOL_ION_IN_EV",
        data_type="REAL",
        property_label="Ionic Energy Tolerance [eV]",
        description="""Energy tolerance for ionic minimization [eV]//Energietoleranz zur ionische Minimierung [eV]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Input",
    )

    atom_el_e_tol_in_ev = PropertyTypeAssignment(
        code="ATOM_EL_E_TOL_IN_EV",
        data_type="REAL",
        property_label="Electronic Energy Tolerance [eV]",
        description="""Energy tolerance for electronic minimization [eV]//Energietoleranz zur elektronische Minimierung [eV]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Input",
    )

    atom_f_tol_in_ev_a = PropertyTypeAssignment(
        code="ATOM_F_TOL_IN_EV_A",
        data_type="REAL",
        property_label="Ionic Force Tolerance [eV/Å]",
        description="""Force tolerance for minimization [eV/Å]//Krafttoleranz für Minimierung [eV/Å]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Input",
    )

    atom_e_cutoff_in_ev = PropertyTypeAssignment(
        code="ATOM_E_CUTOFF_IN_EV",
        data_type="REAL",
        property_label="Energy Cutoff [eV]",
        description="""Energy cutoff for wavefunctions [eV]//Energiegrenzwert für Wellenfunktionen [eV]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Input",
    )

    atom_sigma_in_ev = PropertyTypeAssignment(
        code="ATOM_SIGMA_IN_EV",
        data_type="REAL",
        property_label="Sigma Value [eV]",
        description="""Sigma value [eV]//Sigma-Wert [eV]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Input",
    )

    atomistic_ionic_steps = PropertyTypeAssignment(
        code="ATOMISTIC_IONIC_STEPS",
        data_type="INTEGER",
        property_label="N Ionic Steps",
        description="""Number of ionic steps//Anzahl der Ionischen Schritten""",
        mandatory=False,
        show_in_edit_views=False,
        section="Output",
    )

    atom_fin_tot_eng_in_ev = PropertyTypeAssignment(
        code="ATOM_FIN_TOT_ENG_IN_EV",
        data_type="REAL",
        property_label="Final Total Energy [eV]",
        description="""Final Total Energy [eV]//Letzte Gesamtenergie [eV]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Output",
    )

    atom_fin_pot_eng_in_ev = PropertyTypeAssignment(
        code="ATOM_FIN_POT_ENG_IN_EV",
        data_type="REAL",
        property_label="Final Potential Energy [eV]",
        description="""Final Potential Energy [eV]//Letzte potenzielle Energie [eV]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Output",
    )

    atom_fin_press_in_gpa = PropertyTypeAssignment(
        code="ATOM_FIN_PRESS_IN_GPA",
        data_type="REAL",
        property_label="Final Pressure [GPa]",
        description="""Final pressure [GPa]//Letzter Druck [GPa]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Output",
    )

    atom_fin_vol_in_a3 = PropertyTypeAssignment(
        code="ATOM_FIN_VOL_IN_A3",
        data_type="REAL",
        property_label="Final Volume [Å^3]",
        description="""Final Volume [Å^3]//Letztes Volumen [Å^3]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Output",
    )

    atom_force_max_in_ev_a = PropertyTypeAssignment(
        code="ATOM_FORCE_MAX_IN_EV_A",
        data_type="REAL",
        property_label="Final Maximum Force Component [eV/Å]",
        description="""Final maximum force component [eV/Å]//Letzte maximale Kraftkomponente [eV/Å]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Output",
    )

    atom_fin_totmgmo_in_mub = PropertyTypeAssignment(
        code="ATOM_FIN_TOTMGMO_IN_MUB",
        data_type="VARCHAR",
        property_label="Final Total Magnetic Moment [μ_B]",
        description="""Final total magnetic moment [μ_B]//Leztztes magnetisches Gesamtmoment [μ_B]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Output",
    )


class Amorphous(MatSimStructure):
    defs = ObjectTypeDef(
        code="MAT_SIM_STRUCTURE.AMORPHOUS",
        description="""Material simulation structure - amorphous//Material-simulationsstruktur - amorph""",
        generated_code_prefix="MAT_SIM_STR.AMO",
    )

    atom_short_rng_ord = PropertyTypeAssignment(
        code="ATOM_SHORT_RNG_ORD",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="SHORT_RNG_ORD",
        property_label="Short-range Ordering",
        description="""Chains, rings, tetrahedra etc.//Ketten, Ringe, Tetraeder usw.""",
        mandatory=False,
        show_in_edit_views=False,
        section="Material Information",
    )

    chem_species_by_n_atoms = PropertyTypeAssignment(
        code="CHEM_SPECIES_BY_N_ATOMS",
        data_type="VARCHAR",
        property_label="Chemical Species (number of atoms)",
        description="""Chemical species involved by number of atoms//Chemische Spezies nach Anzahl der Atome""",
        mandatory=False,
        show_in_edit_views=False,
        section="Simulation Information",
    )

    n_atoms_total = PropertyTypeAssignment(
        code="N_ATOMS_TOTAL",
        data_type="INTEGER",
        property_label="Total Number of Atoms",
        description="""Total number of atoms in sample//Gesamtzahl der Atome in der Probe""",
        mandatory=False,
        show_in_edit_views=False,
        section="Simulation Information",
    )

    atom_sample_temp_in_k = PropertyTypeAssignment(
        code="ATOM_SAMPLE_TEMP_IN_K",
        data_type="REAL",
        property_label="Sample Temperature [K]",
        description="""Current temperature of sample [K]//Aktuelle Temperatur der Probe [K]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Simulation Information",
    )


class Crystal(MatSimStructure):
    defs = ObjectTypeDef(
        code="MAT_SIM_STRUCTURE.CRYSTAL",
        description="""Material simulation structure - crystal//Material -Simulationsstruktur - kristallin""",
        generated_code_prefix="MAT_SIM_STR.CRY",
    )

    lattice_param_a_in_a = PropertyTypeAssignment(
        code="LATTICE_PARAM_A_IN_A",
        data_type="REAL",
        property_label="Lattice Parameter (a) [Å]",
        description="""Lattice parameter (a) [Å]//Gitterparameter (a) [Å]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Material Information",
    )

    lattice_param_b_in_a = PropertyTypeAssignment(
        code="LATTICE_PARAM_B_IN_A",
        data_type="REAL",
        property_label="Lattice Parameter (b) [Å]",
        description="""Lattice parameter (b) [Å]//Gitterparameter (b) [Å]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Material Information",
    )

    lattice_param_c_in_a = PropertyTypeAssignment(
        code="LATTICE_PARAM_C_IN_A",
        data_type="REAL",
        property_label="Lattice Parameter (c) [Å]",
        description="""Lattice parameter (c) [Å]//Gitterparameter (c) [Å]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Material Information",
    )

    lattice_c_over_a = PropertyTypeAssignment(
        code="LATTICE_C_OVER_A",
        data_type="REAL",
        property_label="Lattice Parameter (c over a)",
        description="""Lattice parameter (c over a)//Gitterparameter (c über a)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Material Information",
    )

    lattice_angalpha_in_deg = PropertyTypeAssignment(
        code="LATTICE_ANGALPHA_IN_DEG",
        data_type="REAL",
        property_label="Lattice Angle (alpha) [Degrees]",
        description="""Lattice angle (alpha) [Degrees]//Gitterwinkel (alpha) [Grad]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Material Information",
    )

    lattice_angbeta_in_deg = PropertyTypeAssignment(
        code="LATTICE_ANGBETA_IN_DEG",
        data_type="REAL",
        property_label="Lattice Angle (beta) [Degrees]",
        description="""Lattice angle (beta) [Degrees]//Gitterwinkel (beta) [Grad]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Material Information",
    )

    lattice_anggamma_in_deg = PropertyTypeAssignment(
        code="LATTICE_ANGGAMMA_IN_DEG",
        data_type="REAL",
        property_label="Lattice Angle (gamma) [Degrees]",
        description="""Lattice angle (gamma) [Degrees]//Gitterwinkel (gamma) [Grad]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Material Information",
    )

    lattice_volume_in_a3 = PropertyTypeAssignment(
        code="LATTICE_VOLUME_IN_A3",
        data_type="REAL",
        property_label="Lattice Volume [Å^3]",
        description="""Lattice volume [Å^3]//Volumen des Gitters [Å^3]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Material Information",
    )

    space_group = PropertyTypeAssignment(
        code="SPACE_GROUP",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="SPACE_GROUP",
        property_label="Space Group",
        description="""Space group//Raumgruppe""",
        mandatory=False,
        show_in_edit_views=False,
        section="Material Information",
    )

    bravais_lattice = PropertyTypeAssignment(
        code="BRAVAIS_LATTICE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BRAVAIS_LATTICE",
        property_label="Bravais Lattice",
        description="""Bravais lattice//Bravais-Gitter""",
        mandatory=False,
        show_in_edit_views=False,
        section="Material Information",
    )

    chem_species_by_n_atoms = PropertyTypeAssignment(
        code="CHEM_SPECIES_BY_N_ATOMS",
        data_type="VARCHAR",
        property_label="Chemical Species (number of atoms)",
        description="""Chemical species involved by number of atoms//Chemische Spezies nach Anzahl der Atome""",
        mandatory=False,
        show_in_edit_views=False,
        section="Simulation Information",
    )

    n_atoms_total = PropertyTypeAssignment(
        code="N_ATOMS_TOTAL",
        data_type="INTEGER",
        property_label="Total Number of Atoms",
        description="""Total number of atoms in sample//Gesamtzahl der Atome in der Probe""",
        mandatory=False,
        show_in_edit_views=False,
        section="Simulation Information",
    )


class MeasurementSession(ExperimentalStep):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.MEASUREMENT_SESSION",
        description="""Metadata for a group of measurements from a measurement series or session//Metadaten für eine Gruppe von Messungen aus einer Messreihe oder Sitzung""",
        generated_code_prefix="EXP.MSES_",
    )

    responsible_person = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Responsible person",
        description="""Responsible person//Verantwortliche Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    bam_partner = PropertyTypeAssignment(
        code="BAM_PARTNER",
        data_type="VARCHAR",
        property_label="BAM Partner",
        description="""BAM Partner(s)//BAM Partner""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )


class GmawBase(Weldment):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.WELDMENT.GMAW_BASE",
        description="""A simple gas metal arc welding (GMAW) experiment//Ein einfacher MSG-Schweißversuch""",
        generated_code_prefix="EXP.WLD.GMAW_BASE",
    )

    experimental_step_weldment_workpiece_thickness = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.WORKPIECE_THICKNESS",
        data_type="REAL",
        property_label="Thickness of the workpiece [mm]",
        description="""Workpiece thickness//Bauteildicke""",
        mandatory=False,
        show_in_edit_views=False,
        section="Workpiece Parameters",
    )

    experimental_step_weldment_groove_preparation = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.GROOVE_PREPARATION",
        data_type="VARCHAR",
        property_label="Groove preparation",
        description="""Groove or Joint preparation description//Beschreibung der Nahtvorbereitung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Workpiece Parameters",
    )

    experimental_step_weldment_weld_travel_speed = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.WELD_TRAVEL_SPEED",
        data_type="REAL",
        property_label="Welding travel speed [cm/min]",
        description="""Welding travel speed//Schweißgeschwindigkeit""",
        mandatory=False,
        show_in_edit_views=False,
        section="Welding Parameters",
    )

    experimental_step_weldment_shielding_gas_flow = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.SHIELDING_GAS_FLOW",
        data_type="REAL",
        property_label="Shielding gas flowrate [l/min]",
        description="""Shielding gas flowrate//Schutzgasflussgeschwindigkeit""",
        mandatory=False,
        show_in_edit_views=False,
        section="Welding Parameters",
    )

    experimental_step_weldment_arc_process = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.ARC_PROCESS",
        data_type="VARCHAR",
        property_label="Arc welding process",
        description="""Name of the selected arc welding process//Name des Lichtbogenschweißprozesses""",
        mandatory=False,
        show_in_edit_views=False,
        section="Arc welding Parameters",
    )

    experimental_step_weldment_arc_voltage = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.ARC_VOLTAGE",
        data_type="REAL",
        property_label="Arc voltage [V]",
        description="""Welding arc voltage//Lichtbogenspannung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Arc welding Parameters",
    )

    experimental_step_weldment_arc_current = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.ARC_CURRENT",
        data_type="REAL",
        property_label="Arc current [A]",
        description="""Welding arc current//Schweißstrom""",
        mandatory=False,
        show_in_edit_views=False,
        section="Arc welding Parameters",
    )

    experimental_step_weldment_wire_stickout_length = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.WIRE_STICKOUT_LENGTH",
        data_type="REAL",
        property_label="Wire stickout [mm]",
        description="""Length of the wire stickout//Stickoutlänge des Schweißdrahtes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Arc welding Parameters",
    )

    experimental_step_weldment_wire_feed_rate = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.WIRE_FEED_RATE",
        data_type="REAL",
        property_label="Wire feed rate [m/min]",
        description="""Welding wire feed rate//Drahtvorschubrate""",
        mandatory=False,
        show_in_edit_views=False,
        section="Arc welding Parameters",
    )


class LaserHybridMagnet(Weldment):
    defs = ObjectTypeDef(
        code="EXPERIMENTAL_STEP.WELDMENT.LASER_HYBRID_MAGNET",
        description="""A welding experiment using laser-hybrid welding with magnetic support//Ein Laser-Hybrid Schweißversuch mit magnetischer Badstütze""",
        generated_code_prefix="EXP.WLD.LSR_HYB_MGNT",
    )

    experimental_step_weldment_workpiece_thickness = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.WORKPIECE_THICKNESS",
        data_type="REAL",
        property_label="Thickness of the workpiece [mm]",
        description="""Workpiece thickness//Bauteildicke""",
        mandatory=False,
        show_in_edit_views=False,
        section="Workpiece Parameters",
    )

    experimental_step_weldment_groove_preparation = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.GROOVE_PREPARATION",
        data_type="VARCHAR",
        property_label="Groove preparation",
        description="""Groove or Joint preparation description//Beschreibung der Nahtvorbereitung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Workpiece Parameters",
    )

    experimental_step_weldment_weld_travel_speed = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.WELD_TRAVEL_SPEED",
        data_type="REAL",
        property_label="Welding travel speed [cm/min]",
        description="""Welding travel speed//Schweißgeschwindigkeit""",
        mandatory=False,
        show_in_edit_views=False,
        section="Welding Parameters",
    )

    experimental_step_weldment_shielding_gas_flow = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.SHIELDING_GAS_FLOW",
        data_type="REAL",
        property_label="Shielding gas flowrate [l/min]",
        description="""Shielding gas flowrate//Schutzgasflussgeschwindigkeit""",
        mandatory=False,
        show_in_edit_views=False,
        section="Welding Parameters",
    )

    experimental_step_weldment_laser_wire_offset = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.LASER_WIRE_OFFSET",
        data_type="REAL",
        property_label="Laser distance to wire [mm]",
        description="""Distance from laser spot to wire feed//Abstand zwischen Laser und Draht""",
        mandatory=False,
        show_in_edit_views=False,
        section="Laser Parameters",
    )

    experimental_step_weldment_laser_power = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.LASER_POWER",
        data_type="REAL",
        property_label="Laser power [kW]",
        description="""Laser power//Laserleistung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Laser Parameters",
    )

    experimental_step_weldment_laser_focus = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.LASER_FOCUS",
        data_type="REAL",
        property_label="Laser focus [mm]",
        description="""Laser focus position//Laser Fokuslage""",
        mandatory=False,
        show_in_edit_views=False,
        section="Laser Parameters",
    )

    experimental_step_weldment_magnet_capacitance = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.MAGNET_CAPACITANCE",
        data_type="REAL",
        property_label="Capacitance C [µF]",
        description="""Capacitance//Kapazität""",
        mandatory=False,
        show_in_edit_views=False,
        section="Magnet Parameters",
    )

    experimental_step_weldment_magnet_frequency = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.MAGNET_FREQUENCY",
        data_type="REAL",
        property_label="Frequency F [Hz]",
        description="""Frequency//Frequenz""",
        mandatory=False,
        show_in_edit_views=False,
        section="Magnet Parameters",
    )

    experimental_step_weldment_current_transformer = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.CURRENT_TRANSFORMER",
        data_type="REAL",
        property_label="Current transformer HAS 50-S [mV/A]",
        description="""Current transformer HAS 50-S//Stromwandler HAS 50-S""",
        mandatory=False,
        show_in_edit_views=False,
        section="Magnet Parameters",
    )

    experimental_step_weldment_magnet_u_1 = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.MAGNET_U_1",
        data_type="REAL",
        property_label="U_1 [mV]",
        description="""Magnet U_1 value//Magnet U_1 Wert""",
        mandatory=False,
        show_in_edit_views=False,
        section="Magnet Parameters",
    )

    experimental_step_weldment_magnet_i_1 = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.MAGNET_I_1",
        data_type="REAL",
        property_label="I_1 [A]",
        description="""Magnet I_1 value//Magnet I_1 Wert""",
        mandatory=False,
        show_in_edit_views=False,
        section="Magnet Parameters",
    )

    experimental_step_weldment_arc_process = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.ARC_PROCESS",
        data_type="VARCHAR",
        property_label="Arc welding process",
        description="""Name of the selected arc welding process//Name des Lichtbogenschweißprozesses""",
        mandatory=False,
        show_in_edit_views=False,
        section="Arc Welding Parameters",
    )

    experimental_step_weldment_arc_voltage = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.ARC_VOLTAGE",
        data_type="REAL",
        property_label="Arc voltage [V]",
        description="""Welding arc voltage//Lichtbogenspannung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Arc Welding Parameters",
    )

    experimental_step_weldment_arc_current = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.ARC_CURRENT",
        data_type="REAL",
        property_label="Arc current [A]",
        description="""Welding arc current//Schweißstrom""",
        mandatory=False,
        show_in_edit_views=False,
        section="Arc Welding Parameters",
    )

    experimental_step_weldment_wire_stickout_length = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.WIRE_STICKOUT_LENGTH",
        data_type="REAL",
        property_label="Wire stickout [mm]",
        description="""Length of the wire stickout//Stickoutlänge des Schweißdrahtes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Arc Welding Parameters",
    )

    experimental_step_weldment_wire_feed_rate = PropertyTypeAssignment(
        code="EXPERIMENTAL_STEP.WELDMENT.WIRE_FEED_RATE",
        data_type="REAL",
        property_label="Wire feed rate [m/min]",
        description="""Welding wire feed rate//Drahtvorschubrate""",
        mandatory=False,
        show_in_edit_views=False,
        section="Arc Welding Parameters",
    )


class WireSolid(Welding):
    defs = ObjectTypeDef(
        code="CONSUMABLE.WELDING.WIRE_SOLID",
        description="""Solid welding wire//Massivdraht (Schweißzusatz)""",
        generated_code_prefix="CONS.WLD.WRE_SLD",
    )

    welding_wire_diameter = PropertyTypeAssignment(
        code="WELDING_WIRE.DIAMETER",
        data_type="REAL",
        property_label="Diameter [mm]",
        description="""Diameter in mm//Durchmesser in mm""",
        mandatory=True,
        show_in_edit_views=False,
        section="Wire Information",
    )

    welding_wire_iso_specname = PropertyTypeAssignment(
        code="WELDING_WIRE.ISO_SPECNAME",
        data_type="VARCHAR",
        property_label="ISO specification",
        description="""ISO specification of the wire//ISO Klassifizierung des Zusatzwerkstoffs""",
        mandatory=False,
        show_in_edit_views=False,
        section="Wire Information",
    )

    welding_wire_iso_standard = PropertyTypeAssignment(
        code="WELDING_WIRE.ISO_STANDARD",
        data_type="VARCHAR",
        property_label="ISO standard",
        description="""ISO standard providing the specification//ISO Norm o.ä. mit Angabe zur Klassifizierung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Wire Information",
    )

    welding_wire_aws_specname = PropertyTypeAssignment(
        code="WELDING_WIRE.AWS_SPECNAME",
        data_type="VARCHAR",
        property_label="AWS specification",
        description="""AWS specification of the wire//AWS Klassifizierung des Zusatzwerkstoffs""",
        mandatory=False,
        show_in_edit_views=False,
        section="Wire Information",
    )

    welding_wire_aws_standard = PropertyTypeAssignment(
        code="WELDING_WIRE.AWS_STANDARD",
        data_type="VARCHAR",
        property_label="AWS standard",
        description="""AWS standard providing the specification//AWS Standard mit Angabe zur Klassifizierung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Wire Information",
    )

    welding_wire_weight = PropertyTypeAssignment(
        code="WELDING_WIRE.WEIGHT",
        data_type="REAL",
        property_label="Weight [kg]",
        description="""Weight of the wire package as delivered//Gesamtgewicht des Drahtes bei Lieferung""",
        mandatory=False,
        show_in_edit_views=False,
        section="Wire Information",
    )


class Lens(Camera):
    defs = ObjectTypeDef(
        code="INSTRUMENT.CAMERA.LENS",
        description="""Lens used together with imaging camera//Objektiv für Bildaufnahmen mit einer Kamera""",
        generated_code_prefix="INS.CAM.LENS",
    )

    lens_focallength = PropertyTypeAssignment(
        code="LENS_FOCALLENGTH",
        data_type="REAL",
        property_label="Focal length [mm]",
        description="""Focal length of optical lens [mm]//Brennweite der Kameralinse [mm]""",
        mandatory=True,
        show_in_edit_views=False,
        section="Lens Information",
    )

    lens_aperture_max = PropertyTypeAssignment(
        code="LENS_APERTURE_MAX",
        data_type="REAL",
        property_label="Maximum Aperture [f/]",
        description="""Maximum Aperture [f/]//Maximale Blendenöffnung [f/]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Lens Information",
    )

    lens_aperture_min = PropertyTypeAssignment(
        code="LENS_APERTURE_MIN",
        data_type="REAL",
        property_label="Minimum Aperture [f/]",
        description="""Minimum Aperture [f/]//Minimale Blendenzahl [f/]""",
        mandatory=False,
        show_in_edit_views=False,
        section="Lens Information",
    )

    lens_confocal = PropertyTypeAssignment(
        code="LENS_CONFOCAL",
        data_type="BOOLEAN",
        property_label="Confocal",
        description="""Confocal optics//Konfokale Linse""",
        mandatory=False,
        show_in_edit_views=False,
        section="Lens Information",
    )


class GmawTorch(WeldingEquipment):
    defs = ObjectTypeDef(
        code="INSTRUMENT.WELDING_EQUIPMENT.GMAW_TORCH",
        description="""Arc welding torch for gas metal arc welding (GMAW) applications//Schweißbrenner für Metall-Schutzgas-Schweißen (MSG-Schweißen)""",
        generated_code_prefix="INS.WLD_EQP.GMAW_TRCH",
    )

    welding_torch_type = PropertyTypeAssignment(
        code="WELDING.TORCH_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="WELDING.GMAW_TORCH_TYPE",
        property_label="Type",
        description="""type of welding torch//Art des Schweißbrenners""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )


class GmawWeldingPowerSource(WeldingEquipment):
    defs = ObjectTypeDef(
        code="INSTRUMENT.WELDING_EQUIPMENT.GMAW_WELDING_POWER_SOURCE",
        description="""Power source for gas metal arc welding (GMAW) applications//Stromquelle für Metall-Schutzgas-Schweißen (MSG-Schweißen)""",
        generated_code_prefix="INS.WLD_EQP.GMAW_PWR_SRC",
    )

    welding_arc_current_min = PropertyTypeAssignment(
        code="WELDING.ARC_CURRENT_MIN",
        data_type="REAL",
        property_label="Arc current minimum [A]",
        description="""Minimum arc current//Minimaler Schweißstrom""",
        mandatory=False,
        show_in_edit_views=False,
        section="Power Source Information",
    )

    welding_arc_current_max = PropertyTypeAssignment(
        code="WELDING.ARC_CURRENT_MAX",
        data_type="REAL",
        property_label="Arc current maximum [A]",
        description="""Maximum arc current//Maximaler Schweißstrom""",
        mandatory=False,
        show_in_edit_views=False,
        section="Power Source Information",
    )

    welding_arc_current_continuous = PropertyTypeAssignment(
        code="WELDING.ARC_CURRENT_CONTINUOUS",
        data_type="REAL",
        property_label="Maximum continuous arc current [A]",
        description="""Maximum continuous arc current at 100% duty cycle//Maximaler Schweißstrom bei 100% Einschaltdauer""",
        mandatory=False,
        show_in_edit_views=False,
        section="Power Source Information",
    )

    firmware_version = PropertyTypeAssignment(
        code="FIRMWARE_VERSION",
        data_type="VARCHAR",
        property_label="Current firmware version",
        description="""The currently installed firmware version//Die aktuell installierte Firmware-Version""",
        mandatory=False,
        show_in_edit_views=False,
        section="Software Information",
    )


class Positioner(WeldingEquipment):
    defs = ObjectTypeDef(
        code="INSTRUMENT.WELDING_EQUIPMENT.POSITIONER",
        description="""A generic welding table or handling device//Generischer Schweißtisch oder anderer Positionierer zum Schweißen""",
        generated_code_prefix="INS.WLD_EQP.WLD_PSR",
    )

    positioner_type = PropertyTypeAssignment(
        code="POSITIONER_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="POSITIONER_TYPE",
        property_label="Positioner type",
        description="""Positioner type//Art des Positionierers""",
        mandatory=False,
        show_in_edit_views=False,
        section="Positioner Information",
    )

    positioner_axis_count = PropertyTypeAssignment(
        code="POSITIONER_AXIS_COUNT",
        data_type="INTEGER",
        property_label="Number of axis",
        description="""The number of controllable axis of the positioner (a value of 0 indicates static positioner)//""",
        mandatory=False,
        show_in_edit_views=False,
        section="Positioner Information",
    )

    positioner_payload_max = PropertyTypeAssignment(
        code="POSITIONER_PAYLOAD_MAX",
        data_type="REAL",
        property_label="Maximum payload [kg]",
        description="""The maximum payload to be handled by the positioner//Maximal zulässige Traglast""",
        mandatory=False,
        show_in_edit_views=False,
        section="Positioner Information",
    )


class RobotController(WeldingEquipment):
    defs = ObjectTypeDef(
        code="INSTRUMENT.WELDING_EQUIPMENT.ROBOT_CONTROLLER",
        description="""Controller connected to a welding robot//Steuerung für Schweißroboter""",
        generated_code_prefix="INS.WLD_EQP.RBT_CTRL",
    )

    robot_controller_axis_count = PropertyTypeAssignment(
        code="ROBOT_CONTROLLER_AXIS_COUNT",
        data_type="INTEGER",
        property_label="Number of robot axis",
        description="""The number of robot axis the controller can operate//Anzahl der Roboterachsen die von der Steuerung angesteuert werden können""",
        mandatory=True,
        show_in_edit_views=False,
        section="Controller Information",
    )

    robot_controller_axis_count_external = PropertyTypeAssignment(
        code="ROBOT_CONTROLLER_AXIS_COUNT_EXTERNAL",
        data_type="INTEGER",
        property_label="Number of external axis",
        description="""The number of external axis the controller can operate//Anzahl der zusätzlichen externen Achsen die von der Steuerung angesteuert werden können""",
        mandatory=True,
        show_in_edit_views=False,
        section="Controller Information",
    )

    firmware_version = PropertyTypeAssignment(
        code="FIRMWARE_VERSION",
        data_type="VARCHAR",
        property_label="Current firmware version",
        description="""The currently installed firmware version//Die aktuell installierte Firmware-Version""",
        mandatory=False,
        show_in_edit_views=False,
        section="Software Information",
    )


class Robot(WeldingEquipment):
    defs = ObjectTypeDef(
        code="INSTRUMENT.WELDING_EQUIPMENT.ROBOT",
        description="""A generic robot used for welding//Ein generischer Schweißroboter""",
        generated_code_prefix="INS.WLD_EQP.RBT",
    )

    robot_type = PropertyTypeAssignment(
        code="ROBOT_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="ROBOT_TYPE",
        property_label="Type of Robot",
        description="""Type of Robot//Roboterart""",
        mandatory=True,
        show_in_edit_views=False,
        section="Robot Information",
    )

    robot_payload_max = PropertyTypeAssignment(
        code="ROBOT_PAYLOAD_MAX",
        data_type="INTEGER",
        property_label="Robot maximum payload [kg]",
        description="""The maximum allowable payload of the robot//Die maximal zulässig Traglast des Roboters""",
        mandatory=False,
        show_in_edit_views=False,
        section="Robot Information",
    )

    robot_working_range = PropertyTypeAssignment(
        code="ROBOT_WORKING_RANGE",
        data_type="REAL",
        property_label="Maximum working range [mm]",
        description="""The maximum specified working range of the robot (in mm)//Größe des maximal angegegebenen Arbeitsbereiches (in mm)""",
        mandatory=False,
        show_in_edit_views=False,
        section="Robot Information",
    )

    robot_axis_count = PropertyTypeAssignment(
        code="ROBOT_AXIS_COUNT",
        data_type="INTEGER",
        property_label="Number of robot axis",
        description="""The number of a axis on the robot//Anzahl der Roboterachsen""",
        mandatory=False,
        show_in_edit_views=False,
        section="Robot Information",
    )


# ! The parent class of StationLayout is not defined (missing ObjectType)
# StationLayout is defined several times in the model
class StationLayout1(ObjectType):
    defs = ObjectTypeDef(
        code="WELDING.EQUIPMENT.STATION_LAYOUT",
        description="""Layout and configuration of a welding station""",
        generated_code_prefix="INS.WLD_EQP.ST_LYT",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General information",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative Name",
        description="""e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname""",
        mandatory=False,
        show_in_edit_views=False,
        section="General information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="General information",
    )

    device_model_name = PropertyTypeAssignment(
        code="DEVICE_MODEL_NAME",
        data_type="VARCHAR",
        property_label="Model Name",
        description="""Manufacturer model name//Modellname bzw. Gerätebezeichnung seitens des Herstellers""",
        mandatory=False,
        show_in_edit_views=False,
        section="General information",
    )

    manufacturer = PropertyTypeAssignment(
        code="MANUFACTURER",
        data_type="VARCHAR",
        property_label="Manufacturer",
        description="""Manufacturer//Hersteller""",
        mandatory=True,
        show_in_edit_views=False,
        section="General information",
    )

    supplier = PropertyTypeAssignment(
        code="SUPPLIER",
        data_type="VARCHAR",
        property_label="Supplier",
        description="""Supplier//Lieferant""",
        mandatory=False,
        show_in_edit_views=False,
        section="General information",
    )

    serial_number = PropertyTypeAssignment(
        code="SERIAL_NUMBER",
        data_type="VARCHAR",
        property_label="Serial Number",
        description="""Serial Number//Seriennummer""",
        mandatory=False,
        show_in_edit_views=False,
        section="General information",
    )

    dfg_device_code = PropertyTypeAssignment(
        code="DFG_DEVICE_CODE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DFG_DEVICE_CODE",
        property_label="DFG Device Code",
        description="""DFG Device Code//DFG Gerätegruppenschlüssel (GGS)""",
        mandatory=False,
        show_in_edit_views=False,
        section="General information",
    )

    inventory_no = PropertyTypeAssignment(
        code="INVENTORY_NO",
        data_type="INTEGER",
        property_label="Inventory Number",
        description="""PARFIS inventory number (8-digit)//PARFIS Inventarnummer (8-stellig)""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM information",
    )

    inventory_no_add = PropertyTypeAssignment(
        code="INVENTORY_NO_ADD",
        data_type="INTEGER",
        property_label="Inventory Number Addition",
        description="""PARFIS inventory number (8-digit)//PARFIS Inventarnummer (8-stellig)""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM information",
    )

    bam_oe = PropertyTypeAssignment(
        code="BAM_OE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_OE",
        property_label="BAM Organizational Entity",
        description="""BAM Organizational Entity//BAM Organisationseinheit (OE)""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM information",
    )

    responsible_person = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Responsible person",
        description="""Responsible person//Verantwortliche Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM information",
    )

    co_responsible_person = PropertyTypeAssignment(
        code="CO_RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Co-responsible person",
        description="""Co-responsible person//Weitere verantwortliche Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM information",
    )

    bam_room = PropertyTypeAssignment(
        code="BAM_ROOM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_ROOM",
        property_label="BAM Room",
        description="""BAM Room//BAM Raum""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM information",
    )

    bam_floor = PropertyTypeAssignment(
        code="BAM_FLOOR",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_FLOOR",
        property_label="BAM Floor",
        description="""BAM Floor//BAM Etage""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM information",
    )

    bam_house = PropertyTypeAssignment(
        code="BAM_HOUSE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_HOUSE",
        property_label="BAM House",
        description="""BAM House//BAM Haus""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM information",
    )

    bam_location = PropertyTypeAssignment(
        code="BAM_LOCATION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_LOCATION",
        property_label="BAM Location",
        description="""BAM Location//BAM Liegenschaft""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM information",
    )

    bam_location_complete = PropertyTypeAssignment(
        code="BAM_LOCATION_COMPLETE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_LOCATION_COMPLETE",
        property_label="Complete BAM Location",
        description="""Complete BAM location (up to room level)//Komplette BAM-Ortsangabe (bis Raumlevel)""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Details",
    )

    last_systemcheck = PropertyTypeAssignment(
        code="LAST_SYSTEMCHECK",
        data_type="DATE",
        property_label="Last System Check",
        description="""Date of the last system check//Datum des letzten Systemchecks""",
        mandatory=False,
        show_in_edit_views=False,
        section="Details",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )


# StationLayout is defined several times in the model
class StationLayout2(WeldingEquipment):
    defs = ObjectTypeDef(
        code="INSTRUMENT.WELDING_EQUIPMENT.STATION_LAYOUT",
        description="""Layout and configuration of a welding station""",
        generated_code_prefix="INS.WLD_EQP.ST_LYT",
    )


# ! The parent class of StationLayout is not defined (missing ObjectType)
# StationLayout is defined several times in the model
class StationLayout3(ObjectType):
    defs = ObjectTypeDef(
        code="INSTRUMENT.WELDING.EQUIPMENT.STATION_LAYOUT",
        description="""Layout and configuration of a welding station""",
        generated_code_prefix="INS.WLD_EQP.ST_LYT",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alternative Name",
        description="""e.g. abbreviation or nickname//z.B. Abkürzung oder Spitzname""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code="DESCRIPTION",
        data_type="MULTILINE_VARCHAR",
        property_label="Description",
        description="""Short description and/or purpose//Kurzbeschreibung und/oder Zweck""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    device_model_name = PropertyTypeAssignment(
        code="DEVICE_MODEL_NAME",
        data_type="VARCHAR",
        property_label="Model Name",
        description="""Manufacturer model name//Modellname bzw. Gerätebezeichnung seitens des Herstellers""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    manufacturer = PropertyTypeAssignment(
        code="MANUFACTURER",
        data_type="VARCHAR",
        property_label="Manufacturer",
        description="""Manufacturer//Hersteller""",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    supplier = PropertyTypeAssignment(
        code="SUPPLIER",
        data_type="VARCHAR",
        property_label="Supplier",
        description="""Supplier//Lieferant""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    serial_number = PropertyTypeAssignment(
        code="SERIAL_NUMBER",
        data_type="VARCHAR",
        property_label="Serial Number",
        description="""Serial Number//Seriennummer""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    dfg_device_code = PropertyTypeAssignment(
        code="DFG_DEVICE_CODE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="DFG_DEVICE_CODE",
        property_label="DFG Device Code",
        description="""DFG Device Code//DFG Gerätegruppenschlüssel (GGS)""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    inventory_no = PropertyTypeAssignment(
        code="INVENTORY_NO",
        data_type="INTEGER",
        property_label="Inventory Number",
        description="""PARFIS inventory number (8-digit)//PARFIS Inventarnummer (8-stellig)""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    inventory_no_add = PropertyTypeAssignment(
        code="INVENTORY_NO_ADD",
        data_type="INTEGER",
        property_label="Inventory Number Addition",
        description="""PARFIS inventory number (8-digit)//PARFIS Inventarnummer (8-stellig)""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_oe = PropertyTypeAssignment(
        code="BAM_OE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_OE",
        property_label="BAM Organizational Entity",
        description="""BAM Organizational Entity//BAM Organisationseinheit (OE)""",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    responsible_person = PropertyTypeAssignment(
        code="RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Responsible person",
        description="""Responsible person//Verantwortliche Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    co_responsible_person = PropertyTypeAssignment(
        code="CO_RESPONSIBLE_PERSON",
        data_type="OBJECT",
        object_code="PERSON.BAM",
        property_label="Co-responsible person",
        description="""Co-responsible person//Weitere verantwortliche Person""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_room = PropertyTypeAssignment(
        code="BAM_ROOM",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_ROOM",
        property_label="BAM Room",
        description="""BAM Room//BAM Raum""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_floor = PropertyTypeAssignment(
        code="BAM_FLOOR",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_FLOOR",
        property_label="BAM Floor",
        description="""BAM Floor//BAM Etage""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_house = PropertyTypeAssignment(
        code="BAM_HOUSE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_HOUSE",
        property_label="BAM House",
        description="""BAM House//BAM Haus""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_location = PropertyTypeAssignment(
        code="BAM_LOCATION",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_LOCATION",
        property_label="BAM Location",
        description="""BAM Location//BAM Liegenschaft""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_location_complete = PropertyTypeAssignment(
        code="BAM_LOCATION_COMPLETE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BAM_LOCATION_COMPLETE",
        property_label="Complete BAM Location",
        description="""Complete BAM location (up to room level)//Komplette BAM-Ortsangabe (bis Raumlevel)""",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    last_systemcheck = PropertyTypeAssignment(
        code="LAST_SYSTEMCHECK",
        data_type="DATE",
        property_label="Last System Check",
        description="""Date of the last system check//Datum des letzten Systemchecks""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    notes = PropertyTypeAssignment(
        code="NOTES",
        data_type="MULTILINE_VARCHAR",
        property_label="Notes",
        description="""Notes""",
        mandatory=False,
        show_in_edit_views=False,
        section="Additional Information",
    )

    xmlcomments = PropertyTypeAssignment(
        code="$XMLCOMMENTS",
        data_type="XML",
        property_label="Comments",
        description="""Comments log""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code="$ANNOTATIONS_STATE",
        data_type="XML",
        property_label="Annotations State",
        description="""Annotations State""",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )
