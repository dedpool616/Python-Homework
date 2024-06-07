#8.Create a string made of the first, middle and last character of given string with odd number of
#ymbols
#Example:
#Sample = ‘Sevak’
#Expected ‘Svk’



text = input()

MiddleText =int(len(text) / 2)

NewText = text[0] + text[MiddleText] + text[-1] 


print(NewText)

