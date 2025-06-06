from dataclasses import dataclass
from uuid import uuid4

@dataclass
class Appointment:
    user_id: str
    car_id: str
    start_date: str
    end_date: str
    price: float
    status: int
    entity_id: str = str(uuid4())

@dataclass
class Car:
    brand: str
    model: str
    year: int
    gear_type: str
    gas_type: str
    status: int
    price: int
    entity_id: str = str(uuid4())

@dataclass
class User:
    name: str
    email: str
    birthdate: str
    password: str
    priority: int
    id_number: int
    entity_id: str = str(uuid4())