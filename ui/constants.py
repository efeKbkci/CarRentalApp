from enum import Enum

class Windows(Enum):
    LOGIN = 0
    REGISTER = 1
    NORMAL_USER_MAIN = 2
    ADMIN_MAIN = 2
    CAR_SELECTION = 3
    BOOKING = 4
    APPOINTMENTS = 5

class Dialogs(Enum):
    ERROR = "error"
    WARNING = "warning"
    SUCCESS = "success"

class DialogColor:
    ERROR = "#EE404C"
    WARNING = "#FF8000"
    SUCCESS = "#009D8F"