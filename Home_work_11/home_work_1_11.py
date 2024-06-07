# Write a Python function to find the Max of three numbers.


def max_num(first_num,second_num,third_num):
    empty = 0
    if first_num > second_num and first_num > third_num:
        empty = first_num
    elif second_num > first_num and second_num > third_num:
        empty = second_num
    elif third_num > first_num and third_num > second_num:
        empty = third_num
    return empty


y = max_num(3,2,1)
print(y)