from .. import QWidget, loadUi, UiFilePaths, QPixmap
from ..typeHint import Ui_vehicle_card

from model import Car

from PyQt6.QtCore import pyqtSignal

class VehicleCard(QWidget, Ui_vehicle_card):
    clicked = pyqtSignal(object)

    def __init__(self, car: Car):
        super().__init__()
        loadUi(UiFilePaths.VEHICLE_CARD, self)

        self.car = car

        self.brand_label.setText(f"{car.brand} {car.model}")
        self.features_label.setText(f"{car.gear_type} | {car.gas_type} | {car.year}")
        self.price_label.setText(f"{car.price} $")

        self.car_image_label.setPixmap(self.car.image_pixmap if self.car.image_pixmap else QPixmap())

    def mousePressEvent(self, event):
        self.clicked.emit(self)
        super().mousePressEvent(event)