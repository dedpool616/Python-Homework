salary_1 = int(input("input "))
salary_2 = int(input("input "))
salary_3 = int(input("input "))

meaning_max = 0
meaning_min = 0

if salary_1 > salary_2 > salary_3:
    meaning_max = salary_1
elif salary_2 > salary_1 > salary_3:
    meaning_max = salary_2
elif salary_3 > salary_2 > salary_1:
    meaning_max = salary_3

if salary_1 < salary_2 < salary_3:
    meaning_min = salary_1
elif salary_2 < salary_1 < salary_3:
    meaning_min = salary_2
elif salary_3 < salary_2 < salary_1:
    meaning_min = salary_3




difference = meaning_max - meaning_min

print(meaning_max)
print(meaning_min)

print(difference)
