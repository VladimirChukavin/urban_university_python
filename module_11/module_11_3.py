# Домашнее задание по теме "Интроспекция"

from pprint import pprint


class Calculator:
    """
    Class description
    """
    class_attribute = 'some attribute'

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Division by zero")


some_list = [1, 2, 3, 4, 5]


def introspection_info(obj):
    result = {
        'type': type(obj),
        'attributes and methods': obj.__dict__.keys() if hasattr(obj, '__dict__') else dir(obj),
        'name': obj.__name__ if hasattr(obj, '__name__') else 'No attribute',
        'module': obj.__module__ if hasattr(obj, '__module__') else 'No module',
        'doc': obj.__doc__,
        'callable': callable(obj),
        'id': id(obj),
    }
    return result


pprint(introspection_info(Calculator))
pprint(introspection_info(some_list))
