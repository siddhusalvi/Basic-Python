"""1. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them. 
 """

def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
fname = reverse(fname)
lname = reverse(lname)
print ("Hello  " + lname + " " + fname)

