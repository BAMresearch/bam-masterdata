from bam_masterdata.openbis.login import ologin


class OpenbisEntities:
    """
    Class to get openBIS entities and their attributes as dictionaries to be printed in the
    Python modules of `bam_masterdata/datamodel/`.
    """

    def __init__(self, url: str = ""):
        self.openbis = ologin(url=url)

    def _get_formatted_dict(self, entity_name: str):
        # entity_name is property_types, collection_types, dataset_types, object_types, or vocabularies
        entity_types = getattr(self.openbis, f"get_{entity_name}")().df.to_dict(
            orient="records"
        )
        return {entry["code"]: entry for entry in entity_types}

    def _assign_properties(self, entity_name: str, formatted_dict: dict) -> None:
        for entity in getattr(self.openbis, f"get_{entity_name}")():
            perm_id = entity.permId  # Unique identifier for the entity
            assignments = entity.get_property_assignments()

            if assignments:
                # Convert property assignments to list of dictionaries
                assignments_dict = assignments.df.to_dict(orient="records")

                # Create a dictionary of properties using the correct permId
                properties = {}
                for entry in assignments_dict:
                    property_perm_id = self.openbis.get_property_type(
                        entry.get("code", {})
                    ).permId
                    if property_perm_id:
                        # Include the desired property fields
                        properties[property_perm_id] = {
                            "@type": entry.get(
                                "@type", "as.dto.property.PropertyAssignment"
                            ),
                            "@id": entry.get("@id", None),
                            "fetchOptions": entry.get("fetchOptions", None),
                            "permId": property_perm_id,
                            "section": entry.get("section", ""),
                            "ordinal": entry.get("ordinal", None),
                            "mandatory": entry.get("mandatory", False),
                            "showInEditView": entry.get("showInEditView", False),
                            "showRawValueInForms": entry.get(
                                "showRawValueInForms", False
                            ),
                            "semanticAnnotations": entry.get(
                                "semanticAnnotations", None
                            ),
                            "semanticAnnotationsInherited": entry.get(
                                "semanticAnnotationsInherited", False
                            ),
                            "registrator": entry.get("registrator", None),
                            "registrationDate": entry.get("registrationDate", None),
                            "plugin": entry.get("plugin", ""),
                        }
                for prop in assignments:
                    prop = prop.get_property_type()
                    properties[prop.permId].update(
                        {
                            "label": prop.label,
                            "description": prop.description,
                            "dataType": prop.dataType,
                        }
                    )

                # Add properties to the object type in formatted_dict
                formatted_dict[perm_id]["properties"] = properties
            else:
                # If no properties, add an empty dictionary
                formatted_dict[perm_id]["properties"] = {}

    def get_property_dict(self) -> dict:
        """
        Get the property types from openBIS and return them as a dictionary where the keys
        are the property type `code` and the value is a dictionary of attributes assigned to that
        property type.

        Returns:
            dict: Dictionary of property types with their attributes.
        """
        formatted_dict = self._get_formatted_dict("property_types")

        # We return the sorted dictionary in order to have a consistent order for inheritance
        return dict(sorted(formatted_dict.items(), key=lambda item: item[0].count(".")))

    def get_collection_dict(self) -> dict:
        """
        Get the collection types from openBIS and return them as a dictionary where the keys
        are the collection type `code` and the value is a dictionary of attributes assigned to that
        collection type.

        Returns:
            dict: Dictionary of collection types with their attributes.
        """
        formatted_dict = self._get_formatted_dict("collection_types")
        self._assign_properties(
            entity_name="collection_types", formatted_dict=formatted_dict
        )

        # We return the sorted dictionary in order to have a consistent order for inheritance
        return dict(sorted(formatted_dict.items(), key=lambda item: item[0].count(".")))

    def get_dataset_dict(self) -> dict:
        """
        Get the dataset types from openBIS and return them as a dictionary where the keys
        are the dataset type `code` and the value is a dictionary of attributes assigned to that
        dataset type.

        Returns:
            dict: Dictionary of dataset types with their attributes.
        """
        formatted_dict = self._get_formatted_dict("dataset_types")
        self._assign_properties(
            entity_name="dataset_types", formatted_dict=formatted_dict
        )

        # We return the sorted dictionary in order to have a consistent order for inheritance
        return dict(sorted(formatted_dict.items(), key=lambda item: item[0].count(".")))

    def get_object_dict(self) -> dict:
        """
        Get the object types from openBIS and return them as a dictionary where the keys
        are the object type `code` and the value is a dictionary of attributes assigned to that
        object type.

        Returns:
            dict: Dictionary of object types with their attributes.
        """
        formatted_dict = self._get_formatted_dict("object_types")
        self._assign_properties(
            entity_name="object_types", formatted_dict=formatted_dict
        )

        # We return the sorted dictionary in order to have a consistent order for inheritance
        return dict(sorted(formatted_dict.items(), key=lambda item: item[0].count(".")))

    def get_vocabulary_dict(self) -> dict:
        """
        Get the vocabulary types from openBIS and return them as a dictionary where the keys
        are the vocabulary type `code` and the value is a dictionary of attributes assigned to that
        vocabulary type.

        Returns:
            dict: Dictionary of vocabulary types with their attributes.
        """
        formatted_dict = self._get_formatted_dict("vocabularies")

        # Add properties to each object type
        for voc in self.openbis.get_vocabularies():
            code = voc.code  # Unique identifier for the object type

            # BAM_FLOOR, BAM_HOUSE, BAM_LOCATION, BAM_LOCATION_COMPLETE, BAM_OE, BAM_ROOM, PERSON_STATUS
            # are not exported due to containing sensitive information
            if code in [
                "BAM_FLOOR",
                "BAM_HOUSE",
                "BAM_LOCATION",
                "BAM_LOCATION_COMPLETE",
                "BAM_OE",
                "BAM_ROOM",
                "PERSON_STATUS",
            ]:
                continue
            terms = voc.get_terms()

            if terms:
                # Convert property assignments to list of dictionaries
                terms_dict = terms.df.to_dict(orient="records")

                # Create a dictionary of properties using the correct permId
                voc_terms = {}
                for entry in terms_dict:
                    term_code = entry.get("code", {})
                    if term_code:
                        # Include the desired property fields
                        voc_terms[term_code] = {
                            "code": term_code,
                            "description": entry.get("description", ""),
                            "label": entry.get("label", ""),
                        }

                # Add properties to the object type in formatted_dict
                formatted_dict[code]["terms"] = voc_terms
            else:
                # If no properties, add an empty dictionary
                formatted_dict[code]["terms"] = {}

        # We return the sorted dictionary in order to have a consistent order for inheritance
        return dict(sorted(formatted_dict.items(), key=lambda item: item[0].count(".")))
