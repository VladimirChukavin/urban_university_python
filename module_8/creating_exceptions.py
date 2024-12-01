# Создание исключений

def greet_person(person_name):
    if person_name == 'John':
        raise Exception('Error, you not John')
    print(f'Hello, {person_name}')


# greet_person('Alex')
# greet_person('John')

try:
    raise NameError('Hello, John')
except NameError as exc:
    print(f'Exception type {type(exc)} and his params {exc.args}')
    # raise


class ProZero(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info


def func(a, b):
    if b == 0:
        raise ProZero('Division by zero', {'a': a, 'b': b})
    return a / b


# print(func(5, 2))
# print(func(5, 0))

try:
    result = func(10, 0)
    # result = func(10, 3)
    print(result)
except ProZero as exc:
    print(f'Exception info: {exc.message}')
    print(f'Additional info: {exc.extra_info}')
