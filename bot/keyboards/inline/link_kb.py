from calendar import c
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


link_kb = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton(text='Название', callback_data='name')).add(
    InlineKeyboardButton(text='Ozon', callback_data='ozon'),
    InlineKeyboardButton(text='WildBerries', callback_data='wb'),
    InlineKeyboardButton(text='AliExpress', callback_data='ali'),
    InlineKeyboardButton(text='Яндекс маркет', callback_data='ym')).add(
    InlineKeyboardButton(text='📁Сохранить', callback_data='main_menu'),
    InlineKeyboardButton(text='📤Опубликовать', callback_data='push')).add(
    InlineKeyboardButton(text='❌Удалить', callback_data='remove'),   
)