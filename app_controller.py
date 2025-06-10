from ui.window_manager import WindowManager
from account import Authentication
from database import DBTransaction
from ui.constants import Dialogs

class AppController:
    def __init__(self, test = False):
        self.db_transaction = DBTransaction()
        self.authentication = Authentication(self)
        if not test: self.window_manager = WindowManager(self)

    def teardown(self):
        self.db_transaction.close_connection()