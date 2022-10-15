import datetime

from aiogram import types, bot

from sql_methods import sql_events as sql


@bot.message_handler(commands=['Список актуальных мероприятий'])
async def ShowProcess(message):
    some_shit = sql.extract_event_date(datetime.datetime.now())
    for i in some_shit:
        await message.answer(i[0])
