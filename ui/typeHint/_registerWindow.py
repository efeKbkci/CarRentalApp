from PyQt6.QtWidgets import QLineEdit, QPushButton

class Ui_register:
    email_tf: QLineEdit
    name_tf: QLineEdit
    password_tf: QLineEdit
    password_again_tf: QLineEdit
    id_tf: QLineEdit
    birthdate_tf: QLineEdit
    register_btn: QPushButton

    @property
    def text_fields(self):
        """Returns a list of all text fields in the register window."""
        return [
            self.email_tf,
            self.name_tf,
            self.password_tf,
            self.password_again_tf,
            self.id_tf,
            self.birthdate_tf
        ]