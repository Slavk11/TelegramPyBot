from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог'),
    KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Контакты')]
],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт ниже'
)

inline_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог', callback_data='catalog'),
    InlineKeyboardButton(text='Корзина', callback_data='cart'),],
    [InlineKeyboardButton(text='Контакты', callback_data='contacts')]
])

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Nike', callback_data='item_nike')],
    [InlineKeyboardButton(text='Adidas', callback_data='item_adidas')],
    [InlineKeyboardButton(text='Puma', callback_data='item_puma')],
    [InlineKeyboardButton(text='Reebok', callback_data='item_reebok')],
    [InlineKeyboardButton(text='Under Armour', callback_data='item_underarmour')],
    [InlineKeyboardButton(text='New Balance', callback_data='item_newbalance')],
    [InlineKeyboardButton(text='Asics', callback_data='item_asics')],
    [InlineKeyboardButton(text='Fila', callback_data='item_fila')],
    [InlineKeyboardButton(text='Skechers', callback_data='item_skechers')],
    [InlineKeyboardButton(text='Converse', callback_data='item_converse')]
])


back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='catalog')],
])

async def catalog_builder():
    brands = ['Nike', 'Adidas', 'Puma', 'Reebok', 'Under Armour', 'New Balance', 'Asics', 'Fila', 'Skechers', 'Converse']
    keyboard = InlineKeyboardBuilder()
    for brand in brands:
        keyboard.add(InlineKeyboardButton(text=brand, callback_data=f'item_{brand}'))
    return keyboard.adjust(2).as_markup()