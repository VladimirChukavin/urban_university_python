# Систематизация тестов

import unittest
import module_12.simple_unit_tests
import test_suite_2

calcTS = unittest.TestSuite()

# Устаревший метод
# calcTS.addTest(unittest.makeSuite(simple_unit_tests.CalcTest))

calcTS.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12.simple_unit_tests.CalcTest))
calcTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_suite_2.NewCalcTest))

# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(calcTS)
