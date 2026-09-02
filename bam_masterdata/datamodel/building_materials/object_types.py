from bam_masterdata.datamodel.object_types import Sample
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment


class BuildingMaterialsSpecimen(Sample):
    defs = ObjectTypeDef(
        code="SAMPLE.BUILDING_MATERIALS_SPECIMEN",
        description="""A generic sample used for building material tests, such as compressive strength tests.//Ein Standardprüfkörper, der für Baustoffprüfungen, wie beispielsweise Druckfestigkeitsprüfungen, verwendet wird.""",
        generated_code_prefix="SAM.BMS",
    )

    psp_number = PropertyTypeAssignment(
        code="PSP_NUMBER",
        data_type="VARCHAR",
        property_label="PSP Number",
        description="""Identifier or project-specific PSP number associated with the sample.//Kennung bzw. projektspezifische PSP-Nummer, die der Probe zugeordnet ist.""",
        mandatory=False,
        section="Specimen Information",
    )

    building_material_type = PropertyTypeAssignment(
        code="BUILDING_MATERIAL_TYPE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BUILDING_MATERIAL_TYPE",
        property_label="Building material type",
        description="""General category of building material from which the sample consists, such as mineral, bituminous, plastic, or wood-based material.//Allgemeine Kategorie des Baustoffs, aus dem die Probe besteht, z. B. mineralischer, bituminöser, Kunststoff- oder Holzwerkstoff.""",
        mandatory=True,
        section="Specimen Information",
    )

    building_material_details = PropertyTypeAssignment(
        code="BUILDING_MATERIAL_DETAILS",
        data_type="MULTILINE_VARCHAR",
        property_label="Building material details",
        description="""Additional information describing the building material that is not captured by the material type, such as composition, grade, product designation, or other relevant characteristics.//Zusätzliche Angaben zum Baustoff, die nicht durch den Baustofftyp abgedeckt sind, z. B. Zusammensetzung, Sorte, Produktbezeichnung oder andere relevante Eigenschaften.""",
        mandatory=False,
        section="Specimen Information",
    )

    date_of_production = PropertyTypeAssignment(
        code="DATE_OF_PRODUCTION",
        data_type="DATE",
        property_label="Date of production",
        description="""Date on which the sample or the material represented by the sample was produced or prepared.//Datum, an dem die Probe bzw. das durch die Probe repräsentierte Material hergestellt oder angefertigt wurde.""",
        mandatory=False,
        section="Specimen Information",
    )

    sample_age_in_days = PropertyTypeAssignment(
        code="SAMPLE_AGE_IN_DAYS",
        data_type="INTEGER",
        property_label="Sample age",
        units="days",
        description="""Age of the sample in days at the relevant time of characterization or testing.//Alter der Probe in Tagen zum relevanten Zeitpunkt der Charakterisierung oder Prüfung.""",
        mandatory=False,
        section="Specimen Information",
    )

    sample_dimensions_set_points = PropertyTypeAssignment(
        code="SAMPLE_DIMENSIONS_SET_POINTS",
        data_type="VARCHAR",
        property_label="Sample dimensions set points",
        description="""Nominal or target dimensions of the sample, including all dimensions required to describe its geometry, for example "100 mm x 100 mm x 100 mm".//Nenn- bzw. Sollmaße der Probe einschließlich aller zur Beschreibung ihrer Geometrie erforderlichen Abmessungen, z. B. "100 mm x 100 mm x 100 mm".""",
        mandatory=False,
        section="Specimen Information",
    )

    density_kg_per_cubic_meter = PropertyTypeAssignment(
        code="DENSITY_KG_PER_CUBIC_METER",
        data_type="REAL",
        units="kg/m^3",
        property_label="Density",
        description="""Density of the sample expressed in kilograms per cubic metre.//Dichte der Probe in Kilogramm pro Kubikmeter.""",
        mandatory=False,
        section="Specimen Information",
    )

    sample_geometry = PropertyTypeAssignment(
        code="SAMPLE_GEOMETRY",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="SAMPLE_GEOMETRY",
        property_label="Sample geometry",
        description="""Geometric shape of the sample, used to classify its overall sample geometry.//Geometrische Form der Probe zur Klassifizierung ihrer grundlegenden Probengeometrie.""",
        mandatory=False,
        section="Specimen Information",
    )

    sample_origin = PropertyTypeAssignment(
        code="SAMPLE_ORIGIN",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="SAMPLE_ORIGIN",
        property_label="Sample origin",
        description="""Origin of the sample, describing where or how the sampled material was obtained or produced.//Herkunft der Probe mit Angabe, woher bzw. auf welche Weise das beprobte Material gewonnen oder hergestellt wurde.""",
        mandatory=False,
        section="Specimen Information",
    )

    building_name = PropertyTypeAssignment(
        code="BUILDING_NAME",
        data_type="MULTILINE_VARCHAR",
        property_label="Building name",
        description="""Name or designation of the building or structure from which the sample originates, if applicable.//Name oder Bezeichnung des Bauwerks, aus dem die Probe stammt, sofern zutreffend.""",
        mandatory=False,
        section="Specimen Information",
    )

    building_material_test_standard = PropertyTypeAssignment(
        code="BUILDING_MATERIAL_TEST_STANDARD",
        data_type="VARCHAR",
        property_label="Building material test standard",
        description="""Standard, technical specification, or other normative document according to which the building-material test is performed.//Norm, technische Spezifikation oder sonstiges Regelwerk, nach dem die Baustoffprüfung durchgeführt wird.""",
        mandatory=False,
        section="Specimen Information",
    )

    building_materials_test_machine = PropertyTypeAssignment(
        code="BUILDING_MATERIALS_TEST_MACHINE",
        data_type="CONTROLLEDVOCABULARY",
        vocabulary_code="BUILDING_MATERIALS_TEST_MACHINE",
        property_label="Test machine",
        description="""Machine or testing system used to perform the building-material test.//Maschine bzw. Prüfsystem, mit dem die Baustoffprüfung durchgeführt wird.""",
        mandatory=False,
        section="Specimen Information",
    )

    building_materials_test_id = PropertyTypeAssignment(
        code="BUILDING_MATERIALS_TEST_ID",
        data_type="VARCHAR",
        property_label="Test ID",
        description="""Identifier used to uniquely reference the test performed on the sample.//Kennung zur eindeutigen Referenzierung der an der Probe durchgeführten Prüfung.""",
        mandatory=False,
        section="Specimen Information",
    )

    building_materials_test_result = PropertyTypeAssignment(
        code="BUILDING_MATERIALS_TEST_RESULT",
        data_type="MULTILINE_VARCHAR",
        property_label="Test result",
        description="""Result or summary of the result obtained from the building-material test.//Ergebnis bzw. Zusammenfassung des Ergebnisses der durchgeführten Baustoffprüfung.""",
        mandatory=True,
        section="Specimen Information",
    )


class ConcreteMixture(Sample):
    defs = ObjectTypeDef(
        code="SAMPLE.CONCRETE_MIXTURE",
        description="""CA concrete mixture representing the composition and fresh-state characteristics of concrete from which samples may be prepared or building-material tests may be performed.//Eine Betonmischung, die die Zusammensetzung und Frischbetoneigenschaften eines Betons beschreibt, aus dem Proben hergestellt oder Baustoffprüfungen durchgeführt werden können.""",
        generated_code_prefix="SAM.CON_MIX",
    )

    binder = PropertyTypeAssignment(
        code="BINDER",
        data_type="MULTILINE_VARCHAR",
        property_label="Binder",
        description="""Description of the binder system used in the concrete mixture, including its constituent binder materials and relevant specifications where known.//Beschreibung des in der Betonmischung verwendeten Bindemittelsystems einschließlich der enthaltenen Bindemittel und, soweit bekannt, relevanter Spezifikationen.""",
        mandatory=False,
        section="Concrete Information",
    )

    water_to_cement_ratio = PropertyTypeAssignment(
        code="WATER_TO_CEMENT_RATIO",
        data_type="MULTILINE_VARCHAR",
        property_label="Water-to-cement ratio",
        description="""Water-to-cement ratio of the concrete mixture, or a description of how the ratio was determined when it cannot be represented by a single value.//Wasser-Zement-Wert der Betonmischung bzw. Beschreibung seiner Bestimmung, wenn dieser nicht durch einen einzelnen Wert dargestellt werden kann.""",
        mandatory=False,
        section="Concrete Information",
    )

    consistency = PropertyTypeAssignment(
        code="CONSISTENCY",
        data_type="MULTILINE_VARCHAR",
        property_label="Consistency",
        description="""Consistency of the fresh concrete, including the measured value, consistency class, test method, or other relevant information where available.//Konsistenz des Frischbetons einschließlich Messwert, Konsistenzklasse, Prüfverfahren oder anderer relevanter Angaben, sofern verfügbar.""",
        mandatory=False,
        section="Concrete Information",
    )

    fresh_concrete_density = PropertyTypeAssignment(
        code="FRESH_CONCRETE_DENSITY",
        data_type="MULTILINE_VARCHAR",
        property_label="Fresh concrete density",
        description="""Density of the concrete mixture in its fresh state, including the value and unit or other relevant measurement information.//Dichte der Betonmischung im frischen Zustand einschließlich Wert und Einheit bzw. weiterer relevanter Messangaben.""",
        mandatory=False,
        section="Concrete Information",
    )

    air_voids_content = PropertyTypeAssignment(
        code="AIR_VOIDS_CONTENT",
        data_type="MULTILINE_VARCHAR",
        property_label="Air voids content",
        description="""Air content or air-void content determined for the fresh concrete, including the value, unit, and measurement method where available.//Bestimmter Luftgehalt bzw. Luftporengehalt des Frischbetons einschließlich Wert, Einheit und Messverfahren, sofern verfügbar.""",
        mandatory=False,
        section="Concrete Information",
    )

    fresh_concrete_temperature = PropertyTypeAssignment(
        code="FRESH_CONCRETE_TEMPERATURE",
        data_type="MULTILINE_VARCHAR",
        property_label="Fresh concrete temperature",
        description="""Temperature of the fresh concrete at the relevant time of preparation, sampling, or testing, including the value and unit.//Temperatur des Frischbetons zum relevanten Zeitpunkt der Herstellung, Probenahme oder Prüfung einschließlich Wert und Einheit.""",
        mandatory=False,
        section="Concrete Information",
    )

    aggregate = PropertyTypeAssignment(
        code="AGGREGATE",
        data_type="MULTILINE_VARCHAR",
        property_label="Aggregate",
        description="""Description of the aggregate or aggregate mixture used in the concrete, including information such as aggregate type, source, grading, or particle-size fractions where available.//Beschreibung der im Beton verwendeten Gesteinskörnung bzw. Gesteinskörnungsmischung, einschließlich Angaben wie Art, Herkunft, Sieblinie oder Korngrößenfraktionen, sofern verfügbar.""",
        mandatory=False,
        section="Concrete Information",
    )

    admixtures = PropertyTypeAssignment(
        code="ADDMIXTURES",
        data_type="MULTILINE_VARCHAR",
        property_label="Admixtures",
        description="""Description of concrete admixtures added to modify properties of the fresh or hardened concrete, including type, product, and dosage where available.//Beschreibung der Betonzusatzmittel zur gezielten Beeinflussung der Eigenschaften des Frisch- oder Festbetons einschließlich Art, Produkt und Dosierung, sofern verfügbar.""",
        mandatory=False,
        section="Concrete Information",
    )

    additives = PropertyTypeAssignment(
        code="ADDITIVES",
        data_type="MULTILINE_VARCHAR",
        property_label="Additives",
        description="""Description of concrete additions used as constituents of the mixture, including type, material, and quantity where available.//Beschreibung der als Bestandteil der Betonmischung verwendeten Betonzusatzstoffe einschließlich Art, Material und Menge, sofern verfügbar.""",
        mandatory=False,
        section="Concrete Information",
    )
