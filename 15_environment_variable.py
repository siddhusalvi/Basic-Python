"""
Write a python program to access environment variables.
"""
import os

v = os.environ  # getting information of all variables
print(v)

variable = "HOME"
info = os.environ.get(variable)  # accessing specific variable
print(info)

os.environ[variable] = "/c/users/java/jdk"  # modification
