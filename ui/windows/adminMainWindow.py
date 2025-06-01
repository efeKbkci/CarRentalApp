from .. import *
from ..typeHint import Ui_AdminMain
from PyQt6.QtWidgets import QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt

class AdminMainWindow(QWidget, Ui_AdminMain):
    def __init__(self):
        super().__init__()
        loadUi(r"ui\uiFiles\adminMainWindow.ui", self)

        self.setFixedSize(1000, 750)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Font ayarla
        font = QFont("Roboto Mono", 14)
        """
        for row in range(5):
            bgColor = "#FF2E63" if row % 2 else "#D1BEBC"
            textColor = "white" if row % 2 else "black"
            for column in range(7):
                item = QTableWidgetItem(f"Item {row}, {column}")
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                item.setBackground(QColor(bgColor))
                item.setForeground(QColor(textColor))
                self.table.setItem(row, column, item)       """

    def onCarClicked(self, row, col):
        if col == 0:
            print(f"Car clicked: Row {row}")
    
    def onTrashClicked(self, row):
        print(f"Trash clicked: Row {row}")