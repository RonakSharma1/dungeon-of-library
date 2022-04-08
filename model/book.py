from dataclasses import dataclass, field
from marshmallow import validate
from datetime import date
import marshmallow_dataclass

@dataclass
class Book:
    book_name: str = field(metadata=dict(required=True, 
                                         validate=validate.Length(min=1)))
    author_name: str = field(metadata=dict(required=True, 
                                           validate=validate.Length(min=1)))
    genre: str = field(metadata=dict(required = False, 
                                     load_default="Unknown",
                                     dump_default="Unknown"))
    price: float = field(metadata=dict(required=True))    
    current_owner: int = field(metadata=dict(required = True))
    date_of_issue: date = field(metadata=dict(required=True))
    
BookSchema = marshmallow_dataclass.class_schema(Book)
