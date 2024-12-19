# Очереди в потоках

from queue import Queue
import time
import threading


def getter(queue):
    while True:
        time.sleep(5)
        item = queue.get()
        print(threading.current_thread(), 'take element ', item)


q = Queue(maxsize=10)
# q.put(5)
# print(q.get(timeout=2))
# print('End of program')

thread_1 = threading.Thread(target=getter, args=(q,), daemon=True)
thread_1.start()

for i in range(10):
    time.sleep(2)
    q.put(i)
    print(threading.current_thread(), 'put in queue element', i)
