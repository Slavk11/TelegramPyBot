from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог'),
    KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Контакты')]
],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт ниже'
)

inline_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог', url='https://telegram.org'),
    InlineKeyboardButton(text='Корзина', url='https://telegram.org')],
    [InlineKeyboardButton(text='Контакты', url='https://telegram.org')]
])