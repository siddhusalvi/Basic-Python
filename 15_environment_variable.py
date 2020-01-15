"""
Write a python program to access environment variables.
"""
import os

enviromnt_v =os.environ  #getting information of all variables
#print(enviromnt_v)

variable = "HOME"
data = os.environ.get(variable)#accessing specific variable
print(data)

os.environ[variable] = "/c/users/java/jdk" #modification
