from dataclasses import dataclass
from datetime import date
from marshmallow import validate, fields
import marshmallow_dataclass

@dataclass
class User:
    full_name: fields.String(required=True, validate=validate.Length(min=1)) 
    age: fields.Integer(required=True, 
                        validate=validate.Range(min=18, max=100),
                        error_messages={"required": {"message": "You must be an adult but not too old", "code": 400}}
                        )
    weight: fields.Integer(load_default=70, dump_default=70)
    birth_date: fields.Date(required=True)
    birth_country: fields.String(required=True)
    email: fields.String(required=True)
    reading_budget: fields.Integer(required=True)
    gender: fields.String(required=True, validate=validate.OneOf(["Male", "Female", "Other"]))
    married: fields.Boolean(load_default=False, dump_default=False)

UserSchema = marshmallow_dataclass.class_schema(User)
