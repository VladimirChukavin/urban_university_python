# Асинхронность. Понятия

import time
import asyncio


async def notification():
    time.sleep(5)
    print('Через 5 секунд')


async def main():
    task = asyncio.create_task(notification())
    print('Что-то происходит')
    print('Финал')


asyncio.run(main())
