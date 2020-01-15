"""
8. Write a Python program to create a histogram from a given list of integers.
"""
def print_histogram(list):
    flag = True
    count  = 0
    for x in list:
        if flag:
            max = x
            flag = False
        elif max < x:
            max = x
        count +=1
        str = ""
    limit = max
    for x in range(0,max):
        for y in range(0,count):
            if list[y]>=limit:
                str += "* "
            else:
                str += "  "
        str += "\n"
        limit -=1
    print(str)


list = [5,1,3,6,8,7]
print_histogram(list)