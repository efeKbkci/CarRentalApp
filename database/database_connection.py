import mysql.connector

class DatabaseConnection:
    __active: bool = False

    def __init__(self):
        self.connection = None
        self.cursor = None

        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="taha7373",
                database="rentacar"
            )
            self.cursor = self.connection.cursor()
            self.__active = True
            print(" Database connection established.")
        except mysql.connector.Error as err:
            print("Connection Error:", err)
            self.__active = False

    def is_connection_active(self) -> bool:
        return self.__active

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            self.__active = False
            print("Connection Closed.")
