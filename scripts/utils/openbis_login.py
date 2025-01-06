from decouple import config as environ
from pybis import Openbis


# Connect to openBIS
def ologin():
    url = environ("URL")
    o = Openbis(url)
    o.login(environ("USERNAME"), environ("PASSWORD"), save_token=True)
    return o