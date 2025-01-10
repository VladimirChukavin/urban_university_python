# Систематизация тестов

import unittest
import module_12.simple_unit_tests


class NewCalcTest(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(module_12.simple_unit_tests.sqrt(4), 2)

    def test_pow(self):
        self.assertEqual(module_12.simple_unit_tests.pow(4, 2), 16)
