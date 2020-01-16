"""1. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them. 
 """


def reverse(word):
    new_word = ""
    for i in word:
        new_word = i + new_word
    return new_word


fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
fname = reverse(fname)
lname = reverse(lname)
print("Hello  " + fname + " " + lname)
