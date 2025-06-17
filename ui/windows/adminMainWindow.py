from .. import *
from ..typeHint import Ui_admin_main
from ..uiFiles import UiFilePaths
from ..helperWidgets.baseWidget import BaseWidget
from .adminCarDialog import AdminCarDialog
from ..constants import Dialogs
from ..helperWidgets import TopAppBar

from database import Table
from model import Car

from PyQt6.QtWidgets import QHeaderView, QTableWidgetItem, QAbstractItemView
from PyQt6.QtGui import QIcon

class AdminMainWindow(Ui_admin_main, BaseWidget):
    enable_double_click = False

    def __init__(self, app_controller):
        super().__init__(app_controller)
        loadUi(UiFilePaths.ADMIN_MAIN, self)
        
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)        

        self.cars:list[Car] = self.app_controller.db_transaction.get_entities(Table.CAR)
        self.table.setRowCount(len(self.cars))

        [self.fill_table_row(row, car) for row, car in enumerate(self.cars)]

        self.top_app_bar = TopAppBar(app_controller, window_title = "Car Management", show_back = False)
        self.mainLayout.insertWidget(0, self.top_app_bar)

        self.connect_signals()
        self.set_properties()

    def connect_signals(self):
        self.add_car_btn.clicked.connect(self.open_dialog)
        self.editing_active_btn.clicked.connect(self.change_table_edibility)
        self.search_tf.textChanged.connect(self.filter_cars)

    def set_properties(self):
        self.add_car_btn.setProperty("class", "primary")
        self.editing_active_btn.setProperty("dialog", "error")
        self.search_tf.setProperty("class", "primary")

    def fill_table_row(self, row: int, car: Car):
        pixmap = car.image_pixmap.scaled(64, 64)
        label = QLabel()
        label.setPixmap(pixmap)
        self.table.setCellWidget(row, 0, label)

        columns = [
            car.brand, car.model, str(car.year), car.gear_type.capitalize(),
            car.gas_type.capitalize(), "Active" if car.status else "Inactive", f"{car.price:.2f}"
        ]

        for col, value in enumerate(columns, start=1):
            self.table.setItem(row, col, QTableWidgetItem(value))

        delete_btn = QPushButton()
        delete_btn.setIcon(QIcon(r"assets\icons\trash.ico"))
        delete_btn.clicked.connect(lambda: self.delete_car(self.table.currentRow()))
        self.table.setCellWidget(row, 8, delete_btn)

    def open_dialog(self, row: int = None, _ = None):
        car = self.cars[row] if row else None
    
        dialog = AdminCarDialog(self.app_controller, self, car)
    
        if dialog.exec():
            car = dialog.get_data()
            self.update_car(row, car) if row else self.add_car(car)

    def add_car(self, car):
        self.cars.append(car)
        self.app_controller.db_transaction.add_new_entity(Table.CAR, car)
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.fill_table_row(row, car)

    def update_car(self, row, updated_car):
        self.cars[row] = updated_car
        self.app_controller.db_transaction.update_entity(Table.CAR, updated_car)
        self.fill_table_row(row, updated_car)

    def delete_car(self, row):
        response = self.app_controller.window_manager.show_dialog(Dialogs.WARNING, "Car Deletion", "Are you sure you want to delete the car?")  
        
        if not response:
            return
        
        car = self.cars[row]
        self.app_controller.db_transaction.delete_entity(Table.CAR, car.entity_id)
        self.table.removeRow(row)
        self.cars.pop(row)

    def change_table_edibility(self):
        if not self.enable_double_click:
            self.editing_active_btn.setProperty("dialog", "success")
            self.editing_active_btn.setText("Editing On")
            self.table.cellDoubleClicked.connect(self.open_dialog)
            self.enable_double_click = True
        else:     
            self.editing_active_btn.setProperty("dialog", "error")
            self.editing_active_btn.setText("Editing Off")
            self.table.cellDoubleClicked.disconnect()
            self.enable_double_click = False

        self.editing_active_btn.style().unpolish(self.editing_active_btn)
        self.editing_active_btn.style().polish(self.editing_active_btn)
    
    def filter_cars(self):
        keyword = self.search_tf.text()

        for row in range(self.table.rowCount()):
            name = f"{self.table.item(row, 1).text()} {self.table.item(row, 2).text()}".lower()
            self.table.setRowHidden(row, not keyword.lower() in name)