# Домашнее задание по теме "Методы Юнит-тестирования"

import unittest
import runner_and_tournament


class TournamentTest(unittest.TestCase):
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

    def test_tournament_1(self):
        tournament = runner_and_tournament.Tournament(90, self.runner_1, self.runner_3)
        self.assertEqual(self.runner_1.distance, 0)
        self.assertEqual(self.runner_2.distance, 0)
        all_results = tournament.start()
        self.all_results[self.test_tournament_1.__name__] = {i: all_results[i].name for i in all_results.keys()}
        self.assertTrue(all_results.get(max(all_results.keys())) == 'Ник')

    def test_tournament_2(self):
        tournament = runner_and_tournament.Tournament(90, self.runner_2, self.runner_3)
        self.assertEqual(self.runner_2.distance, 0)
        self.assertEqual(self.runner_3.distance, 0)
        all_results = tournament.start()
        self.all_results[self.test_tournament_2.__name__] = {i: all_results[i].name for i in all_results.keys()}
        self.assertTrue(all_results.get(max(all_results.keys())) == 'Ник')

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
