from .. import *
from ..typeHint import Ui_Login
from ..additionalMethods import loadBg

class LoginWindow(QWidget, Ui_Login):    

    def __init__(self):
        super().__init__()
        loadUi(UiFilePaths.LOGIN.value, self)
        loadBg(self, r"assets\11771164_4850037.jpg")

    def resizeEvent(self, a0):
        self.backgroundLabel:QLabel
        self.backgroundLabel.setGeometry(0, 0, self.width(), self.height())
        return super().resizeEvent(a0)