from .vehicleCard import VehicleCard
from .. import *
from ..typeHint import Ui_car_selection
from ..additionalMethods import changePlaceHolderColor
from PyQt6.QtWidgets import QGridLayout
from itertools import batched

from PyQt6.QtCore import Qt

class CarSelectionWindow(QWidget, Ui_car_selection):    
    
    __columnNumber = 0

    def __init__(self):
        super().__init__()
        loadUi(UiFilePaths.CAR_SELECTION, self)

        changePlaceHolderColor([self.maxPriceTextF, self.minPriceTextF, self.maxYearTextF, self.minYearTextF], "black")
        changePlaceHolderColor([self.searchTextF], "white")

        self.__createGridLayout()

    def placeCars(self, carList: list = [1,2,3,4,5,6,7]): # It should be carList: list[Car], Car class hasn't been created yet
        self.__clearGridLayout()

        for rowIndex, cars in enumerate(batched(carList, self.__columnNumber)): # NEW!, TODO: Ne işe yaradığını öğren
            for columnIndex, car in enumerate(cars):
                vehicle = VehicleCard()
                """
                vehicle.brand.setText(car.brand)
                vehicle.features.setText(car.features)
                vehicle.price.setText(car.price)
                """
                self.__gridLayout.addWidget(vehicle, rowIndex, columnIndex)

    def resizeEvent(self, event): # NEW!
        new_width = event.size().width()
        if new_width // 450 != self.__columnNumber:
            self.__columnNumber = new_width // 450
            self.placeCars()
        super().resizeEvent(event)

    def __createGridLayout(self):
        self.__gridLayout = QGridLayout(self.carWidget)
        self.carWidgetLayout.addLayout(self.__gridLayout)
        self.__gridLayout.setSpacing(25)
        self.__gridLayout.setContentsMargins(25,25,25,25)
        self.__gridLayout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

    def __clearGridLayout(self):
        for i in reversed(range(self.__gridLayout.count())):
            self.__gridLayout.itemAt(i).widget().setParent(None)
