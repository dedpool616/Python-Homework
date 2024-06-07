#2. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If
#the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string
#is less than 3, leave it unchanged.
#Example:
#Sample String : 'abc'
#Expected Result : 'abcing'
#_______________________
#Sample String : 'string'
#Expected Result : 'stringly'


text = input('Write your text')

last = text[-3:]

textly = text + "ly"

texting = text + "ing"


if last == "ing":
    print(textly)

else:
    print(texting)



TextTwo = input()

if TextTwo[-3:] == "ing":
    print(TextTwo + "ly")
else:
    print(TextTwo + "ing")
