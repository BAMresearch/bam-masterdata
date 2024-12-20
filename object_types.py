from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.entities import ObjectType


class SearchQuery(ObjectType):
    defs = ObjectTypeDef(
        code='SEARCH_QUERY',
        description="",
        generated_code_prefix='SEARCH_QUERY.',
    )

    name = PropertyTypeAssignment(
        code='$NAME',
        data_type='',
        property_label="",
        description="",
        mandatory=True,
        show_in_edit_views=False,
        section="General",
    )

    search_query_search_criteria = PropertyTypeAssignment(
        code='$SEARCH_QUERY.SEARCH_CRITERIA',
        data_type='',
        property_label="",
        description="",
        mandatory=True,
        show_in_edit_views=False,
        section="General",
    )

    search_query_fetch_options = PropertyTypeAssignment(
        code='$SEARCH_QUERY.FETCH_OPTIONS',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    search_query_custom_data = PropertyTypeAssignment(
        code='$SEARCH_QUERY.CUSTOM_DATA',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )


class GeneralElnSettings(ObjectType):
    defs = ObjectTypeDef(
        code='GENERAL_ELN_SETTINGS',
        description="",
        generated_code_prefix='S',
    )

    eln_settings = PropertyTypeAssignment(
        code='$ELN_SETTINGS',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Settings",
    )


class Entry(ObjectType):
    defs = ObjectTypeDef(
        code='ENTRY',
        description="",
        generated_code_prefix='ENTRY',
    )

    name = PropertyTypeAssignment(
        code='$NAME',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    show_in_project_overview = PropertyTypeAssignment(
        code='$SHOW_IN_PROJECT_OVERVIEW',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    document = PropertyTypeAssignment(
        code='$DOCUMENT',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    annotations_state = PropertyTypeAssignment(
        code='$ANNOTATIONS_STATE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class GeneralProtocol(ObjectType):
    defs = ObjectTypeDef(
        code='GENERAL_PROTOCOL',
        description="",
        generated_code_prefix='GEN',
    )

    name = PropertyTypeAssignment(
        code='$NAME',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    for_what = PropertyTypeAssignment(
        code='FOR_WHAT',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Details",
    )

    general_protocol_protocol_type = PropertyTypeAssignment(
        code='GENERAL_PROTOCOL.PROTOCOL_TYPE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Details",
    )

    general_protocol_materials = PropertyTypeAssignment(
        code='GENERAL_PROTOCOL.MATERIALS',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Details",
    )

    general_protocol_time_requirement = PropertyTypeAssignment(
        code='GENERAL_PROTOCOL.TIME_REQUIREMENT',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Details",
    )

    procedure = PropertyTypeAssignment(
        code='PROCEDURE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Details",
    )

    general_protocol_protocol_evaluation = PropertyTypeAssignment(
        code='GENERAL_PROTOCOL.PROTOCOL_EVALUATION',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Details",
    )

    general_protocol_spreadsheet = PropertyTypeAssignment(
        code='GENERAL_PROTOCOL.SPREADSHEET',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Details",
    )

    reference = PropertyTypeAssignment(
        code='REFERENCE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="References",
    )

    publication = PropertyTypeAssignment(
        code='PUBLICATION',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="References",
    )

    notes = PropertyTypeAssignment(
        code='NOTES',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    xmlcomments = PropertyTypeAssignment(
        code='$XMLCOMMENTS',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )

    annotations_state = PropertyTypeAssignment(
        code='$ANNOTATIONS_STATE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class ExperimentalStep(ObjectType):
    defs = ObjectTypeDef(
        code='EXPERIMENTAL_STEP',
        description="",
        generated_code_prefix='EXP',
    )

    name = PropertyTypeAssignment(
        code='$NAME',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    show_in_project_overview = PropertyTypeAssignment(
        code='$SHOW_IN_PROJECT_OVERVIEW',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    finished_flag = PropertyTypeAssignment(
        code='FINISHED_FLAG',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    start_date = PropertyTypeAssignment(
        code='START_DATE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    end_date = PropertyTypeAssignment(
        code='END_DATE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    experimental_step_experimental_goals = PropertyTypeAssignment(
        code='EXPERIMENTAL_STEP.EXPERIMENTAL_GOALS',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Experimental details",
    )

    experimental_step_experimental_description = PropertyTypeAssignment(
        code='EXPERIMENTAL_STEP.EXPERIMENTAL_DESCRIPTION',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Experimental details",
    )

    experimental_step_experimental_results = PropertyTypeAssignment(
        code='EXPERIMENTAL_STEP.EXPERIMENTAL_RESULTS',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Experimental details",
    )

    experimental_step_spreadsheet = PropertyTypeAssignment(
        code='EXPERIMENTAL_STEP.SPREADSHEET',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Experimental details",
    )

    reference = PropertyTypeAssignment(
        code='REFERENCE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="References",
    )

    publication = PropertyTypeAssignment(
        code='PUBLICATION',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="References",
    )

    notes = PropertyTypeAssignment(
        code='NOTES',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    xmlcomments = PropertyTypeAssignment(
        code='$XMLCOMMENTS',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )

    annotations_state = PropertyTypeAssignment(
        code='$ANNOTATIONS_STATE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class Storage(ObjectType):
    defs = ObjectTypeDef(
        code='STORAGE',
        description="",
        generated_code_prefix='S',
    )

    name = PropertyTypeAssignment(
        code='$NAME',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    storage_row_num = PropertyTypeAssignment(
        code='$STORAGE.ROW_NUM',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    storage_column_num = PropertyTypeAssignment(
        code='$STORAGE.COLUMN_NUM',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    storage_box_num = PropertyTypeAssignment(
        code='$STORAGE.BOX_NUM',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    storage_storage_space_warning = PropertyTypeAssignment(
        code='$STORAGE.STORAGE_SPACE_WARNING',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    storage_box_space_warning = PropertyTypeAssignment(
        code='$STORAGE.BOX_SPACE_WARNING',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General info",
    )

    storage_storage_validation_level = PropertyTypeAssignment(
        code='$STORAGE.STORAGE_VALIDATION_LEVEL',
        data_type='',
        property_label="",
        description="",
        mandatory=True,
        show_in_edit_views=False,
        section="General info",
    )

    xmlcomments = PropertyTypeAssignment(
        code='$XMLCOMMENTS',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )

    annotations_state = PropertyTypeAssignment(
        code='$ANNOTATIONS_STATE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class StoragePosition(ObjectType):
    defs = ObjectTypeDef(
        code='STORAGE_POSITION',
        description="",
        generated_code_prefix='STO',
    )

    storage_position_storage_code = PropertyTypeAssignment(
        code='$STORAGE_POSITION.STORAGE_CODE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Physical Storage",
    )

    storage_position_storage_rack_row = PropertyTypeAssignment(
        code='$STORAGE_POSITION.STORAGE_RACK_ROW',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Physical Storage",
    )

    storage_position_storage_rack_column = PropertyTypeAssignment(
        code='$STORAGE_POSITION.STORAGE_RACK_COLUMN',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Physical Storage",
    )

    storage_position_storage_box_name = PropertyTypeAssignment(
        code='$STORAGE_POSITION.STORAGE_BOX_NAME',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Physical Storage",
    )

    storage_position_storage_box_size = PropertyTypeAssignment(
        code='$STORAGE_POSITION.STORAGE_BOX_SIZE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Physical Storage",
    )

    storage_position_storage_box_position = PropertyTypeAssignment(
        code='$STORAGE_POSITION.STORAGE_BOX_POSITION',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Physical Storage",
    )

    storage_position_storage_user = PropertyTypeAssignment(
        code='$STORAGE_POSITION.STORAGE_USER',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Physical Storage",
    )

    xmlcomments = PropertyTypeAssignment(
        code='$XMLCOMMENTS',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )

    annotations_state = PropertyTypeAssignment(
        code='$ANNOTATIONS_STATE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class Supplier(ObjectType):
    defs = ObjectTypeDef(
        code='SUPPLIER',
        description="",
        generated_code_prefix='SUP',
    )

    name = PropertyTypeAssignment(
        code='$NAME',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    supplier_company_address_line_1 = PropertyTypeAssignment(
        code='$SUPPLIER.COMPANY_ADDRESS_LINE_1',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    supplier_company_address_line_2 = PropertyTypeAssignment(
        code='$SUPPLIER.COMPANY_ADDRESS_LINE_2',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    supplier_company_fax = PropertyTypeAssignment(
        code='$SUPPLIER.COMPANY_FAX',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    supplier_company_phone = PropertyTypeAssignment(
        code='$SUPPLIER.COMPANY_PHONE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    supplier_company_email = PropertyTypeAssignment(
        code='$SUPPLIER.COMPANY_EMAIL',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    supplier_company_language = PropertyTypeAssignment(
        code='$SUPPLIER.COMPANY_LANGUAGE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    supplier_customer_number = PropertyTypeAssignment(
        code='$SUPPLIER.CUSTOMER_NUMBER',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    supplier_company_contact_name = PropertyTypeAssignment(
        code='SUPPLIER.COMPANY_CONTACT_NAME',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    supplier_company_contact_email = PropertyTypeAssignment(
        code='SUPPLIER.COMPANY_CONTACT_EMAIL',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    supplier_preferred_order_method = PropertyTypeAssignment(
        code='SUPPLIER.PREFERRED_ORDER_METHOD',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    supplier_url = PropertyTypeAssignment(
        code='SUPPLIER.URL',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    supplier_additional_information = PropertyTypeAssignment(
        code='SUPPLIER.ADDITIONAL_INFORMATION',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    xmlcomments = PropertyTypeAssignment(
        code='$XMLCOMMENTS',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )

    annotations_state = PropertyTypeAssignment(
        code='$ANNOTATIONS_STATE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class Product(ObjectType):
    defs = ObjectTypeDef(
        code='PRODUCT',
        description="",
        generated_code_prefix='PRO',
    )

    name = PropertyTypeAssignment(
        code='$NAME',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    product_product_secondary_names = PropertyTypeAssignment(
        code='PRODUCT.PRODUCT_SECONDARY_NAMES',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    product_description = PropertyTypeAssignment(
        code='PRODUCT.DESCRIPTION',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    product_company = PropertyTypeAssignment(
        code='PRODUCT.COMPANY',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    product_catalog_num = PropertyTypeAssignment(
        code='$PRODUCT.CATALOG_NUM',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    product_category = PropertyTypeAssignment(
        code='PRODUCT.CATEGORY',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    product_hazard_statement = PropertyTypeAssignment(
        code='PRODUCT.HAZARD_STATEMENT',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    product_price_per_unit = PropertyTypeAssignment(
        code='$PRODUCT.PRICE_PER_UNIT',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    product_currency = PropertyTypeAssignment(
        code='$PRODUCT.CURRENCY',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    product_size_of_item = PropertyTypeAssignment(
        code='PRODUCT.SIZE_OF_ITEM',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    xmlcomments = PropertyTypeAssignment(
        code='$XMLCOMMENTS',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )

    annotations_state = PropertyTypeAssignment(
        code='$ANNOTATIONS_STATE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class Request(ObjectType):
    defs = ObjectTypeDef(
        code='REQUEST',
        description="",
        generated_code_prefix='REQ',
    )

    name = PropertyTypeAssignment(
        code='$NAME',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    ordering_order_status = PropertyTypeAssignment(
        code='$ORDERING.ORDER_STATUS',
        data_type='',
        property_label="",
        description="",
        mandatory=True,
        show_in_edit_views=False,
        section="General",
    )

    request_project = PropertyTypeAssignment(
        code='REQUEST.PROJECT',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    request_department = PropertyTypeAssignment(
        code='REQUEST.DEPARTMENT',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    request_buyer = PropertyTypeAssignment(
        code='REQUEST.BUYER',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    annotations_state = PropertyTypeAssignment(
        code='$ANNOTATIONS_STATE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class Order(ObjectType):
    defs = ObjectTypeDef(
        code='ORDER',
        description="",
        generated_code_prefix='ORD',
    )

    name = PropertyTypeAssignment(
        code='$NAME',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    order_ship_to = PropertyTypeAssignment(
        code='$ORDER.SHIP_TO',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    order_bill_to = PropertyTypeAssignment(
        code='$ORDER.BILL_TO',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    order_ship_address = PropertyTypeAssignment(
        code='$ORDER.SHIP_ADDRESS',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    order_contact_phone = PropertyTypeAssignment(
        code='$ORDER.CONTACT_PHONE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    order_contact_fax = PropertyTypeAssignment(
        code='$ORDER.CONTACT_FAX',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    ordering_order_status = PropertyTypeAssignment(
        code='$ORDERING.ORDER_STATUS',
        data_type='',
        property_label="",
        description="",
        mandatory=True,
        show_in_edit_views=False,
        section="General",
    )

    order_price_paid = PropertyTypeAssignment(
        code='ORDER.PRICE_PAID',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    order_additional_information = PropertyTypeAssignment(
        code='$ORDER.ADDITIONAL_INFORMATION',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    order_order_state = PropertyTypeAssignment(
        code='$ORDER.ORDER_STATE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code='$ANNOTATIONS_STATE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class Publication(ObjectType):
    defs = ObjectTypeDef(
        code='PUBLICATION',
        description="",
        generated_code_prefix='PUB',
    )

    name = PropertyTypeAssignment(
        code='$NAME',
        data_type='',
        property_label="",
        description="",
        mandatory=True,
        show_in_edit_views=False,
        section="General",
    )

    publication_organization = PropertyTypeAssignment(
        code='$PUBLICATION.ORGANIZATION',
        data_type='',
        property_label="",
        description="",
        mandatory=True,
        show_in_edit_views=False,
        section="General",
    )

    publication_type = PropertyTypeAssignment(
        code='$PUBLICATION.TYPE',
        data_type='',
        property_label="",
        description="",
        mandatory=True,
        show_in_edit_views=False,
        section="General",
    )

    publication_identifier = PropertyTypeAssignment(
        code='$PUBLICATION.IDENTIFIER',
        data_type='',
        property_label="",
        description="",
        mandatory=True,
        show_in_edit_views=False,
        section="General",
    )

    publication_url = PropertyTypeAssignment(
        code='$PUBLICATION.URL',
        data_type='',
        property_label="",
        description="",
        mandatory=True,
        show_in_edit_views=False,
        section="General",
    )

    publication_description = PropertyTypeAssignment(
        code='$PUBLICATION.DESCRIPTION',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    publication_openbis_related_identifiers = PropertyTypeAssignment(
        code='$PUBLICATION.OPENBIS_RELATED_IDENTIFIERS',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General",
    )

    xmlcomments = PropertyTypeAssignment(
        code='$XMLCOMMENTS',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )

    annotations_state = PropertyTypeAssignment(
        code='$ANNOTATIONS_STATE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class LocationC(ObjectType):
    defs = ObjectTypeDef(
        code='LOCATION_C',
        description="Locations using vocabularies for each property",
        generated_code_prefix='LOCATION_C',
    )

    roomc = PropertyTypeAssignment(
        code='ROOMC',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="LOCATION INFO",
    )

    building = PropertyTypeAssignment(
        code='BUILDING',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="LOCATION INFO",
    )

    housec = PropertyTypeAssignment(
        code='HOUSEC',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="LOCATION INFO",
    )

    level = PropertyTypeAssignment(
        code='LEVEL',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="LOCATION INFO",
    )

    room_number_c = PropertyTypeAssignment(
        code='ROOM_NUMBER_C',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="LOCATION INFO",
    )


class BamLocation(ObjectType):
    defs = ObjectTypeDef(
        code='BAM_LOCATION',
        description="Complete location (up to room level)//Komplette Ortsangabe (bis Raumlevel)",
        generated_code_prefix='BAM_LOCATION_COMPLETE',
    )

    bam_location_complete = PropertyTypeAssignment(
        code='BAM_LOCATION_COMPLETE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="GENERAL LOCATION",
    )

    bam_location = PropertyTypeAssignment(
        code='BAM_LOCATION',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="GENERAL LOCATION",
    )

    bam_house = PropertyTypeAssignment(
        code='BAM_HOUSE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="GENERAL LOCATION",
    )

    bam_floor = PropertyTypeAssignment(
        code='BAM_FLOOR',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="GENERAL LOCATION",
    )

    bam_room = PropertyTypeAssignment(
        code='BAM_ROOM',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="GENERAL LOCATION",
    )

    test_vocab = PropertyTypeAssignment(
        code='TEST_VOCAB',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="GENERAL LOCATION",
    )

    description = PropertyTypeAssignment(
        code='DESCRIPTION',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="GENERAL LOCATION",
    )


class TestAmount(ObjectType):
    defs = ObjectTypeDef(
        code='TEST_AMOUNT',
        description="Object to test amount entity validation script",
        generated_code_prefix='TEST_AMOUNT',
    )

    amount = PropertyTypeAssignment(
        code='AMOUNT',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="PROPERTIES",
    )

    amount_unit = PropertyTypeAssignment(
        code='AMOUNT_UNIT',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="PROPERTIES",
    )


class TestObject(ObjectType):
    defs = ObjectTypeDef(
        code='TEST_OBJECT',
        description="Object to test validation scripts",
        generated_code_prefix='TEST_OBJECT',
    )

    positive_number = PropertyTypeAssignment(
        code='POSITIVE_NUMBER',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="TEST_PROPERTIES",
    )

    percentage = PropertyTypeAssignment(
        code='PERCENTAGE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="TEST_PROPERTIES",
    )

    prop1 = PropertyTypeAssignment(
        code='PROP1',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="TEST_PROPERTIES",
    )

    prop2 = PropertyTypeAssignment(
        code='PROP2',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="TEST_PROPERTIES",
    )

    prop3 = PropertyTypeAssignment(
        code='PROP3',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="TEST_PROPERTIES",
    )

    rectangle_length = PropertyTypeAssignment(
        code='RECTANGLE_LENGTH',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="TEST_PROPERTIES",
    )

    rectangle_width = PropertyTypeAssignment(
        code='RECTANGLE_WIDTH',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="TEST_PROPERTIES",
    )

    rectangle_area = PropertyTypeAssignment(
        code='RECTANGLE_AREA',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="TEST_PROPERTIES",
    )

    rectangle_length_in_m = PropertyTypeAssignment(
        code='RECTANGLE_LENGTH_IN_M',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="TEST_PROPERTIES",
    )

    rectangle_width_in_m = PropertyTypeAssignment(
        code='RECTANGLE_WIDTH_IN_M',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="TEST_PROPERTIES",
    )

    rectangle_area_in_qm = PropertyTypeAssignment(
        code='RECTANGLE_AREA_IN_QM',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="TEST_PROPERTIES",
    )


class BamActivity(ObjectType):
    defs = ObjectTypeDef(
        code='BAM_ACTIVITY',
        description="Testing bam_area_selector",
        generated_code_prefix='BAM_ACTIVITY',
    )

    name = PropertyTypeAssignment(
        code='$NAME',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM_FIELD_&_AREA",
    )

    bam_field_of_activity = PropertyTypeAssignment(
        code='BAM_FIELD_OF_ACTIVITY',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM_FIELD_&_AREA",
    )

    bam_focus_area = PropertyTypeAssignment(
        code='BAM_FOCUS_AREA',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM_FIELD_&_AREA",
    )

    bam_focus_area_v2 = PropertyTypeAssignment(
        code='BAM_FOCUS_AREA_V2',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM_FIELD_&_AREA",
    )


class Task(ObjectType):
    defs = ObjectTypeDef(
        code='TASK',
        description="Demo object to test interaction",
        generated_code_prefix='TASK',
    )

    name = PropertyTypeAssignment(
        code='$NAME',
        data_type='',
        property_label="",
        description="",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    last_check = PropertyTypeAssignment(
        code='LAST_CHECK',
        data_type='',
        property_label="",
        description="",
        mandatory=True,
        show_in_edit_views=False,
        section="Automation",
    )

    freq_check = PropertyTypeAssignment(
        code='FREQ_CHECK',
        data_type='',
        property_label="",
        description="",
        mandatory=True,
        show_in_edit_views=False,
        section="Automation",
    )

    state_check = PropertyTypeAssignment(
        code='STATE_CHECK',
        data_type='',
        property_label="",
        description="",
        mandatory=True,
        show_in_edit_views=False,
        section="Automation",
    )

    annotations_state = PropertyTypeAssignment(
        code='$ANNOTATIONS_STATE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )


class Chemical(ObjectType):
    defs = ObjectTypeDef(
        code='CHEMICAL',
        description="Chemical Substance//Chemische Substanz Objekttyp",
        generated_code_prefix='CHEM',
    )

    name = PropertyTypeAssignment(
        code='$NAME',
        data_type='',
        property_label="",
        description="",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    alias = PropertyTypeAssignment(
        code='ALIAS',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    iupac_name = PropertyTypeAssignment(
        code='IUPAC_NAME',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    cas_number = PropertyTypeAssignment(
        code='CAS_NUMBER',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    manufacturer = PropertyTypeAssignment(
        code='MANUFACTURER',
        data_type='',
        property_label="",
        description="",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    supplier = PropertyTypeAssignment(
        code='SUPPLIER',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    lot_number = PropertyTypeAssignment(
        code='LOT_NUMBER',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    barcode_external = PropertyTypeAssignment(
        code='BARCODE_EXTERNAL',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    description = PropertyTypeAssignment(
        code='DESCRIPTION',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )

    hazardous_substance = PropertyTypeAssignment(
        code='HAZARDOUS_SUBSTANCE',
        data_type='',
        property_label="",
        description="",
        mandatory=True,
        show_in_edit_views=False,
        section="General Information",
    )

    bam_room = PropertyTypeAssignment(
        code='BAM_ROOM',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_floor = PropertyTypeAssignment(
        code='BAM_FLOOR',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_house = PropertyTypeAssignment(
        code='BAM_HOUSE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_location = PropertyTypeAssignment(
        code='BAM_LOCATION',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    bam_location_complete = PropertyTypeAssignment(
        code='BAM_LOCATION_COMPLETE',
        data_type='',
        property_label="",
        description="",
        mandatory=True,
        show_in_edit_views=False,
        section="BAM Information",
    )

    responsible_person = PropertyTypeAssignment(
        code='RESPONSIBLE_PERSON',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    ba_dyn_test = PropertyTypeAssignment(
        code='BA_DYN_TEST',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="BAM Information",
    )

    mass_molar = PropertyTypeAssignment(
        code='MASS_MOLAR',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Chemical Properties",
    )

    concentration = PropertyTypeAssignment(
        code='CONCENTRATION',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Chemical Properties",
    )

    density_gram_per_cubic_cm = PropertyTypeAssignment(
        code='DENSITY_GRAM_PER_CUBIC_CM',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Chemical Properties",
    )

    date_bottling = PropertyTypeAssignment(
        code='DATE_BOTTLING',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Handling",
    )

    date_opening = PropertyTypeAssignment(
        code='DATE_OPENING',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Handling",
    )

    date_expiration = PropertyTypeAssignment(
        code='DATE_EXPIRATION',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Handling",
    )

    substance_empty = PropertyTypeAssignment(
        code='SUBSTANCE_EMPTY',
        data_type='',
        property_label="",
        description="",
        mandatory=True,
        show_in_edit_views=False,
        section="Handling",
    )

    notes = PropertyTypeAssignment(
        code='NOTES',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Details",
    )

    xmlcomments = PropertyTypeAssignment(
        code='$XMLCOMMENTS',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="Comments",
    )

    annotations_state = PropertyTypeAssignment(
        code='$ANNOTATIONS_STATE',
        data_type='',
        property_label="",
        description="",
        mandatory=False,
        show_in_edit_views=False,
        section="",
    )

