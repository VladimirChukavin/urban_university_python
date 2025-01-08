# Простые Юнит-тесты
import unittest


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def add(a, b):
    return a ** 2 + b ** 2


class CalcTest(unittest.TestCase):
    def test_add(self):
        """
        Test add
        :return:
        """
        self.assertEqual(add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(sub(3, 2), 1)

    def test_mul(self):
        self.assertEqual(mul(3, 2), 6)

    def test_div(self):
        self.assertEqual(div(4, 2), 2)


if __name__ == '__main__':
    unittest.main()
