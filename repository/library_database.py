from mysql.connector import connect
from mysql.connector import Error
import pandas as pd
import config

def create_connection(host_name, user_name, user_password, db_name):
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

def insert_to_database (connection, query, value) :
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

def get_from_database (query) :
    connection = create_connection( config.database["host_name"], 
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

def get_all_person_data():
    list_of_person = get_from_database(config.database_query["display_person"])
    return list_of_person.set_index("PersonId")

def get_all_book_data():
    list_of_book = get_from_database(config.database_query["display_book"])
    return list_of_book.set_index("BookId")
