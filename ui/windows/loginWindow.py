from .baseWidget import BaseWidget

from .. import UiFilePaths, loadUi
from ..constants import Windows, Dialogs
from ..typeHint import Ui_login

from account import Validation
from model import Priority

import os

class LoginWindow(Ui_login, BaseWidget):    
    def __init__(self, app_controller):
        super().__init__(app_controller)
        loadUi(UiFilePaths.LOGIN, self)
        self.set_background_image(self, os.path.join("assets", "11771164_4850037.jpg"))

        self.set_properties() # set the properties of the widgets for styling
        self.connect_signals()

    def connect_signals(self):
        self.login_btn.clicked.connect(self.login_btn_clicked)
        self.register_btn.clicked.connect(self.register_btn_clicked)
        self.email_tf.textChanged.connect(self.validate_form)
        self.password_tf.textChanged.connect(self.validate_form)

    def set_properties(self):
        self.login_btn.setProperty("class", "primary")
        self.email_tf.setProperty("class", "form")
        self.password_tf.setProperty("class", "form")   

    def login_btn_clicked(self): 
        email = self.email_tf.text().strip()
        password = self.password_tf.text().strip()
        user = self.app_controller.authentication.verify_login_credentials({"email": email, "password": password})

        if not user:
            self.app_controller.window_manager.show_dialog(Dialogs.ERROR, "Incorrect Username or Password", "The user information you entered does not match a user", True)

        elif user.priority == Priority.NORMAL_USER:
            self.app_controller.window_manager.navigate_to_window(Windows.NORMAL_USER_MAIN)

        elif user.priority == Priority.ADMIN: # I didn't use else keyword directly due to increase understandability
            self.app_controller.window_manager.navigate_to_window(Windows.ADMIN_MAIN)

    def register_btn_clicked(self):
        self.app_controller.window_manager.navigate_to_window(Windows.REGISTER)

    def validate_form(self):
        email = self.email_tf.text().strip()
        email_validation = Validation.check_email_format(email)
        email and self.update_error_style(self.email_tf, email_validation, "Check your email format")

        # If email or password is empty, text fields will not go into warning mode.
        # Only, the validation will be marked as False. 

        password = self.password_tf.text()
        password_validation = bool(password)
        password and self.update_error_style(self.password_tf, password_validation, "Password cannot be empty")

        self.login_btn.setEnabled(email_validation and password_validation)