# Домашнее задание по теме "Логирование"

import logging
import unittest
from rt_with_exceptions import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner('red', -5)
            logging.info('"test_walk" выполнен успешно')
            for i in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            runner = Runner(555)
            logging.info('"test_run" выполнен успешно')
            for i in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format='%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s')
    unittest.main()
