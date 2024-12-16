# Проблемы многопоточного программирования, блокировки и обработка ошибок

import threading

counter = 0
lock = threading.Lock()


# print(lock.locked())


# def increment(name):
#     global counter
#     lock.acquire()
#     for i in range(1000):
#         counter += 1
#         print(name, counter)
#     lock.release()

def increment(name):
    global counter
    with lock:
        for i in range(1000):
            counter += 1
            print(name, counter)


# def decrement(name):
#     global counter
#     lock.acquire()
#     for i in range(1000):
#         counter -= 1
#         print(name, counter, lock.locked())
#     lock.release()

def decrement(name):
    global counter
    try:
        lock.acquire()
        for i in range(1000):
            counter -= 1
            print(name, counter, lock.locked())
    except Exception:
        pass
    finally:
        lock.release()


# def decrement(name):
#     global counter
#     with lock:
#         for i in range(1000):
#             counter -= 1
#             print(name, counter, lock.locked())


thread_1 = threading.Thread(target=increment, args=('Thread-1',))
thread_2 = threading.Thread(target=decrement, args=('Thread-2',))
thread_3 = threading.Thread(target=increment, args=('Thread-3',))
thread_4 = threading.Thread(target=decrement, args=('Thread-4',))
thread_1.start()
thread_3.start()
thread_2.start()
thread_4.start()
