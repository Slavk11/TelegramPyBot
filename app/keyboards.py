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
