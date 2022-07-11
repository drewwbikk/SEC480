import json
import argparse

# Parse arguments
parser = argparse.ArgumentParser(description="Search a JSON db file.",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-db", help="Full JSON DB File Location")
parser.add_argument("-file", help="Name and extension of file you want to search")
parser.add_argument("-os", help="Name of the OS")
args = parser.parse_args()
config = vars(args)
file_name = config['db']
exe_name = config['file']
os_name = config['os']
winIsoPath = ""

# File name of json db file, will be a required parameter in the future
file_name = r"C:\Users\Drew\Desktop\ISOs\paths.json"

# Open the json file and load the multidimensional array into a python dictionary
with open(file_name, 'r', encoding='utf-8') as f:
    os_paths = json.load(f)

# Check if the OS name parameter passed matches an OS in the db (dict)
if not os_name in os_paths.keys():
    print("\'" + os_name + "\' OS not in database!")
    print("Current OSs in database:", end=" ")
    for key in os_paths.keys():
        print(key, end=" ", flush=True)