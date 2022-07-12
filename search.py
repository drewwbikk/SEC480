import argparse
import subprocess, sys

# Parse arguments
parser = argparse.ArgumentParser(description="Search for executable filename and return known good paths.",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("osname", help="Name of OS")
parser.add_argument("filename", help="Name of file to search for")
args = parser.parse_args()
config = vars(args)
osName = config['osname']
fileName = config['filename']

print("Searching for " + fileName + " for " + osName + "...")

# Open file with paths, and search for the file name. Print the path of the file. 
# The plan is to do this in SQL later on, but simple search to test ingest_files.py works correctly.
with open('file_paths.txt', 'r') as inF:
    for line in inF:
        if fileName in line:
            print(line)
            