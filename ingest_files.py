import argparse
import subprocess, sys
import sqlite3

def ingest_files(os_name, file_name, os_type):
    # Array to hold file paths and related info for db insertion
    val = []

    # Open the db and create a cursor
    db_file = r'filepaths.db'
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    # open the csv file of filepaths exported from FTK Imager
    with open(file_name, 'r') as csv:
        # Skip header
        if (os_type == "windows"): next(csv)
        # Create a list from the last column in each row
        data = [line.strip().split(',')[-1] for line in csv.readlines()]
        
        # Determine whether OS is Windows or unix-based
        if os_type == "windows":
        
            # Iterate through each item and select only executables (.exe and .dll) and remove the system backup directory
            for point in data:
                if (point.endswith('.exe"') or point.endswith('.dll"')) and "WinSxS" not in point and "\$" not in point:
                    # Format as readable path and replace the \root\ directory with C:\
                    file_path = ((point.split('[NTFS]')[1])[:-1]).replace('\\[root]\\', 'C:\\')
                    # Separate the file name
                    file_name = file_path.split('\\')[-1]
                    # Add to the array of values
                    val.append((file_name, os_name, file_path))
            
        else:
        
            # Iterate through each item and select only executables (TBD in Linux) and remove the system backup directory
            for point in data:
                # Format as readable path and replace the \root\ directory with C:\
                file_path = point.replace('"','')
                # Separate the file name
                file_name = file_path.split('/')[-1]
                # Add to the array of values
                val.append((file_name, os_name, file_path))

    # Prepare the SQL statement
    sql = "INSERT INTO file_paths (file_name, os_name, file_path) VALUES(?, ?, ?)"

    # Execute the SQL statement with the array of values and commit the changes.
    cur.executemany(sql, val)
    con.commit()
    
    # Close the db.
    con.close()

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description="Ingest csv of file paths.",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("osname", help="Name of OS")
    parser.add_argument("filename", help="Name of CSV file")
    parser.add_argument("ostype", help="Type of OS: Windows or Unix")
    args = parser.parse_args()
    config = vars(args)
    
    # Ingest Files
    ingest_files(config['osname'], config['filename'], config['ostype'])

if __name__ == '__main__':
    main()