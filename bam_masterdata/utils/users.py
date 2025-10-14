from bam_masterdata.openbis import ologin

class UserID:
    def __init__(self, url: str = ""):
        if not url:
            raise ValueError("Missing url to connect to openBIS")
        self.openbis = ologin(url=url)
        self.users = self.openbis.get_users()

    def _split_name(self, name):
        """
        Split a full name into firstname and lastname using comma ',' or space ' ' as separator.
        """
        parts = re.split(r',|\s+', name.strip())
        parts = [p for p in parts if p]
        if len(parts) >= 2:
            return parts[0], parts[1]
        return parts[0], ''  # if only one name

    def get_userid_from_names(self, firstname, lastname):
        """
        Return the userId matching the given first and last name (case-insensitive).

        Parameters:
            firstname (str): First name
            lastname (str): Last name
            openbis (Openbis, optional): Connected Openbis object. If None, connect automatically.

        Returns:
            str or None: Matching userId or None if not found
        """
        for u in self.users:
            if u.firstName.lower() == firstname.lower() and u.lastName.lower() == lastname.lower():
                print(f"First name: {firstname}, Last name: {lastname} → userId: {u.userId}")
                return u.userId
        print("No match found")
        return None

    def get_userid_from_fullname(self, name):
        """
        Return the userId matching the given fullname (case-insensitive).
        Uses the split_name function.
        """
        firstname, lastname = self._split_name(name)
        for u in self.users:
            if (u.firstName.lower(), u.lastName.lower()) == (firstname.lower(), lastname.lower()) \
            or (u.firstName.lower(), u.lastName.lower()) == (lastname.lower(), firstname.lower()):
                print(f"Match found: {u.firstName} {u.lastName} → userId: {u.userId}")
                return u.userId
        print("No match found")
        return None
