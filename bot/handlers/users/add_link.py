from aiogram import types
from aiogram.dispatcher.storage import FSMContext

from loader import dp
from sql import User, Link
from keyboards.inline import main_kb, link_kb
from states import AddLink
from .start import main_menu


@dp.message_handler(commands=['show_link'])
async def open_link(message: types.Message, state: FSMContext):
    link = Link.get(Link.id == int(message.text.split(' ')[1]))
    await show(message, state, link)


async def show(message: types.Message, state: FSMContext, link):
    text = f"Название: {link.name}\n"
    text += f"Озон: {link.ozon}\n" if link.ozon else ''
    text += f"WildBerries: {link.wb}\n" if link.wb else ''
    text += f"AliExpress: {link.ali}\n" if link.ali else ''
    text += f"Яндекс маркет: {link.ym}" if link.ym else ''

    await message.answer(text, reply_markup=link_kb, parse_mode='html')

    await state.update_data({
        'link': link
    })
    await AddLink.add.set()


@dp.callback_query_handler(text='remove', state=AddLink.add)
async def remove(c: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    link = data['link']
    link.delete_instance()

    await main_menu(c, state)


@dp.callback_query_handler(text='new_link')
@dp.callback_query_handler(text='name', state=AddLink.add)
async def new_link(c: types.CallbackQuery):
    await c.message.edit_text('Пришли название карточки')
    await AddLink.name.set()


@dp.message_handler(state=AddLink.name)
async def name(message: types.Message, state: FSMContext):
    try:
        data = await state.get_data()
        link = data['link']
        link.name = message.text
        link.save()

        await show(message, state, link)

    except Exception as e:
        user = User.get(User.tg_id == message.from_user.id)
        link = Link()
        link.name = message.text
        link.user = user
        link.save()

        await show(message, state, link)


@dp.callback_query_handler(state=AddLink.add)
async def link(c: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    data['type_link'] = c.data
    await state.update_data(data)

    await c.message.answer('Пришлите ссылку:')
    await AddLink.link.set()


@dp.message_handler(state=AddLink.link)
async def link_set(message: types.Message, state: FSMContext):
    data = await state.get_data()
    link = data['link']

    if data['type_link'] == 'ozon':
        link.ozon = message.text
    elif data['type_link'] == 'wb':
        link.wb = message.text
    elif data['type_link'] == 'ali':
        link.ali = message.text
    elif data['type_link'] == 'ym':
        link.ym = message.text

    link.save()

    await show(message, state, link)
