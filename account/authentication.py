from typing import Optional
from model import User
from .session import Session
from model import RegistrationFormDTO
from enum import Enum

class DBTransaction:
    pass
class MailService:
    pass

class Table(Enum):
    USER_TABLE = "user"
    CAR_RENTAL = "car"
    APPOINTMENTS_TABLE = "appointments"

class Authentication:
    def __init__(self):
        self.session: Optional[Session] = None

    def verify_login_credentials(self, db_transaction: DBTransaction, credentials: dict) -> Optional[User]:
        query = f' SELECT * FROM user WHERE email = {credentials["email"]}, password = {credentials["password"]}'
        
        user_list:list = db_transaction.get_entities(Table.USER_TABLE, query) # type: ignore
        
        if not len(user_list): # Is the user registered in the database?
            return None
        else:        
            user = user_list[0] # There can be only one user from the same email in the system
            self.start_new_session(user)
            return user 

    def save_new_user(self, db_transaction: DBTransaction, form: RegistrationFormDTO) -> bool:
        return db_transaction.add_new_entity(Table.USER_TABLE, form.convert_dict()) # type: ignore

    def verify_verification_code(self, mail_service: MailService, email: str) -> None:
        pass

    def start_new_session(self, user: User) -> None:
        self.session = Session(user) 

    def reset_session(self) -> None:
        self.session = None