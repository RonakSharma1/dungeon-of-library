import os
# -----------DATABASE CONFIGURATIONS--------#

database = dict(
    host_name = "library-dungeons.corn2n66y93y.eu-west-2.rds.amazonaws.com",
    user_name = os.getenv('DATABASE_USERNAME'),
    user_password = os.getenv('DATABASE_PASSWORD'),
    db_name = "library_practice"
)
# ----------------------------------------- #

# ------------------DATABASE QUERIES-------------#

database_query = dict(
    add_person = '''  INSERT INTO library_practice.Person (Full_Name, Age, Weight, Date_Of_Birth, Country_Of_Birth, Email, Reading_Budget, Gender, Married)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                ''',
    add_book = '''  INSERT INTO library_practice.Book (Book_Name, Author_Name, Genre, Price, Current_Owner, Date_of_Issue)
                    VALUES (%s,%s,%s,%s,%s,%s)
                ''',

    display_person = '''
                    SELECT * FROM library_practice.Person;
                    ''',

    display_book = '''
                    SELECT * FROM library_practice.Book;
                    '''
    
)
# ----------------------------------------- #
