import platform
import os
import argparse
import subprocess, sys

# Parse arguments
parser = argparse.ArgumentParser(description="Enumerate an ISO file.",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("iso", help="Full ISO File Location")
parser.add_argument("os", help="Name of the OS")
parser.add_argument("type", help="Type of OS: Windows or Unix")
args = parser.parse_args()
config = vars(args)
iso = config['iso']
osName = config['os']
osType = config['type']
winIsoPath = ""

def mount_iso():
    # Set the command to run the PowerShell script to mount, enumerate, and parse all file paths of a new ISO/OS
    p_cmd = r"C:\Users\Drew\Desktop\ISOs\week6\new_iso.ps1 -i " + iso + " -os " + osName + " -type " + osType
    # Run the command in Powershell, and direct output to stdout
    p = subprocess.Popen(['powershell.exe', p_cmd], stdout=sys.stdout)
    # Redirect output to console
    p.communicate()

mount_iso()