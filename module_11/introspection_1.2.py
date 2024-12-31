# Интроспекция. 1.2

import requests
from pprint import pprint
import inspect

some_string = 'test'
some_number = 243
some_list = [some_string, some_number]


def func():
    pass


class SomeClass:
    """
    Some class
    """

    def __init__(self):
        self.attribute_1 = 6565

    def some_method(self, value):
        self.attribute_1 = value
        print(self.attribute_1)


some_object = SomeClass()
some_func = func

attr_name = 'atribute_2'

# print(some_object.__dir__())
# print(hasattr(some_object, 'attribute_1'))
# print(hasattr(some_object, attr_name))
#
# print(getattr(some_object, attr_name, 'Not exists attribute'))
# print(getattr(some_object, 'attribute_1'))
#
# for attr in dir(requests):
#     attr_obj = getattr(requests, attr)
#     print(attr, type(attr_obj))

# print(callable(attr_name))
# print(callable(some_func))
# print(callable(some_object))
# print(callable(some_object.attribute_1))
# print(callable(some_object.some_method))
#
# print(isinstance(some_object, SomeClass))
# print(isinstance(some_number, SomeClass))
# print(isinstance(some_number, int))
# print(isinstance(some_number, str))

print(inspect.ismodule(some_object))
print(inspect.ismodule(requests))
print(inspect.isclass(requests))
print(inspect.isfunction(requests))
print(inspect.isbuiltin(requests))

some_func_module = inspect.getmodule(some_func)
print(type(some_func_module), some_func_module)
