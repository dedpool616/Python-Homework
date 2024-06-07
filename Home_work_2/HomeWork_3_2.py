#Input a two-digit natural number and output the sum of its digits. You can
#assume that the input will be a two-digit number and need not check that
#programmatically.

number = input()

first_element = number[0]
second_element = number[-1]
addition_element = int(first_element) + int(second_element)

if len(number) == 2:
    print(addition_element)
else:
    print("Error")