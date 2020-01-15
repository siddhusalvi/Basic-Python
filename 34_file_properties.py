"""
34. Write a Python program to retrieve file properties.
"""

import os.path
import time

file = "/home/admin2/Desktop/random.csv"
print('File         :', file)
print('Access time  :', time.ctime(os.path.getatime(file)))
print('Modified time:', time.ctime(os.path.getmtime(file)))
print('Change time  :', time.ctime(os.path.getctime(file)))
print('Size         :', os.path.getsize(file))
