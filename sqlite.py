import sqlite3

## Connect to database
connection = sqlite3.connect("student.db")

## Create a cursor object to execute queries
cursor = connection.cursor()

## Create the table if it does not already exist
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
"""
cursor.execute(table_info)  # Execute the table creation query

## Insert some records
cursor.execute("INSERT INTO STUDENT VALUES ('Huzaifa', 'Data Science', 'A', 90)")
cursor.execute("INSERT INTO STUDENT VALUES ('Okasha', 'Data Science', 'B', 100)")
cursor.execute("INSERT INTO STUDENT VALUES ('Ali', 'Data Science', 'A', 86)")
cursor.execute("INSERT INTO STUDENT VALUES ('Akram', 'Database', 'A', 50)")
cursor.execute("INSERT INTO STUDENT VALUES ('Danish', 'Database', 'A', 35)")

## Display all the records
print("The inserted records are:")
data = cursor.execute("SELECT * FROM STUDENT")
for row in data:
    print(row)

## Commit your changes in the database
connection.commit()
connection.close()
