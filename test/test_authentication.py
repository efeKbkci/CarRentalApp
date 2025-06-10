from account import Authentication
from model import User, Priority
from app_controller import AppController

import pytest

@pytest.fixture(scope="class")
def authentication():
    app_controller = AppController(test = True)
    auth = Authentication(app_controller)
    
    yield auth

    app_controller.db_transaction.conn.execute("DELETE FROM users;")  # tabloyu temizle
    app_controller.db_transaction.conn.commit()
    app_controller.db_transaction.conn.close()

@pytest.mark.usefixtures("authentication")
class TestAuthentication():
    def test_save_new_user(self, authentication: Authentication):
        fake_user = User("John David", "johndavid@gmail.com", "05.04.2002", "john_david123", Priority.NORMAL_USER.value, 123456)
        response = authentication.save_new_user(fake_user)

        assert response == True

    def test_verify_login_credentials(self, authentication: Authentication):
        fake_user_credentials = {"email": "johndavid@gmail.com", "password": "john_david123"}
        result = authentication.verify_login_credentials(fake_user_credentials)

        assert type(result) == User
        assert authentication.session != None

