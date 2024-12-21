# Домашнее задание по теме "Многопроцессное программирование"

import multiprocessing
from datetime import datetime

filenames = [f'./file {number}.txt' for number in range(1, 5)]


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline().rstrip('\n')
            all_data.append(line)
            if not line:
                break


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        return (end - start).total_seconds()

    return wrapper


@measure_time
def measure_time_line_call():
    for filename in filenames:
        read_info(filename)


@measure_time
def measure_time_multi_process_call():
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)



if __name__ == '__main__':
    # print(measure_time_line_call())
    print(measure_time_multi_process_call())
