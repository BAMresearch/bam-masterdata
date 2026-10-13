from bam_masterdata.metadata.definitions import VocabularyTerm, VocabularyTypeDef
from bam_masterdata.metadata.entities import VocabularyType

# Every vocabulary in this module mirrors an enumeration of the DRMD schema (drmd.xsd)
# or of one of its supporting schemas (DCC, D-SI). The term `label` always holds the
# exact token that is written to the XML document, so a generator can emit it verbatim.
# The term `code` is the same token in openBIS notation (upper case, words separated by
# underscores). Terms are listed in the order of the schema enumeration.


class DrmdDocumentTitle(VocabularyType):
    # Schema: drmd:titleOfDocumentType (drmd:coreData/drmd:titleOfTheDocument)
    defs = VocabularyTypeDef(
        code="DRMD_DOCUMENT_TITLE",
        description="""Type of a DRMD document (drmd:titleOfTheDocument); it decides which requirements of ISO 33401:2024, Table 1 apply//Art eines DRMD-Dokuments (drmd:titleOfTheDocument); sie legt fest, welche Anforderungen der ISO 33401:2024, Tabelle 1 gelten""",
    )

    product_information_sheet = VocabularyTerm(
        code="PRODUCT_INFORMATION_SHEET",
        label="productInformationSheet",
        description="""Product information sheet accompanying a reference material that is not certified (ISO 33401:2024, 3.3)//Produktinformationsblatt für ein nicht zertifiziertes Referenzmaterial (ISO 33401:2024, 3.3)""",
    )

    reference_material_certificate = VocabularyTerm(
        code="REFERENCE_MATERIAL_CERTIFICATE",
        label="referenceMaterialCertificate",
        description="""Reference material certificate accompanying a certified reference material (CRM), with certified values, measurement uncertainty and metrological traceability//Referenzmaterialzertifikat für ein zertifiziertes Referenzmaterial (ZRM) mit zertifizierten Werten, Messunsicherheit und metrologischer Rückführung""",
    )


class DrmdValidityType(VocabularyType):
    # Schema: drmd:ValidityType (xs:choice of drmd:untilRevoked, drmd:timeAfterDispatch, drmd:specificTime)
    defs = VocabularyTypeDef(
        code="DRMD_VALIDITY_TYPE",
        description="""Form in which the period of validity of a DRMD document is stated (drmd:validity, ISO 33401:2024, 5.2.8)//Form, in der die Gültigkeitsdauer eines DRMD-Dokuments angegeben wird (drmd:validity, ISO 33401:2024, 5.2.8)""",
    )

    until_revoked = VocabularyTerm(
        code="UNTIL_REVOKED",
        label="untilRevoked",
        description="""Valid until the producer withdraws or replaces the document//Gültig, bis der Hersteller das Dokument zurückzieht oder ersetzt""",
    )

    time_after_dispatch = VocabularyTerm(
        code="TIME_AFTER_DISPATCH",
        label="timeAfterDispatch",
        description="""Valid for a period counted from the dispatch date of the unit//Gültig für einen Zeitraum ab dem Versanddatum der Einheit""",
    )

    specific_time = VocabularyTerm(
        code="SPECIFIC_TIME",
        label="specificTime",
        description="""Valid until a fixed end date//Gültig bis zu einem festen Enddatum""",
    )


class DrmdRefType(VocabularyType):
    # Schema: drmd:refTypesType (attribute @refType of DRMD-typed elements)
    defs = VocabularyTypeDef(
        code="DRMD_REF_TYPE",
        description="""Controlled list for the refType attribute of DRMD elements (drmd:refTypesType)//Kontrollierte Liste für das refType-Attribut von DRMD-Elementen (drmd:refTypesType)""",
    )

    basic_certificate_identification = VocabularyTerm(
        code="BASIC_CERTIFICATE_IDENTIFICATION",
        label="basic_certificateIdentification",
        description="""The element identifies the document//Das Element identifiziert das Dokument""",
    )

    basic_measured_value = VocabularyTerm(
        code="BASIC_MEASURED_VALUE",
        label="basic_measuredValue",
        description="""The element is a measured value (a quantity)//Das Element ist ein Messwert (eine Größe)""",
    )


class DrmdValueType(VocabularyType):
    # Schema: xs:choice inside dcc:primitiveQuantityType (extended by drmd:quantityType).
    # The complex-valued choices si:complex and si:complexListXMLList are not modelled;
    # see README.md, section 13 "Scope".
    defs = VocabularyTypeDef(
        code="DRMD_VALUE_TYPE",
        description="""Encoding of the value of a quantity, i.e. the choice made inside dcc:primitiveQuantityType//Kodierung des Werts einer Größe, d. h. die Auswahl innerhalb von dcc:primitiveQuantityType""",
    )

    si_real = VocabularyTerm(
        code="SI_REAL",
        label="si:real",
        description="""One numeric value with a D-SI unit and an optional measurement uncertainty//Ein Zahlenwert mit D-SI-Einheit und optionaler Messunsicherheit""",
    )

    si_hybrid = VocabularyTerm(
        code="SI_HYBRID",
        label="si:hybrid",
        description="""The same quantity stated in several units; the member values are linked as parent quantities//Dieselbe Größe in mehreren Einheiten angegeben; die Einzelwerte sind als Eltern-Größen verknüpft""",
    )

    si_constant = VocabularyTerm(
        code="SI_CONSTANT",
        label="si:constant",
        description="""A constant (e.g. a fundamental or conventional constant) with a D-SI unit//Eine Konstante (z. B. eine Natur- oder konventionelle Konstante) mit D-SI-Einheit""",
    )

    si_real_list_xml_list = VocabularyTerm(
        code="SI_REAL_LIST_XML_LIST",
        label="si:realListXMLList",
        description="""A list of numeric values of one quantity; the list elements are linked as parent quantities//Eine Liste von Zahlenwerten einer Größe; die Listenelemente sind als Eltern-Größen verknüpft""",
    )

    dcc_no_quantity = VocabularyTerm(
        code="DCC_NO_QUANTITY",
        label="dcc:noQuantity",
        description="""A non-numeric statement given in place of a value//Eine nicht-numerische Angabe anstelle eines Werts""",
    )

    dcc_chars_xml_list = VocabularyTerm(
        code="DCC_CHARS_XML_LIST",
        label="dcc:charsXMLList",
        description="""A whitespace-separated list of tokens, e.g. codes or categories//Eine durch Leerzeichen getrennte Liste von Zeichenketten, z. B. Codes oder Kategorien""",
    )


class DrmdQuantityRole(VocabularyType):
    # Schema: the containers that hold dcc:primitiveQuantityType elements in a DRMD document
    defs = VocabularyTypeDef(
        code="DRMD_QUANTITY_ROLE",
        description="""Place of a quantity in a DRMD document; required where one object can hold quantities of different roles//Stelle einer Größe in einem DRMD-Dokument; erforderlich, wo ein Objekt Größen unterschiedlicher Rollen enthalten kann""",
    )

    result_data = VocabularyTerm(
        code="RESULT_DATA",
        label="data",
        description="""Value of a result (drmd:result/drmd:data)//Wert eines Ergebnisses (drmd:result/drmd:data)""",
    )

    minimum_sample_size = VocabularyTerm(
        code="MINIMUM_SAMPLE_SIZE",
        label="minimumSampleSize",
        description="""Minimum sample size of the material (drmd:minimumSampleSize, ISO 33401:2024, 5.2.7)//Mindestprobenmenge des Materials (drmd:minimumSampleSize, ISO 33401:2024, 5.2.7)""",
    )

    item_quantities = VocabularyTerm(
        code="ITEM_QUANTITIES",
        label="itemQuantities",
        description="""Quantity describing the unit as supplied, e.g. nominal mass, dimensions or number of items (drmd:itemQuantities)//Größe, die die gelieferte Einheit beschreibt, z. B. Nennmasse, Abmessungen oder Stückzahl (drmd:itemQuantities)""",
    )

    used_method_quantities = VocabularyTerm(
        code="USED_METHOD_QUANTITIES",
        label="usedMethodQuantities",
        description="""Quantity belonging to a measurement procedure (dcc:usedMethodQuantities)//Größe, die zu einem Messverfahren gehört (dcc:usedMethodQuantities)""",
    )


class DrmdUncertaintyType(VocabularyType):
    # Schema: xs:choice inside si:measurementUncertaintyUnivariateType (D-SI v2.2.1).
    # The deprecated D-SI forms si:expandedUnc and si:coverageInterval are mapped onto
    # EXPANDED_MU and COVERAGE_INTERVAL_MU, which carry the same information.
    defs = VocabularyTypeDef(
        code="DRMD_UNCERTAINTY_TYPE",
        description="""Form of the univariate measurement uncertainty of a D-SI value (si:measurementUncertaintyUnivariate)//Form der univariaten Messunsicherheit eines D-SI-Werts (si:measurementUncertaintyUnivariate)""",
    )

    standard_mu = VocabularyTerm(
        code="STANDARD_MU",
        label="standardMU",
        description="""Standard uncertainty//Standardunsicherheit""",
    )

    expanded_mu = VocabularyTerm(
        code="EXPANDED_MU",
        label="expandedMU",
        description="""Expanded uncertainty with coverage factor and coverage probability//Erweiterte Unsicherheit mit Erweiterungsfaktor und Überdeckungswahrscheinlichkeit""",
    )

    coverage_interval_mu = VocabularyTerm(
        code="COVERAGE_INTERVAL_MU",
        label="coverageIntervalMU",
        description="""Coverage interval with standard uncertainty and coverage probability, e.g. for asymmetric uncertainties//Überdeckungsintervall mit Standardunsicherheit und Überdeckungswahrscheinlichkeit, z. B. für asymmetrische Unsicherheiten""",
    )


class DrmdConformity(VocabularyType):
    # Schema: dcc:stringConformityStatementStatusType (DCC v3.3.0), used by dcc:metaData/dcc:conformity
    defs = VocabularyTypeDef(
        code="DRMD_CONFORMITY",
        description="""Status of a conformity statement according to the DCC schema (dcc:stringConformityStatementStatusType)//Status einer Konformitätsaussage gemäß DCC-Schema (dcc:stringConformityStatementStatusType)""",
    )

    pass_ = VocabularyTerm(
        code="PASS",
        label="pass",
        description="""Pass//Bestanden""",
    )

    fail = VocabularyTerm(
        code="FAIL",
        label="fail",
        description="""Fail//Nicht bestanden""",
    )

    conditional_pass = VocabularyTerm(
        code="CONDITIONAL_PASS",
        label="conditionalPass",
        description="""Conditional pass//Bedingt bestanden""",
    )

    conditional_fail = VocabularyTerm(
        code="CONDITIONAL_FAIL",
        label="conditionalFail",
        description="""Conditional fail//Bedingt nicht bestanden""",
    )

    no_pass = VocabularyTerm(
        code="NO_PASS",
        label="noPass",
        description="""Status noPass of the DCC conformity statement, used as defined there//Status noPass der DCC-Konformitätsaussage, wie dort festgelegt verwendet""",
    )

    no_fail = VocabularyTerm(
        code="NO_FAIL",
        label="noFail",
        description="""Status noFail of the DCC conformity statement, used as defined there//Status noFail der DCC-Konformitätsaussage, wie dort festgelegt verwendet""",
    )
