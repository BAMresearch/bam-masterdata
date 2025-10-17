from unittest.mock import patch

import pytest

from bam_masterdata.utils.users import UserID


class TestUserID:
    @patch("bam_masterdata.utils.users.ologin")
    def test_init(self, mock_ologin, mock_openbis):
        mock_ologin.return_value = mock_openbis

        user_id = UserID(url="https://fake.openbis")
        assert user_id.users == mock_openbis.get_users.return_value
        mock_ologin.assert_called_once_with(url="https://fake.openbis")

    def test_init_missing_url(self):
        with pytest.raises(ValueError, match="Missing url to connect to openBIS"):
            UserID()

    def test_split_name(self):
        user_id = object.__new__(UserID)  # bypass __init__
        assert user_id._split_name("John Doe") == ("John", "Doe")
        assert user_id._split_name("Doe, John") == ("Doe", "John")
        assert user_id._split_name("Single") == ("Single", "")

    @patch("bam_masterdata.utils.users.ologin")
    def test_get_userid_from_names(self, mock_ologin, mock_openbis):
        mock_ologin.return_value = mock_openbis

        user_id = UserID(url="https://fake")
        result = user_id.get_userid_from_names("John", "Doe")
        assert result == "jdoe"

        result_none = user_id.get_userid_from_names("Nonexistent", "User")
        assert result_none is None

    @patch("bam_masterdata.utils.users.ologin")
    def test_get_userid_from_fullname(self, mock_ologin, mock_openbis):
        mock_ologin.return_value = mock_openbis

        user_id = UserID(url="https://fake")
        assert user_id.get_userid_from_fullname("John Doe") == "jdoe"
        assert user_id.get_userid_from_fullname("Doe, John") == "jdoe"
        assert user_id.get_userid_from_fullname("Jane Smith") == "jsmith"
        assert user_id.get_userid_from_fullname("Smith, Jane") == "jsmith"
        assert user_id.get_userid_from_fullname("Unknown User") is None
