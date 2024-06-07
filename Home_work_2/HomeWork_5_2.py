#The program prompts the user their birth year. Assuming a person’s age
#is a non-negative integer not exceeding 120, output the user’s age or the
#words “Incorrect Year”. The sample outputs assume it’s currently the year
#2016. If you are writing this program during any other year, the correct
#answers may differ. Store the value of the current year in a variable.
current_year = (1896,2016)

user_year = int(input("write your age "))

subtraction = current_year[-1] - user_year

if current_year[0] <= user_year <= current_year[-1]:
    print(subtraction)
else:
    print("incorrect Year") 


# VARIANT 2 
    
#current_year = 2016

#lim_year = 1896

#user_year = int(input("write your age "))

#subtraction = current_year - user_year

#if lim_year <= user_year <= current_year:
#    print(subtraction)
#else:
#    print("Incorrect Year")