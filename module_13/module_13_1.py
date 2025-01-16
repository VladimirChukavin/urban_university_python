# Домашнее задание по теме "Асинхронность на практике"
import asyncio


async def start_strongman(name, power):
    number_balls = 5
    print(f'Силач {name} начал соревнования.')

    for num_ball in range(1, number_balls + 1):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {num_ball} шар.')

    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Pasha', 3))
    task_2 = asyncio.create_task(start_strongman('Denis', 4))
    task_3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task_1
    await task_2
    await task_3


asyncio.run(start_tournament())
