# Декораторы 1.2

import time
import sys


def func_gen_dec(precision):
    def dec(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            elapsed = round(end - start, precision)
            print(f'Function worked {elapsed} seconds')
            return result

        return wrapper

    return dec


def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))


sys.set_int_max_str_digits(10 ** 5)

time_track_precision_6 = func_gen_dec(5)
digits = time_track_precision_6(digits)
result = digits(3141, 5926, 2718, 2818)
print(result)

print('-' * 40)


@func_gen_dec(10)
def digits(*args):
    total = 1
    for number in args:
        total *= number ** 4000
    return len(str(total))


result = digits(3141, 5926, 2718, 2818)
print(result)
