from PyQt6.QtWidgets import QLabel, QPushButton, QCheckBox, QLineEdit, QWidget

class Ui_car_selection:
    window_title_label: QLabel
    user_name_label: QLabel
    min_price_tf: QLineEdit
    max_price_tf: QLineEdit
    min_year_tf: QLineEdit
    max_year_tf: QLineEdit
    automatic_cbox: QCheckBox
    manual_cbox: QCheckBox
    gasoline_cbox: QCheckBox
    diesel_cbox: QCheckBox
    search_tf: QLineEdit
    apply_btn: QPushButton
    back_btn: QPushButton
    widget_for_cards: QWidget

    @property
    def filter_text_fields(self):
        return [
            self.min_price_tf,
            self.max_price_tf,
            self.min_year_tf,
            self.max_year_tf,
        ]