"""
2. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""


def generate_list_tuple(data):
    new_list = []
    for x in data:
        if x != ',':
            new_list.append(x)
    print(new_list)
    new_tuple = (*new_list,)
    print(new_tuple)


data = input("Enter your list")
generate_list_tuple(data)
