from .baseWidget import BaseWidget
from .appointmentCard import AppointmentCard

from .. import loadUi, UiFilePaths
from ..constants import Windows, Dialogs
from ..typeHint import Ui_appointments

from database import Table
from model import Appointment

from PyQt6.QtWidgets import QSpacerItem, QSizePolicy

class AppointmentWindow(Ui_appointments, BaseWidget):
    def __init__(self, app_controller):
        super().__init__(app_controller)
        loadUi(UiFilePaths.APPOINTMENTS, self)

        self.connect_signals()
    
    def connect_signals(self):
        self.back_btn.clicked.connect(lambda: self.app_controller.window_manager.navigate_to_window(Windows.NORMAL_USER_MAIN))

    def set_properties(self):
        pass

    def place_appointments(self):
        self.__clearHorizontalLayout(self.active_appointments_layout)
        self.__clearHorizontalLayout(self.inactive_appointments_layout)

        session = self.app_controller.authentication.session

        appointments:list[Appointment] = self.app_controller.db_transaction.get_entities(Table.APPOINTMENTS, ("user_id", "=", session.user.entity_id))
        cars = [self.app_controller.db_transaction.get_entity(Table.CAR, {"entity_id": appointment.car_id}) for appointment in appointments]

        for appointment, car in zip(appointments, cars):
            appointment_card = AppointmentCard(appointment, car)
            appointment_card.cancel_btn_clicked.connect(self.cancel_btn_clicked)
            self.set_pixmap(appointment_card.car_image_label, car.image_pixmap)

            if appointment.status:
                self.active_appointments_layout.addWidget(appointment_card)
            else:
                self.inactive_appointments_layout.addWidget(appointment_card)
            
        self.__setSpacers()

        self.active_appointments_layout.update()
        self.active_appointments_layout.parentWidget().adjustSize()
        self.inactive_appointments_layout.update()
        self.inactive_appointments_layout.parentWidget().adjustSize()

    def cancel_btn_clicked(self, appointment_card: AppointmentCard):
        appointment = appointment_card.appointment

        if appointment_card.appointment.status:
            response = self.app_controller.window_manager.show_dialog(Dialogs.WARNING, "Appointment Cancellation", "Do you agree to cancel the appointment?")
            if response:
                appointment.status = 0
                self.app_controller.db_transaction.update_entity(Table.APPOINTMENTS, appointment)
                self.place_appointments()
        else:
            self.app_controller.db_transaction.delete_entity(Table.APPOINTMENTS, appointment.entity_id)
            self.place_appointments()

    def __clearHorizontalLayout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            
            if widget:
                widget.setParent(None)
                widget.deleteLater()            
        layout.update()

    def __setSpacers(self):
        self.active_appointments_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        self.inactive_appointments_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
