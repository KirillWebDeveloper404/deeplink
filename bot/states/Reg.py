from aiogram.dispatcher.filters.state import State, StatesGroup


class Reg(StatesGroup):
    name = State()
    phone = State()