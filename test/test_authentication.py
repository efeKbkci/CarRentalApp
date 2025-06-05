import pytest
from unittest.mock import Mock, patch
from account import Authentication
from model import User, Priority
from datetime import datetime

@pytest.fixture
def authentication():
    return Authentication()

@pytest.mark.usefixtures("authentication")
class TestAuthentication():
    def test_verify_login_credentials(self, authentication: Authentication):
        fake_user_credentials = {"email": "efkanefekabakcii@gmail.com", "password": "ef145635920"}
        mock_db_transaction = Mock()
        fake_user = User("Efe", "Kabakcı", "efkanefekabakcii@gmail.com", datetime.strptime("24.04.2004", "%d.%m.%Y"), Priority.NORMAL_USER)
        mock_db_transaction.get_entities.return_value = [fake_user]
        
        result = authentication.verify_login_credentials(mock_db_transaction, fake_user_credentials)

        assert result == fake_user
        assert authentication.session != None
        assert authentication.session.user == fake_user



