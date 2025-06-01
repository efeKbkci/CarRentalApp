from .. import *
from ..typeHint import Ui_Card

class VehicleCard(QWidget, Ui_Card):
    def __init__(self):
        super().__init__()
        loadUi(UiFilePaths.VEHICLE_CARD.value, self)