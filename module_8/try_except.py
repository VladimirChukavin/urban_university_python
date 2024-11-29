# Try и Except

try:
    i = 0
    print(4 / i)
    print('Done')
except ZeroDivisionError:
    print('Error, division by zero')

try:
    t = a + b
    t = 3 / 0
except (ZeroDivisionError, NameError):
    print('Error, division by zero or name error')

try:
    r = a + b
    r = 3 / 0
except ZeroDivisionError:
    print('Error, division by zero')
except NameError:
    print('Error, name error')

try:
    a = 3 / 0
except ZeroDivisionError as exc:
    print(f'Error, {exc}')

try:
    file = open('blabla.txt', 'r')
except OSError as exc:
    print(f'Error, {exc}, params: {exc.args}')

i = int(input('Enter your number: '))

try:
    result = 2 * (4 / i)
except ZeroDivisionError as exc:
    print(f'Error, {exc}')
else:
    print(f'2 * (4 / {i}) = {result}')
finally:
    print('Final example')
