"""
26. Write a Python program to count the number occurrence of a specific character in a string. 
"""


def count_occur(word, c):  # function to return count
    count = 0
    for i in range(len(word)):
        if word[i] == c:
            count += 1
    return count


word = "thisisveryverybigword"
c = 'i'
print(count_occur(word, c))
