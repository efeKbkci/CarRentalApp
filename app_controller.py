from ui.window_manager import WindowManager
from account import Authentication
from database import DBConnection, DBTransaction

class AppController:
    def __init__(self):
        self.db_connection = DBConnection()
        self.db_transaction = DBTransaction()
        self.authentication = Authentication(self)
        # TODO : MAIL SERVICE
        self.window_manager = WindowManager(self)
