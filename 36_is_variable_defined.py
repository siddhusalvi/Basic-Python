"""
36. Write a Python program to determine if variable is defined or not.
def is_defined(v):
    try:
        x = x+1;
    except NameError:
        return False
    else:
        return True

print(is_defined(x))
"""

try:
    x = 10
except NameError:
    print("Variable is not defined....!")
else:
    print("Variable is defined.")
try:
    y
except NameError:
    print("Variable is not defined....!")
else:
    print("Variable is defined.")
