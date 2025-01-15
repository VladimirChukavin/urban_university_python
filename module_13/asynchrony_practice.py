# Асинхронность на практике

import time
import asyncio

async def get_temp():
    await asyncio.sleep(2)
    print('First indication')
    print('25 C')


async def get_press():
    await asyncio.sleep(4)
    print('Second indication')
    print('101 kPa')


async def main():
    print('Start')
    task1 = asyncio.create_task(get_temp())
    task2 = asyncio.create_task(get_press())
    await task1
    await task2
    print('Finish')


start = time.time()
asyncio.run(main())
finish = time.time()

print(f'Working time: {round(finish - start, 2)} seconds')
