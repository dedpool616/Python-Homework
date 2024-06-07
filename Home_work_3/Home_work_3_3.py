#Write a Python program to get the smallest number from a list.

x = [14,88856,7743,3,0,48,844]

min_num = x[0]

for z in x:
    if z < min_num:
        min_num = z
print(min_num)

