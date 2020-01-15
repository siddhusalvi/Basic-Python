"""
21. Write a Python program to sort files by date.
"""
import glob
import os
files = glob.glob("*")
files.sort(key=os.path.getmtime)
print(files)
