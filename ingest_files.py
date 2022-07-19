import argparse
import subprocess, sys
import sqlite3

# Parse arguments
parser = argparse.ArgumentParser(description="Ingest csv of file paths.",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("osname", help="Name of OS")
parser.add_argument("filename", help="Name of CSV file")
parser.add_argument("type", help="Type of OS: Windows or Unix")
args = parser.parse_args()
config = vars(args)
osName = config['osname']
fileName = config['filename']
osType = config['type']

# Array to hold file paths and related info for db insertion
val = []

# Open the db and create a cursor
db_file = r'C:\Users\Drew\Desktop\ISOs\week6\filepaths.db'
con = sqlite3.connect(db_file)
cur = con.cursor()

# open the csv file of filepaths exported from FTK Imager
with open(fileName, 'r') as csv:
    # Skip header
    next(csv)
    # Create a list from the last column in each row
    data = [line.strip().split(',')[-1] for line in csv.readlines()]
    
    # Determine whether OS is Windows or unix-based
    if osType == "windows":
    
        # Iterate through each item and select only executables (.exe and .dll) and remove the system backup directory
        for point in data:
            if (point.endswith('.exe"') or point.endswith('.dll"')) and "WinSxS" not in point and "\$" not in point:
                # Format as readable path and replace the \root\ directory with C:\
                file_path = ((point.split('[NTFS]')[1])[:-1]).replace('\\[root]\\', 'C:\\')
                # Separate the file name
                file_name = file_path.split('\\')[-1]
                # Add to the array of values
                val.append((file_name, osName, file_path))
        
        # Prepare the SQL statement
        sql = "INSERT INTO file_paths (file_name, os_name, file_path) VALUES(?, ?, ?)"
        
        # Execute the SQL statement with the array of values and commit the changes.
        cur.executemany(sql, out)
        con.commit()
    else:
    
        # Iterate through each item and select only executables (TBD in Linux) and remove the system backup directory
        for point in data:
            # Format as readable path and replace the \root\ directory with /
            file_path = ((point.split('[NTFS]')[1])[:-1]).replace('\\[root]\\', '\/')
            # Add to the output
            # out += file_path + "\n"

# Close the db.
con.close()