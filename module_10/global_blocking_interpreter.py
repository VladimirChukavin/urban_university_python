# Глобальная блокировка интерпретатора
import threading


def count_up(name, n):
    for i in range(n):
        print(name, i, sep=': ')


t1 = threading.Thread(target=count_up, args=('Thread-1', 50))
t2 = threading.Thread(target=count_up, args=('Thread-2', 50))

t1.start()
t2.start()

t1.join()
t2.join()
