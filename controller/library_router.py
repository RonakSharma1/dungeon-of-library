from marshmallow import ValidationError
from flask import Flask, request, jsonify
from model.book import BookSchema
from model.user import UserSchema
from service import library_business

app =  Flask(__name__)

@app.route("/all_user", methods=['GET', 'POST'])
def get_user () :
    if request.method == 'GET':
        list_of_people = library_business.get_all_user()
        return list_of_people.to_html(header="true", table_id="table")
    elif request.method == 'POST':
        try:
            # Deserialisation
            user = UserSchema().load(request.get_json())
            library_business.add_user(user)
            # Serialisation (AN ID SHOULD BE RETURNED)
            schema = UserSchema(only=("full_name", "birth_date"))
            return schema.dump(user)
        except ValidationError as err:
            return(err.messages)
    else:
        return jsonify(
            isError= True,
            message= "Failure",
            statusCode= 400,
            data= "Invalid request type"), 400

@app.route("/all_book", methods=['GET', 'POST'])
def get_book () :
    if request.method == 'GET':
        database_book = library_business.get_all_book()
        return database_book.to_html(header="true", table_id="table")
    elif request.method == 'POST':
        try:
            # Deserialisation
                # Use  BookSchema(many=True) when multiple objects in POST
            book = BookSchema().load(request.get_json())
            library_business.add_book(book)

            # Serialisation (An ID should be returned)
            schema = BookSchema(only={"book_name","author_name","price"})
            return schema.dump(book)
        except ValidationError as err:
            return(err.messages)
    else:
        return jsonify(
            isError= True,
            message= "Failure",
            statusCode= 400,
            data= "Invalid request type"), 400
