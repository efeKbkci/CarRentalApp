from .. import loadUi, UiFilePaths
from ..helperWidgets import BaseWidget, TopAppBar
from ..constants import Windows
from ..typeHint import Ui_user_main

from PyQt6.QtCore import QPointF, QRect

class UserMainWindow(Ui_user_main, BaseWidget):
    def __init__(self, app_controller):
        super().__init__(app_controller)

        loadUi(UiFilePaths.USER_MAIN, self)

        self.top_app_bar = TopAppBar(app_controller, window_title = "Home", show_back=False)
        self.mainLayout.insertWidget(0, self.top_app_bar)

        self.select_car_btn.mousePressEvent = lambda event: self.select_car_btn_clicked()
        self.view_appointments_btn.mousePressEvent = lambda event: self.view_appointments_btn_clicked()

    def select_car_btn_clicked(self):
        self.app_controller.window_manager.navigate_to_window(Windows.CAR_SELECTION)
        self.app_controller.window_manager.window_dict[Windows.CAR_SELECTION].place_cars()

    def view_appointments_btn_clicked(self):
        self.app_controller.window_manager.navigate_to_window(Windows.APPOINTMENTS)
        self.app_controller.window_manager.window_dict[Windows.APPOINTMENTS].place_appointments()
