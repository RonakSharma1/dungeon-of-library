from dataclasses import dataclass
from datetime import date
from marshmallow import validate
import marshmallow_dataclass

@dataclass
class User:
    full_name: str
    age: int
    weight: int
    birth_date: date
    birth_country: str
    email: str
    reading_budget: int
    gender: str
    married: bool

UserSchema = marshmallow_dataclass.class_schema(User)
