# Интроспекция. 1.1

# Интроспекция - это способность объекта во время выполнения получить тип, доступные атрибуты
# и методы, а также другую информацию, необходимую для выполнения дополнительных операций с объектом.

import requests
from pprint import pprint

# help(requests)

print(requests.__name__)

some_string = 'test'
some_number = 243
some_list = [some_string, some_number]


def func():
    pass


class SomeClass:
    """
    Some class
    """
    pass


# print(some_string.__name__)
# print(some_number.__name__)
print(SomeClass.__dict__)
print(SomeClass.__name__)
print(SomeClass.__doc__)

print(type(some_number))
print(type(some_string))
print(type(requests))
print(type(func))
print(type(SomeClass))

print(type(some_number) is int)
print(type(some_number) is list)

pprint(dir(some_string))
pprint(dir(some_number))
pprint(dir(some_list))
pprint(dir(func))
pprint(dir(SomeClass))
pprint(dir(requests))
pprint(dir())
