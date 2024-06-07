#Input two positive integers, and output a line describing their relation.
#Follow the sample format.

first_number = input("First Number ")
second_number = input("Second Number ")

first_transformation = int(first_number)
second_transformation = int(second_number)



if first_transformation > second_transformation:
    print(first_number + " > " + second_number)
if first_transformation < second_transformation:
    print(first_number + " < " + second_number)
if first_transformation == second_transformation:
    print(first_number + " = " + second_number)