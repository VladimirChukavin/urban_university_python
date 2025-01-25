# Машина состояний

import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

load_dotenv()

api = os.getenv('TELEGRAM_BOT_TOKEN')
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    address = State()


@dp.message_handler(text='Заказать')
async def buy(message):
    await message.answer('Отправьте нам свой адрес!')
    await UserState.address.set()


@dp.message_handler(state=UserState.address)
async def fsm_handler(message, state):
    await state.update_data(first=message.text)
    data = await state.get_data()
    await message.answer(f"Заказ будет отправлен на {data['first']}")
    print(data['first'])
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
