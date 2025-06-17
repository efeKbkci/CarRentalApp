from .. import loadUi, UiFilePaths
from ..constants import Windows, Dialogs
from ..typeHint import Ui_booking
from ..helperWidgets import BaseWidget, TopAppBar

from model import Car, Appointment
from database import Table
from account import Validation

import os
from datetime import datetime

class BookingWindow(Ui_booking, BaseWidget):
    viewed_car:Car = None  # This will be set when the user selects a car from the CarSelectionWindow

    def __init__(self, app_controller):
        super().__init__(app_controller)
        loadUi(UiFilePaths.BOOKING, self)
        self.set_background_image(self, os.path.join("assets", "tireTrackBg.jpg"))

        self.set_properties()

        self.top_app_bar = TopAppBar(app_controller, window_title = "Booking")
        self.mainLayout.insertWidget(0, self.top_app_bar)
        
        self.connect_signals()

    def connect_signals(self):
        self.create_appointment_btn.clicked.connect(self.create_appointment)
        self.top_app_bar.back_btn.clicked.connect(self.back_btn_clicked)
        [tf.textChanged.connect(self.validate_date) for tf in (self.starting_date_tf, self.return_date_tf)]
    
    def set_properties(self):
        [tf.setProperty("class", "form") for tf in self.text_fields]
        self.create_appointment_btn.setProperty("class", "primary")

    def adjust_window(self):
        self.set_pixmap(self.car_image_label, self.viewed_car.image_pixmap)
        
        self.starting_date_tf.setText("")
        self.return_date_tf.setText("")

        self.car_name_label.setText(self.viewed_car.full_name)
        self.year_tf.setText(str(self.viewed_car.year))
        self.gear_tf.setText(self.viewed_car.gear_type)   
        self.gas_tf.setText(self.viewed_car.gas_type)
        self.price_tf.setText(self.viewed_car.price_str)

    def validate_date(self) -> bool:
        starting_date = self.starting_date_tf.text()
        starting_date_validation = Validation.check_date_format(starting_date)
        starting_date and self.update_error_style(self.starting_date_tf, starting_date_validation, "Check the date format (dd.mm.yyyy)")

        return_date = self.return_date_tf.text()
        return_date_validation = Validation.check_date_format(return_date) 
        return_date and self.update_error_style(self.return_date_tf, Validation.check_date_format(return_date), "Check the date format (dd.mm.yyyy)")

        if starting_date_validation and return_date_validation:
            day_difference = self.calculate_day_difference(starting_date, return_date)
            if day_difference < 1:
                self.update_error_style(self.return_date_tf, False, "Return date must be after starting date")
                return_date_validation = False
            else:
                self.total_price_tf.setText(str(day_difference * self.viewed_car.price))

        self.create_appointment_btn.setEnabled(return_date_validation and starting_date_validation)

    def create_appointment(self):
        starting_date = self.starting_date_tf.text()
        return_date = self.return_date_tf.text()

        response = self.app_controller.window_manager.show_dialog(
                        Dialogs.WARNING, 
                        "Appointment Confirmation", 
                        "Do you confirm the appointment?"
                    )

        if not response:
            return

        appointment = Appointment(
            self.app_controller.authentication.session.user.entity_id,
            self.viewed_car.entity_id,
            starting_date,
            return_date,
            self.calculate_day_difference(starting_date, return_date) * self.viewed_car.price,
            status = 1
        )

        if self.app_controller.db_transaction.add_new_entity(Table.APPOINTMENTS, appointment):
            self.app_controller.window_manager.show_dialog(Dialogs.SUCCESS, "Successful", "Your appointment has been successfully booked.", True)
            self.app_controller.window_manager.navigate_to_window(Windows.NORMAL_USER_MAIN)
        else:
            self.app_controller.window_manager.show_dialog(Dialogs.ERROR, "Failure", "Your appointment booking failed.", True)

    def back_btn_clicked(self):
        self.app_controller.window_manager.navigate_to_window(Windows.CAR_SELECTION)
        [tf.setText("") for tf in (self.starting_date_tf, self.return_date_tf, self.total_price_tf)]

    def calculate_day_difference(self, starting_date: str, return_date: str) -> int:
        starting_date_datetime = datetime.strptime(starting_date, "%d.%m.%Y")
        return_date_datetime = datetime.strptime(return_date, "%d.%m.%Y")
        days = (return_date_datetime - starting_date_datetime).days

        return days 