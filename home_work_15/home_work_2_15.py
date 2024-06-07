# Write a function that generates a random password for the user. Allow the user to
# specify the length and complexity of the password (include letters, numbers, and
# symbols).
# Ogtvel random u string module-neric (string.ascii_letters,
# string.digits,string.punctuation, 
# 

# chhaskaca vonca petq anel 
import random as a
pasword_length = int(input("password length "))
x = chr(a.randint(32,127))
y = []
while len(y) == pasword_length:
    y.append(x)
print(y)

