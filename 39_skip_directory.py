"""
39. Write a Python program to find files and skip directories of a given directory.
"""

import os
files = os.listdir()
dir = ["1",".git"]
print(files)
#print(os.path.abspath("/1"))
for x in files:
    if os.path.isdir(x) and x not in dir:
         print(x)
