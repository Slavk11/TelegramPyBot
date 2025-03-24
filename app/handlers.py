import asyncio
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.enums import ChatAction
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
from app.states import Reg

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

@router.message(Command('reg'))
async def cmd_reg(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Отправьте ваше имя')


@router.message(Reg.name)
async def cmd_reg(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.age)
    await message.answer('Введите ваш возраст')


@router.message(Reg.age)
async def cmd_reg_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Reg.phone)
    await message.answer('Отправьте ваше фото')


@router.message(Reg.phone, F.photo)
async def cmd_reg_photo(message: Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    data = await state.get_data()
    print(data)
    await message.answer_photo(photo=data['photo'], caption=f'Имя {data["name"]}\nВозраст {data["age"]}',)
    await state.clear()


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
    await callback.message.edit_text('Выберите категорию', reply_markup= await kb.catalog_builder())

@router.callback_query(F.data.startswith('item_'))
async def item_handler(callback: CallbackQuery):
    await callback.answer('Вы выбрали товар')
    await callback.message.edit_text(f'Вы выбрали {callback.data}',
                                     reply_markup=kb.back)

