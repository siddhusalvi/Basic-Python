"""
38. Write a Python program to add leading zeroes to a string.
Python string method ljust() returns the string left justified in a string of length 
"""
def add_leadin_zeros(str,num):
    zeros = ""
    for x in range(num):
        zeros += "0"
    return zeros + str
str1='1.78'
num =4
print(add_leadin_zeros(str1,num))
