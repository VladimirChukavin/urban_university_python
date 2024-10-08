# Функции в Python. Функция с параметром. Документирование функции
import random


def say_hello():
    print('Hello World')


say_hello()
say_hello()
say_hello()


def welcome(name):
    print('Welcome ' + name)


welcome('John')
welcome('Alex')


def lottery():
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    winner = random.choice(tickets)
    return winner


print(lottery())


def bingo(one, two):
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    winner1 = random.choice(tickets)
    tickets.remove(winner1)
    winner2 = random.choice(tickets)
    print(one, two)
    return winner1, winner2


win1, win2 = bingo('one', 'two')
print(win1, win2)


def jackpot(*args, **kwargs):
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    winner1 = random.choice(tickets)
    tickets.remove(winner1)
    winner2 = random.choice(tickets)
    print(*args)
    return winner1, winner2


win1, win2 = jackpot('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
print(win1, win2)


def test(a=2, b=True):
    print('default params:', a, b)


test()
test([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
test(*[1, 2])
