# Стиль кода 1.2. Цикл While

while True:
    number = int(input('Enter a number: '))
    if number % 2 == 0:
        print('The number is even')
    else:
        print('The number is odd')
        break

print('End cycling')

# Домашняя работа по уроку "Стиль кода часть II. Цикл While."

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# my_list = [42, 69, 322, 13, 0, 99, 9, 8, 7, 5]
# my_list = [42, -69, 322, 13, 0, 99, 9, 8, 7, 5]
# print(len(my_list))
start = 0

while start < len(my_list):
    if my_list[start] > 0:
        print(my_list[start])
    elif my_list[start] < 0:
        break
    start += 1

# while start < len(my_list):
#     if my_list[start] == 0:
#         start += 1
#         continue
#     elif my_list[start] < 0:
#         break
#     else:
#         print(my_list[start])
#     start += 1
