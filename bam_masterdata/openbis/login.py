from decouple import config as environ
from pybis import Openbis


# Connect to openBIS
def ologin(url: str = "") -> Openbis:
    """
    Connect to openBIS using the credentials stored in the environment variables.

    Args:
        url (str): The URL of the openBIS instance. Defaults to the value of the `OPENBIS_URL` environment variable.

    Returns:
        Openbis: Openbis object for the specific openBIS instance defined in `URL`.
    """
    o = Openbis(url)
    o.login(environ("OPENBIS_USERNAME"), environ("OPENBIS_PASSWORD"), save_token=True)
    return o
