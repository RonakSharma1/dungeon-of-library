from flask import Flask
from service import library_business
app =  Flask(__name__)

@app.route("/all_person")
def get_person () :
    list_of_people = library_business.get_all_person()
    return list_of_people.to_html(header="true", table_id="table")

@app.route("/all_book")
def get_book () :
    database_book = library_business.get_all_book()
    return database_book.to_html(header="true", table_id="table")
