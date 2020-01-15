"""
42. Write a Python program to determine if the python shell is executing in 32bit or 64bit mode
on operating syst struct is a module for packing and unpacking data to and from C representations.

P represents void * (a generic pointer). 
"""
import struct
print(struct.calcsize("P") * 8)
