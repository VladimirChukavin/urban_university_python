# Инлайн клавиатуры

import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv()

api = os.getenv('TELEGRAM_BOT_TOKEN')
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup()
button = InlineKeyboardButton(text='Информация', callback_data='info')
kb.add(button)

start_menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text='Info')],
        [
            KeyboardButton(text='Shop'),
            KeyboardButton(text='Donate')
        ]
    ]
)


@dp.message_handler(commands=['start'])
async def start(message):
    # await message.answer('Рады вас видеть', reply_markup=kb)
    await message.answer('Рады вас видеть', reply_markup=start_menu)


# @dp.callback_query_handler(text='info')
# async def info(cb):
#     await cb.message.answer('Информация о боте')
#     await cb.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
