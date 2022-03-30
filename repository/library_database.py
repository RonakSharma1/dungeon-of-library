from mysql.connector import connect
from mysql.connector import Error
from dataclasses import astuple
import pandas as pd
import config

def _create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database=db_name
        )
        print(f"Connected to database {db_name}")
    except Error as e:
        print(f"Error is {e}")
    return connection

def _insert_to_database (query, value) :
    connection = _create_connection( config.database["host_name"], 
                                    config.database["user_name"],
                                    config.database["user_password"],
                                    config.database["db_name"])
    cursor =  connection.cursor()
    
    try:
        cursor.execute(query, value)
        connection.commit()

    except Error as e:
        print(f"Error is {e}")

    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

def _get_from_database (query) :
    connection = _create_connection( config.database["host_name"], 
                                    config.database["user_name"],
                                    config.database["user_password"],
                                    config.database["db_name"])
    try:
        records = pd.read_sql(query, connection)
        return records

    except Error as e:
        print(f"Error is {e}")

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

def get_all_user_data():
    list_of_person = _get_from_database(config.database_query["display_user"])
    return list_of_person.set_index("PersonId")

def get_all_book_data():
    list_of_book = _get_from_database(config.database_query["display_book"])
    return list_of_book.set_index("BookId")

def add_new_user(user_information):
    user_information =astuple(user_information)
    _insert_to_database(config.database_query["add_user"], user_information)
