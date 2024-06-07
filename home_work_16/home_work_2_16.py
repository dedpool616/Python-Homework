# Write a function that removes an element at a specified index from a list. Handle the
# IndexError by raising a custom exception if the index is out of range.

def my_func(my_list,list_index):
    try:
        my_list.pop(list_index)
    except IndexError:
        print("high index value")
    return my_list
print(my_func(["hello","1254","alacazam"],-1))