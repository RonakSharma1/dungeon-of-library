from repository import library_database
import pandas as pd


def get_all_person () :
    return library_database.get_all_person_data()

def get_all_book () :
    return library_database.get_all_book_data()
