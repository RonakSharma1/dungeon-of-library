from dataclasses import dataclass, field
from datetime import date
from marshmallow import validate
import marshmallow_dataclass

@dataclass
class User:
    full_name: str = field(metadata=dict(required=True, 
                                         validate=validate.Length(min=1))) 
    age: int = field(metadata=dict(required=True, 
                                   validate=validate.Range(min=18, max=100),
                                   error_messages={"required": {"message": "You must be an adult but not too old", 
                                                                "code": 400}}))
    weight: float = field(metadata=dict(required = False, 
                                      load_default=70))
    birth_date: date = field(metadata=dict(required=True))
    birth_country: str = field(metadata=dict(required=True))
    email: str = field(metadata=dict(required=True))
    reading_budget: float = field(metadata=dict(required=True))
    gender: str = field(metadata=dict(required=True, 
                                      validate=validate.OneOf(["Male", "Female", "Other"])))
    married: bool = field(metadata=dict(required = False, 
                                        load_default=False))

UserSchema = marshmallow_dataclass.class_schema(User)
