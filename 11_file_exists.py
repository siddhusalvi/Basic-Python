"""
11. Write a Python program to check whether a file exists.
"""

import os.path


def is_exist(filename):
    try:
        with open(filename, 'r') as f:
            return True
    except IOError as x:
        return False


file = "one.txt"

if is_exist(file):
    print("File is exist.")
else:
    print("File doesn't exist.")
