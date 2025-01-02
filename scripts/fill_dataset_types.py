from decouple import config as environ
from pybis import Openbis

# Connect to openBIS
url = environ("URL")
o = Openbis(url)
o.login(environ("USERNAME"), environ("PASSWORD"), save_token=True)

def get_dataset_dict():
    # Retrieve object types and convert to dictionary
    dtypes = o.get_dataset_types().df
    dtypes_dict = dtypes.to_dict(orient="records")
    formatted_dict = {entry["permId"]: entry for entry in dtypes_dict}

    return formatted_dict