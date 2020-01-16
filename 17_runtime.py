"""
Write a program to get execution time for a Python method.
"""

import time

start = time.time()

for i in range(100000000): 
    number = i
end = time.time()
time = end - start
print(time)
