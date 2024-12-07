# Создание функций на лету
from pprint import pprint

my_func = lambda x: x + 10

print(my_func(x=42))
print(my_func(42))
print(type(my_func))
print(my_func.__name__)

my_numbers = [3, 2, 0, 9, 6, 4, 7, 6, 9, 8]
result = map(lambda x: x + 10, my_numbers)
print(list(result))

list_1 = [1, 2, 3, 34, 83]
list_2 = [148, 2, 378, 34, 83]

result = map(lambda x, y: x + y, list_1, list_2)
print(list(result))

test = lambda: 'test'
print(test)

print('-' * 40)


def get_multiplier(n):
    if n == 2:
        def multiplier(x):
            return x * 2
    elif n == 3:
        def multiplier(x):
            return x * 3
    else:
        raise Exception('Multiplier only 2 or 3!')
    return multiplier


by_2 = get_multiplier(2)
by_3 = get_multiplier(3)
# by_4 = get_multiplier(4)

result = map(by_2, my_numbers)
print(list(result))
result = map(by_3, my_numbers)
print(list(result))
# result = map(by_4, my_numbers)
# print(list(result))

print('-' * 40)


def get_multiplier_v2(n):
    def multiplier(x):
        return x * n

    return multiplier


by_5 = get_multiplier_v2(5)
print(by_5(x=42))

by_10 = get_multiplier_v2(10)
by_100 = get_multiplier_v2(100)

print(list(map(by_10, my_numbers)))
print(list(map(by_100, my_numbers)))

print('-' * 40)


def matrix(some_list):
    def multiply_column(x):
        res = []
        for element in some_list:
            res.append(x * element)
        return res

    return multiply_column


matrix_on_list = matrix(list_1)

result = map(matrix_on_list, list_2)
pprint(list(result))

list_1.extend([3, 5, 1])
result = map(matrix_on_list, list_2)
pprint(list(result))

print('-' * 40)


class Multiplier:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n * x


by_500 = Multiplier(500)
result = by_500(x=42)
print(result)

result = map(by_500, my_numbers)
print(list(result))
