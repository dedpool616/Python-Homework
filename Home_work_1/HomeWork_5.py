#5. Write a Python function to get a string made of 4 copies of the last two characters of a
#specified string (length must be at least 2).
#Example:
#Sample = ‘Python'
#Expected onononon
#________________
#Sample 'Exercises'
#Expected eseseses


text = input()

factor = int(input())

NewText = text[-2:] * factor

print(NewText)