# Домашнее задание по теме "Доработка бота"
# Продолжение разработки телеграмм-бота из модуля 13

import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv()

api = os.getenv('TELEGRAM_BOT_TOKEN')
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

start_menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text='Рассчитать')],
        [KeyboardButton(text='Информация')],
        [KeyboardButton(text='Купить')],
    ]
)

inline_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')],
    ]
)

product_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Product1', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product2', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product3', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product4', callback_data='product_buying')],
    ]
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Start', reply_markup=start_menu)


@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=inline_menu)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in range(1, 5):
        with open(f'images/{i}.jpg', 'rb') as img:
            await message.answer_photo(img, f'Название: Product{i} | Описание: описание {i} | Цена: {i * 100}')
    await message.answer('Выберите продукт для покупки:', reply_markup=product_menu)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (лет) + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    if not message.text.isdigit():
        await message.answer('Введите свой возраст:')
    else:
        await state.update_data(age=message.text)
        await message.answer('Введите свой рост:')
        await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    if not message.text.isdigit():
        await message.answer('Введите свой рост:')
    else:
        await state.update_data(growth=message.text)
        await message.answer('Введите свой вес:')
        await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def set_calories(message, state):
    if not message.text.isdigit():
        await message.answer('Введите свой вес:')
    else:
        await state.update_data(weight=message.text)
        data = await state.get_data()
        number_calories = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
        await message.answer(f'Ваша норма калорий {number_calories}')
        await state.finish()


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
