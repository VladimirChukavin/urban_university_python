# Практика 1.1

import random
import time
import threading
import queue


class Bulka(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            # time.sleep(random.randint(1, 2))
            time.sleep(3)
            if random.random() > 0.9:
                self.queue.put('Burning bulka')
            else:
                self.queue.put('Normal bulka')


class Kotleta(threading.Thread):
    def __init__(self, queue, count):
        super().__init__()
        self.queue = queue
        self.count = count

    def run(self):
        while self.count:
            print('Queue size:', self.queue.qsize())
            bulka = self.queue.get(timeout=3)
            if bulka == 'Normal bulka':
                time.sleep(random.randint(1, 2))
                self.count -= 1
            print(f'Bulka number: {self.count}')


queue = queue.Queue(maxsize=10)

t1 = Bulka(queue)
t2 = Kotleta(queue, 10)

t1.start()
t2.start()

t1.join()
t2.join()
