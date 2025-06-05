from .windows_enum import Windows
from .. import *
from ..typeHint import Ui_login
from ..additionalMethods import loadBg
from account import Validation
from model import Priority

class LoginWindow(QWidget, Ui_login):    
    def __init__(self, app_controller):
        super().__init__()
        loadUi(UiFilePaths.LOGIN, self)
        loadBg(self, r"assets\11771164_4850037.jpg") 

        # if we put this line at the top of the file, we'll get "circular import" error.
        # local import breaks the loop
        from app_controller import AppController
        self.app_controller:AppController = app_controller

        # login button must be disabled until the form data has been entered correctly. 
        self.login_btn.setDisabled(True)

        # signals and slots
        self.login_btn.clicked.connect(self.on_login_btn_clicked)   
        self.register_btn.clicked.connect(self.on_register_btn_clicked)     
        self.email_tf.textChanged.connect(self.on_validate_form)
        self.password_tf.textChanged.connect(lambda: self.on_validate_form(self.email_tf.text(), self.password_tf.text()))

    def on_login_btn_clicked(self, email, password): 
        user = self.app_controller.authentication.verify_login_credentials({"email": email, "password": password})

        if not user:
            print("DEBUG | Your credentials doesn't match with any user")

        elif user.priority == Priority.NORMAL_USER:
            self.app_controller.window_manager.navigate_to_window(Windows.NORMAL_USER_MAIN)

        elif user.priority == Priority.ADMIN: # I didn't use else keyword directly due to increase understandability
            self.app_controller.window_manager.navigate_to_window(Windows.ADMIN_MAIN)

    def on_register_btn_clicked(self):
        self.app_controller.window_manager.navigate_to_window(Windows.REGISTER)

    def on_validate_form(self):
        email = self.email_tf.text()
        password = self.password_tf.text()

        email_validation = Validation.check_email_format(email) 

        if email_validation and password != "":
            self.login_btn.setEnabled(True)
            print("DEBUG | Button is active again")
        else:
            self.login_btn.setDisabled(True)
            if not email_validation:
                print("DEBUG | Check your email format")
            else:
                print("DEBUG | Password mustn't be empty")

    def resizeEvent(self, a0): # As the window size changes, the size of the background photo also changes.
        self.backgroundLabel:QLabel
        self.backgroundLabel.setGeometry(0, 0, self.width(), self.height())
        return super().resizeEvent(a0)