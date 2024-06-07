# Write a Python program to find if a given string starts with a given
# character using Lambda.

my_text= input("input your text")
search_symbol= input("inpput your simvvol")
func_1= filter(lambda x:x==search_symbol,my_text[0])
print(list(func_1))

# ...........................................................................
#VARIANT 2 bayc chi ashxatum normal 


# my_text= input("input your text ")
# transform = my_text.split()
# print(transform[0])
# search_symbol= input("inpput your simvvol ")
# func_1= filter(lambda x:x is search_symbol,transform[0])
# print(list(func_1))

