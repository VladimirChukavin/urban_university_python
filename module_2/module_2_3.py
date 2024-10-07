# Домашняя работа по уроку "Стиль кода часть II. Цикл While."

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
start = 0

while start < len(my_list):
    if my_list[start] > 0:
        print(my_list[start])
    elif my_list[start] < 0:
        break
    start += 1
