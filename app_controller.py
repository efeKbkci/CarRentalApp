from ui.window_manager import WindowManager
from account import Authentication
from database import DBTransaction
import sys

class AppController:
    def __init__(self, test = False):
        self.db_transaction = DBTransaction()
        self.authentication = Authentication(self)
        if not test: self.window_manager = WindowManager(self)

        admin, normal = self.parse_args(sys.argv)

        login = self.window_manager.login_screen
        if admin:
            login.email_tf.setText("admin_test@gmail.com")
            login.password_tf.setText("Admin548154")
            login.login_btn.setEnabled(True)
        elif normal:
            login.email_tf.setText("normal_user@gmail.com")
            login.password_tf.setText("NormalUser3356")
            login.login_btn.setEnabled(True)

    def parse_args(self, args:list) -> tuple[bool]:
        admin = False
        normal = False

        if "-a" in args:
            admin = True
        elif "-n" in args:
            normal = True
        elif len(args) > 1:
            print("Unexpected Arguments:", args[1:])
        
        return (admin, normal)

    def teardown(self):
        self.db_transaction.close_connection()