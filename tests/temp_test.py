from decouple import config as environ
from pybis import Openbis

openbis = Openbis(environ("OPENBIS_URL"))
openbis.login(environ("OPENBIS_USERNAME"), environ("OPENBIS_PASSWORD"), save_token=True)


for object_type in openbis.get_object_types():
    assignments = object_type.get_property_assignments()
    a_dict = assignments.df.to_dict(orient="records")

    for entry in a_dict:
        # ! This has changed and now permId does not exist on the property assignments!!
        property_perm_id = openbis.get_property_type(entry.get("code", {})).permId
        print(property_perm_id)
