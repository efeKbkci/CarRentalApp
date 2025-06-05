from .. import QWidget, loadUi, UiFilePaths
from ..typeHint import Ui_booking

class BookingWindow(QWidget, Ui_booking):
    def __init__(self):
        super().__init__()
        loadUi(UiFilePaths.BOOKING, self)