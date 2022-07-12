import argparse
import subprocess, sys

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

# String for output to file
out = ""

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
            if (point.endswith('.exe"') or point.endswith('.dll"')) and "WinSxS" not in point:
                # Format as readable path and replace the \root\ directory with C:\
                file_path = ((point.split('[NTFS]')[1])[:-1]).replace('\\[root]\\', 'C:\\')
                # Add to the output
                out += file_path + "\n"
    else:
    
        # Iterate through each item and select only executables (TBD in Linux) and remove the system backup directory
        for point in data:
            # Format as readable path and replace the \root\ directory with /
            file_path = ((point.split('[NTFS]')[1])[:-1]).replace('\\[root]\\', '\/')
            # Add to the output
            out += file_path + "\n"

# Write output to txt file while SQL isn't set up yet, to test if output is generating correctly.
text_file = open("file_paths.txt", "w")
n = text_file.write(out)
text_file.close()