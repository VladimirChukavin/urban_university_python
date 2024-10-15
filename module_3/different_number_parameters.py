# Произвольное число параметров

def test_func(*params):
    # print(params)
    print('Type:', type(params))
    print('Arguments:', params)


test_func()
test_func(1, 2, 3, 4)


def summator(txt, *values, type='sum'):
    s = 0
    for i in values:
        s += i
    return f'{txt} {s} {type}'


print(summator('Sum of numbers:', 1, 2, 3, 4, type='summator'))


def info(one, *types, user='Fred', **values):
    print('Type:', type(values))
    print('Arguments:', values)
    for key, value in values.items():
        print(f'{key}: {value}')
    print(one, types, user)


info('Example', 1, 2, 3, user='Alex', name='John', age=23)


def my_sum(n, *args, text='Sum of numbers'):
    s = 0
    for i in range(len(args)):
        s += args[i] ** n
    print(f'{text}: {s}')


my_sum(1, 4, 8, 9)
my_sum(2, 4, 8, 9, text='Sum of squares')
my_sum(3, 4, 8, 9, text='Sum of cubes')
