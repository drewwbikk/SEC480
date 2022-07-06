import platform
import os
import argparse
import subprocess, sys

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
    p_cmd = r"C:\Users\Drew\Desktop\ISOs\new_iso.ps1 -i " + iso + " -os " + osName + " -type " + osType
    p = subprocess.Popen(['powershell.exe', p_cmd], stdout=sys.stdout)
    p.communicate()

mount_iso()