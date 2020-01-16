"""
37. Write a Python program to empty a variable without destroying it.
type() produces the type object for each value, which when called produces an 'empty' new value.
"""


num = 53
dictionary = {"x": 50}
list1 = [1, 3, 5]
tuple1= (5, 7, 8)
print(type(num)())
print(type(dictionary)())
print(type(list1)())
print(type(tuple1)())
