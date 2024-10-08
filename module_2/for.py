# Цикл for

for i in 1, 2, 3, 4, 5:
    print(i)

for i in 'hello':
    print(i)

list_ = ['one', 'two', 'three', 'four']
for i in list_:
    print(i)

for i in list_:
    if i == 'three':
        list_.remove(i)

print(list_)

for i in range(5):
    print(i)

for i in range(len(list_)):
    print(list_[i])

for i in range(len(list_)):
    list_[i] = list_[i] + ';-)'

print(list_)

numbers = [2, 9, 3, 7, 1, 0]
summ = 0
for i in numbers:
    summ += i

print(summ)

for i in range(1, 11):
    for j in range(1, 10):
        print(f'{i} * {j} = {i * j}')

dict_ = {'a': 1, 'b': 2, 'c': 3}
for i in dict_:
    print(i, dict_[i])

for i in dict_.keys():
    print(i)

for i in dict_.values():
    print(i)

for key, value in dict_.items():
    print(key, value)

for i in range(2, 2):
    print('test', i)
