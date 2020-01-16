"""
20. Write a Python program to sort three integers without using conditional statements and
loops.
"""


def sort_three_num(number1, number2, number3):
    maximum = max(number1, max(number2, number3))
    minimum = min(number1, min(number2, number3))
    middle = (number1 + number2 + number3) - (maximum + minimum)
    print("minimus :", minimum, "middle :", middle, "max :", maximum)


numb1, numb2, numb3 = 11, 5, 10
sort_three_num(numb1, numb2, numb3)
