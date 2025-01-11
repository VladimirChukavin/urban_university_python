# Пропуск тестов

import unittest
import simple_unit_tests
import tests.test_suite_2

calcTS = unittest.TestSuite()

calcTS.addTest(unittest.TestLoader().loadTestsFromTestCase(simple_unit_tests.CalcTest))
calcTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests.test_suite_2.NewCalcTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTS)
