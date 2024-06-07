my_list = [1,2,3,5,7,9,25]
my_func_1 = map(lambda x,:x**2,my_list)
my_func_2 = map(lambda y:y**3,my_list)
print(list(my_func_1),list(my_func_2))
