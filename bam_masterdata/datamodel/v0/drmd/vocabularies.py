from bam_masterdata.metadata.definitions import VocabularyTerm, VocabularyTypeDef
from bam_masterdata.metadata.entities import VocabularyType


class Language(VocabularyType):
    defs = VocabularyTypeDef(
        code="LANGUAGE",
        description="""Language according to ISO 639-1; the term code is the two-letter language code in upper case""",
    )

    en = VocabularyTerm(
        code="EN",
        label="English",
        description="""English (ISO 639-1 code en)""",
    )

    de = VocabularyTerm(
        code="DE",
        label="German",
        description="""German (ISO 639-1 code de)""",
    )


class DrmdDocumentTitle(VocabularyType):
    defs = VocabularyTypeDef(
        code="DRMD_DOCUMENT_TITLE",
        description="""Type of a DRMD document; it decides which requirements of ISO 33401:2024, Table 1 apply (drmd:titleOfTheDocument)""",
    )

    product_information_sheet = VocabularyTerm(
        code="PRODUCT_INFORMATION_SHEET",
        label="Product information sheet",
        description="""Document accompanying a reference material that is not certified (ISO 33401:2024, 3.3; XML value productInformationSheet)""",
    )

    reference_material_certificate = VocabularyTerm(
        code="REFERENCE_MATERIAL_CERTIFICATE",
        label="Reference material certificate",
        description="""Document accompanying a certified reference material (CRM), with certified values, measurement uncertainty and metrological traceability (XML value referenceMaterialCertificate)""",
    )


class DrmdValidityType(VocabularyType):
    defs = VocabularyTypeDef(
        code="DRMD_VALIDITY_TYPE",
        description="""Form in which the period of validity of a DRMD document is stated (drmd:validity, ISO 33401:2024, 5.2.8)""",
    )

    until_revoked = VocabularyTerm(
        code="UNTIL_REVOKED",
        label="Until revoked",
        description="""Valid until the producer withdraws or replaces the document (XML element untilRevoked)""",
    )

    time_after_dispatch = VocabularyTerm(
        code="TIME_AFTER_DISPATCH",
        label="Time after dispatch",
        description="""Valid for a period counted from the dispatch date of the unit (XML element timeAfterDispatch)""",
    )

    specific_time = VocabularyTerm(
        code="SPECIFIC_TIME",
        label="Specific time",
        description="""Valid until a fixed end date (XML element specificTime)""",
    )


class DrmdValueType(VocabularyType):
    defs = VocabularyTypeDef(
        code="DRMD_VALUE_TYPE",
        description="""Form in which the value of a quantity is given, i.e. the choice made in dcc:primitiveQuantityType""",
    )

    si_real = VocabularyTerm(
        code="SI_REAL",
        label="Real",
        description="""One numeric value with a D-SI unit and an optional measurement uncertainty (si:real)""",
    )

    si_hybrid = VocabularyTerm(
        code="SI_HYBRID",
        label="Hybrid",
        description="""The same quantity stated in several units; the member values are linked as parent quantities (si:hybrid)""",
    )

    si_constant = VocabularyTerm(
        code="SI_CONSTANT",
        label="Constant",
        description="""A fundamental or conventional constant with a D-SI unit (si:constant)""",
    )

    si_real_list_xml_list = VocabularyTerm(
        code="SI_REAL_LIST_XML_LIST",
        label="Real list",
        description="""A list of numeric values of one quantity; the list elements are linked as parent quantities (si:realListXMLList)""",
    )

    dcc_no_quantity = VocabularyTerm(
        code="DCC_NO_QUANTITY",
        label="No quantity",
        description="""A non-numeric statement given in place of a value (dcc:noQuantity)""",
    )

    dcc_chars_xml_list = VocabularyTerm(
        code="DCC_CHARS_XML_LIST",
        label="Character list",
        description="""A whitespace-separated list of tokens, e.g. codes or categories (dcc:charsXMLList)""",
    )


class DrmdQuantityRole(VocabularyType):
    defs = VocabularyTypeDef(
        code="DRMD_QUANTITY_ROLE",
        description="""Place of a quantity in a DRMD document; needed where one object can hold quantities of different roles""",
    )

    result_data = VocabularyTerm(
        code="RESULT_DATA",
        label="Result data",
        description="""Value of a result (drmd:result/drmd:data)""",
    )

    minimum_sample_size = VocabularyTerm(
        code="MINIMUM_SAMPLE_SIZE",
        label="Minimum sample size",
        description="""Minimum sample size of the material (drmd:minimumSampleSize, ISO 33401:2024, 5.2.7)""",
    )

    item_quantities = VocabularyTerm(
        code="ITEM_QUANTITIES",
        label="Item quantity",
        description="""Quantity describing the unit as supplied, e.g. nominal mass, dimensions or number of items (drmd:itemQuantities)""",
    )

    used_method_quantities = VocabularyTerm(
        code="USED_METHOD_QUANTITIES",
        label="Method quantity",
        description="""Quantity belonging to a measurement procedure (dcc:usedMethodQuantities)""",
    )


class DrmdUncertaintyType(VocabularyType):
    defs = VocabularyTypeDef(
        code="DRMD_UNCERTAINTY_TYPE",
        description="""Form of the univariate measurement uncertainty of a D-SI value (si:measurementUncertaintyUnivariate)""",
    )

    standard_mu = VocabularyTerm(
        code="STANDARD_MU",
        label="Standard uncertainty",
        description="""Standard uncertainty (si:standardMU)""",
    )

    expanded_mu = VocabularyTerm(
        code="EXPANDED_MU",
        label="Expanded uncertainty",
        description="""Expanded uncertainty with coverage factor and coverage probability (si:expandedMU)""",
    )

    coverage_interval_mu = VocabularyTerm(
        code="COVERAGE_INTERVAL_MU",
        label="Coverage interval",
        description="""Coverage interval with standard uncertainty and coverage probability, e.g. for asymmetric uncertainties (si:coverageIntervalMU)""",
    )


class DrmdConformity(VocabularyType):
    defs = VocabularyTypeDef(
        code="DRMD_CONFORMITY",
        description="""Status of a conformity statement according to the DCC schema (dcc:stringConformityStatementStatusType)""",
    )

    # `pass` is a reserved word in Python, hence the trailing underscore
    pass_ = VocabularyTerm(
        code="PASS",
        label="Pass",
        description="""Status pass of the DCC conformity statement (XML value pass)""",
    )

    fail = VocabularyTerm(
        code="FAIL",
        label="Fail",
        description="""Status fail of the DCC conformity statement (XML value fail)""",
    )

    conditional_pass = VocabularyTerm(
        code="CONDITIONAL_PASS",
        label="Conditional pass",
        description="""Status conditionalPass of the DCC conformity statement, used as defined there (XML value conditionalPass)""",
    )

    conditional_fail = VocabularyTerm(
        code="CONDITIONAL_FAIL",
        label="Conditional fail",
        description="""Status conditionalFail of the DCC conformity statement, used as defined there (XML value conditionalFail)""",
    )

    no_pass = VocabularyTerm(
        code="NO_PASS",
        label="No pass",
        description="""Status noPass of the DCC conformity statement, used as defined there (XML value noPass)""",
    )

    no_fail = VocabularyTerm(
        code="NO_FAIL",
        label="No fail",
        description="""Status noFail of the DCC conformity statement, used as defined there (XML value noFail)""",
    )
