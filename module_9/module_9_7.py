# Домашнее задание по теме "Декораторы"
import math


def is_prime(func):
    def check_prime(num):
        if num == 2 or num == 3:
            return True

        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False

        return True

    def wrapper(*args, **kwargs):
        result_func = func(*args, **kwargs)
        definition = 'Простое' if check_prime(result_func) else 'Составное'
        print(definition)

        return result_func

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
