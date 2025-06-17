from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QGraphicsDropShadowEffect, QPushButton
from PyQt6.QtGui import QPalette, QColor, QPixmap

class BaseWidget(QWidget):
    def __init__(self, app_controller):
        super().__init__()
        
        from app_controller import AppController
        self.app_controller:AppController = app_controller
        self.background_label: QLabel = None

    def connect_signals(self):
        """Connects signals to their respective slots. Override this method in subclasses."""
        raise NotImplementedError("Subclasses should implement this method.")
    
    def set_properties(self):
        """Sets properties for the widgets. Override this method in subclasses."""
        raise NotImplementedError("Subclasses should implement this method.")

    def set_background_image(self, parent_widget: QWidget, image_path: str) -> None:
        """Sets a background image for the given parent widget."""
        self.background_label = QLabel(parent_widget)
        self.background_label.setGeometry(0, 0, parent_widget.width(), parent_widget.height())
        self.background_label.setPixmap(QPixmap(image_path))
        self.background_label.setScaledContents(True)
        self.background_label.lower() # en arkaya atar
        parent_widget.__setattr__("background_label", self.background_label)

    def set_pixmap(self, widget: QLabel, pixmap: QPixmap):
        widget.setScaledContents(True)
        widget.setPixmap(pixmap)

    def change_place_holder_color(self, tf: QLineEdit, color):
        palette = tf.palette()
        palette.setColor(QPalette.ColorRole.PlaceholderText, QColor(color))
        tf.setPalette(palette)

    def set_drop_shadow(button : QPushButton):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(1)  # Gölgenin yayılma miktarı
        shadow.setOffset(3, 4)  # Gölgenin x ve y ekseninde kayması
        shadow.setColor(QColor.fromRgb(0, 0, 0, 70))  # Gölgenin rengi (RGBA)
        button.setGraphicsEffect(shadow)

    def update_error_style(self, tf: QLineEdit, validation: bool, error_message: str = ""):
        if validation:
            self.clean_error_style(tf)
        else:
            self.set_error_style(tf, error_message)

    def set_error_style(self, tf: QLineEdit, error_message: str):
        tf.setProperty("class", "error")
        tf.style().unpolish(tf)
        tf.style().polish(tf)
        tf.setToolTip(error_message)

    def clean_error_style(self, tf: QLineEdit):
        tf.setProperty("class", "form")
        tf.style().unpolish(tf)
        tf.style().polish(tf)
        tf.setToolTip("")
    
    def resizeEvent(self, a0): # As the window size changes, the size of the background photo also changes.
        self.background_label and self.background_label.setGeometry(0, 0, self.width(), self.height())
        return super().resizeEvent(a0)