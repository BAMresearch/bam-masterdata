from decouple import config as environ
from pybis import Openbis

# Connect to openBIS
url = environ("URL")
o = Openbis(url)
o.login(environ("USERNAME"), environ("PASSWORD"), save_token=True)

def get_obj_dict():
    # Retrieve object types and convert to dictionary
    otypes = o.get_object_types().df
    otypes_dict = otypes.to_dict(orient="records")
    formatted_dict = {entry["permId"]: entry for entry in otypes_dict}

    # Add properties to each object type
    for obj in o.get_object_types():
        perm_id = obj.permId  # Unique identifier for the object type
        assignments = obj.get_property_assignments()

        if assignments:
            # Convert property assignments to list of dictionaries
            assignments_dict = assignments.df.to_dict(orient="records")

            # Create a dictionary of properties using the correct permId
            properties = {}
            for entry in assignments_dict:
                property_perm_id = (
                    entry.get('permId', {})
                        .get('propertyTypeId', {})
                        .get('permId')
                )
                if property_perm_id:
                    # Include the desired property fields
                    properties[property_perm_id] = {
                        "@type": entry.get("@type", "as.dto.property.PropertyAssignment"),
                        "@id": entry.get("@id", None),
                        "fetchOptions": entry.get("fetchOptions", None),
                        "permId": property_perm_id,
                        "section": entry.get("section", ""),
                        "ordinal": entry.get("ordinal", None),
                        "mandatory": entry.get("mandatory", False),
                        "showInEditView": entry.get("showInEditView", False),
                        "showRawValueInForms": entry.get("showRawValueInForms", False),
                        "semanticAnnotations": entry.get("semanticAnnotations", None),
                        "semanticAnnotationsInherited": entry.get("semanticAnnotationsInherited", False),
                        "registrator": entry.get("registrator", None),
                        "registrationDate": entry.get("registrationDate", None),
                        "plugin": entry.get("plugin", "")
                    }

            for prop in assignments:
                properties[prop.permId].update({
                    "label": prop.label,
                    "description": prop.description,
                    "dataType": prop.dataType
                })     

            # Add properties to the object type in formatted_dict
            formatted_dict[perm_id]["properties"] = properties
        else:
            # If no properties, add an empty dictionary
            formatted_dict[perm_id]["properties"] = {}

    return formatted_dict