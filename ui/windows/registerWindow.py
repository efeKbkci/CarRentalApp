from .. import *
from ..typeHint import Ui_Register
from ..additionalMethods import loadBg

class RegisterWindow(QWidget, Ui_Register):    

    def __init__(self):
        super().__init__()
        loadUi(UiFilePaths.REGISTER.value, self)
        loadBg(self, r"assets\tireTrackBg.jpg")

    def resizeEvent(self, a0):
        self.backgroundLabel:QLabel
        self.backgroundLabel.setGeometry(0, 0, self.width(), self.height())
        return super().resizeEvent(a0)