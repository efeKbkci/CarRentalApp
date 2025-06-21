from ..helperWidgets.baseWidget import BaseWidget

from .. import loadUi, UiFilePaths
from ..constants import Windows, Dialogs 
from ..typeHint import Ui_register

from account import Validation
from model import User, Priority

import os
from datetime import datetime
from PyQt6.QtGui import QIntValidator 
    
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeyEvent

class RegisterWindow(Ui_register, BaseWidget):    

    def __init__(self, app_controller):
        super().__init__(app_controller)
        loadUi(UiFilePaths.REGISTER, self)
        self.set_background_image(self, os.path.join("assets", "tireTrackBg.jpg"))

        self.set_properties()
        self.connect_signals()

        self.id_tf.setValidator(QIntValidator())

    def connect_signals(self):
        [tf.textChanged.connect(self.validate_form) for tf in self.text_fields]
        self.register_btn.clicked.connect(self.register_btn_clicked)

    def set_properties(self):
        [tf.setProperty("class", "form") for tf in self.text_fields]
        self.register_btn.setProperty("class", "primary")

    def validate_form(self):
        email = self.email_tf.text()
        email_validation = Validation.check_email_format(email)
        email and self.update_error_style(self.email_tf, email_validation, "Check your email format")

        password = self.password_tf.text()
        password_validation = Validation.check_password_format(password)
        password and self.update_error_style(self.password_tf, password_validation, "Check your password format")

        password_again = self.password_again_tf.text()
        password_again_validation = password == password_again
        password_again and self.update_error_style(self.password_again_tf, password_again_validation, "Passwords don't match")

        birthdate = self.birthdate_tf.text()
        birthdate_validation = Validation.check_date_format(birthdate) and Validation.check_users_age(datetime.strptime(birthdate, r"%d.%m.%Y"))
        birthdate and self.update_error_style(self.birthdate_tf, birthdate_validation, "Birthdate format must be dd.mm.yyyy \nYou must be at least 18 years old")

        self.id_tf.text() and self.update_error_style(self.id_tf, self.id_tf.text() != "", "ID cannot be empty")
        self.name_tf.text() and self.update_error_style(self.name_tf, self.name_tf.text() != "", "Name cannot be empty")

        validation = (  
            email_validation,
            password_validation,
            password_again_validation,
            birthdate_validation, 
            self.id_tf.text() != "", self.name_tf.text() != ""
        )

        self.register_btn.setEnabled(all(validation))

    def register_btn_clicked(self):
        response = self.app_controller.window_manager.show_dialog(Dialogs.WARNING, "Registration Confirmation", "Are you sure you want to create a new user record?")
        if not response:
            return

        if self.is_email_already_registered():
            self.app_controller.window_manager.show_dialog(Dialogs.ERROR, "Registration Failed", "Email has already been registered in the system.", True)
            return

        form = User(
            self.name_tf.text(),
            self.email_tf.text(),
            self.birthdate_tf.text(),
            self.password_tf.text(),
            Priority.NORMAL_USER.value,
            self.id_tf.text()
        )

        if self.app_controller.authentication.save_new_user(form):
            self.app_controller.window_manager.show_dialog(Dialogs.SUCCESS, "Registration is Successful", single_btn = True)
            self.app_controller.window_manager.create_user_windows()
            self.app_controller.window_manager.navigate_to_window(Windows.NORMAL_USER_MAIN)    
        
    def is_email_already_registered(self):
        email = self.email_tf.text()
        is_registered = self.app_controller.authentication.is_email_already_registered(email)
        self.update_error_style(self.email_tf, is_registered, "This email is already registered")
        return is_registered

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Escape:
            self.app_controller.window_manager.navigate_to_window(Windows.LOGIN)
        else:
            super().keyPressEvent(event)