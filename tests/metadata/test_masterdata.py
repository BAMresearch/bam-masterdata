from decouple import config as environ
from pybis import Openbis

# Connect to openBIS
url = environ("URL")
o = Openbis(url)
o.login(environ("USERNAME"), environ("PASSWORD"), save_token=True)

terms_dict = o.get_vocabulary("BAM_HOUSE").get_terms().df.to_dict(orient="records")

for entry in terms_dict:
    print(entry)
    break

# vtypes = o.get_vocabularies().df
# vtypes_dict = vtypes.to_dict(orient="records")
# formatted_dict = {entry["code"]: entry for entry in vtypes_dict}

# print(formatted_dict)

