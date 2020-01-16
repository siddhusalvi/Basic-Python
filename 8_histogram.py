"""
8. Write a Python program to create a histogram from a given list of integers.
"""


def print_histogram(numbers):
    flag = True
    count = 0
    for x in numbers:
        if flag:
            maximum = x
            flag = False
        elif maximum < x:
            maximum = x
        count += 1
        output = ""
    limit = maximum
    for x in range(0, maximum):
        for y in range(0, count):
            if numbers[y] >= limit:
                output += "* "
            else:
                output += "  "
        output += "\n"
        limit -= 1
    print(output)


data = [5, 1, 3, 6, 8, 7]
print_histogram(data)
