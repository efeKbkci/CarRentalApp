from PyQt6.QtWidgets import QApplication
from app_controller import AppController
from assets.fonts import FontFamilies
import sys
import os

def turnOffAutoScaling():
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"
    os.environ["QT_SCALE_FACTOR"] = "1"
    os.environ["QT_DEVICE_PIXEL_RATIO"] = "1"

if __name__ == "__main__":

    turnOffAutoScaling()

    app = QApplication(sys.argv)

    FontFamilies.loadFonts()

    app_controller = AppController()

    app_controller.window_manager.show()

    sys.exit(app.exec())
