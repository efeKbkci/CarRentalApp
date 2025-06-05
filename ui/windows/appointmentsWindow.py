from .. import QWidget, loadUi, UiFilePaths
from ..typeHint import Ui_appointments

class AppointmentWindow(QWidget, Ui_appointments):
    def __init__(self):
        super().__init__()
        loadUi(UiFilePaths.APPOINTMENTS, self)