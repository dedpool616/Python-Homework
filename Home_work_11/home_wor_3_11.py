# Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument

def factorial(number):
    a = 1
    for i in range(1,number + 1):
        a*=i
    return(a)
y = factorial(8)
print(y)