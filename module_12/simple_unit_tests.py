# Простые Юнит-тесты
import math
import unittest
import random


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


# def add(a, b):
#     return a ** 2 + b ** 2

def sqrt(a):
    return math.sqrt(a)


def pow(a, b):
    return a ** b


class CalcTest(unittest.TestCase):
    @unittest.skip('Fail test')
    def test_add(self):
        # """
        # Test add
        # :return:
        # """
        self.assertEqual(add(1, 2), 3)

    @unittest.skipIf(random.randint(0, 2), 'Wrong choice')
    def test_sub(self):
        self.assertEqual(sub(3, 2), 1)

    def test_mul(self):
        self.assertEqual(mul(3, 2), 6)

    def test_div(self):
        self.assertEqual(div(4, 2), 2)


if __name__ == '__main__':
    unittest.main()
