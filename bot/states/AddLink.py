from aiogram.dispatcher.filters.state import State, StatesGroup


class AddLink(StatesGroup):
    add = State()
    name = State()
    link = State()