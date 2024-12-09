# Генераторы
import time


def func_generator(n):
    num = 0
    while num != n:
        yield num
        num += 1


obj = func_generator(10)
print(obj)

for i in obj:
    print(i)

print('-' * 40)


def fibonacci(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


fib_1 = fibonacci(10)
print(fib_1)

for val in fib_1:
    print(val)

fib_2 = fibonacci_gen(10)
print(fib_2)

for val in fib_2:
    print(val)

for i in fib_2:
    print(i)

print('-' * 40)


def fibonacci_gen_alt():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# for i in fibonacci_gen_alt():
#     print(i)
#     if i > 100 ** 6:
#         break

print('-' * 40)

start = time.time()


def read_large_file(filename):
    with open(filename, 'r') as file:
        for row in file:
            yield row.strip()


for line in read_large_file('voyna-i-mir.txt'):
    print(line)

finish = time.time()

print((finish - start) * 1000)
