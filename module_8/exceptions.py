# Сложные моменты и исключения в стеке вызовов функции

def f1(number):
    return 3 / number


def f2():
    print('Welcome')
    result_f1 = f1(0)
    return result_f1


try:
    total = f2()
    print(total)
except ZeroDivisionError as exc:
    print(f'Error for f2: {exc}')


def f3():
    print('Welcome again')
    summ = 0
    for i in range(-2, 2):
        summ += f1(i)
        print(summ)
    return summ


try:
    total = f3()
except ZeroDivisionError as exc:
    print(f'Error for f3: {exc}')

def f4():
    summ = 0
    for i in range(-2, 2, 1):
        try:
            summ += f1(i)
            print(f'summ: {summ}')
        except ZeroDivisionError as exc:
            print(f'Error in f4: {exc}')
    return summ / 0

try:
    total = f4()
    print(f'Result for f4: {total}')
except ZeroDivisionError as exc:
    print(f'Error out f4: {exc}')