import asyncio
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.enums import ChatAction

router = Router()

@router.message(F.text == 'проверка роутера')
async def check_router(message: Message):
    await message.answer('все ок!')

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                       action=ChatAction.TYPING)
    await asyncio.sleep(2)
    await message.answer('Добро пожаловать!')

@router.message(F.text == 'Привет!')
async def hello(message: Message):
    await message.reply('Как дела?')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Пока что бот не умеет нчиего!')

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