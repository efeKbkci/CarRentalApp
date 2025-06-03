from PyQt6.QtGui import QPalette, QColor, QPixmap
from PyQt6.QtWidgets import QGraphicsDropShadowEffect
from . import QWidget, QLabel, QPushButton

def changePlaceHolderColor(widgets: list[QWidget], color):
    for widget in widgets:
        palette = widget.palette()
        palette.setColor(QPalette.ColorRole.PlaceholderText, QColor(color))
        widget.setPalette(palette)

def loadBg(parentWidget: QWidget, bgImage: str):
    background_label = QLabel(parentWidget)
    background_label.setGeometry(0, 0, parentWidget.width(), parentWidget.height())
    background_label.setPixmap(QPixmap(bgImage))
    background_label.setScaledContents(True)
    background_label.lower() # en arkaya atar
    parentWidget.__setattr__("backgroundLabel", background_label)

def addDropShadowToButton(button : QPushButton):
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(1)  # Gölgenin yayılma miktarı
    shadow.setOffset(3, 4)  # Gölgenin x ve y ekseninde kayması
    shadow.setColor(QColor.fromRgb(0, 0, 0, 70))  # Gölgenin rengi (RGBA)
    button.setGraphicsEffect(shadow)