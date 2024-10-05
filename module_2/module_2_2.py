# Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."

first = int(input())
second = int(input())
third = int(input())

# вариант решения 1
if first == second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)

# вариант решения 2
set_numbers = {first, second, third}
length_set = len(set_numbers)

if length_set == 1:
    print(3)
elif length_set == 2:
    print(2)
elif length_set == 3:
    print(0)
