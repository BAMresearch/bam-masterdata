from decouple import config as environ
from pybis import Openbis

# Connect to openBIS
url = environ("URL")
o = Openbis(url)
o.login(environ("USERNAME"), environ("PASSWORD"), save_token=True)

print(o.get_collection_types())

