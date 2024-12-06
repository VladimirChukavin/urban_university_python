# Генераторные сборки
import time

my_numbers = [3, 2, 0, 9, 6, 4, 7, 6, 9, 8]

result = (x ** 10 for x in my_numbers)
print(result)

for element in result:
    print(element)

print('again')

for element in result:
    print(element)

start_time = time.time()
result = (x ** 3000 for x in my_numbers)
print(result)

for i in result:
    print(i)

finish_time = time.time()
print('Total time, millisecond:', (finish_time - start_time) * 1000)

list_1 = [1, 2, 3, 34, 83]
list_2 = [148, 2, 378, 34, 83]

ran = range(10, 30)
zp = zip(list_1, list_2)
mp = map(str, list_1)

print(ran, zp, mp)

print(list(ran))
print(list(zp))
print(list(mp))
