#Write a Python program to find the second smallest number in a list.
x = [4,45,68,875]

first_min = x[0]
second_min = x[0]
first_max = x[0]

for i in x:
    if i < first_min:
        first_min = i
    elif i > first_max:
        first_max = i
    elif second_min < first_max and second_min > first_min:
        second_min = i
    print(second_min)

    