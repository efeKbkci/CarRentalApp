from .baseWidget import BaseWidget
from .vehicleCard import VehicleCard

from .. import loadUi, UiFilePaths
from ..constants import Windows
from ..typeHint import Ui_car_selection

from model import Car, CarFeatures
from database import Table

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator, QDoubleValidator 
from PyQt6.QtWidgets import QGridLayout
from itertools import batched

class CarSelectionWindow(Ui_car_selection, BaseWidget):    
    __columnNumber = 0
    __car_list = []

    def __init__(self, app_controller):
        super().__init__(app_controller)
        loadUi(UiFilePaths.CAR_SELECTION, self)

        self.set_properties()

        self.connect_signals()
    
        [self.change_place_holder_color(tf, "black") for tf in self.filter_text_fields]
        self.change_place_holder_color(self.search_tf, "white")
        [tf.setValidator(QDoubleValidator(bottom = 0)) for tf in (self.min_price_tf, self.max_price_tf)]
        [tf.setValidator(QIntValidator(bottom = 2000)) for tf in (self.min_year_tf, self.max_year_tf)]
    
        self.__createGridLayout()

    def connect_signals(self):
        self.apply_btn.clicked.connect(self.place_cars)
        self.back_btn.clicked.connect(lambda: self.app_controller.window_manager.navigate_to_window(Windows.NORMAL_USER_MAIN))

    def set_properties(self):
        self.apply_btn.setProperty("class", "primary")

    def place_cars(self):
        self.__clearGridLayout()

        self.__car_list = self.app_controller.db_transaction.get_entities(Table.CAR)
        filtered_cars = self.filter_cars(self.__car_list)

        # batched function is used to split the list into chunks of size __columnNumber 
        # Example: car_list = [1,2,3,4,5,6,7,8,9] and __columnNumber = 3
        # will return [[1,2,3], [4,5,6], [7,8,9]]
        # with enumerate, it'll return (0, [1,2,3]), (1, [4,5,6]), (2, [7,8,9])
        for rowIndex, cars in enumerate(batched(filtered_cars, self.__columnNumber)): 
            for columnIndex, car in enumerate(cars):
                card = VehicleCard(car)
                card.clicked.connect(self.card_clicked)
                self.__car_list.append(card)
                self.__gridLayout.addWidget(card, rowIndex, columnIndex)

    def card_clicked(self, card: VehicleCard):
        self.app_controller.window_manager.window_dict[Windows.BOOKING].viewed_car = card.car
        self.app_controller.window_manager.window_dict[Windows.BOOKING].adjust_window()
        self.app_controller.window_manager.navigate_to_window(Windows.BOOKING)

    def filter_cars(self, car_list: list[Car]) -> list[Car]:
        min_price, max_price = [float(price) if price else None for price in (self.min_price_tf.text(), self.max_price_tf.text())]
        min_year, max_year = [int(year) if year else None for year in (self.min_year_tf.text(), self.max_year_tf.text())]

        search_text = self.search_tf.text().strip().lower()

        filtered_cars = []

        for car in car_list:
            car: Car
            if not car.status:
                continue
            
            if (min_price and car.price < min_price) or (max_price and car.price > max_price):
                continue
            
            if (min_year and car.year < min_year) or (max_year and car.year > max_year):
                continue

            if car.gear_type == CarFeatures.AUTOMATIC and not self.automatic_cbox.isChecked():
                continue

            if car.gear_type == CarFeatures.MANUAL and not self.manual_cbox.isChecked():
                continue

            if car.gas_type == CarFeatures.DIESEL and not self.diesel_cbox.isChecked():
                continue

            if car.gas_type == CarFeatures.GASOLINE and not self.gasoline_cbox.isChecked():
                continue
            
            if search_text and search_text not in car.full_name.lower():
                continue

            filtered_cars.append(car)

        return filtered_cars

    def __createGridLayout(self):
        self.__gridLayout = QGridLayout()
        self.widget_for_cards.setLayout(self.__gridLayout)
        self.__gridLayout.setSpacing(25)
        self.__gridLayout.setContentsMargins(25,25,25,25)
        self.__gridLayout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

    def __clearGridLayout(self):
        for i in reversed(range(self.__gridLayout.count())):
            card = self.__gridLayout.itemAt(i).widget()
            card.setParent(None)
            card.deleteLater()
        self.__gridLayout.update()

    def resizeEvent(self, event): # NEW!
        new_width = event.size().width()
        if new_width // 450 != self.__columnNumber:
            self.__columnNumber = new_width // 450
            self.place_cars()
        super().resizeEvent(event)
