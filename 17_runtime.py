"""
Write a program to get execution time for a Python method.
"""

import time
start = time.time()

for i in range(100000000):#approx 5 sec
   num = i 
end = time.time()
time = end-start
print(time)
