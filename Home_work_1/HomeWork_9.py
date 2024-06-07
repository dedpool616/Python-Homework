#9. Append new string in the middle of a given (even number of characters) string
#Example:
#Sample = ‘python’
#new_string = ‘new’
#Expected ‘pytnewhon


Text = input()

TextNumTwo = input()

MiddleText = int(len(Text) / 2)

NewText = Text[:MiddleText] + TextNumTwo + Text[MiddleText:] 

print(NewText)