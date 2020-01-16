"""
41. Write a Python program to convert an integer to binary keep leading zeros.
Question is wrong
Sample data : 50
Expected output : 110010
"""


def int_to_binary(number, data):  # function that returns binary number
    data = ""
    while number != 0:
        data += str(number % 2)
        number = number // 2
    reverse = ""
    for i in data:
        reverse = i + reverse
    print(reverse)


num = 20
print(int_to_binary(num, " "))
