from dataclasses import dataclass, field

from uuid import uuid4
from PyQt6.QtGui import QPixmap
import os

@dataclass
class Appointment:
    user_id: str
    car_id: str
    start_date: str
    end_date: str
    price: float
    status: int
    entity_id: str = field(default_factory=lambda: str(uuid4()))

@dataclass
class Car:
    brand: str
    model: str
    year: int
    gear_type: str
    gas_type: str
    status: int
    price: float
    car_image_path: str
    entity_id: str = field(default_factory=lambda: str(uuid4()))

    @property
    def full_name(self) -> str:
        return f"{self.brand} {self.model}"
    
    @property
    def image_pixmap(self) -> QPixmap | None:
        return QPixmap(self.car_image_path) if os.path.exists(self.car_image_path) else None

    @property
    def price_str(self) -> str:
        return f"{self.price} $"    
    
    @property
    def features(self) -> str:
        return f"{self.gear_type} | {self.gas_type} | {self.year}"



@dataclass
class User:
    name: str
    email: str
    birthdate: str
    password: str
    priority: int
    id_number: int
    entity_id: str = field(default_factory=lambda: str(uuid4()))