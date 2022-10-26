from aiogram.utils import executor
from create_bot import dp, bot
import os
async def on_startup(_):
	os.system('cls')
	print('Мы вышли в онлайн. Закройте это окно чтобы прекратить работу')
	#Добавление команд
from handlers import SimpleHandlers, SubHandlers, CreateEventHandler, ServiceHandlers, CreateFormHandler, RegInsideHandler, AcessHandlers, ShowEvents
try:
	ServiceHandlers.register_ServiceHandlers(dp)
	SimpleHandlers.register_SimpleHandlers(dp)
	SubHandlers.register_SubHandlers(dp)
	CreateEventHandler.register_CreatingEventHandler(dp)
	CreateFormHandler.register_CreateFormHandlers(dp)
	RegInsideHandler.register_RegInsideHandlers(dp)
	AcessHandlers.register_AcessHandlers(dp)
	ShowEvents.register_ShowEventsHandlers(dp)
	executor.start_polling(dp, skip_updates = True, on_startup = on_startup)
except Exception as e:
	print(e)