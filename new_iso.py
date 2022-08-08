import platform
import os
import argparse
import subprocess, sys
import sqlite3


def mount_iso():
    # Set the command to run the PowerShell script to mount, enumerate, and parse all file paths of a new ISO/OS
    p_cmd = r"new_iso.ps1 -i " + iso + " -os " + os_name + " -type " + os_type
    # Run the command in Powershell, and direct output to stdout
    p = subprocess.Popen(['powershell.exe', p_cmd], stdout=sys.stdout)
    # Redirect output to console
    p.communicate()

def new_iso(iso, os_name, os_type):
    out_file_name = r"file_paths_iso.txt"

    # Open the db and create a cursor
    db_file = r'filepaths.db'
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    sql = "SELECT DISTINCT os_name FROM file_paths WHERE os_name = ?;"
    val = (os_name,)

    os_in_db = cur.execute(sql, val)
    if os_in_db.fetchone():
        print("Error: OS " + os_name + " already exists in db. Please choose a different OS name.")
        quit()

    mount_iso()

    val = []

    with open(out_file_name, 'r') as f:
        for line in f:
            line = line.strip()
            if not line.isspace():
                file_path = line
                file_name = file_path.split('\\')[-1]
                val.append((file_name, os_name, file_path))

    os.remove(out_file_name)

    # Prepare the SQL statement
    sql = "INSERT INTO file_paths (file_name, os_name, file_path) VALUES(?, ?, ?)"

    # Execute the SQL statement with the array of values and commit the changes.
    cur.executemany(sql, val)
    con.commit()

    # Close the db
    con.close()

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description="Enumerate an ISO file.",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("iso", help="Full ISO File Location")
    parser.add_argument("os", help="Name of the OS")
    parser.add_argument("type", help="Type of OS: Windows or Unix")
    args = parser.parse_args()
    config = vars(args)
    
    #New ISO
    new_iso(config['iso'], config['os'], config['type'])

if __name__ == '__main__':
    main()