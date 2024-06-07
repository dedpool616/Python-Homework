# Print a square pattern using a nested for loop. The pattern should have 5 rows and 5
# columns.




for i in range(5):
     for j in range(1):
         for k in range(1):
             for x in range(1):
                 for y in range(1):
                     print(i,j,k,x,y)




#VARIANT 2

my_list = [chr(42),chr(42),chr(42),chr(42),chr(42),]
my_list_2 = [chr(42)]

for i in my_list:
    for j in my_list_2:
        for k in my_list_2:
            for x in my_list_2:
                for y in my_list_2:
                    print(i,j,k,x,y)
