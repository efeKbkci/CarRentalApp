import pytest
from account import Validation
from datetime import datetime

@pytest.mark.parametrize("email, correctness", [
    ("efkanefekabakcii@gmail.com", True),
    ("yzgll_0981@firat.edu.tr", True),
    ("efkanefekabakcii @gmail.com", False),
    ("yzgll_0981@firat.edu.tr.", False),
    ("efkanefekabakcii@gmail", False)
])
def test_check_email_format(email, correctness):
    assert Validation.check_email_format(email) == correctness

@pytest.mark.parametrize("password, correctness", [
    ("xhjgshs", False),
    ("Xgssks", False),
    ("afh67hj", False),
    ("Hsdytr52", True)
])
def test_check_password_format(password, correctness):
    assert Validation.check_password_format(password) == correctness

@pytest.mark.parametrize("birth_date, correctness", [
    (datetime.strptime("03.05.2007", "%d.%m.%Y"), True),
    (datetime.strptime("19.08.2008", "%d.%m.%Y"), False),
    (datetime.strptime("24.06.1996", "%d.%m.%Y"), True),
])
def test_check_users_age(birth_date, correctness):
    assert Validation.check_users_age(birth_date) == correctness

@pytest.mark.parametrize("birth_date, correctness", [
    ("3.5.2007", True),
    ("03.05.2007", True),
    ("13.15.2001", False),
    ("36.12.2000", False),
    ("03:05:2005", False)
])
def test_check_birth_date_format(birth_date, correctness):
    assert Validation.check_birth_date_format(birth_date) == correctness