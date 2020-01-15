"""
20. Write a Python program to sort three integers without using conditional statements and
loops.
"""


def sort_three_num(num1,num2,num3):
    maxn = max(num1, max(num2,num3)) 
    minn = min(num1, min(num2, num3))
    middle = (num1 + num2 + num3) - (maxn + minn) 
    print(minn, " " , middle, " " , maxn) 


num1, num2, num3 = 11, 5, 10
sort_three_num(num1,num2,num3) 


