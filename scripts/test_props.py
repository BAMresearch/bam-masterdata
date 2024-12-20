from decouple import config as environ
from pybis import Openbis

# Connect to openBIS
url = environ("URL")
o = Openbis(url)
o.login(environ("USERNAME"), environ("PASSWORD"), save_token=True)

openbis_entity = o.get_object_type("CHEMICAL")

openbis_properties_data = {}

for prop in openbis_entity.get_property_assignments():
        print(dir(prop))
        openbis_properties_data[prop.code] = {
            "label": prop.label,
            "description": prop.description,
            "dataType": prop.dataType,
            "vocabulary": prop.vocabulary if prop.vocabulary is not None else "",
            "metaData" : prop.metaData
        }
print(openbis_properties_data)


# if assignments:

            # for prop in assignments:
            #     openbis_properties_data[prop.permId] = {
            #         "code": prop.code,
            #         "property_label": prop.label,
            #         "description": prop.description,
            #         "data_type": prop.dataType,
            #         "mandatory": prop.mandatory,
            #         "show_in_edit_views": prop.showInEditView,
            #         "section": prop.section,
            #         "metaData" : prop.metaData
            #     }

            # if twice > 0:
            #     print(openbis_properties_data)
            #     twice = twice - 1