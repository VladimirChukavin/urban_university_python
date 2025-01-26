from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='Цена'),
            KeyboardButton(text='О нас'),
        ]
    ]
)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Средняя игра', callback_data='medium')],
        [InlineKeyboardButton(text='Большая игра', callback_data='large')],
        [InlineKeyboardButton(text='Очень большая игра', callback_data='extra-large')],
        [InlineKeyboardButton(text='Другие предложения', callback_data='other')],
    ]
)

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Купить!', url='https://www.ya.ru')],
    ]
)

other_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Спросить', callback_data='ask')]
    ]
)
