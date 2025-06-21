from ..typeHint import Ui_dialog
from ..constants import DialogColor, Dialogs
from ..uiFiles import UiFilePaths
from .. import loadUi, QPixmap

from PyQt6.QtWidgets import QDialog 
from PyQt6.QtCore import Qt

class DialogBox(Ui_dialog, QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        loadUi(UiFilePaths.DIALOG, self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

    def change_appearance(self, dialog_type: Dialogs, subject: str, message: str, single_btn: bool = False):
        self.confirmation_btn.setProperty("dialog", dialog_type.value) # for confirmation btn
        self.confirmation_btn.style().unpolish(self.confirmation_btn)
        self.confirmation_btn.style().polish(self.confirmation_btn)

        self.confirmation_btn.clicked.connect(self.accept)
        self.cancellation_btn.clicked.connect(self.reject)

        if single_btn: 
            self.cancellation_btn.hide()
        else: 
            self.cancellation_btn.show()
        self.cancellation_btn.update()

        if dialog_type == Dialogs.ERROR: 
            self.__customize_dialog(r"assets\icons\warning.png", subject, message, DialogColor.ERROR)
            self.confirmation_btn.setText("Confirm")

        elif dialog_type == Dialogs.WARNING: 
            self.__customize_dialog(r"assets\icons\problem.png", subject, message, DialogColor.WARNING)
            self.confirmation_btn.setText("Okay")

        else: 
            self.__customize_dialog(r"assets\icons\approve.png", subject, message, DialogColor.SUCCESS)
            self.confirmation_btn.setText("Okay")

    def __customize_dialog(self, icon_path: str, subject: str, message: str, line_color: str):
            
            scaled_pixmap = QPixmap(icon_path).scaled(
                self.icon.size(), 
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.icon.setPixmap(scaled_pixmap)
            self.top_line.setStyleSheet(f"color: {line_color};")
            self.subject_label.setText(subject)
            self.message_label.setText(message)
