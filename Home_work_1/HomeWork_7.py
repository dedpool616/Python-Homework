#7. Write a Python program to print the floating numbers upto 2 decimal places
#(number must be not greater than 10)
#Example:
#Sample = 2.145548
#Expected - 2.14
#_______________________
#Sample = 9.5748
#Expected - 9.57

FloatNum = float(input())
    
IntNum = FloatNum * 100

ShortFloatNum = int(IntNum) / 100 
 
print(ShortFloatNum)


