"""
30. Write a Python program to access and print a URL's content to the console.
"""

from http.client import HTTPConnection
conn = HTTPConnection("medium.com")
conn.request("GET", "/")  
result = conn.getresponse() 
data = result.read() 
print(data)
