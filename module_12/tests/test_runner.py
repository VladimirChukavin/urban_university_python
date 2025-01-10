# Систематизация тестов

import unittest
from test_suite_1 import calcTS

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTS)
