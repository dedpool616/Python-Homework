#Write a Python program to remove duplicates from a list.

my_list = [4,5,6,8,5]

unique_items = []
for item in my_list:
    if item not in unique_items:
        unique_items.append(item)

print(unique_items)