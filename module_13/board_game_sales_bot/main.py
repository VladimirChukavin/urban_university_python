# Бот продажи настольных игр. 1.1
# Бот продажи настольных игр. 1.2

import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import API
from keyboards import start_kb, catalog_kb, buy_kb, other_kb
import texts

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(texts.start, reply_markup=start_kb)


@dp.message_handler(text='О нас')
async def info(message):
    await message.answer(texts.about, reply_markup=start_kb)


@dp.message_handler(text='Цена')
async def price(message):
    await message.answer('Что вас интересует?', reply_markup=catalog_kb)


@dp.callback_query_handler(text='medium')
async def buy_medium(call):
    await call.message.answer(texts.game.get('medium'), reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='large')
async def buy_large(call):
    await call.message.answer(texts.game.get('large'), reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='extra-large')
async def buy_extra_large(call):
    await call.message.answer(texts.game.get('extra-large'), reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='other')
async def buy_other(call):
    await call.message.answer(texts.other, reply_markup=other_kb)
    await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
