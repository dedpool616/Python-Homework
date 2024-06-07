#Input three integers. Output the word “Sorted” if the numbers are listed in
#a non-increasing or non-decreasing order and “Unsorted” otherwise.

x = int(input())
y = int(input())
z = int(input())

if x <= y <= z:
    print("Sorted")
elif x >= y >= z:
    print("Sorted")
else:
    print("Unsorted")

#Variant 2
    
#x = int(input())
#y = int(input())
#z = int(input())

#status = "Unsorted"

#if x <= y <= z:
#    status = "Sorted"
#elif x >= y >= z:
#    status = "Sorted"
#else:
#    status = "Unsorted"

#print(status)
