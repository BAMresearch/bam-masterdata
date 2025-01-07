from bam_masterdata.openbis.login import ologin


class OpenbisEntities:
    """
    Class to get openBIS entities and their attributes as dictionaries to be printed in the
    Python modules of `bam_masterdata/datamodel/`.
    """

    def __init__(self):
        self.openbis = ologin()

    def get_collection_dict(self) -> dict:
        """
        Get the collection types from openBIS and return them as a dictionary where the keys
        are the collection type `code` and the value is a dictionary of attributes assigned to that
        collection type.

        Returns:
            dict: Dictionary of collection types with their attributes.
        """
        ctypes = self.openbis.get_collection_types().df
        ctypes_dict = ctypes.to_dict(orient='records')
        formatted_dict = {entry['permId']: entry for entry in ctypes_dict}

        return formatted_dict

    def get_dataset_dict(self) -> dict:
        """
        Get the dataset types from openBIS and return them as a dictionary where the keys
        are the dataset type `code` and the value is a dictionary of attributes assigned to that
        dataset type.

        Returns:
            dict: Dictionary of dataset types with their attributes.
        """
        dtypes = self.openbis.get_dataset_types().df
        dtypes_dict = dtypes.to_dict(orient='records')
        formatted_dict = {entry['permId']: entry for entry in dtypes_dict}

        return formatted_dict

    def get_object_dict(self) -> dict:
        """
        Get the object types from openBIS and return them as a dictionary where the keys
        are the object type `code` and the value is a dictionary of attributes assigned to that
        object type.

        Returns:
            dict: Dictionary of object types with their attributes.
        """
        otypes = self.openbis.get_object_types().df
        otypes_dict = otypes.to_dict(orient='records')
        formatted_dict = {entry['permId']: entry for entry in otypes_dict}

        # Add properties to each object type
        for obj in self.openbis.get_object_types():
            perm_id = obj.permId  # Unique identifier for the object type
            assignments = obj.get_property_assignments()

            if assignments:
                # Convert property assignments to list of dictionaries
                assignments_dict = assignments.df.to_dict(orient='records')

                # Create a dictionary of properties using the correct permId
                properties = {}
                for entry in assignments_dict:
                    property_perm_id = (
                        entry.get('permId', {}).get('propertyTypeId', {}).get('permId')
                    )
                    if property_perm_id:
                        # Include the desired property fields
                        properties[property_perm_id] = {
                            '@type': entry.get(
                                '@type', 'as.dto.property.PropertyAssignment'
                            ),
                            '@id': entry.get('@id', None),
                            'fetchOptions': entry.get('fetchOptions', None),
                            'permId': property_perm_id,
                            'section': entry.get('section', ''),
                            'ordinal': entry.get('ordinal', None),
                            'mandatory': entry.get('mandatory', False),
                            'showInEditView': entry.get('showInEditView', False),
                            'showRawValueInForms': entry.get(
                                'showRawValueInForms', False
                            ),
                            'semanticAnnotations': entry.get(
                                'semanticAnnotations', None
                            ),
                            'semanticAnnotationsInherited': entry.get(
                                'semanticAnnotationsInherited', False
                            ),
                            'registrator': entry.get('registrator', None),
                            'registrationDate': entry.get('registrationDate', None),
                            'plugin': entry.get('plugin', ''),
                        }

                for prop in assignments:
                    properties[prop.permId].update(
                        {
                            'label': prop.label,
                            'description': prop.description,
                            'dataType': prop.dataType,
                        }
                    )

                # Add properties to the object type in formatted_dict
                formatted_dict[perm_id]['properties'] = properties
            else:
                # If no properties, add an empty dictionary
                formatted_dict[perm_id]['properties'] = {}

        return formatted_dict

    def get_property_dict(self) -> dict:
        """
        Get the property types from openBIS and return them as a dictionary where the keys
        are the property type `code` and the value is a dictionary of attributes assigned to that
        property type.

        Returns:
            dict: Dictionary of property types with their attributes.
        """
        ptypes = self.openbis.get_property_types().df
        ptypes_dict = ptypes.to_dict(orient='records')
        formatted_dict = {entry['code']: entry for entry in ptypes_dict}

        return formatted_dict

    def get_vocabulary_dict(self) -> dict:
        """
        Get the vocabulary types from openBIS and return them as a dictionary where the keys
        are the vocabulary type `code` and the value is a dictionary of attributes assigned to that
        vocabulary type.

        Returns:
            dict: Dictionary of vocabulary types with their attributes.
        """
        vtypes = self.openbis.get_vocabularies().df
        vtypes_dict = vtypes.to_dict(orient='records')
        formatted_dict = {entry['code']: entry for entry in vtypes_dict}

        # Add properties to each object type
        for voc in self.openbis.get_vocabularies():
            code = voc.code  # Unique identifier for the object type
            terms = voc.get_terms()

            if terms:
                # Convert property assignments to list of dictionaries
                terms_dict = terms.df.to_dict(orient='records')

                # Create a dictionary of properties using the correct permId
                voc_terms = {}
                for entry in terms_dict:
                    term_code = entry.get('code', {})
                    if term_code:
                        # Include the desired property fields
                        voc_terms[term_code] = {
                            'code': term_code,
                            'description': entry.get('description', ''),
                            'label': entry.get('label', ''),
                        }

                # Add properties to the object type in formatted_dict
                formatted_dict[code]['terms'] = voc_terms
            else:
                # If no properties, add an empty dictionary
                formatted_dict[code]['terms'] = {}

        return formatted_dict
