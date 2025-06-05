from .. import QWidget, loadUi, UiFilePaths
from ..typeHint import Ui_vehicle_card

class VehicleCard(QWidget, Ui_vehicle_card):
    def __init__(self):
        super().__init__()
        loadUi(UiFilePaths.VEHICLE_CARD, self)