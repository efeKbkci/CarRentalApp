from .constants import Windows, Dialogs
from .windows import *
from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QSizePolicy
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtCore import QSize

class CustomStackedWidget(QStackedWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
    def sizeHint(self):
        current = self.currentWidget()
        return current.sizeHint() if current else super().sizeHint()

class WindowManager(QMainWindow):

    def __init__(self, app_controller):
        super().__init__()

        self.app_controller = app_controller
        self.screen_size = QGuiApplication.primaryScreen().availableSize()
        self.stacked_widget = CustomStackedWidget(self)

        self.setCentralWidget(self.stacked_widget)
        self.setWindowTitle("Car Rental Application")

        self.window_size_dict = {
            Windows.LOGIN: QSize(800, 600),
            Windows.REGISTER: QSize(800, 600),
            Windows.CAR_SELECTION: QSize(1000, 750),
            Windows.BOOKING: QSize(1000, 750),
            Windows.APPOINTMENTS: QSize(1000, 750)
        }

        self.login_screen = LoginWindow(app_controller)
        self.register_screen = RegisterWindow(app_controller)

        self.window_dict = {
            Windows.LOGIN: self.login_screen,
            Windows.REGISTER: self.register_screen
        }

        self.stacked_widget.addWidget(self.login_screen)
        self.stacked_widget.addWidget(self.register_screen)

        self.dialog = DialogBox(None)

        self.center_widget(self.login_screen)

    def create_user_windows(self):
        window_dict = {
            Windows.NORMAL_USER_MAIN: UserMainWindow(self.app_controller),
            Windows.CAR_SELECTION: CarSelectionWindow(self.app_controller),
            Windows.BOOKING: BookingWindow(self.app_controller),
            Windows.APPOINTMENTS: AppointmentWindow(self.app_controller)
        }

        [self.stacked_widget.addWidget(widget) for widget in window_dict.values()]
        
        self.window_size_dict[Windows.NORMAL_USER_MAIN] = QSize(800, 600)

        self.window_dict.update(window_dict) 

    def create_admin_window(self):
        admin_main = AdminMainWindow(self.app_controller)
        self.stacked_widget.addWidget(admin_main)
        self.window_dict[Windows.ADMIN_MAIN] = admin_main      
        self.window_size_dict[Windows.ADMIN_MAIN] = QSize(1000, 750)  

    def delete_user_windows(self):
        for index in (Windows.NORMAL_USER_MAIN, Windows.CAR_SELECTION, Windows.BOOKING, Windows.APPOINTMENTS):
            self.remove_window(index)

    def delete_admin_window(self):
        self.remove_window(Windows.ADMIN_MAIN)

    def remove_window(self, window_index: Windows):
        window = self.window_dict[window_index]
        self.stacked_widget.removeWidget(window)
        window.deleteLater()
        self.window_dict.pop(window_index)

    def navigate_to_window(self, window: Windows):
        self.stacked_widget.setCurrentIndex(window.value)
        self.center_widget(self.window_size_dict[window])

    def closeEvent(self, a0):
        self.app_controller.teardown()
        return super().closeEvent(a0)

    def show_dialog(self, dialog_type:Dialogs, subject: str, message: str = "", single_btn: bool = False) -> int:
        self.dialog.change_appearance(dialog_type, subject, message, single_btn)
        return self.dialog.exec()
    
    def center_widget(self, child_widget_size: QSize):
        child_w = child_widget_size.width()
        child_h = child_widget_size.height()
        screen_w = self.screen_size.width()
        screen_h = self.screen_size.height()

        x = (screen_w - child_w) // 2
        y = (screen_h - child_h) // 2

        self.setGeometry(x, y, child_w, child_h)