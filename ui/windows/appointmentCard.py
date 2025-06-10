from .. import QWidget, loadUi, UiFilePaths
from ..typeHint import Ui_appointment_card

from model import Appointment, Car

from PyQt6.QtCore import pyqtSignal

class AppointmentCard(QWidget, Ui_appointment_card):
    cancel_btn_clicked = pyqtSignal(object)

    def __init__(self, appointment: Appointment, car: Car):
        super().__init__()
        loadUi(UiFilePaths.APPOINTMENT_CARD, self)

        self.connect_signals()

        self.appointment = appointment
        self.car = car

        self.car_name_label.setText(car.full_name)
        status = "Active" if appointment.status else "Inactive"
        self.status_label.setText(f"Status: {status}")
        self.starting_date_label.setText(appointment.start_date)
        self.return_date_label.setText(appointment.end_date)

        if not appointment.status:
            self.change_style()

    def connect_signals(self):
        self.cancel_btn.clicked.connect(lambda: self.cancel_btn_clicked.emit(self))

    def change_style(self):
        self.setStyleSheet('''
        QFrame {
            background-color: rgba(64, 85, 128, 0.8);
            color: #F0F0F0;
            border-radius: 9px;
        }
                            
        QLabel {
            background-color: transparent;
        }
        ''')