import asyncio
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.enums import ChatAction

import app.keyboards as kb

router = Router()

@router.message(F.text == 'проверка роутера')
async def check_router(message: Message):
    await message.answer('все ок!')

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                       action=ChatAction.TYPING)
    await asyncio.sleep(0.5)
    await message.answer('Добро пожаловать!',
                         reply_markup=kb.inline_main)

@router.message(F.text == 'Привет!')
async def hello(message: Message):
    await message.reply('Как дела?')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Пока что бот не умеет ничего!')

@router.message(F.photo)
async def photo_photo(message: Message):
    file_id = message.photo[-1].file_id
    await message.answer_photo(file_id, caption= f'id фотограции: {file_id}')

@router.message(F.video)
async def video_video(message: Message):
    file_id = message.video.file_id
    await message.answer_video(file_id, caption='help')

@router.message(F.sticker)
async def sticker_sticker(message: Message):
    file_id = message.sticker.file_id
    await message.answer_sticker(file_id)

@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer('Это всплывающее окно')
    await callback.message.edit_text('Выберите категорию', reply_markup=kb.catalog)

@router.callback_query(F.data.startswith('item_'))
async def item_handler(callback: CallbackQuery):
    await callback.answer('Вы выбрали товар')
    await callback.message.edit_text(f'Вы выбрали {callback.data}',
                                     reply_markup=kb.back)