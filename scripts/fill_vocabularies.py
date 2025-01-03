from decouple import config as environ
from pybis import Openbis

# Connect to openBIS
url = environ("URL")
o = Openbis(url)
o.login(environ("USERNAME"), environ("PASSWORD"), save_token=True)

def get_voc_dict():
    # Retrieve object types and convert to dictionary
    vtypes = o.get_vocabularies().df
    vtypes_dict = vtypes.to_dict(orient="records")
    formatted_dict = {entry["code"]: entry for entry in vtypes_dict}

    # Add properties to each object type
    for voc in o.get_vocabularies():
        code = voc.code  # Unique identifier for the object type
        terms = voc.get_terms()

        if terms:
            # Convert property assignments to list of dictionaries
            terms_dict = terms.df.to_dict(orient="records")

            # Create a dictionary of properties using the correct permId
            voc_terms = {}
            for entry in terms_dict:
                term_code = (
                    entry.get('code', {})
                )
                if term_code:
                    # Include the desired property fields
                    voc_terms[term_code] = {
                        "code": term_code,
                        "description": entry.get("description", ""),
                        "label": entry.get("label", "")
                    }

            # Add properties to the object type in formatted_dict
            formatted_dict[code]["terms"] = voc_terms
        else:
            # If no properties, add an empty dictionary
            formatted_dict[code]["terms"] = {}

    return formatted_dict