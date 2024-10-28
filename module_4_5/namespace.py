# Пространство имен
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