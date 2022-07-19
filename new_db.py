import sqlite3
from sqlite3 import Error

# fully-qualified path for db
db_path = r"C:\Users\Drew\Desktop\ISOs\week6\filepaths.db"

# Initialize connection variable
con = None

# Try to connect to the db (create it if it doesn't exist)
try:
    con = sqlite3.connect(db_path)
except Error as e:
    print(e)
finally:
    if con:
        print("Database created.")

# Create the table for filepaths if it doesn't exist yet.
con.execute('''CREATE TABLE IF NOT EXISTS file_paths(
"file_name" TEXT NOT NULL,
"os_name" TEXT NOT NULL,
"file_path" TEXT NOT NULL);''')

# Close the db
con.close()