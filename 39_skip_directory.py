"""
39. Write a Python program to find files and skip directories of a given directory.
"""

import os

files = os.listdir()
sns = ["1", ".git"]
print(files)
for x in files:
    if os.path.isdir(x) and x not in sns:
        print(x)
