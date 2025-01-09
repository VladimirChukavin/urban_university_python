# Методы Юнит-тестирования

import unittest
import idea_unit_testing


class CalcTest(unittest.TestCase):
    def setUp(self):
        print('setup')

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    def tearDown(self):
        print('tearDown')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    # def test_add(self):
    #     """
    #     Test for add function
    #     :return:
    #     """
    #     self.assertEqual(idea_unit_testing.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(idea_unit_testing.sub(3, 2), 1)

    def test_mul(self):
        self.assertEqual(idea_unit_testing.mul(3, 2), 6)

    def test_div(self):
        self.assertEqual(idea_unit_testing.div(4, 2), 2)

    def test_test(self):
        self.assertIn('a', 'abc')
        # self.assertAlmostEqual(1.546838484638, 1.54683)


if __name__ == '__main__':
    unittest.main()
