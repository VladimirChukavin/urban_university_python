# Потоки на классах

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name, counter, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter
        self.delay = delay

    def timer(self, name, counter, delay):
        while counter:
            time.sleep(delay)
            print(f'{name}: {time.ctime(time.time())}')
            counter -= 1

    def run(self):
        print(f'Thread {self.name} started')
        self.timer(self.name, self.counter, self.delay)
        print(f'Thread {self.name} stopped')


thread_one = MyThread('Thread one', 5, 1)
thread_two = MyThread('Thread two', 3, 0.5)
thread_one.start()
thread_two.start()
