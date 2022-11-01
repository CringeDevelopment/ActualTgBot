import datetime

from aiogram import types, bot

from sql_methods import sql_events as sql


@bot.message_handler(commands=['Список актуальных мероприятий'])
async def ShowProcess(message):
    events = sql.extract_events()
    for event in events:
        await message.answer(event[1])
