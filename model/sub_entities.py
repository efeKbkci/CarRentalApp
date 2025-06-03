from dataclasses import dataclass
from datetime import datetime
from .constants import CarFeatures, Priority
from .base_entity import BaseEntity

@dataclass
class Appointment(BaseEntity):
    user_id: str
    car_id: str
    start_time: datetime
    end_time: datetime
    total_price: float
    pdf_document = None #NOT READY

@dataclass
class Car(BaseEntity):
    brand: str
    model: str
    year: int
    gear_type: CarFeatures
    gas_type: CarFeatures

@dataclass
class User(BaseEntity):
    name: str
    surname: str
    email: str
    birth_date: datetime
    priority: Priority

@dataclass
class RegistrationFormDTO(User):
    password: str