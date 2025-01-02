from decouple import config as environ
from pybis import Openbis

# Connect to openBIS
url = environ("URL")
o = Openbis(url)
o.login(environ("USERNAME"), environ("PASSWORD"), save_token=True)

def get_coll_dict():
    # Retrieve object types and convert to dictionary
    ctypes = o.get_collection_types().df
    ctypes_dict = ctypes.to_dict(orient="records")
    formatted_dict = {entry["permId"]: entry for entry in ctypes_dict}

    return formatted_dict