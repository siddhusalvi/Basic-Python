"""
7. Write a Python program to check whether a specified value is contained in a group of values. 
Test Data : 
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
"""
def is_in_list(numbers, num):
    for data in numbers:
        if num == data:
            return True
    return False

data = []

size = int(input("Enter number of elements : ")) 
  
for i in range(0, size): 
    num = int(input()) 
    data.append(num) 

num = int(input("Enter number to check : ")) 

if is_in_list(data, num):
    print("Number is present in the group.")
else:
    print("Number is absent in the group.")
