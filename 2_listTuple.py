"""
2. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""
def generate_list_tuple(str):
    list = []
    for x in str:
        if x != ',':
            list.append(x)
    print(list)
    tuple = (*list, )
    print(tuple)


data = input("Enter your list")
generate_list_tuple(data)