from ui.windows import *
from PyQt6.QtWidgets import QStackedWidget

class WindowManager(QStackedWidget):
    def __init__(self, app_controller):
        super().__init__()

        window_list = [
                        LoginWindow(app_controller), RegisterWindow(), 
                        UserMainWindow(), AdminMainWindow(), 
                        CarSelectionWindow(), BookingWindow(), 
                        AppointmentWindow()
                    ]
        
        [self.addWidget(widget) for widget in window_list]

    def navigate_to_window(self, window: Windows):
        print(self.currentWidget().size())
        self.setCurrentIndex(window.value)
        print(self.currentWidget().size())

    def show_dialog(self, dialog):
        pass 