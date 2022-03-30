from dataclasses import dataclass
from datetime import date
from marshmallow import validate
import marshmallow_dataclass

@dataclass
class Book:
    book_name: str
    author_name: str
    price: int
    date_of_issue: date
    genre: str
    reading_budget: int
    current_owner: str

BookSchema = marshmallow_dataclass.class_schema(Book)
