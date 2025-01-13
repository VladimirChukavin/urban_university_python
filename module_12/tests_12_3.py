# Домашнее задание по теме "Систематизация и пропуск тестов"

import unittest
from runner import Runner
import runner_and_tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, '')
    def test_walk(self):
        runner = Runner('red')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, '')
    def test_run(self):
        runner = Runner('red')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, '')
    def test_challenge(self):
        runner_1 = Runner('red')
        runner_2 = Runner('blue')
        for i in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner_2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner_3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(value)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        tournament = runner_and_tournament.Tournament(90, self.runner_1, self.runner_3)
        self.assertEqual(self.runner_1.distance, 0)
        self.assertEqual(self.runner_2.distance, 0)
        all_results = tournament.start()
        self.all_results[self.test_tournament_1.__name__] = {i: all_results[i].name for i in all_results.keys()}
        self.assertTrue(all_results.get(max(all_results.keys())) == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        tournament = runner_and_tournament.Tournament(90, self.runner_2, self.runner_3)
        self.assertEqual(self.runner_2.distance, 0)
        self.assertEqual(self.runner_3.distance, 0)
        all_results = tournament.start()
        self.all_results[self.test_tournament_2.__name__] = {i: all_results[i].name for i in all_results.keys()}
        self.assertTrue(all_results.get(max(all_results.keys())) == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        tournament = runner_and_tournament.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.assertEqual(self.runner_1.distance, 0)
        self.assertEqual(self.runner_2.distance, 0)
        self.assertEqual(self.runner_3.distance, 0)
        all_results = tournament.start()
        self.all_results[self.test_tournament_3.__name__] = {i: all_results[i].name for i in all_results.keys()}
        self.assertTrue(all_results.get(max(all_results.keys())) == 'Ник')


if __name__ == '__main__':
    unittest.main()
