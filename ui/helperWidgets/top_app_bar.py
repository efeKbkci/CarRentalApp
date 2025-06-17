from .. import loadUi, QWidget
from ..typeHint import Ui_top_app_bar
from ..constants import Windows, Dialogs

from model import Priority

class TopAppBar(QWidget, Ui_top_app_bar):
    def __init__(self, app_controller, window_title: str, show_logout = True, show_back = True):
        super().__init__()
        loadUi(r"ui\uiFiles\topAppBar.ui", self)

        self.app_controller = app_controller

        self.window_title.setText(window_title)

        self.logout_btn.setVisible(show_logout)
        self.back_btn.setVisible(show_back)

        self.logout_btn.clicked.connect(self.logout_btn_clicked)

    def logout_btn_clicked(self):
        session = self.app_controller.authentication.session
        window_manager = self.app_controller.window_manager

        response = window_manager.show_dialog(Dialogs.WARNING, "Log Out", "Are you sure you want to log out?")
        if not response:
            return

        window_manager.navigate_to_window(Windows.LOGIN)

        if session.user.priority == Priority.ADMIN:
            window_manager.delete_admin_window()
        else:
            window_manager.delete_user_windows()
        
        self.app_controller.authentication.reset_session()