import re

from bam_masterdata.openbis.login import ologin


class UserID:
    def __init__(self, url: str = ""):
        if not url:
            raise ValueError("Missing url to connect to openBIS")
        self.openbis = ologin(url=url)
        self.users = self.openbis.get_users()

    def _split_name(self, name: str):
        """
        Split a full name into firstname and lastname using comma ',' or space ' ' as separator.

        Args:
            name (str): Full name to split, e.g., "John Doe" or "Doe, John"
        """
        parts = re.split(r",|\s+", name.strip())
        parts = [p for p in parts if p]
        if len(parts) >= 2:
            return parts[0], parts[1]
        return parts[0], ""  # if only one name

    def _de_replacements(self, name: str) -> str:
        """
        Perform common German name replacements to standardize the name.

        Args:
            name (str): Name to standardize.

        Returns:
            str: Standardized name.
        """
        replacements = {
            "Ä": "Ae",
            "Ö": "Oe",
            "Ü": "Ue",
            "ä": "ae",
            "ö": "oe",
            "ü": "ue",
            "ß": "ss",
        }
        for old, new in replacements.items():
            name = name.replace(old, new)
        return name

    def get_userid_from_names(self, firstname: str, lastname: str) -> str | None:
        """
        Return the userId matching the given first and last name (case-insensitive).

        Args:
            firstname (str): First name.
            lastname (str): Last name.

        Returns:
            str | None: The userId if a match is found, otherwise None.
        """
        firstname = self._de_replacements(firstname)
        lastname = self._de_replacements(lastname)
        for u in self.users:
            if (
                u.firstName.lower() == firstname.lower()
                and u.lastName.lower() == lastname.lower()
            ):
                return u.userId
        return None

    def get_userid_from_fullname(self, name: str) -> str | None:
        """
        Return the userId matching the given fullname (case-insensitive). It uses the `_split_name` function.

        Args:
            name (str): Full name, e.g., "John Doe" or "Doe, John".

        Returns:
            str | None: The userId if a match is found, otherwise None.
        """
        firstname, lastname = self._split_name(name)
        firstname = self._de_replacements(firstname)
        lastname = self._de_replacements(lastname)
        for u in self.users:
            if (u.firstName.lower(), u.lastName.lower()) == (
                firstname.lower(),
                lastname.lower(),
            ) or (u.firstName.lower(), u.lastName.lower()) == (
                lastname.lower(),
                firstname.lower(),
            ):
                return u.userId
        return None
