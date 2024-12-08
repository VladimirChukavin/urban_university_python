# Итераторы

import sys
from itertools import repeat

ex_iterator = repeat('4', 100000)
print(ex_iterator)
# print(f'Iterators size - {sys.getsizeof(ex_iterator)}')

ex_str = '4' * 100000
# print(f'List size - {sys.getsizeof(ex_str)}')

print('-' * 40)


class Iter:
    def __init__(self):
        self.first = 'First element'
        self.second = 'Second element'
        self.third = 'Third element'
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i == 1:
            return self.first
        if self.i == 2:
            return self.second
        if self.i == 3:
            return self.third
        if self.i == 4:
            return 'Final count'
        raise StopIteration()


obj = Iter()
# print(obj)
# for value in obj:
#     print(value)

try:
    while True:
        value = obj.__next__()
        print(value)
except StopIteration:
    pass

print('-' * 40)


def fibonacci(n):
    result = []
    a, b = 0, 1

    for _ in range(n):
        result.append(b)
        a, b = b, a + b

    return result


# for value in fibonacci(100):
#     print(value)

print('-' * 40)


class Fibonacci:
    def __init__(self, n):
        self.i, self.a, self.b, self.n = 0, 0, 1, n

    def __iter__(self):
        self.i, self.a, self.b = 0, 0, 1
        return self

    def __next__(self):
        self.i += 1
        if self.i > 1:
            if self.i > self.n:
                raise StopIteration()
            self.a, self.b = self.b, self.a + self.b
        return self.a

fib_iterator = Fibonacci(20)
print(fib_iterator)
for value in fib_iterator:
    print(value)
