from aiogram import types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent

from loader import dp
from sql import User, Link


@dp.inline_handler()
async def links(inline_query: types.InlineQuery):
    user = User.get(User.tg_id == inline_query.from_user.id)
    res = [
        InlineQueryResultArticle(
            id=el.id,
            title=el.name,
            description=f"Название: {el.name}\nОзон: {el.ozon}\nWildBerries: {el.wb}\nAliExpress: {el.ali}\nЯндекс маркет: {el.ym}",
            input_message_content=InputTextMessageContent(
                message_text=f'/show_link {el.id}',
                parse_mode="HTML"
            ) 
        )
        for el in Link.select().join(User).where(User.id == user.id)
    ]

    await inline_query.answer(results=res, is_personal=True, cache_time=0)