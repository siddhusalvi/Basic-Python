"""
31. Write a Python program to get system command output.
"""

import subprocess
data = subprocess.check_output("dir", shell=True, universal_newlines=True)
print("dir command to list file and directory")
print(data)
