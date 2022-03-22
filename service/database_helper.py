# Database Interactive Helper Functions
from mysql.connector import connect
from mysql.connector import Error
import pandas as pd

# ----------------------- #

# Intitialisation for Database
host_name = "library-dungeons.corn2n66y93y.eu-west-2.rds.amazonaws.com"
user_name = "ronak1997"
user_password = "abcd1234"
db_name = "library_practice"

# Database Queries
query_add_person = ''' INSERT INTO library_practice.Person (Full_Name, Age, Weight, Date_Of_Birth, Country_Of_Birth, Email, Reading_Budget, Gender, Married)
                       VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                   '''
query_add_book = ''' INSERT INTO library_practice.Book (Book_Name, Author_Name, Genre, Price, Current_Owner, Date_of_Issue)
                     VALUES (%s,%s,%s,%s,%s,%s)
                 '''

query_all_person_data = '''
                        SELECT * FROM library_practice.Person;
                      '''

query_all_book_data = '''
                        SELECT * FROM library_practice.Book;
                      '''
# ----------------------- #

# Maybe move these functions to a differnet file such as repository and leave this
#  file as service level and the router as the controller
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
    connection = create_connection(host_name, user_name, user_password, db_name)
    try:
        records = pd.read_sql(query, connection)
        return records

    except Error as e:
        print(f"Error is {e}")

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

def get_all_person () :
    list_of_person = get_from_database(query_all_person_data)
    return list_of_person.set_index("PersonId")

def get_all_book () :
    database_book = get_from_database(query_all_book_data)
    return database_book.set_index("BookId")

def add_person (connection, value) :
    value = tuple(value)
    insert_to_database(connection, query_add_person, value)

def add_book (connection, value) :
    value = tuple(value)
    insert_to_database(connection, query_add_book, value)
