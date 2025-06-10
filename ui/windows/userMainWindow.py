from .baseWidget import BaseWidget
from .customShapeBtn import CustomShapeButton

from ..constants import Windows

from PyQt6.QtCore import QPointF, QRect

class UserMainWindow(BaseWidget):

    def __init__(self, app_controller):
        super().__init__(app_controller)
        self.setFixedSize(800, 600)
        self.setObjectName("user_main")

        self.__create_buttons()

    def select_car_btn_clicked(self):
        self.app_controller.window_manager.navigate_to_window(Windows.CAR_SELECTION)
        self.app_controller.window_manager.window_dict[Windows.CAR_SELECTION].place_cars()

    def view_appointments_btn_clicked(self):
        self.app_controller.window_manager.navigate_to_window(Windows.APPOINTMENTS)
        self.app_controller.window_manager.window_dict[Windows.APPOINTMENTS].place_appointments()

    def __create_buttons(self):
        self.select_car_btn = CustomShapeButton(
            geometry = QRect(0, 0, 692, 600),
            bgImagePath = r"assets\carRentalBtnBg_a50.png", 
            bgImageHoverPath = r"assets\carRentalBtnBg_a100",
            callback = lambda: self.select_car_btn_clicked(),
            parent = self
        )
        area = [QPointF(x, y) for x, y in zip((0, 692, 100, 0), (0, 0, 600, 600))]
        self.select_car_btn.adjustClickableArea(area)
        
        self.view_appointments_btn = CustomShapeButton(
            geometry = QRect(108, 0, 692, 600),
            bgImagePath = r"assets\myCarsBtnBg_a80.png", 
            bgImageHoverPath = r"assets\myCarsBtnBg_a100.png",
            callback = lambda: self.view_appointments_btn_clicked(),
            parent = self
        )
        # Tıklanabilir alan hesabında noktaların kordinatları belirlenirken referans noktası ana pencerenin sol üst köşesi olmamalıdır.
        # myCarsBtn için başlangıç noktasını (108, 0) seçtik. Bu durumda butonun sol üst köşesi (700, 0) olması gerekirken (592,0) olacaktır.
        # Çünkü noktanın parent widget'ına göre x = 592 noktası, ana pencereye göre x = 700 olacaktır. 
        area = [QPointF(x, y) for x, y in zip((592, 800, 800, 0), (0, 0, 600, 600))]
        self.view_appointments_btn.adjustClickableArea(area)

        for btn in (self.select_car_btn, self.view_appointments_btn):
            btnGeometry = btn.geometry()
            btn.createAnimation(btnGeometry, btnGeometry.adjusted(0, 0, 8, 8)) 