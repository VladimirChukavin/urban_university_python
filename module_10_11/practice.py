# Многопроцессное программирование. Практика

import multiprocessing
from queue import Empty
from PIL import Image
from datetime import datetime

timeout = 5


def resize_image_on_queue(image_paths, queue):
    for image_path in image_paths:
        image = Image.open(image_path).resize((800, 600))
        queue.put((image_path, image))


def change_color_on_queue(queue):
    while True:
        try:
            image_path, image = queue.get(timeout=timeout)
        except Empty:
            break
        image = image.convert('L')
        image.save(image_path)


def resize_image_on_pipe(image_paths, pipe, stop_event):
    for image_path in image_paths:
        image = Image.open(image_path).resize((800, 600))
        image.save(image_path)
        pipe.send(image_path)
    stop_event.set()


def change_color_on_pipe(pipe, stop_event):
    while not stop_event.is_set():
        image_path = pipe.recv()
        image = Image.open(image_path).convert('L')
        image.save(image_path)


def test_queue():
    data = []
    queue = multiprocessing.Queue()

    for i in range(1, 21):
        data.append(f'./images/image-{i}.jpg')

    resize_process = multiprocessing.Process(target=resize_image_on_queue, args=(data, queue))
    change_color_process = multiprocessing.Process(target=change_color_on_queue, args=(queue,))

    start = datetime.now()
    resize_process.start()
    change_color_process.start()

    resize_process.join()
    change_color_process.join()
    end = datetime.now()
    print((end - start).total_seconds() - timeout)


def test_pipe():
    data = []
    conn1, conn2 = multiprocessing.Pipe()
    stop_event = multiprocessing.Event()

    for i in range(1, 21):
        data.append(f'./images/image-{i}.jpg')

    resize_process = multiprocessing.Process(target=resize_image_on_pipe, args=(data, conn1, stop_event))
    change_color_process = multiprocessing.Process(target=change_color_on_pipe, args=(conn2, stop_event))

    start = datetime.now()
    resize_process.start()
    change_color_process.start()

    resize_process.join()
    change_color_process.join()
    end = datetime.now()
    print((end - start).total_seconds())


if __name__ == '__main__':
    # test_queue()
    test_pipe()