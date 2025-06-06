from datetime import datetime
from dateutil.relativedelta import relativedelta
import re

class Validation:
    @staticmethod
    def check_password_format(password: str) -> bool:
        # At least: 1 Upper Word, 1 Lower Word, 1 Number. Min. Lenght: 8 Digit
        if len(password) < 8:
            return False

        if not re.search(r'[A-Z]', password):
            return False

        if not re.search(r'[a-z]', password):
            return False

        if not re.search(r'[0-9]', password):
            return False

        return True

    @staticmethod
    def is_passwords_identical(password: str, password_again: str) -> bool:
        return password == password_again

    @staticmethod
    def check_email_format(email: str) -> bool:
        # [\w\.-]+ : efkanefekabakcii, efkan.5412, efe78-85
        # @ : @
        # [\w\.]+ : Domain part. "gmail.com", "firat.edu.tr", "outlook.com"
        return bool(re.search(r"^[\w\.-]+@[\w\.]+\.\w+$", email))

    @staticmethod
    def check_users_age(birth_date: datetime) -> bool:
        today = datetime.today()
        eighteen_years_ago = today - relativedelta(years=18)
        return birth_date <= eighteen_years_ago
    
    @staticmethod
    def check_birth_date_format(birth_date: str) -> bool:
        # Expected format: DD.MM.YYYY
        try:
            datetime.strptime(birth_date, r"%d.%m.%Y")  
            return True
        except:
            return False