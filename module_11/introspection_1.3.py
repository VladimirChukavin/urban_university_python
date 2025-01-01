# Интроспекция. 1.3

import sys
from pprint import pprint

pprint(dir(sys))

# путь к интерпретатору Python
print(sys.executable)

# тип операционной системы
print(sys.platform)

# текущая версия Python
print(sys.version)
print(sys.version_info)


def func(x):
    if sys.version.split(' ')[0] == '3.12.6':
        return x + 10
    else:
        raise Exception('Version denied')


try:
    print(func(5))
except Exception as e:
    print(e)

# параметры в командной строке
print(sys.argv)

pprint(sys.path)

# все модули загруженные в проекте
pprint(sys.modules)

# встроенные объекты в интерпретатор
print(__builtins__)
pprint(dir(__builtins__))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# sys.setrecursionlimit(5000)
# sys.set_int_max_str_digits(6000)
# print(factorial(2000))
print(sys.getsizeof(factorial))