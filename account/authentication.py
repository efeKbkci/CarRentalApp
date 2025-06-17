from .session import Session

from model import User
from database import Table

from typing import Optional


class Authentication:
    def __init__(self, app_controller):
        from app_controller import AppController
        self.app_controller:AppController = app_controller
        self.session: Optional[Session] = None

    def verify_login_credentials(self, credentials: dict) -> Optional[User]:        
        user:User = self.app_controller.db_transaction.get_entity(Table.USER, credentials)
        user and self.start_new_session(user)
        return user

    def save_new_user(self, user: User) -> bool:
        response = self.app_controller.db_transaction.add_new_entity(Table.USER, user)
        response and self.start_new_session(user)
        return response
    
    def is_email_already_registered(self, email: str) -> bool:
        user: User = self.app_controller.db_transaction.get_entity(Table.USER, {"email": email})
        return user is not None

    def start_new_session(self, user: User) -> None:
        self.session = Session(user) 

    def reset_session(self) -> None:
        self.session = None