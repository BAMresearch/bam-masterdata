from decouple import config as environ
from pybis import Openbis


# Connect to openBIS
def ologin() -> Openbis:
    """
    Connect to openBIS using the credentials stored in the environment variables.

    Returns:
        Openbis: Openbis object for the specific openBIS instance defined in `URL`.
    """
    url = environ('URL')
    o = Openbis(url)
    o.login(environ('USERNAME'), environ('PASSWORD'), save_token=True)
    return o
