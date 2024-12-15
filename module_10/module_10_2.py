# Домашнее задание по теме "Потоки на классах"

import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = 100
        self.battle_days = 0

    def battle(self):
        while self.enemies > 0:
            time.sleep(1)
            self.battle_days += 1
            self.enemies -= self.power
            print(f'{self.name} сражается {self.battle_days} день(дня)..., осталось {self.enemies} воинов.')

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.battle()
        print(f'{self.name} одержал победу спустя {self.battle_days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)
first_knight.start()
second_knight.start()
