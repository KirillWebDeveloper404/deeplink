from aiogram import types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.storage import FSMContext

from loader import dp
from sql import User
from keyboards.inline import main_kb
from states import Reg


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    try:
        user = User.get(User.tg_id == message.from_user.id)
        await message.answer('Главное меню', reply_markup=main_kb)

    except User.DoesNotExist as e:
        await message.answer(f"Привет, для начала давай заполним анкету. \nКак тебя зовут?", parse_mode='html')
        await Reg.name.set()


@dp.callback_query_handler(text='main_menu', state='*')
async def main_menu(c: types.CallbackQuery, state: FSMContext):
    await state.finish()
    try:
        user = User.get(User.tg_id == c.from_user.id)
        await c.message.answer('Главное меню', reply_markup=main_kb)

    except User.DoesNotExist as e:
        await c.message.answer(f"Привет, для начала давай заполним анкету. /nКак тебя зовут?")
        await Reg.name.set()


@dp.message_handler(state=Reg.name)
async def setName(message: types.Message):
    user = User()
    user.tg_id = message.from_user.id
    user.name = message.text
    user.phone = 0
    user.save()

    await message.answer('Теперь пришли свой телефон', reply_markup=ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton('Отправить номер телефона', request_contact=True)
        ]
    ], resize_keyboard=True))

    await Reg.phone.set()


@dp.message_handler(content_types=['contact'], state=Reg.phone)
async def phone(message: types.Message, state: FSMContext):
    phone = message.contact['phone_number']

    try:
        user = User.get(User.tg_id == message.from_user.id)
        user.phone = phone
        user.save()

        await message.answer('Вы успешно прошли регистрацию!', reply_markup=ReplyKeyboardRemove())
        await message.answer('Главное меню', reply_markup=main_kb)
        await state.finish()
    
    except Exception as e:
        pass
