#4. Write a Python program to change a given string to a new string where the first and last chars
#have been exchanged.
#Example:
#Sample: ‘abcdefgh’
#Expected: ‘hbcdefga’


text = input()

NumOne = int(input())

NumTwo = int(input())

NewText = text[NumOne] + text[1:-1] + text[NumTwo]

print(NewText)