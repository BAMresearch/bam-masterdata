from decouple import config as environ
from pybis import Openbis


# Connect to openBIS
def ologin(url: str | Openbis = "") -> Openbis:
    """
    Connect to openBIS using the credentials stored in the environment variables.

    If an existing Openbis session is provided, the session is returned.

    Args:
        url (str, Openbis): The URL of the openBIS instance. Defaults to the value of the `OPENBIS_URL` environment variable.
        An existing Openbis session can be provided.

    Returns:
        Openbis: Openbis object for the specific openBIS instance defined in `URL`.
    """
    if not isinstance(url, Openbis):
        o = Openbis(url)

    if not o.is_session_activ():
        o.login(environ("OPENBIS_USERNAME"), environ("OPENBIS_PASSWORD"), save_token=True)

    return o
