from .session import Session
from typing import Optional
from model import RegistrationFormDTO, User
from database import Table

class Authentication:
    def __init__(self, app_controller):
        from app_controller import AppController
        self.app_controller:AppController = app_controller
        self.session: Optional[Session] = None

    def verify_login_credentials(self, credentials: dict) -> Optional[User]:
        query = f' SELECT * FROM user WHERE email = {credentials["email"]}, password = {credentials["password"]}'
        
        user_list:list = self.app_controller.db_transaction.get_entities(Table.USER_TABLE, query) # type: ignore
        
        if not len(user_list): # Is the user registered in the database?
            return None
        else:        
            user = user_list[0] # There can be only one user from the same email in the system
            self.start_new_session(user)
            return user 

    def save_new_user(self, form: RegistrationFormDTO) -> bool:
        return self.app_controller.db_transaction.add_new_entity(Table.USER_TABLE, form.convert_dict()) # type: ignore

    def verify_verification_code(self, email: str) -> None: # TODO: MAIL SERVICE
        pass

    def start_new_session(self, user: User) -> None:
        self.session = Session(user) 

    def reset_session(self) -> None:
        self.session = None