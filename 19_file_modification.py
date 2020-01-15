"""
19. Write a Python program to get file creation and modification date/times.
"""

import os
import datetime
 
file = "/home/admin2/Desktop/random.csv"
 
print("Created :")
print(os.path.getctime(file))
print(datetime.datetime.fromtimestamp(os.path.getctime(file))) 
print("Modified:")
print(os.path.getmtime(file))
print(datetime.datetime.fromtimestamp(os.path.getmtime(file)))
