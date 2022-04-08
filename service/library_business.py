from marshmallow_dataclass import dataclass
from repository import library_database

def get_all_user() :
    return library_database.get_all_user_data()

def get_all_book() :
    return library_database.get_all_book_data()

def add_user(user_information):
    print(user_information.age, user_information.weight, user_information.birth_date)
    library_database.add_new_user(user_information)
