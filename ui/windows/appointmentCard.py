from .. import QWidget, loadUi, UiFilePaths
from ..typeHint import Ui_appointment_card

class AppointmentCard(QWidget, Ui_appointment_card):
    def __init__(self):
        super().__init__()
        loadUi(UiFilePaths.APPOINTMENT_CARD, self)