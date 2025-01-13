# Домашнее задание по теме "Систематизация и пропуск тестов"

import unittest
from tests_12_3 import RunnerTest, TournamentTest

tournament_test_suite = unittest.TestSuite()

tournament_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
tournament_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner_test_suite = unittest.TextTestRunner(verbosity=2)
runner_test_suite.run(tournament_test_suite)
