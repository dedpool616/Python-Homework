#Given a real number, round it to the nearest whole.

number = float(input("input Number "))

number_2 = int(number * 10)

number_3 = str(number_2)

number_4 = number_3[-1]

result_1 = int(number)

result_2 = int(number) + 1

if int(number_4) < 5:
    print(result_1)
elif int(number_4) >= 5:
    print(result_2)