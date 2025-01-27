# Методы отправки сообщений

import os
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()

api = os.getenv('TELEGRAM_BOT_TOKEN')
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text=['Urban', 'asd'])
async def urban_message(message):
    print('Urban message')
    await message.answer('Urban message!')


@dp.message_handler(commands=['start'])
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Welcome to our bot!')


@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer(message.text.upper())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
