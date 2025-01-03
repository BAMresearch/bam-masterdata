from decouple import config as environ
from pybis import Openbis

# Connect to openBIS
url = environ("URL")
o = Openbis(url)
o.login(environ("USERNAME"), environ("PASSWORD"), save_token=True)

def get_prop_dict():
    # Retrieve object types and convert to dictionary
    ptypes = o.get_property_types().df
    ptypes_dict = ptypes.to_dict(orient="records")
    formatted_dict = {entry["code"]: entry for entry in ptypes_dict}

    return formatted_dict