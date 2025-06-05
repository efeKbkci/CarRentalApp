from os.path import join

class UiFilePaths:
    __base_directory = r".\ui\uiFiles"

    LOGIN = join(__base_directory, "loginWindow.ui")
    REGISTER = join(__base_directory, "registerWindow.ui")
    USER_MAIN = join(__base_directory, "userMainWindow.ui")
    ADMIN_MAIN = join(__base_directory, "adminMainWindow.ui")
    APPOINTMENTS = join(__base_directory, "appointmentsWindow.ui")
    APPOINTMENT_CARD = join(__base_directory, "appointmentCard.ui")
    CAR_SELECTION = join(__base_directory, "carSelectionWindow.ui")
    VEHICLE_CARD = join(__base_directory, "vehicleCard.ui")
    BOOKING = join(__base_directory, "bookingWindow.ui")