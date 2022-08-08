import argparse
import subprocess, sys
import sqlite3

def search(file_name, os_name):
    print("Searching for " + file_name + " in " + os_name + "...\n")

    # Open the database and create a cursor
    db_file = r'C:\Users\Drew\Desktop\ISOs\week6\filepaths.db'
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    # Create SQL query to search for file
    sql = "SELECT * FROM file_paths WHERE file_name LIKE ? AND os_name LIKE ?;"

    # Format values for query for searching pattern
    file_name = "%" + file_name + "%"
    os_name = "%" + os_name + "%"

    # Create values to put in query
    val = (file_name, os_name)

    # Execute query with values
    out = cur.execute(sql, val)

    # Print the OS and the file path from results
    for row in out:
        print(row[1] + ": " + row[2])

    # Close the db    
    con.close()
    
def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description="Search for executable filename and return known good paths.",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("osname", help="Name of OS")
    parser.add_argument("filename", help="Name of file to search for")
    args = parser.parse_args()
    config = vars(args)
    
    # Search the db
    search(config['osname'], config['filename'])

if __name__ == '__main__':
    main()