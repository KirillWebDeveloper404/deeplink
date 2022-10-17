from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


main_kb = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text='🗒Мои ссылки', switch_inline_query_current_chat=''),
    InlineKeyboardButton(text='➕Добавить ссылку', callback_data='new_link'),
    InlineKeyboardButton(text='🏦Баланс', callback_data='cash')
)