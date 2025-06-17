from ..typeHint import Ui_admin_car_dialog
from ..uiFiles import UiFilePaths
from .. import loadUi, QPixmap
from ..constants import Dialogs

from model import Car

from PyQt6.QtWidgets import QDialog, QFileDialog
from PyQt6.QtGui import QIntValidator, QDoubleValidator 
import re

class AdminCarDialog(QDialog, Ui_admin_car_dialog):
    def __init__(self, app_controller, parent = None, car: Car = None):
        super().__init__(parent)
        loadUi(UiFilePaths.ADMIN_CAR_DIALOG, self)

        self.car = car
        self.image_path = car.car_image_path if car else None
        self.app_controller = app_controller

        if car:
            self.brand_tf.setText(car.brand)
            self.model_tf.setText(car.model)
            self.year_tf.setText(str(car.year))
            self.price_tf.setText(str(car.price))
            self.fuel_combo.setCurrentText(car.gas_type.capitalize())
            self.gear_combo.setCurrentText(car.gear_type.capitalize())
            status = "Active" if car.status else "Inactive"
            self.status_combo.setCurrentText(status)
            self.car_image_label.setPixmap(self.car.image_pixmap.scaled(85,28))
            self.confirm_btn.setDisabled(False)
        else:
            self.confirm_btn.setDisabled(True)

        self.year_tf.setValidator(QIntValidator(0, 2026))
        self.price_tf.setValidator(QDoubleValidator())

        self.connect_signals()

    def connect_signals(self):
        self.cancel_btn.clicked.connect(self.reject)
        self.confirm_btn.clicked.connect(self.accept)
        self.select_image_btn.clicked.connect(self.choose_image)
        [tf.textChanged.connect(self.validate_entries) for tf in (self.year_tf, self.brand_tf, self.model_tf, self.price_tf)]
        
    def get_data(self):
        car = Car(
            self.brand_tf.text(),
            self.model_tf.text(),
            self.year_tf.text(),
            self.gear_combo.currentText(),
            self.fuel_combo.currentText(),
            1 if self.status_combo.currentText() == "Active" else 0,
            self.price_tf.text(),
            self.image_path
        )
        
        car.year = int(car.year)
        car.price = float(car.price)

        if self.car:
            car.entity_id = self.car.entity_id 
        
        return car
    
    def validate_entries(self):
        validation = (
            self.brand_tf.text() and
            self.model_tf.text() and
            self.year_tf.text() and
            self.price_tf.text() and
            self.image_path
        )
        self.confirm_btn.setEnabled(bool(validation))

    def choose_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Choose Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.webp)"
        )
        if file_path:
            relative_path = re.search(r"assets[\\\/]cars[\\\/].*", file_path)
            if relative_path:
                self.image_path = relative_path.group()
            print(relative_path)
            self.car_image_label.setPixmap(QPixmap(self.image_path).scaled(85,28))
            
        self.validate_entries()