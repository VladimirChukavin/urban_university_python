# Обработка ошибок в потоках

import threading
import time


def some_function():
    time.sleep(3)
    raise Exception


def thread_function():
    try:
        some_function()
    except Exception as e:
        print('Error!!!')


t1 = threading.Thread(target=thread_function)
t2 = threading.Thread(target=thread_function)

# t1.start()
# t2.start()

# t1.join()
# t2.join()


def exception_hook(args):
    print(args.thread.is_alive())
    print(args.thread.name)


threading.excepthook = exception_hook

t3 = threading.Thread(target=some_function)
t4 = threading.Thread(target=some_function)

t3.start()
t4.start()

t3.join()
t4.join()
