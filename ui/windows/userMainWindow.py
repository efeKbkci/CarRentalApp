from .. import *
from PyQt6.QtCore import QPoint, QPointF, QRect
from .customShapeBtn import CustomShapeButton

class UserMainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 600)
        self.setObjectName("user_main")
        self.__create_buttons()

    def __create_buttons(self):
        self.carRentalBtn = CustomShapeButton(
            geometry = QRect(0, 0, 692, 600),
            bgImagePath = r"assets\carRentalBtnBg_a50.png", 
            bgImageHoverPath = r"assets\carRentalBtnBg_a100",
            callback = lambda: print("Car Rental Button"),
            parent = self
        )
        area = [QPointF(x, y) for x, y in zip((0, 692, 100, 0), (0, 0, 600, 600))]
        self.carRentalBtn.adjustClickableArea(area)
        
        self.myCarsBtn = CustomShapeButton(
            geometry = QRect(108, 0, 692, 600),
            bgImagePath = r"assets\myCarsBtnBg_a80.png", 
            bgImageHoverPath = r"assets\myCarsBtnBg_a100.png",
            callback = lambda: print("My Cars Button"),
            parent = self
        )
        # Tıklanabilir alan hesabında noktaların kordinatları belirlenirken referans noktası ana pencerenin sol üst köşesi olmamalıdır.
        # myCarsBtn için başlangıç noktasını (108, 0) seçtik. Bu durumda butonun sol üst köşesi (700, 0) olması gerekirken (592,0) olacaktır.
        # Çünkü noktanın parent widget'ına göre x = 592 noktası, ana pencereye göre x = 700 olacaktır. 
        area = [QPointF(x, y) for x, y in zip((592, 800, 800, 0), (0, 0, 600, 600))]
        self.myCarsBtn.adjustClickableArea(area)

        for btn in (self.carRentalBtn, self.myCarsBtn):
            btnGeometry = btn.geometry()
            btn.createAnimation(btnGeometry, btnGeometry.adjusted(0, 0, 8, 8)) 