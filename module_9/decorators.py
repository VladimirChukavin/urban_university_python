# Декораторы
import time
import sys


def null_decorator(func):
    return func


def greet():
    return 'Hello World'


greet = null_decorator(greet)
print(greet())

print('-' * 40)


@null_decorator
def greet_alt():
    return 'Hello World Alt'


print(greet_alt())

print('-' * 40)


def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper


@uppercase
def greet_uppercase():
    return 'Hello World Uppercase'


print(greet_uppercase())

print('-' * 40)


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        finished_at = time.time()
        elapsed_time = round(finished_at - started_at, 4)
        print(f'Elapsed time: {elapsed_time} seconds')
        return result

    return surrogate


@time_track
def digits(*args):
    total = 1
    for num in args:
        total *= num ** 5000
    return len(str(total))


sys.set_int_max_str_digits(100000)

result = digits(3141, 5926, 2718, 2818)
print(result)
