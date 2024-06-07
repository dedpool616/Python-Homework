# Print the multiplication table of 5 using a for loop and f”strings”. The table should be
# printed up to 10

x = [1,2,3,4,5,6,7,8,9,10]

for i in x:
    result = 5*i
    y = f'5*{i}={result}'
    print(y)