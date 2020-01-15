"""
9. Write a Python program to concatenate all elements in a list into a string and return it.  
"""
def concatenate_list(list): #Function to concatenate list
    output =""
    for data in list:
        output += str(data)
    return output

data = ['a','b','c','d','e']

string = concatenate_list(data)
print(string)
