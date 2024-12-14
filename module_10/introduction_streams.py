# Введение в потоки

import threading
import time

print(threading.current_thread())
print(threading.current_thread().name)
print(threading.enumerate())


def func_one():
    for i in range(10):
        time.sleep(0.5)
        print(i, threading.current_thread())


def func_two(x):
    for i in range(10):
        time.sleep(x)
        print(i, threading.current_thread())
        # print(threading.current_thread().is_alive())


thread = threading.Thread(target=func_two, args=(1, ), daemon=True)
thread.start()
# thread.join()
print(thread.is_alive())

func_one()

print(threading.current_thread())
print(threading.enumerate())
