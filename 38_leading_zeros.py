"""
38. Write a Python program to add leading zeroes to a string.
Python string method ljust() returns the string left justified in a string of length 
"""


def add_leading_zeros(word, number):
    zeros = ""
    for x in range(number):
        zeros += "0"
    return zeros + word


str1 = '1.78'
num = 4
print(add_leading_zeros(str1, num))
