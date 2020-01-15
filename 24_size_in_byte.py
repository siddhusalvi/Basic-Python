"""
24. Write a Python program to get the size of an object in bytes.
"""

import sys
str1 = "ten"
print("Memory size of '"+str1+"' = "+str(sys.getsizeof(str1))+ " bytes")
print()
