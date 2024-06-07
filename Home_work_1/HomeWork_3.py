#3. Write a Python program to remove the n-th index character from a nonempty string.
#Example:
#Sample string: ‘abcdefgh’
#n - 3
#Expected result: abcefgh

text = str(input())

NElement = int(input())


NewText = text[:NElement -1] + text[NElement:]

print(NewText)