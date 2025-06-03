from enum import Enum

class CarFeatures(str, Enum):
    AUTOMATIC = "automatic"
    MANUAL = "manual"
    GASOLINE = "gasoline"
    DIESEL = "diesel"

class Priority(int, Enum):
    ADMIN = 0
    NORMAL_USER = 1