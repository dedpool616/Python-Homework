#Input two integers and print out their sum. Preserve the exact format from
#the examples (e.g. the output should contain exactly three lines)

first_num = input("write the first number ")
second_num = input("write the second number ")
first_index = input("write the first index ")
second_index = input("write the second number ")


addition = int(first_num) + int(second_num)
addition_index = first_index + " + " + second_index + " = " + first_num + " + " + second_num + " = " + str(addition)
index_1 = first_index + " = " + first_num
index_2 = second_index + " = " + second_num 


print(index_1)
print(index_2)
print(addition_index)
