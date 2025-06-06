from .windows_enum import Windows
from .. import *
from ..typeHint import Ui_register
from ..additionalMethods import loadBg
from account import Validation
from datetime import datetime
from model import User, Priority

class RegisterWindow(QWidget, Ui_register):    

    def __init__(self, app_controller):
        super().__init__()
        loadUi(UiFilePaths.REGISTER, self)
        loadBg(self, r"assets\tireTrackBg.jpg")

        from app_controller import AppController
        self.app_controller:AppController = app_controller

        # signals and slots
        tf_list = [self.email_tf, self.password_tf, self.password_again_tf, self.birthdate_tf] # tf : text field
        [tf.editingFinished.connect(self.validate_form) for tf in tf_list]
        self.register_btn.clicked.connect(self.on_register_btn_clicked)

    def validate_form(self):
        validation = (  
            self.validate_email(self.email_tf.text()) and
            self.validate_password(self.password_tf.text()) and
            self.validate_password_again(self.password_again_tf.text()) and
            self.validate_birthdate(self.birthdate_tf.text()) and 
            self.id_tf.text() != "" and self.name_tf.text() != ""
        )

        if validation:
            self.register_btn.setEnabled(True)
            print("DEBUG | Button is active again")

    def on_register_btn_clicked(self):

        form = User(
            self.name_tf.text(),
            self.email_tf.text(),
            self.birthdate_tf.text(),
            self.password_tf.text(),
            Priority.NORMAL_USER.value,
            self.id_tf.text()
        )

        if self.app_controller.authentication.save_new_user(form):
            print("DEBUG | User registered successfully")
            self.app_controller.window_manager.navigate_to_window(Windows.NORMAL_USER_MAIN)    

    def validate_email(self, email):
        if email == "":
            # TODO: Text Field won't be changed, if it's in an warning stuation, it'll be turned into normal.
            return False

        elif not Validation.check_email_format(email):
            # TODO: Text Field will be changed
            print("DEBUG | Check your email format")
            return False
        
        else:
            return True

    def validate_password(self, password):
        if password == "":
            return False
        
        elif not Validation.check_password_format(password):    
            # TODO: Text Field will be changed
            print("DEBUG | Check your password format")
            return False
        
        else:
            return True

    def validate_password_again(self, password_again):
        if password_again == "":
            return False
        
        elif self.password_tf.text() != password_again:
            # TODO: Text Field will be changed
            print("DEBUG | Passwords don't match")
            return False
        
        else:
            return True 

    def validate_birthdate(self, birthdate):
        if birthdate == "":
            return False
        
        elif not Validation.check_birth_date_format(self.birthdate_tf.text()):
            # TODO: Text Field will be changed
            print("DEBUG | Check your birthdate format")   
            return False
        
        elif not Validation.check_users_age(datetime.strptime(birthdate, r"%d.%m.%Y")):
            # TODO: Text Field will be changed
            print("DEBUG | You must be at least 18 years old")  
            return False
        
        else:
            return True

    def resizeEvent(self, a0):
        self.backgroundLabel:QLabel
        self.backgroundLabel.setGeometry(0, 0, self.width(), self.height())
        return super().resizeEvent(a0)