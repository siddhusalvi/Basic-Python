"""
7. Write a Python program to check whether a specified value is contained in a group of values. 
Test Data : 
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
"""


def is_in_group(numbers, elem):
    for i in numbers:
        if elem == i:
            return True
    return False


data = []
size = int(input("Enter number of elements : "))
for i in range(0, size):
    ele = input("enter a ele :")
    data.append(ele)
ele = int(input("Enter number to check : "))
if is_in_group(data, ele):
    print("element is present in the group.")
else:
    print("element is absent in the group.")
