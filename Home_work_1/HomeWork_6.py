#6. Write a Python function to get a string made of its first three characters of a specified string. If
#the length of the string is less than 3 then return the original string.
#Example:
#Sample ='ipy'
#Expected ipy
#______________
#Sample ='python'
#Expected pyt


text = input()

if text ==text[0:3]:
    print(text)
else:
    print(text[0:3])