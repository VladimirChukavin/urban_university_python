# Списковые, словарные сборки

def by_3(x):
    return x * 3


def is_odd(x):
    return x % 2


my_numbers = [3, 2, 0, 9, 6, 4, 7, 6, 9, 8]
result = map(by_3, filter(is_odd, my_numbers))
print(list(result))

result = [x * 3 for x in my_numbers]
print(result)

result = [x * 3 for x in my_numbers if x % 2]
print(result)

my_numbers = ['a', 1, 3, 'c', 5, 8, 2, 'b']
result = [x if type(x) == str else x * 5 for x in my_numbers]
print(result)

one = [3, 2, 0, 9, 6]
two = [2, 3, 8, 0, 1]

result = [x * y for x in one for y in two]
print(result)

result = [x * y for x in one for y in two if x % 2]
print(result)

result = [x * y for x in one for y in two if x % 2 and y // 2]
print(result)

result = {x for x in my_numbers}
print(result)

result = {x: x ** 2 for x in one}
print(result)