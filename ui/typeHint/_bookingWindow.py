from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton

class Ui_booking:
    car_image_label: QLabel
    car_name_label: QLabel
    year_tf: QLineEdit
    gear_tf: QLineEdit
    price_tf: QLineEdit
    gas_tf: QLineEdit
    starting_date_tf: QLineEdit
    return_date_tf: QLineEdit
    total_price_tf: QLineEdit
    create_appointment_btn: QPushButton
    back_btn: QPushButton

    @property
    def text_fields(self):
        return [
            self.year_tf,
            self.gear_tf,
            self.price_tf,
            self.gas_tf,
            self.starting_date_tf,
            self.return_date_tf,
            self.total_price_tf
        ]