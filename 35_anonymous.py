"""
35. Write a Python program to get numbers divisible by fifteen from a list using an anonymous
function.
"""

numbers = [47,78,12,15,64,19,30,300]
#result = list(filter(lambda x: (x % 15 == 0), numbers))
result = []
for i in numbers:
    lambda i : (i % 15 == 0),result.append(i)
print(result)