"""
43. Write a Python function to find the maximum and minimum numbers from a sequence of
numbers.
Note: Do not use built-in functions.
"""

def sort(data):
    for i in range(1,len(data)):
        ii = data[i]
        j = ii-1
        while j >=0 and ii < data[j]:
            data[j+1] = data[j]
            j -=1
        data[j+1] = i
        return data
list = [1,5,4,8,7,9,6,3,12,15,46,84]
data = sort(list)
min = data[0]
max = list[len(data)-1]
print(min)
print(max)
