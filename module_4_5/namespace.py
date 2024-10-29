# Пространство имен
# Пространства имен часть II и области видимости
# import this
import math

# from math import *

a = 5
print(a)
print(math.sqrt(a))


# print(sqrt(a))

def square(x):
    global a
    a = x ** 2
    # print(globals())
    print(locals())
    return a


def square_alt():
    return a ** 2


b = square(2)
print(a)
print(b)
print(globals())
print(square_alt())


def square_one(x):
    d = x ** 2

    def even(x):
        # d = x * 2
        nonlocal d
        d = x / 2
        if x % 2 == 0:
            print('Even')
        else:
            print('Odd')

    even(x)
    return d

print(square_one(4))
print(square_one(3))