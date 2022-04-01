from xml.dom import ValidationErr
from flask import Flask, request, jsonify
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
            # Serialisation
            schema = UserSchema(only=("full_name", "birth_date"))
            return schema.dump(user)
        except ValidationErr as err:
            print(err.messages)

    else:
        return jsonify(
            isError= True,
            message= "Failure",
            statusCode= 400,
            data= "Invalid request type"), 400

@app.route("/all_book")
def get_book () :
    database_book = library_business.get_all_book()
    return database_book.to_html(header="true", table_id="table")
