# Введение в функциональное программирование

def get_russian_names():
    # print(['Иван', 'Владимир', 'Света'])
    return ['Иван', 'Владимир', 'Света']


# get_russian_names()

# print(type(get_russian_names))
# print(get_russian_names.__name__)

# my_func = get_russian_names
# print('my_func:', my_func())
# print(my_func.__name__)


def get_british_names():
    return ['John', 'Dan', 'Lane']


name_getters = [get_russian_names, get_british_names]

for name_getter in name_getters:
    print(name_getter())


def adder(args):
    res = 0
    for arg in args:
        res += arg
    return res


def multiplier(args):
    res = 1
    for arg in args:
        res *= arg
    return res


def process_numbers(numbers, function):
    result = function(numbers)
    print(f'Result: {result}')


my_numbers = [4, 1, 2, 8, 3, 4, 1, 6, 5]

process_numbers(numbers=my_numbers, function=adder)
process_numbers(numbers=my_numbers, function=multiplier)


def mul_by_2(x):
    return x * 2


result = map(mul_by_2, my_numbers)
print(result)
print(list(result))


def is_odd(x):
    return x % 2


result = filter(is_odd, my_numbers)
print(result)
print(list(result))
