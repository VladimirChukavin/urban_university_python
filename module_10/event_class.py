# Класс Event

from threading import Thread, Event
import time


def worker_1():
    print('First worker run task')
    event.wait()
    print('First worker executing task')
    time.sleep(5)
    print('First worker finished task')


def worker_2():
    print('Second worker run task')
    time.sleep(10)
    print('Second worker finished task')
    event.set()
    event.clear()
    print(event.is_set())


event = Event()

thread1 = Thread(target=worker_1)
thread2 = Thread(target=worker_2)
thread1.start()
thread2.start()

# print(event.is_set())
# print(event.set())
# print(event.is_set())
event.wait(timeout=3)
# print(event.is_set())
