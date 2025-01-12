# Логирование
import logging

import math


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        a / b
        logging.info(f'Succesful divide {a} / {b}')
        return a / b
    except ZeroDivisionError as err:
        logging.error(f'Cannot divide by zero', exc_info=True)
        return math.inf


def sqrt(a):
    try:
        math.sqrt(a)
        logging.info(f'Succesful square root of {a}')
        return math.sqrt(a)
    except:
        logging.error(f'Cannot calculate square root', exc_info=True)
        return None


def pow(a, b):
    return a ** b


if __name__ == '__main__':
    # logging.debug('debug')
    # logging.info('info')
    # logging.warning('warning')
    # logging.error('error')
    # logging.critical('critical')
    logging.basicConfig(level=logging.INFO, filemode='w', filename='module_12.log',
                        format='%(asctime)s | %(levelname)s | %(message)s')
    print(div(3, 5))
    print(div(3, 0))
    print(sqrt(9))
    print(sqrt(-4))
